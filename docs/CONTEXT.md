# CONTEXT

## Current Task
2026-07-11 session: mass role-drafting via Workflow-tool orchestration across O*NET groups 19/21/25/27/29/31. 186 roles shipped, lint 0 errors, all pushed to main, npm published as v0.5.0. Full remaining scope + exact runbook (re-runnable script + payloads) in `docs/onet-fill-remaining.md` — read that file first when resuming.

## Key Decisions
- Switched batch mechanism from manual Agent forks (prior session) to the Workflow tool: one script call per O*NET group, draft phase (parallel agents, one per occupation) then ops phase (lint/regenerate/commit/push) as two workflow phases.
- Same skip conventions as before: "All Other" catch-alls and O*NET group 55 (Military) excluded; ~161 real gaps remain across groups 33/39/41/43/47/49/51/53.
- Runner script must live outside this repo's tracked tree (scratchpad only) — got accidentally committed once via a batch agent's `git add -A`, since fixed by scoping ops-step `git add` to explicit paths.

## Next Steps
- Resume via `docs/onet-fill-remaining.md`: smallest groups first (49, 43, 53) to sanity-check, then 33, 41, 39, 47, then 51 (63 roles, biggest).
- Known bug to fix: `roles/critical-care-nurse/` is mismapped to code 29-1141.01 (Acute Care Nurses) instead of its titled 29-1141.03 — needs a rename/split pass.
- Bump version + tag + push after each meaningful batch to keep npm in sync (see Release section in the runbook).
