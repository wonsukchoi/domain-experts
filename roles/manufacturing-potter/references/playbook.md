# Playbook

## Total-shrinkage wet-form calculation (filled example)

Target fired diameter 80mm, clay body total shrinkage 12%.

| Step | Value |
|---|---|
| Target fired diameter | 80mm |
| Total shrinkage rate | 12% |
| Wet-form diameter required | 80 / (1 − 0.12) = 80 / 0.88 = 90.9mm |
| Result if naive 80mm wet-form used | 80 × 0.88 = 70.4mm fired diameter |
| Shortfall | 80 − 70.4 = 9.6mm (12% short of target) |

**Comparison across shrinkage rates (same 80mm target):**

| Total shrinkage | Wet-form diameter required | Fired result if naive 80mm wet-form used |
|---|---|---|
| 8% | 80 / 0.92 = 87.0mm | 80 × 0.92 = 73.6mm (8% short) |
| 12% | 80 / 0.88 = 90.9mm | 80 × 0.88 = 70.4mm (12% short) |
| 16% | 80 / 0.84 = 95.2mm | 80 × 0.84 = 67.2mm (16% short) |

**Rule applied:** Every clay body's specific shrinkage rate has to be looked up and applied individually — reusing a wet-form dimension calculated for one body on a different body with a different shrinkage rate produces a proportionally different sizing error.

## Critical-range firing schedule reference (filled example)

| Temperature range | Ramp rate | Reason |
|---|---|---|
| Room temp – 200°C | Moderate (e.g. 100°C/hr) | Driving off residual moisture |
| 200°C – 550°C | Moderate | Organic burnout, no major volume change risk |
| 550°C – 600°C (quartz inversion at ~573°C) | **Slow** (e.g. 50°C/hr or slower) | Rapid silica volume change — cracking risk if rushed |
| 600°C – peak | Can resume faster ramp | Past the critical inversion range |
| Cooling through 573°C on the way down | **Slow** | Quartz inversion occurs on cooling too, not just heating |

**Rule applied:** The quartz inversion range needs a slower ramp rate on both the way up and the way down through 573°C — treating it as a one-directional concern (only during heating) misses the equal cracking risk during cooling.
