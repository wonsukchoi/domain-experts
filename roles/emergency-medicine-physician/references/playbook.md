# Emergency Medicine Playbook

Filled tools an ED physician actually runs at the bedside — decision-rule tables with real cutoffs, order-set sequences, and a disposition template. Populate with the specific patient's numbers; don't describe the tool, run it.

## 1. HEART score (chest pain risk stratification)

| Component | Criteria | Points |
|---|---|---|
| **H**istory | Slightly/non-suspicious = 0; moderately suspicious = 1; highly suspicious = 2 |
| **E**KG | Normal = 0; nonspecific repolarization disturbance = 1; significant ST deviation = 2 |
| **A**ge | <45 = 0; 45–65 = 1; >65 = 2 |
| **R**isk factors (HTN, hyperlipidemia, DM, obesity, smoking, family history, prior atherosclerotic disease) | None = 0; 1–2 = 1; ≥3 or known atherosclerotic disease = 2 |
| **T**roponin | ≤normal limit = 0; 1–3x normal limit = 1; >3x normal limit = 2 |

**Risk bands and action:**

| Total score | Risk category | 6-week MACE rate | Disposition |
|---|---|---|---|
| 0–3 | Low | 0.9–1.7% | HEART Pathway eligible: discharge if two troponins negative 3h apart, no ischemic EKG changes |
| 4–6 | Moderate | 12–16.6% | Admit or observe for serial troponin/telemetry; not single-troponin-discharge eligible |
| 7–10 | High | 50–65% | Admit, expedite cardiology, treat as acute coronary syndrome pending workup |

## 2. PERC rule (pulmonary embolism rule-out — use only if pretest probability is already low/gestalt <15%)

All 8 must be true to rule out PE without D-dimer:
1. Age <50
2. HR <100
3. SpO2 ≥95% on room air
4. No prior DVT/PE
5. No recent trauma or surgery (≤4 weeks)
6. No hemoptysis
7. No exogenous estrogen
8. No unilateral leg swelling

**If any criterion fails, or pretest probability isn't already low, do not use PERC** — proceed to Wells criteria instead:

| Wells criterion | Points |
|---|---|
| Clinical signs of DVT | 3 |
| PE is #1 diagnosis or equally likely | 3 |
| HR >100 | 1.5 |
| Immobilization/surgery in past 4 weeks | 1.5 |
| Prior DVT/PE | 1.5 |
| Hemoptysis | 1 |
| Malignancy (treated within 6 months or palliative) | 1 |

Score ≤4: PE unlikely → D-dimer; if negative, PE excluded. Score >4: PE likely → CT pulmonary angiogram directly, skip D-dimer.

## 3. Sepsis hour-1 bundle (Surviving Sepsis Campaign, 2018 update)

Clock starts at time of recognition (sepsis-alert trigger or clinical suspicion), not at triage time.

| Step | Action | Threshold/target |
|---|---|---|
| 1 | Measure lactate | Remeasure if initial ≥2 mmol/L |
| 2 | Obtain blood cultures | Before first antibiotic dose, don't delay antibiotics to obtain them |
| 3 | Administer broad-spectrum antibiotics | Within 1 hour of recognition |
| 4 | Begin crystalloid bolus | 30 mL/kg for hypotension or lactate ≥4 mmol/L |
| 5 | Reassess volume status/perfusion | If hypotensive after bolus or initial lactate ≥4, add vasopressors to target MAP ≥65 mmHg |

## 4. ESI (Emergency Severity Index) triage assignment

Walk the algorithm in order, stop at first "yes":

1. **Requires immediate life-saving intervention?** → ESI 1.
2. **High-risk situation, new confusion/lethargy, or severe pain/distress?** → ESI 2.
3. **How many resources will this visit need** (labs, imaging, IV fluids, specialist consult each count as one; a single X-ray = 1 resource, an EKG alone doesn't count):
   - 0 resources expected → ESI 5
   - 1 resource expected → ESI 4
   - ≥2 resources expected → ESI 3, **then check danger-zone vitals**
4. **Danger-zone vitals for a would-be ESI 3** (any one bumps to ESI 2): adult HR >100, RR >20, SpO2 <92%; pediatric age-adjusted equivalents.

## 5. Boarding / crowding escalation (NEDOCS-anchored)

| NEDOCS score | Interpretation | Operational response (not a clinical threshold change) |
|---|---|---|
| <60 | Not busy / busy | Standard flow |
| 60–100 | Overcrowded | Activate split-flow/vertical track for ESI 4–5 |
| 100–140 | Severely overcrowded | Charge nurse escalates to bed management/house supervisor; increase reassessment frequency for boarders |
| >140 | Dangerously overcrowded | Hospital-wide surge protocol; diversion consideration per hospital policy |

The clinical risk-stratification threshold (HEART, Wells, ESI danger-zone vitals) does not change at any NEDOCS level — only staffing allocation and reassessment cadence do.

## 6. Discharge / return-precaution template (filled example)

> "Diagnosis today: [working diagnosis, e.g., 'musculoskeletal chest wall pain, coronary event ruled out per HEART Pathway']. What we ruled out and how: [specific tests/scores, e.g., 'HEART score 2, troponins negative 3 hours apart, no ischemic EKG changes']. Return immediately (call 911, do not drive) if: [named, specific triggers tied to the ruled-out badness, e.g., 'chest pain at rest, new shortness of breath, sweating with the pain, or fainting']. Follow up: [named clinic/timeframe, e.g., 'primary care within 1 week; cardiology if pain recurs']."

## 7. EMTALA screening/stabilization sequence (order matters)

1. Medical screening exam (MSE) performed by qualified provider — sufficient to determine whether an emergency medical condition (EMC) exists. A triage vitals check alone does not satisfy this.
2. If an EMC is found: stabilize within the hospital's capability before any transfer, discharge, or turn-away for inability to pay is considered.
3. If transfer is medically necessary and the patient is stabilized (or transfer risk/benefit is documented when not fully stabilized): receiving facility must have accepted and have capacity; transfer packet includes MSE findings, treatment given, and physician certification of the risk/benefit determination.
4. Insurance status, ability to pay, and any receiving facility's or insurer's preference are not inputs to steps 1–3 — they're addressed after the EMTALA obligation is satisfied.
