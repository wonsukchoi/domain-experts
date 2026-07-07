# Red Flags

### No retention schedule exists, or the last review predates 5+ years
- **Usually means:** disposal decisions are being made ad hoc by individual employees, or nothing is ever disposed of.
- **First question:** "When a record's retention period expires today, who decides whether it's actually deleted?"
- **Data to pull:** last retention schedule revision date, disposal log (if any) for the past 12 months.

### Migration exception rate climbing wave over wave (e.g., 0.5% → 2% → 5%)
- **Usually means:** a systemic source-corruption or metadata-crosswalk gap, not random noise — later waves are often hitting an older or less-maintained part of the source system.
- **First question:** "What's different about the content in this wave vs. the clean earlier waves — age, folder structure, custom fields?"
- **Data to pull:** exception root-cause breakdown by wave, source system audit log for the affected date range.

### A litigation hold notice with no documented scope (custodians, date range, keywords)
- **Usually means:** the hold was issued verbally or via a vague email and never operationalized into a system-enforceable rule.
- **First question:** "Can I show, in writing, exactly which custodians and content this hold covers?"
- **Data to pull:** the original hold notice, current list of flagged content, comparison against the notice's stated scope.

### ROT audit finds >50% of a population as disposal-eligible
- **Usually means:** either a genuinely unmanaged file share (plausible) or an overly aggressive ROT definition sweeping in active records — verify before trusting either direction.
- **First question:** "What sample size and method produced this number, and has anyone from the business unit validated a sample?"
- **Data to pull:** the sampling methodology, a business-unit sign-off on a reviewed sample of flagged items.

### Version count on a single document exceeds 20 with no major/minor labeling convention
- **Usually means:** no check-out/check-in discipline; multiple people are editing in parallel with no declared "official" copy.
- **First question:** "Which version is authoritative right now, and who decided that?"
- **Data to pull:** version history metadata, list of editors and edit timestamps for the last 10 versions.

### A disposal certificate references a retention schedule section that doesn't exist or was superseded
- **Usually means:** disposal is running against a stale cached copy of the schedule, or the citation was never checked against the current published version.
- **First question:** "When was this schedule section last updated, and does the disposal authority still match?"
- **Data to pull:** current published retention schedule, version/date of the schedule cited on the certificate.

### Custom metadata fields present in the source system aren't listed in the migration crosswalk
- **Usually means:** the crosswalk was built from the platform's default schema, not an actual inventory of fields in active use.
- **First question:** "Did we run a field-usage report on the source system, or did we assume the default schema?"
- **Data to pull:** source-system field usage report (frequency of population per custom field).

### Legal hold release has no written confirmation, only "the case settled"
- **Usually means:** informal assumption that the case's end automatically ends the preservation duty — it doesn't; the hold has to be formally lifted.
- **First question:** "Has legal sent written confirmation the hold is released, and for what scope?"
- **Data to pull:** case status from legal, the original hold notice's stated release conditions.

### A migration project has no hash-sample validation step, only count matching
- **Usually means:** the project plan treats "file exists in target" as equivalent to "file is intact" — it isn't; truncation and corruption can preserve file count while destroying content.
- **First question:** "What sample of migrated files has anyone actually opened or hash-compared against the source?"
- **Data to pull:** the migration project plan's validation section, any existing hash-comparison results.
