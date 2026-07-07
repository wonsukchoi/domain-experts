# Billing and Posting Clerk — Vocabulary

### Remittance advice
The document (email, check stub, wire memo, or portal export) accompanying a payment that specifies which invoice(s) it covers and any deductions taken.
**In use:** "The wire came in short, but the remittance advice shows they took the volume rebate — let's check if the rebate math is right before chasing the balance."
**Common misuse:** Treated as optional or skippable when a payment doesn't match an invoice exactly — without it, applying a mismatched payment is a guess, not a reconciliation.

### Short-pay
A payment received for less than the invoiced amount, whether disputed, discounted, or simply short by error.
**In use:** "That's the third short-pay from this account on the same line item — time to check if our system is applying an old rate."
**Common misuse:** Assumed to always mean the customer is stalling — a recurring short-pay is more often a data problem on the vendor's side than a delay tactic.

### Suspense account (unapplied cash)
A holding account for payments received but not yet matched to a specific invoice, used when the correct application isn't clear.
**In use:** "Don't force this payment onto the oldest invoice — put it in suspense and open a research ticket since the amount doesn't match anything on the account."
**Common misuse:** Used as a place to park anything confusing indefinitely rather than a queue that gets researched and cleared within days.

### Write-off vs. adjustment
A write-off removes a balance from the books as uncollectible (a credit-manager/finance decision); an adjustment corrects a billing error (a clerk-level correction within authorization limits).
**In use:** "This isn't a write-off — it's an adjustment, because we billed the wrong rate, not because the customer can't pay."
**Common misuse:** Used interchangeably; conflating them misclassifies why a balance changed and can hide a systemic billing error inside what looks like a routine bad-debt write-off.

### Aging report
A report bucketing open receivables by how many days past due they are (e.g., current, 31-60, 61-90, 91+).
**In use:** "The aging report shows $40K in the 61-90 bucket, but half of that is one disputed invoice, not five slow-paying customers."
**Common misuse:** Read as a list of customers who "aren't paying" rather than a list of balances needing a specific next action — dispute, delivery-failure, cash-flow issue, and approval-delay all look identical on the report.

### Volume rebate / tiered discount
A contract term that reduces price once a customer's cumulative purchases cross a defined threshold within a period.
**In use:** "They crossed the $50K quarterly threshold on this invoice, so the 2% rebate kicks in starting here, not retroactively on prior invoices."
**Common misuse:** Assumed to apply retroactively to all invoices in the period unless the contract explicitly says so — most tiered discounts apply prospectively from the crossing point forward.

### Proration
Adjusting a billed amount to reflect a partial period (e.g., a service that started mid-cycle).
**In use:** "The first invoice should be prorated for 12 days, not billed at the full monthly rate — check the start date against the billing-cycle anchor."
**Common misuse:** Skipped when a new account is set up mid-cycle, producing a full-rate first invoice that's wrong by construction and guaranteed to trigger a dispute.

### FIFO application (first-in, first-out)
The default rule of applying a payment to the oldest open invoice first when no remittance advice specifies otherwise.
**In use:** "No remittance came with this check, so we're applying FIFO — oldest invoice first."
**Common misuse:** Applied even when a remittance advice explicitly names different invoices — FIFO is the fallback for ambiguous payments, not a rule that overrides explicit instructions.

### Credit memo
A document reducing an amount owed on a specific invoice, issued for a documented reason (return, pricing error, service failure, negotiated concession).
**In use:** "I can't process a credit memo without an invoice number and a reason code — which line item is this against?"
**Common misuse:** Issued on request without verifying against the original invoice, which is one of the most common vectors for both honest billing errors and deliberate account manipulation to compound undetected.

### Cash application
The process of matching an incoming payment to the specific invoice(s) it satisfies and posting it to close or partially close those invoices.
**In use:** "Cash application on this account is behind by three days — that's why the aging report shows balances that were actually paid last week."
**Common misuse:** Treated as pure data entry; in practice every payment that doesn't match an invoice amount exactly requires a judgment call about which invoice(s) it applies to and why.
