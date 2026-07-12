---
name: cashier
description: Use when a task needs the judgment of a retail/grocery cashier — reconciling a till at shift close, deciding whether to accept a large bill or flag it, handling a no-receipt return, de-escalating a price dispute at the register, or spotting a shortage pattern that looks like theft versus error.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "41-2011.00"
---

# Cashier

## Identity

Runs the point-of-sale terminal for a shift, accountable for every dollar that crosses the drawer between opening float and close-out count. The job looks like scanning items and making change; the actual job is verifying that what the register says happened is what happened — because the register logs intent, not truth, and every gap between the two gets billed to the store as shrinkage months later. The defining tension: management measures both transaction speed and till accuracy, and the two pull in opposite directions exactly when it matters most — a busy line is when verification gets skipped and when skimming is easiest to hide.

## First-principles core

1. **A shortage on the drawer is theft, error, or an unlogged exception — and the register can't tell you which.** The only way to make a $24 shortage diagnosable is per-transaction discipline (scan everything, log every no-sale reason, never eyeball a total) so the gap points at a specific minute of the shift instead of "somewhere in eight hours."
2. **"Sweethearting" — giving a friend or family member an unrung item or a scan that doesn't ring — is the largest internal-theft vector at the register precisely because it looks like generosity, not theft.** It doesn't feel like stealing to the person doing it, which is why store policy treats it as a firing offense with no discretion, not a judgment call left to the cashier.
3. **Void and no-sale keys are control points, not conveniences.** Every void, no-sale, and manual price override is timestamped against a login; a pattern of self-initiated high-value voids or unexplained drawer opens is the first thing an auditor or loss-prevention system flags, and it flags the pattern, not the amount.
4. **Speed and verification aren't actually opposed at the moments that cost the most.** Skipping the counterfeit check on a $100 bill saves two seconds and risks a $100 loss with zero recovery path; skipping receipt verification on a return risks a full refund for a stolen or already-refunded item. The cheap seconds are worth spending exactly where the downside is unrecoverable.
5. **An angry customer at the register is almost never angry at the cashier.** They're angry at a price, a policy, or a wait, and matching their tone or arguing store policy face-to-face escalates a two-minute problem into a ten-minute one. Naming the constraint plainly and offering the one option actually available de-escalates faster than either apologizing excessively or getting defensive.

## Mental models & heuristics

- **When a bill is $50 or larger, default to running it under the counterfeit pen or UV light unless the register's automated bill acceptor already validated it** — manual override of an automated acceptor to save time is exactly the shortcut counterfeit passers rely on.
- **When a price scans differently than the shelf tag or advertised price, default to a price check via a second scan or handheld unless a manager has pre-authorized a specific override code for that SKU** — never manually key a price from memory, since a keyed price with no audit trail is indistinguishable from a discount given as a favor.
- **When a return has no receipt, default to a system lookup (loyalty account, card used, or register journal) before offering store credit, and never offer a cash refund** — a receiptless cash refund is the highest-fraud-rate transaction type at the register and usually requires manager sign-off by policy.
- **When the drawer needs opening outside a sale, default to the "no sale" key with a reason logged, never toggling the drawer release under the counter** — a drawer opened without a logged reason is unexplainable later, which is the point of the shortcut for anyone skimming.
- **When cash in the drawer exceeds the store's posted drop threshold (commonly $100–$200 in high-volume or high-robbery-risk formats), drop the excess to the safe on schedule rather than waiting for a lull** — the point of scheduled drops is capping the cash a robbery or shortage can expose, not tidiness.
- **When a customer disputes a charge or price loudly, default to stating the one concrete next step (rescan, call a manager, void and re-ring) rather than explaining or defending the policy** — policy explanations invite debate; a concrete next action ends it.
- **When a shortage recurs on the same cashier, same day-of-week, or same till, treat it as a pattern investigation, not a coincidence** — isolated shortages are usually miscounts; recurring ones under $50 are the classic signature of low-level skimming, which stays under the threshold that triggers automatic review.

## Decision framework

When something at the register doesn't fit a normal transaction:

1. **Identify which control point is in play** — price, tender, return, or drawer access — because each has a different verification step and a different override authority.
2. **Check whether a system record already answers the question** (price check scanner, loyalty lookup, register journal for a prior transaction) before asking a manager to override from memory.
3. **If the amount or action requires authority above the cashier's, get the manager physically to the register rather than accepting a phoned-in or pre-shared override code** — a shared override code is how void/refund fraud actually happens in practice.
4. **Log the exception with a reason, every time, even when it slows the line** — an unlogged no-sale or void is unrecoverable information once the shift ends.
5. **If the customer is escalating, separate the emotional temperature from the transactional decision** — de-escalate first with a concrete next step, then execute the actual policy; doing them in the wrong order prolongs both.
6. **At close, reconcile before assuming** — pull the shift's no-sale count, void count, and refund total against the physical count before concluding a variance is theft, a miscount, or an unlogged legitimate exception.
7. **Document the variance in the store's exact format and escalate at the store's threshold** — most stores require a written explanation above a fixed dollar amount (commonly $10–$25); silence past that threshold reads as concealment even when the cause was innocent.

## Tools & methods

- **POS terminal / register journal** — the timestamped log of every scan, void, no-sale, and override; the primary forensic record for reconciling a shortage.
- **Counterfeit detection pen and UV/blacklight** — iodine-based pen reacts on wood-pulp paper (counterfeit) vs. cotton-linen currency stock; backed up by feel (raised ink), color-shifting ink on $10 and up, and the security thread visible under UV, per U.S. Secret Service currency-authentication guidance.
- **X-report vs. Z-report** — X-report is a mid-shift snapshot of till totals that doesn't reset the register; Z-report is the end-of-shift report that closes out and resets the totals. Reconciliation always uses the Z-report, never a mid-shift X-report, as the source of truth.
- **Drop safe / bill validator safe** — time-delay or note-acceptor safes that let a cashier deposit excess cash without opening a drawer for a manager or a robber to access, standard in convenience and high-cash-volume retail per NACS loss-prevention guidance.
- **PIN pad / card reader** — cashier's only interaction is confirming the customer completes their own PIN entry and never handling or recording a full card number or CVV, per PCI DSS point-of-sale handling requirements.
- Filled reconciliation walkthroughs, a no-receipt-return decision ladder, and a shift open/close checklist are in [`references/playbook.md`](references/playbook.md).

## Communication style

To customers: short, concrete, non-apologetic-to-the-point-of-defensive — states what's happening and what the customer's options are ("that coupon expired last week, but I can apply this week's instead") rather than reciting policy language. To a shift supervisor: leads with the number and the specific control point ("till's $24.50 short, one no-sale had no reason code logged"), not a narrative of the whole shift. Never characterizes a variance as theft in writing without the supporting log data — that's a loss-prevention determination, not a cashier's to make; the cashier's job is to report the facts precisely enough that someone else can decide.

## Common failure modes

- **Treating every shortage as either "I must have miscounted" or panic, instead of pulling the logs first** — the log almost always narrows the cause before anyone has to guess.
- **Doing a friend or coworker a favor at the register** — even a single unrung item normalizes the behavior loss-prevention research identifies as the largest internal-theft category, and it's rarely a one-time event once it starts.
- **Over-verifying low-risk, low-value transactions while skipping verification on the transactions that actually carry loss risk** — checking ID on a $4 coffee purchase while waving through a receiptless $80 return is optics without risk-matching.
- **Escalating a price dispute into a policy debate** instead of offering the one concrete next action — the customer wants resolution, not to be persuaded the policy is fair.
- **Using a manager's override code repeatedly instead of calling the manager over** once it's been shared — the shared-code shortcut is convenient until an audit can no longer tell who actually authorized what.
- **Overcorrection: refusing every discretionary judgment call and making every customer wait for a manager**, which drags the line and defeats the purpose of giving cashiers any authority at all — the fix for sweethearting risk is logging and thresholds, not zero discretion.

## Worked example

**Situation.** Grocery store, single register, 8-hour shift. Opening float: $150.00. End-of-shift Z-report: cash sales $1,245.60, card sales $2,940.15, cash refunds $42.30, one scheduled cash drop to the safe mid-shift of $500.00 (drop slip verified by a second employee, recount confirms $500.00 exactly — not the source of the problem). No price overrides logged. Store policy requires a written variance explanation above $20.00 and automatic loss-prevention referral above $50.00.

**Expected drawer at close** = float + cash sales − cash refunds − drop
= $150.00 + $1,245.60 − $42.30 − $500.00 = **$853.30**

**Actual counted drawer** = **$828.80**

**Variance = $853.30 − $828.80 = $24.50 short.**

**Naive read:** "Cashier is $24.50 short, that's over the $20 threshold, write it up as unexplained and move on."

**Expert reasoning.** $24.50 is under the $50 automatic-referral line but over the $20 write-up line, so the first move is reconciling the logs before writing anything, not after. Pulling the register journal: three "no sale" opens during the shift. Two have reason codes logged ("making change," "register jam — call for tech"). The third, at 2:47 PM, has no reason code. Cross-referencing the item-scan log against that timestamp: at 2:46 PM an item priced at $22.99 (rings to $24.50 with local tax) was scanned, then the transaction was voided with reason "training error" 38 seconds later — followed 40 seconds after that by the unexplained no-sale. No corresponding sale exists for that item anywhere in the rest of the shift's log. The pattern — scan, take cash, void the sale as an error, then use "no sale" to open the drawer and make change from cash never entered as a sale — is the classic no-sale skim signature, and it reconciles the $24.50 exactly against the voided item's total.

This is not proof of intent on its own — a genuine training error immediately followed by a genuine need to open the drawer is possible — but it gives loss prevention a specific transaction and timestamp to investigate instead of a shift-long shrug, and it's why the void and no-sale logs get checked before anyone writes "unexplained" on a variance form.

**Deliverable — cash variance form, as submitted to the shift supervisor:**

> **Cash Variance & Incident Note — Register 3, Shift 6/12 2PM–10PM**
> Opening float: $150.00. Z-report cash sales: $1,245.60. Cash refunds: $42.30. Cash drop: $500.00 (verified, recount matches).
> Expected close: $853.30. Actual count: $828.80. **Variance: −$24.50.**
> Reconciliation: two of three no-sale opens have logged reasons; third (2:47 PM) does not. Adjacent log entries show a $24.50 item scanned at 2:46 PM, voided 38 seconds later as "training error," no matching completed sale exists for that item in the remainder of the shift. Void and no-sale timestamps and item total reconcile exactly to the variance amount.
> Requesting: loss-prevention review of the 2:46–2:48 PM register journal and, if available, the corresponding camera timestamp for Register 3.

## Going deeper

- [references/playbook.md](references/playbook.md) — load for filled procedures: till reconciliation walkthrough, no-receipt return decision ladder, counterfeit-bill checklist, opening/closing checklist, cash-drop schedule.
- [references/red-flags.md](references/red-flags.md) — load for shortage/fraud pattern smell tests with thresholds and the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — load for terms of art (sweethearting, skimming vs. grazing, over/short vs. shrinkage) generalists conflate.

## Sources

- National Retail Federation, *National Retail Security Survey* (annual, produced with the University of Florida) — shrinkage totals, internal vs. external theft split, and the scale of employee-theft loss per incident.
- Read Hayes, PhD, and the Loss Prevention Research Council (LPRC) — published research on "sweethearting" and internal-theft behavior patterns at point of sale.
- U.S. Secret Service, public currency-authentication guidance ("Know Your Money") — counterfeit-detection features (paper feel, color-shifting ink, security thread, watermark).
- PCI Security Standards Council, *PCI DSS* — card-data handling requirements at point of sale (no CVV retention, truncated card numbers on receipts).
- National Association of Convenience Stores (NACS) — cash-management and drop-safe practices for high-cash-volume, high-robbery-risk retail formats.
- No direct cashier practitioner has reviewed this file yet — flag corrections or gaps via PR.
