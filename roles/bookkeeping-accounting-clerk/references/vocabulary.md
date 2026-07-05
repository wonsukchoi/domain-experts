# Bookkeeping working vocabulary

Terms a clerk uses daily and precisely. Format: definition → how a practitioner says it → common misuse.

**Reconciling item** — A specific, named difference between two balances that should agree (bank vs. book, subledger vs. control account), each traceable to a document.
In use: "Two reconciling items left: an outstanding check and a bank fee — once those post, we tie."
Misuse: using it as a catch-all label for "the unexplained difference," which is the opposite of the term's purpose — every reconciling item has to be a specific, named thing, not a placeholder for one.

**Outstanding check vs. deposit in transit** — Outstanding check: written and recorded in the books, hasn't cleared the bank yet. Deposit in transit: recorded and deposited, hasn't been credited by the bank yet (a timing lag, usually 1 business day).
In use: "Three outstanding checks and one deposit in transit account for the whole gap — nothing left to chase."
Misuse: treating a deposit in transit older than a few business days as still "in transit" without checking — past that window it's usually a posting error, not timing.

**Suspense account** — A temporary holding account for a transaction that can't yet be classified correctly, used deliberately and cleared quickly.
In use: "It's sitting in suspense for 48 hours while I confirm which vendor it belongs to."
Misuse: using it as a permanent parking spot for anything that doesn't reconcile — a suspense balance that's been open for a full close cycle is a red flag, not a solution.

**Three-way match** — Comparing the purchase order, the receiving report, and the vendor invoice independently before releasing payment; all three must agree on quantity and price.
In use: "Three-way match failed on quantity — receiving shows 480 units, invoice bills 500."
Misuse: calling it a "match" when only the invoice and PO were compared — skipping the receiving report defeats the entire purpose, since that's the only document confirming the goods actually arrived.

**Accrual vs. cash basis** — Accrual: revenue/expense recorded when earned/incurred, regardless of when cash moves. Cash basis: recorded when cash actually changes hands.
In use: "We accrued the March utility bill even though it won't be paid until April — it belongs to March's expenses."
Misuse: assuming "we haven't paid it yet" means it isn't an expense for the period — under accrual accounting, timing of cash has nothing to do with which period the expense belongs to.

**Cutoff** — The rule for which period a transaction belongs to, based on when the underlying event (shipment, receipt, service performed) occurred, not when it was entered into the system.
In use: "That invoice is dated 4/2 but the goods arrived 3/30 — cutoff says it's a March accrual."
Misuse: using the invoice date or entry date as the deciding factor instead of the date the actual economic event happened.

**Subledger vs. control account** — The subledger (AR aging, AP aging) holds transaction-level detail; the control account is the single summarized balance in the general ledger that should always equal the subledger's total.
In use: "AP subledger total is $420 under the control account — someone posted a credit memo straight to the GL without touching the subledger."
Misuse: treating a subledger-to-control variance as a rounding issue rather than proof that a transaction bypassed the normal entry path.

**Debit memo vs. credit memo** — A credit memo reduces what's owed (issued by a vendor to you, or by you to a customer); a debit memo increases what's billed, or documents a formal short-pay/dispute against a vendor.
In use: "We're issuing a debit memo to Bellwether for the 20 lb short-ship instead of just paying the invoice as billed."
Misuse: using "credit" and "debit" memo interchangeably with the double-entry terms debit/credit — the memo direction depends on who's issuing it and which side of the relationship it adjusts, not on which account gets debited in the underlying entry.

**NSF (non-sufficient funds)** — A customer's check or ACH payment bounced because their account lacked funds; the deposit gets reversed and typically triggers a bank fee.
In use: "That $1,325 deposit reversed as NSF — reinstate the customer's receivable and add the return fee."
Misuse: recording the cash reversal without reinstating the customer's AR balance, which understates what the customer actually still owes.

**Float** — The delay between when a payment is recorded/sent and when it actually clears and affects the bank balance.
In use: "Payroll float means the book balance drops Thursday but the bank doesn't clear it until Monday — don't panic at the gap."
Misuse: confusing float (a normal, explainable timing lag) with an actual reconciling error — a repeating, predictable float pattern doesn't need investigating every period, an unexplained one does.

**Class / location (dimension) tracking** — A tag on a transaction (separate from the account itself) that attributes it to a department, location, or business unit for internal P&L reporting.
In use: "The account was right — Equipment Lease — but the Class was wrong, so it hit Loc 2's P&L instead of Production's."
Misuse: checking only that the account is correct and ignoring the Class/location field, which is exactly where multi-location miscoding actually happens.

**Adjusting journal entry (AJE) vs. reclass** — An AJE changes a reported financial result for a period (an accrual, a correction to a prior misstatement); a reclass moves an amount between accounts or classes with no net income or cash impact.
In use: "That's a reclass, not an AJE — it moves the $2,150 from Loc 2 to Production, net income for the company doesn't change."
Misuse: labeling every correcting entry an "adjustment" without distinguishing whether it actually changes reported income, which affects who needs to approve it.

**Period lock** — A control setting that prevents new entries or edits to a closed accounting period without an explicit unlock and log entry.
In use: "March is locked — if that reclass needs to go into March, it needs the controller to unlock it first, logged."
Misuse: treating the lock as a formality to work around quietly rather than a control that exists specifically to prevent silent changes to closed numbers.

**Aging schedule** — A report bucketing open AR or AP balances by how long they've been outstanding (e.g., current, 31–60, 61–90, 90+ days).
In use: "Nothing new in the 90+ bucket this month, but two invoices just rolled into 61–90 — worth a call before they age further."
Misuse: reading the aging total only, without checking which specific invoices moved between buckets — the total can look flat while individual accounts are quietly deteriorating.
