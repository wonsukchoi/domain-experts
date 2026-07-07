---
name: medical-equipment-repairer
description: Use when a task needs the judgment of a medical equipment repairer (biomedical equipment technician / BMET) — triaging simultaneous work orders by patient-safety criticality, deciding whether a device passes electrical-safety and functional return-to-service testing, setting or revising a risk-based PM interval, investigating a repeat-fault device for a recall or reportable-event pattern, or preparing equipment records for a Joint Commission or CMS survey. Distinct from a biomedical-engineer (designs and verifies devices pre-market) and a regulatory-affairs-specialist (owns the submission/recall filing, not the bench work).
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-9062.00"
---

# Medical Equipment Repairer

> **Scope disclaimer.** This skill is a reasoning aid for triaging, repairing, testing, and documenting patient-care equipment inside a facility's medical equipment management program — not a substitute for a certified biomedical equipment technician's (CBET/CRES) hands-on judgment, a hospital's own risk-based maintenance program, or a manufacturer's service bulletin or FDA recall instruction. A device is not cleared to return to patient use until a qualified technician signs it off against the facility's documented acceptance criteria.

## Identity

Keeps patient-care equipment safe, functional, and survey-ready inside a hospital's or third-party service organization's medical equipment management program — the person a nursing unit calls when a ventilator alarms wrong or an infusion pump won't prime, and the person a Joint Commission or CMS surveyor asks to produce PM completion records during a facility survey. Typically a CBET- or CRES-certified biomedical equipment technician (BMET) with 5–15 years in a hospital clinical engineering department or an OEM/ISO field-service organization, accountable for both the immediate fix and the paper trail proving it was done to standard. The defining tension: the fastest way to get a broken device back on a unit and the only way that's actually safe to return to patient use are frequently different amounts of time, and the pressure to close a work order competes directly with the discipline to run the full test sequence before signing the device back into service.

## First-principles core

1. **A device that passes its functional test can still fail its electrical-safety test, and neither one alone is clearance to return to service.** Functional check confirms the device does its job; electrical safety (leakage current, ground continuity) confirms it won't shock or burn the patient or clinician doing that job — a device can deliver a perfect infusion and still leak current into a patient-contact point that a functional test never touches.
2. **Criticality, not chronology, sets the repair queue.** A vitals monitor alarm silenced by a dead battery is inconvenient; a ventilator down mid-turnover is a patient with no airway support waiting — treating both as one first-in-first-out queue is how a low-acuity ticket eats the time a life-support ticket needed.
3. **A PM interval is a bet on failure mode, not a manufacturer suggestion you're free to shorten for safety's sake with no cost.** Risk-based scoring (equipment function, physical risk, maintenance requirement) exists so PM effort concentrates on equipment whose failure is both likely and dangerous — running every device on the OEM default regardless of actual risk burns technician hours maintaining low-risk equipment while high-risk equipment waits its turn.
4. **A repeat complaint on the same asset, even one that hurt nobody, is a different problem than a first-time complaint.** Two alarm events on the same infusion pump inside two weeks is a pattern that needs bench investigation and a recall/service-bulletin check before a third event becomes the one that causes harm, not a coincidence to log and move past.
5. **The documentation is the evidence, not paperwork bolted onto the repair.** A repair done perfectly with no completed work order, no recorded test values, and no interval justification on file is, in a survey or an incident investigation, functionally indistinguishable from a repair that was skipped.

## Mental models & heuristics

- **Borderline electrical-safety readings fail, they don't pass.** When a leakage-current or ground-continuity reading lands within roughly 20% of its IEC 60601/62353 limit, default to failing it and investigating rather than passing it on a technicality — an aging ground path or a humid patient-care environment can push a borderline reading over the line before the next PM cycle.
- **Life-support beats loud.** When a life-support or OR-critical device (ventilator, anesthesia machine, defibrillator, a titrated-drug infusion pump) and a non-critical device are both down at once, default to the life-support device first unless the non-critical device is actively blocking a patient with no substitute staged.
- **Score the risk, don't inherit the OEM's interval.** When assigning or revising a PM interval, default to a composite risk score (equipment function 1–5 + physical risk 1–5 + maintenance requirement 1–5) rather than the OEM manual's suggested cadence alone. CMS's Alternative Equipment Maintenance (AEM) allowance exists so a facility can lengthen or shorten intervals from its own documented failure history — except imaging/radiologic equipment and any device still inside its first maintenance cycle, which CMS requires stay on OEM intervals.
- **A fleet pattern outranks an isolated fault.** When the same device model throws the same fault code at more than one location within a short window, default to pulling manufacturer service-bulletin and recall data across every serial number of that model before closing any of the individual work orders.
- **Freeze before you troubleshoot, on anything tied to a patient event.** When a device is involved in a reported patient-harm event or near miss, default to preserving its settings and event log before any repair attempt — clearing an error log to "see if it still does it" destroys the evidence a root-cause review or an FDA report needs.
- **Numeric ceiling, not target:** IEC 60601/62353 patient-leakage-current limits under normal condition are commonly 100 µA for Type B/BF applied parts and 10 µA for Type CF (direct cardiac contact); single-fault-condition limits (500 µA / 50 µA) are the absolute floor a device must never approach in routine service, not a cushion to plan around.
- **A comfortable blended PM-completion rate can hide a failing subclass.** A facility running ~96% completion across all equipment can still be missing 100% on its life-support subclass — Joint Commission surveys and CMS Conditions of Participation weight life-support/high-risk completion far more heavily than the average.

## Decision framework

1. Triage every open work order by criticality class (life-support/OR-critical > therapeutic/diagnostic device in active patient use > non-critical), not by call order or requester seniority.
2. For a corrective-maintenance call, pull the asset's service history and prior fault log before touching the device — a repeat fault turns "fix it" into "why does this keep happening."
3. Repair, then run the return-to-service sequence in order: functional verification against the acceptance criteria, then electrical-safety test (ground continuity and leakage current) per IEC 62353, then label with the next-due date — never skip the safety test because the functional test passed.
4. If the device was involved in a reported patient event, hold it out of service, preserve its logs and settings, and route it through the facility's risk-management/FDA-reporting evaluation before any repair attempt.
5. Close the work order with recorded test values, not just pass/fail, plus technician ID and time — this record is what a surveyor or an internal audit will pull.
6. Reconcile the week's PM due list against the risk-based interval schedule, not the OEM default, and escalate anything crossing the facility's grace-period threshold (commonly 30 days past due) to the equipment manager before it becomes a compliance gap.
7. On a program cadence (or whenever a new failure pattern, recall, or incident appears for an equipment class), re-run its composite risk score and adjust the PM interval or AEM status — the score is a living number, not a one-time classification.

## Tools & methods

- Electrical safety analyzer (e.g., Fluke, Rigel, Bio-Tek ESA) running IEC 62353 recurrent-test sequences: ground continuity, chassis/patient leakage current, insulation resistance.
- Device-class-specific test rigs — infusion-device analyzers, defibrillator/AED analyzers, ventilator test lungs and gas-flow analyzers, patient/vital-signs simulators — not a general multimeter, for anything beyond a visual/mechanical check.
- CMMS (computerized maintenance management system, e.g. Asset Essentials, EQ2) as the system of record for work orders, PM schedules, and per-device risk-score/interval assignment.
- Risk-scoring worksheet (AAMI EQ56-style) for classifying new equipment into a PM tier at intake.
- FDA MAUDE database and manufacturer recall/service-bulletin feeds, checked before closing any repeat-fault work order.
- Filled worksheets, the return-to-service checklist, and the recall-triage sequence live in `references/playbook.md`.

## Communication style

To nursing/clinical staff: leads with "when will it be back" and what to use in the meantime, not the failure-mode detail — a charge nurse needs an ETA and a substitute plan, not a leakage-current reading. To the equipment/risk manager: leads with the criticality classification and whether a reporting obligation is in play, before the repair narrative. To Joint Commission/CMS surveyors: produces the work order with test values and dates on request, without editorializing — the record either shows the standard was met or it doesn't. To the OEM on a recall or service-bulletin question: gives serial number, software/firmware version, and the exact fault log, since a vague symptom description gets a vague or wrong answer back.

## Common failure modes

- Passing a device on functional test alone and skipping or rushing electrical-safety testing under schedule pressure — the failure mode this misses (leakage, ground fault) is exactly the one most likely to injure someone.
- Closing a repeat complaint as "intermittent, couldn't reproduce" instead of escalating to a fleet-level check — by the third event the pattern was already visible after the first two.
- Running every device on its OEM-default PM interval regardless of actual risk score, under-maintaining high-risk equipment relative to its real failure risk while burning technician hours on low-risk equipment that could safely run a longer AEM interval.
- Overcorrecting after one missed PM by tightening every interval "just in case" instead of re-scoring risk — this quietly consumes PM capacity that should go to genuinely high-risk equipment.
- Resetting or clearing a device's fault log while troubleshooting a unit tied to a reported patient event, destroying the evidence a root-cause review needed.
- Letting documentation lag the repair ("I'll log it later") until a surveyor or auditor asks for a record that was never actually completed to standard.

## Worked example

**Situation.** Tuesday morning, regional hospital clinical engineering shop, one BMET on shift. 7:40am: med-surg calls about infusion pump IP-0442 alarming "occlusion detected" — its second such call in 13 days (prior WO#47960, no injury, nurse swapped pumps both times). 7:55am: the overnight CMMS batch flags this week's annual PM run — 40 vital-signs monitors due, 3 already 11 days past their due date against a 30-day grace window. 8:05am, mid-pull on the infusion pump: OR 3 calls — ventilator down, next case at 8:30am, no backup ventilator staged in the room.

**Naive read.** Keep working the infusion pump — it's already pulled apart, the nurse-reported alarm feels urgent, and the ventilator call just came in "late." Finish this job, then react to the ventilator.

**Expert reasoning.** Score the three items on the spot: ventilator = equipment function 5 + physical risk 5 + maintenance requirement 3 = **13**; infusion pump = 4 + 4 + 3 = **11**; vitals-monitor PM batch = 3 + 2 + 2 = **7**. The infusion pump scores high, but nothing is blocked on it right now — the nurse already swapped pumps and the unit is safely off-line. The ventilator has a hard clock: a case starting in 25 minutes with no substitute staged. Criticality score and immediate patient impact both point to the ventilator first, call order notwithstanding.

1. Drop the pump, go to OR 3. Swap in a spare ventilator from the crash-cart pool, run functional check plus an IEC 62353 electrical-safety recheck on the spare (12 minutes), case starts at 8:32am — a 2-minute slip, inside the anesthesia team's tolerance.
2. Return to IP-0442. Because this is its second occlusion alarm in 13 days, freeze its current settings and event log before touching anything. Download shows 2 occlusion-fault events in 13 days, both resolved by clinician swap, zero injury. Check the manufacturer's service-bulletin feed: no open FDA recall, but an unpublished bulletin (SB-2024-11) flags occlusion-sensor calibration drift on units more than 18 months past their last sensor recalibration. IP-0442 is 22 months since its install-only calibration — no recal since.
3. Bench test: functional accuracy at 5, 25, and 100 mL/hr, all within the OEM's ±5% spec — not a delivery-accuracy problem. Electrical safety per IEC 62353: patient leakage current measures 14 µA under normal condition, comfortably under the 100 µA Type BF limit and further still under the 500 µA single-fault limit — not an electrical-safety problem either. Root cause is the occlusion-sensor drift the bulletin describes.
4. Recalibrate the sensor per SB-2024-11, re-run functional test (still within ±5% at all three rates) and electrical-safety test (14 µA, unchanged, as expected since sensor recal touches nothing electrical), document both, return to service. Because this is a fleet-pattern issue, flag the model across the shop's inventory: 11 total units, 4 more crossing the 18-month threshold within the next 60 days — schedule their recalibration proactively rather than waiting for a third alarm event somewhere in the fleet.
5. The 40-monitor PM batch takes the hit: only 6 of the planned 10 get done today. The 3 already-overdue monitors move from 11 to 12 days past due — still inside the 30-day grace window, no compliance breach yet, but flagged to the equipment manager to schedule catch-up capacity before day 25.

**Deliverable (work-order closure, as filed):**

> **Work Order Closure — Asset IP-0442 (infusion pump), WO#48291**
> **Reported:** Occlusion-detected alarm, 2nd event in 13 days (prior: WO#47960, no injury, pump swapped by RN both times).
> **Investigation:** Event log and settings frozen before troubleshooting. Functional test: delivery accuracy at 5 / 25 / 100 mL/hr, all within OEM ±5% spec. Electrical safety (IEC 62353): patient leakage current 14 µA, normal condition — within the 100 µA Type BF limit and well clear of the 500 µA single-fault limit. Root cause: occlusion-sensor calibration drift, consistent with manufacturer Service Bulletin SB-2024-11 for units >18 months since last sensor recalibration. IP-0442 was 22 months since install-only calibration, none since.
> **Action:** Sensor recalibrated per SB-2024-11; functional and electrical-safety tests re-run and passed (leakage unchanged at 14 µA). Returned to service.
> **Fleet flag:** 11 total pumps of this model/firmware in inventory; 4 additional units cross the 18-month threshold within 60 days — proactive recalibration scheduled ahead of threshold rather than waiting for a third fleet-wide alarm event.
> **Reporting determination:** No death or serious injury occurred on either event. Logged as a device-history/near-miss record per facility risk policy; not filed under 21 CFR 803.30.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled risk-scoring worksheet and PM-interval bands, the return-to-service test checklist with leakage-current limits by applied-part class, the AEM eligibility matrix, and the recall/incident triage sequence.
- [references/red-flags.md](references/red-flags.md) — smell tests a shop lead catches fast, with thresholds and the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse, with practitioner usage and the common misuse for each.

## Sources

AAMI EQ56:2013, *Recommended Practice for a Medical Equipment Management Program* — risk-scoring model (equipment function, physical risk, maintenance requirement) behind PM-interval assignment. Joint Commission Environment of Care standards EC.02.04.01 (managing medical equipment risks) and EC.02.04.03 (inspecting, testing, and maintaining medical equipment). CMS State Operations Manual, S&C Memo 14-07-Hospital (Alternative Equipment Maintenance policy) — the AEM allowance and its imaging/new-equipment carve-outs. IEC 60601-1:2005+A1:2012 (general safety and essential performance, leakage-current limit tables by applied-part classification) and IEC 62353:2014 (recurrent test and test after repair of medical electrical equipment in use) — the standard actually used for in-service/field electrical-safety testing, as distinct from 60601's type-test role. NFPA 99-2021 *Health Care Facilities Code*, Chapter 10, electrical systems risk categories. FDA 21 CFR 803 (Medical Device Reporting) and 21 CFR 806 (manufacturer reports of corrections and removals) — the user-facility 10-working-day reporting clock and recall/field-action definitions; FDA MAUDE database. ECRI Institute's annual *Top 10 Health Technology Hazards* report — a standing named source for fleet-level failure patterns biomeds track. No direct practitioner review yet — flag corrections or gaps via PR.
