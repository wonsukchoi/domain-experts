# Playbook

## Dot-gain diagnosis calculation (filled example)

CMYK process job, 150 lpi, cyan plate midtone dot built at 32% (compensated for expected 18-point gain to hit a 50% printed target).

| Step | Value |
|---|---|
| Plate midtone dot | 32% |
| Expected gain (compensation assumption) | 18 points |
| Expected printed dot | 32 + 18 = 50% |
| Measured printed dot (mid-run) | 58% |
| Actual gain | 58 − 32 = 26 points |
| Excess gain vs. compensation | 26 − 18 = 8 points |

**Diagnosis:** Actual gain (26 points) exceeds the compensated assumption (18 points) by 8 points. This is isolated to dot gain at this tonal point — check highlight and shadow control patches to confirm the shift isn't uniform across the whole tonal range (which would instead suggest a general density issue).

## Compensation-curve rebuild worksheet (filled example)

If press investigation confirms this press consistently runs 26 points of gain at midtone (not a one-off drift correctable within the run):

| Step | Value |
|---|---|
| True press gain at midtone (confirmed across multiple runs) | 26 points |
| Target printed midtone dot | 50% |
| Rebuilt plate dot needed | 50 − 26 = 24% |
| Old plate dot (based on incorrect 18-point assumption) | 32% |
| Difference | 32 − 24 = 8 points lower plate dot needed |

**Result:** Future plates for this job on this specific press/substrate combination should be built at a 24% midtone dot, not the original 32%, to correctly hit the 50% printed target given this press's actual observed behavior.

## Control-patch reading log (filled example)

| Sheet count | Cyan midtone density | Registration (thousandths off) | Action |
|---|---|---|---|
| 100 (makeready approval) | 1.40 (target) | 0.5 | Approved |
| 500 | 1.42 | 0.5 | Within tolerance, no action |
| 1,500 | 1.51 | 1.0 | Ink/water adjustment made |
| 3,000 | 1.41 | 0.5 | Back within target after adjustment |

Spot-checks at 500-sheet intervals caught the drift at the 1,500-sheet mark before it accumulated further — a single makeready approval alone would not have surfaced this until the run was substantially further along.
