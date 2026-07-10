# Playbook

## Plating-time calculation accounting for cathode efficiency (filled example)

Target thickness 25 microns nickel, part area 500 cm², theoretical deposition rate 0.5 microns/min at 100% efficiency, bath cathode efficiency 95%.

| Step | Value |
|---|---|
| Theoretical deposition rate (100% efficiency) | 0.5 microns/min |
| Bath cathode efficiency | 95% |
| Actual achievable rate | 0.5 × 0.95 = 0.475 microns/min |
| Target thickness | 25 microns |
| Required time | 25 / 0.475 = 52.6 minutes |
| Naive time (efficiency ignored) | 25 / 0.5 = 50.0 minutes |
| Thickness achieved at naive 50-minute time | 50 × 0.475 = 23.75 microns |
| Shortfall | 25 − 23.75 = 1.25 microns (5.0%) |

**Comparison across cathode efficiencies (same 25-micron target, same 0.5 micron/min theoretical rate):**

| Cathode efficiency | Required time | Time if naive (efficiency ignored) | Shortfall at naive time |
|---|---|---|---|
| 98% | 25 / 0.49 = 51.0 min | 50.0 min | 25 − (50×0.49) = 0.5 microns (2.0%) |
| 95% | 25 / 0.475 = 52.6 min | 50.0 min | 25 − (50×0.475) = 1.25 microns (5.0%) |
| 85% | 25 / 0.425 = 58.8 min | 50.0 min | 25 − (50×0.425) = 3.75 microns (15.0%) |

**Rule applied:** As bath efficiency drops (from contamination, chemical depletion), the gap between naive and correct time calculations grows — a bath at 85% efficiency ignored in the calculation produces a shortfall three times larger than a bath at 95% efficiency, making periodic efficiency re-verification more important as bath age/condition changes.

## Current density / throwing power reference (filled example)

| Bath type | Effective current density range | Typical throwing power | Notes |
|---|---|---|---|
| Bright nickel | 2–6 A/dm² | Moderate | Good general-purpose throwing power for moderately complex geometry |
| Hard chrome | 15–30 A/dm² | Poor | Requires auxiliary anodes or special fixturing for recessed areas |
| Cyanide copper | 1–4 A/dm² | Good | Better throwing power, suitable for complex geometry as a strike layer |

**Applied check:** A part with deep recesses plated in a hard chrome bath (poor throwing power) needs specific verification at those recessed locations regardless of how good the exposed-surface thickness measures — the bath chemistry itself predicts this risk before any measurement is even taken.
