# Red Flags

### FREEMIX (contamination estimate) > 0.03-0.05 depending on assay
- **Usually means:** Index hopping between samples on a shared flow cell, or physical sample/reagent cross-contamination during library prep.
- **First question:** Are the elevated-FREEMIX samples adjacent in the index-pooling plan or the plate layout?
- **Data to pull:** Index-hopping rate for the run, plate map, and FREEMIX values for every sample in the same pool (not just the flagged one).

### %bases at 20x more than 5 points below the assay's historical median, with mean coverage passing
- **Usually means:** Capture/hybridization inefficiency tied to a specific reagent lot, not a loading problem (which would drop the mean too).
- **First question:** Do the failing samples share a capture-kit lot, prep batch, or reagent lot?
- **Data to pull:** MultiQC per-sample uniformity table grouped by lot/batch metadata from the LIMS.

### Ti/Tv ratio outside 2.0-2.1 (exome/genome) with everything else passing
- **Usually means:** Wrong reference build, variant-caller misconfiguration, or a pipeline-version mismatch against the validated baseline.
- **First question:** What reference build and pipeline/caller version ran on this sample versus the validation cohort?
- **Data to pull:** Pipeline run log / version manifest for the sample.

### Duplication rate > 15% (exome) or > 30% (RNA-seq, protocol-dependent)
- **Usually means:** Low input DNA/RNA mass forcing extra PCR cycles, or a library-complexity problem upstream.
- **First question:** What was the input mass and PCR cycle count for this library versus protocol spec?
- **Data to pull:** Library-prep worksheet (input ng, cycle count) from the LIMS.

### Run-wide Q30 < 80% or cluster PF% < 80%
- **Usually means:** Flow-cell defect, instrument fault, or reagent-kit expiry/storage problem affecting the whole run, not any individual sample.
- **First question:** Has this instrument or reagent lot had a prior flagged run in the last 30 days?
- **Data to pull:** Instrument QC/maintenance log and reagent lot history.

### Two or more samples failing the same metric and sharing an index pool, plate row, or reagent lot
- **Usually means:** A shared upstream cause (pooling, pipetting, reagent) rather than three independent sample-level failures.
- **First question:** What do the failing samples have in common that the passing samples in the same run don't?
- **Data to pull:** Full-run metadata table (index pool, lot numbers, plate position) cross-joined against the QC metric table.

### Coverage or QC metrics compared against a threshold set before a reference-build, aligner, or caller version change
- **Usually means:** The threshold itself is stale — the comparison, not the sample, is invalid.
- **First question:** When was this assay's QC threshold last re-validated against the current pipeline version?
- **Data to pull:** Assay validation record / revalidation log.

### Insert-size distribution bimodal or median far outside the library-prep protocol's target range
- **Usually means:** Adapter dimer contamination or size-selection failure during library prep.
- **First question:** Does the bimodal peak match the known adapter-dimer size (~120bp)?
- **Data to pull:** Picard CollectInsertSizeMetrics histogram for the sample.

### Clinical turnaround-time deadline reached with an unresolved QC flag
- **Usually means:** Pressure to release with a caveat instead of stopping the line — the single highest-risk moment in a clinical workflow.
- **First question:** Is this flag one this lab's validated protocol allows to be caveated, or does it require rejection?
- **Data to pull:** The assay's written QC-exception policy, not verbal precedent.
