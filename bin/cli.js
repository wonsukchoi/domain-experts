#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const https = require("https");
const os = require("os");

const ROLES_DIR = path.join(__dirname, "..", "roles");
const DATA_FILE = path.join(__dirname, "..", "data", "roles.json");
const PKG = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "package.json"), "utf8"));
const UPDATE_CACHE_FILE = path.join(os.tmpdir(), "domain-experts-update-check.json");
const UPDATE_CHECK_INTERVAL_MS = 24 * 60 * 60 * 1000; // once per day
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
      jurisdictionPaths: (r.jurisdictions || [])
        .filter((c) => c !== "us")
        .map((c) =>
          path.join(path.dirname(r.skill), "references", "jurisdictions", `${c}.md`)
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

const GAP_LOG_FILE = path.join(__dirname, "..", "data", "gap-log.jsonl");

// Append-only signal for scripts/generate_roadmap.py's gap summary: every
// query nobody could confidently match is evidence for what to draft next
// (e.g. repeated narrow-niche queries under one parent role justify a leaf).
// Best-effort — a read-only global npm install directory shouldn't crash the CLI.
function logGap(query, candidates) {
  try {
    const entry = JSON.stringify({
      ts: new Date().toISOString(),
      query,
      candidates: candidates.map((c) => c.slug),
    }) + "\n";
    fs.appendFileSync(GAP_LOG_FILE, entry);
  } catch {
    /* best-effort */
  }
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

  if (!confident) logGap(query, top);

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

// Map '## Heading' -> body text, mirroring scripts/lint_roles.py's
// section_bodies so preview shows exactly what the linter validates.
function sectionBodies(text) {
  const parts = text.split(/^## +(.+?)\s*$/m);
  const out = {};
  for (let i = 1; i < parts.length - 1; i += 2) out[parts[i].trim()] = parts[i + 1];
  return out;
}

async function cmdPreview(slug) {
  if (!slug) {
    console.error("Usage: domain-experts preview <slug>");
    process.exit(1);
  }
  const roles = loadRoles();
  const role = findRoleOrMeta(slug, roles);
  if (!role) {
    console.error(`No role "${slug}" found. Run "domain-experts list" to see available roles.`);
    process.exit(1);
  }
  const text = await readRoleFile(role.file, role.skillPath);
  const body = text.split("---\n", 3).length >= 3 ? text.split("---\n").slice(2).join("---\n") : text;
  const sections = sectionBodies(body);

  console.log(`# ${slug}\n`);
  for (const name of ["Identity", "Worked example"]) {
    if (sections[name]) {
      console.log(`## ${name}`);
      console.log(sections[name].trim());
      console.log("");
    }
  }
  if (!sections["Identity"] && !sections["Worked example"]) {
    console.log("(legacy-format role — showing raw file)\n");
    console.log(body.trim());
  }
  console.log(`Full file: domain-experts add ${slug}`);
}

async function cmdAdd(slug, opts) {
  if (!slug) {
    console.error("Usage: domain-experts add <slug> [--to <dir>] [--country <iso2>]");
    process.exit(1);
  }
  const roles = loadRoles();
  // Meta-skills (e.g. the router) live in skills/, not roles/ — small
  // enough that they still ship bundled in the package.
  let role = findRoleOrMeta(slug, roles);
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
    const allJurisdictionPaths = role.jurisdictionPaths || [];
    let jurisdictionPaths = allJurisdictionPaths;
    if (opts.country) {
      const wanted = opts.country.toLowerCase();
      jurisdictionPaths = allJurisdictionPaths.filter(
        (p) => path.basename(p, ".md") === wanted
      );
      if (allJurisdictionPaths.length > 0 && jurisdictionPaths.length === 0) {
        console.error(
          `No "${opts.country}" jurisdiction overlay for "${slug}" — installing US baseline only. ` +
            `Available: ${allJurisdictionPaths.map((p) => path.basename(p, ".md")).join(", ")}`
        );
      }
    }
    if (jurisdictionPaths.length > 0) {
      const jurisDir = path.join(targetDir, "references", "jurisdictions");
      fs.mkdirSync(jurisDir, { recursive: true });
      for (const jPath of jurisdictionPaths) {
        const localJFile = path.join(__dirname, "..", jPath);
        const jText = await readRoleFile(localJFile, jPath);
        fs.writeFileSync(path.join(jurisDir, path.basename(jPath)), jText);
      }
      installed += ` + jurisdictions/ (${jurisdictionPaths.length} file${jurisdictionPaths.length > 1 ? "s" : ""})`;
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

function findRoleOrMeta(slug, roles) {
  let role = roles.find((r) => r.slug === slug);
  if (!role) {
    const metaFile = path.join(__dirname, "..", "skills", slug, "SKILL.md");
    if (fs.existsSync(metaFile)) {
      role = { slug, file: metaFile, skillPath: `skills/${slug}/SKILL.md`, referencePaths: [], jurisdictionPaths: [] };
    }
  }
  return role;
}

async function cmdInit(roleSlugs, opts) {
  console.log("Installing domain-expert router...");
  await cmdAdd("domain-expert-router", {});
  console.log("\nInstalling /domain-expert command...");
  await cmdCommand(opts);
  for (const slug of roleSlugs) {
    console.log(`\nInstalling role "${slug}"...`);
    await cmdAdd(slug, {});
  }
  console.log(
    `\nDone. Start a new session, then try: ${TOOLS[opts.tool || "claude"].usage}`
  );
}

async function cmdUpdate(opts) {
  const baseDir = path.resolve(opts.to || path.join(".claude", "skills"));
  if (!fs.existsSync(baseDir)) {
    console.error(`No installed skills found at "${baseDir}".`);
    process.exit(1);
  }
  const roles = loadRoles();
  const installedSlugs = fs
    .readdirSync(baseDir, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .filter((slug) => fs.existsSync(path.join(baseDir, slug, "SKILL.md")));

  if (installedSlugs.length === 0) {
    console.log(`No installed roles found in "${baseDir}".`);
    return;
  }

  let updated = 0;
  let unchanged = 0;
  let missing = 0;
  for (const slug of installedSlugs) {
    const role = findRoleOrMeta(slug, roles);
    if (!role) {
      console.log(`? ${slug}: no longer in the role index, skipping`);
      missing++;
      continue;
    }
    const targetDir = path.join(baseDir, slug);
    try {
      const remoteSkill = await readRoleFile(role.file, role.skillPath);
      const localSkillPath = path.join(targetDir, "SKILL.md");
      const localSkill = fs.existsSync(localSkillPath)
        ? fs.readFileSync(localSkillPath, "utf8")
        : null;
      let changed = remoteSkill !== localSkill;
      fs.writeFileSync(localSkillPath, remoteSkill);

      for (const refPath of role.referencePaths) {
        const localRefFile = path.join(__dirname, "..", refPath);
        const remoteRef = await readRoleFile(localRefFile, refPath);
        const refsDir = path.join(targetDir, "references");
        fs.mkdirSync(refsDir, { recursive: true });
        const localRefPath = path.join(refsDir, path.basename(refPath));
        const localRef = fs.existsSync(localRefPath)
          ? fs.readFileSync(localRefPath, "utf8")
          : null;
        if (remoteRef !== localRef) changed = true;
        fs.writeFileSync(localRefPath, remoteRef);
      }

      if (changed) {
        console.log(`* ${slug}: updated`);
        updated++;
      } else {
        console.log(`  ${slug}: up to date`);
        unchanged++;
      }
    } catch (err) {
      console.log(`! ${slug}: failed (${err.message})`);
    }
  }
  console.log(`\n${updated} updated, ${unchanged} up to date, ${missing} skipped.`);
}

// Each entry's projectPath/globalPath match that tool's *documented* custom
// command/prompt mechanism as of this writing — verified against each
// tool's own docs, not assumed from Claude Code's convention. Where a
// tool's placeholder-substitution behavior for user-typed arguments isn't
// documented (Cursor, Windsurf, Amp), the template avoids relying on one
// and just tells the agent to route "the task described in this message."
const TOOLS = {
  claude: {
    label: "Claude Code",
    template: "commands/domain-expert.md",
    projectPath: () => path.join(".claude", "commands", "domain-expert.md"),
    globalPath: () => path.join(os.homedir(), ".claude", "commands", "domain-expert.md"),
    usage: "/domain-expert <your task>",
  },
  codex: {
    label: "Codex CLI",
    // Codex only reads prompts from the user-level ~/.codex/prompts dir,
    // not a project-local one — project/global resolve the same here.
    // Note: OpenAI's docs mark this mechanism deprecated in favor of
    // "skills," but it's still functional as of this writing.
    template: "commands/domain-expert.codex.md",
    projectPath: () => path.join(os.homedir(), ".codex", "prompts", "domain-expert.md"),
    globalPath: () => path.join(os.homedir(), ".codex", "prompts", "domain-expert.md"),
    usage: "/domain-expert <your task> (or /prompts:domain-expert <your task>)",
  },
  gemini: {
    label: "Gemini CLI",
    template: "commands/domain-expert.gemini.toml",
    projectPath: () => path.join(".gemini", "commands", "domain-expert.toml"),
    globalPath: () => path.join(os.homedir(), ".gemini", "commands", "domain-expert.toml"),
    usage: "/domain-expert <your task>",
  },
  cursor: {
    label: "Cursor",
    template: "commands/domain-expert.generic.md",
    projectPath: () => path.join(".cursor", "commands", "domain-expert.md"),
    globalPath: () => path.join(os.homedir(), ".cursor", "commands", "domain-expert.md"),
    usage: "/domain-expert <your task>",
  },
  windsurf: {
    label: "Windsurf",
    template: "commands/domain-expert.generic.md",
    projectPath: () => path.join(".windsurf", "workflows", "domain-expert.md"),
    globalPath: () =>
      path.join(os.homedir(), ".codeium", "windsurf", "global_workflows", "domain-expert.md"),
    usage: "/domain-expert <your task>",
  },
  roo: {
    label: "Roo Code",
    template: "commands/domain-expert.roo.md",
    projectPath: () => path.join(".roo", "commands", "domain-expert.md"),
    globalPath: () => path.join(os.homedir(), ".roo", "commands", "domain-expert.md"),
    usage: "/domain-expert <your task>",
  },
  amp: {
    label: "Amp",
    // Amp only documents a fixed repo-root location, no separate global dir.
    template: "commands/domain-expert.generic.md",
    projectPath: () => path.join(".agents", "commands", "domain-expert.md"),
    globalPath: () => path.join(".agents", "commands", "domain-expert.md"),
    usage: "/domain-expert <your task>",
  },
};

async function cmdCommand(opts) {
  const toolId = opts.tool || "claude";
  const tool = TOOLS[toolId];
  if (!tool) {
    console.error(
      `Unknown --tool "${toolId}". Available: ${Object.keys(TOOLS).join(", ")}`
    );
    process.exit(1);
  }
  const defaultPath = opts.global ? tool.globalPath() : tool.projectPath();
  const targetPath = path.resolve(opts.to || defaultPath);
  const localFile = path.join(__dirname, "..", tool.template);
  try {
    fs.mkdirSync(path.dirname(targetPath), { recursive: true });
    const text = await readRoleFile(localFile, tool.template);
    fs.writeFileSync(targetPath, text);
    console.log(`Installed /domain-expert for ${tool.label} -> ${targetPath}`);
    console.log(`Start a new session, then try: ${tool.usage}`);
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
    } else if (rest[i] === "--tool") {
      opts.tool = rest[i + 1];
      i++;
    } else if (rest[i] === "--global") {
      opts.global = true;
    } else if (rest[i] === "--json") {
      opts.json = true;
    } else if (rest[i] === "--country") {
      opts.country = rest[i + 1];
      i++;
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
  domain-experts preview <slug>       Print a role's Identity + Worked example, no install
  domain-experts add <slug> [--to dir] [--country iso2]
                                       Copy a role (SKILL.md + references/) into <dir> (default: .claude/skills/<slug>/).
                                       --country installs only that jurisdiction overlay instead of all available ones.
  domain-experts command [--tool <id>] [--global] [--to path]
                                       Install the /domain-expert command/prompt for <id>
                                       (default: claude). --global installs to the tool's
                                       user-level directory instead of the project directory.
  domain-experts init [slug...] [--tool <id>] [--global]
                                       One-shot setup: router + /domain-expert command,
                                       plus any role slugs passed.
  domain-experts update [--to dir]    Re-fetch all installed roles (default: .claude/skills/)

  Supported --tool values: ${Object.keys(TOOLS).join(", ")}

Repo: https://github.com/wonsukchoi/domain-experts`);
}

function isNewerVersion(latest, current) {
  const a = latest.split(".").map(Number);
  const b = current.split(".").map(Number);
  for (let i = 0; i < 3; i++) {
    if ((a[i] || 0) > (b[i] || 0)) return true;
    if ((a[i] || 0) < (b[i] || 0)) return false;
  }
  return false;
}

// Fire-and-forget: checks npm registry for a newer published version at most
// once per day (cached in the OS temp dir) and prints a nudge to stderr so it
// never pollutes stdout/--json output. Any failure (offline, registry down,
// corrupt cache) is swallowed silently — this must never break a command.
async function checkForUpdate() {
  try {
    let cache = null;
    if (fs.existsSync(UPDATE_CACHE_FILE)) {
      cache = JSON.parse(fs.readFileSync(UPDATE_CACHE_FILE, "utf8"));
    }
    const fresh = cache && Date.now() - cache.checkedAt < UPDATE_CHECK_INTERVAL_MS;
    const latest = fresh
      ? cache.latest
      : JSON.parse(await fetchText("https://registry.npmjs.org/domain-experts/latest")).version;

    if (!fresh) {
      fs.writeFileSync(UPDATE_CACHE_FILE, JSON.stringify({ latest, checkedAt: Date.now() }));
    }
    if (latest && isNewerVersion(latest, PKG.version)) {
      console.error(
        `\n→ domain-experts v${latest} is available (you have v${PKG.version}). Run: npm i -g domain-experts@latest\n`
      );
    }
  } catch {
    // offline or registry unreachable — never fail the command over this
  }
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
    case "preview":
      await cmdPreview(positional[0]);
      break;
    case "add":
      await cmdAdd(positional[0], opts);
      break;
    case "command":
      await cmdCommand(opts);
      break;
    case "init":
      await cmdInit(positional, opts);
      break;
    case "update":
      await cmdUpdate(opts);
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

  if (!opts.json && command !== "help" && command !== "--help" && command !== "-h") {
    await checkForUpdate();
  }
}

main();
