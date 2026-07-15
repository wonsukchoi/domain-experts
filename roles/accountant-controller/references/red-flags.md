# Red flags — what a controller notices instantly

Smell tests with thresholds. Format per flag: the signal → what it usually means → first question to ask → data to pull. Any single one can be innocent; two or three together are a pattern.

## Close and reconciliation

### Close calendar slipping (e.g., day 8 close creeping to day 15 over 3+ months)
- **Usually means:** accounting is under-resourced for current transaction volume, or a system change broke a previously automated step.
- **First question:** "Which specific checklist step is taking longer, and since which period?"
- **Data to pull:** close calendar actuals for the trailing 6 months, ticket/system-change log for the accounting stack.

### A reconciling item sitting in a suspense or clearing account for 2+ periods
- **Usually means:** someone plugged a variance instead of tracing it, or a process (e.g. inventory receiving) has a systematic timing gap nobody's fixed.
- **First question:** "What was the original transaction that created this entry, and why hasn't it cleared?"
- **Data to pull:** suspense account activity detail, aging of unresolved items by age bucket.

### Manual (top-side) journal entries above $10K posted outside the standard sub-ledger flow
- **Usually means:** a system limitation being worked around, or — less innocently — an override to hit a target number.
- **First question:** "Walk me through why this couldn't be entered through the normal AP/AR/inventory process."
- **Data to pull:** top-side JE log with preparer/approver, frequency by preparer, dollar total by month.

### Post-close adjusting entries recurring in the same account every period
- **Usually means:** the underlying sub-ledger process has a structural error that's being corrected after the fact instead of fixed at the source.
- **First question:** "Why does this same account need a correction every month — what breaks it?"
- **Data to pull:** adjusting entry log by account for the trailing 4 quarters, the sub-ledger process document for that account.

## Revenue and receivables

### Revenue recognized before delivery, acceptance, or the performance obligation is satisfied
- **Usually means:** sales pressure to book revenue in the current period regardless of ASC 606 timing, or a genuine misunderstanding of when control transfers.
- **First question:** "What contractual milestone or delivery event triggers recognition here, and has it actually occurred?"
- **Data to pull:** the contract's performance obligations and acceptance terms, shipping/delivery confirmation, signed acceptance if required.

### DSO up >15% quarter-over-quarter with no change to standard billing terms
- **Usually means:** collections discipline slipping, disputed invoices accumulating, or non-standard payment terms granted informally.
- **First question:** "Show me the five largest invoices past 60 days and why each is unpaid."
- **Data to pull:** AR aging by customer, dispute log, any side-letter or non-standard terms granted in the last two quarters.

### A single customer crossing 20% of AR or 25% of revenue
- **Usually means:** concentration accreted without anyone deciding it should — now a solvency and disclosure risk, not just a sales win.
- **First question:** "What's our exposure if this customer goes 90 days slow-pay, and does it need disclosure?"
- **Data to pull:** contract terms and renewal date, payment history trend, concentration-related disclosure requirements.

## Expenditure and controls

### A three-way match mismatch overridden to make a payment run
- **Usually means:** a genuine receiving delay being paid around, or a control being bypassed under deadline pressure to avoid a vendor escalation.
- **First question:** "Which leg didn't match, and who approved paying anyway?"
- **Data to pull:** the PO, receiving record, and invoice side by side; override-approval log for the payment run.

### The same person initiating a payment and reconciling the account it clears against
- **Usually means:** a genuine segregation-of-duties gap, most often from headcount constraints rather than intent.
- **First question:** "Is there a compensating control — independent review of the bank statement or the payment log?"
- **Data to pull:** the access/role matrix in the ERP, evidence of any compensating review.

### AP days stretching >10 days beyond stated terms with no negotiated change
- **Usually means:** cash is being quietly managed by sitting on bills, which is either an unflagged liquidity issue or an AP process breakdown — either way, discovered from the balance sheet instead of from the team.
- **First question:** "Are we paying slow on purpose? Who decided, and which vendors are affected?"
- **Data to pull:** AP aging, vendor credit-hold or complaint notices, disbursement assumptions vs. actuals.

## Estimates and disclosure

### An estimate (allowance, accrual, useful life) that hasn't been revisited in 4+ quarters despite changed underlying facts
- **Usually means:** the estimate is stale — carried forward by habit rather than re-derived from current data.
- **First question:** "What data was this estimate built on, and is that data still current?"
- **Data to pull:** the original support for the estimate, current actuals it should be re-tested against (e.g. actual bad-debt write-offs vs. the allowance rate).

### A related-party transaction processed through the standard vendor/customer workflow with no separate flag
- **Usually means:** the relationship wasn't disclosed to accounting, or the disclosure requirement was overlooked — both are a control and reporting problem.
- **First question:** "Is this counterparty related to an officer, director, or major shareholder, and is that documented anywhere?"
- **Data to pull:** vendor/customer master list cross-referenced against known related parties, board minutes referencing related-party approvals.

### EBITDA or earnings "adjustments" exceeding 20% of reported EBITDA during diligence prep
- **Usually means:** the earnings figure is being engineered for a transaction narrative rather than reflecting sustainable, cash-backed performance.
- **First question:** "Walk me through each addback — which would a buyer's quality-of-earnings review disallow?"
- **Data to pull:** monthly (not quarterly) revenue and expense detail for 24 months, addback support schedules, any rev-rec policy changes in the last two years.
