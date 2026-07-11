# Red flags — pathology quality and case-level signals

### Frozen section-to-permanent discordance rate >2% for one pathologist over a quarter
- **Usually means:** sampling/technical artifact clustering in one specimen type, or that individual's diagnostic threshold is miscalibrated for a specific entity — less often a broad competence problem.
- **First question:** are the discordances concentrated in a single diagnosis or specimen type, or scattered across many unrelated case types?
- **Data to pull:** departmental frozen-permanent correlation log for the quarter, benchmarked against the CAP Q-Probes major-discordance rate of roughly 1-2%.

### Amended report rate >0.5% of accessioned cases in a month
- **Usually means:** a clerical/demographic error cluster (specimen or patient mislabeling) rather than diagnostic error — clerical amendments outnumber diagnostic ones in most CAP Q-Probes data.
- **First question:** what fraction of the amendments are clerical (labeling, demographics) versus diagnostic (changed interpretation)?
- **Data to pull:** amendment log with root-cause category tagged per CAP Q-Probes classification, not a single undifferentiated count.

### Turnaround time for a routine surgical specimen exceeds 3 business days with no decalcification, consult, or special-stain flag
- **Usually means:** grossing or sign-out queue backlog rather than a case-specific complexity issue.
- **First question:** is the delay pre-analytic (grossing backlog), analytic (stain reruns, IHC turnaround), or post-analytic (sitting in the sign-out queue)?
- **Data to pull:** LIS turnaround-time report broken out by phase (accession-to-gross, gross-to-stain, stain-to-sign-out).

### Margin recorded as "close" without a measured distance in millimeters
- **Usually means:** the gross exam skipped systematic inking/measurement, or the dictation shortcut ("close") substituted for an actual number.
- **First question:** was the margin actually inked and measured with an ocular micrometer, or is "close" an unaided visual estimate?
- **Data to pull:** original gross-description cassette map; re-review the slide with a calibrated ocular scale if the number is missing.

### Biopsy diagnosis benign but referring imaging is BI-RADS 4C or 5 (or an equivalent high-suspicion category)
- **Usually means:** a sampling miss — the needle didn't reach the actual target — more often than a true negative on a genuinely benign lesion.
- **First question:** does an imaging-pathology concordance review confirm the biopsy clip/needle track actually intersected the suspicious lesion?
- **Data to pull:** stereotactic/ultrasound biopsy images showing clip placement relative to the lesion, presented at the concordance conference.

### An immunohistochemistry panel returns all markers positive or all markers negative on a diagnostically difficult case
- **Usually means:** a technical failure (antigen retrieval, reagent lot, or control tissue not run correctly on that batch) rather than a genuine biological finding.
- **First question:** did the positive and negative control tissue on the same run stain as expected?
- **Data to pull:** the IHC run's control log for that specific batch and reagent lot.

### Outside subspecialty consult disagreement rate trending up over a quarter
- **Usually means:** a shift in case mix toward an organ system the group under-covers, or drift in one pathologist's threshold on a specific entity — rarely a uniform quality collapse.
- **First question:** is the disagreement concentrated in one organ system, one entity, or one signing pathologist's cases?
- **Data to pull:** consult log tagged by organ system and by the original signing pathologist.

### Gleason score/Grade Group reported with no percentage of pattern 4 noted on a biopsy with mixed architecture
- **Usually means:** incomplete synoptic dictation rather than a wrong grade — but the missing percentage is itself clinically consequential (it affects active-surveillance eligibility).
- **First question:** what percentage of pattern 4 was actually present on re-review of the original slide?
- **Data to pull:** original H&E slide with pattern-4 percentage explicitly quantified on re-read.

### Specimen accessioned with no clinical history or imaging reference in the requisition
- **Usually means:** the ordering clinician skipped the history field, or an EHR-to-LIS interface failure dropped it, not that history was truly unavailable.
- **First question:** can the correlating clinical note or imaging report be pulled from the EHR before grossing begins?
- **Data to pull:** the EHR chart entry (imaging report, clinic note) tied to the accession number.

### Frozen section deferred to permanent on more than 10% of a specific specimen type
- **Usually means:** the entity is inherently difficult to call intraoperatively (expected for entities like follicular thyroid lesions) rather than a performance issue — but it needs benchmarking, not assumption.
- **First question:** does the deferral rate for that specimen type match published literature benchmarks for the same entity?
- **Data to pull:** departmental deferral log stratified by specimen type, compared against published frozen-section performance studies for that entity.

### Pathology T-category and imaging T-category disagree at tumor board
- **Usually means:** fixed-tissue shrinkage (commonly 10-20% relative to fresh or in-vivo imaging size) rather than a genuinely missed extent of disease.
- **First question:** was the reported gross size measured on fresh or on fixed tissue, and does that explain the size gap versus imaging?
- **Data to pull:** the gross-exam worksheet noting both fresh and post-fixation dimensions.

### One pathologist's benign-diagnosis rate on a specific specimen type is a statistical outlier versus departmental peers
- **Usually means:** either under-calling malignancy (a miss-risk pattern worth reviewing) or a genuinely different referral case mix — both are plausible and need to be distinguished, not assumed.
- **First question:** does a blinded peer re-review of a sample of that pathologist's benign calls on that specimen type reproduce the same diagnosis?
- **Data to pull:** the departmental peer-review/QA sampling log for that pathologist and specimen type.
