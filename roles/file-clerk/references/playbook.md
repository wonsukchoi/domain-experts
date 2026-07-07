# File Clerk — Playbook

## Filing-scheme comparison (filled)

| Scheme | Best for | Retrieval logic | Misfile-risk driver |
|---|---|---|---|
| Straight alphabetic | <2,000 active records, name-based lookup | Last name, first name, unit-by-unit (ARMA rules) | Nothing/nothing-something transposition, similar surnames |
| Straight numeric | Sequential-order regulatory requirement | Full ID, ascending | New-file clustering at high end slows filing/retrieval in one section |
| Terminal-digit | >10,000 active records, continuous daily filing | Last 2 digits (primary section) → middle 2 (secondary) → first 2 (tertiary) | Primary/terminal digit-pair transposition (habit of reading ID left-to-right) |
| Subject/chronological | Project or matter files, date-driven retrieval | Subject code, then date within subject | Subject-code ambiguity (record fits two categories) |

## Misfile-audit sequencing (filled)

1. Pull a random sample sized to the active population: ~250 files for 10,000–20,000 active records (roughly 1.5–2% sample), ~100 files for under 5,000.
2. For each pulled file, log three fields: (a) correctly filed Y/N, (b) if N, the section where it was actually found, (c) the case/record ID.
3. Compute the misfile rate: misfiled / sampled.
4. Group the misfiled records by found-location pattern — do the errors cluster on a specific digit range, a specific record type, a specific date range (suggesting a specific clerk's shift), or are they scattered?
5. If ≥60% of errors share one pattern, the fix is scheme- or training-specific (e.g., a tab color change, a rule clarification) — pilot it on new filings only, then re-audit a smaller sample in 30 days before rolling out broadly.
6. If errors are scattered with no shared pattern, the fix is a general refresher on the classification rules, not a scheme change.

## Charge-out log fields (filled)

| Field | Example | Why it's required |
|---|---|---|
| Record ID | Case #445-1122 | Unambiguous identifier, not "the Johnson file" |
| Requester | J. Alvarez, Escrow Dept | Accountability for return |
| Date charged out | 2026-03-14 | Aging calculation |
| Expected return date | 2026-03-17 | Overdue-tracking trigger |
| Actual return date | 2026-03-16 | Closes the loop |
| Re-filed by / date | R. Chen, 2026-03-16 | Confirms it didn't just land back on a desk |

Overdue trigger: flag any charge-out past its expected-return date by more than 3 business days for a follow-up request — files charged out longer than that have a materially higher chance of becoming a "we don't know where it is" incident.

## Retention-purge cycle checklist (filled)

1. Pull the list of record series with a purge date in the current cycle from the retention schedule.
2. Cross-check every series against the current active legal-hold list — any overlap pulls that series out of this cycle's purge regardless of schedule.
3. For series clear of holds, generate a destruction manifest (record IDs, series, purge-eligible date, destruction method).
4. Route the manifest for the required sign-off (per the organization's retention policy — typically records-management or legal) before destruction.
5. Execute destruction, retain the signed manifest itself as the compliance record (a destruction certificate is evidence the schedule was followed, not the record being destroyed).
