# Clinical Data Manager — Playbook

## Query-metrics table (filled example, T-minus-3-weeks to lock)

| Site | Queries issued | Resolved | Open <30d | Open >=30d | Median resolution (days) |
|---|---|---|---|---|---|
| 03 | 41 | 40 | 1 | 0 | 6 |
| 05 | 28 | 28 | 0 | 0 | 4 |
| 07 | 52 | 44 | 3 | 5 | 22 |
| 09 | 19 | 19 | 0 | 0 | 5 |
| 11 | 47 | 40 | 4 | 3 | 24 |
| ...remaining 9 sites | 233 | 231 | 2 | 0 | 5 |
| **Total** | **420** | **402** | **10** | **8** | **7 (all-site median)** |

Escalation rule: any site crossing 30-day median resolution or carrying >=3 queries open past 30 days moves to direct CRA contact this cycle, not another automated reminder.

## External reconciliation checklist (run before any clean-data declaration)

1. **Central lab**: every result batch received matched to an expected visit in the CRF visit schedule. Flag: result received, no visit record (orphaned result) — target 0 before lock.
2. **ePRO**: every expected diary/questionnaire entry present for the visit window; flag missing entries past the site's grace period (commonly 3 days) as a query, not a silent gap.
3. **IRT/randomization**: dosing/randomization record cross-checked against drug accountability log; any mismatch escalated as a query against both systems, not assumed correct in either.
4. **SAE reconciliation**: every serious adverse event in the safety database has a matching CRF AE record and vice versa — run both directions, since a gap in either direction means either underreporting or an orphaned safety record.
5. **Local lab normal ranges**: confirm each site's local lab range table loaded matches what was used to flag out-of-range CRF values — a stale range table produces false or missed range-check queries silently.

## Lock-readiness back-planning worksheet (filled example)

| Milestone | Target date | Depends on |
|---|---|---|
| Last subject, last visit (LSLV) | Day 0 | Protocol-defined |
| Last external data batch expected (central lab, slowest vendor) | LSLV + 10 | Vendor's stated batch cadence |
| Edit-check freeze (no new checks deployed after this date) | LSLV + 14 | 4 weeks before target lock |
| Query resolution cutoff (all queries must be closed or have a disposition) | LSLV + 24 | 1 week before target lock |
| External reconciliation complete | LSLV + 26 | After last batch + query cutoff |
| Clean-data sign-off memo issued | LSLV + 28 | Reconciliation complete |
| Soft lock | LSLV + 29 | Sign-off countersigned |
| Hard lock | LSLV + 31 | SAP locked-variable list reconfirmed unchanged |

Rule: the "last external data batch expected" date sets the floor for everything downstream — if the slowest vendor's cadence pushes past LSLV+10, every later milestone shifts by the same amount; don't compress the query-resolution or reconciliation windows to protect the original lock date.

## Fallback positions when lock date is at risk (in preference order)

1. Escalate specific aged queries/reconciliation gaps to CRA/site directly, with a named resolution date — always the first move, never blanket "please clean your data" reminders.
2. Partial soft lock on subjects/sites that are fully reconciled, holding the remainder open — viable only if the SAP's analysis population definition allows a staggered lock; confirm with biostatistician before proposing.
3. Move the lock date, with the delay quantified against a named root cause (not "data cleaning is taking longer than expected") — the last resort, and always accompanied by the DMP defect that will prevent the same slip next time.
