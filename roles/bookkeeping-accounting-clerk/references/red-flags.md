# Red flags — what a bookkeeping/accounting clerk notices instantly

Smell tests with thresholds. Format per flag: signal → what it usually means → first question → data to pull.

### Bank reconciliation unmatched difference persists into a second close cycle
- **Usually means:** an item was missed in the "chase" the prior month (often something sitting in the bank feed's "excluded" or "for review" queue), or a duplicate/missing posting that keeps rolling forward instead of getting found.
- **First question:** "What did we assume the difference was last month, and did we ever actually confirm it, or did we carry it forward unresolved?"
- **Data to pull:** prior month's reconciliation worksheet, bank feed excluded/for-review queue, the full bank transaction detail for both months side by side.

### AR invoice open >90 days with no dispute logged
- **Usually means:** either a real collection problem nobody escalated, or the invoice was actually paid and misapplied/unapplied in the system.
- **First question:** "Has anyone actually called this customer, or has it just been sitting on the aging report?"
- **Data to pull:** AR aging detail by customer, payment application history, any correspondence log tied to the invoice.

### Same recurring journal entry posts to the same account/class combination two or more periods running with no source-document check
- **Usually means:** a template set up once with an error is propagating silently — nobody re-verifies a recurring entry against its source document after the first posting.
- **First question:** "When was this template last checked against the actual invoice or lease, not just re-approved because it looked the same as last month?"
- **Data to pull:** the recurring transaction template settings, the underlying contract/invoice, three months of postings from that template.

### Invoice quantity or price differs from the PO/receiving report by more than 2% or $50
- **Usually means:** a short shipment, a vendor price increase pushed through without an approved change, or occasionally a data-entry error on the PO itself.
- **First question:** "Did we actually receive what's being billed, at the price we agreed to — pull the receiving report before touching the check register."
- **Data to pull:** PO, receiving report, invoice, any price-change approval on file for that vendor/SKU.

### Same invoice number or amount paid twice within a short window
- **Usually means:** a duplicate entry from a manual re-key plus an automated bank-feed match, or a vendor resubmitting an invoice that was already processed under a different reference number.
- **First question:** "Pull both payments — are they actually the same invoice, or two legitimately similar ones?"
- **Data to pull:** AP payment history filtered by vendor and amount, check/ACH register, the two invoices side by side.

### Petty cash count doesn't match the log balance
- **Usually means:** an unlogged disbursement, a receipt filed but not entered, or (less often but not to be dismissed) cash handling outside the log entirely.
- **First question:** "What's the last logged transaction, and does the physical receipt pile match everything since then?"
- **Data to pull:** petty cash log, receipt envelope/folder, prior period's reconciled count.

### NSF/returned customer check not re-invoiced or written off within 30 days
- **Usually means:** the bounce got recorded as a cash reduction but nobody closed the loop on the customer's receivable or the returned-item fee.
- **First question:** "Has this customer been re-billed for the amount and the return fee, or is this just sitting as an unresolved cash difference?"
- **Data to pull:** returned-item notice from the bank, customer's AR balance, any prior history of NSF from the same customer.

### Journal entry posted directly to a subledger control account (AR/AP/cash) instead of through the subledger
- **Usually means:** someone bypassed the module to save time, which breaks the tie-out between the subledger total and the GL control balance — the two will no longer agree until it's found.
- **First question:** "Why did this go in as a direct JE instead of through AP/AR — was there a transaction type the subledger couldn't handle, or was this a shortcut?"
- **Data to pull:** the JE detail and preparer, subledger-to-control variance report for the period.

### A department/location's expense line moves >15% month over month with no known operational cause
- **Usually means:** a miscoding (especially a Class/location dimension error on a multi-location chart of accounts), not an actual change in spend.
- **First question:** "Is this a real change in activity, or did something get coded to this location that belongs somewhere else?"
- **Data to pull:** transaction detail behind the line for the month, the same account for the prior three months, any recurring template touching that account.

### New vendor added with a bank routing number or address matching an existing employee
- **Usually means:** most often an honest mix-up (an employee's side business, a shared family address); occasionally a fraud setup — either way it needs a documented check before the first payment goes out, not after.
- **First question:** "Has anyone independently verified this vendor's bank details against something other than the form the vendor submitted?"
- **Data to pull:** vendor master file change log, employee address/direct-deposit records, the vendor onboarding form and its approver.

### Sales tax liability account balance doesn't match tax collected per POS/register report
- **Usually means:** a POS integration sync gap, a manual journal entry that touched the tax liability account directly, or a location applying the wrong tax rate.
- **First question:** "Reconcile the tax liability account to the register tape total for the period before assuming either number is right."
- **Data to pull:** POS/register tax-collected report by location, tax liability account detail, remittance filings for the period.
