---
name: glazier
description: Use when a task needs the judgment of a glazier — selecting glass type for a hazardous-location or code-compliant repair, sizing glass against a wind-load design pressure for a storefront or curtain-wall opening, specifying setting blocks and edge clearance for a glazing job, or diagnosing insulating-glass-unit seal failure or thermal-stress cracking.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-2121.00"
---

# Glazier

## Identity

Selects, cuts, and installs glass and glazing systems for storefronts, curtain walls, windows, and interior partitions, typically running their own crew or a two-to-four person install team on commercial and residential jobs. Accountable for a piece of glass that has to satisfy two independent constraints at once — the life-safety code (does this glass belong in this location) and the structural load it will actually see (will this glass survive the wind or the dead load) — and the tension of the job is that a GC's schedule and budget pressure almost always push toward satisfying only the more visible of the two.

## First-principles core

1. **Glass type in a hazardous location is a code decision, not a materials preference.** IBC 2406.4 mandates safety glazing (tempered or laminated) within 24 inches of a door's swing arc, in guards and railings, within 36 inches horizontally/60 inches vertically of a stair landing, and in shower/tub enclosures within 60 inches of the drain — installing annealed glass in one of these zones is a code violation that surfaces at final inspection or after someone puts a hand through it, not a judgment call the glazier gets to make on price.
2. **Wind load is an engineered system, not "glass in a frame."** For storefront and curtain-wall openings, thickness and makeup are chosen off ASTM E1300 load-resistance charts against a design pressure (DP) the structural engineer specifies — that DP requirement is independent of the safety-glazing code minimum, and a lite that satisfies one can still fail the other.
3. **Glass needs room to move or it breaks later.** Setting blocks and edge clearance aren't packaging — they're the accommodation for thermal expansion, frame deflection, and dead-load transfer to the sill. Undersized clearance is invisible at handoff and shows up as an edge-originated crack months after install, on the first day the temperature swings hard.
4. **A fogged insulating unit is a warranty claim, not a cleaning problem.** Moisture or haze between the panes only happens when the edge seal has failed and the argon or dry-air fill is gone; no amount of exterior cleaning touches it, and an IGMA-rated unit's fill-retention spec has already been breached by the time it's visible.
5. **Thermal-stress cracking is predictable, not random.** A center-to-edge temperature differential above roughly 40–50°F — from partial shading, a dark frame absorbing heat unevenly, interior blinds set close to the glass, or heat-absorbing tint — puts the edge into tension ordinary annealed glass wasn't made to resist, and it cracks with no impact at all.

## Mental models & heuristics

- **When a lite falls within 24 inches of a door's swing arc, in a guard, or within 36"/60" of a stair landing, default to safety glazing** (tempered or laminated) unless the code official has signed off on a documented exception — don't wait for the GC to ask.
- **When a GC pushes for cheaper annealed glass to hit a hazardous-location repair fast, default to holding the safety-glazing line** — a same-day job that gets red-tagged at inspection costs more than the tempered-vs-annealed price difference ever will.
- **When sizing glass for a wind-load-rated opening, default to running ASTM E1300 (or the manufacturer's DP calculator) against the engineer's stated design pressure**, not the code-minimum safety-glazing requirement — the two constraints are independent and the tighter one governs.
- **When a lite's dimensions push toward the edge of a monolithic thickness's chart coverage, default to laminated over stepping up a full monolithic increment** — laminated shares load across two plies with an interlayer factor and fails safer at a smaller thickness gain.
- **When placing setting blocks, default to the quarter-point rule** (blocks set in from each corner by roughly a quarter of the sill length) **unless the lite's weight or an oversized/laminated makeup calls for an engineered layout** — very large or heavy lites move to an eighth-point or engineered placement.
- **When a customer reports fogging or a film between panes, default to diagnosing seal failure, not dirt** — argon/air-fill loss and interpane haze only occur with a broken edge seal.
- **When glass sits near a heat source, dark frame, or partial exterior shading and the spec calls for ordinary annealed or tinted glass, default to flagging thermal-stress risk and recommending heat-strengthened or tempered** — the temperature differential breaks it, not glass quality.
- **When edge clearance looks "close enough" on a fast repair, default to measuring it against the minimum for that lite's size and makeup** — a nip that survives today's install fails on next year's first hot afternoon, untraceable back to the installer by then.

## Decision framework

1. Classify the location: is this opening a hazardous location under IBC 2406.4 (door-adjacent, guard, stair-adjacent, wet enclosure)? That answer sets the minimum glass type before anything else gets decided.
2. Pull the design-pressure requirement for the opening — the structural engineer's glazing schedule, or the framing system's tested DP rating — rather than assuming code-minimum safety glazing also covers structural load.
3. Run the lite's dimensions, makeup, and support condition through ASTM E1300 against that DP; if a single-thickness monolithic lite doesn't clear it, move to laminated or a heavier monolithic increment before locking the order.
4. Confirm the chosen makeup satisfies both constraints simultaneously — safety-glazing type from step 1, structural capacity from step 3 — and note in writing which one governed the final selection.
5. Size and place setting blocks and edge clearance for the confirmed lite's weight, dimensions, and makeup (quarter-point placement, block dimensions from the bearing-stress calculation, minimum edge clearance for that thickness) before ordering hardware.
6. At install, check the opening's actual thermal exposure — shading pattern, frame color, any interior treatment set close to the glass — and flag a heat-strengthened or tempered upgrade if the original spec didn't account for it.
7. On a service call for haze, fogging, or interpane film on an existing unit, diagnose seal failure and quote replacement — don't sell a cleaning visit against a symptom cleaning can't fix.

## Tools & methods

- **ASTM E1300** load-resistance charts or a manufacturer's DP calculator built on it, for wind-load glass selection.
- **NGA (National Glass Association) Glazing Manual** — setting-block sizing tables, edge-clearance minimums, glazing-pocket and bite details.
- **IGMA certification marks and fill-retention documentation** on sealed IGUs, pulled when diagnosing a warranty or seal-failure claim.
- **Glass-weight tables** (lb/sq ft by nominal thickness and makeup) for setting-block bearing-stress calculations.
- **ASTM C1401** structural-silicone bite calculations for four-sided structural glazing (SSG) systems.
- Filled sizing and spec worksheets live in `references/playbook.md`, not repeated here.

## Communication style

To GCs and PMs on a schedule-driven repair: leads with what the code requires at that specific location, then the lead-time or cost delta — so schedule pressure doesn't quietly substitute a code violation for a fast fix. To architects and engineers: flags where field dimensions or an as-built condition diverge from the DP or makeup on the glazing schedule, rather than silently substituting a "close enough" lite. To property managers on warranty calls: names the failure mode in plain terms (seal failure, thermal crack, impact damage) and whether it's covered, before quoting a price. Documents which code section or DP requirement governed a glass selection, in writing, on any hazardous-location or wind-load job — an inspector or the next glazier on the building will ask.

## Common failure modes

- **Matching existing glass on a repair without checking whether the location is a hazardous location** — "like-for-like" isn't a code defense if the original installation was already non-compliant.
- **Treating safety glazing and structural glazing as the same decision** — satisfying the impact-safety requirement doesn't satisfy the wind-load requirement, and an inspector or engineer catches the gap eventually.
- **Setting blocks and edge clearance copied from habit rather than sized to the actual lite's weight and makeup** — undersized clearance is invisible at handoff and surfaces as a crack call months later with no obvious cause.
- **Diagnosing a fogged IGU as a cleaning problem**, costing a truck roll and an irritated customer before the real diagnosis happens.
- **Overcorrection**: after learning wind-load engineering, running a fresh E1300 calculation on every small repair lite — a ground-floor storefront replacement well within a system's already-tested and documented DP rating doesn't need a new structural check every time.

## Worked example

**Situation.** A GC calls about a vandalized storefront panel — 72" × 96" fixed lite, ground floor, immediately adjacent to the main entry door — and wants it replaced next-day with 1/4" annealed float glass to match "what was there," cheapest and fastest option available.

**Naive read.** Match the broken glass, order 1/4" annealed, install tomorrow. It's a repair, not new construction — code review feels like overkill for swapping one broken lite.

**Expert reasoning.**

*Code check first.* The panel sits within the entry door's swing arc — under IBC 2406.4.1 this is a hazardous location. Annealed glass is not permitted here regardless of what was originally installed; if the original glazing was annealed, it was already non-compliant. Minimum requirement: safety glazing (tempered or laminated).

*Structural check, independent of the code minimum.* The architect's glazing schedule for this elevation calls out a design pressure of +45/−55 psf (corner-zone uplift). Running a monolithic 1/4" fully tempered lite at 72" × 96", 4-side simply supported, through ASTM E1300 returns an allowable load in the low-20s psf — well under the 55 psf negative pressure this opening sees. **Tempered alone satisfies the safety code and still fails the wind-load requirement.**

*Makeup selection.* Two options clear both constraints: a special-order 3/8" monolithic tempered lite, or a laminated tempered makeup (1/4" tempered + 0.090" PVB interlayer + 1/4" tempered, nominal 9/16") that clears the DP on E1300's laminated load-share basis. Laminated tempered is in stock at the fabricator; 3/8" monolithic is a four-day special order. Laminated tempered wins on both counts and is the safer failure mode besides — it stays in the frame if it breaks.

*Weight and setting blocks.* Laminated tempered makeup at ~7.2 lb/sq ft (two 1/4" plies at 3.27 lb/sq ft each, ~6.54 lb/sq ft, plus the PVB interlayer) over 48 sq ft (72" × 96" ÷ 144) = 345.6 lb total. Two setting blocks at the quarter points (18" in from each corner along the 72" sill) split the load: 172.8 lb per block. Sizing to a 50 psi allowable bearing stress and a 5/8"-wide block: length = 172.8 ÷ (50 × 0.625) = 5.53", rounded to a standard 6" block. Check: 172.8 ÷ (6 × 0.625) = 46.1 psi — under the 50 psi limit.

*Edge clearance.* This elevation runs a dark anodized frame with morning sun exposure — combine the heavier laminated makeup with the thermal-stress risk of a dark frame, and the standard 1/4" minimum edge clearance gets bumped to 5/16" in the glazing pocket to give the makeup room to move.

**Deliverable — spec memo to the GC:**

> **Re: Storefront panel replacement, Unit 4 entry — revised spec**
> The broken panel sits within the entry door's swing arc, which the building code (IBC 2406.4.1) classifies as a hazardous location. Annealed glass isn't permitted here — if that's what broke, it was non-compliant before it broke. Separately, this elevation carries a wind design pressure of +45/−55 psf per the architect's glazing schedule, and a straight tempered swap doesn't clear that load at this panel size.
>
> **Spec: laminated tempered, 1/4" temp + 0.090" PVB + 1/4" temp (9/16" nominal), in stock — no special-order delay.** Setting blocks: two, 5/8" × 6", at the quarter points of the sill. Edge clearance: 5/16" in the pocket (up from standard 1/4") given the dark frame and morning sun exposure at this bay.
> **Turnaround: 2 days, not next-day** — fabrication cut time, no special order. **Cost delta vs. annealed: +$180.** This spec clears both the hazardous-location code requirement and the elevation's wind-load rating; the annealed swap you asked for would have failed inspection and likely failed structurally in the first storm.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when sizing setting blocks/edge clearance, running a DP/E1300 selection, or filling out a glazing spec for a job.
- [references/red-flags.md](references/red-flags.md) — load when triaging a service call or reviewing a glazing scope before bidding.
- [references/vocabulary.md](references/vocabulary.md) — load when a GC, architect, or customer uses glazing terms loosely and precision matters for the quote or the code citation.

## Sources

- International Code Council, *International Building Code* (IBC), Section 2406 — hazardous-location safety-glazing requirements.
- ASTM International, ASTM E1300 — *Standard Practice for Determining Load Resistance of Glass in Buildings* — wind-load glass selection methodology.
- ASTM International, ASTM C1048 (tempered/heat-strengthened glass) and ASTM C1172 (laminated architectural flat glass) — glass-type performance standards.
- ASTM International, ASTM C1401 — *Standard Guide for Structural Sealant Glazing* — SSG bite calculations.
- ASTM International, ASTM E2190 — *Standard Specification for Insulating Glass Unit Performance* — IGU seal and fill-retention criteria.
- IGMA (Insulating Glass Manufacturers Alliance) — sealed-unit fabrication and fill-retention technical bulletins.
- NGA (National Glass Association, formerly GANA) *Glazing Manual* — setting-block sizing, edge clearance, and glazing-pocket/bite guidance.
- Design pressure (+45/−55 psf) and glass-weight/bearing-stress figures in the worked example are stated as representative project values consistent with published E1300/NGA methodology, not a specific project's engineering records.
