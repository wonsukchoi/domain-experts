# CONTEXT

## Current Task
2026-07-15 session: finished remaining O*NET coverage — group 51 (last 2 roles), then 9 education/healthcare roles (teachers + special-ed grade bands + nurses) via parallel subagents. 927/1016 drafted. Repo cleaned up: closed 7 stale PRs, deleted 7 stale branches (only `main` remains).

## Key Decisions
- 927/1016 (91.2%) declared effective 100% coverage — remaining 89 = 73 "All Other" catch-alls + 16 group-55 military, both out of scope (no real practitioner behind a catch-all; military excluded by convention). Documented in both `README.md` and auto-generated in `ROADMAP.md` (see `generate_roadmap.py`'s progress-note block) so it self-maintains.
- Parallel subagents draft files only (no git ops) — coordinator sequentially lints/commits/pushes to avoid concurrent-push races. Worked cleanly across 9 roles.
- Fixed the known `critical-care-nurse` mismapping bug (was on 29-1141.01) — moved to correct code 29-1141.03, which surfaced 29-1141.01 (Acute Care Nurses) as newly uncovered; drafted that too.
- Closed PRs #27-33 and deleted their branches — all duplicated content already merged directly to main this session; merging would have clobbered/conflicted.

## Next Steps
- No open role-drafting work remains in scope. If military group 55 (16 roles) is ever wanted, same recipe applies.
- Haven't bumped npm version this session (still v0.5.0) — bump/tag/push per Release section in `AGENTS.md` if a release is desired.
- `docs/onet-fill-remaining.md` runbook is now fully executed and can be retired/archived.
