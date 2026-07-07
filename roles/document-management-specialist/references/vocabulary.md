# Vocabulary

### ROT (Redundant, Obsolete, Trivial)
Content with no ongoing business, legal, or regulatory value — duplicate copies, superseded versions, or personal/test files.
**In use:** "The ROT audit came back at 35% of the archive — that's our disposal-eligible population before we even touch the retention-schedule content."
**Common misuse:** Generalists use "ROT" as a synonym for "old files," conflating it with content that's simply aged but still an active or permanent record.

### Legal hold
A directive to preserve specific documents and data because litigation is reasonably anticipated or pending, suspending normal retention/disposition for the in-scope content.
**In use:** "The hold covers all correspondence with Acme from January 2024 forward — nothing in that scope gets auto-deleted regardless of its retention class."
**Common misuse:** Treating a hold as informal guidance rather than an enforceable, scoped override that must be operationalized in the system, not just communicated verbally.

### Spoliation
The destruction, alteration, or failure to preserve evidence relevant to litigation, which can trigger court sanctions.
**In use:** "Auto-deletion firing on held content isn't a technical glitch to apologize for — it's a spoliation event legal has to disclose."
**Common misuse:** Assuming spoliation requires intent; courts sanction negligent failures to preserve, not only deliberate destruction.

### Crosswalk (metadata crosswalk)
A field-by-field mapping between a source system's metadata schema and a target system's schema, used to preserve classification and retrievability through a migration.
**In use:** "The crosswalk didn't include the custom 'matter number' field, so those five documents migrated with no way to find them again."
**Common misuse:** Building the crosswalk from the platform's default schema instead of an actual inventory of fields in use in the source system.

### GARP (Generally Accepted Recordkeeping Principles)
ARMA International's eight-principle framework (Accountability, Transparency, Integrity, Protection, Compliance, Availability, Retention, Disposition) for evaluating a records program's maturity.
**In use:** "We scored the program against GARP and Accountability is the weak point — nobody owns disposition sign-off."
**Common misuse:** Treating GARP as a checklist of eight boxes to tick rather than a diagnostic for where ownership is missing.

### Records series
A group of related records that share the same retention treatment, managed as a unit rather than record-by-record.
**In use:** "Signed customer contracts is one series — same 7-year retention, same disposal method, regardless of which product line."
**Common misuse:** Defining series too granularly (one per department or one per project), which multiplies retention-schedule maintenance without changing the underlying legal requirement.

### Defensible disposal
Disposal of records that can be affirmatively justified — the right authority, no active hold, correctly classified — if ever challenged.
**In use:** "We can show a defensible-disposal trail for every one of those 63,000 files: retention schedule citation, hold-clearance check, sign-off date."
**Common misuse:** Treating "defensible" as "we didn't get caught" rather than "we can produce the authority and process on demand."

### DoD 5015.02-STD
A US Department of Defense conformance standard for records management software, used industry-wide as a benchmark for whether an RM module truly enforces classification, retention, and auditable disposition.
**In use:** "The vendor claims RM capability, but it isn't 5015.02-certified — let's verify it actually enforces disposition holds before we depend on it."
**Common misuse:** Assuming any platform with a "records management" feature toggle meets this bar without checking actual certification or independent testing.

### Check-out/check-in
A version-control mechanism that locks a document for exclusive editing by one user at a time, preventing concurrent silent edits.
**In use:** "Nobody checked the file out, so two people edited it in parallel and we now have two 'final' versions to reconcile."
**Common misuse:** Assuming platform versioning alone (keeping a history of saves) substitutes for check-out discipline; versioning records the fork, it doesn't prevent it.

### Migration wave
A defined, bounded subset of a migration population moved and reconciled as a unit before the next subset begins.
**In use:** "Wave 1 was our pilot at 5,000 documents — we don't scale up until the exception rate is back under control."
**Common misuse:** Treating "waves" as arbitrary batching for throughput rather than as reconciliation checkpoints that should gate progression.

### File plan
The organizing structure (taxonomy) that classifies records into series and links each to its retention schedule — the map records management is executed against.
**In use:** "The file plan hasn't been updated since the reorg three years ago; half these folders don't map to a current business function."
**Common misuse:** Confusing the file plan (a governance/classification structure) with a folder structure in a content management system (a storage/navigation structure) — they should align but often don't.

### Reconciliation (migration)
The process of confirming source count, migrated count, and exception count sum with zero unaccounted, typically paired with a sampled integrity check.
**In use:** "Reconciliation isn't done until the exception count is fully remediated and the counts match exactly — not approximately."
**Common misuse:** Treating a migrated-count-close-to-source-count as sufficient without accounting for every difference by name.
