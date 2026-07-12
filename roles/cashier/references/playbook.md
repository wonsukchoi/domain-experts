# Playbook

Filled procedures a cashier actually runs, with real numbers and thresholds. Store-specific policy always overrides the numbers here — these are the shape of a well-run procedure, not a universal policy.

## 1. Till reconciliation at close (walkthrough)

Run every close, in this order — never total the drawer first and work backward to explain it.

1. **Pull the Z-report**, not an X-report. The Z-report resets the register and is the only source of truth for the shift's totals: cash sales, card sales, refunds, voids, no-sales, drops.
2. **Compute expected cash:**
   ```
   Expected cash = Opening float
                 + Cash sales (from Z-report)
                 − Cash refunds
                 − Cash drops to safe (each drop verified against a signed drop slip)
   ```
3. **Count the drawer twice**, once by denomination-stack count, once by a second pass on any bill $50+, checked for counterfeit markers if not already checked at acceptance.
4. **Compare actual to expected.** If actual ≠ expected:
   - **Under store's no-action threshold** (commonly ≤$5–10): log and move on, no write-up. Register-level rounding and one missed count are normal at this size.
   - **Above that threshold but below the write-up threshold** (commonly $10–20): recount once, note the variance in the shift log even if unexplained.
   - **Above the write-up threshold** (commonly $20): pull the no-sale, void, and refund logs and reconcile before writing anything. Submit a variance form regardless of whether a cause is found.
   - **Above the automatic-referral threshold** (commonly $50): variance form plus automatic loss-prevention notification, independent of whether the cashier can explain it.
5. **Never adjust the count to match the expected total.** A drawer "corrected" to hit the expected number destroys the only evidence a real shortage or overage leaves behind.

**Example, filled (see SKILL.md worked example for the full reconciliation):**

| Line | Amount |
|---|---|
| Opening float | $150.00 |
| + Cash sales (Z-report) | $1,245.60 |
| − Cash refunds | $42.30 |
| − Cash drop (verified) | $500.00 |
| **Expected cash** | **$853.30** |
| Actual counted | $828.80 |
| **Variance** | **−$24.50 (short)** |

## 2. No-receipt return decision ladder

Work down the ladder; stop at the first step that resolves it. Never skip to cash refund.

1. **Look it up.** Search the register journal or loyalty account by the card used, phone number, or loyalty ID. Most POS systems retain 60–90 days of transaction history — a "no receipt" return is very often a "no printed receipt" return.
2. **If found:** process as a normal return against that transaction — cash back to cash, card back to the same card, never cash back for a card purchase.
3. **If not found, check the item against store policy for receiptless returns** — typically store credit only, at the item's current lowest sale price (not original price), capped per transaction (commonly $20–50) without a manager.
4. **If the customer wants cash and there's no record, escalate to a manager** — do not offer cash from the drawer under any circumstance without manager sign-off; a receiptless cash refund is the single highest-fraud-rate transaction at a register.
5. **If the item shows signs of prior use, mismatched packaging, or price-tag swapping** ("wardrobing" or ticket-switching), escalate regardless of receipt status — this is a distinct fraud pattern from simple no-receipt returns and gets flagged to loss prevention, not processed as a normal return.

## 3. Counterfeit-bill checklist (bills $50 and up, or any bill that feels off)

Run in order — stop and decline the bill at the first clear failure, calling a manager rather than confronting the customer directly.

1. **Feel:** genuine U.S. currency is cotton-linen blend with raised ink from intaglio printing — counterfeit on inkjet/laser paper feels slick and flat.
2. **Look at the portrait watermark** (held to light): should be a faint, matching image of the same person on the bill, visible from both sides.
3. **Check the security thread** (held to light or under UV): embedded vertical strip with printed text (denomination + "USA"), glows a specific color under UV depending on denomination.
4. **Tilt for color-shifting ink** on the denomination numeral (bottom-right, front) on $10 and up — should shift color as the bill tilts; a static, flat-printed number is a fail.
5. **Compare to a reference bill or the counterfeit pen** as a last, weakest check — the iodine reaction shows brown/black on wood-pulp (fake) paper vs. no reaction on genuine cotton-linen stock; a pen pass alone is not sufficient on a bill that failed steps 1–4.
6. **If any two checks fail, do not accept the bill.** Say plainly you can't accept that bill and offer another payment method; call a manager if the customer disputes it. Never argue the bill's authenticity directly with the customer at the register.

## 4. Price-dispute and override script

```
CUSTOMER: "This rang up wrong, the sign said $3.99."
CASHIER (step 1 — verify, don't argue): "Let me rescan/pull that up."
  → Handheld price-check scanner on the shelf tag, or manager-authorized
    override list for known sale-sign lag.

IF the scanner confirms the shelf price differs from the register price:
  → Apply the lower price via the register's price-match/override function,
    logged automatically against the cashier's login. No manager needed if
    within the store's self-authorized override cap (commonly up to $10
    difference).

IF the difference exceeds the self-authorized cap, or there's no shelf-tag
evidence:
  → "I can get my manager to verify that for you" — call the manager
    physically to the register. Never accept the customer's stated price
    from memory and never use a manager's override code without the
    manager present.
```

## 5. Cash-drop schedule (high-volume format example)

| Trigger | Action |
|---|---|
| Drawer cash exceeds $200 | Drop excess above $100 to the safe at the next natural lull |
| Every 2 hours regardless of drawer total | Scheduled drop, logged with a signed slip and a second employee's initials |
| Before/after any armed-robbery-risk period (late night, low staffing) | Drop down to the minimum operating float immediately |
| End of shift | Full drop and reconciliation before the next cashier's float is counted in |

Each drop is logged with: timestamp, amount, cashier ID, witness ID, and drop-safe slot number — this log is what makes a drop "verified" rather than merely claimed, and it's the first thing pulled when a variance investigation needs to rule the drop in or out as the cause.

## 6. Opening / closing checklist

**Open:** count and sign for opening float against the prior close's recorded float (not against memory) → verify receipt paper, card reader connectivity, counterfeit pen/UV light present → check for any overnight manager notes on price changes or held items.

**Close:** run Z-report → reconcile per section 1 → bag and label the drop with shift date/time/cashier ID → sign the variance form even if the variance is zero → hand off float count to the next cashier with a witness, not by leaving cash in an unattended drawer.
