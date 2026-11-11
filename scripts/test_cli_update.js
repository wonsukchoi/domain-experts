#!/usr/bin/env node
// Regression test for `domain-experts update` (no network, no dependencies).
// Run: node scripts/test_cli_update.js
//
// 2026-11-12: `update` printed a failed role but left it out of the summary
// and exited 0, never refreshed installed jurisdiction overlays, and wrote
// SKILL.md before fetching the references, so a failure part-way left a new
// SKILL.md next to old references.
"use strict";

const assert = require("assert");
const fs = require("fs");
const os = require("os");
const path = require("path");

const cli = require("../bin/cli.js");

async function run() {
  const base = fs.mkdtempSync(path.join(os.tmpdir(), "de-update-"));

  // Role A: installed with its Korean overlay at old text.
  const a = path.join(base, "new-accounts-clerk");
  fs.mkdirSync(path.join(a, "references", "jurisdictions"), { recursive: true });
  fs.writeFileSync(path.join(a, "SKILL.md"), "OLD skill");
  fs.writeFileSync(path.join(a, "references", "jurisdictions", "kr.md"), "OLD kr overlay");

  // Role B: its reference download fails part-way.
  const b = path.join(base, "financial-manager");
  fs.mkdirSync(path.join(b, "references"), { recursive: true });
  fs.writeFileSync(path.join(b, "SKILL.md"), "OLD fm skill");

  const fetched = [];
  cli.deps.readRoleFile = async (_local, remote) => {
    fetched.push(remote);
    if (remote.includes("financial-manager") && remote.endsWith("/references/red-flags.md")) {
      throw new Error("simulated network failure");
    }
    return `NEW ${remote}`;
  };

  const logs = [];
  const origLog = console.log;
  console.log = (...args) => logs.push(args.join(" "));
  let result;
  try {
    process.exitCode = 0;
    result = await cli.cmdUpdate({ to: base });
  } finally {
    console.log = origLog;
  }
  const out = logs.join("\n");

  // (1) the failure is counted and the exit code says so
  assert.strictEqual(result.failed, 1, out);
  assert.match(out, /1 failed\./, out);
  assert.strictEqual(process.exitCode, 1, "update must exit non-zero when a role failed");

  // (2) the installed overlay is refreshed; no other country is added
  const kr = fs.readFileSync(path.join(a, "references", "jurisdictions", "kr.md"), "utf8");
  assert.match(kr, /^NEW roles\/new-accounts-clerk\/references\/jurisdictions\/kr\.md$/, kr);
  assert.deepStrictEqual(fs.readdirSync(path.join(a, "references", "jurisdictions")), ["kr.md"]);
  assert.strictEqual(result.updated, 1, out);

  // (3) a role that failed part-way is left exactly as it was
  assert.strictEqual(fs.readFileSync(path.join(b, "SKILL.md"), "utf8"), "OLD fm skill");
  assert.ok(fetched.some((p) => p.endsWith("financial-manager/references/red-flags.md")));

  fs.rmSync(base, { recursive: true, force: true });
  process.exitCode = 0;
  origLog("test_cli_update: ok");
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
