# CONTEXT

## Current Task
2026-07-15 session (later): added ESCO taxonomy diff + curated 260-role expansion backlog, then started working the spec-2 upgrade queue — upgraded `accountant-controller` (rubric 17/18) and `administrative-services-manager` (rubric 16/18), both also cleared off needs-refresh. Paused; `advertising-promotions-manager` queued as next (task #1).

## Key Decisions
- Fetched all 2,942 ESCO occupations via the public API, diffed against 937 roles, curated the 1,994 unmatched candidates with 8 parallel judge agents: 702 dup / 1,032 niche / 260 genuinely new. Shipped as `data/esco_occupations.tsv` + `ESCO-BACKLOG.md`, linked from `ROADMAP.md`'s "Beyond O*NET" section.
- Spec-2 upgrades follow CONTRIBUTING.md's upgrade recipe exactly: restructure to 10-section template, add references/ trio, worked example needs real reconciling arithmetic + quoted deliverable, self-score against AUTHORING.md rubric (≥14/18, no zero), lint 0 errors before commit.
- Picked upgrade-queue entries that were also on the needs-refresh list (double win) — accountant-controller was 5/18, administrative-services-manager was 7/18. Needs-refresh list now down to 2 entries.

## Next Steps
- Task #1 (tracked): upgrade `advertising-promotions-manager` to spec 2 — next in the queue (40 roles remain after the two done this session) and also needs-refresh (5/18).
- After that, `agricultural-manager` is next unclaimed queue entry.
- ESCO-BACKLOG.md's 260 new roles (biggest chunks: ISCO 2 Professionals 128, ISCO 3 Technicians 53) are a separate, larger body of work — not started, no roles drafted from it yet.
