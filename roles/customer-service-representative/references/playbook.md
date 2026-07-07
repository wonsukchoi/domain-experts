# Customer Service Representative — Playbook

## Discretion-authority table (filled example)

| Action | Front-line agent | Senior agent | Supervisor |
|---|---|---|---|
| Refund up to | $100 | $300 | $1,000 |
| Goodwill credit up to | $50 | $150 | $500 |
| Free-shipment waiver | 1 order | 3 orders | Unlimited, time-boxed |
| Contract/SLA exception | Not authorized | Not authorized | Case-by-case |
| Account cancellation with retention offer | Not authorized | Up to $200 offer | Unlimited |

Rule of thumb: if the total ask across all components exceeds your threshold by any amount, escalate the whole request rather than approving the parts you can and declining the rest — a partial approval on a single connected ask (e.g. refund yes, credit no) often reads to the customer as worse than a clean escalation with a fast turnaround.

## Root-cause tagging taxonomy

Every closed ticket gets exactly one root-cause tag, chosen from:

- `product-defect` — something was broken or didn't work as designed
- `process-failure` — the product worked, but a business process failed (missed SLA, wrong item shipped, billing error)
- `expectation-mismatch` — no promise was broken; the customer expected something the product/policy never offered
- `information-gap` — the customer didn't know something that was documented (self-service deflection opportunity)
- `abuse-pattern` — request appears to exploit policy rather than reflect a genuine issue

`process-failure` and `product-defect` tags roll up weekly to the team that owns the underlying system — a single agent fixing the same `process-failure` ticket ten times a week without it surfacing upstream is the ticketing system failing at its second job (pattern detection), not just resolving individual complaints.

## Escalation write-up template (filled example)

```
ESCALATION: Ticket #48213
Customer: [Name], account since 2022-11, ~$1,020/yr order volume
Ask: Full refund ($85) + goodwill credit ($50) + 3 free expedited shipments (~$45) = $180 total
Root cause: process-failure (carrier missed guaranteed delivery window)
Recommendation: APPROVE — total ask is 4.4% of estimated $4,080 LTV;
  failure was ours, not a preference mismatch; account has zero prior
  refund/credit history (checked account tags 2022-11 to present).
Discretion needed: exceeds my $100/$50/1-shipment thresholds; total request $180 > my $150 combined cap.
```

A recommendation with a number attached (LTV estimate, prior-history check already done) gets approved faster than a bare forward — it does the supervisor's diligence for them instead of asking them to redo it.

## Handoff script (warm transfer, filled example)

> "I'm bringing in [Name] from billing who can adjust the recurring charge directly — [Name], this is [Customer], their March invoice double-charged them $34.50 due to a proration error on the plan change from the 12th. I've already confirmed the double-charge in the billing log, they just need the credit applied — [Customer], you won't need to re-explain what happened."

The test for a warm handoff: the customer should not have to repeat the core facts of their issue to the next person. If they do, the transfer failed regardless of whether the eventual answer was correct.

## Customer Effort Score (CES) diagnostic table

| CES (1=low effort, 5=high effort) | Ticket marked | Diagnosis |
|---|---|---|
| 1–2 | Resolved | Genuine first-contact resolution — no action needed |
| 3 | Resolved | Borderline — check touch count; 2 touches may still be acceptable |
| 4–5 | Resolved | Contradiction — pull full contact history; likely mislabeled or routing-broken |
| 4–5 | Escalated/pending | Expected if genuinely complex — check against SLA, not CES |

A high CES on a ticket the system calls "resolved" is the strongest single signal that the resolution metric itself is being gamed (closing tickets to hit a resolution-rate target rather than because the issue is actually fixed).
