# CONTEXT

## Current Task
2026-07-17 session: drafted `acoustical-engineer` (spec 2, rubric 17/18) as a new top-level engineering role — ESCO 2149.1, no O*NET-SOC match; existing candidates (sound-engineering-technician, audiovisual-equipment-installer, energy-engineer) don't cover architectural/environmental acoustics engineering.

## Key Decisions
- Confirmed no reasonable parent role exists among candidates: wrong tools/absent decision steps (no Sabine equation, no STC/NIC, no NC/RC, no vibration isolation), not just "less detail".
- Added UNMAPPED_NOTES entry for `acoustical-engineer` in `scripts/generate_roadmap.py`; regenerated `data/roles.json`, `README.md`, `ROADMAP.md` via the standard pipeline.

## Next Steps
- Resume ESCO-BACKLOG.md one-by-one from ISCO 1 remaining (consul, diplomat, ambassador, police commissioner, etc.), then ISCO 2/3.
- Same recipe each time: draft → checkbox + UNMAPPED_NOTES → lint → regenerate → commit/push individually.
