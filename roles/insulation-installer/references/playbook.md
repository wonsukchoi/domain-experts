# Insulation Installer Playbook

Filled tables and sequences for the jobs referenced in SKILL.md. Figures are stated defaults from IECC tables, NAIMA/CIMA/SPFA manufacturer data, and the FTC R-Value Rule's coverage-chart requirement; a specific product's own bag or data sheet always overrides these when it states its own value, and the locally adopted code edition always governs over the generic figures below.

## Climate-zone R-value and air-leakage targets (IECC-style, approximate — verify against the locally adopted edition)

| Climate zone | Attic/ceiling R | Wall cavity R (2x4 / 2x6) | Floor over unconditioned space R | Blower-door target (ACH50) |
|---|---|---|---|---|
| 1-2 | R-30 | R-13 / R-20 | R-13 | ≤ 5 |
| 3 | R-38 | R-13 / R-20 | R-19 | ≤ 5 |
| 4 (not marine) | R-49 | R-13+5 or R-20 | R-19 | ≤ 5 |
| 4 marine, 5 | R-49 | R-20 or R-13+5 | R-30 | ≤ 3 |
| 6 | R-49 | R-20+5 or R-13+10 | R-30 | ≤ 3 |
| 7-8 | R-60 | R-20+5 or R-13+10 | R-38 | ≤ 3 |

**Reading the table:** the wall column's "+N" figure is continuous exterior insulation added over the cavity fill — required when cavity-only fill can't reach the target R without exceeding the framing depth.

## Job sizing worksheet (attic re-insulation example)

1. Measure existing depth and identify material (batt/loose-fill/none).
2. Look up existing material's compressed or settled R-value (compression chart for batts, bag chart for loose-fill) — do not use the nominal/as-new R-value if the material has aged or been compressed.
3. Subtract from the code target R for the climate zone: `R needed = target R − existing effective R`.
4. Divide by the new material's settled R-value per inch (from its bag/data-sheet chart) to get required installed depth; round up to the next whole inch.
5. Multiply installed depth by area for total board-feet or bag count using the manufacturer's coverage chart (required under the FTC R-Value Rule).

**Fiberglass batt compression chart (approximate, per manufacturer compression data):**

| Nominal batt | Designed thickness | Compressed to 5" | Compressed to 4" | Compressed to 3.5" |
|---|---|---|---|---|
| R-19 | 6.25" | R-15 | R-13 | R-11.5 |
| R-30 | 10" | R-20 | R-16 | R-14 |
| R-38 | 12" | R-24 | R-19 | R-17 |

## Spray foam selection

| Property | Open-cell | Closed-cell |
|---|---|---|
| Nominal density | ~0.5 lb/ft³ | ~2.0 lb/ft³ |
| R-value per inch | R-3.5–3.7 | R-6.0–7.0 |
| Vapor permeance class | Class III (permeable) | Class II at ≥1.5" (semi-impermeable), approaches Class I at ~2" |
| Typical use | Deep cavities, interior walls, sound-deadening, where vapor permeability is wanted | Shallow cavities (2x4, rim joists), where the foam must double as air/vapor control layer, below-grade |
| Cost (relative) | Lower per board foot | Higher per board foot |

**Thermal/ignition barrier requirement:** any foam left exposed in a habitable or occupiable space needs either a 1/2" gypsum thermal barrier (15-minute rating, IRC R316.4/IBC 2603.4) or a product specifically tested and listed as an ignition barrier under its ICC-ES/AC377 report. Attics and crawlspaces not used for storage or occupancy may qualify for reduced coverage under a specific foam's listing — check that listing, not a general rule of thumb.

## Dense-pack cellulose wall cavity

1. Confirm cavity is fully enclosed (drywall or netting on one side, sheathing on the other) before blowing.
2. Load to minimum ~3.5 lb/ft³ density (per CIMA-referenced blow chart for the specific machine and material) — verify against the machine's blow-chart setting for the cavity depth, not by eye.
3. Fill from the bottom of the cavity upward through a tube, backing the tube out as the cavity fills, to avoid bridging a void behind the netting.
4. Check for full fill at outlets, top and bottom plates, and around blocking — these are the most common void locations.
5. Log the density setting and bag count per cavity for the job file; this is the record if a settling complaint comes later.

## Air-sealing sequence (before any insulation goes in)

1. Attic hatch or scuttle — weatherstrip and add a rigid insulated cover.
2. Top plates along all exterior and interior partition walls — caulk or foam the plate-to-drywall gap from the attic side.
3. Recessed light housings — foam or caulk the housing-to-drywall gap; note any non-IC-rated fixture for clearance instead of direct contact.
4. Plumbing and electrical penetrations (vent stacks, wiring runs, HVAC boots) — foam seal at the penetration.
5. Chimney and flue chases — use fire-rated sealant/blocking per code, never combustible foam directly against a flue.
6. Rim joists (if accessible from the same job) — foam board or spray foam sealed at the sill.

**Example — 1,600 sq ft attic, climate zone 5 (see SKILL.md worked example for full cost detail):**
- Air-seal package: hatch, 5 fixtures, 3 penetrations, ~210 linear ft top plate — $450.
- Baffles: 24 rafter bays × $12 = $288.
- Blown cellulose to 10" (R-3.7/in settled) over existing compressed R-13 batts = R-50 total, vs. R-49 target.
- Total: $2,658 ($1.66/sq ft blended).

## Attic ventilation baffle placement

1. Identify every rafter bay with a soffit vent from outside (or from the attic if soffit vents are visible from inside).
2. Install one baffle per vented bay, stapled or clipped to hold its shape against blown or batted material, running from the soffit vent opening to above the top of the intended insulation depth.
3. Confirm a minimum 1" airspace is maintained between the baffle and the roof deck along its length.
4. For an unvented/conditioned attic design (spray foam at the roofline instead of the attic floor), skip baffles entirely — that assembly has no soffit-to-ridge airflow path by design.
</content>
