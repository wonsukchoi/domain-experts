# Energy Auditor — Playbook

## Diagnostic testing sequence and what each gates

| Order | Test | What it measures | What it gates |
|---|---|---|---|
| 1 | Utility billing pull (12 mo, weather-normalized) | Actual metered baseline consumption | The truth check every later savings estimate is reconciled against |
| 2 | Walkthrough (envelope, equipment, visible moisture/staining) | Assembly types, insulation levels, equipment age/efficiency | Which diagnostic tests are needed and where |
| 3 | Blower door (CFM50/ACH50) | Whole-house envelope leakage | Whether air sealing is indicated and to what target |
| 4 | Duct leakage test (total + to-outside CFM25) | Forced-air duct leakage | Whether duct sealing precedes insulation/air-sealing in that zone |
| 5 | Combustion safety: worst-case CAZ depressurization, spillage, ambient/flue CO | Backdraft risk for every fuel-burning appliance | Whether any air-sealing work in that zone can proceed at all |
| 6 | Reconciliation against billing baseline | Whether diagnostics + walkthrough explain the metered bill | Whether more investigation is needed before computing savings |

**Use:** Combustion safety (step 5) is not optional and not last because it's least important — it's tested after the blower door specifically because worst-case depressurization has to be induced with exhaust fans and other air-moving equipment running, which is easiest to stage once the envelope test crew and equipment are already on site.

## Blower door: CFM50 to ACH50 (filled example)

| Step | Value |
|---|---|
| Measured CFM50 | 3,200 CFM |
| House volume (1,800 ft² x 8 ft ceiling) | 14,400 ft³ |
| ACH50 = (CFM50 x 60) / volume | (3,200 x 60) / 14,400 = **13.33 ACH50** |
| 2021 IECC prescriptive target, climate zones 3-5 | 3.0 ACH50 |
| Typical WAP post-work target (existing-home retrofit, zone 5) | 6-8 ACH50 — full code-level tightening is rarely cost-effective or achievable on an existing envelope in one pass |

**Use:** Existing-home retrofit targets are not the new-construction code number — treat the IECC figure as the ceiling of ambition, not the retrofit goal, unless the scope includes full envelope reconstruction.

## Duct leakage test (filled example)

| Step | Value |
|---|---|
| Total leakage (CFM25) | 220 CFM25 |
| Leakage to outside (CFM25) | 140 CFM25 |
| Conditioned floor area | 1,800 ft² |
| Leakage to outside per 100 ft² = (140 / 1,800) x 100 | **7.78 CFM25 per 100 ft²** |
| 2021 IECC threshold | 4.0 CFM25 per 100 ft² |
| Result | Fails — 94% over threshold; sequence duct sealing before insulation/air-sealing in this zone |

**Use:** Total leakage and leakage-to-outside are different numbers — a system can have high total leakage inside conditioned space (wasted but not lost) and still pass the to-outside threshold, or the reverse. Report both; only leakage-to-outside gates the sequencing decision.

## Combustion safety: worst-case CAZ depressurization and spillage (filled example)

| Condition | Pressure reading | Call |
|---|---|---|
| Idle (no exhaust fans, doors open) | -1 Pa | Not representative — do not report as the safety finding |
| Worst case (exhaust fans + dryer running, interior door to CAZ closed) | -7 Pa | Below -5 Pa mitigation threshold — fail |
| Spillage test at worst case (water heater draft hood, smoke pencil or mirror) | Spillage persists through full test | Fail — appliance is backdrafting at worst case |

| CAZ pressure range | Action |
|---|---|
| 0 to -2 Pa | Pass, no action |
| -2 to -5 Pa | Marginal — attempt mitigation (make-up air, duct interlock) and retest before any other call |
| Below -5 Pa with spillage failure | Fail — exclude zone from air-sealing scope until resolved; recommend mitigation attempt first, appliance replacement/power-vent conversion only if mitigation retest still fails |

**Use:** Mitigation before replacement is the default sequence on cost grounds ($150 make-up air attempt vs. $1,200 power-vent conversion) — but if a mitigation retest still fails, don't attempt a second mitigation approach on the same visit; escalate to replacement rather than repeatedly re-testing a fix that already didn't work.

## Ambient CO action levels (BPI)

| Reading | Required action |
|---|---|
| 9-35 ppm | Further investigation before closing the job; identify source before proceeding |
| 36-69 ppm | Appliance shutdown and remediation required before any other work proceeds |
| 70+ ppm | Occupant evacuation and emergency notification |

**Use:** These are step-function thresholds, not a sliding scale — a 34 ppm reading and a 9 ppm reading get the same "investigate before closing" response; a 36 ppm reading gets a materially different response than a 35 ppm reading, so record the exact figure, not a rounded one.

## SIR ranking and package assembly (filled example)

| Measure | Annual savings | Installed cost | Measure life | PV annuity factor (3%) | PV(savings) | SIR | In funded package? |
|---|---|---|---|---|---|---|---|
| Attic insulation R-19 to R-49 | $112 | $1,850 | 20 yr | 14.88 | $1,666.56 | 0.90 | No — below 1.0 cutoff |
| Duct sealing to outside | $71 | $450 | 15 yr | 11.94 | $847.70 | 1.88 | Yes |
| Air sealing to ACH50 8 | $157 | $650 | 20 yr | 14.88 | $2,335.70 | 3.59 | Yes |
| CAZ mitigation (make-up air) | n/a — health & safety | $150 | n/a | n/a | n/a | n/a (exempt from SIR test) | Yes — mandatory |

**Use:** SIR = PV(annual savings, at the measure's own service life and the program's discount rate) / installed cost. A measure below 1.0 is not "close enough" — it's excluded from the funded package unless bundling it with another measure raises the blended SIR above 1.0, in which case report the bundle's SIR, not each measure's individually.

## Scope of work — filled deliverable template

> **Energy Audit Scope of Work — [Address], Permit/Job #[ID]**
> **Baseline:** [fuel] [usage]/yr ($[cost]), [fuel] [usage]/yr ($[cost]), total $[total]/yr, weather-normalized against 12-month billing.
> **Health & safety — mandatory, precedes all envelope work:** [appliance] fails [test] at [reading] (limit [threshold]). [Mitigation attempt and cost] before authorizing [replacement and cost]. No air-sealing work proceeds in [zone] until this item clears.
> **Funded measures (SIR >= 1.0):**
> 1. [Measure]: $[cost] installed, $[savings]/yr savings, SIR [value].
> 2. [Measure]: $[cost] installed, $[savings]/yr savings, SIR [value].
> **Excluded from funded package:** [Measure] — corrected savings $[savings]/yr against $[cost] installed cost, SIR [value]. Does not clear program cost-effectiveness on its own; [re-evaluation condition].
> **Funded package total:** $[total] installed; predicted annual energy savings $[total]/yr, excluding the health-and-safety line.

**Use:** Every excluded measure gets its SIR reported, not just omitted — a funder or homeowner reviewing the file needs to see that the measure was evaluated and failed the cutoff, not that it was overlooked.
