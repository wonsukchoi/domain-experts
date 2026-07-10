# Playbook

## Fill-target / z-score calculation (filled example)

Label weight 500g, individual minimum 485g, measured process SD 8g.

| Scenario | Fill target | Distance to 485g minimum | z-score | Approx. individual non-compliance rate |
|---|---|---|---|---|
| Naive (target = label weight) | 500g | 500 − 485 = 15g | 15 / 8 = 1.875 | ~3.0% |
| Corrected (12g overfill margin) | 512g | 512 − 485 = 27g | 27 / 8 = 3.375 | ~0.04% |

**Comparison across overfill margins (same 485g minimum, 8g SD):**

| Fill target | Overfill margin | z-score | Approx. non-compliance rate |
|---|---|---|---|
| 500g | 0g | 1.875 | ~3.0% |
| 505g | 5g | 2.5 | ~0.62% |
| 512g | 12g | 3.375 | ~0.04% |
| 520g | 20g | 4.375 | <0.001% |

**Rule applied:** The overfill margin required to hit a given z-score target scales directly with the process's actual standard deviation. To hit the same z = 3.375 safety margin at SD 4g instead of 8g, the required distance above 485g is 3.375 × 4 = 13.5g, giving a fill target of 485 + 13.5 = 498.5g — nearly 13.5g less overfill than the 512g needed at SD 8g. Tighter process control (lower SD) directly reduces the product cost of maintaining the same compliance margin.

## Checkweigher threshold worksheet (filled example)

| Parameter | Value |
|---|---|
| Label weight | 500g |
| Individual minimum (regulatory) | 485g |
| Fill target (with overfill margin) | 512g |
| Checkweigher reject threshold | Set at or just above 485g (e.g., 486g) to reject anything at or below the regulatory floor with margin for scale accuracy |
| Checkweigher upper-side monitoring (optional) | Flag packages significantly above target (e.g., >530g) as a process-drift signal, not a compliance issue per se |

**Result:** The reject threshold is derived directly from the regulatory individual-minimum requirement (485g), not from an operator's sense of "close enough" — setting it at, say, 490g "to be extra safe" would reject compliant product unnecessarily, while setting it at 480g "to reduce waste" would pass legally non-compliant packages.

## Headspace verification by process type (filled example)

| Process/container type | Typical headspace requirement | Consequence of insufficient headspace |
|---|---|---|
| Retort-processed can | 6–10% of container height | Deformation/rupture risk from thermal expansion during retort |
| Vacuum-sealed pouch | Minimal, but sufficient for seal integrity | Seal failure or incomplete vacuum if fill is too high |
| Carbonated beverage bottle | Specific target per product carbonation level | Pressure buildup risk, or under-carbonation feel if headspace too large |

**Applied check:** Minimizing headspace to "get more product per container" on a retort-processed can specifically risks container failure during the thermal process — the headspace target here is a safety-relevant process parameter, not a cost-optimization lever.
