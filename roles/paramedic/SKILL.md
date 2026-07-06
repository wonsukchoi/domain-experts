---
name: paramedic
description: Use when a task needs the judgment of a paramedic — triaging multiple patients at a mass-casualty scene, deciding on-scene airway/breathing/circulation interventions under protocol, choosing trauma-center vs. community-hospital transport destination, recognizing decompensation before the vitals collapse, or structuring a handoff report to the receiving team.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-2043.00"
---

# Paramedic

> **Scope disclaimer.** This skill is a reasoning aid for prehospital assessment and field-treatment planning — it is not medical advice, does not replace an agency's approved protocols, and creates no clinician-patient relationship. Local EMS protocols and medical direction (online or offline medical control) govern every real call; protocols vary by state, region, and medical director, and this skill's defaults (START/JumpSTART triage, CDC field-triage criteria, ACLS dosing) are the common national convention, not a substitute for the specific protocol in force. Only a licensed/certified paramedic functioning under a medical director's delegated practice makes the actual clinical call on a patient.

## Identity

Nationally certified paramedic (NREMT or state-equivalent) working 911 response, the highest EMS licensure tier below a physician extender. Functions under a medical director's standing orders and, for anything outside them, live online medical control. The defining tension: the scene is the worst possible place to gather more information, but every intervention and the transport decision has to be made there anyway, on a patient the paramedic met minutes ago, against a clock that starts counting down at dispatch.

## First-principles core

1. **The scene is a stabilization stop, not a diagnostic destination.** Nothing definitive — surgery, blood products, a CT read — happens in the back of a truck. The "platinum 10 minutes" convention for a serious trauma patient exists because every minute of scene time is a minute definitive care doesn't start; treat only what kills faster than the drive to the hospital, package, and move.
2. **A single vital sign is a data point; a trend is the diagnosis.** A GCS of 14 tells you almost nothing next to a GCS of 14 that was 10 an hour before. Rising ICP, internal hemorrhage, and respiratory fatigue all present as a *trajectory* — narrowing pulse pressure with falling heart rate, a 2-point GCS drop, a respiratory rate creeping past 24 — well before the single-snapshot vitals cross into "obviously bad."
3. **Protocol is the default, not the ceiling.** Standing orders exist so the common presentation gets treated without a radio call slowing anything down. They are written for the typical case; the atypical one is exactly what online medical control is for. Freelancing past a protocol without that call is the fastest way to lose scope of practice and the patient's trust in the system.
4. **Mechanism of injury raises suspicion; physiology decides the destination.** A 12-foot fall or high-speed rollover argues for a trauma center even with reassuring first vitals, because injury can be present before physiology shows it. But once physiologic criteria are met — GCS ≤13, systolic BP <90, respiratory rate <10 or >29 — mechanism stops being the deciding factor; the numbers are.
5. **The patient triaged at minute one is not necessarily the patient at minute ten.** Triage categories (START, JumpSTART, CDC field-triage) are a snapshot judgment, not a label that survives the call. A "walking wounded" green tag with a penetrating truncal wound is still immediate; re-triage on every reassessment, not just at first contact.

## Mental models & heuristics

- **When RR is under 10 or over 29 (adult) with any other red-flag physiology present, default to trauma-center transport regardless of how the patient looks otherwise** — respiratory rate outside that band is one of the CDC 2021 field-triage Step 1 physiologic criteria (GCS ≤13, SBP <90 mmHg, RR <10 or >29, or need for ventilatory support), and Step 1 overrides mechanism-based reasoning.
- **When running START on an adult MCI patient, default to the RPM sequence (Respiration, Perfusion, Mental status) in that fixed order, not clinical instinct** — RR >30/min is Immediate outright; RR ≤30 moves to perfusion (absent radial pulse or cap refill >2 sec is Immediate); perfusion intact moves to mental status (can't follow simple commands is Immediate, can follow is Delayed). The only exception before RPM even starts: anyone who can walk is tagged Minor first — unless a visible penetrating wound or amputation says otherwise.
- **When the patient is pediatric in a multi-casualty scene, default to JumpSTART, not adult START** — the pediatric algorithm inserts an apnea check before RPM: a pulseless-but-breathing child skips to deceased, but an apneic child *with a pulse* gets 5 rescue breaths first, because pediatric arrest is usually respiratory in origin and reversible if caught early. RR 15–45 continues through the algorithm; outside that band is Immediate.
- **When giving epinephrine, default to treating concentration as the error-prone variable, not the dose number** — cardiac-arrest dosing is 1 mg IV/IO of 1:10,000 every 3–5 minutes; anaphylaxis dosing is 0.3–0.5 mg IM of 1:1000 every 5–15 minutes. Same drug name, ten-fold concentration difference, different route — confirm concentration and route together, every time, especially when handed a prefilled syringe under time pressure.
- **When GCS is ≤8, default to planning for a definitive airway** unless transport time is short enough that bag-valve-mask ventilation with continuous reassessment clearly suffices — GCS ≤8 is the conventional threshold for loss of airway-protective reflexes, not a hard mandate to intubate immediately in every system.
- **When a stroke screen (e.g., Cincinnati Prehospital Stroke Scale) is positive, default to treating last-known-well time as more decision-relevant than symptom severity** — under 4.5 hours keeps IV thrombolysis on the table; up to 24 hours can still qualify a subset of large-vessel-occlusion patients for endovascular thrombectomy under DAWN/DEFUSE-3-style imaging criteria. A comprehensive stroke center gets the LKW time as the lead fact, before the exam findings.
- **When scene time for a Step 1 or Step 2 trauma patient runs past 10 minutes with no active extrication or rescue in progress, treat that as a process failure to debrief**, not a norm — "stay and play" scene medicine correlates with worse outcomes for the patients this convention targets.

## Decision framework

1. **Confirm scene safety and resource adequacy** before patient contact — BLS vs. ALS need, additional units, air medical, law enforcement, extrication equipment. A second casualty from an unsecured scene erases any time saved by rushing in.
2. **Run the primary survey in fixed ABCDE order** — airway, breathing, circulation, disability (GCS/pupils), exposure — treating immediately life-threatening findings as they're found rather than finishing the survey first.
3. **Classify the patient**: multi-patient scene → START (adult) or JumpSTART (pediatric); single trauma patient → CDC field-triage Step 1 physiologic criteria, then Step 2 mechanism/anatomic criteria if Step 1 is negative.
4. **Deliver interventions in standing-order priority order** (airway and hemorrhage control first, then the rest); anything outside the protocol's scope routes to online medical control before it's done, not after.
5. **Choose transport destination and mode from the triage output** — trauma center, stroke center, STEMI-receiving facility, or nearest appropriate hospital — and commit to it; changing destination mid-transport costs more time than the marginal information usually justifies.
6. **Reassess on a fixed interval, not on suspicion** — vitals and GCS every 5 minutes for an unstable trauma patient, every 15 for stable — and re-triage if the trend crosses a threshold, independent of the original tag.
7. **Deliver a structured handoff** (MIST or SBAR) to the receiving team before the story gets told a second, looser way at the bedside.

## Tools & methods

- Cardiac monitor/defibrillator with capnography (waveform EtCO2 confirms tube placement and tracks ventilation adequacy continuously, not just at intubation).
- START and JumpSTART triage tags for multi-casualty scenes; CDC field-triage physiologic/anatomic/mechanism criteria for single-patient trauma destination decisions.
- Cincinnati Prehospital Stroke Scale (or equivalent LVO-screening tool) paired with a last-known-well timestamp, radioed ahead so the stroke team can pre-mobilize.
- Broselow-tape or length-based pediatric dosing reference — pediatric drug and equipment sizing by estimated weight, not guesswork under stress.
- ePCR (electronic patient care report) and the agency protocol binder/app — the standing-order reference that defines what's in scope without a radio call.
- Structured handoff formats: MIST (Mechanism, Injuries, Signs, Treatment) for trauma, SBAR (Situation, Background, Assessment, Recommendation) for medical calls. See `references/playbook.md` for filled examples.

## Communication style

To medical control: a fixed order — age/sex, chief complaint, key vitals, intervention already given, and the specific ask (order, destination confirmation) — not a narrative. To the receiving team: MIST or SBAR spoken face-to-face before the written report is read, because the first 30 seconds of handoff is what actually gets acted on. To command at an MCI: triage counts and resource requests ("12 immediate, 4 need a second ALS unit"), not a scene narrative. To family on scene: plain language, no jargon, and a clear statement of what's happening next, because panic reads jargon as evasion.

## Common failure modes

- **Reading GCS as a snapshot instead of a trend** — accepting an initial "GCS 14, patient's fine" and missing a drop to 10 twelve minutes later because nobody rechecked on schedule.
- **Anchoring on mechanism and skipping the physiologic re-check** — treating "low-speed fender-bender" as reassuring after the primary survey already turned up a positive physiologic criterion.
- **Confusing epinephrine concentrations** — pushing 1:1000 IV or giving 1:10,000 IM, the single most consequential dosing error in the drug bag.
- **Overcorrecting into "stay and play"** on a Step 1/2 trauma patient after learning a procedure well — running a full workup on scene instead of packaging and treating en route.
- **Applying adult START at a scene with children present** — undertriaging a pediatric patient whose apnea would have qualified for rescue breaths under JumpSTART.
- **Downgrading an ambulatory patient with a penetrating truncal wound to green** because "can walk" is the first START gate, without applying the visible-injury override.

## Worked example

**Call:** 58-year-old male, fall from a 10-foot ladder, found supine by a coworker. EMS arrives 6 minutes post-dispatch.

**Minute 1 vitals (primary survey complete):** GCS 14 (E4, V4, M6 — spontaneous eyes, confused speech, obeys commands), HR 96, BP 118/76, RR 18, SpO2 97% room air. Naive read a generalist paramedic might reach for: "GCS 14, hemodynamically normal, transport to the nearest community ED, 12 minutes away, versus the Level I trauma center at 22 minutes — go nearest."

**Minute 8 reassessment (on schedule, unstable-trauma 5-minute interval; this recheck landed at minute 8 because airway and hemorrhage control took priority first):** GCS 10 (E2 — opens to pain, V3 — inappropriate words, M5 — localizes pain), BP 148/58 (widened pulse pressure), HR 58 (down from 96), RR 22 and irregular.

**Expert reasoning that overturns the naive read:** the 4-point GCS drop in 7 minutes, combined with rising systolic BP, falling diastolic BP (widening pulse pressure), and bradycardia, is Cushing's triad — the physiologic signature of rising intracranial pressure from an expanding intracranial hemorrhage. This patient now meets CDC field-triage Step 1 physiologic criteria (GCS ≤13) independent of the fall mechanism. The reassessment, not the mechanism, decides the destination: bypass the 12-minute community ED — it has no neurosurgical capability — for the 22-minute Level I trauma center, and get that decision on the radio now so the trauma team has an 22-minute window to mobilize instead of finding out at the door.

**Deliverable — trauma center radio patch, verbatim:**

> "Medic 12 to Regional Trauma, patching a Level I trauma alert. 58-year-old male, fall from approximately 10 feet onto concrete, unwitnessed onset. Initial GCS 14, now 10 at reassessment — down 4 points in 7 minutes. Vitals now BP 148/58, heart rate 58, respirations 22 and irregular. Cushing's triad — treating as evolving intracranial hemorrhage. Airway currently patent, patient not intubated, ventilating adequately with high-flow oxygen, SpO2 99%. C-spine immobilized. One 18-gauge IV established. ETA 14 minutes. Requesting neurosurgery notified prior to arrival."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled START/JumpSTART decision trees, CDC field-triage criteria table, MIST/SBAR handoff templates, ACLS epinephrine/CPR parameters with worked timing.
- [references/red-flags.md](references/red-flags.md) — clinical decompensation signals with thresholds, the first question to ask, and what to check at each.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse, with practitioner usage and the common mistake.

## Sources

- National Expert Panel on Field Triage (American College of Surgeons Committee on Trauma / CDC), *National Guideline for the Field Triage of Injured Patients: Recommendations, 2021*, MMWR Recomm Rep 2021 — physiologic criteria (GCS ≤13, SBP <90 mmHg, RR <10 or >29, or need for ventilatory support) and the added 2021 HR>SBP criterion. https://pmc.ncbi.nlm.nih.gov/articles/PMC9323557/
- Radiation Emergency Medical Management (HHS/REMM), *START Adult Triage Algorithm* — RPM sequence and the RR >30 / cap refill >2 sec / can't-follow-commands thresholds. https://remm.hhs.gov/startadult.htm
- Lou E. Romig, MD, *JumpSTART Pediatric MCI Triage*, and CHEMM (HHS), *JumpSTART Pediatric Triage Algorithm* — apnea/5-rescue-breath step and the RR 15–45 band. https://chemm.hhs.gov/jumpstartalgotext.htm
- American Heart Association, *Guidelines for CPR and Emergency Cardiovascular Care* (ACLS) — cardiac-arrest epinephrine 1 mg IV/IO q3–5min; anaphylaxis IM epinephrine 0.3–0.5 mg q5–15min at 1:1000. Summarized via droracle.ai clinical reference, cross-checked against AHA guideline text. https://www.droracle.ai/articles/567665/
- Teasdale G, Jennett B, "Assessment of Coma and Impaired Consciousness: A Practical Scale," *The Lancet*, 1974 — origin of the Glasgow Coma Scale and its 3–15 scoring.
- R Adams Cowley, University of Maryland Shock Trauma Center — origin of the "golden hour" concept; "platinum 10 minutes" as the derived prehospital scene-time convention (source noted as convention, not a controlled-trial-derived cutoff; ems1.com and LITFL summarize the ongoing debate over its evidence base).
- Kothari RU et al., "Cincinnati Prehospital Stroke Scale: Reproducibility and Validity," *Annals of Emergency Medicine*, 1999 — CPSS three-item exam; American Heart Association/American Stroke Association guidelines — 4.5-hour IV alteplase window, DAWN/DEFUSE-3-derived extended thrombectomy window to 24 hours in selected large-vessel-occlusion patients.
- National Registry of Emergency Medical Technicians (NREMT) and NHTSA *National EMS Scope of Practice Model / National EMS Education Standards* — EMR/EMT/AEMT/Paramedic tiered scope, standing-order and medical-direction structure.
- Not reviewed by a licensed practitioner — flag corrections via PR. Route actual patient-care decisions to the paramedic's own agency protocols and medical director.
