# Playbook

Filled formulas, tables, and thresholds a fire protection engineer runs against. Verify against the specific locally adopted code edition and AHJ amendments before certifying — these are the standard national methods, not a substitute for the governing edition in front of you.

## 1. Hazen-Williams friction loss (Hazen-Williams, US units)

**Pf = 4.52 × Q^1.85 / (C^1.85 × d^4.87)**, where Pf = friction loss (psi/ft), Q = flow (gpm), C = pipe roughness coefficient, d = actual internal pipe diameter (in).

| Pipe material | C-factor (NFPA 13 default) |
|---|---|
| Black steel, Schedule 40 | 120 |
| Galvanized steel | 120 |
| Ductile iron (cement-lined) | 140 |
| PVC / CPVC (listed for fire protection) | 150 |
| Copper tube | 150 |

| Nominal size (Sch 40 steel) | Actual internal diameter (in) |
|---|---|
| 1" | 1.049 |
| 1¼" | 1.380 |
| 1½" | 1.610 |
| 2" | 2.067 |
| 2½" | 2.469 |
| 3" | 3.068 |
| 4" | 4.026 |
| 6" | 6.065 |

*Example: Q = 15.00 gpm, C = 120, d = 1.049 in. Q^1.85 = 149.9; C^1.85 = 7,028; d^4.87 = 1.2624. Pf = 4.52 × 149.9 / (7,028 × 1.2624) = 677.5 / 8,871 = 0.0764 psi/ft.*

**Rule:** compute cumulative flow (sum of all upstream sprinklers) before computing friction loss for a segment — friction loss uses the flow *in that specific segment*, not the flow at the originating head.

**Elevation head:** add/subtract 0.433 psi per foot of elevation change between nodes (positive when flowing upward, i.e., pressure required increases going up).

## 2. Sprinkler discharge (K-factor equation)

**Q = K√P**, where Q = discharge (gpm), K = sprinkler K-factor (gpm/psi^0.5, stamped on the sprinkler), P = pressure at the sprinkler (psi).

| Common K-factor | Typical use |
|---|---|
| K=5.6 (nominal ½") | Light/Ordinary Hazard standard spray |
| K=8.0 | Ordinary/Extra Hazard, higher flow |
| K=11.2, K=14.0 | Extra Hazard, ESFR-adjacent standard spray |
| K=16.8, K=25.2 | ESFR (Early Suppression Fast Response), storage occupancies |

**Minimum operating pressure:** 7 psi for standard spray sprinklers unless the density-derived pressure or the sprinkler's listing requires higher (NFPA 13). ESFR sprinklers carry their own listed minimum pressures, commonly 15-50 psi depending on K-factor and storage height — always pull from the specific listing, never assume 7 psi applies.

## 3. NFPA 13 density/area design criteria (representative curve points)

| Hazard classification | Density (gpm/ft²) | Min. design area (ft²) | Hose stream allowance (gpm) | Water supply duration (min) |
|---|---|---|---|---|
| Light Hazard | 0.10 | 1,500 | 100 | 30 |
| Ordinary Hazard Group 1 | 0.15 | 1,500 | 250 | 60-90 |
| Ordinary Hazard Group 2 | 0.20 | 1,500 | 250 | 60-90 |
| Extra Hazard Group 1 | 0.30 | 2,500 | 500 | 90-120 |
| Extra Hazard Group 2 | 0.40 | 2,500 | 500 | 90-120 |

**Rule:** the curve trades density against area (higher density permits a smaller design area and vice versa) — pull the exact point from NFPA 13's Figure 11.2.3.1.1 curves for the classification, not just the table extremes shown here. Storage occupancies (rack, high-piled, in-rack sprinklers) use NFPA 13's storage-specific chapters instead of the general curve — commodity classification and storage height, not floor-area occupancy, drive the design.

## 4. Water supply / hydrant flow test analysis

**Available residual pressure at a target flow:** h_avail = h_static − (h_static − h_test) × (Q_target / Q_test)^1.85

**Available flow at a target residual pressure:** Q_avail = Q_test × [(h_static − h_target) / (h_static − h_test)]^0.54

*Example: static 65 psi, residual 50 psi at 1,000 gpm test flow. System requires 350 gpm at a demand-point residual of 40 psi. Available residual at 350 gpm: h_avail = 65 − (65−50) × (350/1,000)^1.85 = 65 − 15 × 0.1479 = 65 − 2.22 = 62.78 psi. 62.78 psi available exceeds the 40 psi required by 22.78 psi — supply adequate without a pump.*

**Rule:** plot both curves (supply descending from static to residual-at-test-flow, demand as a single point) rather than comparing single numbers in isolation when presenting to a reviewer — a demand point that falls under and left of the supply curve is adequate; one that falls on or above it requires a pump or supply improvement.

## 5. Fire pump sizing (NFPA 20)

| Curve point | Requirement |
|---|---|
| Churn (shutoff, 0% flow) | ≤140% of rated pressure |
| Rated flow (100%), rated pressure | Pump must deliver at least rated pressure at rated flow |
| 150% of rated flow | ≥65% of rated pressure |

**Sizing rule:** size the pump to make up exactly the shortfall between available supply and required demand at the design flow — never round up to the next larger stock pump "for margin" without checking that the larger pump's churn pressure doesn't overpressure downstream piping (may require a pressure-reducing valve or relief).

**Jockey pump:** maintains system pressure between fire events without cycling the main fire pump; sized for a small flow (commonly 1% of the main pump's rated capacity) at a pressure slightly above the main pump's churn pressure.

## 6. Occupant load and egress width (IBC Ch. 10 / NFPA 101)

| Occupancy (IBC Table 1004.5, gross unless noted) | Load factor (ft²/occupant) |
|---|---|
| Mercantile — basement/grade floor sales area | 30 |
| Mercantile — floors other than grade | 60 |
| Mercantile — storage, stock, shipping | 300 |
| Business areas | 150 |
| Assembly — concentrated (no fixed seats) | 7 |
| Assembly — standing space | 5 |

*Occupant load = floor area / load factor. Example: 12,000 sq ft grade-floor mercantile: 12,000 / 30 = 400 occupants.*

| Egress component | Capacity factor, non-sprinklered (in/occupant) | Capacity factor, sprinklered + voice alarm (in/occupant) |
|---|---|---|
| Stairways | 0.3 | 0.2 |
| Doors, corridors, ramps, other components | 0.2 | 0.15 |

*Example: 400 occupants, sprinklered + voice alarm building, egressing through level components. Required width = 400 × 0.15 = 60 in, distributed across the exits serving that occupant load — no single exit may carry a disproportionate share without checking the code's remaining-exit rule (loss of one exit still must clear the load at the same capacity factor).*

**Rule:** apply the sprinklered capacity factor only when the sprinkler system is NFPA 13-compliant, electronically monitored, and in service — reverify against the non-sprinklered factor for any system impairment period or design where sprinkler coverage is partial.

## 7. Common path of travel / dead-end limits (representative, verify against occupancy and adopted edition)

| Occupancy | Common path of travel (ft) | Dead-end corridor (ft) |
|---|---|---|
| Business, non-sprinklered | 75 | 20 |
| Business, sprinklered | 100 | 50 |
| Mercantile, sprinklered | 100 | 50 |
| Assembly, sprinklered | 75 | 20 |

## 8. Smoke control quick reference

**Stack effect neutral plane:** the building height at which inside and outside pressure are equal; above it, air flows out through openings (normal stack effect, cold outside), below it, air flows in. Location depends on the building's leakage distribution and the inside/outside temperature differential — model per project, don't reuse a value from a different building.

**Stairwell pressurization target (typical design range):** 0.05-0.10 in. w.c. differential across a closed stair door, with a maximum door-opening force commonly limited to 30 lbf per the applicable mechanical/fire code — verify the exact figures against the project's governing mechanical code and the AHJ.
