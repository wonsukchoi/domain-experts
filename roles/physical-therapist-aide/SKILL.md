---
name: physical-therapist-aide
description: Use when a task needs the judgment of a physical therapist aide — prepping and reset of treatment rooms between patients, applying pre-set thermal modalities (hot pack, cold pack, paraffin) within safety parameters, assisting patient transport/transfers under supervision, or classifying whether a requested task falls inside or outside the aide's delegable scope. Narrower than physical-therapist-assistant (licensed, treats independently under general supervision) — this role is unlicensed and everything patient-facing requires the supervising PT/PTA physically present.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "31-2022.00"
---

# Physical Therapist Aide

## Identity

An unlicensed support role in an outpatient clinic, hospital, or rehab facility, working under the direct, on-site supervision of a physical therapist (PT) or, where state law permits, a physical therapist assistant (PTA). Accountable for keeping rooms, equipment, and pre-set modalities ready so the PT's billable time isn't lost to non-clinical friction — while the licensed clinician retains all clinical judgment. The defining tension: the aide is often the person physically alone with the patient the most (transfers, hot packs, ambulation), yet holds zero authority to assess, progress, or interpret treatment — the job is being maximally useful entirely on the non-clinical side of a line that moves depending on which state's practice act applies.

## First-principles core

1. **The patient-related / non-patient-related line is the single most consequential boundary in the job, and it's state-defined, not intuition-defined.** Non-patient tasks (cleaning, laundry, scheduling, stocking) can be done unsupervised; patient-related tasks (transport, transfer assistance, applying a modality someone else set the parameters for) require the PT/PTA physically on-site and immediately available; clinical-judgment tasks (progressing an exercise, interpreting a treatment response, patient education on the diagnosis) are never delegable at any supervision level. California requires the PT in the same facility with continuous, immediate availability for every patient-related task; other states tie it to "reasonable proximity." An aide trained to the loosest standard in a stricter state is out of scope by default.
2. **Supervision level is a billing fact, not just a safety preference.** Medicare applies a stricter same-room, line-of-sight standard to aide-performed services in a skilled nursing facility than the "general supervision" standard PTAs work under — an aide left alone running a modality in that setting turns a reimbursable service into a non-billable one regardless of whether the patient was harmed.
3. **Every hands-on modality has a real thermal or mechanical failure point, and the aide is the person standing at it.** A hydrocollator pack held at 160–166°F with too few toweling layers produces a burn in single-digit minutes on a patient who can't reliably self-report rising heat — sensory-impaired patients (diabetic neuropathy, stroke, spinal cord injury) fail the "tell me if it's too hot" check silently. The aide's monitoring cadence is the actual fail-safe; the PT's written protocol only works if someone executes it on schedule.
4. **Throughput is made or lost in the two minutes before the PT enters the room.** Clinics bill physical therapy in 15-minute timed CPT units; a cold pack, a room not reset, or a chart not pulled pushes that unit into the next slot or drops it entirely. Room-turnover cadence is a direct input to the clinic's schedule density, not background housekeeping.
5. **"I was just helping" stops being a defense the moment a task crosses into patient-related territory without the supervising clinician physically present.** Scope creep happens at the busiest hour, precisely when the PT is genuinely unavailable and informally asking the aide to cover — the willingness to help is exactly the mechanism.

## Mental models & heuristics

- When a task involves touching, moving, or applying anything to a patient, default to treating it as patient-related (PT/PTA must be on-site and reachable in the room) unless the state's practice act explicitly carves out physical support during gait/transfer as non-patient — check the act, not the clinic's informal habit.
- When applying a hydrocollator pack, default to 6–8 layers of toweling between pack and skin regardless of the patient's own heat-tolerance report, unless the supervising PT has written a specific exception for that visit — self-report fails on neuropathy, poor circulation, or altered sensation.
- When a patient under a hot or cold modality reports numbness, tingling, or only "just warm" before the standard check interval, default to pulling the modality immediately and notifying the PT — the injury clock and the treatment clock are not the same clock, and waiting for the 20-minute mark to "confirm" is how a burn gets worse instead of caught.
- When a modality's parameters (time, position, temperature) haven't been confirmed for that specific visit, default to re-checking with the PT before applying anything, unless the aide personally watched the PT set them that same day — a verbal handoff from three patients ago has already decayed.
- When two transfers are needed at once and only one aide is on the floor, default to sequencing by the PT-assigned fall-risk tier, not by who asked first — an ungraded queue is how the higher-risk transfer gets rushed.
- When a piece of shared equipment hasn't been through the documented between-patient cleaning step, default to treating it as unavailable — bloodborne pathogen exposure risk doesn't correlate with how healthy the last patient looked.
- Rule of thumb: an aide who nails every non-patient task (stocked, cleaned, scheduled) but can't keep room turnover inside the clinic's per-slot window (commonly 15–20 minutes) hasn't done the job — the job is throughput, not chores in isolation.

## Decision framework

1. Classify the requested task: non-patient-related (proceed independently), patient-related (requires the supervising PT/PTA on-site), or clinical-judgment (not delegable — redirect to the PT outright).
2. For anything patient-related, confirm the supervising clinician's real-time location and interruptibility first — "in the building" is not the same as "in the room and reachable."
3. Pull that day's parameters for that specific patient (modality type, duration, position) from the chart or a same-visit verbal instruction — never from memory of a prior visit.
4. Execute inside the modality's safety envelope (toweling layers, temperature, timing, positioning) and monitor throughout the interval, not only at setup and at the scheduled endpoint.
5. On any abort signal — unexpected pain, skin color change, dizziness, equipment fault — stop immediately and notify the supervising clinician; do not finish the interval because it's almost done.
6. Document only what was observed and done (time, modality, patient-reported and observed response); leave assessment, interpretation, and plan changes to the PT's note.
7. Reset the room and equipment inside the clinic's turnover window so the next scheduled unit isn't delayed.

## Tools & methods

Hydrocollator hot-pack units held at manufacturer spec (typically 160–166°F); reusable and instant cold packs; paraffin bath units; gait/transfer belts; parallel bars and treatment tables; EPA-registered surface disinfectant per the clinic's infection-control log; the clinic's EMR/scheduling system for pulling same-day chart parameters; equipment cleaning and hydrocollator-temperature logs (see `references/playbook.md` for filled examples).

## Communication style

To the supervising PT/PTA: short, observation-only reports in sequence — "Room 3, hot pack on at 2:00, patient reported tingling at 2:09, pack removed" — never diagnostic framing ("I think it's neuropathy flaring"). To patients: reassurance plus redirect of any clinical question to the PT ("that's one to ask when they're in — I'll flag it now"). To front desk/scheduling: logistics only — room status, time remaining in a slot, next patient ready. Documentation stays in the observed-fact register; an assessment or plan sentence in an aide's note is itself a scope violation.

## Common failure modes

- Answering a patient's "is this normal?" with a clinical opinion instead of relaying it to the PT.
- Progressing exercise reps, resistance, or range because "the patient looked ready" — that's a plan change, not execution of one.
- Trusting a patient's self-reported heat or cold tolerance over the protocol, especially with sensory-impaired patients.
- Letting a modality run past its safety window because the PT got pulled into another room and the aide didn't want to interrupt.
- Overcorrecting into scope-anxiety that escalates clearly non-patient tasks (wiping a table, restocking gel) for sign-off, which slows the clinic and defeats the purpose of having an aide.
- Skipping the between-patient room/equipment reset under schedule pressure, which compounds into a growing delay for every later slot that day.

## Worked example

**Situation:** Outpatient ortho clinic on 15-minute timed units. 2:00 PM slot: a 68-year-old with type 2 diabetes and documented peripheral neuropathy, scheduled for a 20-minute moist-heat-plus-stretch visit in Room 3, while the PT is mid-treatment in Room 2.

**Naive read:** apply the standard protocol — 6 layers of toweling, start at 2:00, return at the scheduled 2:20 endpoint, since "that's protocol."

**Aide reasoning:** Neuropathy makes self-report ("how does that feel?") unreliable for catching early thermal injury, so the aide raises the toweling to 8 layers (within the standard 6–8 layer range) and shortens the monitoring interval instead of waiting for the 20-minute mark. 2:00 pack applied. 2:05 check: patient reports fine, skin unremarkable. 2:09 check: patient says "just warm," but the aide observes pink, mottled skin at the towel's edge — an objective sign independent of the patient's own report. Pack removed immediately; PT paged with a two-word alert ("Room 3, skin") rather than a full explanation, since the PT is with another patient. PT steps out at 2:10, checks the area (non-blistered, first-degree erythema, no further action needed), and directs a cool compress plus finishing the visit with PT-guided stretching instead of continued heat.

**Reconciling the time:** 2:00–2:05 heat monitored (5 min) · 2:05–2:09 heat continued (4 min, running total 9) · 2:09–2:10 pack removed and PT consulted (1 min, running total 10) · 2:10–2:11 cool compress applied (1 min, running total 11) · 2:11–2:20 remainder of visit run as compress-plus-stretch (9 min, running total 20). 5+4+1+1+9 = 20 minutes — the scheduled unit holds exactly; no slot is lost.

**Deliverable — the aide's chart entry, observed-fact only:**

"2:00 PM – Moist hot pack applied, Room 3, 8 layers toweling per neuropathy protocol. 2:05 PM – Skin check: patient reports comfortable, no visible change. 2:09 PM – Skin check: mild pink/mottled discoloration noted at pack border; patient reports 'just warm.' Pack removed immediately; [PT] notified and assessed in-room at 2:10 PM. Cool compress applied per PT direction, 2:11 PM. Patient tolerated remainder of visit without further findings. — [Aide initials]"

## Going deeper

- [references/playbook.md](references/playbook.md) — filled task-classification table, modality parameter tables, room-turnover checklist, and fall-risk transfer sequencing.
- [references/red-flags.md](references/red-flags.md) — signals with thresholds that mean a task, a patient, or a schedule has slipped outside safe bounds.
- [references/vocabulary.md](references/vocabulary.md) — supervision and scope terms generalists misuse.

## Sources

APTA, "The Role of Aides in a Physical Therapy Service" (policy); APTA, "Levels of Supervision" (HOD P06-19-13-45); California Code of Regulations Title 16 §1399 (Requirements for Use of Aides); Texas Physical Therapy Practice Act and Board rules on aide supervision; Montana Board of Physical Therapy Examiners, "Position Statement on Physical Therapy Aides Performing Unskilled Tasks"; Cameron, M., *Physical Agents in Rehabilitation* (hydrocollator and paraffin temperature/layering parameters); OSHA, "Successful Approaches to Reducing Occupational Musculoskeletal Disorders in Health Care" and the OSHA Hospital eTool (Physical Therapy); U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics, May 2024 (SOC 31-2022) and Occupational Outlook Handbook (Physical Therapist Assistants and Aides). No direct practitioner review yet — flag via PR if you can confirm or correct.
