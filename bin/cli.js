#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const https = require("https");

const ROLES_DIR = path.join(__dirname, "..", "roles");
const DATA_FILE = path.join(__dirname, "..", "data", "roles.json");
const REMOTE_RAW_BASE = "https://raw.githubusercontent.com/wonsukchoi/domain-experts/main/";

// Package ships only data/roles.json (the index), not the roles/ content
// itself — that stayed a 2.4M npm download otherwise. Role files are
// fetched from GitHub raw on demand in cmdAdd. When developing inside the
// monorepo, roles/ exists locally, so we still read straight from disk.
function loadRoles() {
  return JSON.parse(fs.readFileSync(DATA_FILE, "utf8"))
    .roles.map((r) => ({
      slug: r.slug,
      description: r.description,
      category: r.category,
      maturity: r.maturity,
      file: path.join(__dirname, "..", r.skill),
      skillPath: r.skill,
      referencePaths: (r.references || []).map((f) =>
        path.join(path.dirname(r.skill), "references", f)
      ),
    }))
    .sort((a, b) => a.slug.localeCompare(b.slug));
}

function fetchText(url) {
  return new Promise((resolve, reject) => {
    https
      .get(url, { headers: { "User-Agent": "domain-experts-cli" } }, (res) => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          resolve(fetchText(res.headers.location));
          return;
        }
        if (res.statusCode !== 200) {
          reject(new Error(`GET ${url} -> HTTP ${res.statusCode}`));
          res.resume();
          return;
        }
        let body = "";
        res.setEncoding("utf8");
        res.on("data", (chunk) => (body += chunk));
        res.on("end", () => resolve(body));
      })
      .on("error", reject);
  });
}

// Read a role file locally if bundled (monorepo dev), else fetch from
// GitHub raw (installed-via-npm case, where roles/ isn't shipped).
async function readRoleFile(localPath, repoRelativePath) {
  if (fs.existsSync(localPath)) return fs.readFileSync(localPath, "utf8");
  return fetchText(REMOTE_RAW_BASE + repoRelativePath);
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

async function cmdAdd(slug, opts) {
  if (!slug) {
    console.error("Usage: domain-experts add <slug> [--to <dir>]");
    process.exit(1);
  }
  const roles = loadRoles();
  let role = roles.find((r) => r.slug === slug);
  if (!role) {
    // Meta-skills (e.g. the router) live in skills/, not roles/ — small
    // enough that they still ship bundled in the package.
    const metaFile = path.join(__dirname, "..", "skills", slug, "SKILL.md");
    if (fs.existsSync(metaFile)) {
      role = { slug, file: metaFile, skillPath: `skills/${slug}/SKILL.md`, referencePaths: [] };
    }
  }
  if (!role) {
    console.error(`No role "${slug}" found. Run "domain-experts list" to see available roles.`);
    process.exit(1);
  }
  const targetDir = path.resolve(opts.to || path.join(".claude", "skills", slug));
  try {
    fs.mkdirSync(targetDir, { recursive: true });
    const skillText = await readRoleFile(role.file, role.skillPath);
    fs.writeFileSync(path.join(targetDir, "SKILL.md"), skillText);
    let installed = "SKILL.md";
    if (role.referencePaths.length > 0) {
      const refsDir = path.join(targetDir, "references");
      fs.mkdirSync(refsDir, { recursive: true });
      for (const refPath of role.referencePaths) {
        const localRefFile = path.join(__dirname, "..", refPath);
        const refText = await readRoleFile(localRefFile, refPath);
        fs.writeFileSync(path.join(refsDir, path.basename(refPath)), refText);
      }
      installed += ` + references/ (${role.referencePaths.length} files)`;
    }
    console.log(`Installed ${slug} (${installed}) -> ${targetDir}`);
  } catch (err) {
    if (err.code === "EACCES" || err.code === "EPERM") {
      console.error(`Permission denied writing to "${targetDir}". Check the path or pass a different --to.`);
    } else if (err.code === "ENOTDIR" || err.code === "EEXIST") {
      console.error(`"${targetDir}" already exists as a file, not a directory. Pass a different --to.`);
    } else {
      console.error(`Failed to install "${slug}": ${err.message}`);
    }
    process.exit(1);
  }
}

async function cmdCommand(opts) {
  const targetPath = path.resolve(
    opts.to || path.join(".claude", "commands", "domain-expert.md")
  );
  const localFile = path.join(__dirname, "..", "commands", "domain-expert.md");
  try {
    fs.mkdirSync(path.dirname(targetPath), { recursive: true });
    const text = await readRoleFile(localFile, "commands/domain-expert.md");
    fs.writeFileSync(targetPath, text);
    console.log(`Installed /domain-expert -> ${targetPath}`);
    console.log(`Start a new session (or run /doctor to reload commands), then try: /domain-expert <your task>`);
  } catch (err) {
    if (err.code === "EACCES" || err.code === "EPERM") {
      console.error(`Permission denied writing to "${targetPath}". Check the path or pass a different --to.`);
    } else {
      console.error(`Failed to install the domain-expert command: ${err.message}`);
    }
    process.exit(1);
  }
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
  domain-experts command [--to dir]   Install the /domain-expert slash command (default: .claude/commands/domain-expert.md)

Repo: https://github.com/wonsukchoi/domain-experts`);
}

async function main() {
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
      await cmdAdd(positional[0], opts);
      break;
    case "command":
      await cmdCommand(opts);
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
