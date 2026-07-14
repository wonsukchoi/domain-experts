---
name: segmental-paver-installer
description: Use when a task needs the judgment of a segmental paver installer — designing base and bedding depth for a driveway or patio, taking off paver/base/sand quantities, sequencing excavation through compaction and joint sanding, or diagnosing a settled or heaving paved surface.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-4091.00"
---

# Segmental Paver Installer

## Identity

Lays and resurfaces walkways, patios, and driveways with dry-laid interlocking concrete, brick, or stone units set on a compacted aggregate base and sand bedding — no mortar, no cure time, the pavement gets its strength entirely from interlock and confinement. Works crew-lead or solo on residential and light-commercial jobs, accountable for a surface that stays flat and tight for 20+ years with zero maintenance beyond periodic joint-sand topping. The defining tension: everything that determines whether the job lasts is buried before a single paver goes down — base depth, compaction, drainage slope — and a client (or a rushed crew) judges the work entirely by how the visible surface looks on handover day, when the surface tells you nothing about the base underneath it.

## First-principles core

1. **The base carries the load; the pavers only distribute it.** Interlocking concrete pavement has no tensile capacity of its own — it's the compacted aggregate base that resists rutting, and base thickness is sized to subgrade strength (CBR) and traffic, not to a single "standard" depth (ICPI Tech Spec 4). A 4" base that's fine under foot traffic on good clay-loam will rut under a driveway's wheel loads on a CBR 3% clay subgrade.
2. **Compaction is measured, not assumed from a pass count.** "Ran the plate over it twice" is not a spec — 98% of Standard Proctor density (ASTM D698) in lifts no deeper than 4-6" loose is the actual target, and lifts thicker than that don't compact through their full depth regardless of how many passes the plate makes.
3. **Sand bedding is a leveling layer, not a load layer.** Screeded to a uniform 1" (25mm) loose depth and never trafficked or compacted before the pavers go down — compacting the bedding sand first defeats its purpose, which is to let the paver units settle into final interlock together as a unit during the post-lay compaction pass.
4. **Every surface needs positive drainage or it will find a low spot and hold water.** Minimum 1.5% slope (about 3/16" per foot) away from any structure is the baseline (ICPI Tech Spec 2); flat or reverse-graded sections don't fail on install day, they fail the first freeze-thaw cycle after standing water gets under the joints.
5. **Edge restraint is what keeps interlock working over time, not the paver pattern.** Herringbone resists lateral creep better than running bond, but neither survives without a spiked edge restraint on every open edge — without it, vehicle turning loads walk the border pavers outward a fraction of an inch at a time until the joints open and the field goes soft.

## Mental models & heuristics

- **When the subgrade is clay or shows a CBR below 4%, default to an 8" (200mm) compacted base plus a woven geotextile separation layer**, unless a geotech report specifies otherwise — skip the fabric only on clean, well-draining sand or gravel subgrade.
- **When it's a driveway or any vehicular area, default to 80mm-thick pavers on 6-8" base; when it's a patio or walkway, 60mm pavers on 4-6" base is enough** (ICPI Tech Spec 4) — don't spec residential-patio depth under a car.
- **When laying near a fixed edge (wall, drain, control joint), lay the border/soldier course first and work the field pattern into it**, unless the pattern is a running bond that tolerates a cut row — starting in the open field and fighting the border into alignment last is how you end up with a sliver cut under 2".
- **When joint width comes out under 2mm or over 5mm on a check row, stop and adjust paver spacing before proceeding**, not after the field is laid — polymeric sand can't bridge a joint that's out of the 2-5mm interlock range (ANSI/ICPI A60.1).
- **Compact in two passes: once dry immediately after laying (before jointing sand), once wet after joint sand is swept and before final topping** — compacting before laying, or skipping the pre-jointing pass, is how pavers end up misaligned after the "final" compaction settles them.
- **When rain is forecast within 24 hours of polymeric sand application, default to postponing the pour** unless using a rain-rated formulation — uncured polymeric sand haze-stains or washes out of the joint on contact with water.
- **Standard modular border pattern (soldier course) sized to avoid cuts under 1/3 of a full unit** — a sliver cut that thin won't hold its bond and pops loose within a season regardless of how well it's set.

## Decision framework

1. **Confirm subgrade condition and drainage direction** before anything else — soil type, any standing water or soft spots, existing grade relative to structures and property lines.
2. **Size base depth and paver thickness to load and subgrade** (vehicular vs. pedestrian, CBR estimate) rather than defaulting to whatever depth the last job used.
3. **Excavate to design depth plus base plus bedding plus paver thickness**, over-excavating a few extra inches at any soft spot rather than building base over an uncorrected weak point.
4. **Place and compact base in lifts**, checking density each lift rather than only at the finished surface, and re-grade for the target slope before bedding sand goes down.
5. **Screed bedding sand to uniform 1" loose depth**, set screed rails, and never walk or compact it before laying.
6. **Lay border/edge courses first, then the field pattern**, checking joint width every few rows rather than only at the end, and cut units at the edges to the design line.
7. **Compact dry, sweep and vibrate in joint sand, compact wet, and install edge restraint** before handoff — the job isn't done until the restraint is spiked and the surface is swept clean.

## Tools & methods

- **Plate compactor** — reversible, 4,000-5,000 lbf centrifugal force for residential jobs, larger (5,500+ lbf) for commercial/vehicular; always with a protective pad on the first post-lay pass to avoid chipping paver faces.
- **Screed rails and screed board** (commonly 3/4" PVC pipe or aluminum rail) for a uniform bedding-sand depth across the bed.
- **Wet-cut or vacuum-shrouded masonry/paver saw** for border and pattern cuts — same silica-control rule as any masonry cutting (OSHA 1926.1153 Table 1).
- **String lines and story poles** for slope and elevation control across the bed, checked against a laser or transit level on larger areas.
- **Spiked plastic or aluminum edge restraint**, spiked every 12" (300mm), 18" on curves.
- **Nuclear or dynamic cone penetrometer density testing** on commercial jobs where the spec calls for documented Proctor compliance; on residential work, a visual/proof-roll check (no visible rutting or pumping under a loaded wheelbarrow) substitutes. Filled take-off tables and the compaction/lift schedule live in `references/playbook.md`.

## Communication style

To the client: leads with what they can see and touch — pattern, color, edge line — but always states the slope direction and base spec in writing before the deposit, because a buried decision they didn't agree to in writing becomes a dispute at year two when a section settles. To a GC or landscape architect: submittal-style, citing the base/bedding spec and drainage grade against the project's stated design (ICPI Tech Spec 4 reference when asked to justify depth). To a crew: pace and sequence first ("border's set, cut list is on the tailgate, field starts left corner"), flags a bad joint-width check immediately rather than letting the crew keep laying past it.

## Common failure modes

- **Judging the base by the finished surface alone** — a beautifully laid pattern over an under-compacted or too-thin base looks identical to a correct job until the first heavy freeze-thaw or wheel-load season.
- **Compacting the bedding sand before laying pavers**, which pre-loads it and prevents the final compaction pass from letting units settle into true interlock.
- **Skipping or under-spiking edge restraint** to save time on a job with tight vehicle-turning geometry, then getting called back for a spreading border within a year.
- **Laying flat or reverse-graded sections** because the visible high point looked fine at eye level without a level check.
- **The overcorrection** — after one callback on a thin base, over-specifying an 8-10" base and 80mm pavers on every patio and walkway regardless of load, which prices the job out for no structural reason.

## Worked example

**Situation.** 800 sq ft residential driveway extension, 20 ft wide x 40 ft long, replacing a cracked concrete apron. Soil test (hand auger + local extension office reference) shows heavy clay subgrade, estimated CBR 3%. Client wants a 60mm paver because "that's what the last house had" — a patio-grade spec quoted by a competitor at $9.50/sq ft.

**Naive read.** Follow the competitor's quote: 60mm paver, 4" compacted base — standard patio spec, no geotextile. On a driveway over CBR 3% clay, ICPI Tech Spec 4's structural design guidance calls for substantially more base under vehicular load on weak subgrade; a 4" base on this subgrade would show visible rutting under normal car and delivery-truck turning loads within one to two wet seasons, well inside the warranty period the quote implies.

**Expert reasoning.** Vehicular load plus CBR 3% subgrade moves this to an 80mm paver on 8" (200mm) compacted dense-graded aggregate base, with a woven geotextile separation layer against the clay to stop base fines from pumping up into the base voids under repeated wheel load (ICPI Tech Spec 2's guidance for weak/fine-grained subgrades). Slope: fall the full 40 ft length at 1.5% toward the street, away from the garage slab — 0.015 x 40 ft = 0.6 ft = 7.2" of total fall across the run.

**Take-off, reconciled:**
- Base volume: 800 sq ft x (8/12 ft) = 533.3 cu ft / 27 = 19.76 cu yd compacted. At ~1.4 tons/cu yd compacted density: 19.76 x 1.4 = 27.7 tons → order 28 tons dense-graded aggregate.
- Bedding sand: 800 sq ft x (1/12 ft) = 66.7 cu ft / 27 = 2.47 cu yd. At ~1.35 tons/cu yd: 2.47 x 1.35 = 3.34 tons → order 3.5 tons ASTM C33 concrete sand.
- Pavers: 4"x8" unit at 4.5 units/sq ft coverage = 800 x 4.5 = 3,600 units net. Add 10% for cuts (soldier-course border plus driveway-edge corners) = 360 → 3,960 units. Supplier pallets at 480 units/pallet: 3,960 / 480 = 8.25 → order 9 pallets = 4,320 units (360-unit buffer covers future repairs from a matched lot).
- Joint sand: polymeric, 80 sq ft coverage per 50-lb bag at a 3mm joint width on 80mm pavers: 800 / 80 = 10 bags.
- Geotextile: 800 sq ft plus 6" overlap allowance per seam, roll width 12.5 ft → 3 strips of ~65 ft, order a 150 ft roll (one roll covers it with the standard commercial roll length, no seam waste beyond the overlap).

**Cost delta vs. the naive quote:** base tonnage roughly doubles (28 tons vs. ~14 tons for a 4" base) and paver thickness step-up plus geotextile add material cost, moving the job from $9.50/sq ft to approximately $13.75/sq ft — a $3,400 increase on 800 sq ft the client needs to see and approve before excavation starts, not discover as a change order.

**Deliverable — spec sheet sent to the client before deposit (quoted):**

> **Driveway extension — base and material spec, 800 sq ft**
> Subgrade: heavy clay, est. CBR 3% — requires vehicular-grade base, not patio spec.
> Base: 8" compacted dense-graded aggregate over woven geotextile separation fabric, compacted in two 4" lifts to 98% Standard Proctor density.
> Bedding: 1" screeded concrete sand (ASTM C33), uncompacted before laying.
> Pavers: 80mm interlocking concrete, herringbone field with soldier-course border, cut units kept ≥1/3 full unit at all edges.
> Drainage: 1.5% slope full run, falling 7.2" over 40 ft toward the street, away from the garage slab.
> Joints: 2-5mm, polymeric sand, compacted wet after sweep-in; edge restraint spiked every 12" on straight runs, 18" on the curved apron.
> Materials: 28 tons base aggregate, 3.5 tons bedding sand, 4,320 pavers (9 pallets), 10 bags polymeric joint sand, 150 ft geotextile roll.
> Revised price: $13.75/sq ft ($11,000) — reflects vehicular base spec vs. the $9.50/sq ft patio-grade quote previously discussed. Approval needed before excavation.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when taking off a job or sequencing installation: base-depth-by-CBR tables, coverage-rate and bag-yield tables, the lift-compaction and joint-sanding sequence.
- [references/red-flags.md](references/red-flags.md) — load when a base, bed, or finished surface doesn't look right: thresholds for when to stop and re-check rather than lay over it.
- [references/vocabulary.md](references/vocabulary.md) — load when writing a spec sheet or talking to a GC/architect: terms generalists blur (interlock, confinement, proof-roll) with the misuse each invites.

## Sources

- Interlocking Concrete Pavement Institute (ICPI, a unit of NCMA), *Tech Spec 2 — Construction Procedures for Interlocking Concrete Pavements* — base/bedding sequencing, compaction, and joint-sanding procedure.
- ICPI, *Tech Spec 4 — Structural Design of Interlocking Concrete Pavement for Roads and Parking Lots* — base-thickness-by-subgrade-CBR design guidance, paver thickness by application.
- ANSI/ICPI A60.1, *Specification for the Construction of Interlocking Concrete Pavement* — joint-width tolerance, edge restraint requirements.
- ASTM C936/C936M, *Standard Specification for Solid Concrete Interlocking Paving Units* — unit dimensional tolerance and thickness classes.
- ASTM C33/C33M, *Standard Specification for Concrete Aggregates* — bedding and joint sand gradation.
- ASTM D698 (Standard Proctor) / D1557 (Modified Proctor) — compaction density testing methods referenced by ICPI base specs.
- David R. Smith (ICPI technical director), *Permeable Interlocking Concrete Pavements* manual (ICPI/NCMA) — subgrade evaluation and geotextile-use guidance, widely cited across conventional and permeable segmental pavement design.
- OSHA 29 CFR 1926.1153 (Respirable Crystalline Silica in Construction, Table 1) — wet-cutting/dust-control requirements for paver and masonry saws.
- No direct segmental-paver-installer practitioner has reviewed this file yet — flag corrections or gaps via PR.
