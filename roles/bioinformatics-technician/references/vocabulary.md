# Vocabulary

### FREEMIX
A contamination-estimate statistic from VerifyBamID2, estimating the fraction of reads originating from a genetically distinct source mixed into the sample.
**In use:** "FREEMIX came back at 0.041 on those three samples — that's above our 0.03 cutoff, I'm not calling variants off this until we know why."
**Common misuse:** Treating any nonzero FREEMIX as automatic failure — a small nonzero value is expected background noise; the number only matters relative to the assay's validated cutoff.

### Ti/Tv ratio (transition/transversion ratio)
The ratio of transition (purine-purine or pyrimidine-pyrimidine) to transversion substitutions among called variants, expected to fall in a narrow, biology-driven range.
**In use:** "Ti/Tv dropped to 1.6 on this batch — that's not biology, that's a caller or reference problem."
**Common misuse:** Assuming Ti/Tv is a hard biological constant rather than an assay- and species-dependent convention; panels with very few variants don't have enough calls for the ratio to be meaningful.

### PF% (percent passing filter)
The fraction of sequencing clusters on a flow cell that pass the instrument's built-in quality filter and get included in the base-call output.
**In use:** "PF was only 74% on this flow cell — that's a run-level problem, not something any one sample's QC will fix."
**Common misuse:** Confusing PF% (an instrument-level cluster-quality metric) with Q30 (a base-call-accuracy metric) — they measure different things and can move independently.

### Q30
The percentage of sequenced bases with a Phred quality score of 30 or higher (predicted base-call error rate <=0.1%).
**In use:** "Q30 is 88%, within spec — the run itself isn't the problem here."
**Common misuse:** Treating Q30 as a per-sample metric; it's typically reported and gated at the run/lane level.

### Duplication rate
The fraction of aligned reads flagged as PCR or optical duplicates — copies of the same original DNA fragment rather than independent sequencing events.
**In use:** "Duplication's at 22% on a library that should be under 15% — check the input mass, this smells like low-input over-amplification."
**Common misuse:** Assuming duplicates simply "waste" coverage proportionally; high duplication actually reduces effective unique coverage nonlinearly and can hide under a passing raw mean-coverage number.

### Uniformity (coverage uniformity)
How evenly sequencing depth is distributed across the target region, distinct from mean depth. Commonly reported as % of bases at or above a depth threshold (e.g. %>=20x).
**In use:** "Mean's 111x but only 79% of bases clear 20x — that's a uniformity failure, not a depth failure."
**Common misuse:** Reading a passing mean-coverage number as sufficient evidence of usable data without checking the uniformity metric separately.

### Index hopping
Misassignment of sequencing reads to the wrong sample's index/barcode during multiplexed sequencing, most common on patterned-flow-cell instruments.
**In use:** "Elevated FREEMIX across the whole pool, not just one sample — that pattern points to index hopping, not individual contamination."
**Common misuse:** Diagnosing every contamination flag as wet-lab pipetting error without first checking whether it's pool-wide (pointing to index hopping) or isolated to one sample (pointing to handling).

### Joint genotyping
The step in a germline variant-calling pipeline (e.g. GATK's GenotypeGVCFs) where variant calls across multiple samples are made jointly rather than independently, improving sensitivity for rare variants.
**In use:** "This cohort needs to be re-joint-genotyped as a batch — calling it sample-by-sample will miss low-frequency sites the joint model would catch."
**Common misuse:** Assuming per-sample (single-sample) calling and joint genotyping are interchangeable QC-wise; a sample re-run alone after joint calling is not directly comparable to its original joint-called output.

### CLIA / CAP
CLIA (Clinical Laboratory Improvement Amendments, 42 CFR 493) is the US federal regulatory framework for clinical lab testing; CAP (College of American Pathologists) accreditation layers additional checklist requirements, including molecular-pathology-specific QC documentation.
**In use:** "This is a CLIA-regulated run — an unresolved QC flag doesn't get a caveat in the report, it gets a deviation filed and the sample held."
**Common misuse:** Treating CLIA/CAP requirements as generic "quality" language rather than as a specific obligation to document and act on QC exceptions before release.

### Deviation report
A formal documented record, required under a clinical lab's quality management system, when a process or result falls outside validated parameters.
**In use:** "Filing DR-2026-041 for the capture-kit lot — three samples affected, lot quarantined pending vendor response."
**Common misuse:** Treating a deviation report as paperwork overhead rather than the mechanism that prevents the same reagent-lot problem from silently recurring on the next run.
