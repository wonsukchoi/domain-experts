# Hospitalist Playbook

Operational sequences with concrete thresholds. Defaults, not laws — deviate when the case warrants it, but document why.

## 1. Admission-status workup (first hour)

1. **Count expected midnights.** Will the patient plausibly need care crossing two midnights? If yes and documented at the time of the decision, admit inpatient. If no, observation — unless the procedure is on CMS's inpatient-only list, which overrides the count regardless of expected duration.
2. **Write the medical-necessity line separately from the clinical note.** One sentence: why this patient, why now, why this level of care. This is the sentence a recovery audit contractor (RAC) reads in isolation 18 months later; a chart with excellent clinical reasoning but no explicit necessity statement still gets denied on audit.
3. **Flag anticipated discharge date on day one**, even as a rough estimate — CHF/COPD/pneumonia exacerbations without complication: 3–5 days; uncomplicated cellulitis or PID: 2–3 days; anything with a pending procedure: procedure date + 1–2 days recovery. Revise daily; a date that never moves after day 2 is itself a signal something is being missed.

## 2. Rounding / differential triage sequence

For each new problem on rounds, in this order:

1. **Can't-miss first.** Name the one diagnosis that would seriously harm or kill the patient if missed, and state explicitly what rules it in or out — even if it's not the most likely explanation.
2. **Common cause second.** Base rates: a new fever on hospital day 3 is a line infection, UTI, or C. diff before it's a rare drug reaction or an exotic infection.
3. **State today's trajectory target as a checkable fact**, not a feeling: "creatinine should be ≤1.4 by tomorrow AM" or "off supplemental O2 by end of day" — not "continue to monitor."
4. **Route the question to the cheapest sufficient channel.** Curbside consult (phone/hallway, same day, no note) for questions a specialist can answer without seeing the patient; formal consult (bedside evaluation, dictated note) only when the answer is procedural, surgical, or carries independent liability (e.g., "does this patient need surgery," "can we discontinue anticoagulation before a procedure").

## 3. VTE prophylaxis — Padua Prediction Score

| Risk factor | Points |
|---|---|
| Active cancer | 3 |
| Previous VTE (excluding superficial) | 3 |
| Reduced mobility (≥3 days) | 3 |
| Known thrombophilic condition | 3 |
| Recent (≤1 month) trauma or surgery | 2 |
| Age ≥70 | 1 |
| Heart and/or respiratory failure | 1 |
| Acute MI or ischemic stroke | 1 |
| Acute infection and/or rheumatologic disorder | 1 |
| Obesity (BMI ≥30) | 1 |
| Ongoing hormonal treatment | 1 |

**Score ≥4 = high risk** → pharmacologic prophylaxis (e.g., enoxaparin or unfractionated heparin) unless a bleeding contraindication is present, in which case mechanical prophylaxis (sequential compression devices). **Score <4** → mechanical prophylaxis alone is usually sufficient; routine pharmacologic prophylaxis on every admission regardless of score is the more common overcorrection, not the underuse.

## 4. Discharge readiness and risk-stratified follow-up

**Step 1 — Confirm the clinical target is met**, not just "no acute issue": vitals within the patient's baseline range for 24h, oral intake tolerated, pain controlled on an oral regimen, and — for a volume-status admission like CHF — weight at or near the documented dry-weight goal, not simply "trending down."

**Step 2 — Compute LACE.**

| Component | Scoring |
|---|---|
| **L**ength of stay | 1 day=1, 2=2, 3=3, 4–6=4, 7–13=5, 14+=7 |
| **A**cuity (urgent/emergent admission) | 3 (0 if elective) |
| **C**omorbidity (Charlson index) | 0=0, 1=1, 2=2, 3=3, ≥4=5 |
| **E**D visits in prior 6 months | 0=0, 1=1, 2=2, 3=3, ≥4=4 |

**Score ≥10 = high risk** of 30-day readmission or death. High-risk pathway: 7-day follow-up appointment (not 2–4 weeks), home health nursing referral, and a phone check at 48–72 hours post-discharge. Below 10: routine 2–4 week PCP follow-up is adequate; adding home health to every low-risk discharge is the overcorrection, not underuse.

**Step 3 — Reconcile every medication being converted in route or dose**, not just renamed. Example table:

| Drug | Inpatient route/dose | Discharge route/dose | Conversion basis |
|---|---|---|---|
| Furosemide | IV 40 mg BID (80 mg/day) | PO 80 mg BID (160 mg/day) | ~50% oral bioavailability |
| Morphine | IV 4 mg q4h PRN | Oxycodone 5–10 mg q4h PRN PO | ~3:1 oral:IV opioid ratio (agent-specific) |
| Heparin gtt | Weight-based IV | Apixaban 5 mg BID or warfarin per INR | Indication-specific, not a fixed ratio |

**Step 4 — Transmit the discharge summary within 48 hours**, including: admission diagnosis, hospital course in 3–5 sentences, discharge medications with what changed and why, pending results at discharge, and the specific follow-up appointment (date, provider, reason). A summary that reaches the PCP after the follow-up visit already happened has functionally not been transmitted.

## 5. Handoff (I-PASS), every transition

- **I**llness severity — stable / watcher / unstable, stated first, one word.
- **P**atient summary — one-paragraph synopsis: why admitted, what's been done, current status.
- **A**ction list — to-do items with owner and timeframe ("recheck K+ at 6pm, call renal if >5.5").
- **S**ituation awareness — contingency plans: "if SBP drops below 90, give 500mL bolus and call me before pressors."
- **S**ynthesis by receiver — the incoming physician reads the plan back in their own words before the outgoing physician leaves; a handoff without this step is verified nowhere and is the single most common point where the written sign-out and the receiver's actual understanding diverge.
