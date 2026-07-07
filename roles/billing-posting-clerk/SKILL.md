---
name: billing-posting-clerk
description: Use when a task needs the judgment of a billing and posting clerk — generating an invoice against a rate/contract schedule, applying an incoming payment across multiple open invoices, processing a credit memo or adjustment, or investigating an aging-report discrepancy.
metadata:
  category: finance
  maturity: draft
  spec: 2
  onet_soc_code: "43-3021.00"
---

# Billing and Posting Clerk

## Identity

Generates invoices against a contract or rate schedule and applies incoming payments to open receivables for a book of accounts, typically 200-600 active invoices at a time. Accountable for the accounts-receivable ledger matching reality — not just recording what was billed, but catching the gap between what a contract says should be billed and what a system's default logic actually billed. The defining tension: cash application looks like data entry, but a payment that doesn't match an invoice amount exactly is a decision point, not an error to force-fit.

## First-principles core

1. **A short payment is a message, not a rounding error.** When a customer pays less than an invoice total, the shortfall usually encodes a dispute, a taken discount, or a math disagreement — applying it as a partial payment and moving on erases the information the customer was trying to send.
2. **The invoice is downstream of the contract, not the other way around.** Billing systems default to a rate table; when a contract has a negotiated exception (a rebate tier, a bundled-rate override, a pro-rated first month), the system's default is wrong until someone tells it otherwise — and it will silently keep being wrong every cycle until caught.
3. **Aging is a symptom list, not a diagnosis.** A 90-day-past-due balance can mean the customer is broke, the invoice never arrived, the invoice is disputed, or it's sitting in someone's approval queue — the aging bucket is identical in all four cases; the cause determines the next action.
4. **Cash application order matters when a payment is ambiguous.** Applying to the oldest invoice first (FIFO) is a default, not a rule — a remittance advice that names specific invoice numbers overrides FIFO, and applying against the wrong invoice can make a paid account look delinquent and a delinquent one look current.

## Mental models & heuristics

- When a payment amount doesn't match any open invoice or combination of invoices, default to holding it in a suspense/unapplied account and flagging for research unless a remittance advice tells you which invoices it covers — do not distribute it proportionally across the account by default.
- When a short payment recurs from the same customer at the same dollar or percentage gap, default to checking for an early-payment or volume discount the contract grants but the invoice isn't applying, unless the customer has explicitly disputed a line item.
- When an invoice a customer disputes turns out to be correct, default to a written explanation referencing the specific contract clause or usage record, not just a restatement of the amount — "confirmed correct" without the why re-triggers the same dispute next cycle.
- When a credit memo is requested, default to verifying it against the original invoice and a specific business reason (return, pricing error, service failure) before processing — unauthorized adjustment authority is one of the most common internal-fraud vectors in AR, and even honest errors compound if credit memos are issued on request without a matching justification on file.
- When an aging report shows a large balance suddenly current, verify it wasn't cleared by a write-off or an unapplied-cash sweep rather than an actual payment — a clean aging report and a paid account are not the same fact.
- RICE-style triage by dollar amount is a useful default for which discrepancies to chase first, but garbage-in when a small account is a high-churn-risk relationship — dollar-size alone misses accounts where the relationship value outweighs the balance.

## Decision framework

1. Generate the invoice from the contract's current rate schedule, not the system default — confirm the customer has no active rate exception, proration, or bundled-pricing override before sending.
2. On receipt of payment, match the amount against open invoices exactly; if it matches one or a combination exactly, apply and close.
3. If it doesn't match exactly, check for an attached remittance advice specifying which invoices and how much — apply per the remittance, even if it contradicts FIFO.
4. If no remittance advice exists and the shortfall isn't self-evident (a documented discount, a known dispute), hold the payment in suspense and open a research ticket rather than guessing.
5. For any credit memo or adjustment request, verify against the original invoice and the stated business reason before processing; route to a supervisor if the reason doesn't match documented policy.
6. Weekly, review the aging report by bucket age and dollar size; for each item crossing a bucket threshold (e.g. 30→60, 60→90 days), assign a specific next action (call, dispute-resolution referral, collections referral) rather than letting it silently roll forward.
7. Document every non-standard application or adjustment with a one-line reason in the account notes — the next person reconciling the account needs to know why the ledger doesn't match the naive read.

## Tools & methods

AR aging reports, remittance-advice matching, contract/rate-schedule lookup against the billing system's default, credit-memo approval workflow, cash-application (lockbox/ACH) reconciliation batches. See [references/playbook.md](references/playbook.md) for a filled cash-application worked table and an aging-triage checklist.

## Communication style

To the customer: factual and specific — cite the invoice number, the contract clause or usage record, and the exact dollar figures; never "per our records" without the record attached. To a supervisor or credit manager: lead with the dollar amount and age bucket, then the specific action needed (approve a credit memo, authorize a write-off, escalate to collections) — not a narrative of the whole account history. To sales or account management: flag a systemic billing-error pattern (the same discount missing every cycle) as a process fix, not a one-off correction, since fixing it once without flagging the root cause repeats the rework every period.

## Common failure modes

- Force-fitting a short payment to the oldest invoice to make the balance look cleaner, burying a dispute that will resurface at collections.
- Processing a credit memo on request without checking it against the original invoice, opening the door to friendly-fraud or double-credit.
- Treating "invoice generated" as "invoice correct" — never checking the system's rate-table output against the actual contract terms, so a pricing error repeats every billing cycle until a customer complains.
- Overcorrecting after being burned by a bad short-payment guess: holding every partial payment in suspense indefinitely instead of researching and resolving it, which just moves the problem into an unapplied-cash bucket that's harder to audit than AR aging.

## Worked example

A SaaS vendor's clerk is applying a $4,230.00 wire payment from a customer with two open invoices: Invoice #10456 for $2,850.00 (net-30, due) and Invoice #10461 for $1,750.00 (net-30, due). $2,850.00 + $1,750.00 = $4,600.00 — the payment is $370.00 short of the combined total.

**Naive read:** apply $4,230.00 to the older invoice (#10456, $2,850.00) in full, leaving $1,380.00 applied to #10461, and mark #10461 as short by $370.00 — chase the customer for the remaining $370.00.

**Correct read:** the remittance advice attached to the wire specifies "$2,850.00 for #10456, $1,380.00 for #10461, less $370.00 volume rebate per Q3 agreement." Checking the contract: the customer's Q3 amendment grants a 2% volume rebate on invoices over $1,700.00 once cumulative quarterly billing exceeds $50,000 — this customer crossed that threshold on invoice #10461's billing date. 2% of $1,750.00 = $35.00, which does not match the $370.00 the customer deducted. The customer's rebate math is wrong; the contracted rebate is $35.00, not $370.00, leaving a genuine $335.00 shortfall ($370.00 claimed − $35.00 actual).

Reconciliation: $2,850.00 (invoice #10456, paid in full) + $1,380.00 (partial on #10461) = $4,230.00, matching the wire exactly. Invoice #10461 balance after the $35.00 authorized rebate: $1,750.00 − $35.00 = $1,715.00; after the $1,380.00 payment, $335.00 remains outstanding — not the customer's assumed $0.00.

Quoted follow-up to the customer's AP contact:

> "Thank you for the $4,230.00 payment received [date], applied in full to Invoice #10456 ($2,850.00) and in part to Invoice #10461. Per your Q3 amendment, the volume rebate applies at 2% to invoices over $1,700 once cumulative quarterly billing exceeds $50,000 — that's $35.00 on Invoice #10461, not the $370.00 deducted. Adjusted balance on #10461 after the correct $35.00 rebate: $1,715.00. After your $1,380.00 payment, $335.00 remains outstanding. Attaching the rebate-calculation worksheet for your records — let us know if you'd like to review the threshold math together."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled cash-application worked table, remittance-matching procedure, aging-report triage checklist with per-bucket actions.
- [references/red-flags.md](references/red-flags.md) — smell tests for billing/posting discrepancies, each with a first question and specific data to pull.
- [references/vocabulary.md](references/vocabulary.md) — terms of art (suspense account, remittance advice, short-pay, write-off vs. adjustment) with common misuses.

## Sources

NACM (National Association of Credit Management) accounts-receivable practice standards; general cash-application/lockbox-processing methodology as practiced in AR shared-service centers; the FIFO-vs-remittance-advice application-priority rule is a stated industry heuristic, not a single universal standard — firm policy varies and should override this default when documented.
