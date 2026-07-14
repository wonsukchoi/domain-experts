# Resilient Floor Installer Playbook

Filled protocols and tables for the jobs referenced in SKILL.md. Thresholds are the stated defaults from ASTM test methods, RFCI work practices, and common adhesive/manufacturer data sheets; a specific product's own spec sheet always overrides these when it states its own tolerance.

## Legacy-material testing and disposition sequence

1. Determine the flooring's installation era from building records or prior renovation history. Pre-1980, or unknown, triggers presumed-ACM status for both the surface material and any adhesive layer under it.
2. Pull bulk samples per EPA/AHERA protocol: minimum 3 samples per homogeneous material type (e.g., one sample set for the tile, a separate set for the mastic) for areas under 1,000 sq ft; add samples for larger or visually distinct areas.
3. Do not dry-scrape, sand, grind, or drill any sampled material before results return.
4. On a positive result, run a bond-pull test (ASTM D4541-style adhesion test or a simple pry-and-measure field pull) and a flatness check (straightedge per ASTM F710) on the confirmed layer.

**Disposition table:**

| Bond test | Flatness | Disposition |
|---|---|---|
| Fully adhered, no delamination | Within ASTM F710 tolerance | Encapsulate in place (prime + skim-coat) per RFCI work practices |
| Fully adhered, no delamination | Fails tolerance | Encapsulate, then self-level over the encapsulated layer |
| Any delamination, lifting, or cracking | Either | Licensed abatement removal required — encapsulation is not valid over an unstable layer |
| Spec requires full removal regardless of condition (e.g., radiant heat retrofit under the layer) | Either | Licensed abatement removal required |

**Example — 2,400 sq ft office, 1975 construction (see SKILL.md worked example for full cost detail):**
- Tile: negative. Mastic: positive at 2% chrysotile, Category I nonfriable.
- Bond-pull: fully adhered. Flatness: within tolerance.
- Disposition: encapsulate in place, $1.75/sq ft × 2,400 = $4,200, vs. $6.25/sq ft × 2,400 = $15,000 for full removal.

## Moisture, alkalinity, and flatness test protocol

**Test count by area (ASTM F1869 calcium chloride):**

| Area | Minimum test locations |
|---|---|
| First 1,000 sq ft | 3 |
| Each additional 1,000 sq ft (or fraction) | +1 |
| Example: 2,400 sq ft | 3 + 2 = 5 |

- Condition the space to normal service temperature/humidity for 48 hours before testing.
- Dome sits 60-72 hours; result reported in lbs MVER/1,000 ft²/24hr.
- Run ASTM F2170 RH probes alongside CaCl when the adhesive spec cites an RH limit — drill to 40% of slab depth, equilibrate a minimum of 24 hours before reading.
- pH: wet the slab surface with distilled water, press a pH strip or meter probe to the wetted spot, read after 60-90 seconds. Test at minimum 3 locations per 1,000 sq ft, same as CaCl.

**Adhesive/mitigation selection by reading (typical thresholds — verify against the specific product sheet):**

| MVER (lbs/1,000ft²/24hr) | RH (%) | pH | Selection |
|---|---|---|---|
| ≤ 3 | ≤ 75% | 7-9 | Standard resilient adhesive |
| 3-8 | 75-85% | 9-10 | Moisture-tolerant adhesive or pH-tolerant primer, per which test failed |
| > 8 | > 85% | > 10 | Full moisture-mitigation system (epoxy or urethane MVB) before any adhesive |

- A reading at a threshold boundary gets treated as the higher tier — over-mitigating one tier costs far less than a callback under warranty.
- Document every reading with location, date, and technician; this is the only record if a warranty claim comes later.

**Flatness (ASTM F710):** no more than 3/16 in. deviation in 10 ft, no abrupt change greater than 1/32 in. Check with a 10-ft straightedge across multiple directions in every room; mark and self-level any area outside tolerance rather than patching only the deepest point.

## Heat-welded sheet vinyl seam spec

1. Butt-seam the sheet edges with a slight overlap, then double-cut through both layers with a seam cutter guided by a straightedge for a tight, matched joint.
2. Groove the seam with a hand or powered groover to roughly two-thirds of the material's gauge (e.g., ~0.05-0.06 in. deep on a 0.080 in. gauge sheet) — deep enough for the weld rod to seat, shallow enough not to cut through to the substrate.
3. Set the hot-air welder to the material's rated range (commonly ~750°F tip temperature for homogeneous PVC sheet; consult the manufacturer's chart for heterogeneous or rubber sheet, which run cooler).
4. Feed the weld rod into the groove at a steady walking pace, keeping the shoe seated in the groove so the rod fuses to both sheet edges without scorching.
5. Rough-trim the excess bead while still warm and pliable, using a hook-blade trimmer skimmed just above the surface.
6. Let the weld cool 30-60 minutes, then finish-trim flush with a flush trimmer for a seam that reads level under raking light.

## Floating LVT/LVP installation sequence

1. Acclimate material on-site, in the room it will be installed, for a minimum of 48 hours at the room's expected service temperature (typically 65-85°F) and humidity — unless the manufacturer's data sheet states a longer period.
2. Inspect and correct the substrate to the manufacturer's flatness tolerance (commonly the same 3/16 in. per 10 ft used for glue-down; some floating systems tolerate a looser spec — check the product sheet).
3. Roll out underlayment (if not pre-attached to the plank) with seams taped, not overlapped.
4. Begin the first row against a straight reference line, leaving a 1/4-3/8 in. perimeter expansion gap at every fixed vertical surface (walls, cabinetry, built-ins) — cover with base/quarter-round, not caulked solid.
5. Stagger end joints a minimum of 6-8 in. between adjacent rows (or per the manufacturer's stagger spec) to distribute load and avoid a repeating seam line.
6. For runs exceeding roughly 40-50 linear ft in any direction, or crossing between rooms with different HVAC zones, install a T-molding or expansion transition rather than running the floor as one continuous plane.
7. Leave the same expansion gap around any vertical penetration (pipes, columns) and at every doorway transition.

**Example — 900 sq ft open floor plan, two rooms connected by a 6-ft-wide opening:**
- Acclimate 48 hrs, confirm substrate flatness.
- Install as one continuous field with a 1/4 in. perimeter gap at all outer walls.
- Because the combined run exceeds 50 ft along the long axis, place a T-molding transition at the doorway opening between the two rooms rather than carrying one uninterrupted field across both.
</content>
