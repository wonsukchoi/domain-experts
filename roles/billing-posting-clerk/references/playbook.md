# Billing and Posting Clerk — Playbook

## Cash-application worked table

Wire received: $4,230.00. Open invoices for the account:

| Invoice | Original amount | Contract adjustment | Adjusted amount | Applied | Remaining |
|---|---|---|---|---|---|
| #10456 | $2,850.00 | none | $2,850.00 | $2,850.00 | $0.00 |
| #10461 | $1,750.00 | 2% volume rebate = $35.00 | $1,715.00 | $1,380.00 | $335.00 |
| **Total** | **$4,600.00** | **$35.00** | **$4,565.00** | **$4,230.00** | **$335.00** |

Check: $2,850.00 + $1,380.00 = $4,230.00 — matches the wire exactly. Remaining balance across both invoices after the correct rebate: $4,565.00 − $4,230.00 = $335.00.

## Remittance-matching procedure

1. Pull the remittance advice (email, check stub, wire memo, or portal-generated backup) attached to the payment.
2. List every invoice number and dollar amount the remittance cites.
3. Sum the cited amounts; compare to the actual payment received. If they match, apply per the remittance and stop.
4. If they don't match (as above), recompute any cited adjustment (discount, rebate, dispute credit) against the contract terms — do not assume the customer's math is correct.
5. If no remittance exists, check for a pattern: same customer, same dollar or percentage gap, repeating cycle-over-cycle → likely a contract term the billing system isn't applying. One-off, no pattern → hold in suspense, open a research ticket, contact AP.
6. Never split an unexplained shortfall proportionally across multiple invoices by default — it hides which invoice actually has the problem.

## Aging-report triage checklist

| Bucket | Default action | Escalation trigger |
|---|---|---|
| 0-30 days | No action — normal cycle | N/A |
| 31-60 days | Automated reminder; clerk confirms invoice was actually delivered (not lost in a portal upload failure) | Same invoice reappears at 31-60 after having been "resolved" |
| 61-90 days | Clerk calls AP contact directly; confirm dispute status | No response after 2 contact attempts in 10 business days |
| 91+ days | Refer to credit manager for write-off or collections decision; clerk does not authorize either | Any single invoice over $10,000 — refer at 61 days, not 91 |

For every item crossing a bucket boundary, log the specific cause (delivery failure, dispute, cash-flow issue, approval-queue delay) — an aging report that only shows dollar-and-days without cause can't be triaged by anyone reviewing it later.

## Credit-memo authorization checklist

Before processing any credit memo:

- [ ] Original invoice number and line item(s) being credited identified
- [ ] Business reason documented (return, pricing error, service failure, negotiated concession) and matches a category in policy
- [ ] Amount reconciles to the original invoice line, not a round-number estimate
- [ ] For amounts over the clerk's authorization limit (commonly $500-$1,000, set by firm policy), supervisor sign-off obtained before posting
- [ ] Credit applied to the correct invoice, not the account balance generally, so the aging report reflects which invoice was adjusted
