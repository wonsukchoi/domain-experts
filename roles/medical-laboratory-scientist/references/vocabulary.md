# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Westgard Rules / multirule QC

- **Definition:** a decision system (1_3s, 2_2s, R_4s, 4_1s, etc.) for accepting or rejecting an analytic run based on where control results fall relative to their established mean and SD, chosen to match the assay's error tolerance.
- **Practitioner usage:** "Level 2 tripped 2_2s, not 1_3s — that's a systematic shift, hold the run and check the calibration before rerunning."
- **Common misuse:** treating every QC failure the same way ("rerun and see if it passes") instead of reading which rule fired — 1_3s and 2_2s point to different root causes and need different investigations.

## Sigma-metric

- **Definition:** a single number, Sigma = (%TEa − %bias)/%CV, describing how much room an assay has between its normal analytic noise and the error limit that would make a result clinically wrong.
- **Practitioner usage:** "This assay is only running Sigma 4.5 since the reagent lot change — we need the full multirule now, not the lean 1_3s-only schedule we used to run."
- **Common misuse:** assuming Sigma is a fixed property of the analyte rather than the specific instrument/reagent/calibration combination in use today — a method comparison or reagent lot change can move it.

## Delta check

- **Definition:** an automatic comparison of a patient's current result to their own prior result for the same analyte, flagging a change too large or too fast to be plausible biology.
- **Practitioner usage:** "Sodium delta-checked at +14 mmol/L in six hours with no documented fluid or dialysis — confirm identity before this goes out, not just a repeat on the same tube."
- **Common misuse:** resolving a delta-check flag by re-testing the same tube, which can only rule out an analyzer error — the flag exists specifically to catch specimen misidentification, which a repeat on the same tube cannot detect.

## Critical (panic) value

- **Definition:** a result far enough outside the reference range to represent an immediate threat to the patient, requiring a documented, time-bound direct notification to a clinician — not merely a flagged abnormal result.
- **Practitioner usage:** "6.7 is critical regardless of the fact she's a known dialysis patient — the callback and read-back documentation still happen on the clock."
- **Common misuse:** treating "expected for this patient" as grounds to skip or delay the callback — the notification requirement is independent of clinical plausibility.

## Total Allowable Error (TEa)

- **Definition:** the maximum combined bias-plus-imprecision an analyte's result can have before it's considered clinically unacceptable — set by CLIA (fixed limits for regulated analytes), a professional body, or the manufacturer.
- **Practitioner usage:** "TEa for potassium is a fixed ±0.5 mmol/L, not a percentage — that's what the Sigma-metric calculation for this assay is measured against."
- **Common misuse:** confusing TEa with the reference (normal) range — TEa is about how wrong the measurement is allowed to be, not what a healthy value looks like.

## Preanalytical / analytical / postanalytical phase

- **Definition:** the three phases of the total testing process — preanalytical (ordering through specimen receipt), analytical (the actual measurement), postanalytical (reporting, interpretation, and action on the result).
- **Practitioner usage:** "This isn't an analyzer problem — the specimen sat unspun for three hours on the floor, that's a preanalytical failure."
- **Common misuse:** defaulting to blaming the instrument for an error, when published data attributes the largest share of total laboratory error to the preanalytical phase, not the analytic one.

## Proficiency testing (PT) vs internal QC

- **Definition:** internal QC is the lab's own daily control-material testing against its own established limits; PT is an external, regulator-mandated program (e.g., CAP Surveys) where blind samples from an outside agency are tested and graded against peer laboratories.
- **Practitioner usage:** "PT samples get logged and run exactly like a patient specimen — no comparing notes with the lab across town before we submit."
- **Common misuse:** treating PT samples as "special" and handling them outside the routine workflow — doing so (referral testing, informal consultation) is a CLIA violation, not a quality-assurance best effort.

## Hemolysis / icterus / lipemia (H/I/L) index

- **Definition:** a semi-quantitative measure, usually generated automatically by the analyzer, of how much a specimen's hemolysis, bilirubin, or lipid content could interfere with a given assay's chemistry.
- **Practitioner usage:** "H-index is 150 on this tube — that's above the potassium interference cutoff, hold that analyte and request a clean re-draw."
- **Common misuse:** applying one H/I/L judgment to an entire panel, when interference thresholds are analyte-specific — a hemolyzed specimen can invalidate potassium while leaving glucose unaffected.

## Levey-Jennings chart

- **Definition:** a run-chart of control results over time plotted against the established mean and ±1/2/3 SD lines, used to see drift and shifts a single run's pass/fail status hides.
- **Practitioner usage:** "Pass/fail looks fine today, but the Levey-Jennings shows Level 2 creeping toward +1SD for the last five days — that's a 4_1s building, not nothing."
- **Common misuse:** only checking whether today's control is in range, without looking at the trend — a slow systematic drift is invisible one run at a time and obvious over ten.

## Autoverification

- **Definition:** LIS/middleware logic that releases a result automatically when it passes a defined set of checks (QC status, delta check, critical/reference range, specimen integrity flags) without a human review step.
- **Practitioner usage:** "This result didn't autoverify because it delta-checked — it's sitting in the review queue, not released."
- **Common misuse:** assuming autoverification means "no quality check happened" — properly configured, it's enforcing the same gates a human would, just faster; the risk is in poorly configured rules, not the concept itself.

## Reference interval vs. clinical decision limit

- **Definition:** the reference interval describes the range seen in a defined healthy population (commonly the central 95%); a clinical decision limit is a value chosen because it's the point where clinical action changes, and the two numbers frequently differ.
- **Practitioner usage:** "The reference interval for troponin doesn't matter here — the decision limit for ruling in a myocardial infarction is a specific assay-validated cutoff, not the top of 'normal.'"
- **Common misuse:** treating "within reference range" as synonymous with "clinically fine" — some decision limits sit inside the reference interval, and some clinically urgent thresholds are defined independently of it.

## Reflex testing

- **Definition:** a pre-authorized rule that automatically orders a follow-up test when an initial result meets a defined condition (e.g., an abnormal TSH automatically reflexes to free T4).
- **Practitioner usage:** "TSH reflexed to free T4 per the standing order — no need to call the provider for authorization."
- **Common misuse:** assuming reflex testing is the technologist's own judgment call in the moment — it's a pre-approved algorithm, and testing outside that algorithm without authorization is an unauthorized add-on, not initiative.

## Turnaround time (TAT)

- **Definition:** the elapsed time from a defined start point (order, collection, or receipt — specify which) to result availability, benchmarked against published targets (e.g., CAP Q-Probes) for STAT vs. routine tests.
- **Practitioner usage:** "Our STAT potassium TAT is measured collection-to-result, and it's tracking 8 minutes over the Q-Probes benchmark — that's a transport problem, not an analyzer problem."
- **Common misuse:** comparing TAT numbers across labs or reports without confirming they use the same start point — receipt-to-result and order-to-result for the same test can differ by 20+ minutes and aren't the same metric.
