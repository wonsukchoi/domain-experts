# Playbook

Filled walkthroughs for the four places this trade gets shortcut: trench-protection selection, bedding class by pipe material, slope/velocity by diameter, and water/sewer separation. Numbers are worked examples to adapt, not universal constants — always check the project's geotechnical report, adopted code, and the pipe manufacturer's own chart.

## 1. Trench-protection selection (OSHA 29 CFR 1926 Subpart P)

**Soil classification (Appendix A), illustrative field indicators:**

| Type | Description | Max allowable slope |
|---|---|---|
| A | Cohesive clay, unfissured, unsaturated, no prior disturbance | 3/4:1 (53°) |
| B | Cohesive but fissured, or granular cohesionless (angular gravel) | 1:1 (45°) |
| C | Granular soil (gravel, sand, loamy sand), submerged or seeping, or previously disturbed | 1.5:1 (34°) |

**Protective-system trigger:** any trench 5 ft deep or greater requires a protective system (sloping/benching, shoring, or shielding) unless the excavation is entirely in stable rock; trenches 20 ft deep or greater require a system designed by a registered professional engineer. A competent person classifies the soil and inspects the trench daily and after any rain, groundwater change, or other condition that could affect stability.

**Worked example:** A trench for the 8 in. sewer reaches 7.5 ft at its deepest station. Soil is classified Type B (cohesive, some fissuring, no groundwater observed). At Type B, sloping to 1:1 would require benching back 7.5 ft horizontally per side of trench at that depth — impractical in a narrow utility corridor — so an aluminum trench box rated for the depth and soil type is used instead, with the box's manufacturer load rating checked against the Type B soil pressure at 7.5 ft.

**Other Subpart P triggers to check regardless of protective system:** spoil piles and equipment kept at least 2 ft back from the trench edge; a ladder, ramp, or other egress within 25 ft of lateral travel for any worker in a trench 4 ft deep or greater; atmospheric testing before entry on trenches with a potential for hazardous atmosphere (confined-space-adjacent conditions near sewer connections).

## 2. Bedding class by pipe material (ASTM D2321 framework, flexible pipe; separate load-chart approach for rigid pipe)

**Bedding classes for flexible pipe (PVC, HDPE) per ASTM D2321:**

| Class | Bedding material | Typical use |
|---|---|---|
| Class IA | Manufactured angular, open-graded stone (e.g., crushed stone, no fines) | Poor native soil, high groundwater, or where maximum support is specified |
| Class IB | Crushed stone or gravel with some fines | Common default for sewer/storm PVC in average soil |
| Class II | Coarse sand, gravel with some fines, native granular soil meeting gradation | Acceptable native-soil bedding where gradation qualifies |
| Class III | Fine sand or silty sand | Lower-load, shallow-cover, non-traffic applications only |

**Compaction targets by zone (worked defaults — confirm against project spec):**

| Zone | Target (% standard Proctor, ASTM D698) | Lift thickness |
|---|---|---|
| Bedding (below pipe) | 90% | 4–6 in. |
| Haunch (pipe springline down to bedding) | 90–95% | 4–6 in., hand or mechanical tamped, no direct impact on pipe |
| Initial backfill (to 12 in. over crown) | 85–90% | 6–8 in. |
| Final backfill (to surface, non-traffic) | 85% | 8–12 in. |
| Final backfill under pavement/traffic | 95% (modified Proctor, ASTM D1557, per pavement design) | 6–8 in. |

**Rigid pipe (ductile iron, reinforced concrete) bedding note:** rigid pipe resists crushing load primarily through wall strength (D-load rating, ASTM C76 three-edge-bearing test for RCP; wall thickness class per AWWA C150/C151 for ductile iron), so it tolerates a lower-support bedding class than flexible pipe at the same depth — but still requires uniform bearing along the barrel to avoid point loading at bell-and-spigot joints. Using a flexible-pipe Class IA spec on a rigid-pipe run isn't wrong, just unnecessary cost; using a rigid-pipe-adequate bedding under flexible pipe under-supports it and risks exceeding the 5% ring-deflection limit.

**Worked haunch-compaction example:** 8 in. PVC, Class II bedding, native soil meets gradation. Haunch compacted in two 4 in. lifts (springline is 4 in. above pipe invert for 8 in. pipe) to 92% standard Proctor, verified by nuclear density gauge at two points per 100 ft of run — density readings below 88% at any test point trigger re-excavation and recompaction of that section before the next lift proceeds.

## 3. Slope and velocity by diameter (Manning's equation, n = 0.013 for PVC/smooth-wall pipe)

**Minimum slope by diameter (illustrative baseline targeting ~2 fps self-cleansing velocity at full flow — confirm against the adopted local standard):**

| Diameter | Minimum slope | Minimum slope (in./ft equivalent) |
|---|---|---|
| 4 in. | 1.00% | ~1/8 in./ft (commonly rounded to 1/4 in./ft in older codes) |
| 6 in. | 0.60% | ~3/4 in./10 ft |
| 8 in. | 0.40% | ~5/8 in./10 ft |
| 10 in. | 0.28% | ~1/3 in./10 ft |
| 12 in. | 0.22% | — |
| 15 in. | 0.15% | — |
| 18 in. | 0.12% | — |
| 24 in. | 0.08% | — |

**Velocity check formula (US customary):** V = (1.486/n) × R^(2/3) × S^(1/2), where R is hydraulic radius (D/4 at full flow for a circular pipe) and S is slope as a decimal.

**Worked example (8 in. pipe, full flow, n = 0.013, R = 0.167 ft):**
- At S = 0.0040 (0.40%, the code minimum): V = 114.3 × 0.303 × 0.0632 ≈ **2.19 fps** — meets the ~2 fps self-cleansing target.
- At S = 0.0015 (0.15%, a mis-graded run): V ≈ 114.3 × 0.303 × 0.0387 ≈ **1.34 fps** — below target; solids settle over time even though the pipe still conveys clear water today.

**Maximum velocity ceiling:** commonly capped around 10 fps for rigid pipe (lower for some jointed or thin-wall pipe per manufacturer data) to limit scour and joint erosion, especially approaching a manhole drop — a steep reach engineered for slope adequacy alone without this check can erode joints and invert channels over years of service even though it never backs up.

## 4. Water/sewer separation (Ten States Standards framework)

**Standard separation:**

| Condition | Requirement |
|---|---|
| Parallel water main and sewer | 10 ft horizontal, edge to edge |
| Crossing, standard case | 18 in. vertical clearance, water main above sewer |
| Parallel run, cannot achieve 10 ft | Water main in separate trench, or on undisturbed shelf, with main's bottom at least 18 in. above sewer's top |
| Crossing, cannot achieve 18 in. vertical | Use pressure-rated pipe (water-main-grade material) for the sewer, centered on the crossing for at least 10 ft each side, or full encasement |

**Worked example:** New 8 in. sewer runs parallel to an existing 8 in. water main for 120 ft, then crosses it once near station 1+50. Design horizontal separation along the parallel section measures 11 ft — meets the 10 ft minimum, no special material required. At the single crossing, water-main invert is surveyed 2.1 ft above the sewer's crown — exceeds the 18 in. (1.5 ft) minimum vertical clearance with water above sewer, so the crossing needs no pressure-pipe substitution or encasement. Had the vertical clearance measured only 1.0 ft, the fallback would require either lowering the sewer, raising the water main, or installing a length of pressure-rated pipe (e.g., ductile iron or C900 PVC) centered on the crossing.

**Rule:** check separation at design time against the actual surveyed alignment and elevations, not the plan's nominal corridor spacing — utility conflicts discovered only at trench-opening force a redesign under time pressure that a pre-construction overlay check would have caught for free.
