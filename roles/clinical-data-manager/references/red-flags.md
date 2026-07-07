# Clinical Data Manager — Red Flags

### Query rate on a single CRF form exceeds 15-20% of fields queried at least once
- **Usually means:** the form's edit-check specification or field instructions are ambiguous, less often a training gap at specific sites.
- **First question:** is the query rate concentrated on this form across all sites, or spread evenly — form-wide points to design, site-concentrated points to training.
- **Data to pull:** query report grouped by CRF form and field, cross-tabbed by site.

### Site median query resolution time exceeds 30 days
- **Usually means:** site has a CRA/coordinator capacity problem, or the query itself is unclear and the site doesn't know how to close it.
- **First question:** has this site's resolution time been trending up for multiple cycles, or is it a one-cycle spike from a specific batch of queries?
- **Data to pull:** site-level query aging report, trended over the last 3 reporting cycles.

### External data source shows a result received with no matching CRF visit record
- **Usually means:** a visit wasn't entered in the EDC yet, or the external vendor's subject/visit mapping is misaligned with the CRF visit schedule.
- **First question:** does the site's paper/source record show the visit occurred on the date the external result implies?
- **Data to pull:** external vendor batch file, cross-referenced against the EDC visit-completion report.

### More than 5% of a locked/critical variable's expected values still missing at 2 weeks before planned lock
- **Usually means:** either the visit genuinely hasn't happened (protocol timeline slip) or the data was collected but not yet entered.
- **First question:** for the missing records, is the visit date in the future, or already past with no CRF entry?
- **Data to pull:** locked-variable completeness report against the visit schedule.

### A query is marked "resolved" with the identical value re-entered and no source-document reference
- **Usually means:** the site re-typed the same number without actually checking the source document the query asked about.
- **First question:** does the query-resolution comment reference a specific source document, or just restate the value?
- **Data to pull:** query resolution comment log for that field.

### New edit check deployed inside the T-minus-4-week freeze window
- **Usually means:** a late-discovered gap in the original edit-check spec, or scope creep from a stakeholder request.
- **First question:** how many new queries will this check generate, and is there runway to resolve them before lock?
- **Data to pull:** simulated query count from running the new check against current data.

### Central lab batch cadence extends past the planned data-cutoff-to-lock buffer
- **Usually means:** the lock date was set from CRF completion timelines without back-planning from the slowest external vendor.
- **First question:** what is the vendor's contractually stated batch turnaround, and when is the last batch actually due?
- **Data to pull:** vendor data transfer agreement (DTA) batch schedule.

### SAE reconciliation shows a mismatch between safety database and CRF adverse-event records
- **Usually means:** either the CRF AE wasn't linked to its SAE follow-up report, or the safety database entry predates a CRF update that hasn't synced.
- **First question:** which system has the more recent timestamp, and was a reconciliation run in both directions?
- **Data to pull:** SAE reconciliation report (bidirectional), safety database export.

### A subject has zero open queries but was never touched by an external reconciliation pass
- **Usually means:** the team is treating "no open queries" as equivalent to "clean," skipping the reconciliation step entirely.
- **First question:** when was the last full external reconciliation run for this subject, and is it dated after their last visit?
- **Data to pull:** reconciliation log timestamp per subject.

### Protocol amendment affecting a locked-variable definition arrives after edit-check freeze
- **Usually means:** clinical/regulatory timeline moved independently of the data management schedule.
- **First question:** does the amendment change the SAP's primary or key secondary endpoint definition?
- **Data to pull:** amendment redline against the current DMP locked-variable list.
