# Playbook

Filled procedures for the three recurring workflows: AFIS candidate disposition, NCIC validation cycle, and records-disclosure authorization.

## 1. AFIS/NGI candidate disposition sequence

Work the returned candidate list in rank order. Stop at the first verified identification; don't screen the rest of the list "to be thorough" — that just burns examiner time without changing the disposition.

| Step | Action | Disposition trigger |
|---|---|---|
| 1 | Compare general pattern class (loop/whorl/arch) and ridge flow | Mismatch → **exclude**, no minutiae count needed |
| 2 | If pattern class matches, count corresponding minutiae in the latent's usable area | <8 with no corroborating ridge-count/pore detail → **inconclusive** |
| 3 | If ≥8 corresponding minutiae, check ridge counts along at least 2 independent delta-to-core paths | Any unexplained discrepancy → **inconclusive**, re-examine before excluding |
| 4 | Zero unexplained discrepancies, consistent ridge counts | → **identification** |
| 5 | Route identification to a second examiner, blind to case context and to step 1–4's conclusion | Disagreement → escalate to agency's technical review board, do not average or split the difference |

Minutiae-count thresholds above are a **stated internal QA heuristic**, not a legal minimum — IAI has no fixed national point standard. Set and document your agency's own threshold; the number matters less than having one applied consistently and disclosed if challenged.

## 2. NCIC validation cycle tracking

Run this as a standing weekly report, not an as-needed lookup.

| Field | Example entry |
|---|---|
| NIC number | W123456789 |
| Entry type | Wanted person |
| Entry date | 2026-03-15 |
| First validation due | 2026-06-13 (90 days) |
| Subsequent validation cadence | Annual from first validation |
| Originating unit contacted | Detective Bureau, Case 26-01187 |
| Confirmation received | Y/N, date |
| Action if unconfirmed by due date | Escalate to unit supervisor 5 business days before deadline; if still unconfirmed at deadline, entry purges automatically — log the purge and notify the originating unit same day |

Weekly batch example: 42 entries due for validation this cycle.

| Disposition | Count |
|---|---|
| Confirmed active, revalidated | 31 |
| Confirmed served/closed, cancelled | 6 |
| No response by deadline, escalated | 3 |
| No response after escalation, purged | 2 |
| **Total** | **42** |

31 + 6 + 3 + 2 = 42. The 2 purges get a same-day notice to the originating detective — a purged want is a want that stops surfacing on any agency's routine NCIC query, not a paperwork event.

## 3. Records-disclosure authorization check

Run this classification before any release, every time — familiarity with a requester is not an authorization.

| Requester type | Authorized scope | Governing authority | Log requirement |
|---|---|---|---|
| Criminal justice agency, active case | Full CHRI relevant to stated case | 28 CFR Part 20, interagency agreement | Requester agency, case number, officer name |
| Employer / licensing board | Only what state statute authorizes for that license/employment category (often excludes sealed/juvenile/non-conviction data) | 28 CFR 20.33, state licensing statute | Requester, statutory basis cited, scope released |
| Court order / subpoena | Only what the order specifically compels | Court order text | Order number, issuing court, scope |
| Sealed or expunged record surfaced in a routine search | **None** — withhold from response | Sealing/expungement statute (state-specific) | Internal flag for record correction, not a disclosure log entry |
| Individual requesting own record | Full record, subject to identity verification | State public-records/personal-access statute | ID verification method, scope released |

If the requester's stated purpose doesn't map cleanly to a row above, don't guess — hold the request and get a written statutory citation from the requester or route to the records supervisor/legal counsel before releasing anything.
