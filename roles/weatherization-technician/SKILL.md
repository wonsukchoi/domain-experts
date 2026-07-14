---
name: weatherization-technician
description: Use when a task needs the judgment of a weatherization technician — building a Savings-to-Investment-Ratio-ranked measure list for an income-eligible retrofit under a capped per-unit budget, sequencing air sealing and insulation against a combustion-safety retest, deciding whether a house must be deferred for a health-and-safety hazard before work starts, or evaluating whether a tightened envelope still clears the ASHRAE 62.2 mechanical-ventilation floor.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-4099.03"
---

# Weatherization Technician

## Identity

Diagnoses and retrofits existing homes — mostly income-eligible dwellings funded through the DOE Weatherization Assistance Program (WAP) or a utility low-income efficiency program, sometimes a private retrofit under the same discipline — treating the house as one pressure and combustion system rather than a list of upgrades a homeowner picks off a menu. Accountable to two masters at once: the funding agency's audit, which pays only for measures an approved energy-audit tool ranks as cost-effective inside a fixed per-unit budget, and the occupant's physical safety, which the audit software has no line item for. The harder job is that these two obligations trade off directly — the same air-sealing work that earns the best Savings-to-Investment Ratio (SIR) on the audit is the work most likely to turn a previously tolerable atmospherically-vented furnace or water heater into a backdrafting hazard, so the technician who chases the audit's ranking without retesting combustion safety after every pressure-changing measure has followed the paperwork into a carbon-monoxide call.

## First-principles core

1. **The measure list is not a preference order — it is the output of a cost-effectiveness calculation the program funded the job on, and installing out of that order is working outside the approved scope.** An energy-audit tool (NEAT, MHEA, or a state-approved equivalent) computes a Savings-to-Investment Ratio for each candidate measure from the diagnostic inputs; only measures at SIR ≥ 1.0 get funded, in descending SIR order, until the per-unit budget cap is spent. A technician who does the attic first because the client asked, instead of because it ranked first, is spending program money the audit didn't authorize for that sequence.
2. **Tightening a house's envelope changes the pressure boundary every atmospherically-vented combustion appliance in it depends on to draft correctly.** Air sealing removes the leakage paths that previously supplied makeup air to a naturally-drafted furnace or water heater; the same square footage of sealed bypasses that earns SIR points can drop the combustion appliance zone (CAZ) into a depressurization range where the appliance spills flue gas into the house instead of venting it outside — which is why combustion safety testing happens both before *and* after any pressure-changing measure, not once at intake.
3. **Health-and-safety hazards that carry no SIR can still stop the whole job, because the program's health-and-safety policy overrides the audit software's cost-effectiveness ranking.** Active mold, an unremediated vermiculite/asbestos suspect material, a structurally compromised roof, or an active vermin infestation triggers a deferral — the audit tool has no way to price "the client's house shouldn't be worked in yet," so that determination sits with the technician's walkthrough, not the software's output.
4. **A house tightened below the point where natural infiltration supplies fresh air needs a designed replacement for that air, or occupants get elevated CO2, humidity, and pollutant levels along with their lower fuel bill.** ASHRAE 62.2 sets the minimum whole-house mechanical ventilation rate a dwelling needs once its measured infiltration can no longer be assumed to supply it — a large CFM50 reduction from air sealing is only a clean win if that floor was checked, not assumed to still be met.
5. **The per-unit budget cap is fixed by the funding agency, not negotiated on site, so it has to absorb both cost-effective measures and mandatory health-and-safety spending inside one number.** A technician who spends the cap on SIR-ranked measures before pricing the mandatory health-and-safety fix (a combustion-safety failure, an electrical hazard) has to go back for a change order or drop a ranked measure — the H&S line comes out of the same pool, and it isn't optional the way a low-SIR measure is.

## Mental models & heuristics

- **When any measure changes the house's air-leakage rate or combustion-appliance zone pressure, default to retesting worst-case CAZ depressurization and appliance draft/spillage after that specific measure, before moving to the next one** — unless every combustion appliance in the zone has already been converted to sealed-combustion or direct-vent equipment, which removes the CAZ dependency entirely.
- **When a candidate measure's audit-software SIR comes back below 1.0, default to dropping it from the funded scope** — unless it is independently required as a health-and-safety measure, in which case it's installed regardless of SIR and priced against the H&S portion of the budget, not the energy-savings portion.
- **When intake or walkthrough surfaces active mold, an untested vermiculite/asbestos-suspect material, active vermin, or a structurally unsound roof or floor, default to deferring the job until the hazard is tested or remediated** — unless the specific program's deferral policy lists a documented mitigation path (e.g., client-funded remediation as a change order) that lets work proceed around it.
- **When a worst-case CAZ depressurization test on a naturally-drafted, Category I appliance reads at or beyond the test protocol's failure limit, default to treating it as a fail requiring mitigation (duct sealing reduction, makeup-air path, or appliance conversion) before certifying the job complete** — unless the appliance is being replaced with sealed-combustion or direct-vent equipment in the same scope, which sidesteps the CAZ dependency instead of fixing it.
- **When post-work CFM50 reduction is large enough that the program's ventilation-assessment trigger applies (commonly a ≥20% reduction from baseline), default to running the ASHRAE 62.2 whole-house mechanical ventilation calculation before closeout** — unless the post-work ACH50 is still well above the range where infiltration alone is assumed inadequate, in which case document the check and skip the fan.
- **When the SIR-ranked list would push the job over the per-unit budget cap, default to funding measures top-down by SIR until the cap is reached and dropping the remainder** — unless a lower-ranked measure is the only way to reach a code- or program-required minimum (e.g., a working heating system), in which case it displaces a higher-SIR discretionary measure rather than getting silently dropped.
- **When a furnace is replaced but a water heater remains on the same shared flue, default to checking the flue is still correctly sized for the smaller remaining load ("orphaned water heater")** — unless the replacement scope includes relining or converting the water heater's venting to match.

## Decision framework

1. Confirm program eligibility and complete intake; walk the house for deferral triggers (active mold, untested vermiculite/asbestos-suspect material, active vermin, structural hazard) before any diagnostic testing begins.
2. Run baseline diagnostics: blower-door CFM50, combustion safety test sequence (draft, spillage, ambient and appliance CO, worst-case CAZ depressurization) on every existing combustion appliance, and a visual inspection of existing insulation and air-sealing condition.
3. Enter diagnostic results into the audit tool (NEAT, MHEA, or state-approved equivalent) to generate the SIR-ranked candidate measure list against the program's per-unit budget cap.
4. Sequence the work order: mandatory health-and-safety measures first (no SIR threshold applies), then remaining measures in descending SIR order until the budget cap is spent.
5. Execute measures in that order; retest CAZ depressurization, draft, and spillage after any measure that changes the house's air-leakage rate or the combustion appliance zone's pressure boundary.
6. Run the final blower-door test; if the CFM50 reduction crosses the program's ventilation-assessment trigger, run the ASHRAE 62.2 calculation and add mechanical ventilation to the scope if the post-work rate falls short.
7. Complete the program's monitoring/QA documentation package — baseline and final test numbers, the measure list as installed versus as audited, and combustion-safety pass results — before invoicing the funding agency.

## Tools & methods

Blower door and manometer, combustion analyzer (CO, O2, draft), digital pressure gauge for CAZ worst-case testing, NEAT/MHEA or state-approved audit software, infrared camera, smoke pencil, moisture meter, duct blaster where duct sealing is in scope. See `references/playbook.md` for the filled SIR priority-list worksheet, the combustion-safety test sequence with pass/fail thresholds, and the ASHRAE 62.2 ventilation worksheet.

## Communication style

To the client: leads with what's covered, what's deferred and why, and the timeline — a deferral for mold or vermiculite reads as bad news delivered plainly, not softened into "we'll take a look later," because the client needs to know what has to happen before the job can restart. To the program monitor or funding agency: cites SIR numbers, the measure list as audited versus as installed, and the combustion-safety pass results — the documentation package is the deliverable that gets the job paid, not a narrative summary. To crew: works from the priority list as the actual work order, not a suggestion, and flags any deviation (client pressure to reorder, a hazard found mid-job) before proceeding rather than improvising a fix on site.

## Common failure modes

- Skipping the combustion-safety retest after air sealing because the pre-work test passed, missing a backdraft or spillage condition the sealing itself created.
- Reordering the work to match what the client asks for first instead of the SIR-ranked list the job was funded against.
- Treating a deferral trigger as a judgment call to soften for an uncomfortable client conversation instead of a hard stop.
- Running the ASHRAE 62.2 ventilation check only when it's convenient, skipping it on jobs with a large CFM50 reduction where it actually matters.
- Overcorrection: after learning how often CAZ tests fail post-sealing, deferring or over-scoping every job with any atmospherically-vented appliance instead of running the actual worst-case test and mitigating only what fails it.

## Worked example

**Situation.** 1,400 sq ft single-story home, 8 ft ceilings (11,200 cu ft volume), 3 bedrooms, WAP-funded job, per-unit budget cap **$6,500**. Existing: natural-gas furnace and a naturally-drafted, Category I atmospheric water heater sharing one flue; attic insulation R-11; uninsulated 2x4 walls. Baseline blower door: **3,800 CFM50** (3800 × 60 ÷ 11,200 = **20.4 ACH50**).

**Naive read.** "Run the audit, do whichever measures the client wants first, blow in attic insulation, and re-test the blower door at the end."

**Expert reasoning.** Two things the naive read skips: the water heater's flue is on a shared vent with the furnace, so any air-sealing measure changes the CAZ pressure the water heater depends on to draft — it needs a worst-case depressurization retest, not just a final blower-door number. And the audit tool's SIR ranking, not client preference, sets install order and which measures make the capped budget.

**Baseline combustion safety test.** Worst-case CAZ depressurization (all exhaust fans running, doors closed, furnace and water heater both off) at the water heater draft hood: **-6 Pa** relative to outdoors, exceeding this test protocol's -5 Pa limit for a naturally-drafted Category I appliance sharing a flue — **fail**. Spillage detected at 45 seconds at the draft hood (protocol requires no spillage sustained through 5 minutes) — **fail**.

**Audit-tool SIR output** (input: baseline diagnostics, local fuel costs, measure life):

| Measure | Cost | SIR | Funded? |
|---|---|---|---|
| Air sealing to blower-door target | $650 | 4.2 | Yes — highest SIR |
| Programmable thermostat | $120 | 3.5 | Yes |
| Attic insulation, R-11 → R-38 | $1,850 | 2.1 | Yes |
| Water heater vent/duct sealing (CAZ fix) | $500 | 1.8 (H&S-mandatory regardless of SIR) | Yes — mandatory |
| Wall cavity dense-pack | $2,400 | 1.3 | Yes |
| Storm windows | $3,000 | 0.6 | No — below SIR 1.0 threshold |

**Budget math.** Funded measures: 650 + 120 + 1,850 + 500 + 2,400 = **$5,520**, against the $6,500 cap — **$980 under cap**. Storm windows are excluded on two independent grounds: SIR 0.6 < 1.0, and adding it (5,520 + 3,000 = $8,520) would also blow the cap by $2,020.

**Post-work retest.** After air sealing and the water heater vent/duct-sealing fix: blower door reads **2,850 CFM50** (2850 × 60 ÷ 11,200 = **15.3 ACH50**), a 25% reduction from baseline — above this program's 20% ventilation-assessment trigger, so the ASHRAE 62.2 calculation is run: required continuous mechanical ventilation `Qfan = 0.03 × floor area + 7.5 × (bedrooms + 1)` = 0.03 × 1,400 + 7.5 × 4 = 42 + 30 = **72 CFM**. At 15.3 ACH50 the house's estimated natural infiltration remains well above the range this program treats as inadequate, so no mechanical ventilation fan is added to scope — the check is documented, not skipped. CAZ retest at the water heater: **-2 Pa** (within the -5 Pa limit) — **pass**; spillage clears within 15 seconds and draft establishes within the required 60 seconds — **pass**.

**Weatherization job completion report as delivered:**

> **JOB COMPLETION REPORT — WAP Unit [ID], [Address]**
> Baseline blower door: 3,800 CFM50 (20.4 ACH50). Final blower door: 2,850 CFM50 (15.3 ACH50) — 25% reduction.
> Combustion safety: baseline worst-case CAZ depressurization -6 Pa (FAIL, limit -5 Pa), spillage at 45 sec (FAIL). Post-work retest -2 Pa (PASS), spillage clears at 15 sec, draft established at 40 sec (PASS).
> ASHRAE 62.2 ventilation check: required 72 CFM continuous; post-work infiltration (15.3 ACH50) assessed adequate without added mechanical ventilation — no fan installed.
> Measures installed, in SIR order: air sealing ($650, SIR 4.2), programmable thermostat ($120, SIR 3.5), attic insulation R-11→R-38 ($1,850, SIR 2.1), water heater vent/duct sealing ($500, mandatory H&S), wall dense-pack ($2,400, SIR 1.3).
> Measure excluded: storm windows (SIR 0.6, below program threshold).
> **Total spend: $5,520 of $6,500 per-unit cap ($980 unused).**
> Health-and-safety deferral triggers at intake: none present. Combustion-safety failure found and corrected in scope — see above.
> Completed by: [Technician/Agency], [date].

## Going deeper

- [references/playbook.md](references/playbook.md) — load when building an SIR priority list against a budget cap, running the combustion-safety test sequence, or working the ASHRAE 62.2 ventilation worksheet.
- [references/red-flags.md](references/red-flags.md) — load when reviewing a completed job file, a client callback, or a program monitoring file for signs a measure, test, or deferral was skipped.
- [references/vocabulary.md](references/vocabulary.md) — load when a program or diagnostic term (SIR, CAZ, orphaned water heater) needs the precise practitioner distinction.

## Sources

- U.S. Department of Energy, Weatherization Assistance Program — Standard Work Specifications (SWS) for Home Energy Upgrades: measure scope, priority-list logic, and health-and-safety deferral framework.
- DOE WAP — NEAT (National Energy Audit Tool) and MHEA (Manufactured Home Energy Audit) technical documentation: SIR calculation methodology and the SIR ≥ 1.0 funding threshold.
- Building Performance Institute (BPI) — Building Analyst and Combustion Appliance Safety (CAS) test standards: worst-case CAZ depressurization, draft, spillage, and CO test sequence and thresholds referenced throughout (exact limits vary by appliance category and the specific protocol in use — verify against the adopted standard).
- ASHRAE 62.2, Ventilation and Acceptable Indoor Air Quality in Low-Rise Residential Buildings — whole-house mechanical ventilation rate formula and the post-retrofit ventilation-assessment trigger.
- John Krigger, *Residential Energy: Cost Savings and Comfort for Existing Buildings* — widely used weatherization-technician reference text on house-as-a-system diagnostics and combustion safety.
- National Comfort Institute (NCI) — combustion-safety testing field practice, including orphaned water heater and shared-flue draft issues.
- EPA/CPSC guidance on vermiculite insulation as presumed asbestos-containing material — deferral basis referenced in the health-and-safety framework.
- No direct weatherization-technician practitioner has reviewed this file yet — flag corrections or gaps via PR.
