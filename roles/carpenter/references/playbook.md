# Playbook

Filled procedures for the four situations that generate the most callbacks and failed inspections: bearing-wall header sizing, moisture-content field checks, stair layout, and engineered-lumber field modification. Numbers are worked, not illustrative placeholders — recompute for the actual species/grade/load in front of you.

## 1. Bearing-wall header check — three-part sequence

Run all three checks. A header that clears bending can still fail bearing; a header that clears both can still fail deflection on a long span with a stiff finish (tile, plaster) below it.

**Step 1 — establish the load.** Tributary width (ft) × combined load (psf) = load on the wall (plf). Combined load = live load + dead load for the use above (residential floor: 40 psf live + 10 psf dead = 50 psf combined; habitable attic: 30 psf live + 10 psf dead; non-habitable attic with storage: 20 psf live + 10 psf dead — pull the actual occupancy's live-load value, don't default to 40).

**Step 2 — bending.** M = wL²/8 (w in plf, L in ft, M in lb-ft). Compare to allowable moment = Fb (psi, from NDS Supplement Table 4A for the species/grade) × section modulus S (in³), converted to lb-ft.

| Species/grade (No. 2) | Fb (psi) | Fc⊥ (psi) | E (psi) |
|---|---|---|---|
| Douglas Fir-Larch | 875–900 | 625 | 1,600,000 |
| Southern Pine | 1,000–1,100 | 565 | 1,400,000 |
| Hem-Fir | 850–875 | 405 | 1,300,000 |
| Spruce-Pine-Fir | 700–850 | 425 | 1,200,000 |
| LVL, 1.9E grade | ~2,600 | ~750 | 1,900,000 |

**Step 3 — deflection.** Δ = 5wL⁴ ÷ (384EI), w converted to lb/in, L in inches. Compare to L/360 (floors, finished ceilings) or L/240 (unfinished/roof-only). A member that passes bending by a wide margin (as engineered lumber typically does versus dimensional) usually isn't deflection-limited either — recompute rather than assume.

**Step 4 — bearing at the ends.** Reaction (lb) = total load W ÷ 2 for a uniformly loaded, simply supported span. Bearing stress = reaction ÷ (jack-stud width × header width, in²). Compare to Fc⊥. If it fails, double (or triple) the jack studs rather than resizing the header — bearing area scales with stud count, not header depth.

**Example, filled:** 600 plf, 8-ft span, SPF No. 2 header candidate (double 2x10, before switching to LVL): M = 600×8²/8 = 4,800 lb-ft. S doubled 2x10 = 42.8 in³. Allowable M = 700 × 42.8 ÷ 12 = 2,497 lb-ft. Demand exceeds allowable by 92% — fails harder than the DF-L case in SKILL.md's worked example, because SPF's Fb is lower still. This is the reason "double 2x10" as a blanket habit is dangerous: the same nominal header fails by a different margin depending on which species actually showed up on the truck.

## 2. Moisture-content field protocol

**When to check:** on delivery, again after any weather exposure before enclosure, and always at the pre-drywall walk — not just once.

**Where to check:** rim joist (often the wettest member, least ventilated), studs at 3 ft height on at least two exterior walls, and any lumber that was rained on during framing. A single reading at a top plate understates a wet rim joist by a wide margin.

**Reading bands:**

| Reading | Status | Action |
|---|---|---|
| ≤ 15% | Professional target — dry-in ready | Proceed to enclose |
| 16–18% | Code-legal, ENERGY STAR caution range | Wait if schedule allows; if not, document the reading and the decision to proceed |
| 19% | IRC legal ceiling | Last acceptable reading — do not round up from 19.x% |
| > 19% | Code violation | Do not enclose; force-dry (fans, dehumidification, time) and recheck |

**Instrument note:** use a pin-type meter with insulated pins driven to the member's core, not a surface/pinless meter reading through a dry outer layer over a wet core — pinless meters can understate core moisture by several points on thick or recently-wetted members.

## 3. Stair stringer layout — worked arithmetic

**Given:** total floor-to-floor rise = 108 in (9 ft).

1. Pick a target unit rise near 7 in (comfortable range, well under the 7.75 in code max). 108 ÷ 7 = 15.4 → round to a whole number of risers: **15 risers**.
2. Recompute actual unit rise: 108 ÷ 15 = **7.2 in** — under the 7.75 in max, and every riser in the flight is identical by construction (satisfies the 3/8 in max-variance rule automatically, since there's one computed value, not 15 separately-cut ones).
3. Number of treads = risers − 1 = **14 treads** (the top tread is the floor above).
4. Pick unit run ≥ 10 in code minimum; if treads are solid risers with nosing, run can be 9 in with a 3/4–1-1/4 in nosing per tread — confirm which condition applies before cutting stringers, since the two produce different stringer layouts.
5. Verify headroom: measure from the nosing line to the ceiling/header above at every point along the stair's slope, not just at the top — code minimum is 80 in (6 ft-8 in), and headers or ductwork mid-run are the usual violation point.
6. Verify handrail height 34–38 in above the nosing line, and guard height 34 in minimum along the open side of the stair (36 in at landings, per the adopted edition — confirm the local amendment).

**Cut the first stringer, hold it against the actual rough opening, and check rise/run/headroom directly before cutting the rest** — a layout error caught on stringer one costs one board; caught on stringer four costs the set.

## 4. Rough-opening tolerance — worked check

**Given:** a 3068 exterior door unit; manufacturer spec sheet calls for a rough opening of 38" wide × 82" tall (confirm against the specific unit — this varies by manufacturer and is not a fixed add-2-inches rule).

1. Frame to 38" × 82".
2. Compute the expected diagonal: √(38² + 82²) = √(1,444 + 6,724) = √8,168 ≈ **90.4 in**.
3. Measure both actual diagonals (corner to corner, both directions).
4. If the two measured diagonals differ from each other by more than **1/4 in**, the opening is out of square — rack the frame square before setting the unit, don't rely on shims to absorb it. Shims correct minor gaps; they don't correct a racked frame, and a door set into a racked opening will bind or fail to latch within a season.

**Window rough openings:** always pull the manufacturer's spec sheet number for the specific unit and series — vinyl, wood, and clad units from different manufacturers use different frame-thickness assumptions, and a generic "unit size + 2 inches" rule produces an opening that's wrong in either direction depending on which unit actually gets installed.

## 5. Engineered-lumber field modification — decision order

Follow this order; do not skip to a later step because the manufacturer's literature isn't on hand.

1. **Pull the manufacturer's span and hole chart for the specific product line and depth** (e.g., a 9-1/2" TJI 210 has a different hole chart than an 11-7/8" TJI 560). Generic "I-joist" rules don't exist — every manufacturer publishes its own.
2. **Never cut, notch, or drill the flanges**, top or bottom, under any circumstance the chart doesn't explicitly show — flanges carry the bending load an I-joist is designed around.
3. **Holes in the web** are permitted only within the size, location (distance from bearing), and spacing limits the chart specifies — round holes only unless the chart shows otherwise, and never overlapping holes closer than the chart's minimum spacing.
4. **For LVL, avoid notching entirely except at bearing ends**, and only up to 1/10 of the member's depth there — tension-side notching mid-span is not a permitted field modification.
5. **Where a point load (post, beam, girder truss) lands on the floor system, install a squash block before the subfloor goes down** — retrofitting one after sheathing is installed means pulling sheathing back, which is why this step gets skipped and why it needs to be checked at framing, not at trim-out.
6. **If the chart doesn't cover the specific condition in front of you, call the manufacturer's technical line before cutting** — engineered lumber technical support is free and faster than an engineering fix after the cut is made. Freehand judgment calibrated on dimensional lumber does not transfer to engineered products.
