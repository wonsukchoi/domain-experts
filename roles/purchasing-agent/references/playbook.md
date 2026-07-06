# Procurement execution playbook

Filled templates for the five recurring purchasing-agent tasks: threshold lookup, RFQ/RFP quote scoring, three-way match reconciliation, split-purchase detection, and sole-source justification.

## 1. Current dollar-threshold table (check before every buy — do not cite from memory)

| Threshold | Amount (effective Oct 1, 2025 cycle) | Instrument required above this line |
|---|---|---|
| Micro-purchase (federal) | $15,000 | Above: competition generally required (soliciting price/rate quotes from 2+ sources) |
| Simplified acquisition threshold (federal) | $350,000 | Above: full sealed bid / negotiated procurement procedures |
| Davis-Bacon public-works micro-purchase ceiling | $2,000 | Above: prevailing-wage requirements attach regardless of instrument |
| P-card single-transaction limit (org example) | $2,500 | Above: requisition + PO required, card declined by policy |
| P-card monthly cap (org example) | $10,000 | Above: card suspended pending review, not a hard stop on the buy itself |
| Cost/price analysis trigger (org example range) | $5,000–$9,999.99 | Above: written cost/price analysis required regardless of procurement method |

Lookup procedure: (1) identify funding source — federal grant, state/local, or purely organizational; (2) pull the current table for that source, not last year's; (3) apply the org policy threshold only if it is stricter than the funding-source threshold (stricter always wins).

## 2. RFQ vs. RFP selection and quote-scoring worksheet

Selection rule:

```
Spec fully defined + price is the only variable      -> RFQ
Spec has options, service-level, or approach variance -> RFP
Requirements/supplier field still unclear             -> RFI first, then RFQ or RFP
```

**RFQ scoring (price-driven, fixed spec)** — lowest total landed cost wins unless a vendor fails a pass/fail gate:

| Vendor | Unit price | Qty | Freight | Total landed cost | Lead time (bus. days) | Meets spec (Y/N) | Rank |
|---|---|---|---|---|---|---|---|
| Incumbent Corp | $1,150 | 22 | $0 (included) | $25,300 | 12 | Y | 1 |
| Vendor B | $1,090 | 22 | $340 | $24,320 | 18 | Y | — (fails lead-time gate of 15 days) |
| Vendor C | $1,205 | 22 | $0 | $26,510 | 10 | Y | 2 |

Rule: a lower total landed cost is disqualified, not just down-ranked, if it fails a stated pass/fail gate (lead time, spec compliance, certification) — rank only among vendors that clear every gate.

**RFP scoring (multi-criteria, weighted)** — use when quality, approach, or service level vary across bids:

| Criterion | Weight | Vendor A score (1–10) | Vendor A weighted | Vendor B score (1–10) | Vendor B weighted |
|---|---|---|---|---|---|
| Price | 40% | 7 | 2.8 | 9 | 3.6 |
| Technical approach | 25% | 9 | 2.25 | 6 | 1.5 |
| Past performance | 20% | 8 | 1.6 | 7 | 1.4 |
| Delivery schedule | 15% | 6 | 0.9 | 8 | 1.2 |
| **Total** | 100% | — | **7.55** | — | **7.70** |

Award to highest weighted total, not lowest price — document the weighting scheme in the solicitation before quotes come in, never after, to avoid a defensibility gap.

## 3. Three-way match reconciliation sequence

Run on every invoice before releasing payment:

1. Pull PO, receiving report, and invoice side by side.
2. Compare **quantity**: PO qty vs. receiving report qty vs. invoice qty.
3. Compare **unit price**: PO price vs. invoice price.
4. Compare **line items**: every invoice line traces to a PO line.
5. If all three agree within tolerance (organization example: unit price variance ≤ $0.50 or ≤1%, whichever is greater) — release for payment.
6. If any field disagrees beyond tolerance — **hold payment**, do not pay-and-reconcile-later, and route by likely cause:

| Mismatch pattern | Most likely cause | Route to |
|---|---|---|
| Invoice qty > receiving report qty | Partial shipment billed as full, or receiving miscount | Receiving, to confirm actual count |
| Invoice unit price > PO unit price | Vendor billed at list instead of negotiated rate | AP, with PO copy attached, for vendor correction |
| Invoice missing PO reference | AP can't match without it | Return to vendor for corrected invoice, do not manually force-match |
| Receiving report shows qty received but invoice not yet in system | Timing lag, not a true mismatch | Hold in pending queue, recheck in 5 business days before escalating |

Example: PO for 22 units at $1,150 ($25,300 total); receiving report confirms 22 units received; invoice bills 22 units at $1,175 each ($25,850). Unit price variance is $25 (>1% tolerance) — hold payment, route to AP with note: "invoice unit price $1,175 vs. PO $1,150, variance $25/unit ($550 total), request corrected invoice or vendor confirmation of price change with documentation."

## 4. Split-purchase detection check

Run monthly against p-card statement, or immediately when two invoices from the same vendor land in the same week:

```
Flag if: same vendor + transactions within same day (or same week for invoice-based buys)
         AND sum of transactions > single-transaction cap
```

| Vendor | Date | Amount | Card limit | Cumulative same-day/vendor total | Flag |
|---|---|---|---|---|---|
| Office Supply Co | 3/14 | $2,400 | $2,500 | $2,400 | No |
| Office Supply Co | 3/14 | $2,150 | $2,500 | $4,550 | **Yes — split purchase, no exception** |
| Tech Distributors | 3/10 | $2,300 | $2,500 | $2,300 | No |
| Tech Distributors | 3/12 | $2,450 | $2,500 | $4,750 (same week) | **Yes — escalate, review both transactions together** |

Action on flag: do not approve or process either transaction independently — combine into a single requisition retroactively reviewed against the correct threshold and document the finding (no-exception rule per SKILL.md's Mental models).

## 5. Sole-source / single-quote justification memo template

Use only when one of the four conditions is met — fill the template with the actual condition cited, not a paraphrase of vendor preference:

```
Requisition #: <ID>
Vendor: <name>          Amount: <$>
Condition claimed (check exactly one):
  [ ] (a) Item available from only one source — attach market-scan evidence
  [ ] (b) Public exigency/emergency — attach dated description of the exigency
  [ ] (c) Funding agency authorized noncompetitive procurement in writing — attach authorization
  [ ] (d) Competition solicited in good faith and failed — attach solicitation record and no-bid/no-response documentation
Cost/price analysis attached (required if amount > org trigger): <yes/no, attach>
Approving official: <name, title>
```

Reject-and-return trigger: if none of (a)–(d) is checked with attached evidence, the requisition is not sole-source — reroute to RFQ/RFP per Section 2 regardless of the requester's stated preference.

## 6. Maverick-spend / on-contract logging

Log every completed transaction against the running compliance rate:

```
Running off-contract rate = (off-contract $ this period) ÷ (total procurement $ this period)
```

| Threshold | Status |
|---|---|
| < 5% | In control — no action |
| 5%–20% | Investigate which categories are drifting off-contract, flag to purchasing manager |
| > 20% | Contract compliance program is not functioning — escalate as a program-level finding, not a transaction-level one |

Compare against the reported cross-organization average of ~59.5% off-contract compliance (i.e., ~40.5% on-contract) as a reality check: if your own off-contract rate isn't being tracked at all, assume it is closer to the average than to the <5% benchmark until measured.
