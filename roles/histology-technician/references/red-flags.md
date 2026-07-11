# Red flags

### Floater on an H&E slide that doesn't match the case's tissue type
- **Usually means:** Cross-contamination during grossing, embedding, or at the water bath from another case processed in the same batch/session; second most likely: microtome blade carryover from the previous block.
- **First question:** Does the floater's morphology and any inclusions match tissue from another block processed the same day at the same station?
- **Data to pull:** Gross log and block list for every case processed in the same run, water-bath cleaning log for that shift, blade-change log.

### IHC positive control weak or absent, patient tissue also negative
- **Usually means:** Antigen-retrieval or reagent failure invalidating the whole run, not a true patient-negative; second: expired or degraded antibody/reagent lot.
- **First question:** Did the control tissue show any staining anywhere on the slide, even patchy or weak?
- **Data to pull:** Reagent lot number and expiration, retrieval protocol (method, buffer, pH, time) used for that run, instrument maintenance/calibration log.

### Chatter or compression lines on sections at the standard microtome setting
- **Usually means:** Dull or nicked blade, or block face too warm/cold for the clearance angle in use; second: incorrect blade/clearance angle for the tissue type.
- **First question:** Does the artifact persist after a blade change and a fresh block face?
- **Data to pull:** Microtome maintenance and blade-change log, block/room temperature at time of cutting.

### Fixation time under 6 hours before processing on a hormone-receptor or HER2 case
- **Usually means:** Late-day/weekend specimen backlog outrunning the processor schedule; second: inadequate fixative volume relative to specimen size (diluted or insufficient ratio).
- **First question:** What time did the specimen actually enter formalin versus when processing began?
- **Data to pull:** Specimen accession timestamp, gross dictation, processor start log.

### Routine biopsy turnaround time exceeding 3 business days repeatedly
- **Usually means:** Processor or embedding/microtomy bottleneck from staffing gaps; second: batch scheduling concentrating cases at the slowest pipeline stage.
- **First question:** Which pipeline stage — accession, gross, process, embed, cut, stain, sign-out — is where the delay actually accumulates?
- **Data to pull:** LIS timestamps per pipeline stage for the affected cases over the trailing month.

### Decalcification "finished" by elapsed time with no chemical end-point test on a bone or marrow specimen
- **Usually means:** Over- or under-decalcified tissue depending on actual bone density, since clock-based decal doesn't account for case-to-case variation; second: wrong decal reagent chosen for a case with downstream IHC ordered.
- **First question:** Was a chemical end-point test (e.g., ammonium oxalate) run, or was the call made on elapsed time alone?
- **Data to pull:** Decalcification log (reagent, concentration, time in solution), any recorded end-point test result.

### Pale or washed-out H&E across an entire stain run, not one slide
- **Usually means:** Exhausted or degraded hematoxylin, or incorrect differentiation/bluing time; second: contaminated or diluted water-bath/rinse water affecting the whole batch.
- **First question:** When was the hematoxylin last changed, and how many slides have gone through it since?
- **Data to pull:** Stain-reagent change log, slide count since last reagent change, differentiation step timing for that run.

### Frozen-section/permanent-section discordance rate above roughly 2–3% for the month
- **Usually means:** Freezing artifact obscuring architecture or a sampling/orientation gap at the frozen level, not a true diagnostic disagreement; second: margin-call interpretation difference between frozen and permanent read.
- **First question:** Was the discordance technical (freeze artifact, missed area) or a genuine diagnostic difference on re-review?
- **Data to pull:** Monthly frozen/permanent correlation log, the specific blocks and levels in question.

### Cassette or slide label mismatch caught at any QC checkpoint
- **Usually means:** Batch-labeling error during a busy grossing or embedding session; second: barcode scanner misread accepted without a manual check.
- **First question:** How many other cases were in the same labeling batch as the mismatched one?
- **Data to pull:** Accession log for the batch window, barcode-scan audit trail.

### Antigen-retrieval time or pressure repeatedly increased to "fix" a weak stain
- **Usually means:** Masking an unaddressed upstream fixation-time or fixative-type problem rather than a retrieval-settings problem; second: wrong retrieval buffer specified for that particular antibody.
- **First question:** What actually changed between the last run where this antibody worked and this one?
- **Data to pull:** Antibody validation sheet's specified retrieval method, fixation log for the block in question.

### Water bath temperature outside roughly 10°C below the paraffin's melting point
- **Usually means:** Thermostat drift or an ambient-temperature change (HVAC, season) shifting the bath without anyone re-verifying it; second: wrong paraffin type loaded for the bath's set temperature.
- **First question:** When was the bath temperature last checked with an independent thermometer against the log?
- **Data to pull:** Water-bath temperature log, room-temperature log for the same period.

### QC log shows a control slide skipped or marked "N/A" on a run day
- **Usually means:** Production-volume pressure pushing a run out without the control; second: control tissue block genuinely exhausted with no replacement queued.
- **First question:** Was a control block physically available and simply not sectioned that day?
- **Data to pull:** Control-block inventory log, run log, staffing schedule for that shift.
