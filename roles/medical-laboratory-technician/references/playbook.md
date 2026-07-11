# Lab Operations Playbook

Filled reference tables with working numbers and thresholds. These are commonly cited defaults, not universal law — the facility's own procedure manual and medical director govern; deviate consciously and document why.

## 1. Westgard multirule QC — rule, trigger, and action

Two control levels run each shift; mean and SD established over 20+ runs per level.

| Rule | Trigger | Interpretation | Action |
|---|---|---|---|
| 1-2s | One control outside ±2 SD | Warning only | Inspect the other rules below; do not reject on this alone |
| 1-3s | One control outside ±3 SD | Random error | Reject the run; hold all patient results |
| 2-2s | Two consecutive controls (same level, or both levels same run) outside the same ±2 SD side | Systematic error | Reject the run; check calibration/reagent lot |
| R-4s | Range between two controls in one run exceeds 4 SD | Random error | Reject the run |
| 4-1s | Four consecutive controls (across levels/runs) outside the same ±1 SD side | Systematic error, trending | Reject the run; recalibrate |
| 10x | Ten consecutive controls fall on the same side of the mean | Systematic bias, no magnitude | Reject the run; check for reagent/calibration drift |

**Worked check.** Glucose Level 1 mean 100 mg/dL, SD 3 mg/dL; Level 2 mean 250 mg/dL, SD 7 mg/dL. Today's run: Level 1 = 106 mg/dL (+2.0 SD), Level 2 = 264 mg/dL (+2.0 SD). Neither individually trips 1-3s, but both landing on the same side at exactly ±2 SD in the same run is a 2-2s violation (across levels) — reject the run, hold patient results, and check for a shared cause (calibration drift, reagent lot change) before rerunning.

## 2. Delta-check limits by analyte (illustrative defaults — set per lab's own historical variance)

| Analyte | Delta-check limit | Typical window |
|---|---|---|
| Potassium | ±1.5 mmol/L | 72 hours |
| Sodium | ±10 mmol/L | 72 hours |
| Glucose | ±100 mg/dL (or 50% relative) | 24 hours |
| Creatinine | ±0.5 mg/dL (or 50% relative) | 72 hours |
| Calcium (total) | ±1.5 mg/dL | 72 hours |
| Hemoglobin | ±3 g/dL | 72 hours |

Delta trip → hold for repeat on the same specimen (rule out clot, dilution, instrument carryover) before deciding whether to escalate to a redraw or accept as a genuine clinical change.

## 3. HIL (hemolysis/icterus/lipemia) interference thresholds — representative

| Analyte | Hemolysis (H-index, mg/dL free Hgb) | Lipemia (L-index) | Icterus (I-index, mg/dL bilirubin) |
|---|---|---|---|
| Potassium | Interferes above ~50 | Minimal | Minimal |
| LDH | Interferes above ~20 | Minimal | Minimal |
| AST | Interferes above ~50 | Minimal | Minimal |
| Total bilirubin | Minimal | Interferes above ~200 | N/A |
| Triglycerides | Minimal | N/A (lipemic itself) | Minimal |
| Direct bilirubin, some immunoassays | Minimal | Minimal | Interferes above ~20 |

Actual numeric thresholds are method-specific — pull the interference table from the analyzer's package insert for the exact assay in use before applying these as more than a starting screen.

## 4. Critical (panic) value list and callback window — representative

| Analyte | Low critical | High critical | Callback window |
|---|---|---|---|
| Potassium | <2.5 mmol/L | >6.5 mmol/L | Within 15 minutes of verification |
| Glucose | <40 mg/dL | >500 mg/dL | Within 15 minutes |
| Sodium | <120 mmol/L | >160 mmol/L | Within 30 minutes |
| Hemoglobin | <7.0 g/dL | — | Within 30 minutes |
| Platelet count | <20,000/µL | >1,000,000/µL | Within 30 minutes |
| INR | — | >5.0 | Within 30 minutes |
| Blood culture, positive | Any growth | — | Immediate, upon Gram stain result |

Every callback is logged with: value, unit, date/time of verification, date/time of call, name and title of person notified, and confirmation of read-back.

## 5. Specimen rejection criteria

| Condition | Threshold | Action |
|---|---|---|
| Gross hemolysis on potassium/LDH/AST order | H-index exceeds analyte's interference threshold | Reject that analyte; recollect |
| Clotted specimen (hematology/coag) | Visible clot on inversion or in automated clot detection | Reject entire specimen; recollect |
| QNS (quantity not sufficient) | Below minimum volume for ordered panel | Reject; recollect or prioritize by clinical urgency if redraw is difficult |
| Wrong tube/anticoagulant | Tube type doesn't match test requirement | Reject; recollect in correct tube |
| Unlabeled or mislabeled specimen | Any discrepancy between label and order | Reject outright — no exceptions for "obviously correct" mislabels |
| Prolonged transport time | Exceeds analyte-specific stability window (e.g., glucose >2 hours unspun without a glycolysis inhibitor tube) | Reject or flag per stability data; recollect if outside window |

## 6. ISLH-consensus criteria for manual smear review (representative subset)

Any one of the following on a CBC/differential triggers manual review over the automated differential:

1. Blasts or other immature cells flagged by the analyzer.
2. Nucleated RBCs ≥2 per 100 WBC counted.
3. New, unexplained absolute lymphocytosis (>4.0 × 10⁹/L) in an adult without a known lymphoproliferative history.
4. WBC <1.0 × 10⁹/L or >30 × 10⁹/L, first occurrence for this patient.
5. Platelet count <20,000/µL or >1,000,000/µL, first occurrence.
6. Analyzer flags for atypical lymphocytes, immature granulocytes, or RBC morphology it cannot classify.
7. Any result the ordering provider specifically requests morphologic confirmation on.

Manual review means a technologist-performed 100-cell differential with morphology comments; discordant or malignancy-suggestive findings route to pathologist review before the result is finalized.
