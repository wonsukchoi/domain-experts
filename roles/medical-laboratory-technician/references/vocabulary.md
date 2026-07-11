# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Westgard rules (multirule QC)

- **Definition:** a set of statistical rules (1-3s, 2-2s, R-4s, 4-1s, 10x, etc.) applied to control results across two levels to distinguish random from systematic analytic error, each with different sensitivity to each error type.
- **In use:** "That's a 2-2s, not a 1-3s — both levels drifted the same direction, so I'm suspecting the calibrator, not a random blip."
- **Common misuse:** treating any single control outside ±2 SD (1-2s) as an automatic run rejection. 1-2s is a warning rule meant to trigger a check of the other rules, not a reject-on-its-own trigger — over-applying it causes needless reruns and burns reagent and turnaround time.

## Delta check

- **Definition:** a comparison of a patient's current result against their own prior result for the same analyte, flagged when the change exceeds a lab-defined limit, independent of whether either value falls inside the reference range.
- **In use:** "Reference range is fine, but that's a 3.5 delta on potassium against a 1.5 limit — I'm holding it for repeat before it goes out."
- **Common misuse:** assuming a result inside the reference range needs no further scrutiny. Reference range and delta check answer different questions — a "normal" value can still represent a dangerous or spurious jump from the patient's own baseline.

## HIL index (hemolysis / icterus / lipemia)

- **Definition:** a semi-quantitative index reported by chemistry analyzers estimating free hemoglobin, bilirubin, or lipid content in a specimen, used to flag likely interference with specific analytes.
- **In use:** "H-index is 300 — that's well past the potassium interference cutoff of 50 for this method, so I'm not reporting it as drawn."
- **Common misuse:** applying one hemolysis cutoff to every analyte on the order. Interference thresholds are analyte-specific — hemolysis biases potassium and LDH heavily but barely touches sodium or chloride.

## Critical (panic) value

- **Definition:** a result so far outside normal limits that it represents an immediate threat to patient safety, requiring verbal notification to the ordering clinician within a defined time window, independent of and in addition to the routine report.
- **In use:** "That's a critical potassium — I'm calling it in now, not waiting for the batch to finalize."
- **Common misuse:** treating the callback as complete once the value is verbally reported. The obligation includes documented read-back and the name/time of the recipient — an undocumented call doesn't satisfy the policy even if it happened.

## Autoverification

- **Definition:** LIS logic that releases a result automatically when it passes a defined set of rules (QC status, delta check, critical-value thresholds, instrument flags) without a technologist manually reviewing it first.
- **In use:** "This potassium autoverified because it passed delta check and wasn't flagged for hemolysis — if the H-index rule wasn't configured for this analyte, that's a gap, not a pass."
- **Common misuse:** assuming autoverification is a comprehensive check. It only enforces the rules it was explicitly configured with — a missing or misconfigured rule (e.g., no HIL gate on a hemolysis-sensitive analyte) lets bad results through silently.

## Wrong blood in tube (WBIT)

- **Definition:** a specimen collected from, or mislabeled as, a different patient than intended — a collection-identity error, distinct from an analytic or typing error.
- **In use:** "Type doesn't match history and there's no prior confirmatory draw — that's a WBIT risk, not a rare biological discrepancy. Redraw before we go further."
- **Common misuse:** attempting to resolve a type discrepancy by rerunning the same tube. Rerunning can only confirm what's in the tube — it cannot rule out that the tube itself was drawn from, or labeled for, the wrong person.

## Linearity / analytical measurement range (AMR)

- **Definition:** the range of analyte concentrations over which the method has been validated to report a proportional, accurate result without dilution; results outside it require verification (dilution and re-assay) before reporting.
- **In use:** "That glucose read >600 and out of AMR — I need to dilute and rerun before this number means anything."
- **Common misuse:** reporting an analyzer's raw "greater than" flag as if it were a precise, reportable value. Above the AMR the relationship between signal and concentration is no longer validated as linear; the number needs dilution confirmation, not a footnote.

## Calibration verification

- **Definition:** periodic testing (per CLIA, at minimum every 6 months or after specific triggering events) confirming that a method's reportable range and accuracy across it remain valid, distinct from daily QC which only checks two or three points on the curve.
- **In use:** "Daily QC passing doesn't substitute for calibration verification — we're due, and a reagent lot change is a trigger event on its own."
- **Common misuse:** treating in-control daily QC as proof the whole reportable range is accurate. QC controls typically sit at only two or three concentrations; calibration verification is what validates the curve across its full range.

## Proficiency testing (PT)

- **Definition:** an external, regulatory-required program (CLIA-mandated for regulated analytes) where a lab tests blinded samples of known value from an outside agency and its results are graded against peer labs, distinct from internal QC.
- **In use:** "PT samples get handled exactly like patient samples — no special handling, or it's a CLIA violation, not just bad practice."
- **Common misuse:** giving PT samples special attention or a second look that a routine patient specimen wouldn't get. That defeats the purpose of PT (verifying real-world performance) and is a specific, cited CLIA violation (PT referral/alteration).

## Moderate complexity vs. waived testing

- **Definition:** CLIA (42 CFR 493) categories describing the regulatory oversight, personnel qualification, and QC requirements attached to a given test — waived tests have minimal oversight (rapid strep, glucose meters); moderate/high complexity require documented personnel competency, more extensive QC, and proficiency testing.
- **In use:** "This assay is moderate complexity — I need my competency assessment on file before I can run it independently, not just a one-time training sign-off."
- **Common misuse:** assuming "the test is simple to perform" and "the test is CLIA-waived" are the same claim. Complexity categorization is a regulatory classification with real documentation requirements, not a statement about how hard the pipetting is.

## Turnaround time (TAT)

- **Definition:** the elapsed time from specimen receipt (or collection) to result verification, tracked against facility- and test-specific targets (e.g., STAT chemistry in under 60 minutes).
- **In use:** "TAT on this STAT potassium is already at 45 minutes because of the hemolysis recollect — that's a documented delay reason, not a missed target."
- **Common misuse:** treating TAT as the primary metric to protect, ahead of analytic correctness. A fast, wrong critical value costs more downstream than a delayed, correct one — TAT pressure is a constraint to manage, not a rule that overrides a QC or delta-check hold.

## Reflex testing

- **Definition:** a pre-approved rule that automatically orders an additional test based on the result of the first (e.g., a reflex to free T4 when TSH is abnormal), executed without a new clinician order.
- **In use:** "TSH came back at 0.05 — that's within our reflex criteria, so free T4 is already queued, no need to call the provider for an add-on order."
- **Common misuse:** confusing reflex testing (protocol-driven, pre-approved) with a technologist unilaterally deciding to add a test they think is clinically indicated. Only tests on the approved reflex list can be added without a new order; anything else requires contacting the ordering provider.
