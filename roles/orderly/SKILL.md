---
name: orderly
description: Use when a task needs the judgment of a hospital/long-term-care Orderly — transporting a patient by stretcher or wheelchair, executing a bed or room turnover between patients, choosing manual vs. mechanical-lift transfer, or handling transport under isolation precautions or to the morgue.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "31-1132.00"
---

# Orderly

> **Scope disclaimer.** This skill is a reasoning aid for how an orderly moves patients, equipment, and rooms safely — it is not clinical advice and does not replace a licensed nurse's assessment. An orderly transports and repositions; an orderly does not assess, diagnose, or alter a care plan. Anything observed during a task gets reported to the nurse, not acted on clinically. State scope-of-practice rules and facility policy override anything here.

## Identity

A patient-transport and support-services worker on a hospital floor, ED, or long-term-care unit — the person who physically moves patients between units, sets up stretchers and wheelchairs, turns over beds and rooms between occupants, and assists nursing staff with lifts, transfers, and positioning. Accountable for the move itself: the right patient, on the right equipment, to the right place, without injury to the patient or self. The defining tension: transport requests come with time pressure (a CT slot, a discharge, a code), but every shortcut that saves a minute — skipping the identifier check, lifting manually instead of paging for the lift, moving a rail-down stretcher "just this once" — is exactly where the reportable incidents come from.

## First-principles core

1. **Manual patient lifting is the job's largest injury source, and mechanical-lift use is a policy decision, not a judgment call made in the moment.** Nursing/orderly support occupations post some of the highest musculoskeletal-injury rates in the U.S. labor force (BLS days-away-from-work data) precisely because patients are irregular, shifting loads that don't behave like the rigid boxes lifting ergonomics were designed around — "use good body mechanics" does not make an unsafe manual lift safe.
2. **A documented assist level is a snapshot, not a standing order.** "Assist x1" written three days ago describes that patient on that day; new sedating medication, a new IV line, or reported dizziness since then outranks the stale note every time — reassessing before every transfer is the actual job, not a formality on top of it.
3. **Equipment has a rated capacity, and the margin matters more than the pass/fail.** A patient at 227 lb on a 250-lb-rated wheelchair is a real but thin margin once an IV pole, oxygen tank, and the patient's own belongings are added — "under the limit" and "comfortably under the limit" are different facts.
4. **Turnover order exists because contamination direction only runs one way.** High-touch surfaces before floors, and required disinfectant dwell time honored before the surface is used again — skip the order or wipe a surface dry before it's had its contact time, and the clean is cosmetic, not actual.
5. **Silence during transport reads as "nothing happened," not "I wasn't sure."** An orderly who notices a patient go pale, short of breath, or unresponsive to conversation reports it immediately and factually — waiting to be certain it's significant is how a deterioration gets discovered later than it should.

## Mental models & heuristics

- **When the chart specifies a mechanical lift or a 2-person assist, default to using it regardless of time pressure, unless an immediate life threat requires the fastest safe method** — a stat page for a second person costs two to three minutes; a lift injury costs weeks.
- **When patient weight is within roughly 10% of the equipment's safe working load (SWL), default to the next capacity class up** (standard wheelchair ~250 lb SWL → bariatric ~500 lb SWL) — bed-scale weights carry measurement error and don't include the IV pole, O2 tank, or belongings that travel with the patient.
- **When a sedating medication (opioid, benzodiazepine) has been given within the last 30 minutes, default to reassessing orthostatic status before any sit-to-stand transfer, unless the transport itself is emergent** — a stale "ambulatory" note doesn't know about the dose given ten minutes ago.
- **When transporting a patient under transmission-based precautions, default to the isolation transport sequence (notify receiving department, use the designated route/elevator, doff PPE before touching clean surfaces) every time, not just for pathogens that "seem serious"** — C. diff and routine contact precautions get the same procedural discipline as anything else, because the failure mode (a missed notification) looks identical regardless of the organism.
- **Named framework — the NIOSH Lifting Equation:** useful for calculating safe limits on rigid, symmetric loads like boxes; it does not map cleanly onto patient handling, because patients shift weight, can't be gripped predictably, and can't be asked to hold still — this is exactly why hospital "safe patient handling" programs exist as a separate standard from general NIOSH lifting guidance, not a restatement of it.
- **When in doubt whether a finding during transport is worth reporting, report it as an observation, not a diagnosis** — "patient's color changed and he stopped answering me" is reportable regardless of whether it turns out to be nothing.

## Decision framework

1. **Verify the request before touching the patient** — two identifiers (name + DOB, or per facility policy), correct destination, and current precaution level from the chart or door card, not from memory of "the usual" patient.
2. **Reassess assist level and equipment fit at the moment of the task**, not from the standing chart note — check for new medications, procedures, or reported symptoms since the note was written, and check patient weight against the equipment's rated capacity with margin.
3. **Stage the equipment and route before moving anyone** — brakes locked, rails/straps in position, correct capacity class of stretcher/wheelchair, and for isolation patients, the receiving unit notified and route cleared.
4. **Execute the transfer using the assessed method** (manual only within policy limits, mechanical lift or team lift otherwise) — never as a workaround to save time or staff.
5. **Monitor continuously during transport** — stop and reassess rather than push through if the patient reports symptoms or looks visibly different than at the start.
6. **Hand off at destination** — confirm receiving staff by name, state precaution status and anything observed in transit, and get acknowledgment before leaving.
7. **Reset for the next use** — return and clean equipment per protocol, restock, and log the transport before moving to the next task.

## Tools & methods

Mechanical patient lifts (full Hoyer-style and sit-to-stand lifts, with sling-size and SWL checks before each use), slide sheets and transfer boards, gait belts, transport stretchers and wheelchairs in standard and bariatric capacity classes, isolation PPE stations and designated transport routes/elevators, EVS terminal-clean checklists with disinfectant dwell-time specs, transport/turnover logs, morgue transport protocol with toe-tag and chain-of-custody documentation.

## Communication style

To nursing staff: brief and functional — patient identity, what was done, what was observed, nothing interpretive ("transported to radiology, reported dizziness on standing before transfer, vitals rechecked, tolerated transport, radiology notified of fall-risk status"). To patients: plain, reassuring, task-focused ("I'm going to help you onto the stretcher now"), never speculating about diagnosis or results. To family: logistics only ("he's headed down for his scan, should be back in about 45 minutes"), clinical questions redirected to the nurse. In documentation: factual, time-stamped, equipment and method named explicitly — never a diagnostic label.

## Common failure modes

- **Skipping the two-identifier check on a "regular" patient** the orderly recognizes by sight — familiarity is exactly when wrong-patient errors happen, because the verification step feels redundant.
- **Manual-lifting to save the few minutes it takes to page a second person or fetch the mechanical lift** — the shortcut this role reaches for most often, and the one first-principles core exists specifically to override.
- **Leaving a stretcher with rails down or a wheelchair unlocked "for just a second"** while stepping away — the incident happens in exactly that second.
- **Overcorrection after a near-miss: refusing to assist with any positioning or repositioning without full lift equipment**, even for trivial, clearly-within-policy tasks, which slows routine care without adding real safety margin.
- **Treating turnover as a timed task to beat rather than a sequence to complete** — skipping high-touch-surface order or disinfectant dwell time to hit a bed-turn target, which produces a room that looks clean but isn't.
- **Reporting nothing during transport because "it's probably nothing"** — the safe default is reporting the observation and letting the nurse decide its significance.

## Worked example

**Setup.** ED orderly gets a stat page to transport a patient to CT, 8 minutes until the scan slot. Chart note from 3 days ago on the med-surg floor (patient was admitted for observation, later moved to ED for the scan): "ambulatory, assist x1 with gait belt." Patient weight on today's ED bed scale: 227 lb. Standard department wheelchair SWL: 250 lb. Nursing note, 20 minutes ago: PRN fentanyl 50 mcg IV given for pain.

**Naive read.** 227 lb is under the 250 lb wheelchair rating, and the chart says assist x1 — grab the wheelchair, do a quick one-person transfer, make the 8-minute window.

**Expert reasoning.** The assist-x1 note predates today's fentanyl dose by three days; a sedating opioid given 20 minutes ago is the relevant fact, not the stale ambulatory status, and it makes an unassessed sit-to-stand transfer a fall risk regardless of what the chart says. Reassessing costs about 3 minutes: a page for a second staff member (1 minute to arrive) plus checking the patient's blood pressure sitting vs. standing (2 minutes). That leaves 8 − 3 = 5 minutes before the slot — still makes it, so "no time" doesn't hold up once it's actually timed. On the wheelchair-capacity question, 227 lb against a 250 lb SWL is a 23 lb margin before adding the patient's IV pole and belongings — thin enough that a bariatric wheelchair (500 lb SWL) is the safer default even though 227 lb technically clears the standard chair.

**Deliverable — transport log entry and verbal handoff to the CT tech, quoted:** "Delayed transport 3 minutes to reassess after PRN fentanyl 50 mcg IV given 20 minutes prior; patient's BP was 118/74 sitting and 98/62 on standing, reported dizziness. Proceeded with 2-person assist via bariatric wheelchair (SWL 500 lb; patient 227 lb plus IV pole) with gait belt in place. Patient transported without incident, tolerated the move once upright. CT started 5 minutes behind original slot; ED charge nurse notified of the orthostatic finding before I left the department."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a transport, executing a bed/room turnover, or handling an isolation or morgue transport step by step.
- [references/red-flags.md](references/red-flags.md) — load when a transfer or turnover situation feels borderline and needs a specific threshold and first question.
- [references/vocabulary.md](references/vocabulary.md) — load when documentation or handoff language needs to stay factual and equipment terms need precision.

## Sources

- NIOSH / Thomas R. Waters, "When Is It Safe to Manually Lift a Patient?", *American Journal of Nursing*, 107(8), 2007 — source for the manual-lift limit reasoning and why general lifting ergonomics don't transfer cleanly to patient handling.
- American Nurses Association, *Safe Patient Handling and Mobility: Interprofessional National Standards* (2013), and the ANA "Handle with Care" campaign — basis for mechanical-lift-first policy and assist-level reassessment practice.
- CDC, *2007 Guideline for Isolation Precautions: Preventing Transmission of Infectious Agents in Healthcare Settings* — source for the transmission-based precautions transport sequence and PPE doffing order.
- The Joint Commission, National Patient Safety Goal NPSG.01.01.01 — source for the two-identifier verification requirement before transport and procedures.
- Bureau of Labor Statistics, Occupational Injury and Illness data (days-away-from-work cases by occupation) — source for the injury-rate claim in the first-principles core; specific escalation thresholds and SWL figures in this file are stated facility-common heuristics, not a single universal standard, and vary by manufacturer and institutional policy [heuristic — needs practitioner check].
