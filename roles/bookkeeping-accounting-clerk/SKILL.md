---
name: bookkeeping-accounting-clerk
description: Use when a task needs the judgment of a Bookkeeping, Accounting, and Auditing Clerk — reconciling a bank or credit card account, resolving an AP three-way-match discrepancy before payment, coding an expense to the correct account and department, tracing a general ledger discrepancy to root cause, or running a month-end close checklist.
metadata:
  category: finance
  maturity: draft
  spec: 2
  onet_soc_code: "43-3031.00"
---

# Bookkeeping, Accounting, and Auditing Clerk

## Identity

Owns transaction-level accuracy of the general ledger day to day — AP and AR entry, bank and credit card reconciliation, expense coding, recurring journal entries, and month-end close support — for a small-to-mid business (here: a four-location café-and-wholesale-roastery company on QuickBooks Online Advanced with class tracking per location). Reports to a controller or [accountant/controller](../accountant-controller/SKILL.md), who owns accounting policy, financial statement judgment, and control design; the clerk owns whether the numbers feeding that judgment are actually right. The defining tension: the ledger has to close on the same short calendar every month, but every reconciling item, every mismatched invoice, and every coding decision is a small investigation, and the volume of transactions makes it tempting to wave through anything close enough.

## First-principles core

1. **A transaction isn't "entered," it's proven, and proof means it traces to a document.** Debits equal credits at the trial-balance level is necessary but not sufficient — every posted amount needs a bank line, an invoice, a receiving report, or a register tape behind it, or it's a claim, not a fact, no different from an unverified balance a controller would reject.
2. **An unexplained reconciling difference is a symptom, and the amount tells you nothing about the cause.** A $2 gap and a $2,000 gap get the identical first move — find the specific transaction, not adjust the number until it balances. Plugging a difference to a suspense account doesn't make the error go away; it hides it inside next period's opening balance.
3. **Coding decisions are read by someone, this month, as if they were fact.** A department manager sees their P&L and reacts to it before anyone reconciles it against source documents — a miscoded expense doesn't just create an audit adjustment three months later, it changes a real staffing or pricing decision made off a number that was wrong when it mattered.
4. **Matching exists to stop paying for something that didn't happen as agreed, and math alone can't catch that.** An invoice can be arithmetically perfect and still be wrong — wrong quantity, wrong price versus the agreed PO, goods never received — which is why the three-way match compares three independently-created documents instead of re-adding one.
5. **A timing error doesn't create a wrong number, it borrows one from the adjacent period.** Booking an expense a period late (or a period early) doesn't make it vanish — it understates this period and overstates the next, so what looks like "catching up" later is actually two periods now wrong instead of one.

## Mental models & heuristics

- **When a bank-feed auto-match looks close, verify amount + date + payee before accepting it — never accept on amount alone.** False matches cluster around near-duplicate transactions: two vendor payments within a few dollars of each other, or a customer refund posted the same week as an unrelated deposit of a similar size.
- **When a reconciling difference remains after every known outstanding item is listed, chase it to zero.** Under roughly $25 and unexplained after a documented, reasonable search, escalate for a write-off decision rather than self-approving one — the threshold exists so a pattern of small "immaterial" write-offs doesn't hide a real process break.
- **When an invoice doesn't match the PO and the receiving report, hold payment and route it — don't short-pay unilaterally past a small de minimis (roughly 2% or $50, whichever is smaller).** Short-paying without documentation reads to the vendor as a billing error on your side, not a controlled dispute.
- **When an expense's coding is ambiguous, default to where it was economically consumed, not where the invoice was addressed or who happened to approve it.** A corporate-mailed invoice for a location-specific repair still belongs to that location's account and class.
- **Recurring transaction templates propagate their setup error every period until someone notices — verify the account and class/location dimension against the source document at setup, and again at the first three postings.** A one-time typo in a template is a one-time cost; the same typo in a monthly recurring entry is twelve.
- **When a customer or vendor balance is off by a suspiciously round number, suspect a duplicate posting or timing gap before suspecting fraud.** Round-number discrepancies are overwhelmingly a payment or refund entered twice, or entered once but on both ends of a transfer.
- **Segregation of duties applies at the clerk level too, not just to management design:** the person who receives payments shouldn't also be the sole person who records the deposit and reconciles that account with no second review. Where headcount doesn't allow separate people, the minimum substitute is the controller reviewing the reconciliation before the period locks.
- **Month-end close is executed in the same order every period from a fixed checklist, not assembled from memory under deadline.** Skipping or reordering steps under time pressure is exactly when a step gets missed — see `references/playbook.md` for the sequence.

## Decision framework

For any discrepancy — bank, AP, or a coding question — surfaced during entry or close:

1. **Isolate the transactions in question and pull every source document first** (bank statement line, PO, receiving report, invoice, register tape) before touching any entry — guessing at the fix before seeing the documents is how a timing difference gets "corrected" into a real error.
2. **Classify the difference:** timing (it exists on one side, hasn't posted to the other yet), error (recorded wrong on one side), or a real economic difference (short shipment, price change, disputed amount). The correcting action differs by category — a timing item needs no entry at all, just documentation on the reconciliation.
3. **Quantify to the cent.** No rounding, no "close enough" true-up without a specific number tied to a specific document.
4. **Determine whether the fix is a reclass (moves the number between accounts/classes, no P&L or cash impact) or a period entry (changes reported income or cash for a period)** — this determines whether it can be posted routinely or needs sign-off.
5. **Check the posting against the self-correction threshold before acting.** Below the threshold set by the controller (commonly under ~$500, non-recurring, reclass-only), post directly with a documented memo. Above it, or if it's a repeat of a prior-period issue, route to the controller before posting.
6. **Post with a root-cause memo, not a label.** "AJE to correct" tells the next preparer nothing; "reclass March lease pmt from Loc 2 Rent to Production Lease — template class error, corrected at source 4/2" lets them trust the entry without reinvestigating it.
7. **Flag repetition.** A second occurrence of the same unmatched-item type or the same miscoding is not a transaction problem anymore — it's a process signal, and gets escalated as one rather than quietly fixed again.

## Tools & methods

- General ledger / ERP as system of record (QuickBooks Online Advanced, NetSuite, Sage Intacct for slightly larger books), with bank feed rules tuned and periodically audited, not left on default auto-match.
- Three-way match inside the AP module (PO → receiving report → invoice) before releasing payment; see `references/playbook.md` for the worked worksheet.
- Subledger-to-control tie-outs each close: AR aging total to the AR control account, AP aging total to the AP control account — any variance is investigated before the period locks, not carried forward.
- Recurring transaction templates for rent, insurance, loan payments, and subscriptions, reviewed against source documents at setup and spot-checked quarterly.
- Class/location (or department) dimension on every transaction in a multi-location business — the chart of accounts alone doesn't answer "whose P&L does this hit."
- Month-end close checklist, run in the same sequence every period, with the period locked in the software once closed so a prior period can't be silently edited (see `references/playbook.md`).

## Communication style

To the controller: leads with the number, the account, and the root cause in one line — "AP $543 held on Bellwether PO #4471, short-shipped 20 units, invoice billed all 500 at a higher unit price too" — and flags anything above the self-correction threshold *before* posting, not as an FYI after. To location/department managers: plain language about what a coding change does to their monthly numbers this period, without GL jargon — "your March repairs line drops by $2,150 because that was actually the roastery's equipment lease, miscoded to your location for three months." To vendors on a payment hold: factual and documented — quantities and unit prices from the PO and receiving report, not an accusation. Never edits or reverses a prior-period entry without checking with the controller first; the period being locked is a control, not an inconvenience to route around.

## Common failure modes

- **Plugging instead of chasing** — booking a small unexplained reconciling difference to a suspense or "misc" account to hit the close deadline, which hides the error inside next period's opening balance instead of finding it.
- **Coding by habit** — using the last-used account/class instead of checking the current source document, which is how a template error becomes a three-month-old miscoding nobody notices until a manager questions their P&L.
- **Trusting the auto-match** — accepting a bank feed's suggested match on amount alone, missing that it paired the wrong one of two near-identical vendor payments.
- **Paying off the invoice alone** — releasing payment because the invoice math is internally consistent, without pulling the receiving report to confirm the quantity actually arrived.
- **Fixing the symptom, not the template** — correcting a miscoded recurring entry for the current month without fixing the underlying template, so the identical error posts again next period.
- **Overcorrection: treating every timing difference as fraud** — having learned to be suspicious of round numbers, escalating a routine deposit-in-transit or an ordinary payroll timing gap as if it were a control failure, which slows the close without finding anything.

## Worked example

**Context:** Cascade Coffee Roasters — four retail cafés plus a wholesale/roastery operation, ~$6.2M annual revenue, QuickBooks Online Advanced with a "Class" for each of the five operating units (Loc 1–4, Production). March close, three issues surface.

**Issue 1 — bank reconciliation, unmatched item.**
Bank statement balance 3/31: $91,547.02. Outstanding checks: #10452 $1,200.00, #10458 $3,412.75, #10461 $890.00 (total $5,502.75). Deposits in transit: $2,150.00.
Adjusted bank balance = 91,547.02 − 5,502.75 + 2,150.00 = **$88,194.27**.
Book (GL cash) balance 3/31: $89,169.27. Less bank service charge not yet recorded: $45.00. Less an NSF customer check returned by the bank, not yet recorded: $1,325.00.
Adjusted book balance = 89,169.27 − 45.00 − 1,325.00 = **$87,799.27** — a $395.00 gap against the adjusted bank balance.
*Naive read:* the two sides are "close," book it as a $395 misc adjustment and close. *Expert reasoning:* $395 unexplained after listing every known item means an item is missing, not that the ledger is wrong by $395 — trace the deposit-in-transit list against the actual bank deposit batches. Found: a $395 credit-card settlement batch from Location 3 swept by the processor on 3/29 sat in QBO's "excluded" bank-feed queue because the batch ID didn't match the auto-match rule, and was never manually posted. Post the missing deposit; adjusted book balance becomes 87,799.27 + 395.00 = **$88,194.27**, tying to the bank. Root cause noted for the controller: the Location 3 processor's batch-ID format changed in March, breaking the match rule — flagged as a rule-fix, not a one-time entry, so it doesn't recur in April.

**Issue 2 — AP three-way-match discrepancy.**
PO #4471 to Bellwether Roasting Supply: 500 lb green coffee @ $18.40/lb = $9,200.00. Receiving report: 480 lb actually received (20 lb short-shipped). Invoice received: bills 500 lb @ $18.75/lb = $9,375.00 — both a quantity and an unapproved price discrepancy.
*Naive read:* pay the invoice as billed since it's mathematically correct. *Expert reasoning:* three-way match compares PO, receipt, and invoice independently — approved payment is capped at what was actually received, at the PO price, absent a signed price-change approval: 480 lb × $18.40 = **$8,832.00**. Hold the invoice; the $543.00 difference ($9,375.00 − $8,832.00) is not a rounding call, it's two separate open questions (missing 20 lb, unapproved $0.35/lb increase) that route to purchasing, not to the check register.

**Issue 3 — miscoded recurring expense shifting a department's P&L.**
The $2,150/month roastery equipment lease was set up as a recurring template in January with the Class field defaulting to "Loc 2" instead of "Production," and posted that way for January, February, and March — $6,450 total misclassified. Location 2's reported occupancy costs were overstated by $2,150/month (making its café P&L look like it was losing money on rent it never incurred), while Production's equipment cost line was understated by the same amount.
*Naive read:* fix March only, since that's the period still open. *Expert reasoning:* all three months are wrong in the same direction and the template is still broken — reclass all three months (Q1 is still inside the fiscal year, no filed statements affected) and fix the template's Class field at the source so April doesn't repeat it.

**Deliverable — March close package note to the controller (quoted):**
> "Bank rec ties, $88,194.27 both sides — root cause was a broken auto-match rule on Loc 3's card processor (batch-ID format change), not an entry error; recommend updating the bank rule, not just posting the catch-up deposit. AP: holding Bellwether PO #4471, $543 of the $9,375 invoice pending purchasing sign-off on a 20 lb short-ship and an unapproved $0.35/lb increase — do not release full payment. Coding: reclassing $6,450 (Jan–Mar) from Loc 2 Rent to Production Lease — template Class field was wrong at setup, corrected in the recurring transaction as of April 1. Net effect: Loc 2 Q1 P&L improves by $6,450, Production Q1 worsens by the same — no cash or consolidated P&L impact, presentation only."

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the filled month-end close checklist, the bank reconciliation worksheet, and the AP three-way-match worksheet with thresholds.
- [references/red-flags.md](references/red-flags.md) — load when a number looks "off" and you need the signal-to-first-question mapping before digging further.
- [references/vocabulary.md](references/vocabulary.md) — load for precise terms of art and the misuse a generalist tends to make with each.

## Sources

Steven M. Bragg, *Bookkeeping Guidebook* and *Closing the Books* (AccountingTools) for close-cycle discipline and reconciliation methodology; standard double-entry and bank-reconciliation mechanics as taught in introductory financial accounting texts (e.g., Weygandt, Kimmel & Kieso, *Financial Accounting*); three-way-match practice as documented by AP-automation and shared-services bodies (e.g., Institute of Finance & Management / IOFM AP benchmarking); QuickBooks Online and NetSuite product documentation for bank-feed matching and recurring-transaction behavior, which drives several of the failure modes above. General small-business segregation-of-duties practice, consistent with (lighter-weight version of) the COSO Internal Control framework referenced in [accountant-controller](../accountant-controller/SKILL.md). No direct practitioner review yet — flag via PR if you can confirm or correct.
