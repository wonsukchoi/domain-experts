# Bench Playbook

Operational defaults with concrete thresholds. Every instrument and lab has its own procedure manual — these are the shape of the decision, not a substitute for the local SOP.

## 1. Westgard rule selection by Sigma-metric

Sigma = (%TEa − %bias) / %CV, computed from the assay's total allowable error (CLIA fixed limit or manufacturer claim), the bias from the last method-comparison or PT study, and the control's coefficient of variation.

| Sigma | Rule set | Controls per run (N) | What a violation means |
|---|---|---|---|
| ≥6 | 1_3s only | 2 | Excellent method; only gross random error trips it |
| 5 to <6 | 1_3s / 2_2s | 2 | Good method; add cross-control systematic-shift detection |
| 4 to <5 | 1_3s / 2_2s / R_4s / 4_1s | 4 | Marginal method; full multirule needed to hold false-rejection rate down while still catching systematic drift |
| <4 | Method review | — | QC frequency isn't the fix — escalate to the lab director; consider a different method or reagent lot before it's used clinically |

**Rule definitions, applied at N=4 (two levels, two runs, or four controls in one run):**
- **1_3s** — any single control beyond mean ±3SD. Rejects on random error. Always in force regardless of Sigma tier.
- **2_2s** — two consecutive controls, either the same level across two runs or two different levels in the same run, both beyond ±2SD in the *same direction*. Signals systematic error (calibration, reagent lot, or a drifting reference electrode).
- **R_4s** — the range between two controls within the same run spans >4SD (e.g., one control +2.1SD, the other −2.3SD). Signals random error at the higher-N tiers.
- **4_1s** — four consecutive controls, across runs, all beyond ±1SD in the same direction. Signals a smaller but persistent systematic shift building over time — the one a same-day check misses.

**On any violation:** hold the entire run's patient results, not just the flagged analyte. Investigate before rerunning — check reagent lot number and expiration, calibration due date, maintenance log, and whether a new calibrator lot went in since the last in-control run. A pass on rerun without an identified cause is not resolution; it's a coin flip that came up heads.

## 2. Specimen acceptability gate (before anything is tested)

Reject or flag for recollection when any of the following hold, and document the reason code in the LIS:

- **Identification mismatch** — label doesn't match requisition on two identifiers (name + DOB/MRN), or the specimen is unlabeled at the bench.
- **Wrong tube/anticoagulant** for the ordered test (e.g., a potassium drawn in a green-top heparin tube run on a system validated for serum only, or a citrate tube underfilled below the fill line for coagulation studies).
- **Clotted whole blood/CBC or coagulation specimen** — visible clot on inversion or on the mixer.
- **Stability window exceeded** — time since draw or since centrifugation beyond the analyte's published stability (e.g., plasma glucose uncentrifuged >2 hours drifts down from glycolysis; potassium in an unspun tube rises over time from cellular leakage).
- **H/I/L index above the assay's published interference threshold** for that specific analyte — hemolysis inflates potassium, LDH, and AST; icterus interferes with bilirubin-adjacent and some enzymatic assays; lipemia scatters light-based methods. Reject or flag *only the affected analytes*, not the whole panel, unless the interference is severe enough to affect the method broadly.

## 3. Delta check

Compare the current result to the patient's most recent prior result for the same analyte; flag when the change exceeds the analyte's plausible-biology threshold in a timeframe too short to explain it (lab-specific, commonly expressed as an absolute or percent change — e.g., sodium change >10 mmol/L within 24 hours, hemoglobin change >3 g/dL within 24 hours without a documented transfusion or bleed).

**On a delta-check flag:**
1. Confirm specimen identity against the requisition and prior draw — this is the step that actually catches a mislabeled tube; re-testing the same tube cannot.
2. If identity checks out, consider a clinical explanation (transfusion, dialysis, IV fluid running into the draw site) documented in the chart.
3. If no explanation is found and identity can't be independently reconfirmed, request a re-draw before release.
4. Document which of the three resolved the flag — this becomes the audit trail an inspector reviews.

## 4. Critical (panic) value callback sequence

1. Result crosses the lab's defined critical threshold (lab- and analyte-specific; commonly potassium <2.8 or >6.0 mmol/L, glucose <40 or >500 mg/dL — confirm against the local policy, these are illustrative, not universal).
2. Call the ordering unit within the policy's time window (commonly 30–60 minutes from result finalization).
3. Deliver patient identifier, analyte, value, units, and reference range verbally.
4. Require the receiver to read the value back; do not accept "got it" as confirmation.
5. Log caller, receiver name/role, time of call, and read-back confirmation in the LIS or callback log — this record, not the phone call itself, is what satisfies the accreditation requirement.
6. If no clinical staff member is reachable within the window, escalate per the lab's defined escalation path (charge nurse → provider → nursing supervisor) — "I called once and no one answered" is not closure.

## 5. Proficiency testing (PT) handling

- Log PT specimens in upon arrival exactly like a patient accession — same worksheet, same rotation, same staff who'd normally run that analyte.
- **Never** send a PT sample to a reference or sister laboratory for testing, and never discuss expected results with another lab or a colleague outside the testing bench before submission. Both are CLIA-prohibited "testing referral" and have resulted in real accreditation and certification loss.
- On a PT failure (any analyte scoring below the acceptable limit, or two of three consecutive events failing for one analyte), open a documented investigation — root cause, corrective action, and evidence the fix was verified — before the next PT event, not after.
