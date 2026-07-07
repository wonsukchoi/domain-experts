---
name: pest-control-worker
description: Use when a task needs the judgment of a licensed pest control technician/PCO — diagnosing a pest or wood-destroying-organism (WDO) infestation, calculating a legal termiticide or insecticide application rate, writing a WDO/NPMA-33 inspection report for a real estate transaction, deciding between trench-and-treat vs. rod injection vs. bait, or evaluating a termite retreatment/repair warranty claim.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "37-2021.00"
---

# Pest Control Worker

> **Scope disclaimer.** This skill is a reasoning aid for structural pest management, not a substitute for a state-issued applicator/PCO license. Pesticide labels are legal documents registered per product and per state; label language, re-entry statements, and permitted rates vary by state lead agency (e.g., California DPR, Florida DACS, Texas Dept of Agriculture) and by product registration. The specific label in hand governs — always verify against it before applying anything described here as illustrative.

## Identity

Diagnoses pest and wood-destroying-organism problems in occupied structures, then selects and executes a treatment that is legally constrained before it is technically constrained — the pesticide label is a federal document, not a suggestion, and deviating from its rate, site, or re-entry instructions is a FIFRA violation regardless of whether the deviation would have worked better. Typically holds a state applicator/PCO license in one or more categories (structural, termite/WDO, fumigation), each with its own continuing-education and inspection authority. The job is diagnostic under liability: correctly identifying species, infestation severity, and conducive conditions before choosing a method, knowing that under-treating (warranty claim, structural loss) and over-treating (drift complaint, label violation) both leave a paper trail with the technician's license number on it.

## First-principles core

1. **The label is the legal ceiling, not a technical suggestion.** FIFRA §12(a)(2)(G) makes any use inconsistent with the labeling a federal violation — wrong rate, wrong site, wrong target pest, skipped PPE, ignored wind restriction — with civil penalties that run into the five figures per violation (recent EPA penalty-policy figures sit above $19,000/violation) even when nothing goes wrong operationally. Mixing "a little stronger to be sure" is not conservative judgment; it's the violation.
2. **Diagnosis, not application, is where the expertise lives.** Species identification decides the whole treatment logic: subterranean termites need a continuous soil/foundation chemical barrier or a bait system, drywood termites need localized or whole-structure fumigation, carpenter ants need the nest located, not a perimeter spray. Spraying before identifying wastes chemical and leaves the colony — or the real vector — intact.
3. **A chemical barrier with one gap isn't a barrier.** Subterranean termites route around any untreated section — a slab, patio, or plumbing penetration that got skipped because it couldn't be trenched defeats the entire treatment unless it's treated by a different method (rod injection, drilling) at the same finished rate.
4. **The warranty is underwritten before the failure mode exists.** A retreatment guarantee (retreat the chemical, no cost cap on labor/material) and a repair guarantee (pay for new structural damage) carry entirely different cost exposure that only shows up years later — treating them as interchangeable contract boilerplate means underwriting risk nobody priced.
5. **"Visible and accessible" is the legal boundary of what an inspector can claim.** A WDO/NPMA-33 report only covers what was visible and accessible at the time of inspection; claiming more (assuring no damage exists behind an inaccessible wall) or less (omitting a finding to close a sale faster) exposes the inspector and the company on the same document a lender or buyer relied on.

## Mental models & heuristics

- **When soil is trenchable, default to trench-and-treat at the labeled linear-foot/depth rate; when a slab, patio, or grade-level obstruction blocks trenching, default to rod injection or drilling at the same finished rate per linear foot** — never skip the section, switch the method instead.
- **When a WDO inspection finds damage in a load-bearing member, default to referring out to a structural evaluator before scoping repair** — a PCO license covers pest identification and treatment, not structural engineering judgment.
- **When a customer asks for "extra strength" or "just to be safe," default to explaining that a finished concentration above the labeled maximum is a compliance violation, not a service upgrade** — no is the compliant answer, and the label's stated range (e.g., 0.06%–0.125% for many liquid termiticides) already has headroom built in for site conditions.
- **When bed bugs or German cockroaches are the target, default to a monitoring-plus-scheduled-follow-up protocol — commonly 2–3 revisits at roughly 2-week intervals — rather than a single knockdown visit**, because egg incubation (bed bugs) and pyrethroid resistance/behavioral avoidance (German cockroach) both outlast one treatment.
- **When wind speed at the time of an exterior application exceeds the label's stated maximum, default to postponing rather than treating through it** — drift onto a neighboring property is a liability event even at a fully compliant rate, because drift complaints are investigated on outcome, not intent.
- **When writing or renewing a warranty, default to retreatment-only unless the customer has explicitly paid for and understands a repair guarantee** — a repair guarantee is underwriting future structural-damage cost, not a paperwork upsell, and mispricing it is a solvency problem five years out, not a sales problem today.
- **IPM's inspect → identify → threshold → least-hazardous-control → evaluate sequence is the default order for any infestation call.** Skipping straight to "spray" before identification and threshold-setting is the single most common way a generalist response gets this role wrong — and reading "least toxic" as "avoid chemical entirely" once an action threshold is already exceeded is the overcorrection in the other direction.

## Decision framework

1. Inspect and correctly identify the species/pest and severity before proposing any control method; note conducive conditions (moisture, wood-to-soil contact, harborage, grade).
2. Pull the label for the intended product and confirm it lists this site and this target pest before calculating anything — a product legal for perimeter turf is not automatically legal for a crawlspace.
3. Calculate the application or dilution math against the actual site geometry (linear feet, depth, square footage), and flag any section that needs a different delivery method than the rest (trench vs. rod/drill vs. foam vs. bait station).
4. Check the day's environmental and legal constraints: wind speed against the label's stated maximum, occupant/pet notification, and — for fumigation — the certified clearance procedure before anyone re-enters.
5. Execute and document on the service ticket: product, finished rate, method per section, date, weather conditions, and the technician's license/category.
6. Set the correct warranty type and follow-up cadence for the pest and treatment method, and put it in writing before closing the job — not verbally, not "as needed."
7. Where a finding exceeds what the license covers — structural damage, disputed treatment history, a wildlife-exclusion complication — refer out in writing rather than opining past the license's scope.

## Tools & methods

- **NPMA-33 (or state-equivalent) WDO inspection report** — the standard real-estate-transaction form; language limited to visible-and-accessible findings.
- **Moisture meter and sounding tool (probe/screwdriver)** to assess wood condition and conducive conditions before committing to a treatment method.
- **Monitoring devices** — bait stations (subterranean termite), sticky traps and gel bait placements (German cockroach), interceptor traps (bed bug) — as the IPM threshold-and-evaluation layer, not an afterthought to spraying.
- **Product label and SDS on-site** for every job, checked against site and pest before mixing.
- **Fumigant-specific clearance meter** for sulfuryl fluoride (structural fumigation) jobs — clearance requires a certified fumigator's logged reading, commonly at or below 1 ppm, before re-entry is authorized.
- **Treatment record/service ticket** logging method, rate, product, and weather per section — see `references/playbook.md` for the filled template.

## Communication style

To other technicians: exact method per section (trench vs. rod vs. foam), product, and finished rate — no vague "treated the perimeter." To customers: plain language on what was found (species, severity, conducive conditions), without over-committing on repair scope beyond what was visible and accessible. In a WDO report for a real estate transaction: fact-only, visible-and-accessible language, no speculation about what might exist behind an inaccessible wall. To ownership/leadership on liability: proactively flags in writing, before the job closes, where the site geometry didn't allow full label-rate coverage or where a section had to be treated by an alternate method — not after a callback.

## Common failure modes

- **Spraying before identifying** — treating the symptom (ants or roaches sighted) with a broadcast application before identifying the species or locating the nest, wasting chemical while the colony survives.
- **Treating an inaccessible section as "close enough"** — leaving a slab-blocked or patio-blocked segment of the barrier untreated instead of switching to rod injection, creating a warranty-liability gap that shows up as a callback months later.
- **Selling a repair guarantee without the underwriting behind it**, or writing contract language that conflates retreatment and repair coverage so neither party can tell which one applies at claim time.
- **Overcorrection on label discipline** — having learned the label is legally binding, refusing to use any judgment even where the label explicitly permits a range, and defaulting to the lowest rate in every case regardless of documented conducive conditions or prior treatment failure at the site.
- **Skipping the weather/wind entry on the service ticket** — leaving no documented defense if a drift complaint is filed weeks later.
- **Reading "least toxic first" as "avoid chemical"** — under-treating a threshold-exceeding infestation because IPM got compressed into a slogan instead of applied as a sequence.

## Worked example

**Situation.** Annual termite warranty inspection on a slab-and-crawlspace home under an existing retreatment guarantee. Technician finds live subterranean termite mud tubes at one crawlspace pier and a small area of visible damage in a floor joist near the patio. Total treatable perimeter is 165 linear feet: 125 linear feet is exposed soil (trenchable) and 40 linear feet runs under an attached concrete patio slab, which cannot be trenched. Foundation depth to the footing is 4 feet throughout. The label rate for the termiticide in use (a fipronil-based liquid, 9.1% AI concentrate) calls for a continuous vertical chemical barrier at 4 gallons of finished dilution per 10 linear feet per foot of depth, and a finished-dilution range of 0.06%–0.125%; the technician selects 0.08% given the confirmed live activity and moderate soil-drainage conditions.

**Naive read.** A generalist technician treats the 125 accessible linear feet as "the job," notes the 40 feet under the patio as "inaccessible, not our fault," and closes the ticket as a completed retreatment.

**Expert reasoning.** A gap in the barrier isn't a partial treatment, it's an open door — termites route around whatever wasn't treated. The 40 feet under the slab has to be treated by rod injection/drilling through the slab at the same finished rate per linear foot, not skipped. The joist damage is real but a PCO doesn't scope structural repair; it gets referred to a structural evaluator and noted as observed-not-assessed on the record, keeping the retreatment guarantee (chemical) and any repair-guarantee question (structural) legally separate.

**Application math.**

*Trenchable section:* 125 ft × 4 ft depth × 0.4 gal/(ft·ft) = 200 gallons finished dilution.
*Rod-injected section (same rate, different delivery):* 40 ft × 4 ft depth × 0.4 gal/(ft·ft) = 64 gallons finished dilution.
*Total finished dilution:* 200 + 64 = 264 gallons.

*Concentrate required at 0.08% finished, 9.1% AI concentrate:*
oz concentrate per gallon of finished dilution = (0.08 ÷ 9.1) × 128 oz/gal ≈ 1.13 oz/gal.
264 gal × 1.13 oz/gal ≈ 298 oz ≈ 2.33 gallons of concentrate — just over one standard 2.5-gallon jug, so the technician orders a second partial container rather than stretching one jug thin to "make it stretch," which would silently drop the finished % below label minimum.

**Deliverable (service ticket, as filed):**

> **Retreatment — Warranty Claim #4471**
> Live subterranean termite activity confirmed, crawlspace pier B-3, mud tubes present. Visible damage noted, floor joist near patio access — observed, not structurally assessed; referred to [structural evaluator] before any repair-guarantee claim is opened.
> Treatment: fipronil 9.1% SC, 0.08% finished dilution. Trench-and-treat, 125 lf × 4 ft depth = 200 gal. Rod injection, patio-slab section, 40 lf × 4 ft depth = 64 gal (same finished rate, alternate method — slab prevented trenching). Total finished dilution: 264 gal; concentrate used: 2.33 gal.
> Wind at application: 6 mph (label max 10 mph) — compliant, logged.
> Warranty: retreatment guarantee renewed, annual, no repair coverage change pending structural evaluator report.
> Applicator license: [category — Termite/WDO], tech ID on file.

The point that survives to the warranty file: the barrier is now continuous across both delivery methods, the structural question is on a separate track from the chemical guarantee, and the math is on the record if the claim is ever contested.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled worksheets: trench-vs-rod method-switch decision, dilution/rate calculators, WDO report field template, warranty-type decision table.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for barrier gaps, label-rate pressure, callback patterns, and license/category mismatches.
- [`references/vocabulary.md`](references/vocabulary.md) — terms generalists conflate (REI vs. re-entry statement, retreatment vs. repair guarantee, misuse vs. off-label, WDO vs. WDI) with practitioner usage and common misuse.

## Sources

- FIFRA, 7 U.S.C. §136 et seq., specifically §12(a)(2)(G) (label-inconsistent use is unlawful) and §14 (civil/criminal penalty structure); state lead agencies (e.g., California DPR, Florida DACS, Texas Dept of Agriculture) enforce under FIFRA §23 cooperative agreements.
- EPA IPM principles (inspect/monitor → identify → threshold → least-hazardous control → evaluate); applied versions from university extension programs (UC Statewide IPM Program, Purdue and Ohio State urban entomology).
- *Mallis Handbook of Pest Control* (GIE Media/Questex, 11th+ ed.) — the standing industry reference text.
- NPMA (National Pest Management Association) training materials and the NPMA-33 Wood Destroying Insect Inspection Report format; NPMA's ACE (Associate Certified Entomologist) credential vs. ESA's BCE (Board Certified Entomologist) credential.
- Bobby Corrigan (RMC Pest Management Consulting) — rodent inspection/monitoring protocols widely cited in NPMA training.
- Liquid termiticide label conventions (e.g., fipronil-based SC formulations) for finished-dilution ranges and the trench/rod linear-foot-per-foot-of-depth rate; sulfuryl fluoride (structural fumigation) clearance procedure. Product-specific figures vary by registration and state — verify against the label in hand, not this file, before any application.
- No direct pest-control-worker practitioner has reviewed this file yet — flag corrections or gaps via PR.
