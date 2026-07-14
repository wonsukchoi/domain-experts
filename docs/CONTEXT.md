# CONTEXT

## Current Task
2026-07-14 session: ran group 47 (36 Construction/Extraction roles) via Workflow-tool orchestration — all 36 added, 0 skipped, lint clean, committed+pushed to main (25d70b5). 854/1016 drafted (≈84.1%). Only group 51 (63 roles, Production, biggest) remains. Runbook: `docs/onet-fill-remaining.md`.

## Key Decisions
- Confirmed direct-to-main push convention with user (matches AGENTS.md/prior batches) despite session's default branch instructions pointing elsewhere — keep pushing role batches straight to main.
- Left commit 25d70b5's author identity as-is (user declined a rewrite of already-shared main history); set git config (user.email noreply@anthropic.com, user.name Claude) so future commits are correctly attributed.
- Same skip conventions as before: "All Other" catch-alls and O*NET group 55 (Military) excluded.

## Next Steps
- Resume via `docs/onet-fill-remaining.md`: group 51 (63 roles, Production, do last) is the only group left.
- Known bug still open: `roles/critical-care-nurse/` mismapped to code 29-1141.01 (Acute Care Nurses) instead of its titled 29-1141.03 — needs rename/split pass.
- Haven't bumped npm version this session (still v0.5.0) — bump/tag/push once group 51 lands, per Release section in the runbook.
