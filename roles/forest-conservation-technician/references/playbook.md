# Playbook

Filled worksheets and protocol tables for the tasks this role executes most often: BAF prism cruising with borderline-call resolution, fixed-radius plot layout, DBH measurement by stem condition, slope correction, and fuel-load transects.

## 1. Plot-radius (limiting distance) factors by basal-area factor (BAF)

Point sampling: a tree is "in" if its horizontal distance from plot center is less than or equal to its limiting distance, where `limiting distance (ft) = DBH (inches) × plot-radius factor`.

| BAF (ft²/acre per tree) | Plot-radius factor | Typical use case |
|---|---|---|
| 5 | 3.88 | Old-growth or widely-spaced stands, low tree count per point |
| 10 | 2.75 | General-purpose cruise, most even-aged pine/hardwood stands |
| 20 | 1.94 | Dense young stands, where BAF 10 would give too many trees per point |
| 40 | 1.37 | Very dense sapling/pole stands or quick reconnaissance cruise |

**Borderline-call check, worked:** BAF 10, tree DBH = 14.2 in. Limiting distance = 14.2 × 2.75 = 39.05 ft. Measure actual horizontal distance with tape or rangefinder; if ≤ 39.05 ft, the tree is IN; if greater, OUT. Never resolve a borderline call by a second look through the prism from the same point — remeasure distance and diameter instead.

**Stand basal area per acre** = mean of (in-tree count × BAF) across all plot points. Volume per acre is then read from a local volume table keyed to basal area and average stand height, or computed tree-by-tree from a volume equation — not estimated directly from basal area alone.

## 2. Slope correction table

Horizontal distance = slope distance × cos(slope angle). Use whenever slope exceeds ~10% and the instrument doesn't already output horizontal distance.

| Slope (%) | Slope angle (≈) | Correction factor (cos θ) | Effect on a 40 ft slope-distance reading |
|---|---|---|---|
| 5% | 2.9° | 0.999 | 40.0 ft → 40.0 ft (negligible) |
| 10% | 5.7° | 0.995 | 40.0 ft → 39.8 ft |
| 25% | 14.0° | 0.970 | 40.0 ft → 38.8 ft |
| 40% | 21.8° | 0.928 | 40.0 ft → 37.1 ft |
| 60% | 31.0° | 0.857 | 40.0 ft → 34.3 ft |

**Rule applied:** at 25% slope, a slope-distance reading of 40.7 ft corrects to 40.7 × 0.970 = 39.5 ft horizontal — the number that actually matters for a limiting-distance or plot-boundary call, not the tape reading itself.

## 3. Fixed-radius plot dimensions (FIA-style design)

Used for permanent inventory plots and for stands where point sampling is a poor fit (very small or very sparse diameter distribution).

| Plot element | Radius | Area | Trees tallied |
|---|---|---|---|
| Subplot | 24.0 ft | 1/24 acre (0.0417 ac) | Trees ≥ 5.0 in DBH |
| Microplot | 6.8 ft | 1/300 acre (0.0033 ac) | Saplings/seedlings 1.0–4.9 in DBH |
| Full plot (4 subplots) | — | 1/6 acre (0.1667 ac) total | Standard FIA cluster: 1 center + 3 subplots at 120 ft and 120° azimuth spacing |

**Breakpoint rule:** a stem at exactly 5.0 in DBH is tallied on the subplot, not the microplot — the breakpoint diameter belongs to the larger plot's protocol.

## 4. DBH measurement point by stem condition

| Stem condition | Measurement point |
|---|---|
| Normal, upright stem on level ground | 4.5 ft vertical height from ground, uphill side not applicable |
| Stem on a slope | 4.5 ft measured along the uphill side of the stem |
| Leaning stem | 4.5 ft measured along the bole's axis (not vertically from the ground) |
| Forked below 4.5 ft | Tally as two separate stems, each measured at 4.5 ft on its own axis |
| Forked at or above 4.5 ft | Tally as one stem, measured below the fork at the standard point |
| Butt swell, burl, or visible damage at 4.5 ft | Measure at the nearest point above the irregularity where the stem returns to normal form, and note the offset height |

**Remeasurement rule:** always use the same measurement point recorded on the plot's prior visit card, even if a different point would technically be "more correct" this cycle — consistency with the historical record matters more than re-optimizing the call.

## 5. Brown's planar-intersect fuel-load transect worksheet

Standard transect length: 50 ft (can vary by fuel-load protocol; confirm against the specific monitoring plan). Tally by size class along the transect line.

| Fuel size class | Diameter range | Count method |
|---|---|---|
| 1-hr | < 0.25 in | Count all pieces crossing first 6 ft of transect |
| 10-hr | 0.25–1.0 in | Count all pieces crossing first 6 ft of transect |
| 100-hr | 1.0–3.0 in | Count all pieces crossing full transect length |
| 1000-hr | > 3.0 in | Count all pieces crossing full transect length, record diameter and decay class (sound/rotten) individually |

**Recording requirement:** transect azimuth, slope, and total length are logged with every count — a fuel-load figure without the transect's slope correction and orientation on file can't be reproduced or QA'd later.

## 6. Field QA checklist (run before leaving the plot, or at latest same day)

1. Every tree/tally number is sequential with no duplicates within the plot.
2. Every borderline prism call has a tape-and-distance check recorded, not just a tally mark.
3. DBH deltas against the prior-cycle card are within expected growth range; anything negative or implausibly large is flagged with a note, not silently accepted or silently corrected.
4. GPS accuracy/PDOP or witness-tree relocation method is logged for the plot, not just a coordinate pair.
5. Slope was read and, if >10%, the correction factor applied is recorded alongside the raw slope-distance readings (not just the corrected number) so a reviewer can re-derive it.
