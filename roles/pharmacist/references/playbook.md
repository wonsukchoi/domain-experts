# Pharmacist — Playbook

## Dose-verification worksheet (renally-cleared drug)

| Field | Value | Notes |
|---|---|---|
| Patient age | 82 | |
| Weight | 55 kg | actual body weight; use ideal/adjusted weight if obese per drug-specific guidance |
| Serum creatinine | 1.6 mg/dL | most recent, within 48h for inpatient |
| Sex | Female | affects CrCl multiplier (x0.85) |
| CrCl (Cockcroft-Gault) | 23.5 mL/min | [(140-age) x wt] / (72 x SCr) x 0.85 |
| Drug renal threshold | <30 mL/min triggers adjustment | per drug label, not a universal cutoff |
| Ordered regimen | 55 mg SC q12h | 1 mg/kg BID — standard treatment dosing |
| Adjusted regimen | 55 mg SC q24h | per-dose mg unchanged, frequency reduced |
| Action | Hold + prescriber contact | discrepancy exceeds drug's therapeutic-index sensitivity |

## Interaction-screening triage sequence

1. Run the full active-medication list (not just the new order) through the interaction database.
2. For each flagged pair, pull: mechanism (pharmacokinetic vs. pharmacodynamic), severity tier, and whether the interacting drugs are at doses/timing where the mechanism is clinically active.
3. Classify:
   - **Mechanism inactive at these doses/timing** (e.g. staggered administration already separates absorption-interacting drugs) — document as reviewed, no action.
   - **Mechanism active, manageable** (e.g. additive QT prolongation, both below individual thresholds but additive risk) — recommend monitoring (ECG, lab), not necessarily discontinuation.
   - **Mechanism active, high-severity, no safe monitoring path** — hold and contact prescriber with an alternative.
4. Document the classification and rationale for every flagged pair reviewed, including "reviewed, no action" — an unreviewed flag left in the system is indistinguishable from a missed one during audit.

## Medication-reconciliation discrepancy table (care transition)

| Medication | Admission note | Fill history (30-day) | Patient interview | Resolved list |
|---|---|---|---|---|
| Lisinopril 10mg | Daily | Last fill 45 days ago | "I take it most days" | Continue 10mg daily, counsel adherence |
| Metformin 500mg | BID | BID, filled on schedule | Confirms BID | Continue as ordered |
| Ibuprofen 400mg | Not listed | Not a prescription fill | "I take it OTC for my knee, most days" | Add to list — flag for NSAID/ACE-inhibitor renal interaction given lisinopril |
| Atorvastatin 20mg | Daily | No fill in 90 days | "I stopped, it upset my stomach" | Remove from active list, document reason, flag for prescriber follow-up on alternative |

Rule: a medication appearing on only one source is not automatically wrong or right — resolve every single-source entry with the patient or prescriber before finalizing the reconciled list, and document why each addition or removal was made.

## Therapeutic-substitution conversion worked example

Formulary swap: patient on fentanyl patch 25 mcg/hr, formulary requires conversion to oral morphine equivalent for a planned route change.

- Fentanyl patch 25 mcg/hr ≈ 60-134 mg oral morphine equivalent/day per standard equianalgesic tables (wide range reflects incomplete cross-tolerance).
- Do not convert at the top of the range for an opioid-naive-relative-to-oral-morphine patient — start at 50% of calculated equivalent dose (30-67 mg/day) to account for incomplete cross-tolerance, then titrate based on response.
- Document the calculated range, the chosen starting dose, and the incomplete-cross-tolerance rationale in the conversion note — a mechanical "convert to the table midpoint" without the safety discount is the common conversion error.
