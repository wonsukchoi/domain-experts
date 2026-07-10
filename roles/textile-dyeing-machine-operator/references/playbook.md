# Playbook

## Bath concentration recalculation across liquor ratios (filled example)

Recipe: 2.0% owf dye, validated at 10:1 liquor ratio. Production batch: 500 kg fiber, machine runs at 6:1.

| Step | Value |
|---|---|
| Dye charge (%owf, liquor-ratio-independent) | 500 kg × 0.02 = 10 kg |
| Validated bath volume (10:1) | 500 × 10 = 5,000 L |
| Validated bath concentration | 10 kg ÷ 5,000 L = 0.20% (2.0 g/L) |
| Production bath volume (6:1) | 500 × 6 = 3,000 L |
| Production bath concentration (same 10 kg charge) | 10 kg ÷ 3,000 L = 0.333% (3.33 g/L) |
| Concentration increase | 3.33 ÷ 2.0 = 1.665 → 66.5% higher than validated |

**Comparison across liquor ratios (same 500 kg batch, same 10 kg dye charge):**

| Liquor ratio | Bath volume | Bath concentration | vs. validated (2.0 g/L) |
|---|---|---|---|
| 10:1 (validated) | 5,000 L | 2.0 g/L | Baseline |
| 8:1 | 4,000 L | 2.5 g/L | +25% |
| 6:1 (production) | 3,000 L | 3.33 g/L | +66.5% |
| 4:1 | 2,000 L | 5.0 g/L | +150% |

## Multi-dye exhaustion diagnosis worksheet (filled example)

Three-dye blend recipe. Finished batch shows an overall shade shift toward red compared to the standard.

| Dye component | Target exhaustion % | Measured exhaustion % | Deviation |
|---|---|---|---|
| Yellow | 92% | 91% | -1 point, within normal variation |
| Red | 88% | 96% | **+8 points — over-exhausting relative to target** |
| Blue | 90% | 89% | -1 point, within normal variation |

**Diagnosis:** The red component is over-exhausting significantly relative to its target while yellow and blue are within normal variation — this explains the overall shift toward red. Correction should target the red dye's exhaustion conditions specifically (e.g., temperature/time for that component, or its auxiliary chemical levels), not a broad adjustment to all three dyes in the recipe.
