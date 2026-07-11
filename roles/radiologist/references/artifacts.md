# Radiologist — artifacts

Filled templates and reference tables. These are working documents to populate, not descriptions of what a document should contain.

## Structured chest CT report (filled example)

```
EXAM: CT Chest without contrast
CLINICAL HISTORY: 61F, chronic cough x 8 weeks, former smoker (25 pack-years, quit 2016).
COMPARISON: None available.
TECHNIQUE: Helical CT of the chest without IV contrast, 1.25mm reconstructions,
lung and soft tissue algorithms. CTDIvol 4.1 mGy, DLP 148 mGy·cm.

FINDINGS:
Lungs/airways: Mild bronchial wall thickening, bilateral, most pronounced in the
lower lobes — nonspecific, compatible with chronic bronchitis given history.
No bronchiectasis. 8mm (average of 9mm long-axis and 6mm short-axis) solid
noncalcified nodule, right upper lobe, series 3 image 61 — see Impression 1.
No other nodule >4mm.
Pleura: No effusion or pneumothorax.
Mediastinum/hila: No mediastinal or hilar lymphadenopathy (short axis <1cm).
Heart/pericardium: Mild coronary calcification. No pericardial effusion.
Upper abdomen (imaged): Unremarkable liver, adrenal glands, visualized kidneys.
Bones: No aggressive osseous lesion. Mild degenerative changes, thoracic spine.

IMPRESSION:
1. 8mm solid noncalcified right-upper-lobe nodule, high-risk category per
   Fleischner Society 2017 criteria given smoking history. Recommend follow-up
   low-dose CT chest in 6-12 months, with consideration for further CT at
   18-24 months if stable. PET/CT or tissue sampling not indicated at this
   size/risk tier absent interval growth.
2. Mild chronic bronchial wall thickening, correlating with reported chronic
   cough; no endobronchial lesion identified.
3. No acute cardiopulmonary process.

Findings and recommendation discussed with Dr. [ordering physician] by
telephone at 14:40; read-back confirmed by recipient.
```

## Fleischner Society 2017 — solid pulmonary nodule follow-up (single nodule)

| Nodule size (mean of long + short axis) | Low-risk patient | High-risk patient |
|---|---|---|
| <6mm | No routine follow-up | Optional CT at 12 months |
| 6-8mm | CT at 6-12 months, then consider CT at 18-24 months | CT at 6-12 months, then CT at 18-24 months |
| >8mm | Consider CT at 3 months, PET/CT, or tissue sampling | Consider CT at 3 months, PET/CT, or tissue sampling |

Risk-tier drivers: older age, heavier/longer smoking history (including remote quitters with a substantial pack-year burden), upper-lobe location, spiculated margins, emphysema, family history of lung cancer. Part-solid and ground-glass nodules follow a separate, longer-interval table (up to 5 years) — do not apply the solid-nodule table to a subsolid nodule.

## BI-RADS categories and management (ACR BI-RADS Atlas, 5th ed.)

| Category | Meaning | Malignancy likelihood | Management |
|---|---|---|---|
| 0 | Incomplete | — | Additional imaging or prior comparison needed |
| 1 | Negative | 0% | Routine screening interval |
| 2 | Benign | 0% | Routine screening interval |
| 3 | Probably benign | <2% | Short-interval (6-month) follow-up |
| 4A | Low suspicion | 2-<10% | Biopsy |
| 4B | Moderate suspicion | 10-<50% | Biopsy |
| 4C | High suspicion | 50-<95% | Biopsy |
| 5 | Highly suggestive of malignancy | ≥95% | Biopsy |
| 6 | Known biopsy-proven malignancy | — | Definitive treatment planning |

A category-3 assignment is only valid when the morphology strictly meets the published probably-benign descriptors (e.g., a circumscribed mass, a focal asymmetry that disperses, a cluster of punctate calcifications matching the classic pattern) — a lesion that doesn't strictly fit gets upgraded to 4A, not softened into a 3 to avoid a biopsy conversation.

## Lung-RADS v2022 (v1.1) — screening-population only

| Category | Finding | Management |
|---|---|---|
| 0 | Incomplete | Prior imaging needed for comparison |
| 1 | Negative | Continue annual screening |
| 2 | Benign appearance/behavior | Continue annual screening |
| 3 | Probably benign | Short-term (6-month) follow-up LDCT |
| 4A | Suspicious | 3-month follow-up LDCT, or PET/CT if ≥8mm solid component |
| 4B/4X | Suspicious — additional features | Chest CT with contrast, PET/CT, and/or tissue sampling |

Lung-RADS applies only within an annual low-dose CT screening program with an established prior; an incidental nodule found on a diagnostic (non-screening) CT is scored against Fleischner, not Lung-RADS.

## Contrast premedication protocols (ACR Manual on Contrast Media, prior reaction to iodinated contrast)

**13-hour protocol (standard elective):**
- Prednisone 50mg PO at 13h, 7h, and 1h before contrast administration.
- Diphenhydramine 50mg PO/IM/IV 1h before contrast administration.

**12-hour accelerated protocol (when the 13-hour schedule can't be met):**
- Methylprednisolone 32mg PO at 12h and 2h before contrast administration.
- Diphenhydramine 50mg PO/IM/IV 1h before, optional per institutional policy.

A documented severe (anaphylactoid) prior reaction is a reason to avoid the same contrast class and consult with the ordering clinician on an alternative study, not an indication to premedicate and proceed as usual.

## Critical-results communication log (filled example row)

| Finding | Urgency tier | Method | Recipient | Time called | Confirmed read-back | Documented in report |
|---|---|---|---|---|---|---|
| Large right MCA territory acute infarct with early mass effect | Critical | Direct phone call | Dr. Alvarez (ED attending) | 03:14 | Yes — repeated back finding and side | Yes, addendum 03:18 |
| 8mm high-risk pulmonary nodule (incidental) | Routine/actionable, non-urgent | Phone call same business day | Dr. Chen (PCP) | 14:40 | Yes | Yes, in original report |

Urgency-tier definitions (per the ACR Practice Parameter framework, with commonly implemented institutional timeframes): **critical/life-threatening** — direct communication as immediately as possible, commonly within 1 hour, by phone or equivalent direct channel; **urgent, non-emergent, unexpected** — timely direct communication, commonly within 24 hours, not deferred to routine report distribution; **routine** — standard report routing is sufficient. Exact minute/hour thresholds are set by institutional policy under the parameter, not by the parameter itself — confirm local policy rather than assuming these numbers.
