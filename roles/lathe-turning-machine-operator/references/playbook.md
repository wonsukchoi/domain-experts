# Playbook

## Surface-speed-by-diameter calculation worksheet

Fill for any stepped part with multiple diameters.

| Section | Diameter | Target SFM | RPM = (SFM × 12) / (π × diameter) | Actual SFM if RPM held from prior section |
|---|---|---|---|---|
| A | 2.000" | 400 | (400×12)/(π×2.000) ≈ 764 | — |
| B | 1.000" | 400 | (400×12)/(π×1.000) ≈ 1,528 | If held at 764: (π×1.000×764)/12 ≈ 200 SFM (50% of target) |

**Formula:** RPM = (SFM × 12) / (π × diameter in inches)

**Rule:** recalculate RPM for every distinct diameter section on a stepped part — never hold RPM constant across sections with meaningfully different diameters.

## Chatter/rigidity reference table (illustrative — always verify against the specific machine/tooling's actual capability)

| Length-to-diameter ratio | Typical risk level | Recommended action |
|---|---|---|
| Up to 3:1 | Low | Standard parameters generally fine |
| 3:1-6:1 | Moderate | Consider reduced depth of cut/feed, monitor for chatter |
| 6:1-10:1 | High | Steady rest or tailstock support typically needed |
| Over 10:1 | Very high | Support required; consult tooling/process engineering for parameter reduction |

**Rule:** always verify against the specific machine and tooling setup's actual documented capability — this table is illustrative of the general risk trend, not a substitute for the setup's specific rigidity characteristics.

## In-process dimensional monitoring guide

1. Identify the critical dimension(s) that turning produces directly (not requiring secondary finishing).
2. Establish a measurement interval appropriate to the tolerance and expected tool wear rate (tighter tolerance/faster wear rate = more frequent checks).
3. Measure the actual dimension at each interval — don't rely on visual tool inspection as a substitute.
4. If a trend toward the tolerance limit is observed, tighten the measurement interval and/or plan a tool change before the limit is reached.
5. Document measurement results and any tool change/adjustment made in response to a detected trend.
