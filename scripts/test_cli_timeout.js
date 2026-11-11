#!/usr/bin/env node
// Regression test: the CLI must not hang when the network never answers.
// Run: node scripts/test_cli_timeout.js   (no network, no dependencies)
//
// 2026-11-12: the npm update check at the end of every command used https.get
// with no timeout, so on a network that drops packets `list` printed its
// output and then waited ~2 minutes for the OS connect timeout.
"use strict";

const assert = require("assert");
const { spawnSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");

// A preload that replaces https.get with a request that never responds. Like a
// stalled socket it keeps the process alive (a 2-minute timer, the OS connect
// timeout) until the request is destroyed; without that handle Node would just
// exit and the test could not see a hang.
const STUB = `
const https = require("https");
const { EventEmitter } = require("events");
https.get = function () {
  const req = new EventEmitter();
  const socket = setTimeout(() => req.emit("error", new Error("connect ETIMEDOUT")), 120000);
  req.setTimeout = () => req;
  req.destroy = (err) => {
    clearTimeout(socket);
    if (err) setImmediate(() => req.emit("error", err));
    return req;
  };
  return req;
};
`;

async function run() {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "de-timeout-"));
  const stubFile = path.join(tmp, "hang.js");
  fs.writeFileSync(stubFile, STUB);
  const cli = path.join(__dirname, "..", "bin", "cli.js");

  // (1) `list` with an unreachable registry exits by itself, normally.
  const start = Date.now();
  const res = spawnSync(process.execPath, ["--require", stubFile, cli, "list"], {
    env: { ...process.env, TMPDIR: tmp, TEMP: tmp, TMP: tmp }, // no update-check cache
    encoding: "utf8",
    timeout: 10000,
    killSignal: "SIGKILL",
  });
  const elapsed = Date.now() - start;
  assert.ok(!res.error && res.signal === null, `CLI did not exit by itself (signal ${res.signal}, ${elapsed} ms)`);
  assert.strictEqual(res.status, 0, res.stderr);
  assert.ok(res.stdout.trim().length > 0, "list printed nothing");
  assert.ok(elapsed < 8000, `list took ${elapsed} ms`);

  // (2) the failed check is cached, so the next command does not wait again.
  const start2 = Date.now();
  const res2 = spawnSync(process.execPath, ["--require", stubFile, cli, "list"], {
    env: { ...process.env, TMPDIR: tmp, TEMP: tmp, TMP: tmp },
    encoding: "utf8",
    timeout: 10000,
    killSignal: "SIGKILL",
  });
  assert.strictEqual(res2.status, 0, res2.stderr);
  assert.ok(Date.now() - start2 < 2000, "second run waited on the registry again");

  // (3) a role download against the same stub fails with a clear timeout.
  require(stubFile);
  const { fetchText } = require(cli);
  await assert.rejects(
    fetchText("https://raw.githubusercontent.com/x/y/main/roles/a/SKILL.md", { timeoutMs: 300 }),
    /timed out after/
  );

  fs.rmSync(tmp, { recursive: true, force: true });
  console.log("test_cli_timeout: ok");
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
