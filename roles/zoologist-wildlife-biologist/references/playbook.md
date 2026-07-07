# Zoologist/Wildlife Biologist — Playbook

## Mark-recapture worksheet (Chapman-modified Lincoln-Petersen)

| Input | Symbol | Value |
|---|---|---|
| Marked, occasion 1 | M | 85 |
| Captured, occasion 2 | C | 76 |
| Recaptured (marked, seen again) | R | 19 |
| Point estimate | N̂ = [(M+1)(C+1)/(R+1)] − 1 | 330 |
| Variance | Var(N̂) = [(M+1)(C+1)(M−R)(C−R)] / [(R+1)²(R+2)] | 2,568 |
| SE | √Var | 50.7 |
| 95% CI | N̂ ± 1.96·SE | 231–429 |

**Closure check before using this estimator:** survey window ≤ ~10% of species' generation time or typical movement/turnover rate. If violated, switch to Schnabel (3+ occasions) or Jolly-Seber (open population).

**Sample-size rule of thumb:** if R < 20, prefer Chapman's correction over raw Lincoln-Petersen (N̂ = MC/R); raw estimator's positive bias grows fast below R ≈ 20.

## Distance-sampling worksheet (line-transect, abbreviated)

| Transect | Length (km) | Detections | Perpendicular distances (m, sample) |
|---|---|---|---|
| T1 | 4.0 | 12 | 8, 22, 45, 15, 60, ... |
| T2 | 4.0 | 9 | 18, 33, 12, 50, ... |
| T3 | 4.0 | 15 | 5, 40, 28, 65, ... |
| **Total** | **12.0** | **36** | — |

1. Fit a detection function (half-normal or hazard-rate) to the pooled perpendicular-distance data → effective strip half-width (ESW).
2. Density = n / (2 × L × ESW), where n = total detections, L = total transect length.
3. Population = Density × total habitat area surveyed.
4. Report density with its CV from the detection-function fit — a detection function fit to <60-80 detections typically has a wide CV; flag if total n is below that range.

## PVA input/output table (abbreviated)

| Vital rate | Estimate | Source years | Notes |
|---|---|---|---|
| Adult survival | 0.82/yr | 2016–2024 (8 yrs) | Mark-resight based |
| Juvenile survival | 0.41/yr | 2018–2024 (6 yrs) | Smaller sample, wider CI |
| Fecundity | 1.3 offspring/female/yr | 2016–2024 | Stable across years sampled |
| Carrying capacity | ~450 (habitat-model estimate) | — | Not field-validated |

**Output (100-run stochastic simulation, 50-year horizon):** median population trajectory declining from 330 to ~210; probability of falling below quasi-extinction threshold (N = 50) within 50 years: 14%.

**Caveat to carry into any report:** vital rates are drawn from 6-8 years of data; a 50-year projection extrapolates roughly 6-8x beyond the observed window. Report the projection's sensitivity to the juvenile-survival estimate specifically (it has the widest CI and the simulation's outcome is most sensitive to it) rather than presenting the median trajectory as a single confident forecast.

## Habitat-suitability vs. occupancy reconciliation

| Grid cell | Modeled suitability | Ground-truthed occupancy | Flag |
|---|---|---|---|
| A | High (0.82) | Occupied | Consistent |
| B | High (0.79) | Unoccupied | **Investigate — competitor species present, camera-trap confirmed** |
| C | Moderate (0.51) | Occupied | Consistent (model conservative) |
| D | Low (0.18) | Unoccupied | Consistent |

Cell B is the actionable finding: high modeled suitability with confirmed absence, and a documented biotic constraint (competitor detected on camera trap) rather than a data gap. Report this as a finding about interspecific exclusion, not as evidence the habitat model needs recalibration — recalibrating to fit cell B would suppress a real ecological signal in every other high-suitability cell.
