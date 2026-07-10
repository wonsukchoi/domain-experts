# Red Flags

Smell tests for QC investigations, trend data, and lab records. Format per flag: what it usually means, the first question to ask, the data to pull.

### Third retest run on the same sample with no documented root cause

- **Usually means:** testing into compliance — the analyst is rerunning until a passing number appears rather than investigating why the first one failed. This is a top FDA-483/warning-letter citation category.
- **First question:** "What SOP authorized this specific retest, and what root cause was documented before it was run?"
- **Data to pull:** the OOS investigation record and its timestamp versus the retest timestamp — if the retest predates a documented root cause, the investigation was backfilled.

### OOS closed as "no root cause found, retest passed, release"

- **Usually means:** Phase I investigation stalled without escalating to Phase II — the easy close was taken instead of the correct one.
- **First question:** "Was Phase II opened, and if not, on what basis was the original result ruled a lab error rather than a product issue?"
- **Data to pull:** the Phase I closure memo and whether it names a specific assignable cause versus stating "inconclusive."

### Cpk or Ppk reported from fewer than ~30 individual results

- **Usually means:** a capability number that looks decision-grade but has a wide, unreported confidence interval — small-sample Cpk swings dramatically lot to lot.
- **First question:** "How many individual data points and how many subgroups is this Cpk built on?"
- **Data to pull:** the raw dataset and subgroup count behind the reported Cpk/Ppk.

### Batch record correction with no initials, date, or reason

- **Usually means:** a data-integrity (ALCOA+) gap — the record was altered without an auditable trail of who, when, and why.
- **First question:** "Who made this correction, when, and is there a documented reason in the record itself?"
- **Data to pull:** the audit trail for that record (paper: single-line-through correction with initials/date; electronic: system audit log).

### Control chart shows 7+ consecutive points on one side of centerline, all technically in spec

- **Usually means:** a real process shift that spec-checking alone would miss entirely — the process mean has moved even though nothing has failed yet.
- **First question:** "What changed around the point where the run of points started — reagent lot, calibration, raw-material lot, analyst, season?"
- **Data to pull:** the control chart with annotated change points; calibration and reagent-lot logs for the same window.

### Reference standard or CRM used past its assigned expiry or requalification date

- **Usually means:** every result generated against that standard since expiry is suspect, not just the flagged one — this can retroactively invalidate a batch of released lots.
- **First question:** "What is the full list of results generated against this standard lot since its expiry date?"
- **Data to pull:** the reference-standard inventory log and every test record citing that standard lot number.

### Analyst overrides their own OOT flag without a documented rationale

- **Usually means:** schedule pressure overriding a real signal — the system caught something and a person suppressed it.
- **First question:** "What is the written justification for overriding the flag, and who approved it?"
- **Data to pull:** the OOT alert log and the corresponding sign-off/deviation record, if one exists.

### Specification tightened immediately after a near-miss, with no formal change control

- **Usually means:** the spec is being adjusted to make a problem disappear on paper rather than fixing the process — a classic move-the-goalposts pattern.
- **First question:** "What change-control record authorizes this spec revision, and what data supports the new limit?"
- **Data to pull:** the change-control record and the validation/stability data justifying the new limit.

### Audit trail disabled, or logged as "not reviewed," on electronic lab data

- **Usually means:** a 21 CFR Part 11 / data-integrity gap — nobody can confirm the electronic record wasn't altered after generation.
- **First question:** "Is the audit trail function enabled system-wide, and is audit-trail review part of the result-approval workflow?"
- **Data to pull:** system configuration settings and the approval workflow's audit-trail-review checkpoint.

### Stability pull-point missing or logged late

- **Usually means:** either a scheduling failure that breaks the ICH stability commitment for that lot, or a sample that was pulled on time but tested late — both undermine the shelf-life claim built on that data.
- **First question:** "Was the sample pulled on the scheduled date, and if so, why is the test date more than a few days later?"
- **Data to pull:** the stability chamber pull log versus the LIMS test-initiation timestamp.

### Deviation or CAPA open more than 30–45 days with no interim containment action

- **Usually means:** the investigation has stalled and product is continuing to be released against an unresolved quality question.
- **First question:** "What interim containment is in place while this stays open, and what's blocking closure?"
- **Data to pull:** the deviation/CAPA tracker with open-date, target-close-date, and any containment actions logged.

### System-suitability check skipped or run after the sample sequence instead of before

- **Usually means:** results were generated on an unverified system — the entire sequence's validity is now retroactive and unproven.
- **First question:** "Where in the sequence log does system suitability appear relative to the sample injections?"
- **Data to pull:** the full injection sequence log with timestamps.
