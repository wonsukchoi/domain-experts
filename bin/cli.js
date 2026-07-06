#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const ROLES_DIR = path.join(__dirname, "..", "roles");

function parseFrontmatter(text) {
  const m = text.match(/^---\n([\s\S]*?)\n---/);
  if (!m) return {};
  const block = m[1];
  const nameM = block.match(/^\s*name:\s*(.+)$/m);
  const descM = block.match(/^\s*description:\s*(.+)$/m);
  const catM = block.match(/^\s*category:\s*(\S+)/m);
  const maturityM = block.match(/^\s*maturity:\s*(\S+)/m);
  return {
    name: nameM ? nameM[1].trim() : "",
    description: descM ? descM[1].trim() : "",
    category: catM ? catM[1].trim() : "",
    maturity: maturityM ? maturityM[1].trim() : "",
  };
}

function loadRoles() {
  return fs
    .readdirSync(ROLES_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => {
      const slug = d.name;
      const file = path.join(ROLES_DIR, slug, "SKILL.md");
      if (!fs.existsSync(file)) return null;
      const fm = parseFrontmatter(fs.readFileSync(file, "utf8"));
      return { slug, file, ...fm };
    })
    .filter(Boolean)
    .sort((a, b) => a.slug.localeCompare(b.slug));
}

function printRoleLine(role) {
  const tag = role.category ? `[${role.category}]` : "";
  console.log(`  ${role.slug} ${tag}`);
  console.log(`    ${role.description}`);
}

function cmdList() {
  const roles = loadRoles();
  console.log(`${roles.length} roles available:\n`);
  roles.forEach(printRoleLine);
}

function cmdSearch(query) {
  if (!query) {
    console.error("Usage: domain-experts search <query>");
    process.exit(1);
  }
  const q = query.toLowerCase();
  const roles = loadRoles().filter(
    (r) =>
      r.slug.toLowerCase().includes(q) ||
      r.description.toLowerCase().includes(q) ||
      r.category.toLowerCase().includes(q)
  );
  if (roles.length === 0) {
    console.log(`No roles matching "${query}". Try "domain-experts list".`);
    return;
  }
  console.log(`${roles.length} match(es) for "${query}":\n`);
  roles.forEach(printRoleLine);
}

const STOPWORDS = new Set([
  "a", "an", "the", "for", "of", "to", "in", "on", "and", "or", "with",
  "my", "me", "i", "need", "want", "act", "as", "like", "help", "who",
  "job", "role", "expert", "someone", "person",
  "how", "much", "many", "do", "does", "did", "have", "has", "having",
  "had", "left", "should", "shall", "would", "could", "can", "will",
  "we", "us", "our", "you", "your", "let", "lets", "get", "give",
  "tell", "please", "this", "that", "these", "those", "is", "are",
  "was", "were", "be", "been", "being", "it", "its", "at", "by", "from",
  "about", "into", "over", "than", "then", "so", "if", "not", "no",
  "what", "when", "where", "which", "why", "just", "really", "some",
  "any", "all", "one", "out", "up", "down", "now",
]);

// Crude suffix stemming so plural/singular variants overlap (e.g. a query
// for "contract" matches a role description that only says "contracts").
// Not linguistically complete — just enough to close the most common gap.
function stem(word) {
  if (word.length <= 4) return word;
  if (word.endsWith("ies")) return word.slice(0, -3) + "y";
  if (/[sxz]es$|[cs]hes$/.test(word)) return word.slice(0, -2);
  if (word.endsWith("s") && !word.endsWith("ss")) return word.slice(0, -1);
  return word;
}

function tokenize(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, " ")
    .split(/\s+/)
    .filter((t) => t && !STOPWORDS.has(t))
    .map(stem);
}

// Inverse document frequency across the whole role library: a query word
// that only a couple of roles' descriptions use (e.g. "runway", "redline")
// is a much stronger signal than one that many roles happen to share
// (e.g. "financial", "risk") — without this, a common-but-irrelevant hit
// can outscore the one role that's actually specific to the query.
function buildIdf(roles) {
  const df = new Map();
  for (const role of roles) {
    const tokens = new Set([
      ...tokenize(role.slug.replace(/-/g, " ")),
      ...tokenize(role.description),
      ...tokenize(role.category),
    ]);
    for (const t of tokens) df.set(t, (df.get(t) || 0) + 1);
  }
  const n = roles.length;
  const idf = new Map();
  for (const [t, count] of df) idf.set(t, Math.log(1 + n / count));
  return idf;
}

// Scores a role against a query by IDF-weighted token overlap: slug and
// category hits count more than description hits (a query word matching
// the role's actual name is a stronger signal than it merely appearing
// somewhere in a long description), and every hit is scaled by how rare
// that word is across the whole role library, so a specific term (e.g.
// "runway") outweighs several generic ones (e.g. "financial", "manage").
function scoreRole(role, queryTokens, idf) {
  const slugTokens = new Set(tokenize(role.slug.replace(/-/g, " ")));
  const descTokens = new Set(tokenize(role.description));
  const catTokens = new Set(tokenize(role.category));
  let score = 0;
  for (const t of queryTokens) {
    const weight = idf.get(t) || 0;
    if (slugTokens.has(t)) score += 3 * weight;
    if (catTokens.has(t)) score += 2 * weight;
    if (descTokens.has(t)) score += 1 * weight;
  }
  return score;
}

function cmdMatch(query, opts) {
  if (!query) {
    console.error('Usage: domain-experts match "<job or task description>"');
    process.exit(1);
  }
  const queryTokens = tokenize(query);
  const roles = loadRoles();
  const idf = buildIdf(roles);
  const scored = roles
    .map((r) => ({ ...r, score: scoreRole(r, queryTokens, idf) }))
    .sort((a, b) => b.score - a.score);

  // A single description-only hit on a moderately rare word (idf ~2) scores
  // ~2, same as before IDF was added; require a bit more than that so one
  // coincidental word in common with many roles' descriptions can't alone
  // count as "confident".
  const MATCH_THRESHOLD = 2.5;
  const top = scored.filter((r) => r.score > 0.01).slice(0, 3);
  const best = top[0];
  const confident = best && best.score >= MATCH_THRESHOLD;

  if (opts.json) {
    console.log(
      JSON.stringify(
        {
          query,
          confident,
          best: best ? { slug: best.slug, score: best.score, file: best.file } : null,
          candidates: top.map((r) => ({ slug: r.slug, score: r.score, file: r.file })),
        },
        null,
        2
      )
    );
    return;
  }

  if (!confident) {
    console.log(`No confident role match for "${query}".`);
    if (top.length > 0) {
      console.log(`\nClosest (low-confidence) candidates:`);
      top.forEach((r) => printRoleLine(r));
    }
    console.log(
      `\nThis role isn't covered yet. Check ROADMAP.md for the closest O*NET occupation and ` +
        `consider opening a PR: https://github.com/wonsukchoi/domain-experts/blob/main/CONTRIBUTING.md`
    );
    return;
  }

  console.log(`Best match: ${best.slug} (score ${best.score})\n`);
  printRoleLine(best);
  console.log(`\nFile: ${best.file}`);
  if (top.length > 1) {
    console.log(`\nOther candidates:`);
    top.slice(1).forEach((r) => printRoleLine(r));
  }
}

function cmdAdd(slug, opts) {
  if (!slug) {
    console.error("Usage: domain-experts add <slug> [--to <dir>]");
    process.exit(1);
  }
  const roles = loadRoles();
  let role = roles.find((r) => r.slug === slug);
  if (!role) {
    // Meta-skills (e.g. the router) live in skills/, not roles/.
    const metaFile = path.join(__dirname, "..", "skills", slug, "SKILL.md");
    if (fs.existsSync(metaFile)) {
      role = { slug, file: metaFile };
    }
  }
  if (!role) {
    console.error(`No role "${slug}" found. Run "domain-experts list" to see available roles.`);
    process.exit(1);
  }
  const targetDir = path.resolve(opts.to || path.join(".claude", "skills", slug));
  fs.mkdirSync(targetDir, { recursive: true });
  const targetFile = path.join(targetDir, "SKILL.md");
  fs.copyFileSync(role.file, targetFile);
  let installed = "SKILL.md";
  const refsDir = path.join(path.dirname(role.file), "references");
  if (fs.existsSync(refsDir)) {
    fs.cpSync(refsDir, path.join(targetDir, "references"), { recursive: true });
    installed += ` + references/ (${fs.readdirSync(refsDir).length} files)`;
  }
  console.log(`Installed ${slug} (${installed}) -> ${targetDir}`);
}

function parseArgs(argv) {
  const [command, ...rest] = argv;
  const opts = {};
  const positional = [];
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === "--to") {
      opts.to = rest[i + 1];
      i++;
    } else if (rest[i] === "--json") {
      opts.json = true;
    } else {
      positional.push(rest[i]);
    }
  }
  return { command, positional, opts };
}

function printHelp() {
  console.log(`domain-experts - browse and install job-role SKILL.md files

Usage:
  domain-experts list                 List all available roles
  domain-experts search <query>       Search roles by slug/description/category
  domain-experts match "<job/task>" [--json]  Best-guess role match for a natural-language ask
  domain-experts add <slug> [--to dir]  Copy a role (SKILL.md + references/) into <dir> (default: .claude/skills/<slug>/)

Repo: https://github.com/wonsukchoi/domain-experts`);
}

function main() {
  const { command, positional, opts } = parseArgs(process.argv.slice(2));
  switch (command) {
    case "list":
      cmdList();
      break;
    case "search":
      cmdSearch(positional[0]);
      break;
    case "match":
      cmdMatch(positional.join(" "), opts);
      break;
    case "add":
      cmdAdd(positional[0], opts);
      break;
    case "help":
    case "--help":
    case "-h":
    case undefined:
      printHelp();
      break;
    default:
      console.error(`Unknown command: ${command}\n`);
      printHelp();
      process.exit(1);
  }
}

main();
