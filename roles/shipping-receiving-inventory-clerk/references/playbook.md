# Shipping, Receiving, and Inventory Clerk — Playbook

## Receiving-inspection decision table

Filled example from a single inbound shipment against its PO and packing slip:

| Line | Item | PO qty | Packing-slip qty | Received qty | Condition | Action |
|---|---|---|---|---|---|---|
| 1 | Widget A | 500 | 500 | 500 | Good | Accept, process into system |
| 2 | Widget B | 200 | 200 | 188 | Good | Short-ship 12 units — accept received qty, flag PO for backorder on remainder |
| 3 | Widget C | 100 | 100 | 100 | 6 units water-damaged | Accept 94 good units, quarantine 6 damaged, file damage claim with carrier |
| 4 | Widget D | 0 (not on this PO) | 50 | 50 | Good | Quarantine entire line — packing-slip item not on PO, hold for purchasing to confirm (could be a different PO number, could be an error) |

Rule of thumb: any line where the packing slip and PO disagree gets quarantined regardless of physical condition — condition-only issues (line 3) can be partially accepted with the good units processed immediately.

## Cycle-count investigation sequence (filled example)

SKU BRK-1180, cycle count shows system 212 units, physical 198 units, variance -14 units.

| Step | Check | Finding |
|---|---|---|
| 1 | Pull 30-day transaction log | 3 receipts (+180), 6 picks (-166) against a 30-day-ago starting count of 198 → 198+180-166=212, matches system |
| 2 | Check adjacent bin locations for a matching offsetting variance | None found within the same aisle |
| 3 | Check for an uncounted partial case | Found — a broken case of 14 units was set aside on a nearby shelf during the last pick, not returned to the primary bin, and not scanned as a location transfer |
| 4 | Resolution | Relocate 14 units to primary bin; no system adjustment needed — this was a location, not a quantity, error |

If step 3 had found nothing, the next step is a full recount of the SKU's total on-hand across all locations (not just the counted bin) before accepting the variance as real shrinkage.

## Outbound pack-verification checklist (filled example)

Order #48213, 4 line items, ship-to verified against order:

| Item | Ordered qty | Picked qty | Packed qty | Label check | Status |
|---|---|---|---|---|---|
| Cable A | 3 | 3 | 3 | Matches order | Pass |
| Cable B | 1 | 1 | 1 | Matches order | Pass |
| Adapter C | 2 | 3 | — | Pick discrepancy caught before packing | Stop — recount, do not pack 3 when order says 2 |
| Power supply D | 1 | 1 | 1 | Ship-to address label mismatch (different suite number than order) | Stop — verify address against order before shipping, do not assume label is right |

Two stops on one order is unusual but not implausible — each stop is checked and resolved independently; neither is waved through because the other three lines were clean.

## Quarantine-to-resolution fallback order

When a receiving discrepancy can't be resolved at the dock:

1. Photograph the discrepancy (damage, wrong item, short-ship) and attach to the receiving record before moving the items to quarantine.
2. Route to purchasing/vendor management with the specific mismatch documented — PO line, expected vs. received, condition.
3. If purchasing confirms a vendor error, quarantine hold continues until a credit, replacement, or return-authorization is issued — don't release to inventory on a verbal "it's fine."
4. If the discrepancy turns out to be an internal PO-entry error (wrong quantity entered originally), correct the PO and release the quarantined stock to inventory with a note on the original discrepancy record.
