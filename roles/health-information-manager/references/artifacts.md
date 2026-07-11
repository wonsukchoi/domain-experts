# Artifacts

Filled examples for the two recurring deliverable types in this role: registry abstracts/governance corrections, and the tables that back MPI, governance, and retention decisions.

## Cancer registry abstract (filled)

The two corrected primaries from the SKILL.md worked example, as they appear in the abstracting system after the void-and-refile correction:

| Field | Primary 1 | Primary 2 |
|---|---|---|
| Sequence number | 00 | 01 |
| Primary site (ICD-O-3 topography) | C50.9 (breast, left) | C50.9 (breast, right) |
| Laterality | 2 – Left | 1 – Right |
| Histology/behavior (ICD-O-3) | 8500/3 (infiltrating duct carcinoma) | 8500/3 (infiltrating duct carcinoma) |
| Grade | 2 – Moderately differentiated | 1 – Well differentiated |
| Date of diagnosis | 01/14/2025 | 05/09/2025 |
| Class of case | 00 (diagnosed and all first-course treatment at this facility) | 00 |
| T / N / M | T2 N0 M0 | T1c N0 M0 |
| AJCC stage group (8th ed.) | IIA | IA |
| Multiplicity determination | SEER MPH Breast Rule — paired organ, coded as separate primary regardless of histology match | Same rule, same citation |
| Follow-up status | Active, next contact due 01/14/2026 | Active, next contact due 05/09/2026 |

## MPI match-decision matrix

Thresholds are the deterministic/probabilistic band structure a governance charter should specify explicitly — the numeric cutoffs below are the shape to fill in with the facility's own validated match-algorithm output, not universal constants:

| Match band | Example criteria | Action | Who executes |
|---|---|---|---|
| Deterministic — exact | SSN + DOB + legal last name all exact match | Auto-merge | System, no human review |
| Deterministic — near-exact | SSN + DOB exact, last name fuzzy-match (nickname/maiden name) | Auto-merge with flag for next-audit spot check | System; HIM specialist samples flagged merges monthly |
| Probabilistic — high confidence | Weighted algorithm score in top band (e.g., top 5% of score distribution, no conflicting demographics) | Manual review, same-day turnaround target | Credentialed HIM specialist |
| Probabilistic — mid band | Score in the ambiguous middle range, or any conflicting field (different address + matching name/DOB) | Manual review, hold merge until resolved | Credentialed HIM specialist, second reviewer for split-decision cases |
| Below threshold | Score below the facility's minimum review trigger | No action; record stays flagged as possible-duplicate for periodic batch review | Batch process, quarterly |

Escalation rule: if the mid-band or below-threshold queue backlog exceeds a facility's defined staffing capacity for two consecutive review cycles, the fallback is tightening the auto-merge threshold to shrink the top-band inflow (freeing reviewer time for the harder cases) — never loosening the probabilistic threshold to auto-clear the backlog.

## Data governance decision-rights table

Filled example distinguishing who decides, who's consulted, and who's merely informed for the recurring event types this role touches:

| Event | Decides | Consulted | Informed |
|---|---|---|---|
| MPI merge, deterministic band | System (automated); HIM manager owns threshold config | — | Registration supervisor (monthly report) |
| MPI merge, probabilistic band | Credentialed HIM specialist (primary + second reviewer on split votes) | Attending physician if clinical conflict found mid-review | Compliance officer (quarterly duplicate-rate trend) |
| New/changed quality-measure definition | Data governance committee chair, with informatics lead sign-off | Clinical department reporting the measure, compliance | All departments using the metric (change log published) |
| Retire or redefine a legacy EHR field | Data governance committee (vote) | IT/EHR build team, HIM coding lead | Downstream report owners consuming the field |
| Cancer registry case classification override | Certified Tumor Registrar (CTR) on the case | Program coordinator if edit-check conflict | CoC accreditation file (audit trail) |
| Record destruction past retention schedule | HIM director, with legal sign-off that no litigation hold applies | Legal/compliance | Governance committee (annual destruction log) |

## Retention and destruction schedule (illustrative structure)

Actual periods are set by state statute and facility policy — this is the table structure to populate, not universal numbers. Every populated cell must cite the governing statute or facility policy, not be left as a bare number:

| Record type | Illustrative retention period | Governing source (fill in per jurisdiction) | Litigation-hold override |
|---|---|---|---|
| Adult inpatient medical record | e.g., 10 years post-discharge | State medical records statute | Yes — hold suspends destruction regardless of elapsed time |
| Minor patient record | e.g., age of majority + statute period | State medical records statute (minors clause) | Yes |
| Cancer registry abstract | Permanent (per CoC accreditation requirement) | CoC accreditation standard | N/A — never destroyed |
| Diagnostic imaging | Per state statute, often shorter than the chart itself | State statute | Yes |
| MPI merge/audit trail | Permanent or facility-defined long retention | Facility governance policy | Yes |

## Accreditation-timeliness self-check (CoC cycle)

Populate before each NCDB submission window closes:

| Metric | Benchmark | This cycle's actual | Gap action if below benchmark |
|---|---|---|---|
| Cases accessioned within 6 months of diagnosis | ≥ 90% (CoC standard) | [fill in] | Triage oldest pending-query cases first; do not close incomplete cases just to hit the date |
| Analytic case follow-up rate | ≥ 90% (CoC standard) | [fill in] | Run NDI (National Death Index) linkage and mailed follow-up letters before declaring lost-to-follow-up |
| Cases with NOS histology or site | Facility-set ceiling, commonly reviewed above ~10% | [fill in] | Audit pathology documentation sufficiency before auditing coder performance |
