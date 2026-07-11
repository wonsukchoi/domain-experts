# Red Flags

Smell tests for health information management, data governance, and cancer/disease registry work.

### Single-system MPI duplicate rate above ~10%

- **Usually means:** deterministic-only matching with no probabilistic layer, or registration staff bypassing the search-before-create step under time pressure. Pew's 2018 patient-matching research found duplicate rates commonly in the 10–20% range within a single system, climbing higher when systems exchange data without shared identifiers.
- **First question:** "What match algorithm and threshold are we running, and when was it last validated against a known sample?"
- **Data to pull:** EMPI vendor match-rate log, most recent duplicate-record audit, registration-staff search-before-create compliance report.

### Commission on Cancer accessioning timeliness below 90% at 6 months

- **Usually means:** either staffing behind caseload growth, or a backlog of cases stuck on unresolved physician queries.
- **First question:** "How many pending cases have been waiting on a query for more than 30 days, and why haven't they escalated?"
- **Data to pull:** registry caseload aging report, open-query log with days-outstanding column.

### Analytic-case follow-up rate below 90%

- **Usually means:** the registry isn't running systematic follow-up (mailed letters, NDI linkage) and is instead relying on incidental chart contact.
- **First question:** "When did we last run a National Death Index linkage batch for this cohort?"
- **Data to pull:** follow-up-rate report by diagnosis year, NDI linkage batch history.

### A coder's caseload with NOS (not otherwise specified) histology or site coding above roughly 10%

- **Usually means:** insufficient pathology documentation detail upstream, or a coder defaulting to NOS instead of querying.
- **First question:** "For the NOS cases, was a query sent to pathology or the treating physician before coding?"
- **Data to pull:** per-coder NOS rate trend, sample of NOS-coded cases with query history attached.

### Case-finding source list missing a known feeder (e.g., outreach lab or referring pathology group)

- **Usually means:** a case-finding source was never onboarded, or an interface silently stopped delivering reports.
- **First question:** "When did we last reconcile the case-finding source list against every pathology and radiation-oncology source that treats this population?"
- **Data to pull:** case-finding source inventory, interface uptime log for pathology/radiology feeds.

### MPI auto-merge threshold loosened specifically to clear a review backlog

- **Usually means:** the queue, not match confidence, is driving the threshold — a known precursor to wrongful merges (two patients sharing one chart), a documented category of EHR safety event.
- **First question:** "Was this threshold change validated against a sample of known-correct and known-incorrect matches, or set to hit a queue-size target?"
- **Data to pull:** threshold change log with justification, post-change sample audit of merged records.

### A "framework" data-governance document with no logged decisions in the last two quarters

- **Usually means:** the charter exists on paper but the committee isn't convening, or isn't the actual venue where merges/reclassifications/field retirements get decided.
- **First question:** "What was the last decision this committee actually made, and can you show me the minutes?"
- **Data to pull:** governance committee minutes, decision log referenced in the artifacts.md decision-rights table.

### Two departments reporting the same named metric with materially different numbers

- **Usually means:** no shared definition owner — each department computed "readmission" or "duplicate rate" from its own query logic.
- **First question:** "Who owns the definition of this metric, and where is it written down?"
- **Data to pull:** both departments' query logic or metric-definition documentation, side by side.

### Sudden jump in reportable case volume or facility Case Mix Index with flat clinical volume

- **Usually means:** either a genuine documentation-improvement initiative, or coding/classification drift (e.g., a case-finding rule change, a new coder defaulting to higher-specificity codes) that needs auditing before it's trusted.
- **First question:** "What changed in either the patient population, the documentation process, or the coding staff this period?"
- **Data to pull:** volume trend by service line, coder roster and tenure changes, any recent documentation-improvement program launch date.

### Record destroyed or purged while a litigation hold is open, or before the retention floor

- **Usually means:** the destruction schedule ran on autopilot without checking the active-hold list — this is spoliation, not a housekeeping miss.
- **First question:** "Was this record or its custodian on the active litigation-hold list at the time of destruction?"
- **Data to pull:** litigation-hold list as of the destruction date, destruction log with authorizing signature.

### A quality measure or registry field built entirely on a free-text source

- **Usually means:** the rate looks authoritative but was never validated against chart review — standardizing the transport (FHIR/USCDI) doesn't fix an uncoded source field.
- **First question:** "Has this field's value ever been validated against manual chart abstraction, and when?"
- **Data to pull:** field-source documentation, most recent validation/chart-audit sample.

### A tumor reclassified from single to multiple primary (or vice versa) with no cited MPH rule

- **Usually means:** the reclassification was judgment-based rather than rule-based, and won't survive a NAACCR edit-check or CoC re-abstracting audit.
- **First question:** "Which specific SEER MPH rule or site module was applied, and is it cited in the abstract notes?"
- **Data to pull:** abstract note/citation trail, NAACCR edit-check output for the case.
