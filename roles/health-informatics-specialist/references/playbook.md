# Health Informatics Specialist — Playbook

## Quality measure validation and extrapolation (filled example)

| Step | Value |
|---|---|
| Denominator (per measure spec) | 1,200 patients |
| Numerator (structured data only, initial automated calculation) | 620 patients |
| **Initial reported rate** | 620 ÷ 1,200 = **51.7%** |
| Manual chart review sample size | 50 non-numerator patients |
| Discrepancy found (result existed but only as scanned attachment) | 8 of 50 = **16%** |
| Non-numerator population | 1,200 − 620 = 580 |
| Estimated additional true-positive patients (580 × 16%) | ≈ **93** |
| Corrected estimated numerator | 620 + 93 = **713** |
| **Corrected estimated rate** | 713 ÷ 1,200 = **59.4%** |
| **Understatement** | 59.4% − 51.7% = **7.7 percentage points** |

**Use:** Always validate an automated measure calculation against a manual chart review sample, and extrapolate any discrepancy rate found to the full population rather than treating it as an isolated finding.

## Measure specification interpretation checklist

1. Pull the exact numerator, denominator, and exclusion definitions from the measure steward's current technical specification — don't rely on a summarized or prior-year understanding.
2. Confirm the age range, lookback period, and qualifying encounter/event definitions match the spec precisely.
3. Confirm every listed exclusion criterion is applied, checked against a sample of denominator patients.
4. Confirm required data elements are captured as structured/coded fields, not free text, before trusting the automated calculation.

## CDS alert override rate review table (illustrative structure)

| Alert | Override rate | Interpretation | Action |
|---|---|---|---|
| Drug interaction warning A | 94% | Alert fatigue — likely too broad | Narrow criteria to higher-risk interaction subset |
| Preventive care reminder B | 45% | Within normal range for a reminder-type alert | Monitor, no immediate redesign needed |
| Allergy conflict warning C | 91% | Alert fatigue | Review specificity of allergy-matching logic |

**Use:** Treat any alert with an override rate above roughly 90% as a redesign candidate — the fix is narrowing the alert's triggering criteria, not clinician retraining or compliance messaging.

## Interoperability/terminology mapping diagnostic checklist

1. Confirm the data element in question exists in the source system (check the source record directly, not just the received exchange).
2. Identify the source system's local code for this data element.
3. Check whether that local code is mapped to the required standard vocabulary (LOINC for labs, RxNorm for medications, SNOMED CT/ICD-10 for diagnoses).
4. If unmapped or incorrectly mapped, this is the likely cause of the apparent "missing data" — correct the mapping rather than concluding the data doesn't exist.

## Findings and recommendation memo — filled example

> **eCQM Data Quality Review — Diabetes A1c Control Measure**
> Initially reported rate: 51.7% (620/1,200), calculated from structured LOINC-coded lab data only.
> Manual chart review (50-record sample): 16% of non-numerator patients actually had a qualifying A1c result, documented only as a scanned attachment rather than a structured lab result.
> **Extrapolated corrected rate: 59.4% (713/1,200 estimated)** — a 7.7 percentage point understatement in the originally reported rate.
> **Recommendation: Flag the historical reporting period as understated pending remediation. Work with the lab interface team to ensure all A1c results transmit as structured, LOINC-coded discrete results going forward, not as scanned attachments.**
