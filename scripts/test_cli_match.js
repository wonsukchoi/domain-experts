#!/usr/bin/env node
// Plain Node checks (no dependencies) for the pure parts of bin/cli.js: the
// match tokenizer and ranking, argument parsing and the version compare.
// Written before bin/cli.js was split into modules, so they guard the split.
"use strict";

const assert = require("assert");
const cli = require("../bin/cli.js");

let failed = 0;
function check(name, fn) {
  try {
    fn();
    console.log(`ok   ${name}`);
  } catch (err) {
    failed++;
    console.error(`FAIL ${name}\n     ${err.message}`);
  }
}

check("stem folds common plurals", () => {
  assert.strictEqual(cli.stem("contracts"), "contract");
  assert.strictEqual(cli.stem("policies"), "policy");
  assert.strictEqual(cli.stem("taxes"), "tax");
  assert.strictEqual(cli.stem("branches"), "branch");
  assert.strictEqual(cli.stem("business"), "business"); // -ss kept
  assert.strictEqual(cli.stem("tax"), "tax"); // <= 4 letters kept
});

check("tokenize lowercases, drops stopwords and punctuation, stems", () => {
  assert.deepStrictEqual(cli.tokenize("I need a Contract Lawyer!"), ["contract", "lawyer"]);
  assert.deepStrictEqual(cli.tokenize("help with my taxes"), ["tax"]);
  assert.deepStrictEqual(cli.tokenize(""), []);
});

check("scoreRole ranks slug > category > description hits, scaled by rarity", () => {
  const roles = [
    { slug: "contract-lawyer", category: "Legal", description: "Reviews agreements and redlines clauses." },
    { slug: "financial-analyst", category: "Finance", description: "Models runway and reviews a contract budget." },
    { slug: "nurse", category: "Health", description: "Patient care." },
  ];
  const idf = cli.buildIdf(roles);
  const q = cli.tokenize("contract lawyer");
  const scores = roles.map((r) => cli.scoreRole(r, q, idf));
  assert.ok(scores[0] > scores[1], `slug match should win: ${scores}`);
  assert.ok(scores[1] > 0, "description hit should count");
  assert.strictEqual(scores[2], 0);
  const rare = cli.scoreRole(roles[1], cli.tokenize("runway"), idf);
  const common = cli.scoreRole(roles[1], cli.tokenize("reviews"), idf);
  assert.ok(rare > common, `rare word should outweigh a shared one: ${rare} vs ${common}`);
});

check("parseArgs reads flags and positionals", () => {
  assert.deepStrictEqual(cli.parseArgs(["add", "nurse", "--to", "x", "--global", "--json"]), {
    command: "add",
    positional: ["nurse"],
    opts: { to: "x", global: true, json: true },
  });
  assert.deepStrictEqual(cli.parseArgs(["match", "contract", "lawyer", "--country", "kr", "--tool", "codex"]), {
    command: "match",
    positional: ["contract", "lawyer"],
    opts: { country: "kr", tool: "codex" },
  });
  assert.deepStrictEqual(cli.parseArgs([]), { command: undefined, positional: [], opts: {} });
});

check("isNewerVersion compares major.minor.patch numerically", () => {
  assert.strictEqual(cli.isNewerVersion("0.5.10", "0.5.9"), true);
  assert.strictEqual(cli.isNewerVersion("0.5.1", "0.5.1"), false);
  assert.strictEqual(cli.isNewerVersion("0.4.9", "0.5.0"), false);
  assert.strictEqual(cli.isNewerVersion("1.0", "0.9.9"), true);
});

if (failed) {
  console.error(`\n${failed} check(s) failed`);
  process.exit(1);
}
console.log("\nall match/args/version checks passed");
