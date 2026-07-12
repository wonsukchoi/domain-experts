# CONTEXT

## Current Task
2026-07-12 session: continued mass role-drafting via Workflow-tool orchestration, groups 49/43/53/33/41/39 all done (91 roles added, lint clean, each batch committed+pushed). 828/1016 drafted. Only groups 47 (36 roles) and 51 (63 roles, biggest) remain. Runbook: `docs/onet-fill-remaining.md`.

## Key Decisions
- Confirmed with user before each Workflow launch this session (multi-agent cost) — ask before firing, don't auto-chain.
- Small-batch lint fixes handled inline by the ops agent each time (banned phrases: "Best Practices" in bailiff citation, "utilize" substring in resident-director) — no roles dropped across 6 batches.
- Same skip conventions as before: "All Other" catch-alls and O*NET group 55 (Military) excluded.

## Next Steps
- Resume via `docs/onet-fill-remaining.md`: group 47 (36 roles) next, then 51 (63, biggest, do last).
- Known bug still open: `roles/critical-care-nurse/` mismapped to code 29-1141.01 (Acute Care Nurses) instead of its titled 29-1141.03 — needs rename/split pass.
- Haven't bumped npm version this session (still v0.5.0) — bump/tag/push once 47+51 land, per Release section in the runbook.
