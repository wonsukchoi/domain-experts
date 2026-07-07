# File Clerk — Red Flags

### Misfile-audit sample rate above 2%
- **Usually means:** A specific scheme-driven pattern (digit transposition, ambiguous subject code) is producing repeat errors, or the classification rules themselves are ambiguous for a specific record type.
- **First question:** When we group the misfiled records by where they were actually found, do they share a pattern?
- **Data to pull:** The misfile-audit log with found-location noted per error, not just the pass/fail count.

### A charge-out overdue by more than 3 business days
- **Usually means:** The file is sitting on a desk and forgotten, not actively in use — the longer it's out, the higher the risk it gets misfiled on return or genuinely lost.
- **First question:** Has the requester been contacted for a status/return estimate?
- **Data to pull:** The charge-out log entry — requester, date charged, expected-return date.

### A record searched under one name/ID comes up empty
- **Usually means:** Either a genuine misfile, or the record was filed correctly under an alternate identifier (maiden name, DBA, case aka) with no cross-reference sheet created.
- **First question:** Is there a plausible alternate name or ID this record could be filed under?
- **Data to pull:** The master index entry for the record, checking for a "also known as" or alternate-ID field.

### A retention purge date arrives for a record series involved in active litigation
- **Usually means:** The retention schedule and the legal-hold list are out of sync — either the hold wasn't communicated to records management, or the purge process didn't check the hold list.
- **First question:** Has this series been cross-checked against the current hold list before today's purge run?
- **Data to pull:** The current active legal-hold list from legal/compliance, dated to today.

### First digitization batch has an index-error rate above 5%
- **Usually means:** The index template itself has a field-mapping problem (wrong field order, missing required field) rather than individual keying mistakes — a template error repeats on every document, a keying error doesn't.
- **First question:** Are the errors concentrated on one index field across most documents, or scattered across different fields?
- **Data to pull:** The index-verification log broken out by field, not just an overall error count.

### A filing backlog exceeds one business day at end of shift
- **Usually means:** Volume has outgrown the current staffing or scheme, or an interruption (a large charge-out request, an audit) displaced routine filing.
- **First question:** Is this a one-time displacement or a recurring end-of-day pattern?
- **Data to pull:** The daily filing-volume log for the past two weeks.

### A cross-reference sheet points to a primary file that no longer exists in that location
- **Usually means:** The primary file was moved, purged, or charged out without updating the cross-reference, or without a charge-out log entry that a searcher can find.
- **First question:** Does the charge-out log show this record as currently checked out, or was it purged?
- **Data to pull:** The charge-out log and the retention-purge manifest for the relevant date range.

### The same clerk's shift accounts for a disproportionate share of a misfile pattern
- **Usually means:** Either a training gap specific to that person, or that clerk is handling a disproportionate share of a genuinely error-prone record type (not necessarily a competency issue).
- **First question:** Does this clerk handle a different mix of record types than others, or the same mix with a higher error rate?
- **Data to pull:** Filing-volume-by-type logs per clerk for the audit period.
