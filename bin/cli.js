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

function cmdAdd(slug, opts) {
  if (!slug) {
    console.error("Usage: domain-experts add <slug> [--to <dir>]");
    process.exit(1);
  }
  const roles = loadRoles();
  const role = roles.find((r) => r.slug === slug);
  if (!role) {
    console.error(`No role "${slug}" found. Run "domain-experts list" to see available roles.`);
    process.exit(1);
  }
  const targetDir = path.resolve(opts.to || path.join(".claude", "skills", slug));
  fs.mkdirSync(targetDir, { recursive: true });
  const targetFile = path.join(targetDir, "SKILL.md");
  fs.copyFileSync(role.file, targetFile);
  console.log(`Installed ${slug} -> ${targetFile}`);
}

function parseArgs(argv) {
  const [command, ...rest] = argv;
  const opts = {};
  const positional = [];
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === "--to") {
      opts.to = rest[i + 1];
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
  domain-experts add <slug> [--to dir]  Copy a role's SKILL.md into <dir> (default: .claude/skills/<slug>/)

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
