# Red flags

### AFIS/NGI top-ranked candidate reported as a "match" before full ACE-V comparison
- **Usually means:** an examiner or a supervisor is treating the algorithm's similarity score as a finding under case-clearance time pressure.
- **First question:** "Was a full manual comparison completed and documented, or are we citing the candidate rank alone?"
- **Data to pull:** the AFIS/NGI search transaction log and the comparison worksheet (or its absence) for the case.

### Identification verified by a second examiner who already knew the first examiner's conclusion
- **Usually means:** "verification" is being run as a same-desk agreement check, not an independent blind re-examination — common where staffing is thin.
- **First question:** "Was the second examiner given the candidate list and latent only, or also the first examiner's call and case context?"
- **Data to pull:** the verification log's documented methodology field, and whether it distinguishes blind re-examination from conclusion review.

### NCIC want/warrant entry past its validation due date with no originating-agency confirmation
- **Usually means:** the validation notice was filed as routine paperwork rather than escalated as a deadline, and the entry is at risk of automatic purge.
- **First question:** "Has the originating detective or unit been contacted directly, or is this sitting in a queue?"
- **Data to pull:** the validation tracking log's due-date and confirmation-status fields for the entry.

### Criminal history record released to a licensing/employment requester without a cited statutory basis
- **Usually means:** the requester was treated as automatically entitled because they're "official," without classifying their specific authorized scope.
- **First question:** "What statute or regulation authorizes this requester's category to receive this specific scope of record?"
- **Data to pull:** the disclosure log's authority field and the requester's stated purpose on file.

### Sealed or expunged case surfaces in a routine background search response
- **Usually means:** the sealing/expungement order updated the court record but the flag never propagated to the CHRI repository, or the search tool doesn't check seal status before returning results.
- **First question:** "Did the disclosure check the seal/expungement flag before this record left the building, or after?"
- **Data to pull:** the court order date, the repository's flag-update timestamp, and whether the flag predates the disclosure.

### Ten-print card or Live Scan submission repeatedly rejected for quality by AFIS/NGI
- **Usually means:** a capture-technique problem at booking (pressure, rolling technique, sensor calibration) rather than a one-off bad print.
- **First question:** "Is this one submission or a pattern from one booking station or one officer?"
- **Data to pull:** the AFIS/NGI rejection log filtered by capture station and by booking officer over the last 30–60 days.

### One examiner's inconclusive rate is far higher or lower than peers on comparable latent quality
- **Usually means:** either overly conservative calling (missing real identifications) or overly liberal calling (risking a Mayfield-type false positive) — not necessarily wrongdoing, but a calibration issue worth checking.
- **First question:** "Is this examiner working a harder subset of cases, or is the calling standard actually different?"
- **Data to pull:** a sample of the examiner's inconclusive and identification worksheets, blind-reviewed by a peer.

### Fingerprint classification or biometric identifier on a new ten-print card conflicts with the existing master record under that name
- **Usually means:** an alias, an identity-fraud attempt, or a data-entry error at a prior booking — needs resolution before the new booking record merges with the old one.
- **First question:** "Does the discrepancy resolve to the same person under a different name, or two different people sharing a name?"
- **Data to pull:** side-by-side ten-print comparison and the master record's booking photo history.

### Subpoena or court order for a sealed record lacks a specific statutory citation
- **Usually means:** the requesting party or their counsel assumed a general subpoena overrides a sealing statute, which is frequently not true without the specific carve-out cited.
- **First question:** "Does this order cite the statute or case exception that permits access to a sealed record, or just compel production generally?"
- **Data to pull:** the order's text and the state's sealing statute's enumerated exceptions.

### CJIS Security Policy audit finds shared login credentials or a gap in the CHRI access audit trail
- **Usually means:** operational convenience (shared terminal, shift handoff) has quietly overridden the individual-accountability requirement the audit trail depends on.
- **First question:** "Can every CHRI query in the last audit period be attributed to one named, authenticated user?"
- **Data to pull:** the system's access log against the current list of individually issued credentials.

### Records disclosure log shows a release with no logged requester purpose
- **Usually means:** an informal request (a phone call, a "professional courtesy") bypassed the intake process that normally captures the statutory basis.
- **First question:** "Who requested this, in what format, and under what stated purpose — and why isn't that in the log?"
- **Data to pull:** the disclosure log entry and any corroborating correspondence or call record.

### A latent comparison identification is based on fewer corresponding minutiae than the agency's own documented sufficiency policy
- **Usually means:** time pressure or case-severity pressure pushed a borderline print past "inconclusive" into "identification."
- **First question:** "Does the worksheet show the corroborating ridge-count or pore detail this call requires, or just the minutiae count?"
- **Data to pull:** the comparison worksheet against the agency's written sufficiency policy.
