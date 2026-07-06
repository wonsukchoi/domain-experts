# Playbook

Filled decision trees and templates for the two process types a paramedic executes most: mass-casualty triage and single-patient field treatment/transport. Numbers below are the conventional national thresholds (CDC 2021 field triage, START/JumpSTART, AHA ACLS) — an agency's own protocol always governs where it differs.

## START adult triage (RPM), full decision tree

Run in this fixed order on every patient at a multi-casualty scene:

1. **Can the patient walk to a designated area under their own power?**
   - Yes → tag **Minor (Green)** — *unless* there's a visible penetrating truncal wound, traumatic amputation, or uncontrolled hemorrhage, in which case override to Immediate and stop the walking gate from applying.
   - No → continue to Respiration.
2. **Respiration.**
   - Absent after one airway repositioning (head-tilt/chin-lift or jaw-thrust) → tag **Deceased/Expectant (Black)**.
   - Present, rate >30/min → tag **Immediate (Red)**.
   - Present, rate ≤30/min → continue to Perfusion.
3. **Perfusion.**
   - Radial pulse absent, or capillary refill >2 seconds → tag **Immediate (Red)**.
   - Radial pulse present, cap refill ≤2 seconds → continue to Mental Status.
4. **Mental status.**
   - Can't follow simple commands (e.g., "squeeze my hand") → tag **Immediate (Red)**.
   - Follows simple commands → tag **Delayed (Yellow)**.

Retag on every subsequent contact — START is a snapshot, not a permanent label.

## JumpSTART pediatric triage, full decision tree

Applies to patients who appear pediatric (roughly ages 1–8, or use judgment/size when age is unclear) at a multi-casualty scene:

1. **Can the child walk?** Yes → **Minor (Green)**, same penetrating-wound/amputation override as adult START. No → continue.
2. **Breathing present?**
   - No → open airway. Still apneic → check pulse.
     - Pulse present → give **5 rescue breaths**. Breathing resumes → **Immediate (Red)**. Still apneic → **Deceased (Black)**.
     - Pulse absent → **Deceased (Black)**.
   - Yes → check rate.
     - RR <15 or >45/min, or irregular → **Immediate (Red)**.
     - RR 15–45/min → continue to Perfusion.
3. **Perfusion.** Palpable peripheral pulse absent → **Immediate (Red)**. Present → continue.
4. **Mental status (AVPU, not GCS, for speed).**
   - "P" (responds to pain only) or "U" (unresponsive) with an abnormal, non-purposeful response → **Immediate (Red)**.
   - Alert, responds to voice, or responds to pain *appropriately* (localizes/withdraws) → **Delayed (Yellow)**.

## CDC field-triage decision (single-patient trauma, non-MCI)

Applied in strict step order — a positive at any step stops the search and decides "trauma center," not necessarily *which level*, which is a local-system question:

**Step 1 — Physiologic.** Any one of: GCS ≤13, systolic BP <90 mmHg (any single reading), respiratory rate <10 or >29/min (<20 for infant <1 year), heart rate > systolic BP (2021 addition), or need for ventilatory support → **transport to highest-level trauma center within reach.**

**Step 2 — Anatomic (if Step 1 negative).** Penetrating injury to head/neck/torso/proximal extremities, flail chest, two or more proximal long-bone fractures, crushed/degloved/mangled/pulseless extremity, amputation proximal to wrist/ankle, pelvic fractures, open or depressed skull fracture, paralysis → **trauma center.**

**Step 3 — Mechanism (if Steps 1–2 negative).** Falls (adults >20 ft / two stories; children >10 ft or 2–3× child's height), high-risk auto crash (intrusion, ejection, death in same vehicle, telemetry indicating high-energy transfer), auto-vs-pedestrian/cyclist with significant impact, motorcycle crash >20 mph → **consider trauma center; contact medical control.**

**Step 4 — Special considerations (if Steps 1–3 negative).** Age >65 with SBP <110, anticoagulant/bleeding disorder, burns with trauma, pregnancy >20 weeks, EMS provider judgment → **consider trauma center or burn/specialty center; contact medical control.**

If none apply → transport to the nearest appropriate (non-trauma) hospital per local protocol.

## ACLS epinephrine and CPR parameters, worked timing

**Cardiac arrest, adult:** compressions at 100–120/min, depth ≥2 in (5 cm), 30:2 ratio for single rescuer/unadvanced airway, minimizing pauses to <10 seconds. Epinephrine 1 mg IV/IO of the 1:10,000 concentration, first dose as soon as IV/IO access allows, then repeated every 3–5 minutes. Worked timeline for a 20-minute resuscitation: dose at minute 2, minute 6, minute 10, minute 14, minute 18 — five total doses at the 4-minute midpoint of the allowed 3–5 minute window.

**Anaphylaxis, adult and pediatric ≥30 kg:** epinephrine 0.3–0.5 mg IM of the 1:1000 concentration into the anterolateral thigh, repeated every 5–15 minutes for persistent symptoms. Worked example: a 34-year-old, 80 kg, biphasic-risk anaphylaxis with ongoing stridor 8 minutes after the first 0.4 mg IM dose — that's within the 5–15 minute repeat window, so a second 0.4 mg IM dose is appropriate before escalating to an IV epinephrine infusion under medical control.

The fatal mixing error: pushing the 1:1000 anaphylaxis concentration IV (10× overdose risk of coronary ischemia/dysrhythmia) or giving the 1:10,000 cardiac-arrest concentration IM (subtherapeutic). Confirm concentration and route as one paired check, not two separate ones.

## MIST handoff template, filled

```
M — Mechanism:    Fall, ~10 ft, onto concrete, unwitnessed onset
I — Injuries:     Suspected closed head injury, possible C-spine injury,
                   no external hemorrhage found on exposure
S — Signs:        GCS 14→10 over 7 min (E4V4M6 → E2V3M5),
                   BP 118/76→148/58, HR 96→58, RR 18→22 irregular,
                   SpO2 99% on 15L NRB
T — Treatment:    C-spine immobilized, high-flow O2, 18g IV L AC,
                   no medications given, reassessed q5min en route
```

## SBAR handoff template, filled (medical call)

```
S — Situation:     67F, acute-onset left facial droop and slurred
                    speech, last known well 47 minutes ago
B — Background:    Hx atrial fibrillation, not on anticoagulation
                    per patient report; no prior stroke
A — Assessment:    CPSS positive x2 (facial droop, arm drift);
                    BP 178/94, HR 88 irregular, blood glucose 118 mg/dL,
                    GCS 15
R — Recommendation: Requesting stroke team activation, LKW 47 min
                    supports both IV alteplase and imaging for
                    possible LVO/thrombectomy candidacy; ETA 9 minutes
```

## Transport-mode fallback ladder

In preference order when the primary option isn't available: 1) ground ALS to the designated trauma/stroke/STEMI center within the platinum-10/golden-hour window → 2) air medical if ground transport time exceeds the window by a wide margin and weather/landing zone allow → 3) ground ALS to the nearest appropriate facility for stabilization with an interfacility transfer to follow → 4) ground BLS with an ALS intercept en route if the closer unit is BLS-only and the patient can tolerate the intercept delay.
