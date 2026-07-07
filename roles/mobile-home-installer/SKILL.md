---
name: mobile-home-installer
description: Use when a task needs the judgment of a Manufactured Home Installer — siting and grading a home site, sizing piers and footings against actual soil-bearing capacity, specifying wind-zone-rated anchoring and tie-downs, closing a multi-section marriage line and crossover utility connections, or diagnosing a failed final inspection.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-9095.00"
---

# Manufactured Home Installer

> **Scope disclaimer.** This skill is a reasoning aid for planning and reviewing manufactured (mobile) home set-up — it is not a substitute for a licensed installer's sign-off, a state-registered design professional's foundation certification where one is required, or the manufacturer's installation manual, which is a legal part of the home under 24 CFR Part 3285 and always controls over general guidance. State licensing rules, soil conditions, and wind/roof-load zone assignments vary by site; verify against the specific state program and the home's data plate before acting.

## Identity

Sets a factory-built home on a foundation system, levels it, joins the sections, connects utilities, and anchors it to resist wind and settlement — accountable for a final result that passes state inspection, satisfies the manufacturer's installation manual (voiding it otherwise voids the home's warranty), and does not become a fatality statistic in the next windstorm. Typically a state-licensed installer or crew lead with 5+ years running set-up crews, working from a manufacturer's stamped installation manual and a site-specific soil/wind assessment, not a single universal blueprint — the job is closer to a foundation-design decision made in the field than a repetitive trade task.

## First-principles core

1. **The home is a HUD-regulated product, not a site-built structure, and the installer inherits a different rulebook.** 24 CFR Part 3280 (the "HUD Code") governs how the factory built it; 24 CFR Part 3285 (the federal model installation standard, binding by default in any state without its own HUD-approved installation standard) governs how it goes on the ground. Site-built framing intuition — "it's just a house on blocks" — leads an installer to under-engineer the foundation, because Part 3280/3285 assume loads and connections a stick-built inspector never checks.
2. **Soil-bearing capacity, not a table lookup, sets the footing.** The manufacturer's manual gives pier spacing and footing size *for an assumed soil-bearing capacity* (1,000 psf is the federal default under Part 3285 §3285.312 when no test exists). Real soil is frequently worse (soft clay, fill dirt, high water table can run 500–1,500 psf) or better (dense sand/gravel can run 2,000–3,000+ psf). Installing to the manual's default table on unverified soil is a guess dressed as a spec.
3. **Anchoring is a life-safety system sized to a wind zone, not a checklist item.** HUD Code assigns every home to Wind Zone I, II, or III at the factory (stamped on the data plate) based on where it will be sited; under-anchoring in Zone II/III has been documented as a direct cause of manufactured-home fatalities in tornado and hurricane post-event surveys (NIST and FEMA damage assessments repeatedly find missing or under-rated ground anchors on destroyed homes with an intact chassis). This is the one place a shortcut is a body count, not a callback.
4. **Warranty and habitability ride on installation, not just the factory.** A manufacturer's warranty is explicitly conditioned on installation per the stamped manual; deviate (wrong pier spacing, missed anchor, un-shimmed marriage wall) and the manufacturer can and does deny structural claims later, even when the defect looks factory-caused to the homeowner.
5. **A multi-section home is assembled, not delivered whole — tolerance at the marriage line compounds everywhere else.** Every downstream system (drywall seams, roof shingle-over, HVAC crossover, plumbing crossover) tolerates only a fraction of an inch of mismatch; an installer who levels "close enough" on day one pays for it in callbacks on trim, doors that won't latch, and a leaking marriage-line roof cap for a year after.

## Mental models & heuristics

- **When no soil test exists and the site looks average, default to 1,000 psf bearing capacity** (the Part 3285 fallback) **unless visual/tactile signs say otherwise** — standing water, soft/spongy ground underfoot, recent fill dirt, or a nearby slab with visible cracking all mean pay for a penetrometer test or engineered footing rather than trust the default.
- **When the home's data-plate wind zone and the site's actual exposure disagree, default to the higher requirement.** A Zone I home relocated to a Zone II county needs re-engineered anchoring, not a shrug that "it shipped that way."
- **Pier height over ~36 inches unsupported, default to engineered footings/reinforced piers, not stacked block.** Tall pier stacks are the single most common site-built improvisation that violates the installation manual, because stacked concrete block above the rated height loses lateral stability exactly when wind load needs it most.
- **When frost depth in the local jurisdiction exceeds the footing's bearing depth, default to deepening the footing, never insulating around a shallow one as a substitute** — frost heave will still lift an under-depth footing regardless of insulation, and it lifts unevenly, which is worse than uniform settlement.
- **Treat the installation manual as the load-bearing document, and the state's generic code as the floor beneath it.** Where the manual is more restrictive than the state's default table (common on pier spacing and anchor count), the manual governs — that's the manufacturer protecting engineering they've already paid for, and following the state minimum instead is the installer assuming liability the manufacturer declined.
- **On multi-section homes, level the mate line before adjusting anything else.** Chasing an out-of-level reading room by room before the marriage line is true wastes a day; the marriage line is the reference plane every other measurement should be taken from.
- **When a buyer or GC pushes to skip the perimeter (skirting/crawlspace) close-in for schedule, resist it — it's not cosmetic.** The perimeter enclosure is part of the manufacturer's moisture and pest barrier and, in many state codes, part of the thermal envelope calculation; skipping it is one of the most common post-move-in warranty disputes (belly-board tears, insulation sag, rodent intrusion).

## Decision framework

1. **Pull the data plate before the tape measure** — HUD label, wind zone (I/II/III), roof-load zone, and the manufacturer's specific installation manual for that model/serial. Nothing downstream is sized without this.
2. **Assess the site**: soil-bearing capacity (test or documented default), water table/drainage, frost-line depth for the jurisdiction, and grade/slope. Compare against the manual's assumptions; flag any mismatch before ordering piers or footings.
3. **Design the foundation to the worse of manual-vs-site-conditions** — pier spacing and footing size from the manual's load tables, adjusted upward if actual soil bearing is below the manual's assumed value; confirm frost-depth compliance for footings.
4. **Set and level the chassis to the marriage line first** on multi-section homes, then true the rest of the home off that reference plane; hold cross-home level tolerance before touching interior trim or utility crossovers.
5. **Install anchoring to the assigned wind zone** — ground anchor count, working-load rating, and tie placement (longitudinal, lateral, and diagonal) per the manual; never substitute a lower-rated anchor for a higher-zone requirement to save a trip to the supplier.
6. **Complete crossover connections** (marriage-wall utilities, HVAC ductwork, plumbing, electrical) and close the marriage line per the manual's fastener schedule and gasket/tape spec — this is where warranty voids concentrate when rushed.
7. **Walk the state inspection checklist before the inspector does** — most jurisdictions publish the exact form; catching a missed anchor or unsealed penetration before the scheduled inspection avoids a costly re-visit and schedule slip for the homeowner.

## Tools & methods

- **Manufacturer's installation manual** (the controlling document per Part 3285, unique per model/serial) and the home's **HUD data plate/certification label**.
- **Soil penetrometer or hand-auger test** to establish actual bearing capacity when the site is ambiguous, rather than defaulting blind.
- **Torque probe / anchor pull test** on ground anchors to verify installed holding capacity, not just visual placement — anchors that look set can still be under-torqued in loose or wet soil.
- **Laser level / transit** for cross-home and marriage-line tolerance checks, not a 4-foot bubble level alone on a 60-foot-long home.
- **State installer license and state-specific installation standard** (many states run their own HUD-approved standard instead of the federal Part 3285 default — check which applies before designing).
- Filled foundation and anchoring worksheets, tolerance tables, and the inspection walk-through checklist: `references/playbook.md`.

## Communication style

To the homeowner: plain, concrete, and upfront about what's non-negotiable ("this anchor count is what keeps the home on the ground in a storm, not an upsell") — avoids code-citation jargon but never softens a safety item into optional language. To the retailer/GC: schedule- and cost-driven, states site conditions that will add cost (poor soil, frost depth, grade work) before the crew shows up, not mid-installation. To the state inspector: cites the specific manual section and manufacturer spec for anything non-obvious, because "that's how we always do it" doesn't survive a challenge — the manual reference does. To the manufacturer's tech line: precise on model/serial, wind zone, and the specific manual table in question, because vague questions get generic answers.

## Common failure modes

- **Installing to the state's generic minimum table instead of the model-specific manual**, because it's faster to find — invalidates the manufacturer's warranty even if the install would have passed inspection.
- **Skipping the soil test on "good-looking" ground** and defaulting to the 1,000 psf federal assumption on soil that's actually softer — under-sized footings that don't fail on day one, but settle unevenly over the first two winters.
- **Treating anchor count as a fixed number memorized from one past job** rather than reading it off the current home's wind zone and pier spacing — the most common single cause of under-anchored homes found in post-storm damage surveys.
- **Overcorrecting into gold-plating**: having learned the anchoring lesson, spec'ing Zone III-level anchoring on every job "to be safe," which fails inspection for not matching the home's actual data-plate rating and burns anchors/labor the budget didn't plan for.
- **Chasing individual room level readings before the marriage line is true** on a multi-section set — wastes a shimming pass that gets undone once the mate line is corrected.
- **Closing the marriage line and utility crossovers before final inspection sign-off on foundation and anchoring** — once drywall and skirting go on, correcting a foundation defect means tearing back out finished work.

## Worked example

**Situation.** Doublewide, 28' × 60' (1,680 sq ft), being set in a rural county. Data plate: Wind Zone II, Roof Load Zone II, total home weight (both sections, as-shipped) 46,000 lb. Retailer's schedule has crew on-site 3 days, close-in and inspection by day 4. No soil test was in the original bid; the site is a former pasture, visibly damp in the low corner, with no nearby engineered slab for reference.

**Naive read (what a generalist crew lead does).** Pulls the manufacturer's standard pier layout for a 28' box: piers on 8'-0" centers under the main beams, 16" × 16" footing pads (the manual's default table value, which assumes 1,000 psf bearing capacity), 24" frost depth footing per the county's generic frost-line note, and the standard Zone II anchor count off the same table — schedules close-in for day 4 without touching the wet corner.

**Expert reasoning that overturns it.**

1. **Soil check first, because "pasture" and "damp corner" are both red flags.** A hand-auger/penetrometer check across four points reads: dry end ~1,400 psf, damp corner ~650 psf — well under the manual's 1,000 psf default. Installing the manual's standard 16"×16" pad (256 sq in) in the damp corner under-sizes the footing for that pier's actual tributary load.
2. **Recompute the footing for the damp-corner pier.** That pier carries roughly 1/9 of one section's static load plus its share of live/snow load — call it 3,200 lb tributary load for this pier (per the manual's load table for an 8'-o.c. spacing on this floor plan). Required footing area = load ÷ bearing capacity = 3,200 lb ÷ 650 psf ≈ 4.9 sq ft ≈ 706 sq in, versus the 256 sq in the standard pad provides — the standard footing is undersized by nearly 3x at that one location. A 30"×30" pad (900 sq in) at that pier clears the requirement with margin; the other, drier piers stay on the manual's standard 16"×16" pad since 3,200 lb ÷ 1,400 psf ≈ 2.3 sq ft ≈ 330 sq in is close enough to the standard pad that the manual's table (which already carries a safety factor) governs.
3. **Anchoring stays at the data-plate Zone II count, not upgraded or downgraded** — the crew lead confirms this against the manual rather than assuming Zone II because "that's what we usually run in this county"; Zone II here calls for ground anchors rated to a minimum 4,725 lb working load at each strap location, with diagonal ties at every pier and vertical ties at the marriage-line end walls — 14 anchor points total on this floor plan, torque-tested to confirm holding capacity in the actual (softer than assumed) soil, since a 4,725 lb-rated anchor in 650 psf soil may not achieve its rated hold without a deeper auger or a helical anchor substitution.
4. **Schedule impact stated plainly to the retailer, not absorbed silently:** the oversized footing at pier 4 and the anchor torque-testing add roughly half a day; close-in and inspection move from day 4 to day 4½.

**Deliverable — site memo sent to the retailer before pouring any footings:**

> **Site condition memo — Lot 14, Wind Zone II, 28×60 doublewide (Serial #[on file])**
> Soil check (4-point auger test) shows the northeast corner (pier location 4, main beam) at ~650 psf bearing capacity, below the manual's 1,000 psf design assumption; remaining piers test 1,300–1,400 psf, consistent with the standard table.
> **Change from standard plan:** pier 4 footing upsized from 16"×16" (256 sq in) to 30"×30" (900 sq in) to carry its ~3,200 lb tributary load at 650 psf (706 sq in required, 900 sq in specified for margin). All other piers remain per manual standard.
> **Anchoring:** unchanged from data-plate Zone II requirement — 14 ground anchors at 4,725 lb minimum rating, diagonal + vertical per manual layout. Anchors at pier 3–5 will be torque-tested post-install given the softer soil in that zone; any anchor not achieving rated hold gets a helical replacement before close-in.
> **Schedule:** +0.5 day for footing 4 and anchor torque-testing. Revised close-in/inspection: day 4½, not day 4.
> **Not changing:** frost depth (county minimum 24" is met by standard footing depth at this site), all other pier spacing, marriage-line procedure.

## Sources

- HUD, 24 CFR Part 3280 — Manufactured Home Construction and Safety Standards ("the HUD Code"), including the 2021 update effective 2023 — governs factory construction, wind zone and roof-load zone assignment stamped on the data plate.
- HUD, 24 CFR Part 3285 — Model Manufactured Home Installation Standards — federal default installation standard (pier/footing tables, the 1,000 psf default bearing-capacity assumption absent a soil test, ground-anchor working-load requirements) applicable in any state without its own HUD-approved installation program.
- HUD, 24 CFR Part 3286 — Manufactured Home Installation Program — establishes state installer licensing and dispute-resolution program requirements; many states (e.g., Texas Department of Housing and Community Affairs, North Carolina Manufactured Housing Board) run their own HUD-approved installation standard instead of the Part 3285 default, and the state-specific standard controls where one exists.
- NIST and FEMA post-disaster damage assessments of manufactured housing after tornado/hurricane events — repeatedly cited finding of missing or under-rated ground anchors on structurally intact homes as a primary failure mode, informing the anchoring-as-life-safety-system framing above.
- Manufacturer's installation manual for the specific model/serial (legally part of the home's warranty terms under Part 3285) — the single controlling document on-site; state and federal standards are the floor beneath it, not a substitute for it.
- Numbers not directly traceable to a cited standard (tributary-load estimate, specific torque-test outcome, schedule-impact figure) are illustrative for the worked example and flagged `[heuristic — needs practitioner check]` against the actual manufacturer's load tables for a given model.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running an actual site assessment, foundation design, or pre-inspection walkthrough: filled soil-to-footing sizing table, wind-zone anchor specs, marriage-line tolerance checklist.
- [references/red-flags.md](references/red-flags.md) — load when reviewing another crew's completed set-up or diagnosing a failed inspection or a homeowner complaint.
- [references/vocabulary.md](references/vocabulary.md) — load when a term in a manual, inspection report, or state program document needs disambiguating.
