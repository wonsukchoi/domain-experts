# Red Flags

Smell tests for QC, specimen, and result-review problems. Format per flag: usual cause, the first question a veteran asks, the data to pull.

### QC in control but a single result looks physiologically implausible

- **Usually means:** an interferent (hemolysis, lipemia, icterus) or a sample mix-up on that specific tube — passing QC only certifies the analyzer's behavior on controls, not this specimen.
- **First question:** "What's the HIL index on this tube, and does it match the patient's history?"
- **Data to pull:** HIL indices for this run, the patient's delta-check history, and the accession log for adjacent specimens processed in the same batch.

### Westgard 2-2s across both control levels in the same run

- **Usually means:** a systematic error — calibration drift, a new reagent lot, or a degrading control material — not a one-off random blip.
- **First question:** "Did anything change today — reagent lot, calibrator lot, or a recent maintenance event?"
- **Data to pull:** reagent/calibrator lot change log, maintenance log, and the Levey-Jennings trend for the prior 5–10 runs on both levels.

### Delta check trips but the tech is tempted to release anyway because "the number looks fine"

- **Usually means:** the current value is inside the reference range but still represents an implausible jump from the patient's own baseline — reference range and delta check answer different questions.
- **First question:** "Is there a documented clinical event (dialysis, transfusion, acute bleed) that explains this specific magnitude of change?"
- **Data to pull:** patient's prior 2–3 results for the same analyte, and the clinical order/notes for the current draw.

### H-index elevated but the ordered panel includes sodium and glucose only

- **Usually means:** hemolysis is present but the specific analytes ordered aren't hemolysis-sensitive — a blanket "reject all hemolyzed specimens" policy wastes a redraw the patient doesn't need.
- **First question:** "Which analytes on this specific order are actually hemolysis-sensitive per the package insert?"
- **Data to pull:** the method's interference table for each ordered analyte, not a generic hemolysis cutoff.

### Blood bank type doesn't match the patient's historical record

- **Usually means:** wrong blood in tube (WBIT) — a specimen drawn from, or labeled for, the wrong patient — far more often than a genuine and previously undocumented type discrepancy.
- **First question:** "Was this patient's blood type ever confirmed on a second, independently drawn specimen?"
- **Data to pull:** collection time and collector ID on both the current and historical specimens; whether a second draw has ever been performed for this patient.

### Automated differential flags "atypical lymphocytes" or immature cells

- **Usually means:** either a genuine hematologic process (infection, leukemia, reactive lymphocytosis) or an analyzer misclassification — the analyzer cannot distinguish reliably at the cell level the way a trained eye can.
- **First question:** "Does this result meet any ISLH manual-review criterion, and has a 100-cell manual differential been done?"
- **Data to pull:** the flagged parameters, prior CBC results for this patient, and whether a manual differential has already been performed on this specimen.

### Antimicrobial susceptibility result is phenotypically implausible

- **Usually means:** either a genuine and reportable resistance mechanism, or a testing/identification error — implausible phenotype-genotype combinations are rare enough to warrant a second look before reporting.
- **First question:** "Does this susceptibility pattern match the expected phenotype for this organism per CLSI M100's tables?"
- **Data to pull:** the organism ID confirmation, the specific antimicrobial/organism combination flagged, and whether confirmatory testing (e.g., repeat identification, molecular confirmation) has been run.

### Critical value called in but no read-back documented

- **Usually means:** the callback was rushed under turnaround-time pressure and the compliance step was skipped — a correct value with no read-back record is functionally undocumented for audit and legal purposes.
- **First question:** "Who took the call, and is their name and the read-back confirmation logged?"
- **Data to pull:** the critical-value log entry for time, recipient name/title, and read-back confirmation field.

### Specimen sat at room temperature well past its analyte's stability window

- **Usually means:** a transport delay is about to produce a falsely low glucose (glycolysis) or falsely elevated potassium (cellular leakage), independent of any analytic error.
- **First question:** "What time was this drawn, and what time did it reach the analyzer?"
- **Data to pull:** collection timestamp vs. receipt timestamp in the LIS, and the analyte-specific stability data for the tube type used.

### A single technologist's results show a cluster of unusual repeats or QC reruns

- **Usually means:** either a training gap on a specific method, or a personal shortcut (skipping the visual hemolysis check, rushing calibration verification) that hasn't yet caused a reportable error.
- **First question:** "Is this concentrated on one instrument, one shift, or one technologist?"
- **Data to pull:** QC rerun logs and repeat-testing logs broken out by technologist and instrument over the past 30 days.
