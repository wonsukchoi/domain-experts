# CONTEXT

## Current Task
Ran the full recurring chore sweep (depcheck/madge/cspell/ts-prune/knip/
jscpd) 2026-08-18. Also verified a low-CTR-high-impression scanner finding
as a false positive (position 12.9 aggregate hid a query-level "(other)"
artifact, same class already debunked here 2026-08-10).

## Key Decisions
- Only real fix: cspell flagged 82 words, all legitimate (HTML entities,
  var abbreviations, real acronyms, British spellings) — added 29 to the
  project dictionary rather than leaving cspell noisy going forward.
- ts-prune/madge: N/A, confirmed — no TypeScript in this repo, plain JS
  CLI + Python static-site generator.

## Next Steps
- ESCO-BACKLOG.md role-authoring work (252 of 260 roles remaining) is
  still paused separately — unrelated to this session, resume whenever.
