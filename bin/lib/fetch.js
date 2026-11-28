"use strict";

// Network helpers for the CLI: a GET with one deadline and redirect limit,
// role files read locally or from GitHub raw, and a small concurrency pool.
// Moved out of bin/cli.js on 2026-11-27 (no behaviour change).

const fs = require("fs");
const https = require("https");

const REMOTE_RAW_BASE = "https://raw.githubusercontent.com/wonsukchoi/domain-experts/main/";
const DOWNLOAD_TIMEOUT_MS = 20 * 1000;
const UPDATE_CHECK_TIMEOUT_MS = 3 * 1000;
const MAX_REDIRECTS = 5;

// GET a URL as text. Every request has a timeout: a network that drops
// packets (or needs a proxy, which Node's https ignores) otherwise leaves the
// socket waiting for the OS connect timeout, about 2 minutes, and the CLI
// cannot exit until then.
function fetchText(url, { timeoutMs = DOWNLOAD_TIMEOUT_MS, redirectsLeft = MAX_REDIRECTS } = {}) {
  return new Promise((resolve, reject) => {
    // One deadline for the whole request (DNS, connect, headers and body), so
    // a stall at any stage ends the request.
    let timer = null;
    const done = (fn, value) => {
      clearTimeout(timer);
      fn(value);
    };
    const req = https.get(url, { headers: { "User-Agent": "domain-experts-cli" } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        res.resume();
        if (redirectsLeft <= 0) {
          done(reject, new Error(`GET ${url} -> too many redirects`));
          return;
        }
        clearTimeout(timer);
        resolve(fetchText(new URL(res.headers.location, url).toString(), { timeoutMs, redirectsLeft: redirectsLeft - 1 }));
        return;
      }
      if (res.statusCode !== 200) {
        res.resume();
        done(reject, new Error(`GET ${url} -> HTTP ${res.statusCode}`));
        return;
      }
      let body = "";
      res.setEncoding("utf8");
      res.on("data", (chunk) => (body += chunk));
      res.on("end", () => done(resolve, body));
      res.on("error", (err) => done(reject, err));
    });
    timer = setTimeout(() => {
      const err = new Error(`GET ${url} -> timed out after ${Math.round(timeoutMs / 1000)}s`);
      req.destroy(err);
      reject(err);
    }, timeoutMs);
    req.on("error", (err) => done(reject, err));
  });
}

// Read a role file locally if bundled (monorepo dev), else fetch from
// GitHub raw (installed-via-npm case, where roles/ isn't shipped).
async function readRoleFile(localPath, repoRelativePath) {
  if (fs.existsSync(localPath)) return fs.readFileSync(localPath, "utf8");
  return fetchText(REMOTE_RAW_BASE + repoRelativePath);
}

// Runs `fn` over `items` with at most `limit` in flight at once — used so
// updating N installed roles doesn't serialize N GitHub-raw round trips.
async function mapWithConcurrency(items, limit, fn) {
  const results = new Array(items.length);
  let next = 0;
  async function worker() {
    while (next < items.length) {
      const i = next++;
      results[i] = await fn(items[i], i);
    }
  }
  const workers = Array.from({ length: Math.min(limit, items.length) }, () => worker());
  await Promise.all(workers);
  return results;
}

module.exports = { REMOTE_RAW_BASE, DOWNLOAD_TIMEOUT_MS, UPDATE_CHECK_TIMEOUT_MS, MAX_REDIRECTS, fetchText, readRoleFile, mapWithConcurrency };
