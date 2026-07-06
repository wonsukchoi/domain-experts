# Paralegal playbook — filled templates

Working structures an agent can populate directly, not descriptions of what they should contain. Primary context: the Doe v. Acme Grocery matter from the SKILL.md worked example, plus one document-review variant (In re Meridian Supply Chain Litigation, a larger commercial matter) where the mechanism differs materially.

## 1. Three-date docket-control entry (filled)

Never docket a rule- or statute-driven deadline as a single date. Every entry gets a readiness check, a hard-stop target, and the true deadline flagged not-for-filing.

| Matter | Governing deadline | True deadline | Readiness review (-~30 days) | Hard-stop filing target (-5 to -7 business days) | Notes |
|---|---|---|---|---|---|
| Doe v. Acme Grocery | 2-yr personal injury SOL from Mar 15, 2024 accrual | Mon, Mar 16, 2026 (rolled forward from Sun, Mar 15) | Mon, Feb 16, 2026 | Mon, Mar 9, 2026 | Do not calendar Mar 15 — clerk's office and e-filing queue both treat Sunday as non-filing |
| Roe v. Meridian Supply | Response to MSJ, local rule = 21 days from service (served Apr 6, 2026) | Mon, Apr 27, 2026 | Fri, Apr 10, 2026 (draft outline) | Tue, Apr 21, 2026 | 21-day count is calendar days; no weekend roll needed since Apr 27 falls midweek |
| Smith v. Highline Freight | Answer due, 30 days from effective service (mailed Jan 2, 2026 + 3-day mail-service extension = Jan 5, 2026 effective date, then 30 days) | Wed, Feb 4, 2026 | Wed, Jan 21, 2026 | Wed, Jan 28, 2026 | Mail-service extension applied to get the effective service date first, then the 30-day count runs from that date — reversing the order understates the deadline by 3 days |

**Rule attached to the table:** the "true deadline" column is never the value entered as the working target elsewhere in the case-management system — the hard-stop column is. If a hard-stop and a true deadline collapse onto the same date (a short-fuse deadline), escalate to the attorney immediately rather than silently accepting the compressed timeline.

## 2. Privilege log — metadata-plus-topic (categorical) format

Grouped by custodian and subject, per Sedona Conference's categorical-logging guidance; switch to document-by-document only for entries a motion to compel specifically targets.

| Log # | Custodian | Date range | Author/sender | Recipients (cc) | Doc type | Subject category | Privilege asserted | Count withheld |
|---|---|---|---|---|---|---|---|---|
| PL-001 | J. Alvarez (GC) | Feb 3–14, 2026 | J. Alvarez | R. Chen (COO), outside counsel | Email chain | Legal risk assessment of vendor termination | Attorney-client | 14 |
| PL-002 | R. Chen (COO) | Feb 5–9, 2026 | Outside counsel | J. Alvarez, R. Chen | Memo | Draft litigation-hold scope | Attorney-client / work product | 3 |
| PL-003 | M. Osei (Finance) | Mar 1–4, 2026 | Outside counsel | M. Osei, J. Alvarez | Spreadsheet + email | Damages exposure modeling for anticipated claim | Work product | 6 |
| PL-004 | J. Alvarez (GC) | Mar 10, 2026 | J. Alvarez | R. Chen, **B. Kwan (VP Sales, non-lawyer, no counsel cc'd)** | Email | Contract renegotiation strategy | **Flagged — no attorney on thread; review before logging as privileged** | 1 |

**Rule attached to the log:** any entry where every recipient is a non-lawyer business person and no attorney appears anywhere in the thread (see PL-004) gets pulled for attorney review before it's logged as privileged at all — cc'ing the general counsel on an unrelated thread doesn't retroactively privilege a business discussion, and logging it as privileged without checking invites the whole log being challenged.

## 3. First-pass review QC tracker (In re Meridian Supply Chain Litigation)

10% QC sample per batch; re-review triggers at >2% sampled error rate.

| Batch | Docs reviewed | Docs/hour | QC sample size | Errors found | Sample error rate | Action |
|---|---|---|---|---|---|---|
| B-014 (custodian: warehouse ops) | 1,240 | 78/hr | 124 | 2 | 1.6% | Pass — no re-review |
| B-015 (custodian: procurement) | 980 | 61/hr | 98 | 3 | 3.1% | **Fail — full batch re-review, not spot-fix** |
| B-016 (custodian: legal/compliance, privilege-sensitive) | 610 | 41/hr | 61 | 1 | 1.6% | Pass — slower rate expected given privilege screening on top of relevance |
| B-017 (custodian: warehouse ops, reviewer new to team) | 1,510 | 156/hr | 151 | 4 | 2.6% | **Fail — re-review; throughput nearly double the batch average is itself a flag independent of the error rate** |

**Rule attached to the tracker:** a batch failing the 2% threshold is re-reviewed in full — the found errors get corrected, but the untested 90% of the batch is now known-unreliable and gets the same scrutiny as the sample, not a spot-check of just the flagged documents.

## 4. Cite-check log (brief: Doe v. Acme Grocery, Motion for Summary Judgment Opposition)

| Citation as drafted | Issue found | Correction |
|---|---|---|
| *Anderson v. Liberty Lobby, Inc.*, 477 U.S. 242, 248 (1986) | Pin cite off by one page — quoted language is on 249, not 248 | Corrected pin cite to 249 |
| "*Id.* at 250" (third use in a row, after an intervening citation to a different case) | `Id.` no longer refers to the immediately preceding authority — intervening cite broke the chain | Replaced with full short form: *Anderson*, 477 U.S. at 250 |
| *Celotex Corp. v. Catrett*, 477 U.S. 317 (1986) | Missing pin cite entirely for a specific quoted holding | Added pin cite (477 U.S. at 323) after confirming against the reporter |
| Signal "See" used before a case that directly states the proposition (should be no signal) | Understates how directly the case supports the point | Removed signal |

**Rule attached to the log:** every pin cite is checked against the actual reporter text, not against the drafting attorney's internal citation or a prior brief that used the same case — a wrong pin cite that's copied forward compounds across every brief that reuses it.

## 5. Exhibit and witness binder index (trial prep, Doe v. Acme Grocery)

| Exhibit # | Bates range | Description | Witness(es) tied to exhibit | Pre-marked | Objection noted |
|---|---|---|---|---|---|
| P-1 | ACME000104–000106 | Incident report, Mar 15, 2024 | Store manager (R. Delgado) | Yes | None |
| P-2 | ACME000210–000238 | ER records, Mar 15, 2024 | Treating physician (Dr. Nkemdirim) | Yes | Defense: foundation (deposition pending) |
| P-3 | ACME000512 | Store surveillance still frame, 2:14 PM | Store manager, plaintiff | Yes | Defense: authentication |
| P-4 | ACME000600–000601 | Maintenance log, prior 90 days | Maintenance supervisor (T. Ruiz) | Yes | None |

**Rule attached to the index:** an exhibit isn't trial-ready because it's Bates-stamped — it's trial-ready when every listed objection has a resolution plan (stipulation, foundation witness confirmed, or motion in limine drafted) attached before the pretrial conference, not discovered at it.
