# Order Clerk — Playbook

## Price-tier lookup table (filled example, SKU-7734)

| Quantity range | Unit price | Order of 340 falls in |
|---|---|---|
| 1–99 | $4.20 | — |
| 100–499 | $3.85 | ✓ (order-total-based) |
| 500+ | $3.40 | — |

Order-total-based policy: the tier is set by the *sum of all units on the order*, not by the size of any single shipment. Re-derive the tier only if the customer formally changes the total quantity — not when a shipment is split for availability reasons.

## Available-to-promise (ATP) check (filled example)

| Component | Units | Notes |
|---|---|---|
| On-hand, unallocated | 250 | Available to ship today |
| Confirmed inbound PO | 90 | Arrives in 5 business days |
| Total ATP within customer's deadline | 250 | The inbound 90 doesn't count if it arrives after the requested date |
| Order quantity | 340 | |
| Shortfall against deadline | 90 | Triggers substitution-or-wait decision |

Rule: ATP for a deadline-bound order only counts inventory that will physically arrive *before* the deadline. Inventory arriving after the deadline is not "available" for that order even if it's confirmed and on order.

## Substitution-decision table

| Condition | Action |
|---|---|
| Compatible substitute SKU in stock, sufficient quantity | Offer substitution as the fastest path to full order by deadline |
| No compatible substitute, deadline can't be met | Offer partial-ship-now-plus-backorder, state the backorder arrival date explicitly |
| Standing account instruction on file (e.g. "always substitute," "never substitute without asking") | Follow the standing instruction, skip the ask — but still notify |
| Substitute SKU has a different price tier structure | Flag for a price check before offering — do not assume price parity |

## Order-confirmation template (filled)

```
Order Confirmation — [Order #12345]
Customer: [Account name]
Ship-to: [Address]

Line 1: SKU-7734, Widget Assembly, Qty 340, Unit EA, Unit Price $3.85, Line Total $1,309.00
  - Ships in two shipments: 250 units today, 90 units [date] (backorder) OR
  - Full 340 units today via substitution [if selected]

Order Total: $1,309.00
```

## Backorder-notice template (filled)

```
Subject: Backorder notice — Order #12345, SKU-7734

90 units of SKU-7734 on your order are backordered, expected to arrive [date].
This shipment will ship separately at no additional freight charge.
Reply if you'd like to substitute or cancel the backordered portion.
```

## SKU-mismatch resolution sequence

1. Compare the stated SKU against the stated description on the same order line.
2. If they don't match a single item in the catalog, search the description first — customers misremember part numbers more often than they misdescribe the item.
3. If the description search returns more than one plausible match, hold the line and contact the customer rather than guessing.
4. Once resolved, note the correction on the internal order record (not just the confirmation) so the pattern is visible if it recurs with the same account.
