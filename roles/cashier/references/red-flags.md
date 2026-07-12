# Red flags

Smell tests a shift supervisor or loss-prevention reviewer checks first. Format for each: what it usually means, the first question to ask, and the data to pull before concluding anything.

### No-sale opens exceeding ~3–4 per shift, or any with no reason code logged

**Usually means:** legitimate reasons are usually one-off (making change, a jam) — repeated opens, or any open with no logged reason, is the standard cover for taking cash without ringing a sale.

**First question:** "Walk me through what happened at each of these opens — what were you doing right before and after?"

**Data to pull:** register journal timestamps for each no-sale; item-scan log in the 60 seconds before and after each one, checking for a scan immediately followed by a void.

### Void rate for one cashier meaningfully above the store's average (commonly >2–3x peers on a comparable shift)

**Usually means:** either a genuinely difficult register/scanner that shift, or the classic scan-take-cash-void pattern used to make a transaction disappear after the cash is already collected.

**First question:** "Show me the voided items and the timestamps — was each void immediately followed by a re-ring, or did the item just disappear from the sale?"

**Data to pull:** void log with item, amount, timestamp, and whether a corresponding completed sale exists later in the shift for the same item.

### Cash refunds without a receipt clustering on one register or one cashier

**Usually means:** receiptless cash refunds are the highest-fraud-rate transaction type at a register; clustering on one person is the tell that it's being exploited rather than occurring randomly across the store.

**First question:** "For these refunds, what did the lookup by loyalty ID or card show — was there ever a matching original sale?"

**Data to pull:** refund log cross-referenced against register journal transaction history for the same item/SKU in the prior 60–90 days.

### Recurring shortage under the automatic-referral threshold (commonly $50), on the same cashier or same till

**Usually means:** a single shortage under threshold is usually a miscount; a recurring pattern just under the threshold is the classic signature of skimming calibrated to avoid automatic review.

**First question:** "Pull the last 90 days of variance forms for this cashier and this register — is this a trend or a one-off?"

**Data to pull:** variance history by cashier and by register separately (a pattern following the cashier across registers points at the person; a pattern following the register points at a hardware or process issue).

### Consistent overage, not just shortage

**Usually means:** counterintuitively, a cashier consistently over on cash is often "banking" small amounts across shifts to cover a larger planned shortage later, or making change errors in their own favor without realizing it — either way, consistent overages get the same scrutiny as shortages, not a pass because the store technically gained cash.

**First question:** "Is the overage steady in size, or does it vary — and does it correlate with any specific transaction type?"

**Data to pull:** overage size and frequency by shift; denomination-level count discrepancies (a specific bill or coin repeatedly over/under suggests a counting habit, not intent).

### High-denomination bills accepted with no counterfeit check logged or performed

**Usually means:** either a genuine process skip under time pressure, or acceptance of currency the cashier suspected was bad rather than risk an argument — both need correction, but the second is a training gap with real loss exposure.

**First question:** "Walk me through your counterfeit-check process for a $100 bill — what do you actually do?"

**Data to pull:** transaction log for bills $50+ against whether the counterfeit-check step (pen mark, UV scan) has a corresponding timestamp or terminal log entry, where the register/pen system tracks it.

### Same loyalty account or discount code applied across multiple different customers' transactions in one shift

**Usually means:** sweethearting — a cashier applying their own or a friend's loyalty discount to other customers' purchases, or running a friend's items through under a discount code that shouldn't apply.

**First question:** "Whose loyalty account is this, and why was it used on transactions for different-looking baskets across the shift?"

**Data to pull:** loyalty-account usage frequency per shift per cashier; basket contents and total across the flagged transactions for a pattern of unrelated purchases under one account.

### Discount or coupon stacking beyond the printed limit

**Usually means:** either genuine confusion about stacking rules, or intentional application of multiple discounts the register should have blocked but didn't (a manual override was used to force it through).

**First question:** "Which override was used to apply the second discount, and was a manager present?"

**Data to pull:** discount/coupon log with override codes used; cross-reference override-code usage against manager schedule for that timestamp.

### Return item shows signs of prior use, mismatched packaging, or a swapped price tag ("wardrobing" / ticket-switching)

**Usually means:** a distinct fraud pattern from a simple no-receipt return — the customer used the item and is returning it as new, or swapped a cheaper item's tag onto a pricier one before returning or purchasing it.

**First question:** "Does the item's condition and packaging match what's described on the receipt or return record?"

**Data to pull:** item SKU vs. the SKU actually rung; photos or description of item condition at return; whether the same customer has multiple similar returns on file.

### Drawer accessed or transactions logged under a cashier ID during a time that cashier wasn't scheduled

**Usually means:** either a shared login (itself a control failure) or someone using another employee's credentials, deliberately or by mistake at shift handoff.

**First question:** "Who was physically at Register 3 at this timestamp, and does it match the schedule?"

**Data to pull:** login timestamps vs. posted schedule; badge/time-clock records if available; whether the store's policy on shared logins was followed.
