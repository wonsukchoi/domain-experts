# Playbook

Filled templates for MEDDPICC discovery, POC scoping, competitive bake-offs, and RFP response. Populate the placeholders per deal; the structure, scoring bands, and thresholds are the reusable part.

## MEDDPICC scorecard (filled example — Northbridge Payments, $240k ACV)

| Pillar | Status | Evidence |
|---|---|---|
| **M**etrics | Confirmed | 51,000/month flagged transactions (4.25%), ~3,400 analyst-hours/month review cost |
| **E**conomic Buyer | Confirmed | VP Fraud Ops, budget owner, met directly week 2 |
| **D**ecision Criteria | Confirmed | Written: latency, flag-reduction %, recall floor, integration effort |
| **D**ecision Process | Confirmed | Tech eval (3 wk) → security review → procurement → VP sign-off |
| **P**aper Process | Partial | Procurement redline SLA unknown — flagged as open risk at POC start |
| **I**dentify Pain | Confirmed | 96.05% recall / 3.48% precision baseline, quantified from 30-day replay |
| **C**hampion | Confirmed | Head of Risk Engineering, co-signed success criteria |
| **C**ompetition | Confirmed | Incumbent rule engine + one named competitor in bake-off |

**Scoring convention:** 2 points confirmed, 1 partial, 0 unknown, 16 max. Score at POC kickoff: 15/16. Deals entering a POC below 8/16 (fewer than half the pillars past "partial") get routed back to discovery — the bake-off is not a substitute for qualification.

## POC success-criteria document (filled example)

| Field | Value |
|---|---|
| Account | Northbridge Payments |
| Champion sign-off | Head of Risk Engineering, 2026-01-20 |
| Economic buyer sign-off | VP Fraud Ops, 2026-01-20 |
| POC window | 2026-01-24 – 2026-02-14 (3 weeks) |
| Success criterion 1 | P95 latency < 150ms per scoring call @ 2,000 req/s simulated load |
| Success criterion 2 | ≥15% relative reduction in flagged-transaction volume on customer's 30-day replay sample, recall ≥95% of 1,850 confirmed frauds |
| Success criterion 3 | Integration into existing decision service ≤ 2 engineer-weeks |
| Out of scope (phase 2 list) | Chargeback-dispute auto-response workflow; multi-currency scoring |
| Data-handling clause | Replayed transaction data only, no live production traffic; PII fields hashed before ingestion |

Convention: cap at 3-5 criteria. A POC with more than 5 signed criteria is usually a sign discovery wasn't focused enough to name the actual pain — scope creep in criteria count predicts scope creep in the exit report.

## POC exit report template (filled)

```markdown
### POC Exit Report — <Account> — <date>
**Criterion 1 (<metric>, <threshold>): PASS/MISS** — measured <value>.
**Criterion 2 (<metric>, <threshold>): PASS/MISS** — measured <value>; root cause if MISS.
**Criterion 3 (<metric>, <threshold>): PASS/MISS** — measured <value>.
**Technical win:** confirmed/not confirmed by <champion name> and <economic buyer name>, <date>.
**Open items logged for phase 2:** <list, explicitly not part of this evaluation>.
**Next step:** handed to AE for <procurement/security review/pricing>; SE remains engaged as <role>.
```

## Bake-off rubric (filled example, weighted co-written with champion)

| Criterion | Weight | Vendor A (this company) | Vendor B (incumbent competitor) |
|---|---|---|---|
| Scoring latency P95 @ 2,000 req/s | 25% | 128ms | 210ms |
| Flag-volume reduction vs. baseline | 30% | 16.1% | 9.4% |
| Recall on known-fraud sample | 25% | 96.2% | 94.8% (below customer's 95% floor) |
| Integration effort (engineer-weeks) | 10% | 3 | 2 |
| SOC 2 Type II report available at bake-off start | 10% | Yes | No — in progress |

Convention: the rubric and weights are agreed with the champion **before** either vendor sees the other's results, and both vendors are scored against the same replayed data set — not each vendor's own cherry-picked sample.

## RFP go/no-go scoring (filled example)

| Factor | Weight | Score (1-5) | Notes |
|---|---|---|---|
| Existing relationship / discovery already done | 30% | 4 | Champion identified, MEDDPICC 12/16 |
| Incumbent-authored language detected in spec | 20% | 2 | Two line items match competitor's exact feature naming |
| Budget confirmed by economic buyer | 20% | 3 | Verbal only, not in writing |
| Realistic technical fit | 20% | 5 | No hard blockers identified |
| Response effort vs. deal size | 10% | 3 | 40 hours estimated against $240k ACV |

**Weighted score:** (4×.3)+(2×.2)+(3×.2)+(5×.2)+(3×.1) = 1.2+0.4+0.6+1.0+0.3 = **3.5/5**. Convention: below 3.0, default to no-bid unless a named executive sponsor overrides in writing — an RFP response is 30-60 hours of SE time that a genuine no-bid signal (incumbent-authored spec, no confirmed budget) rarely overcomes.

## Competitive battlecard snippet (filled example)

```markdown
### vs. Vendor B (incumbent rule engine)
**Where they win:** lower integration effort (2 eng-weeks vs. our 3) when the customer's
decision service uses standard serialization; strong in shops with < 500k tx/month where
latency at scale is never tested.
**Where we win:** flag-volume reduction (16% vs. 9% in replayed comparisons) and P95
latency under load (128ms vs. 210ms at 2,000 req/s).
**Traps to avoid:** do not claim their recall is bad in general — it is comparable at low
volume. The differentiation is specifically under load and at their stated 95% recall floor.
**Two questions that surface the gap:** "What's your P95 latency at 2,000 req/s in your
own load tests?" and "What's your flag-reduction number on a replayed sample, not a
synthetic one?"
```
