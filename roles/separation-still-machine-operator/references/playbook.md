# Playbook

## Effective-theoretical-stages calculation (filled example)

Column with 20 physical trays, tray efficiency 70%.

| Step | Value |
|---|---|
| Physical trays | 20 |
| Tray (Murphree) efficiency | 70% |
| Effective theoretical stages | 20 × 0.70 = 14 |
| Naive assumption (nameplate = theoretical) | 20 stages |
| Overestimate of separation capability | (20 − 14) / 20 = 30% |

**Comparison across tray efficiencies (same 20-tray column):**

| Tray efficiency | Effective theoretical stages | Overestimate if nameplate (20) used instead |
|---|---|---|
| 90% | 20 × 0.90 = 18 | (20−18)/20 = 10% |
| 70% | 20 × 0.70 = 14 | (20−14)/20 = 30% |
| 50% | 20 × 0.50 = 10 | (20−10)/20 = 50% |

**Rule applied:** As tray efficiency degrades (from fouling, wear, or design limitations for a specific separation duty), the gap between nameplate and effective capability widens substantially — a column that was adequately characterized at 90% efficiency years ago may now be running at 70% or lower, and continuing to use the original nameplate-based calculation would produce an increasingly large purity shortfall.

## Reflux ratio / purity comparison table (filled example)

Illustrative relationship between reflux ratio and achievable purity at 14 effective theoretical stages (specific values depend on the actual system's vapor-liquid equilibrium data).

| Reflux ratio | Approximate achievable purity at 14 stages |
|---|---|
| 1.5 | 94% |
| 2.0 | 97% |
| 2.5 | 98.5% |
| 3.0 | 99.2% |

**Applied check:** To reliably hit the 98% target with margin, a reflux ratio around 2.5 is appropriate at 14 effective stages — using a reflux ratio calculated assuming 20 stages (which would predict 98% achievable at a lower ratio, closer to 2.0) would actually deliver something closer to 97% purity at 14 real effective stages, missing the target.
