"use strict";

// Query matching for `domain-experts match` and the roadmap gap log:
// stopwords, plural stemming, IDF weights and role scoring. Moved out of
// bin/cli.js on 2026-11-27 (no behaviour change; scripts/test_cli_match.js).

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

module.exports = { STOPWORDS, stem, tokenize, buildIdf, scoreRole };
