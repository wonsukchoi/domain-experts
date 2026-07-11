# Anesthesiologist playbook

Filled protocols and tables for the recurring decisions — preop risk stratification, airway planning, malignant hyperthermia, regional anesthesia and anticoagulation, and PONV prophylaxis. Populate with the actual patient's numbers; the structures below are ready to execute, not descriptions of what a table should contain.

## 1. Preoperative risk-stratification pass

Run all four in the same preop visit — none alone is sufficient.

### ASA Physical Status (mortality correlate, not a technique choice)

| Class | Definition | Example |
|---|---|---|
| I | Healthy, no systemic disease | 25yo, no comorbidities, elective knee scope |
| II | Mild systemic disease, no functional limitation | Controlled hypertension, well-controlled diabetes |
| III | Severe systemic disease, functional limitation | Poorly controlled diabetes with end-organ effects, COPD limiting exertion |
| IV | Severe disease, constant threat to life | Recent MI (<3 months), severe valve disease, sepsis |
| V | Moribund, not expected to survive without surgery | Ruptured AAA, massive PE |
| VI | Brain-dead, organ donation | — |

Add "E" for emergency (e.g., "IIIE"). III and above: escalate monitoring plan and staff a backup provider before induction.

### STOP-Bang (OSA screening) — score ≥3 is high risk, ≥5 is high risk for moderate-to-severe OSA

| Item | Present = 1 point |
|---|---|
| **S**noring loudly | Yes/No |
| **T**ired during the day | Yes/No |
| **O**bserved apnea | Yes/No |
| **P**ressure (treated hypertension) | Yes/No |
| **B**MI > 35 | Yes/No |
| **A**ge > 50 | Yes/No |
| **N**eck circumference > 40cm | Yes/No |
| **G**ender male | Yes/No |

Score ≥3: default to opioid-sparing multimodal analgesia, regional where feasible, extended PACU monitoring, and continuous pulse oximetry overnight if opioids are used at all.

### Apfel simplified PONV score — each factor present = 1 point

| Points | Baseline PONV risk (no prophylaxis) |
|---|---|
| 0 | ~10% |
| 1 | ~21% |
| 2 | ~39% |
| 3 | ~61% |
| 4 | ~79% |

Factors: female sex, non-smoker, history of PONV or motion sickness, planned postoperative opioids. Prophylaxis default: 0-1 points → single agent or none; 2 points → two antiemetic classes; ≥3 points → two classes plus TIVA (avoid volatile agents and nitrous oxide).

### Revised Cardiac Risk Index (RCRI) — each = 1 point, for major noncardiac surgery

High-risk surgery, ischemic heart disease history, congestive heart failure history, cerebrovascular disease history, insulin-dependent diabetes, preop creatinine >2.0 mg/dL. 0-1 points: ~0.4-1.0% MI/cardiac arrest/death risk; ≥3 points: ~11%+ — triggers preop cardiology input and possibly stress testing before elective surgery.

## 2. Airway plan matrix

Predictors: Mallampati class III/IV, thyromental distance <6cm, mouth opening <3cm (interincisor), limited neck extension, high BMI, prior difficult airway documented.

| Prediction | Default plan |
|---|---|
| No predictors | Standard induction, video laryngoscope on standby per department default |
| 1-2 predictors present | Awake or asleep video laryngoscopy first-line, difficult airway cart in room, second experienced provider notified |
| Multiple predictors / prior documented difficult airway | Awake fiberoptic intubation, full difficult airway team present before induction |

**Can't intubate, can't oxygenate (CICO) — 2022 ASA algorithm attempt cap:**
1. Plan A: direct/video laryngoscopy — max 3 attempts total, no more than 1 by a less experienced provider.
2. Plan B: supraglottic airway (attempt once, optimize position/size before declaring failure).
3. Plan C: facemask ventilation with airway adjuncts and two-person technique.
4. Plan D: emergency front-of-neck access (cricothyrotomy) — decided and equipment opened the moment Plan C fails, not after further attempts at A/B.

Call for help at the first failed attempt, not after the third.

## 3. Malignant hyperthermia protocol (MHAUS)

Trigger: unexplained tachycardia + rising ETCO2 (often the earliest and most sensitive sign) + masseter or generalized rigidity following succinylcholine or a volatile agent.

**Immediate steps:**
1. Call for help, discontinue all triggering agents, call MHAUS hotline (1-800-644-9737).
2. Hyperventilate with 100% oxygen at flows >10 L/min; switch to a clean circuit/CO2 absorbent if available without delaying treatment.
3. **Dantrolene 2.5 mg/kg IV bolus**, repeat every 5-10 minutes until symptoms resolve, up to 10 mg/kg cumulative.
   - Reconstitution math for an 80 kg patient: 2.5 mg/kg × 80 kg = **200 mg initial dose**. Standard dantrolene vials are 20 mg — **200 mg ÷ 20 mg/vial = 10 vials**, each reconstituted per product insert, drawn up in parallel by extra hands.
4. Treat hyperkalemia (calcium, insulin/glucose, hyperventilation), treat arrhythmias (avoid calcium channel blockers with dantrolene), active cooling if core temp >39°C.
5. Send labs: ABG, CK, potassium, coagulation panel; anticipate ICU admission for at least 24 hours (recrudescence risk).

## 4. Regional/neuraxial anesthesia — ASRA anticoagulation hold and restart windows

| Agent | Hold before neuraxial/deep block | Restart after |
|---|---|---|
| Aspirin (monotherapy) | No hold required | No restriction |
| Clopidogrel | 5-7 days | 6 hours post-procedure (or per surgeon) |
| Prophylactic-dose LMWH | 12 hours | 12 hours (24h if traumatic tap) |
| Therapeutic-dose LMWH | 24 hours | 24 hours |
| Unfractionated heparin (subQ, prophylactic) | 4-6 hours | 1 hour |
| Unfractionated heparin (IV, therapeutic) | 4 hours + normal aPTT | 1 hour |
| Warfarin | Until INR ≤1.4 | Per surgical bleeding risk |

Verify against the current ASRA Fourth Edition guideline and institutional protocol before every block — drug list and windows are updated periodically.

**Local anesthetic systemic toxicity (LAST) — treat immediately on perioral numbness, metallic taste, tinnitus, or seizure during/after injection:**
1. Stop injecting, call for help, ensure airway/oxygenation, treat seizure (benzodiazepine, avoid propofol in hemodynamically unstable patients).
2. **20% lipid emulsion: 1.5 mL/kg bolus**, then infusion at 0.25 mL/kg/min; repeat bolus once or twice for persistent cardiovascular collapse, up to a ~10 mL/kg cumulative dose over the first 30 minutes.
3. Reduced epinephrine doses if ACLS needed (large doses can worsen outcomes in LAST-associated arrest).
4. Prolonged resuscitation may be needed — LAST cardiac arrest can require lipid-supported CPR for well over an hour; do not stop early.

## 5. Preoperative fasting (ASA 2017, floor not proxy)

| Intake | Minimum fasting time |
|---|---|
| Clear liquids | 2 hours |
| Breast milk | 4 hours |
| Infant formula / non-human milk / light meal | 6 hours |
| Fried or fatty meal, meat | 8 hours |

Independent aspiration-risk raisers regardless of clock time: trauma, opioid use, pregnancy, gastroparesis (diabetic or otherwise), bowel obstruction, significant obesity — treat these as a separate check, not covered by NPO status alone.

## 6. Multimodal analgesia default (opioid-sparing base layer)

Absent contraindication, build from: acetaminophen (scheduled, not PRN), NSAID/ketorolac (hold if active bleeding or renal concern), gabapentinoid for select high-pain procedures, regional block or local infiltration where feasible, and opioid reserved for breakthrough — not the first-line agent. Reassess against actual PACU pain scores, not the written order set alone.
