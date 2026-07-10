# Playbook

## Non-uniform grade rule calculation (filled example)

Base size 10, target size 20 (5 size steps: 10→12→14→16→18→20). Size chart: 2" bust increment for steps within 4–16, 1.5" increment for steps 16–18 and 18–20.

| Size step | Size chart increment | Cumulative growth |
|---|---|---|
| 10→12 | 2.0" | 2.0" |
| 12→14 | 2.0" | 4.0" |
| 14→16 | 2.0" | 6.0" |
| 16→18 | 1.5" | 7.5" |
| 18→20 | 1.5" | 9.0" |

| Step | Value |
|---|---|
| Correct total growth, size 10 to size 20 | 9.0" |
| Naive uniform 2"/step across all 5 steps | 2.0 × 5 = 10.0" |
| Overshoot | 10.0 − 9.0 = 1.0" |
| Overshoot as % of correct growth | 1.0 / 9.0 = 11.1% |

**Comparison across grading targets (same base size 10, same size chart):**

| Target size | Correct total growth | Naive uniform 2"/step growth | Overshoot |
|---|---|---|---|
| 16 (3 steps, all standard) | 6.0" | 6.0" | 0% (matches — no plus-size steps involved) |
| 18 (4 steps: 3 standard + 1 compressed) | 6.0 + 1.5 = 7.5" | 2.0 × 4 = 8.0" | 6.7% |
| 20 (5 steps: 3 standard + 2 compressed) | 6.0 + 3.0 = 9.0" | 2.0 × 5 = 10.0" | 11.1% |

**Rule applied:** The overshoot only appears once grading crosses into the compressed-increment size breaks — grading within the standard range alone (base 10 to size 16) shows zero error from the naive approach, which is exactly why the non-uniform increment issue is easy to miss until a pattern is graded past the transition point.

## Ease-preservation check across graded sizes (filled example)

Base size 10: bust measurement 34", finished garment measurement 37" (3" ease). Graded size 20: bust measurement 43" (per size chart).

| Approach | Finished garment measurement at size 20 | Resulting ease at size 20 |
|---|---|---|
| Naive (outline grown, ease allowance held as a flat 3" addition regardless of proportion) | 43 + 3 = 46" | 3" ease — same flat amount, but now a smaller % of body measurement |
| Correct (ease scaled proportionally: 3"/34" = 8.8% of bust) | 43 × 1.088 = 46.8" | 3.8" ease — same proportional feel as the base size |

**Result:** A flat 3" ease addition at every size understates the proportional looseness a larger-bust wearer would expect relative to the base size fit — the correct approach scales ease as a consistent percentage of body measurement, not a fixed inch amount, to preserve how the garment actually feels across the size range.
