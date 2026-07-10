# Playbook

## Blowdown-rate recalculation after a production increase (filled example)

Prior steady state: boiler water TDS equilibrium 3,000 ppm, limit 3,500 ppm, makeup water 300 ppm TDS.

| Step | Value |
|---|---|
| Prior equilibrium TDS | 3,000 ppm |
| TDS limit | 3,500 ppm |
| Steam production increase | 25% |
| Projected new equilibrium TDS (proportional approximation) | 3,000 × 1.25 = 3,750 ppm |
| Amount over limit | 3,750 − 3,500 = 250 ppm |
| Percentage over limit | 250 / 3,500 = 7.1% |

**Required correction:** Increase blowdown rate proportionally to the 25% increase in dissolved solids input, then verify via conductivity meter that the new equilibrium actually holds at or below 3,500 ppm — don't assume the proportional calculation alone is sufficient without measurement confirmation.

**Comparison across production increases (same starting conditions):**

| Production increase | Projected new equilibrium TDS | Over/under 3,500 ppm limit |
|---|---|---|
| 10% | 3,000 × 1.10 = 3,300 ppm | Under limit — monitor, may not need blowdown change |
| 25% | 3,000 × 1.25 = 3,750 ppm | 250 ppm (7.1%) over — blowdown increase required |
| 40% | 3,000 × 1.40 = 4,200 ppm | 700 ppm (20%) over — significant blowdown increase required |

## Safety-test independence checklist (filled example)

| Safety system | Last verified | Verification method | Protects against |
|---|---|---|---|
| Blowdown/water chemistry | This week (TDS check) | Conductivity meter reading | Scale, carryover |
| Safety valve | 8 months ago | Lift/reseat test | Overpressure rupture |
| Low-water fuel cutoff | 14 months ago | Slow-drain functional test | Dry-firing/catastrophic overheating |

**Assessment:** Recent water chemistry verification says nothing about the safety valve or low-water cutoff status. If the safety valve's code-required interval is 12 months, it is not yet due at 8 months. If the low-water cutoff's required interval is also 12 months, it is **overdue at 14 months** and requires immediate scheduling — regardless of how recently or well the water chemistry has been maintained.
