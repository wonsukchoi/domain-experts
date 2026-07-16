# Vocabulary

### Data steward / data owner
The named individual accountable for a specific dataset's quality, definition, and appropriate use — distinct from whoever happens to administer the database it lives in.
**In use:** "Who's the data steward for the billing status field? That's who signs off on this definition change."
**Common misuse:** Treating the DBA or platform engineer as the de facto owner by default, when ownership is a business-accountability role, not an infrastructure-access role.

### Data lineage
The traceable path a piece of data takes from its originating source system through every transformation to where it's consumed, used to answer "where did this number actually come from."
**In use:** "Before we trust this dashboard number, walk the lineage back to the source table."
**Common misuse:** Stopping lineage documentation at the first upstream table instead of tracing all the way to the originating system, which hides the actual point of divergence.

### Master data management (MDM)
The discipline and tooling for maintaining one authoritative record for core business entities (customer, product, vendor) that's referenced consistently across systems, rather than each system maintaining its own copy.
**In use:** "Customer ID mismatches across CRM and Billing are an MDM gap, not a one-off bug."
**Common misuse:** Assuming a single database migration solves MDM, when the discipline is ongoing — new systems keep getting built that need to reference the same authoritative record.

### Semantic layer / metrics catalog
A governed layer where business metric definitions are declared once and enforced everywhere they're consumed, so "active users" means the same thing in every tool that reports it.
**In use:** "That number didn't come from the metrics catalog — that's why it doesn't match the board deck."
**Common misuse:** Building the semantic layer but not making it mandatory, so teams that find it inconvenient just query the raw tables directly and reintroduce the original divergence.

### Data minimization
The principle of collecting and retaining only the data necessary for a specific, stated purpose, and for no longer than that purpose requires (GDPR Art. 5(1)(c)).
**In use:** "We don't have a named use case for this field past the trial period — minimization says we stop collecting it at day 14."
**Common misuse:** Applying it only at collection time and forgetting the retention half — collecting narrowly but keeping everything forever isn't minimization.

### PII (personally identifiable information)
Any data that can identify a specific individual alone or combined with other data — broader than obvious fields like name or SSN; includes device fingerprints, precise location, and behavioral patterns that narrow to one person.
**In use:** "Device fingerprint plus click timestamp is PII once it's combined — treat the whole table as Tier 1."
**Common misuse:** Classifying only the obviously-named PII fields (email, SSN) and missing that combinations of "harmless" fields can reidentify individuals just as reliably.

### Data quality dimensions
DAMA-DMBOK's six-part checklist for diagnosing "bad data": accuracy, completeness, consistency, timeliness, validity, uniqueness — each a distinct failure mode with a distinct fix.
**In use:** "This isn't an accuracy problem, it's a timeliness problem — the numbers are right, they're just three days stale."
**Common misuse:** Treating "data quality" as one undifferentiated complaint instead of diagnosing which specific dimension failed, which is what determines the actual fix.

### Single source of truth
The state where exactly one system or definition is the authoritative answer for a given piece of data, and every consumer is required to reference it rather than maintain a parallel copy.
**In use:** "The metrics catalog is the single source of truth for revenue figures — no dashboard gets to define its own."
**Common misuse:** Believing that centralizing storage (a data warehouse) automatically creates a single source of truth, when it requires an enforced definition authority, not just consolidated infrastructure.

### Data catalog
A searchable inventory of an organization's datasets, including their owners, schemas, lineage, and classification tier — the reference system for "what data do we have and who owns it."
**In use:** "Check the data catalog before building a new pipeline — that table might already exist."
**Common misuse:** Populating a catalog once during a governance initiative and letting it go stale, so it becomes actively misleading rather than merely incomplete.

### DPIA (data protection impact assessment)
A required, documented risk assessment under GDPR (Art. 35) before beginning a type of data processing likely to result in high risk to individuals' rights.
**In use:** "This new biometric login feature needs a DPIA before it ships, not after."
**Common misuse:** Treating the DPIA as a compliance formality completed retroactively to justify a decision already made, rather than an input to the decision itself.

### Shadow data / shadow IT
Data stores or pipelines created and operated outside official, governed systems — a personal spreadsheet export, an unsanctioned SaaS tool — invisible to governance because nobody registered them.
**In use:** "The breach postmortem found a shadow export nobody in Data knew existed — that's the actual entry point."
**Common misuse:** Assuming governance coverage is complete because the catalog is complete; the catalog only covers what's been registered, and shadow data is by definition what wasn't.

### Data mesh
An organizational model (Dehghani) where data ownership is distributed to the domain teams that produce it, each treating their data as a product with its own quality and interface contract, rather than centralizing all data engineering in one team.
**In use:** "We're moving to a data mesh model — Payments owns their data product end to end instead of throwing it over the wall to central data eng."
**Common misuse:** Adopting the term to justify decentralizing data ownership without also decentralizing accountability — mesh only works if each domain team actually takes on data-product quality responsibility, not just autonomy.

### Access creep
The gradual, unintentional accumulation of data access grants that were never revoked after the original need ended, common wherever access reviews aren't scheduled.
**In use:** "Access review found 40% of grants to the customer PII table belong to people who left that project over a year ago — that's access creep."
**Common misuse:** Treating access creep as a one-time cleanup instead of an ongoing failure mode that recurs without a scheduled review cadence.
