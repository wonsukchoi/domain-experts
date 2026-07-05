# Bookkeeping close & reconciliation playbook — filled templates

Working structures an agent can populate directly. Context throughout: Cascade Coffee Roasters, four retail cafés + wholesale/roastery, QuickBooks Online Advanced, Class = location.

## 1. Month-end close checklist (fixed sequence, day-of-month targets)

| Day | Step | Owner | Gate before moving on |
|---|---|---|---|
| BD 1 | Cut off AP/AR — no new-period entries dated into the closing period | Clerk | All invoices dated ≤ period end are entered |
| BD 1–2 | Bank and credit card reconciliation, every account | Clerk | Adjusted bank balance = adjusted book balance, to the cent |
| BD 2 | Petty cash count vs. log | Clerk | Variance = $0 or written up with a specific cause |
| BD 2–3 | AR aging total tied to AR control account; AP aging total tied to AP control account | Clerk | Variance = $0; any gap traced before proceeding |
| BD 3 | Recurring journal entries reviewed (lease, insurance, depreciation, prepaid amortization) | Clerk | Each entry's Class/account checked against source doc, not carried from template blindly |
| BD 3–4 | Accruals: expenses incurred but not yet invoiced, revenue earned but not yet billed | Clerk + Controller | Each accrual has a specific estimate basis, not a round-number guess |
| BD 4 | Intercompany/inter-location transfers zero out | Clerk | Net to $0 across locations |
| BD 4–5 | Trial balance review — flag any account with no activity that normally has activity, and any balance that moved >20% from prior month with no known cause | Clerk | Every flagged line has a one-line explanation before sign-off |
| BD 5 | Controller review and period lock in QBO | Controller | Period locked; any post-lock edit requires an unlock log entry |

**Rule:** the sequence doesn't reorder under deadline pressure — if BD 5 arrives and the bank rec still doesn't tie, the close doesn't proceed to lock with a plug; it escalates to the controller for a decision on holding the close.

## 2. Bank reconciliation worksheet (filled — March, operating account)

| Item | Amount | Source |
|---|---|---|
| Bank statement balance, 3/31 | $91,547.02 | Bank statement |
| Less: outstanding check #10452 | ($1,200.00) | Check register |
| Less: outstanding check #10458 | ($3,412.75) | Check register |
| Less: outstanding check #10461 | ($890.00) | Check register |
| Add: deposit in transit (3/31 close-out) | $2,150.00 | Register tape / deposit slip |
| **Adjusted bank balance** | **$88,194.27** | |
| Book (GL cash) balance, 3/31 | $89,169.27 | GL |
| Less: bank service charge, not yet recorded | ($45.00) | Bank statement |
| Less: NSF customer check, not yet recorded | ($1,325.00) | Bank statement / returned-item notice |
| Unmatched difference before chase | $395.00 | — |
| Add: missing deposit found in bank-feed "excluded" queue | $395.00 | Processor batch report, Loc 3 |
| **Adjusted book balance** | **$88,194.27** | Ties |

**Chase protocol for an unmatched difference:** (1) confirm every outstanding check and deposit-in-transit against the prior month's rec — carried-forward items older than 60 days get a separate follow-up, they don't just roll again; (2) re-pull the bank's transaction detail for the exact period and diff line-by-line against the GL, not just the totals; (3) check the "excluded" or "for review" queue in the bank feed — auto-match rules silently skip transactions that don't fit the pattern; (4) if still unresolved after (1)–(3) and under $25, escalate for a documented write-off; above $25, does not close until found.

## 3. AP three-way-match worksheet (filled)

| Field | PO #4471 | Receiving report | Invoice | Match? |
|---|---|---|---|---|
| Quantity | 500 lb | 480 lb | 500 lb | No — 20 lb short |
| Unit price | $18.40 | — | $18.75 | No — $0.35 unapproved variance |
| Extended amount | $9,200.00 | — | $9,375.00 | No |
| Approved-to-pay amount | 480 lb × $18.40 = **$8,832.00** | | | Hold $543.00 pending resolution |

**Approval routing by exception size:**

| Discrepancy | Action |
|---|---|
| ≤2% of invoice or ≤$50, whichever is smaller | Clerk may short-pay to the matched amount and note the reason; no sign-off needed |
| >2% or >$50, quantity variance | Route to purchasing/receiving for confirmation of a backorder vs. a receiving error before paying anything |
| >2% or >$50, price variance | Route to whoever holds vendor pricing authority for a signed price-change approval before paying the increase |
| Any variance on a new (<90-day) vendor | Route to controller regardless of size — new-vendor discrepancies get more scrutiny than an established vendor's routine short-ship |

## 4. Expense coding / recurring-template correction (filled)

| Period | Account posted | Correct account | Class posted | Correct class | Amount |
|---|---|---|---|---|---|
| Jan | Rent Expense | Equipment Lease | Loc 2 | Production | $2,150.00 |
| Feb | Rent Expense | Equipment Lease | Loc 2 | Production | $2,150.00 |
| Mar | Rent Expense | Equipment Lease | Loc 2 | Production | $2,150.00 |
| **Total reclass** | | | | | **$6,450.00** |

**Reclassifying journal entry (quoted, one line per period so the audit trail shows the original error and correction, not a single netted entry):**
> Dr Equipment Lease Expense (Production) $2,150.00 / Cr Rent Expense (Loc 2) $2,150.00 — reclass Jan roastery equipment lease, posted to wrong Class at recurring-template setup. Repeat for Feb, Mar. Template corrected 4/1 so April posts to Production automatically.

**Rule:** never net three months into one entry — a reviewer or auditor needs to see each period's original amount and see that the correction is dated and explained, not absorbed into a single unexplained lump.

## 5. Subledger-to-control tie-out (filled, March)

| Subledger | Subledger total | GL control account balance | Variance | Action |
|---|---|---|---|---|
| AR aging | $142,880.00 | $142,880.00 | $0 | Tie — no action |
| AP aging | $88,412.50 | $88,832.50 | $420.00 | Trace before lock — found: a $420 vendor credit memo posted directly to the GL control account without a matching AP subledger entry; corrected by entering the credit memo in the subledger |
