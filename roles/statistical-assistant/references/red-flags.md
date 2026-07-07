# Statistical Assistant — Red Flags

### Overall discrepancy rate under 1% with no field-level breakdown produced
- **Usually means:** the rate is being reported as a single aggregate without checking whether errors are concentrated in one or two fields, which can hide a form-design problem behind an acceptable-looking average.
- **First question:** "What's the discrepancy rate broken out by field, not just overall?"
- **Data to pull:** the double-entry reconciliation log with a per-field tally.

### One field accounts for more than 30% of all discrepancies
- **Usually means:** a form-design issue (ambiguous format, no input mask, confusing label) rather than an entry-staff training gap.
- **First question:** "What does the source document look like for this field, and does it match what the entry template asks for?"
- **Data to pull:** the source document format/convention for that field, and the entry template's input format/validation.

### A range check hasn't fired in 200+ records of high-volume entry
- **Usually means:** either the field is genuinely clean, or the threshold has drifted loose relative to the current data and stopped catching anything.
- **First question:** "When was this threshold last reviewed against the actual data distribution?"
- **Data to pull:** a distribution of the field's values over the last several batches.

### A codebook's valid-value list doesn't match what's actually appearing in the data
- **Usually means:** either an out-of-range value slipped through without being caught, or the form changed and the codebook wasn't updated to match.
- **First question:** "Is this a new legitimate category the form now allows, or a data-entry error that bypassed the range check?"
- **Data to pull:** the current version of the form/entry template and the codebook's last-updated date.

### A double-entry discrepancy was resolved without checking the source document
- **Usually means:** the resolver picked whichever entry "looked right," which defeats the purpose of double entry and can silently enshrine the wrong value.
- **First question:** "Was the source document pulled for this resolution, or was it a judgment call between the two entries?"
- **Data to pull:** the reconciliation log's resolution-method field for that record.

### Missing-data codes and blank cells are being used interchangeably
- **Usually means:** whoever is entering data hasn't been given (or isn't following) a missing-data-code convention, which will corrupt denominators in any percentage calculation downstream.
- **First question:** "What's the difference in this dataset between a blank cell and each missing-data code?"
- **Data to pull:** the codebook's missing-data-code definitions and a count of blank vs. coded-missing cells.

### A cross-tab cell-suppression decision was made without researcher sign-off
- **Usually means:** the statistical assistant applied their own judgment on a disclosure-risk question that belongs to the researcher's institutional policy.
- **First question:** "What suppression threshold did the researcher specify, and was this cell below it?"
- **Data to pull:** the original tabulation request and its stated suppression rule.

### A form/codebook version mismatch is discovered mid-batch
- **Usually means:** the form was revised (new field, changed valid values) without the codebook being updated first, or entry started on an old form version.
- **First question:** "Which version of the form was actually used to collect this batch?"
- **Data to pull:** the form-revision history and the batch's collection-date range.

### An "obvious" data-entry error is corrected without logging it as a discrepancy
- **Usually means:** a transposition or typo that looks self-evidently wrong (e.g., a 3-digit age) got silently fixed instead of logged, which understates the true error rate and hides a pattern if it's recurring.
- **First question:** "Was this correction logged in the reconciliation record, or fixed and moved past?"
- **Data to pull:** the reconciliation log for that record ID.
