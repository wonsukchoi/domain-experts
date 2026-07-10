# Playbook

## Giveaway-minimization calculation (filled example)

Label weight 200g, individual minimum 190g, measured SD 6g.

| Scenario | Target weight | Distance to 190g minimum | z-score | Approx. non-compliance rate | Giveaway |
|---|---|---|---|---|---|
| Naive (target = label weight) | 200g | 200 − 190 = 10g | 10 / 6 = 1.667 | ~4.75% | 0g (0%) |
| Corrected (8g margin) | 208g | 208 − 190 = 18g | 18 / 6 = 3.0 | ~0.13% | 8g (4.0%) |

**Comparison across measured SD values (same 200g label, 190g minimum):**

| Measured SD | Target for z=3.0 (0.13% non-compliance) | Giveaway (g) | Giveaway (%) |
|---|---|---|---|
| 6g | 190 + (3.0 × 6) = 208g | 8g | 4.0% |
| 4g | 190 + (3.0 × 4) = 202g | 2g | 1.0% |
| 8g | 190 + (3.0 × 8) = 214g | 14g | 7.0% |

**Rule applied:** Giveaway cost scales directly with process variability — reducing SD from 6g to 4g (through blade condition or process improvement) cuts the required giveaway margin from 8g to 2g at the same compliance safety level, a real, quantifiable savings opportunity worth pursuing rather than treating the 6g SD as fixed.

## Blade-condition-vs-cut-quality diagnostic (filled example)

| Symptom | Naive response | Correct diagnostic step |
|---|---|---|
| Ragged/torn slice edges | Slow down machine speed | Check blade sharpness against maintenance interval first |
| Kerf loss trending up (yield declining at same thickness setting) | Adjust thickness thinner to compensate | Check blade condition — a dull blade often increases material loss per cut regardless of thickness setting |
| Portion weight trending heavier at same thickness setting | Readjust thickness down repeatedly | Check whether blade dulling is causing tearing/crushing that adds mass variance, or whether product lot density has shifted |

**Rule applied:** Thickness setting and blade condition are independent variables — a correct thickness setting with a degraded blade still produces defects, and adjusting thickness in response to a blade problem treats the symptom while leaving the actual cause (and its yield cost) unaddressed.
