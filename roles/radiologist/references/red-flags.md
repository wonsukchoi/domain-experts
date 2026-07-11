# Radiologist — red flags

### RADPEER discrepancy score (2b/3/4 combined) above 10% in a quarterly section review
- **Usually means:** a volume- or fatigue-driven perceptual pattern concentrated in one study type or time of shift, less often a genuine knowledge gap.
- **First question:** which modality, body area, or shift (overnight vs. daytime) do the discrepancies cluster in?
- **Data to pull:** quarterly RADPEER report broken out by modality, section, and reading shift.

### STAT/ED report turnaround time consistently exceeding 60-90 minutes
- **Usually means:** worklist prioritization misconfigured (STAT studies not flagged ahead of routine), or staffing below the volume the shift is scheduled for.
- **First question:** is the triage flag being set correctly at order entry, or is it a downstream reading-queue problem?
- **Data to pull:** RIS turnaround-time report segmented by priority level (STAT/urgent/routine).

### Critical-finding communication documented without a read-back timestamp
- **Usually means:** the finding was called in and left as a message, or the addendum was written after the fact without capturing an actual confirmed closed loop.
- **First question:** did the recipient repeat the finding and plan back, or is "communicated" standing in for "attempted"?
- **Data to pull:** critical-results log cross-referenced against the report addendum timestamp.

### "Clinical correlation recommended" or "follow-up as clinically indicated" appearing in more than a small fraction of a radiologist's reports
- **Usually means:** a defensive hedging habit substituting for a specific recommendation, shifting the follow-up decision onto a clinician with less imaging context.
- **First question:** for a sampled report, can the radiologist name the specific correlation or follow-up they actually intended?
- **Data to pull:** text-mined sample of reports containing the phrase, reviewed against what a specific recommendation would have said.

### Pulmonary nodule follow-up recommendation not tied to a named guideline
- **Usually means:** personal risk tolerance substituting for a validated threshold, producing inconsistent management across similar patients.
- **First question:** what size, morphology, and risk factors actually drove this specific interval?
- **Data to pull:** sampled reports with nodule size/risk factors checked against the Fleischner or Lung-RADS table.

### BI-RADS category assigned without a corresponding management statement
- **Usually means:** the lexicon category and the management pathway it implies (short-interval follow-up for 3, biopsy for 4/5) got decoupled — often a template field left unedited.
- **First question:** does the described morphology actually match the assigned category's published descriptors?
- **Data to pull:** BI-RADS audit sample cross-checked against the ACR Atlas category definitions.

### Contrast reaction rate above the institution's expected baseline for the contrast class in use
- **Usually means:** a premedication protocol not followed for a known prior reactor, or the allergy/renal screening question skipped at check-in.
- **First question:** was pre-contrast screening completed and documented for every case in the flagged period?
- **Data to pull:** contrast-reaction log cross-referenced with documented premedication status.

### Paired double-read agreement below 90% on screening mammography audits
- **Usually means:** calibration drift between readers or inconsistent application of the BI-RADS lexicon rather than genuinely ambiguous cases.
- **First question:** which BI-RADS category is generating most of the disagreement — 0 vs. 1, or 3 vs. 4A?
- **Data to pull:** paired-reading comparison log with category-level breakdown.

### CTDIvol or DLP trending above the institution's diagnostic reference level for a protocol
- **Usually means:** an outdated protocol not adjusted for patient size, or an adult default protocol applied to a smaller or pediatric patient.
- **First question:** was a size-specific dose estimate used, and does the protocol match the patient's habitus?
- **Data to pull:** dose-monitoring software report (e.g., an institutional dose registry) by protocol and patient size bracket.

### Missed secondary finding pattern on multi-region trauma studies after the primary injury was identified
- **Usually means:** a single-pass read that stopped once the first injury was found — classic satisfaction of search.
- **First question:** was a deliberate second pass of the full field of view performed and documented after the primary finding?
- **Data to pull:** peer-review case log filtered for trauma studies with a missed secondary finding.

### Resident/trainee preliminary read discordant with the final attending read above 5-10% on overnight coverage
- **Usually means:** a supervision or attestation gap on complex overnight cases, or a genuine case-mix complexity the coverage model wasn't built for.
- **First question:** which study types or subspecialties account for most of the discordance?
- **Data to pull:** resident-attending discrepancy log by study type and time of night.

### Routine outpatient report turnaround exceeding 24-48 hours as a sustained pattern
- **Usually means:** volume exceeding staffed reading capacity, or a worklist queue misprioritizing routine studies behind lower-value work.
- **First question:** is the backlog concentrated in one modality or subspecialty queue, or spread evenly?
- **Data to pull:** RIS backlog report segmented by subspecialty queue and referring department.
