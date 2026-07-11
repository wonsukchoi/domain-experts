# Playbook

Filled protocols and tables an agent can execute or populate directly — not descriptions of what a protocol should contain.

## Risk-classification table (used at intake, admission, and every reassessment)

| Category | Example findings | Management |
|---|---|---|
| Low risk — midwifery-led | Singleton, vertex, term, no significant maternal/fetal comorbidity, prior uncomplicated vaginal births | Independent midwifery management; standard intermittent auscultation protocol |
| Consult (informal) | Post-term (≥41 weeks), GBS-positive requiring prophylaxis logistics, mild gestational hypertension without severe features | Midwife continues as lead; discusses plan with collaborating OB, documents the discussion |
| Co-management | Twin gestation (both vertex), well-controlled gestational diabetes, prior one low-transverse cesarean (TOLAC candidate) | OB and midwife jointly manage; delivery plan and thresholds for transfer agreed in writing before labor |
| Transfer (formal) | Breech presentation at labor onset, Category III tracing, preeclampsia with severe features, non-vertex twin | Care transfers to OB/MFM per written protocol; midwife may continue support role but is not the lead decision-maker |

## Labor-progress benchmarking table (contemporary curve, ACOG/SMFM 2014 / Zhang 2010)

| Dilation | Expected pattern (5th-95th percentile, nulliparous) | Arrest threshold before escalation |
|---|---|---|
| 4-6cm | Highly variable; can be slow (this range is often what used to be mislabeled "prolonged latent phase" under Friedman) | No arrest diagnosis before 6cm regardless of elapsed time, absent a separate indication |
| 6cm onward (active phase begins) | Roughly 0.5-1.2cm/hour median, wide tail | ≥4h no change with adequate contractions (MVU ≥200), or ≥6h with inadequate contractions despite oxytocin titration |
| Second stage, nulliparous | Median ~1h, up to 3h without epidural / 4h with epidural before consult trigger | Consult at 3h (no epidural) / 4h (epidural) without descent |
| Second stage, multiparous | Median ~20-30min, up to 2h without epidural / 3h with epidural before consult trigger | Consult at 2h (no epidural) / 3h (epidural) without descent |

## Oxytocin titration and adequacy check (worked sequence)

1. Start at 1-2 mU/min; increase by 1-2 mU/min every 30-40 minutes per facility protocol until contractions are q2-3min, moderate-strong by palpation, or MVU ≥200 by IUPC.
2. At each increase, log timestamp, dose, and current MVU/palpation quality.
3. If MVU reaches ≥200: start (or restart) the 4-hour arrest clock from that timestamp — not from when oxytocin was first started.
4. If MVU remains <200 at or near maximum protocol dose after 6 hours: this is inadequate contractions despite oxytocin — arrest can be considered at the 6-hour mark if no cervical change, per protocol, with OB consult.

## GBS intrapartum prophylaxis decision table (CDC pathway)

| Situation | Action |
|---|---|
| Culture positive, drawn 35-37 weeks | Prophylaxis (penicillin G first-line; cefazolin or clindamycin/vancomycin per allergy/resistance profile) |
| Culture negative, drawn 35-37 weeks, valid (<5 weeks old at delivery) | No prophylaxis needed based on culture |
| No valid culture available, and any of: preterm labor, ROM ≥18h, intrapartum temp ≥38.0°C, prior infant with GBS disease, GBS bacteriuria this pregnancy | Prophylaxis via risk-based pathway |
| No valid culture, none of the above risk factors present | No prophylaxis indicated; document reasoning |
| Planned cesarean, no labor, membranes intact | No prophylaxis needed regardless of GBS status |

## Postpartum hemorrhage staged response (CMQCC OB Hemorrhage Toolkit, adapted)

| Stage | Trigger (cumulative QBL or clinical signs) | Actions |
|---|---|---|
| Stage 0 | Any vaginal birth, prophylactic | AMTSL (uterotonic + controlled cord traction + massage); QBL tracking starts at birth, not after concern arises |
| Stage 1 | QBL >500mL vaginal / >1000mL cesarean, or vitals trending abnormal | Increase uterotonic dosing, fundal massage, IV access confirmed/upsized, notify OB, begin hemorrhage-cart staging, weigh all materials going forward |
| Stage 2 | QBL >1000mL cumulative, or Stage 1 measures not controlling bleeding within ~15-30 min | Second-line uterotonics (methylergonovine, carboprost, or misoprostol per contraindication profile), consider tranexamic acid, type and crossmatch, OB at bedside, consider exam under anesthesia for retained tissue/laceration |
| Stage 3 | QBL >1500mL, or 2+ units transfused, or vital-sign instability (SBP <90, HR >110, or sustained abnormal trend) | Massive transfusion protocol activation, OR for exam/possible surgical management (balloon tamponade, uterine artery embolization, B-Lynch, hysterectomy as last resort), full team response |

## Informed-choice documentation template (populate per decision point)

```
Decision point: <e.g., GBS intrapartum prophylaxis>
Discussed: <specific risk numbers, e.g., "~1-2 per 1,000 births early-onset GBS disease without
  prophylaxis in GBS-positive patients, reduced to ~0.1-0.3 per 1,000 with adequate prophylaxis">
Alternatives discussed: <e.g., "declining prophylaxis, monitoring newborn closely for signs of
  infection per pediatric protocol">
Patient's stated choice and reasoning: <verbatim or close paraphrase>
Plan: <what's actually being done as a result>
```

## Consult/transfer trigger quick-reference (fires an immediate protocol action, not a discussion)

- Category III fetal heart tracing at any point → immediate OB notification, prepare for expedited delivery.
- Cumulative QBL crossing 1000mL → Stage 2 hemorrhage response, OB at bedside.
- Breech, transverse, or compound presentation discovered at any gestational age in labor → transfer per protocol.
- Cervical exam consistent with active-phase arrest per the benchmarking table above → OB consult before any further oxytocin escalation.
- Maternal blood pressure ≥160/110 sustained, or any new severe-feature symptom (headache unresponsive to acetaminophen, visual changes, epigastric pain, clonus) → immediate OB notification regardless of prior blood-pressure history.
