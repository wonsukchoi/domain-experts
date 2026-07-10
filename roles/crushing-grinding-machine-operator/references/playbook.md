# Playbook

## Classifier cut point vs. target spec assessment (filled example)

Current classifier cut point: 150 microns. Target: 80% passing 106 microns.

| Step | Value |
|---|---|
| Current classifier cut point | 150 microns |
| Target spec (finest requirement) | 106 microns |
| Gap | 150 − 106 = 44 microns |
| Gap as % of current cut point | 44 / 150 = 29.3% |
| Naive fix (extend mill residence time) | Shifts bulk distribution finer, but classifier still passes up to 150 microns |
| Correct fix | Reset classifier cut point to 106 microns (or finer, accounting for separation efficiency) |

**Comparison across target specs (same 150-micron current classifier):**

| Target spec | Gap to current classifier | Gap % |
|---|---|---|
| 80% passing 125 microns | 150 − 125 = 25 microns | 16.7% |
| 80% passing 106 microns | 150 − 106 = 44 microns | 29.3% |
| 80% passing 75 microns | 150 − 75 = 75 microns | 50.0% |

**Rule applied:** The finer the target spec relative to the current classifier setting, the larger the gap that mill residence time alone cannot close — at 50% gap, no amount of extended grinding time will reliably achieve the target without directly resetting the classifier.

## Circulating load reference (filled example)

| Circulating load ratio | Typical circuit condition |
|---|---|
| Under 100% | Classifier likely passing too much oversize, mill capacity for fine grinding sitting idle |
| 150–250% | Commonly cited optimal range for many closed-circuit ball mill operations |
| Over 400% | Mill/classifier likely overloaded, reduced net throughput without proportional fineness gain |

**Applied check:** A circuit reporting stable mill power and throughput but circulating load trending toward 400%+ is a distinct warning sign the power/throughput numbers alone wouldn't reveal — worth investigating classifier performance or feed characteristic changes before assuming the circuit is running normally.
