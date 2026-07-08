# Playbook

Filled formulas, thresholds, and workflows an architectural/civil drafter runs against. Verify against the project's specific CAD standard and the AHJ's submittal requirements — these are commonly applied national-standard patterns, not a substitute for a project-specific standard in front of you.

## 1. Scale factor computation

**Architectural (inch-based model space): scale factor = 12 ÷ (scale fraction in inches per foot).**

| Architectural scale | Scale factor (SF) |
|---|---|
| 1/8" = 1'-0" | 96 |
| 3/16" = 1'-0" | 64 |
| 1/4" = 1'-0" | 48 |
| 3/8" = 1'-0" | 32 |
| 1/2" = 1'-0" | 24 |
| 1" = 1'-0" | 12 |

*Example: 1/4" = 1'-0" → 12 ÷ 0.25 = 48. A viewport at this scale set to 1:48 means 1 model-space inch plots at 1/48 of a real inch.*

**Civil (foot-based model space): scale factor = the feet value stated directly, no inch conversion.**

| Civil scale | Scale factor (SF) |
|---|---|
| 1" = 10' | 10 |
| 1" = 20' | 20 |
| 1" = 30' | 30 |
| 1" = 50' | 50 |
| 1" = 100' | 100 |

*Example: 1" = 20' → SF = 20, not 240. Civil model space is drawn in real-world feet (1 drawing unit = 1 foot), so the conversion that architectural drafting needs (feet to inches, ÷ scale fraction) doesn't apply — applying the architectural formula to a civil scale overscales the viewport by 12x.*

**Rule:** before setting any viewport, confirm the file's `INSUNITS` (or equivalent) setting matches the discipline convention in use. A combined arch/civil sheet set with an architectural background xrefed into a civil sheet (or vice versa) needs an explicit unit-conversion block in the xref insertion, not a matching scale factor.

## 2. Annotation recompute after a scale change

| Element | Plotted target (common NCS convention) | Model-space value = target x SF |
|---|---|---|
| General note text | 3/32" (0.09375") | 0.09375 x SF |
| Dimension text | 3/32" (0.09375") | 0.09375 x SF |
| Dimension tick/arrow | 1/8" (0.125") | 0.125 x SF |
| Title/sheet-name text | 1/4" (0.25") | 0.25 x SF |

*Example: scale factor moves from 48 to 64 (see SKILL.md worked example). General note text: 0.09375 x 48 = 4.5" → 0.09375 x 64 = 6.0". Ratio 64/48 = 1.333 applies uniformly to every scale-dependent value on the sheet, including hatch pattern scale and linetype scale.*

**Rule:** a scale change is never geometry-only — every annotation object whose height/size was set from the old scale factor has to be recomputed by the same ratio, or it plots at the wrong scale on an otherwise-correct sheet.

## 3. Sheet layout fit check

**Usable drawing area = sheet size − border margins − title block width/height.**

*Example (ARCH D, 36" x 24", 0.5" border all sides, 2" right-side title block): usable width = 36 − 0.5 − 0.5 − 2 = 33.0". Usable height = 24 − 0.5 − 0.5 = 23.0".*

| Sheet size | Dimensions | Common usable area (0.5" border, 2" title block strip) |
|---|---|---|
| ARCH C | 24" x 18" | 21.0" x 17.0" |
| ARCH D | 36" x 24" | 33.0" x 23.0" |
| ARCH E | 48" x 36" | 45.0" x 35.0" |

**Rule:** a footprint that exactly equals the usable area at a given scale does not fit — budget a minimum of 4"-8" of clearance beyond the raw geometry for dimension strings, keyed notes, and a north arrow/key plan before accepting a scale. If it doesn't clear with margin, drop to the next standard scale increment and recompute per Section 2.

## 4. NCS sheet numbering (discipline-sheet type-sequence)

| Discipline designator | Discipline | Sheet type digit (first digit after dash) | Example |
|---|---|---|---|
| G | General | 0 = general | G-001 |
| C | Civil | 1 = plans, 2 = site/grading, 5 = details | C-101 (site plan), C-201 (grading plan), C-501 (details) |
| A | Architectural | 1 = plans, 2 = elevations/sections, 5 = details | A-101 (floor plan), A-201 (exterior elevations), A-501 (wall sections/details) |
| S | Structural | 1 = plans, 2 = sections, 5 = details | S-101 (foundation plan) |
| M/E/P | Mechanical/Electrical/Plumbing | per NCS discipline sub-designator | M-101, E-101, P-101 |

*Example: a 3-story office building's floor plans sheet-number as A-101 (Level 1), A-102 (Level 2), A-103 (Level 3), A-201 (exterior elevations), A-501–A-503 (wall section details) — sequence number increments within the same sheet-type digit, never restarts per level unless the project standard says otherwise.*

**Rule:** confirm which NCS version and which sheet-type digit convention the project's specific CAD standard has adopted before assigning numbers — the discipline designator letter is stable across NCS versions, but sheet-type digit groupings have shifted between versions.

## 5. AIA/NCS layer naming (Discipline-Major-Minor-Status)

**Format: `<Discipline>-<Major>-<Minor>-<Status>`**

| Example layer | Discipline | Major | Minor | Status |
|---|---|---|---|---|
| `A-WALL-FULL-N` | Architectural | Wall | Full-height | New |
| `A-WALL-FULL-E` | Architectural | Wall | Full-height | Existing |
| `A-WALL-FULL-D` | Architectural | Wall | Full-height | Demolished |
| `A-DOOR` | Architectural | Door | (none) | (current phase implied) |
| `C-ROAD-CNTR` | Civil | Road | Centerline | (current phase implied) |
| `C-TOPO-EXST` | Civil | Topography | Existing | (redundant with minor, common variant) |

**Status suffix codes:** N = new, E = existing to remain, D = to be demolished/removed, F = future (not in this contract).

**Rule:** a layer's status suffix drives downstream takeoff and cost software filtering — drafting an existing-to-remain element on a `-N` layer prices it as new work. Verify status suffix against the redline's phasing call-out before drafting, not after.

## 6. Civil stationing and vertical datum

**Stationing format: `##+##.##`, read as (station number x 100) + offset in feet** from a defined point of beginning (POB) along an alignment.

*Example: a POB at Sta. 0+00.00, a curve point of tangency at Sta. 4+52.30, is 452.30 ft along the alignment from the POB. A station equation (e.g., "Sta. 12+50.00 Back = Sta. 12+65.15 Ahead") notes a 15.15 ft discontinuity where two alignment surveys were spliced — omitting the equation note makes the alignment appear 15.15 ft shorter or longer than it is.*

**Vertical datum:** civil elevations reference either NGVD29 (older) or NAVD88 (current US standard); the two differ by a location-dependent offset that is not a fixed national constant (it varies roughly 0-1.5 ft across the contiguous US per NGS conversion data).

**Rule:** every benchmark or spot elevation on a civil sheet states its datum explicitly. Two surveys of the same site referencing different datums without a stated offset will appear to disagree even when both are individually correct — reconcile via the NGS datum conversion tool before comparing, never by eye.

## 7. Cut/fill and contour interval sanity check

**Contour interval convention: 1 ft for sites with less than ~10 ft of relief across the parcel, 2 ft for moderate relief, 5 ft for steep/mountainous sites** — a stated heuristic, verify against the project's specific civil standard.

*Example: existing topo survey shows 1 ft contour interval; the grading plan drafted from it uses a 2 ft interval. Comparing the two directly will show apparent "missing" contours that are actually just a coarser interval — not a data error. Flag interval mismatches between an existing-conditions survey and a proposed grading plan before running a cut/fill volume, since a coarse-interval TIN surface understates volume precision.*

**Rule:** cut/fill volumes computed from mismatched contour intervals (existing survey vs. proposed grading) are only as precise as the coarser of the two — note the precision limitation on the grading plan rather than reporting a volume to false precision.

## 8. Plot style (CTB/STB) color-to-lineweight mapping

| AutoCAD color number | Common firm-standard use | Lineweight (mm) |
|---|---|---|
| 1 (red) | Wall cut lines, heavy object lines | 0.50 |
| 2 (yellow) | Hatch/poché, fine fills | 0.25 |
| 3 (green) | Dimension lines/text | 0.25 |
| 5 (blue) | Xref/reference geometry | 0.18 |
| 7 (white/black) | General linework, default | 0.35 |

*Example: reassigning wall cut geometry from color 2 (0.25 mm) to color 1 (0.50 mm) doubles the plotted line weight without touching a single object's override — the fix lives in the CTB file, applied on next plot.*

**Rule:** lineweight is controlled by color-to-CTB/STB mapping, not by per-object override — a firm-wide weight change is a one-file edit; hunting down individual object overrides means the change never fully lands.
