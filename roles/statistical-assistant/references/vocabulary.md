# Statistical Assistant — Vocabulary

### Double entry
Independently entering the same source record twice (by different people, or the same person on separate passes) and comparing the two entries field by field to catch entry errors.
**In use:** "We're double-entering the first 10% of this batch to get a baseline error rate before switching to single entry."
**Common misuse:** Treated as a way to determine which of two entries is "correct" — it only flags disagreement; resolving it requires the source document, not a coin flip between the two entries.

### Range check
An automated rule that flags a value falling outside a plausible range for that field (e.g., age between 0 and 120).
**In use:** "The range check on assessment score caught a 41 that should have been 14 — classic transposition."
**Common misuse:** Assumed to catch all entry errors. It only catches values outside the plausible range; a wrong-but-plausible value (a real age typed instead of the correct one) sails through untouched.

### Consistency check
A rule that validates a field against another field in the same record (e.g., enrollment date must be on or after intake date), rather than checking one field in isolation.
**In use:** "Add a consistency check so enrollment date can't be entered before intake date."
**Common misuse:** Confused with a range check. A consistency check needs two fields; a range check needs only one.

### Missing-data code
A specific, documented value (e.g., -99, "refused," "not applicable") used to record why a value is absent, as distinct from an unexplained blank cell.
**In use:** "That's not a blank — it's coded -98 for 'source form illegible,' which is different from -99 'not asked.'"
**Common misuse:** Used interchangeably with a blank cell, or with each other — "refused" and "not applicable" get treated as the same code when they mean different things for the denominator in a percentage calculation.

### Codebook
The document that defines every variable in a dataset: its label, type, valid values, missing-data codes, and collection-date range.
**In use:** "Before you tabulate, check the codebook — eligibility category has six valid values as of Batch 3, not five."
**Common misuse:** Treated as a one-time document written at project start and never revisited, rather than a living record updated the same day a new missing-data code or accepted out-of-range value comes up.

### Cell suppression
Withholding a specific cell's count in a published tabulation (usually replacing it with a symbol) because the count is small enough to risk identifying an individual.
**In use:** "That cell is n=3 — suppressed per the researcher's n<5 threshold, and I flagged it as suppressed, not a true zero."
**Common misuse:** Confused with rounding, or applied by the data-entry/tabulation staff on their own judgment rather than the researcher's stated disclosure-risk policy.

### Discrepancy rate
The proportion of field-entries (not records) that disagreed between two independent entry passes.
**In use:** "Overall discrepancy rate is 0.78%, but that's hiding a 3.6% rate concentrated in the intake-date field."
**Common misuse:** Reported only as a single aggregate number, which can mask a form-design problem concentrated in one or two fields.

### Field-level error concentration
The pattern where a disproportionate share of total errors cluster in a small number of fields rather than distributing evenly.
**In use:** "Two of twelve fields account for 57% of all discrepancies — that's field-level concentration pointing at the date-format issue, not general carelessness."
**Common misuse:** Missed entirely when only the aggregate discrepancy rate is reported, since concentration is invisible in an average.

### Input mask
A form-field constraint that forces data entry into a specific format (e.g., forcing a date field to accept only DD/MM/YYYY).
**In use:** "Adding an input mask to the date fields should eliminate the format-confusion discrepancies we saw in Batch 3."
**Common misuse:** Assumed to eliminate all entry errors for that field — it enforces format, not correctness; a wrong-but-correctly-formatted date still gets through.

### Tabulation / cross-tab
A summary table of counts (or percentages) broken out by one or more categorical variables, produced to a researcher's specification.
**In use:** "The spec calls for eligibility category by referral source, unweighted counts, cells under 5 suppressed."
**Common misuse:** Produced with the statistical assistant's own choices on weighting, rounding, or suppression rather than exactly what the researcher specified, with any necessary deviation flagged rather than made silently.
