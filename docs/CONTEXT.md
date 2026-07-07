# CONTEXT

## Current Task
2026-07-08 session: mass role-drafting via parallel Agent forks across O*NET groups 35/37/45/47/49/53. 492 roles total (up from 331), lint 0 errors, all pushed to main. Closed groups 35 (Food Prep, 16/18), 37 (Building/Grounds, 8/10), 45 (Farming/Fishing/Forestry, 12/14), 49 (Install/Maint/Repair, 48/52). Opened 47 (Construction/Extraction, 25/65) and 53 (Transportation, 49/57, essentially done).

## Key Decisions
- Skipped O*NET group 55 (Military Specific) entirely — infantry/artillery/special-forces content is weapons-and-tactics doctrine, out of scope for this repo.
- Batch pattern: spawn ~12 parallel general-purpose Agent forks per wave, each does full AUTHORING.md pipeline solo (research→draft→self-critique), self-scores against the 9-criterion rubric, reports concerns; then lint the whole batch, fix any banned-word hits, regenerate roadmap, commit, push.
- Catch-all O*NET codes ("All Other") and thin generic codes (e.g. plain "Transportation Inspectors" when specific sub-codes already covered) are intentionally skipped per repo convention.
- Dual-use-adjacent trades (locksmith, pesticide handler, commercial diver, hazmat removal) shipped fine with professional/compliance framing — no bypass-technique or formulation content.

## Next Steps
- Group 47 (Construction/Extraction) has 40 occupations remaining — biggest open lever.
- Group 53 has 8 remaining (supervisor/catch-all codes) — low priority, likely skip.
- Groups 51 (Production, 0/114) and 53's sibling large group not yet started: still fully open.
- Parity coverage and eval-running (from prior session) still outstanding — not touched this session.
