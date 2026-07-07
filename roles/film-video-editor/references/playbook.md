# Film and Video Editor — Playbook

## Runtime-reduction pass (narrative-weight allocation)

When a cut must lose more than ~15% of its length, allocate the cut budget by narrative weight, not evenly. Rank each act/scene 1 (load-bearing, protect) to 3 (redundant, absorb cuts), then reconcile the total cut to the target.

| Scene/act | Original | Weight (1-3) | Target cut % | New length |
|---|---|---|---|---|
| Setup | 8:00 | 3 | 60% | 3:12 |
| Rising action | 9:30 | 2 | 20% | 7:36 |
| Midpoint turn | 6:00 | 1 | 8% | 5:31 |
| Complication | 7:30 | 3 | 60% | 3:00 |
| Climax | 5:30 | 1 | 5% | 5:14 |
| Resolution | 5:30 | 2 | 25% | 4:08 |

Check: sum the "new length" column and compare to the target runtime. If it overshoots or undershoots, adjust weight-3 scenes first — never weight-1 scenes — until the total reconciles exactly.

## Revision-round budget (agree before the first cut is shown)

| Round | Purpose | Note volume expected | Runtime change allowed |
|---|---|---|---|
| 1 — Rough cut review | Structure, story beats, act order | High (structural notes) | Any |
| 2 — Fine cut review | Pacing, performance selects, scene-level trims | Medium | ±10% of target |
| 3 — Picture lock review | Final polish only — no new structural notes | Low | ±2% of target |
| Post-lock | Formal reopen only, requires sign-off from all downstream departments | N/A | Logged as a change order, not a routine revision |

If Round 3 produces structural notes ("can we move this scene earlier"), that is a signal the review process skipped ahead too fast — flag it rather than absorb it silently, since it usually means Round 1 didn't actually get structural sign-off.

## EDL/AAF/XML finishing handoff checklist

1. Confirm frame rate and resolution match the delivery spec (e.g. 23.976fps ProRes 422 HQ, not the offline proxy's 29.97fps).
2. Export EDL/AAF/XML and re-import into a blank timeline to conform-check before sending — catches gap/dropped-frame errors before they reach the finishing house.
3. Flatten or clearly label all temp music/SFX tracks separately from dialogue/production audio, so sound is not mistakenly conformed with a placeholder track.
4. Attach a shot-by-shot change log for any reel that was recut after a prior handoff — finishing houses conform against the log, not against memory of the last version.
5. Confirm color-critical shots (day-for-night, green screen, heavily graded references) are flagged with source-media links, not just the offline proxy.

## Sample edit notes (filled)

> **EDIT NOTES — Fine Cut 3 → Picture Lock (target 26:30, current 27:05)**
> Remaining overage: 0:35.
> Act 2 (Rising action): recommend cutting the second interview beat (0:22) — repeats a point made in Act 1's opening.
> Act 6 (Resolution): recommend trimming the closing wide shot hold (0:13) — no new information after the 4-second mark.
> Both cuts are below the ±2% Round 3 threshold and do not touch any weight-1 scene. Awaiting sign-off to lock.
