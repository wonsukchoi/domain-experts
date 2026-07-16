# Animator — Artifacts

## Shot-tier tracker (filled, from the SKILL.md worked example)

Sequence 8, 6-day block (3 animators × 6 days = 18 animator-days) before the director's spline-lock review.

| Shot(s) | Tier | Story function | Sec | Rate (sec/animator-day) | Animator-days | Pass status |
|---|---|---|---|---|---|---|
| 3, 7, 11, 14, 19, 22 | 1 — Hero | Dialogue / emotional close-ups | 14 | 1.5 | 9.33 | Blocking → spline → polish |
| Remaining 12 shots | 2 — Coverage | Wide/medium, no featured close-up | 28 | 4.0 | 7.00 | Blocking → spline (no polish) |
| 6 shots | 3 — Background | Off-screen cutaways/reactions | 12 | 10.0 | 1.20 | Blocking only |
| **Total** | | | **54** | | **17.53** | **0.47-day buffer against 18-day budget** |

Reconciliation: the naive uniform-rate plan (54 sec ÷ 1.5 sec/day full-pipeline rate) demands 36 animator-days against 18 available — a 100% overrun. Tiering by story function instead of treating the batch as uniform drops the requirement to 17.53 animator-days, because 18 of the 24 shots never needed the full-pipeline rate in the first place.

## Rig-limitation workaround memo (filled example)

> **To:** Rigging/TD — Sequence 8
> **Shot:** 14 (hero, reach-and-grab across a table)
> **Issue:** Shoulder control gimbal-locks past 90 degrees of forward rotation during the reach extreme; arm snaps on the frame where the pose crosses that threshold.
> **Workaround applied:** Added a driven-key corrective blend shape triggered at 85–95 degrees of shoulder rotation, smoothing the transition through the lock point. Isolated to this shot's rig instance; does not touch the base rig.
> **Recurrence check:** Same failure logged on Shots 14 and 21 (2 of 24 this batch) — under the 5-shot threshold for a rig-team fix. Flagging for tracking; will escalate to a base-rig fix request if a third shot hits it.
> **Time cost:** 1.5 hours added to Shot 14's blocking pass, absorbed within the shot's Tier 1 budget — no schedule impact this batch.

## Revision-note triage log (filled example)

| Shot | Note (as given) | Classification | Action taken | Re-review needed |
|---|---|---|---|---|
| 3 | "The reaction doesn't land — feels like it's a beat too fast." | Timing | Eased out the anticipation hold by 3 frames in the graph editor; no keys moved. | No — spacing-only fix |
| 11 | "Her hand shouldn't be in frame during that line." | Pose | Reopened blocking; repositioned hand pose across 6 keys, re-spline required. | Yes — full re-review |
| 19 | "This just feels heavy, like it's dragging." | Timing | Tightened ease-in curve on the primary body control; secondary (coat) layer untouched. | No — spacing-only fix |
| 22 | "Change the ending pose — she should be looking at the door, not down." | Pose | Reblocked final 4 keys; spline and polish both restarted for the shot's back half. | Yes — full re-review |

Rule applied here: every note is classified pose or timing before any keys are touched. Pose notes reopen blocking and cost a re-spline (and re-polish, if the shot was already in that tier); timing notes are resolved in the graph editor without moving a single keyframe, and don't require a full re-review — only a spot-check against the note.
