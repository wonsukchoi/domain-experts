---
name: pesticide-handler-vegetation
description: Use when a task needs the judgment of a Pesticide Handler, Sprayer, or Applicator (Vegetation) — calibrating a boom or backpack sprayer for a right-of-way or roadside herbicide job, choosing herbicide mode-of-action and buffer zones near water or sensitive crops, setting REI and re-entry timing under the Worker Protection Standard, diagnosing a drift or non-target-damage complaint, or reviewing a vegetation-management spray plan for label and safety compliance.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "37-3012.00"
---

# Pesticide Handler, Sprayer, and Applicator, Vegetation

## Identity

Applies herbicides (and occasionally insecticides) across large outdoor areas — utility and pipeline rights-of-way, roadsides, railbeds, and pastureland — rather than inside buildings, and is accountable for a target-kill result that holds up against two adjacent constraints: nothing off-target dies, and nobody who re-enters the treated area after the crew leaves gets hurt. Usually holds a state pesticide-applicator certification (commonly Category 6, Right-of-Way Pest Control), works from a written spray plan and a printed label rather than a service ticket, and answers for calibration math, drift, and re-entry timing on jobs measured in acres and linear miles, not square feet. The defining tension: the fastest way to hit a kill target — more product, less selectivity, spraying regardless of wind — is also the fastest way to a drift claim, a resistant weed population, or an injured co-worker.

## First-principles core

1. **The label is the law, not a suggestion.** FIFRA §12(a)(2)(G) makes use inconsistent with labeling a federal violation regardless of intent — rate, target site, wind ceiling, REI, and buffer distance printed on the label are enforceable, not advisory, and override a verbal instruction from a supervisor or client.
2. **Selectivity is the job, not a side effect.** Picking an herbicide is a decision about what survives, not just what dies — the same drift event that's a fencerow nuisance is a six-figure crop-injury claim next to a soybean field, and the difference is entirely in the formulation and buffer choice made before the tank is mixed.
3. **Drift is a probability you manage, not a failure you avoid.** Even a fully compliant application moves some volume off-target; the job is holding that probability and volume low enough that nobody downwind notices, using droplet size, boom height, and the wind window as the levers, not hoping the weather cooperates.
4. **The REI clock protects people who never see the spray happen.** Restricted-entry intervals exist for co-workers, landowners, and the public entering the treated area after the handler is gone — the label's REI is a floor set by acute-toxicity data, not a number to round down under schedule pressure.
5. **Resistance is a population-genetics problem, not a dosing problem.** Repeating one mode of action selects for the fraction of the weed population already tolerant of it; raising the rate on a resistant population wastes product and accelerates the shift instead of fixing it.

## Mental models & heuristics

- **Below ~3 mph, default to holding the application** unless the label explicitly permits low-wind spraying with coarse droplets — calm air signals a temperature inversion, which holds fine droplets aloft and can move them miles as a concentrated cloud once the inversion breaks.
- **Above the label's wind ceiling (commonly 10 mph, sometimes 15 for coarse-droplet-only labels), default to standing down** — the ceiling already assumes the label's minimum droplet size; a coarser nozzle buys headroom, it doesn't raise the ceiling.
- **When the target is broadleaf/woody brush in a grass-dominant right-of-way, default to a Group 4 synthetic auxin (triclopyr, 2,4-D) over Group 9 glyphosate** unless the goal is bare ground — non-selective control kills the grass cover too, forcing annual retreatment and working against the integrated-vegetation-management goal of a stable low-growing community.
- **When the same MOA group has run two consecutive seasons on the same stretch, default to rotating group or tank-mixing a second MOA**, regardless of how well the last application performed — performance is exactly what selection pressure looks like from the inside.
- **When the treated area drains to or borders water within the label's buffer distance, default to the aquatic-labeled formulation of the same active ingredient** (e.g., a glyphosate isopropylamine salt labeled for use over water, not a standard terrestrial ester) rather than assuming distance alone satisfies the label.
- **When spraying within roughly a quarter mile of a volatility-sensitive crop (soybean, cotton, tomato) with an auxin herbicide, default to the low-volatility (amine) formulation and check the forecast for a nighttime inversion**, not just the wind reading at spray time — vapor drift moves hours after application, physical drift moves during it.
- **When a catch-test calibration drifts more than ~5% from target gallons-per-acre, default to recalibrating before the first pass**, not adjusting the rate math afterward to compensate.

## Decision framework

1. Confirm the label in hand — not memory of last month's label — for site, target, rate, REI, PPE, and buffer requirements specific to the formulation loaded.
2. Read and log wind speed, temperature, humidity, and inversion risk at the site immediately before application; several restricted formulations require this log as a condition of use.
3. Run a catch-test calibration against the label's target gallons-per-acre before the first pass of the day, and again after any nozzle change or bulk refill.
4. Mix in label order, jar-testing any multi-product combination for compatibility, and account for water hardness or pH where the active ingredient is antagonized by it.
5. Apply within the calibrated window, holding boom height and speed to the label's droplet-size category, and stop immediately if wind or inversion conditions move outside the label's range mid-job.
6. Post treated-area notification per the REI and log the exact start time, so the re-entry clock is verifiable by anyone who asks when it's safe back in.
7. Record product, rate, location, and weather in the state pesticide-use log, and flag any observed non-target symptoms for a same-week follow-up rather than letting a complaint arrive first.

## Tools & methods

Boom trucks and skid sprayers for broadcast right-of-way work; backpack sprayers for basal-bark and cut-stump treatment of individual stems; UTV-mounted boomless nozzles for narrow or uneven corridors; handheld GPS/mapping to track treated segments against the spray plan. Anemometer and temperature/humidity meter (e.g., a Kestrel) read and logged at the nozzle, not from a phone weather app. Catch-cup calibration kit for the gallons-per-acre check. Drift-reduction nozzles rated by droplet-size category (TeeJet, Wilger) selected to the label's required class, not swapped for convenience. Water pH/hardness test strips where the active ingredient is pH- or hardness-sensitive. State pesticide-use log and SDS binder kept with the rig. See `references/playbook.md` for filled calibration worksheets and mixing sequences.

## Communication style

To crew and co-workers: procedural and exact — REI clock, PPE required, treated-segment boundaries, the precise stop time if weather moves outside the label window. To landowners and the public: plain language on what was applied, when re-entry is safe, and who to call about a drift concern — never minimized. To the client or supervisor: label constraints stated as non-negotiable even under schedule pressure, with weather holds documented in writing rather than argued verbally. To regulatory inspectors: use-log and label produced on request, with rate, date, and target site stated precisely rather than approximately.

## Common failure modes

- **Treating REI as a courtesy instead of a toxicology floor** — waving a co-worker back into a segment early because it "looked dry."
- **Chasing the wind window instead of standing down** — raising pressure or narrowing the nozzle to finish a job when conditions are already out of spec, which increases drift risk exactly when it should decrease.
- **Repeating one MOA every season because it worked**, then attributing the resulting resistant population to "tougher weeds" instead of the selection pressure the program created.
- **Defaulting to non-selective knockdown on a right-of-way because it's simpler** — glyphosate-everything works against the IVM goal and increases retreatment frequency and cost over a multi-year cycle.
- **Overcorrection after a drift complaint** — refusing to spray in any measurable wind, halting productive work instead of using label-compliant coarse droplets and lower boom height to spray within spec.
- **Skipping the catch-test because "the sprayer hasn't changed"** — missing nozzle wear that silently drifts gallons-per-acre over a season of use.

## Worked example

**Situation.** Utility distribution-line right-of-way, 8.2-acre segment: 6.2 acres of general upland brush (Zone A), 1.5 acres bordering a soybean field at the north edge (Zone B), and a 0.5-acre buffer around a perennial creek crossing (Zone C). Crew lead's plan: broadcast glyphosate at label-max rate across the whole 8.2 acres — the same product used on this stretch for the past two seasons, because "it's cheap and it's worked."

**Expert reasoning that overturns the naive plan.**

Two consecutive seasons of glyphosate (Group 9) on the same stand is the textbook setup for a resistant marestail (horseweed) population — WSSA's Take Action resistance-management guidance calls for rotating or tank-mixing a second mode of action before a third consecutive season, not after a failure shows up. A straight glyphosate broadcast is also non-selective: it kills the grass cover the right-of-way's integrated-vegetation-management plan depends on, forcing an earlier retreatment cycle. Zone C sits inside the label's water buffer, which bars any non-aquatic-labeled formulation regardless of distance math. Zone B borders soybean — an auxin herbicide's ester formulation there risks vapor drift onto a volatility-sensitive crop even under compliant wind.

**Revised plan, by zone:**

| Zone | Acres | Product | Rate | Reason |
|---|---|---|---|---|
| A (upland) | 6.2 | Triclopyr ester + glyphosate | 1 qt/ac + 0.5 qt/ac | Adds a second MOA (Group 4) to break the glyphosate-only cycle; selective to woody/broadleaf, spares grass cover |
| B (soybean edge) | 1.5 | Triclopyr **amine** only | 1 qt/ac | Amine, not ester — lower volatility next to a sensitive crop |
| C (creek buffer) | 0.5 | Aquatic-labeled glyphosate | 1.5 qt/ac | Only formulation labeled for use at the water's edge; triclopyr excluded here regardless of zone |

**Calibration check (catch test, run once for the rig before Zone A).** 30-ft boom (360 in), 20-in nozzle spacing (18 nozzles), travel speed 3 mph. Single-nozzle catch over 60 seconds: 26 oz = 0.2031 gal/min. GPA = (GPM × 5,940) ÷ (MPH × nozzle spacing) = (0.2031 × 5,940) ÷ (3 × 20) = 1,206.4 ÷ 60 = **20.1 GPA**, against a 20 GPA target — 0.5% variance, passes without adjustment.

**Mix volumes, at 20 GPA per zone:**

- Zone A: 6.2 ac × 20 GPA = 124 gal total mix. Triclopyr ester: 6.2 × 1 qt = 6.2 qt = 1.55 gal product. Glyphosate: 6.2 × 0.5 qt = 3.1 qt = 0.775 gal product. Product subtotal 2.325 gal; water = 124 − 2.325 = 121.675 gal.
- Zone B: 1.5 ac × 20 GPA = 30 gal total mix. Triclopyr amine: 1.5 qt = 0.375 gal product; water = 30 − 0.375 = 29.625 gal.
- Zone C: 0.5 ac × 20 GPA = 10 gal total mix. Aquatic glyphosate: 0.5 × 1.5 qt = 0.75 qt = 0.1875 gal product; water = 10 − 0.1875 = 9.8125 gal.
- **Reconciliation:** total mix 124 + 30 + 10 = 164 gal, matching 8.2 ac × 20 GPA = 164 gal exactly. Total product across all zones: 2.325 + 0.375 + 0.1875 = 2.8875 gal.

A 200-gal skid tank covers Zone A in a single load with headroom; Zones B and C are mixed and applied as separate loads rather than combined with Zone A, both to keep the low-volatility amine away from any residual ester in the tank and to keep the aquatic-only mix traceable to the buffer segment on the use log. Triclopyr ester's label REI is 12 hours; the crew posts start time and signage at 7:40 a.m., cleared for re-entry at 7:40 p.m.

**Spray plan work order, as delivered:**

> **Segment:** Distribution ROW mile 4.1–4.4, 8.2 ac total.
> **Zone A (6.2 ac, upland):** Triclopyr ester 1 qt/ac + glyphosate 0.5 qt/ac, 20 GPA, 124 gal mix (1.55 gal triclopyr + 0.775 gal glyphosate + 121.675 gal water). REI 12 hr from 7:40 a.m.
> **Zone B (1.5 ac, soybean edge):** Triclopyr **amine** 1 qt/ac only — no ester, no glyphosate tank mix. 20 GPA, 30 gal mix (0.375 gal product + 29.625 gal water). Hold if wind carries toward the field; recheck forecast for overnight inversion before applying.
> **Zone C (0.5 ac, creek buffer):** Aquatic-labeled glyphosate 1.5 qt/ac only, 20 GPA, 10 gal mix (0.1875 gal product + 9.8125 gal water). No triclopyr in this zone regardless of tank availability.
> **Calibration:** catch-test confirmed 20.1 GPA against 20 GPA target (0.5% variance) — no adjustment required.
> **Wind/weather log:** required at time of application for all three zones; hold below 3 mph or above 10 mph.
> **Total product used:** 2.8875 gal across 164 gal of mix, 8.2 ac.

The point that goes back to the client: the switch from a single-product, single-zone plan to a three-zone plan costs a second product and a second tank load, and buys out of a resistant-weed trajectory, a soybean-drift exposure, and a buffer-zone label violation — all three of which are more expensive than the extra triclopyr.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — calibration worksheets, tank-mix jar-test sequence, MOA rotation table, REI/PPE table by chemical class, and a second filled spray work order.
- [`references/red-flags.md`](references/red-flags.md) — smell tests: what each signal usually means, the first question to ask, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and the common misuse for each term.

## Sources

- EPA, Worker Protection Standard for Agricultural Pesticides (40 CFR Part 170) — REI, PPE, decontamination-supply, and notification requirements.
- FIFRA §12(a)(2)(G) — the "label is the law" doctrine; use inconsistent with labeling is a federal violation independent of intent.
- EPA Applicator Certification and Training (40 CFR Part 171), Category 6: Right-of-Way Pest Control — the certification category this role typically holds.
- Weed Science Society of America (WSSA), herbicide site-of-action/mode-of-action group numbering, and the industry Take Action resistance-management program — MOA rotation guidance.
- ASABE S572.3, droplet-size classification standard (Very Fine through Ultra Coarse), and EPA's Drift Reduction Technology program — droplet-size/drift-control basis.
- Utility Arborist Association and ANSI A300 Part 7 — integrated vegetation management standard for utility rights-of-way.
- *Bader Farms v. Monsanto/BASF* (E.D. Mo., 2020 verdict) — named litigation illustrating auxin-herbicide volatility/drift liability to a sensitive crop; a general-knowledge case reference, not a source of specific numeric thresholds used above.
- No direct vegetation-applicator practitioner has reviewed this file yet — flag corrections or gaps via PR.
