# Special Effects Artist/Animator — Playbook

## Render-farm budget worksheet

Formula: `frames × minutes-per-frame ÷ node-count = wall-clock hours`. Compare against remaining hours to the deadline before committing to a simulation-resolution decision.

| Input | Value |
|---|---|
| Shot length | 8 sec at 24 fps = 192 frames |
| Per-frame render time (full-res fur) | 96 min |
| Per-frame render time (reduced-substep fur) | 58 min |
| Allocated farm nodes | 8 |
| Deadline (to comp handoff) | 24 hrs |

| Option | Render-hours | Wall-hours (÷8 nodes) | Fits deadline? |
|---|---|---|---|
| Full-res fur | 307.2 | 38.4 | No — 14.4 hrs over |
| Full-res fur + 6 borrowed nodes (14 total) | 307.2 | 21.9 | Yes — but delays 2 other shots |
| Reduced-substep fur | 185.6 | 23.2 | Yes — 0.8 hr buffer, no impact on other shots |

Decision rule: if a resolution reduction passes a side-by-side playblast comparison at delivery viewing distance, it dominates a node-borrowing option that costs another shot its schedule.

## Pipeline approval-gate checklist

Filled example for a single shot moving through the pipeline:

| Stage | Deliverable | Approval required before next stage | Status |
|---|---|---|---|
| Previz | Rough camera + blocking pass | Director sign-off on staging | ✅ Approved v002 |
| Blocking | Key poses, timing, no polish | Director sign-off on timing | ✅ Approved v004 |
| Animation | Full secondary motion, no sim | Anim lead sign-off on performance | ✅ Approved v006 |
| Simulation | Fur/cloth sim layered on approved animation | VFX supervisor sign-off on sim quality/cost | ⚠️ In revision (see render-budget memo) |
| Lighting | Lit render with all AOV passes | DP/supervisor sign-off on look | Blocked on simulation gate |
| Comp | Final composited frame sequence | Director final sign-off | Blocked on lighting gate |

A stage marked "blocked" should never receive full-resolution work — test/preview renders only until its gate clears.

## Revision-round log (filled example)

| Round | Note received | Diagnosis | Disposition |
|---|---|---|---|
| 1 | "The landing doesn't feel heavy enough" | Anticipation frame too short (1 frame vs. needed 3-4 on a heavy landing) | Accepted — added 3 frames anticipation |
| 2 | "Extend the fur sim to the close-up insert" | New simulation scope, not a fix to existing work | Accepted with cost flag — see render-budget memo |
| 3 | "Make the creature look more menacing" | Ambiguous — requested reference or specific beat | Deferred pending director reference material |

Cap revision rounds at the number agreed in the shot's statement of work; a round consumed by an undiagnosed vague note (like round 3 above) should be deferred for clarification rather than spent on a guess.
