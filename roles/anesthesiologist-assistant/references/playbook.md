# Anesthesiologist Assistant — Playbook

Filled protocols and templates, not descriptions of them. Populate the bracketed fields; the structure and thresholds are the point.

## 1. Pre-case Anesthesia Care Team setup checklist

Run before the patient enters the room, every case:

| Item | Confirm |
|---|---|
| Directing anesthesiologist name and location | [Name], currently in Room [#], or induction room if pre-case huddle |
| Concurrent rooms open under this anesthesiologist | [count] of 4 (medical direction ceiling) |
| Communication method for emergent page | [overhead / direct phone / pager #] |
| ASA Physical Status class | [I–VI], matches plan? Y/N |
| Airway exam (Mallampati, thyromental distance, mouth opening) | [class/measurements] |
| OSA screen (STOP-BANG or equivalent) | [score]/8 — high risk if ≥3 (moderate) or ≥5 (severe) |
| Allergies / prior anesthesia complications | [list, incl. family history of MH] |
| Difficult airway cart location if score elevated | [location confirmed] |
| Medications drawn up, independently verified against label | Y/N, verified by [second check or self-read-aloud] |

Do not proceed to induction with any row unconfirmed — treat an unconfirmed row the same as a missing consent.

## 2. Malignant hyperthermia (MH) protocol — timed sequence

Trigger: rising ETCO2 with unchanged ventilation, unexplained tachycardia, and rising core temperature appearing together within a short window (see `red-flags.md` for the specific threshold). Do not wait for all three to fully develop before acting on two with a well-formed capnography waveform.

| Time (relative) | Action |
|---|---|
| T+0 min | Discontinue all volatile agents and succinylcholine; call for help / activate MH response; hyperventilate with 100% O2 at 2–3x normal minute ventilation |
| T+0–1 min | Page directing anesthesiologist with the trigger and numbers, not a narrative (see SKILL.md Communication style) |
| T+1–2 min | Retrieve MH cart; reconstitute dantrolene; call MH hotline |
| T+2–3 min | Give dantrolene 2.5 mg/kg IV — round UP to the nearest whole vial (each vial 20 mg) |
| T+7–8 min | If no reversal, repeat 2.5 mg/kg; continue at 5-minute intervals |
| Ceiling | Total dose ceiling 10 mg/kg absent further direction; doses up to 20 mg/kg reported in refractory cases under physician direction |
| Concurrent | Active cooling (cold IV fluids, surface cooling), treat hyperkalemia and arrhythmias per ACLS, send labs (ABG, CK, potassium, coagulation) |
| Post-reversal | Maintenance dantrolene 1 mg/kg every 4–6 hours for at least 24 hours, monitoring for recrudescence; ICU disposition |

**Worked dosing example:** 95 kg patient. First dose = 95 × 2.5 = 237.5 mg → round up to 12 vials × 20 mg = 240 mg. Second dose (if needed) = another 240 mg = 480 mg cumulative. Ceiling at 10 mg/kg = 950 mg = 48 vials — confirm pharmacy/cart stock supports this before a real event, not during one.

## 3. Local anesthetic systemic toxicity (LAST) protocol

Trigger: perioral numbness, tinnitus, metallic taste, or agitation shortly after a regional block or high-volume local infiltration, progressing to seizure or cardiovascular collapse.

| Step | Action |
|---|---|
| 1 | Stop injecting local anesthetic immediately; call for help |
| 2 | Airway management with 100% O2; avoid hyperventilation-induced alkalosis if possible |
| 3 | Suppress seizure with benzodiazepine (avoid propofol in a hemodynamically unstable patient — it worsens cardiac depression) |
| 4 | Give 20% lipid emulsion: bolus 1.5 mL/kg (lean body weight) over 1 minute, then infusion 0.25 mL/kg/min |
| 5 | Repeat bolus once or twice for persistent cardiovascular collapse; may increase infusion to 0.5 mL/kg/min if BP remains low |
| 6 | Continue lipid infusion for at least 10 minutes after hemodynamic stability |
| Ceiling | Upper limit ~10 mL/kg lipid emulsion over the first 30 minutes |
| If cardiac arrest | Standard ACLS with reduced epinephrine doses (<1 mcg/kg) — high-dose epinephrine worsens lipid resuscitation outcomes in animal data |

## 4. Medical-direction documentation template (CMS seven-step)

Fill contemporaneously per case where the directing anesthesiologist is billing medical direction (QK modifier, ≤4 concurrent rooms):

```
Case: [patient ID / room]
1. Pre-anesthetic exam performed by anesthesiologist: [time] — [Y/N + note if delegated]
2. Anesthesia plan established jointly: [time], plan: [summary]
3. Anesthesiologist present for induction: [time in] – [time out]
4. Anesthesiologist present for emergence: [time in] – [time out]
5. Intraoperative monitoring at [interval] by CAA; anesthesiologist available at: [location/room]
6. Emergencies during case requiring anesthesiologist: [none / describe + response time]
7. Post-anesthesia care documented by anesthesiologist: [time], note: [summary]
Concurrent rooms this anesthesiologist during this case: [count] (must remain ≤4 for QK; 5th concurrent room converts ALL rooms to medical supervision/AD for the overlap period)
```

## 5. PACU handoff structure (SBAR-style, fixed order every time)

```
S — [procedure], [total anesthesia time], ASA PS [class]
B — Relevant history: [allergies, OSA score, difficult airway Y/N]
A — Drugs and total doses given: [list with totals, not just "standard"]
   Hemodynamic course: [stable / notable events with times]
   Fluid balance: [crystalloid/colloid in, EBL, urine output]
R — Unresolved flags: [pain control status, residual paralysis reversal confirmed Y/N, any red flag from this case]
```
