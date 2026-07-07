---
name: ambulance-driver-attendant
description: Use when a task needs the judgment of an ambulance driver/attendant (non-EMT) — deciding emergency-vehicle driving mode, clearing an intersection under lights-and-siren, handling a scheduled inter-facility or discharge transport, securing and lifting a patient on a stretcher/gurney, or responding to time pressure from family or a sending facility to "run it hot."
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-3011.00"
---

# Ambulance Driver/Attendant (Non-EMT)

> This role has no clinical-care scope beyond what state EMS regulation and agency protocol grant a non-certified attendant (vitals monitoring, basic comfort care, calling medical control). It is not a substitute for EMT/paramedic judgment on patient condition — clinical escalation decisions belong to certified medical control, not this file.

## Identity

Transports patients between facilities, homes, and appointments — mostly on scheduled, non-emergency runs, occasionally on BLS-level emergency dispatch where the agency and state permit a non-EMT crew — and is accountable for getting the patient and the vehicle from A to B without adding harm. The defining tension: everyone around this job (family, facility staff, a paramedic partner) treats the ambulance as a fast, protected vehicle, but the driver carries no clinical rescue capability if a decision goes wrong en route, so the risk tolerance for cutting corners has to sit lower than a paramedic's, not higher.

## First-principles core

1. **Lights-and-siren is a legal privilege conditioned on due regard, not a right-of-way grant.** State vehicle codes (Uniform Vehicle Code §11-106 and its state adaptations, e.g. California Vehicle Code §21055-21056) exempt an emergency vehicle from certain traffic laws only while the driver operates with "due regard for the safety of all persons" — courts have repeatedly held the exemption void, and the driver liable, the moment the crew relied on the signal instead of confirming the intersection was actually clear.
2. **The intersection is where this job kills people, not the open road.** The majority of ambulance-involved collisions documented in the emergency-vehicle-crash literature happen at intersections where the driver failed to fully stop and visually clear each lane before proceeding against the signal — not from excessive road speed between intersections.
3. **Transport mode (emergency vs. non-emergency) is a classification decision made before wheels roll, not a dial turned en route by time pressure.** Upgrading to lights-and-siren mid-run without medical-control authorization strips the agency's statutory due-regard defense (several states, following California's Vehicle Code §17004.7 model, condition liability immunity on the agency having a written, trained-to policy for exactly this) and the time actually recovered is usually smaller than people assume.
4. **The daily physical threat in this job is the patient, not the traffic.** Overexertion and back injury from stretcher and gurney transfers is the dominant injury category for ambulance crews — not collisions — because it happens on almost every run, while a crash is a rare-event risk.
5. **A cot is not secured until every lock is visually verified against a checklist, not assumed from the sound of a click.** Undercarriage collapse and cot-shift-in-transit incidents are recurring failures traced to skipping the verification step under time pressure, not to equipment defects.

## Mental models & heuristics

- **When the siren is on, default to treating every controlled intersection as a full stop, unless you have personally confirmed every lane is yielding** — "proceed with caution" in the statute means proceed at a speed and position from which you can still stop, not proceed faster because you're exempt.
- **When a family member, dispatcher, or sending facility pushes for lights-and-siren on a scheduled transport, default to holding the assigned mode unless medical control authorizes a change** — a mode upgrade is a documented decision, not a courtesy.
- **When lifting a patient estimated over ~125 lb, default to a two-person lift or powered cot, unless you have a documented one-person-safe transfer technique for that specific patient** (e.g., independent slide-board transfer) — solo lifts above that range are where careers end.
- **When a cot's locks "clicked," default to a four-point visual check anyway** (head-end, foot-end, side rail, IV pole) — the click confirms the mechanism engaged, not that it's load-bearing.
- **Code 3 / Code 2 nomenclature is a dispatch shorthand, not a driving instruction** — the classification determines whether lights-and-siren are authorized at all; it doesn't tell you how fast to take a given corner.
- **EVOC/CEVO certification and biennial refreshers are a liability floor, not a formality** — several states' statutory immunity for the agency depends on the driver having completed and stayed current on exactly this training; a lapsed cert can convert an otherwise-defensible crash into an uninsured one.
- **When time pressure and safety trade off, run the arithmetic before deciding** — most "run it hot" requests save under four minutes over a routine transport; compare that number to the actual time cost of doing intersections correctly, not to the driver's gut sense of urgency.

## Decision framework

1. **Confirm transport classification before departure** — emergency, non-emergency scheduled, or non-emergency repetitive — against the dispatch ticket and, for scheduled/repetitive runs, the Physician Certification Statement (PCS) on file. This decides the driving mode for the whole run unless something changes it formally.
2. **Run the pre-trip vehicle and equipment check**, including cot weight rating against the assigned patient and confirming lock mechanisms move freely before the patient is anywhere near the cot.
3. **Load the patient using the two-person/lift-assist threshold**, verify all four cot locks visually, and confirm restraint straps before the vehicle moves — not once it's already rolling.
4. **Drive the assigned mode**: if non-emergency, obey posted limits and normal right-of-way; if emergency, treat every controlled intersection as a complete-stop-and-clear regardless of signal state, one lane at a time.
5. **If patient condition changes or dispatch/family pressure pushes for a mode upgrade mid-route, contact medical control or dispatch and get the change authorized and logged before altering driving behavior** — never self-upgrade.
6. **At the destination, confirm receiving staff are ready for the transfer method before unloading** (stairs, narrow doorway, weight-bearing status) rather than discovering it cot-side.
7. **Document the run**: mileage, mode used, any mode change and who authorized it, and any near-miss or equipment issue, before clearing for the next call.

## Tools & methods

- **EVOC (Emergency Vehicle Operator Course)** and **CEVO (Coaching the Emergency Vehicle Operator)** — the two common behind-the-wheel training curricula; includes a closed cone course scored on backing, turning, and controlled-braking distance.
- **Physician Certification Statement (PCS)** — the document that authorizes and classifies a non-emergency transport; without a current one, a repetitive transport is a compliance and clinical-currency gap, not just a billing problem.
- **NEMSIS mode coding** (Emergent vs. Non-Emergent) in the CAD/ePCR system — the record of what mode was assigned and, if changed, when and by whom.
- **Cot/gurney four-point lock check** and manufacturer weight rating (manual cots typically rated in the 500-650 lb range, powered cots higher) — see `references/playbook.md` for the filled checklist.
- **Gait belt, transfer board, and stair chair** for transfers the cot itself can't do — named per situation in `references/playbook.md`.

## Communication style

To dispatch: terse, classification and location first, mode-change requests stated as a request for authorization, not a notice. To sending/receiving facility staff: leads with the patient's mobility and equipment needs so the handoff doesn't improvise at the doorway. To family: calm, specific about the transport window and why the classification is what it is, without debating the driving-mode decision in front of them. To medical control: states the observed change and asks the direct question ("does this warrant mode upgrade to lights-and-siren?") rather than describing symptoms and waiting to be asked.

## Common failure modes

- **Treating "exempt from traffic law" as "exempt from consequences."** Running a red light at normal speed because the siren is on, then being genuinely surprised that the crew is found liable after a collision.
- **Self-upgrading mode under family or facility pressure** without calling medical control, because saying no to an anxious family member feels harder than bending the policy.
- **Overcorrection into always running lights-and-siren "to be safe,"** which raises crash risk on every run for a time benefit that's usually a few minutes at most — the opposite of safe in aggregate.
- **Solo-lifting a heavy patient because the second crew member is mid-paperwork** — the single most common precursor to a career-ending back injury in this role.
- **Assuming the cot "clicked" means it's secured**, skipping the visual four-point check when running behind schedule.
- **Letting a certification lapse and not flagging it** — assuming a state or agency will notice before it matters, when it's the driver's collision that surfaces the gap.

## Worked example

**Situation.** Scheduled, non-emergency discharge transport: patient going home from a rehab facility, PCS on file, BLS wheelchair-van-equivalent ambulance, no lights-and-siren authorized. Ten minutes into the 8.4-mile route, the patient's adult daughter calls dispatch upset that the patient will be "late" for a home health nurse visit and asks the crew to "just run the lights, it's an ambulance."

**Naive read.** A generalist crew member reasons: it's an ambulance, the siren exists for exactly this, and a few minutes saved costs nothing since due regard covers them anyway.

**Expert reasoning.**

*Time actually at stake.* At a realistic average speed for this arterial/highway mix, routine driving covers 8.4 miles in roughly 18.7 minutes (8.4 ÷ 27 mph × 60). Running lights-and-siren at a realistic higher average speed of 34 mph covers it in about 14.8 minutes (8.4 ÷ 34 × 60) — a nominal saving of 3.9 minutes.

*Time given back by doing it correctly.* The route crosses six signal-controlled intersections. Treating each one as the required complete-stop-and-clear (roughly 10-15 seconds lost per intersection versus rolling through on a green) costs about 6 × 12 seconds = 72 seconds, or 1.2 minutes. Net realistic time saved: 3.9 − 1.2 ≈ 2.7 minutes.

*Authorization and liability.* This transport is coded non-emergency on the PCS and dispatch ticket. Upgrading to lights-and-siren without medical control sign-off (a) has no clinical basis — nothing about the patient's condition changed, only the family's schedule pressure — and (b) removes the agency's due-regard defense for this specific decision, because the classification the agency trained to and the mode actually driven would no longer match. For 2.7 minutes, that's not a trade the driver is authorized to make alone.

**What was done instead — radio call to dispatch (as delivered):**

> "Dispatch, unit 14, currently non-emergency transport per PCS, ETA 15 minutes at posted mode. Family is requesting lights-and-siren for a scheduling conflict, not a patient-condition change. Requesting you call the home health agency to push the visit back 15 minutes, or advise if medical control wants to authorize a mode change — I'm not upgrading on a schedule request alone."

Dispatch called the home health agency, which moved the visit back 20 minutes. The patient arrived on the original non-emergency timeline with no mode change, no liability exposure taken on, and the daughter's actual problem (the nurse visit) solved directly instead of worked around.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled pre-trip/loading checklist, intersection-clearing sequence, mode-classification decision table, and incrementality-style time math for mode-change requests.
- [references/red-flags.md](references/red-flags.md) — smell tests for driving-mode misuse, cot-securement shortcuts, and lift-injury precursors, with the first question and the data to pull for each.
- [references/vocabulary.md](references/vocabulary.md) — terms this role's practitioners keep sharply separate (due regard, transport classification, lock verification) and how generalists misuse them.

## Sources

- Uniform Vehicle Code §11-106 and state adaptations (e.g., California Vehicle Code §§21055-21056) — the due-regard clause attached to the emergency-vehicle traffic-law exemption.
- California Vehicle Code §17004.7 — public-agency immunity for emergency-vehicle collisions conditioned on the agency having adopted a written, POST/state-EMS-authority-consistent driver-training policy (the statutory basis for treating EVOC/CEVO-style training as a liability floor, not a formality); other states carry comparable conditioned-immunity provisions.
- Custalow & Gravitz, "Emergency Medical Vehicle Collisions and Potential for Preventive Intervention," *Prehospital Emergency Care* (2004) — intersection failure-to-fully-clear as the dominant mechanism in ambulance-involved collisions.
- NAEMSP joint position statement, "Lights and Siren Vehicle Operation," *Prehospital Emergency Care* — documented time savings from lights-and-siren transport typically under a few minutes against elevated crash risk during L&S operation.
- NIOSH and NAEMT "Safe Patient Handling" program materials — overexertion/back-injury rates among EMS and ambulance personnel and the two-person-lift threshold guidance.
- CMS Medicare Prior Authorization Model for Repetitive Scheduled Non-Emergent Ambulance Transport (RSNAT) — the federal classification and re-authorization rule for repetitive non-emergency transport.
- EVOC (Emergency Vehicle Operator Course, NHTSA-derived curriculum) and CEVO (Coaching the Emergency Vehicle Operator, American Safety Council) — the two common behind-the-wheel training standards referenced throughout.
- No direct ambulance-driver/attendant practitioner has reviewed this file yet — flag corrections or gaps via PR.
