# Playbook

Filled worksheets a mason (or the foreman coordinating a crew) actually runs before laying, during cold-weather work, and when reviewing a submittal against code. Numbers below follow standard published methods (TMS 402/602, ASTM, BIA, NCMA) — a specific project's structural drawings, engineer of record, and local code amendment always govern over a worked example in this document.

## 1. Mortar type selection (ASTM C270)

| Type | Min. avg. compressive strength (28-day) | Typical application |
|---|---|---|
| M | 2,500 psi | Below grade, foundations, retaining walls, high lateral/soil load, masonry in contact with earth |
| S | 1,800 psi | Load-bearing walls needing higher flexural bond strength than N provides (e.g., higher wind/seismic exposure), exterior walls at/near grade |
| N | 750 psi | Exterior above-grade veneer, non-load-bearing walls, most general above-grade masonry — the default unless engineered otherwise |
| O | 350 psi | Interior non-load-bearing partitions, low-stress restoration/tuckpointing where matching an existing soft historic mortar matters more than strength |

**Selection rule:** start from the wall's structural role and exposure (load-bearing vs. veneer, above vs. below grade), not from "what's strongest." A mortar stiffer than the application needs reduces the assembly's ability to accommodate differential movement — that shows up as cracking years later, not on the day it's laid. Historic/soft masonry (pre-1900s, often lime-rich) gets matched to a compatible soft mortar (often Type O or a lime-only mix), never upgraded to Type M or S, or the harder mortar cracks the softer original units instead of the joint.

## 2. Veneer-tie spacing and count worksheet

**Rule:** maximum tributary area per tie is 2.667 sq ft (TMS 402); common spacing grids that satisfy it: 16 in vertical × 24 in horizontal (384 sq in = 2.667 sq ft), or tighter (e.g., 16 in × 16 in = 1.78 sq ft) where seismic design category or wind exposure calls for a denser grid.

**Formula:** columns = wall length ÷ horizontal spacing (round up); rows = wall height ÷ vertical spacing (round up); total ties = columns × rows; check actual area/tie = wall area ÷ total ties ≤ 2.667 sq ft.

**Filled example — 60 ft × 9 ft veneer wall, Seismic Design Category D (denser grid required, 16 in × 16 in spacing):**

| Metric | Calculation | Result |
|---|---|---|
| Wall area | 60 ft × 9 ft | 540 sq ft |
| Columns | 60 ft ÷ 1.333 ft, rounded up | 46 |
| Rows | 9 ft ÷ 1.333 ft, rounded up | 7 |
| Total ties | 46 × 7 | 322 |
| Actual area/tie | 540 ÷ 322 | 1.68 sq ft (under the 2.667 cap, appropriate for SDC D) |

## 3. Weep-hole spacing worksheet

**Rule:** open-head weep holes spaced at 24 in o.c. max (BIA Technical Note 21), immediately above continuous through-wall flashing, at the wall base and above every flashed interruption (shelf angle, lintel, sill). Wick/rope or tubed weeps can extend to roughly 16 in o.c. per the manufacturer's tested drainage rate — never assume wider spacing without a documented product spec.

**Formula:** weep count = (wall length in inches ÷ spacing) + 1 (one at each end).

**Filled example — 60 ft wall, open-head weeps at 24 in o.c.:**

| Metric | Calculation | Result |
|---|---|---|
| Wall length | 60 ft | 720 in |
| Weep holes | 720 ÷ 24, plus one at each end | 31 |

Repeat the same calculation independently above every shelf angle and lintel — a common miss is calculating weeps only at the base and forgetting the mid-height flashing lines that shelf angles create.

## 4. Control/expansion joint spacing worksheet

**Rule (brick veneer, BIA TN 18A):** max spacing ~25 ft between expansion joints; first joint within 10 ft of every outside corner regardless of the interior spacing pattern.

**Rule (CMU, NCMA TEK 10-2/10-3):** control joints at re-entrant corners, abrupt height changes, and both sides of openings wider than ~6 ft; field spacing typically capped at the lesser of ~25 ft or roughly 1.5–2× the wall height, tightened further where horizontal joint reinforcement is omitted.

**Filled example — 150 ft CMU wall, 12 ft tall, two window openings at 40 ft and 100 ft from the left corner:**

1. Mandatory joints at both sides of each opening (4 joints: ~38 ft, ~42 ft, ~98 ft, ~102 ft, assuming ~4 ft wide openings).
2. Check remaining spans against the 25 ft cap: corner-to-first-opening span (0–38 ft) = 38 ft, exceeds 25 ft → add one joint near the midpoint, e.g. at 19 ft, splitting it into 19 ft and 19 ft.
3. Opening-to-opening span (42–98 ft) = 56 ft, exceeds 25 ft → add two joints splitting it into three ~18.7 ft spans (e.g., at 61 ft and 80 ft).
4. Last opening to right corner (102–150 ft) = 48 ft, exceeds 25 ft → add one joint near the midpoint, e.g. at 126 ft, splitting it into 24 ft and 24 ft.
5. Result: 9 joints total (19, 38, 42, 61, 80, 98, 102, 126 ft, plus the right-corner span already under 25 ft), no span over 25 ft, every opening flanked.

## 5. Cold-weather masonry protection thresholds (MCAA / TMS 602 Article 1.8)

| Ambient temp trigger | Required protection |
|---|---|
| Below 40°F | Cover materials and completed masonry from rain/snow; sand/aggregate protected from freezing; no frozen/ice-coated units laid |
| Below 32°F | Heat mixing water (and/or sand) so mortar temperature at placement is 40–120°F; maintain mortar above freezing until initial set |
| Below 25°F | Heat both sand and mixing water; provide wind breaks; heat source maintained at the work area, not just at the mixer |
| Below 20°F | Full enclosure of the work area with auxiliary heat, masonry temperature maintained above 32°F for at least 24 hours (extend to 48 hours for high-lime or slow-set mixes) after laying |

**Cure-time note:** normal-weather mortar reaches workable early strength in 24–72 hours but continues gaining strength for weeks; any protection period above must not be shortened because the wall "looks set" at the surface — surface set and internal hydration are not the same clock.

## 6. IRA / suction test procedure (ASTM C67)

1. Select a representative unit from the delivered lot (not from stock left over from a prior job).
2. Mark a 1 in × 1 in (or scaled) test area on the bed face; weigh the dry unit.
3. Partially submerge the marked face in water 1/8 in deep for exactly 1 minute.
4. Remove, blot lightly, and reweigh; convert weight gain to a suction rate normalized to g/min per 30 sq in.
5. **Decision rule:** suction ≤ 30 g/min/30 in² — lay as-delivered. Suction > 30 g/min/30 in² — pre-wet the units 3–24 hours before laying so the surface is damp, not glistening, at the time of laying (glistening/wet-shine units get set aside further to surface-dry first).

## 7. Freeze-thaw grade selection (ASTM C216)

| Grade | Max. saturation coefficient | Min. freeze-thaw cycles (25-cycle test) | Use |
|---|---|---|---|
| SW (Severe Weathering) | 0.78 (or 0.80 with min. compressive strength met) | 50 cycles, ≤0.5% loss | Below grade, in contact with earth, or any region on BIA's Severe Weathering index — most of the northern half of the US |
| MW (Moderate Weathering) | 0.88 | 18 cycles | Above grade in Moderate Weathering regions, protected from saturation |
| NW (Negligible Weathering) | no limit | not required | Interior use or Negligible Weathering regions only — never specify for an exterior wall in an SW/MW region regardless of appearance match |

**Selection rule:** pull the project location's weathering index from the BIA map (or local building department reference) before accepting a brick submittal on appearance and size alone; grade mismatch is the single most common way a spalling failure gets built into a submittal review that never checked it.
