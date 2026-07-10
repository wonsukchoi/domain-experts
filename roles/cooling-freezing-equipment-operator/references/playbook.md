# Playbook

## Thickness-squared freezing time recalculation (filled example)

Original product: 5cm thickness, 90-minute freezing time. New product: 10cm thickness.

| Step | Value |
|---|---|
| Original thickness | 5cm |
| Original freezing time | 90 min |
| New thickness | 10cm |
| Thickness ratio | 10 / 5 = 2.0 |
| Freezing time scaling factor (ratio²) | 2.0² = 4.0 |
| Recalculated freezing time | 90 × 4.0 = 360 min |
| Naive (linear) freezing time | 90 × 2.0 = 180 min |
| Underestimate if naive time used | (360 − 180) / 180 = 100% |

**Comparison across thickness ratios (same 90-minute baseline):**

| Thickness ratio | Correct (squared) freezing time | Naive (linear) freezing time | Underestimate |
|---|---|---|---|
| 1.5x | 90 × 2.25 = 202.5 min | 90 × 1.5 = 135 min | (202.5−135)/135 = 50% |
| 2.0x | 90 × 4.0 = 360 min | 90 × 2.0 = 180 min | 100% |
| 3.0x | 90 × 9.0 = 810 min | 90 × 3.0 = 270 min | 200% |

**Rule applied:** The gap between naive linear scaling and the correct thickness-squared relationship grows rapidly as the size increase grows — even a modest 50% thickness increase produces a 50% underestimate of required freezing time if scaled linearly instead of by the square.

## Danger-zone time tracking worksheet (filled example)

Food-safety cumulative danger-zone (40–140°F) time limit: 4 hours total across the process.

| Process stage | Time in danger zone | Cumulative total |
|---|---|---|
| Receiving/staging before freezer entry | 25 min | 25 min |
| Transition into freezer (product still above freezing point) | 40 min | 65 min |
| Post-freeze handling before cold storage | 15 min | 80 min |

**Result:** Cumulative danger-zone exposure across the process totals 80 minutes (1.33 hours) — well within the 4-hour limit. This tracking is independent of whether the final product's core temperature verification passes; both checks are required, and a passing core temperature result doesn't substitute for confirming cumulative danger-zone time stayed within limits.
