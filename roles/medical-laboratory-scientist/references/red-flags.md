# Red Flags

Smell tests for QC, specimen handling, and reporting failures at the bench. Format per flag: what it usually means, the first question to ask, the data to pull.

## QC violation "resolved" by a single rerun that passed

- **Usually means:** the root cause (reagent lot degrading, calibration drift, a failing reference electrode) was never identified — a pass on rerun without investigation is a coin flip, not a fix.
- **First question:** "What changed since the last in-control run — reagent lot, calibrator lot, maintenance, or electrode age?"
- **Data to pull:** Levey-Jennings trend for the prior 10–20 runs, reagent/calibrator lot log, maintenance and part-replacement log.

## A single analyte trending toward one QC limit over several days without triggering a hard rule

- **Usually means:** slow systematic drift (reagent aging, calibration verification overdue) building toward a 4_1s or eventual 1_3s violation that hasn't fired yet.
- **First question:** "Has calibration verification been run on schedule for this analyte, and when is the current reagent lot's expiration?"
- **Data to pull:** Levey-Jennings chart with a trend line, not just pass/fail flags; calibration verification due-date log.

## Critical value result-to-callback interval exceeds the policy window (commonly 30–60 minutes)

- **Usually means:** either the result sat unnoticed in the LIS queue, or the callback happened but wasn't documented in time — both are failures the accreditation record will catch.
- **First question:** "What time did the result finalize in the LIS, and what time was the call actually placed?"
- **Data to pull:** LIS result-finalization timestamp vs. callback log timestamp; staffing/workload at the time.

## Delta-check flag overridden by re-testing the same tube instead of requesting a re-draw

- **Usually means:** the technologist treated a possible specimen misidentification as an instrument problem — re-testing the same tube can rule out analyzer error but cannot catch a mislabeled draw.
- **First question:** "Was patient identity independently reconfirmed, or was the same tube just run again?"
- **Data to pull:** delta-check override documentation; whether a second identifier check or re-draw request is on record.

## Result released with a hemolysis/icterus/lipemia (H/I/L) index above the assay's published interference threshold, no disclaimer

- **Usually means:** the interference check was skipped under turnaround-time pressure, most commonly on potassium, LDH, or AST.
- **First question:** "What was the H/I/L index for this specimen, and is it above this specific analyte's threshold?"
- **Data to pull:** analyzer's interference index output for the specimen; the assay's published interference table.

## Turnaround time on a STAT critical analyte (e.g., troponin, potassium) consistently missing benchmark with no documented reason

- **Usually means:** a preanalytical bottleneck (transport delay, centrifugation backlog) or a chronic unresolved QC/interference issue on that instrument, not a one-off.
- **First question:** "Where in the specimen's timeline — collection, transport, centrifugation, queue, analysis — is the time actually going?"
- **Data to pull:** LIS specimen-tracking timestamps at each handoff, compared against the CAP Q-Probes benchmark for that test.

## Proficiency testing (PT) sample handled outside the routine specimen rotation

- **Usually means:** someone diverted a PT sample to a reference lab, consulted a colleague at another facility, or had a supervisor "double-check" it before submission — all are CLIA-prohibited testing referral.
- **First question:** "Was this PT sample logged, accessioned, and tested by the same staff and process as a routine patient specimen, with zero outside consultation?"
- **Data to pull:** PT sample chain-of-custody log; accession timestamp vs. arrival timestamp.

## Specimen rejection rate concentrated in one collecting unit or one phlebotomy team

- **Usually means:** a training or process gap upstream (wrong tube order, underfilled coagulation tubes, delayed transport from that unit) rather than random bad luck.
- **First question:** "Is the rejection reason code the same across most of these — clotting, hemolysis, mislabeling — and does it cluster by shift or by collector?"
- **Data to pull:** rejection-reason breakdown by collecting unit and by shift over 30 days.

## A "normal" result on a specimen that failed the acceptability gate, released anyway

- **Usually means:** the technologist reasoned backward from a plausible-looking number to "it must be fine," instead of forward from the specimen defect to a hold — a hemolyzed specimen with a normal-looking potassium is still not validated, since hemolysis pushes potassium up, not necessarily out of range.
- **First question:** "Was the acceptability gate (identity, tube, stability, H/I/L) actually cleared, or was the decision to release based on the number looking reasonable?"
- **Data to pull:** specimen acceptability checklist for that accession; H/I/L index regardless of whether the analyte flagged.

## Sigma-metric below 4 for a live assay still running the same QC schedule as a Sigma ≥5 assay

- **Usually means:** the QC program wasn't updated after the last method comparison or reagent-lot change revealed a higher bias — running a lean rule set on a marginal method under-detects real errors.
- **First question:** "When was Sigma last recalculated for this assay, and does the QC rule/N match the current tier?"
- **Data to pull:** most recent method-comparison bias study, current CV from cumulative QC data, CLIA/manufacturer TEa for the analyte.
