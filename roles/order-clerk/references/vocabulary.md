# Order Clerk — Vocabulary

### Available to promise (ATP)
Inventory that is both on hand and unallocated to any other order — what can actually be committed to a new order, as distinct from total on-hand inventory.
**In use:** "ATP on that SKU is only 250 — the other 100 units on hand are already allocated to a different order."
**Common misuse:** treating total on-hand quantity as available, ignoring units already committed elsewhere.

### Order-total-based pricing
A tier-pricing policy where the discount tier is determined by the full order quantity, regardless of how many separate shipments fulfill it.
**In use:** "This account is order-total-based, so the backordered units still get the 340-unit tier price, not the 90-unit tier."
**Common misuse:** re-pricing each shipment independently as if it were a separate order, which understates the customer's earned discount on split shipments.

### Ship-complete vs. partial-ship
Ship-complete means an order only ships once all lines/quantities are available; partial-ship allows shipping what's available now with the remainder to follow.
**In use:** "This account is marked ship-complete — we can't send the 250 units now, we have to wait for the full 340."
**Common misuse:** assuming partial-ship is always allowed by default; some accounts require ship-complete and will reject or short-pay an invoice for a partial shipment they didn't authorize.

### Backorder
The unfulfilled portion of an order held for future shipment once inventory becomes available, as distinct from a cancelled or lost order line.
**In use:** "90 units are on backorder, expected next Monday."
**Common misuse:** using "backorder" and "out of stock" interchangeably — a backorder implies a committed future fulfillment date, not indefinite unavailability.

### EDI transaction set (850/855/856)
Standardized electronic-order document types: 850 is the purchase order, 855 is the order acknowledgment (confirming what will actually ship, at what price, by when), 856 is the advance ship notice (confirming what did ship).
**In use:** "Their 850 said 340 units, but our 855 back to them should show the actual price-tier total, in case it looks different from what they expected."
**Common misuse:** treating the 850 as final — the 855 is where discrepancies (price, quantity, availability) get formally communicated back to the customer's system.

### Unit of measure (UOM)
The counting unit an order quantity refers to — each, case, box, pallet — which determines both the actual quantity shipped and the price applied.
**In use:** "Confirm the UOM before entering — this SKU defaults to case, and the customer usually orders in eaches."
**Common misuse:** assuming a bare number always refers to the system's default UOM rather than checking what the customer meant.

### Price break / quantity tier
A pricing structure where the per-unit price decreases at defined quantity thresholds.
**In use:** "340 units crosses the 100-unit price break, so it prices at $3.85, not $4.20."
**Common misuse:** applying the tier based on a single shipment's quantity when the account's policy ties it to the full order quantity instead.

### Pick ticket
The internal warehouse document generated from an order that tells fulfillment staff what to pull from inventory; once printed, the order is considered in-process for fulfillment.
**In use:** "The pick ticket already printed, so this change needs a warehouse hold, not just a system edit."
**Common misuse:** assuming an order can be freely edited any time before it physically ships, without accounting for the pick-ticket-printed cutoff.

### Substitution (SKU cross-reference)
A pre-approved alternate item that can fulfill an order line when the originally ordered SKU is unavailable, distinct from an ad hoc suggestion.
**In use:** "SKU-7735 is the approved substitute for SKU-7734 — same spec, same price tier."
**Common misuse:** offering any similar-sounding item as a substitute without checking the formal cross-reference, risking a spec mismatch the customer didn't agree to.

### Cutoff (order-change window)
The point in the fulfillment process after which a change request can no longer be applied without pulling the order back from an active process step.
**In use:** "We're past the EDI-acknowledgment cutoff — changing this now means re-sending an 855 correction, not a simple edit."
**Common misuse:** treating "before it ships" as the only relevant cutoff, ignoring earlier ones like pick-ticket printing or EDI acknowledgment that make a change costlier even before physical shipment.
