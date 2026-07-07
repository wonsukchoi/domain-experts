# Gambling Cage Worker — Playbook

## Shift-change bank reconciliation

| Component | Amount |
|---|---|
| Opening bank (prior shift closing count) | $75,000.00 |
| + Fills issued to tables this shift | $12,400.00 |
| − Credits received from tables this shift | $8,150.00 |
| − Marker redemptions (cash out) | $9,600.00 |
| − Check cashing / chip redemptions (cash out) | $14,200.00 |
| + Marker issuances funded (chips out, no cash movement) | $0.00 (non-cash, tracked separately in credit ledger) |
| **Book balance (expected closing count)** | **$55,450.00** |
| Physical count at shift change | $55,430.00 |
| **Variance** | **−$20.00** |

A $20 variance is small but not zero — retrace the shift log by timestamp before writing it off as a counting error. Common cause at this size: a $20 bill miscounted in a redemption stack, or a rounding entry on a partial-denomination fill.

## CTR aggregation tracking (per patron, per gaming day)

| Time | Transaction | Amount | Running cash-out total |
|---|---|---|---|
| 11:40am | Chip redemption | $4,300 | $4,300 |
| 1:15pm | Chip redemption | $6,200 | $10,500 — **crosses $10,000, file CTR** |

Track cash-IN and cash-OUT separately — Title 31 aggregates each direction independently. A patron who cashes in $8,000 and cashes out $8,000 the same day has two separate $8,000 totals, neither triggering a CTR alone, unless either direction independently crosses $10,000.

## Marker issuance check

1. Pull patron's approved credit line and current outstanding-marker balance.
2. Confirm: requested marker amount + outstanding balance ≤ approved credit line.
3. Verify ID matches the credit application on file.
4. Patron signs the marker; cage worker countersigns.
5. Chips issued; marker logged to the patron's outstanding-balance ledger.

Example: patron has a $25,000 approved line, $18,000 currently outstanding. Requests a $10,000 marker. $18,000 + $10,000 = $28,000 > $25,000 line — decline or route to credit services for a limit increase; do not issue on cage authority.

## Fill/credit slip processing

| Field | Fill (cage → table) | Credit (table → cage) |
|---|---|---|
| Initiated by | Pit supervisor request | Pit supervisor request |
| Signed by | Dealer, pit supervisor, cage worker | Dealer, pit supervisor, cage worker |
| Chip denominations | Itemized by color/value | Itemized by color/value |
| Copy distribution | Cage, pit, accounting (3-part) | Cage, pit, accounting (3-part) |

Hold any slip missing a required signature — do not release chips (fill) or accept the credit as final (credit) until all three signatures are present.

## Shortage-investigation sequence

1. Confirm the physical count itself (recount before assuming the count is right).
2. Re-verify the book-balance calculation arithmetic independently.
3. Retrace the shift transaction log chronologically, checking each fill/credit/redemption against its slip.
4. Cross-check any voided transactions — a voided transaction with chips or cash already moved before the void is a common shortage source.
5. If unresolved after retracing, escalate to the cage supervisor with the specific transaction window still unreconciled, not a general "we're short."
