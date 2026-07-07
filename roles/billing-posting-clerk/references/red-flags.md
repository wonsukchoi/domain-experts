# Billing and Posting Clerk — Red Flags

### Same-dollar-amount short payment repeats 2+ cycles running
- **Usually means:** a contract-rate exception (discount, rebate tier, proration) the billing system isn't applying, so the customer keeps self-correcting the same gap.
- **First question:** does the contract's amendment history show a rate exception dated before the first short payment?
- **Data to pull:** contract file, rate-schedule change log, prior three invoices for the account.

### Payment amount exceeds all open invoices combined
- **Usually means:** either a duplicate/advance payment, or the customer is prepaying against a future invoice.
- **First question:** did the customer's remittance advice specify "prepayment" or a future invoice number?
- **Data to pull:** remittance advice, customer's payment history for prior overpayments.

### Credit memo requested with no invoice number cited
- **Usually means:** either a legitimate dispute the requester hasn't fully documented yet, or an attempt to get an unearned credit processed on the strength of a relationship rather than a fact pattern.
- **First question:** what specific invoice and line item is this credit against?
- **Data to pull:** original invoice, any prior correspondence referencing a dispute.

### Aging bucket clears without a matching cash-receipt entry
- **Usually means:** a write-off or an unapplied-cash sweep cleared the balance, not an actual payment — the account is not actually current.
- **First question:** is there a cash-receipt transaction dated to match the clearing date?
- **Data to pull:** cash-receipts journal, write-off approval log.

### Invoice total doesn't match a manual recalculation from the rate schedule
- **Usually means:** the billing system applied a stale or default rate instead of the customer's negotiated rate.
- **First question:** when was this customer's rate schedule last updated in the system, and does that date match the current contract?
- **Data to pull:** system rate-table entry, signed contract/amendment, prior invoice for rate-consistency check.

### Same customer disputes 3+ invoices in a rolling 6-month window
- **Usually means:** either a systemic billing error the customer keeps catching one invoice at a time, or a relationship/collections issue being expressed through repeated disputes.
- **First question:** are the disputes about the same line item/charge type each time, or different each time?
- **Data to pull:** dispute log for the account, invoice history, account-management notes.

### Suspense/unapplied-cash account balance grows month over month
- **Usually means:** payments are being held instead of researched and applied — a backlog is forming, not a research queue being worked.
- **First question:** what's the average age of items currently in suspense?
- **Data to pull:** suspense-account aging, count of items over 30 days unresolved.

### A large balance write-off is requested without a documented collections attempt
- **Usually means:** either genuine uncollectibility that hasn't been documented yet, or an attempt to clear a balance without going through the credit-manager approval chain.
- **First question:** what collections steps (calls, letters, referral) are on file for this account?
- **Data to pull:** collections-contact log, credit-manager approval history for prior write-offs at this account.
