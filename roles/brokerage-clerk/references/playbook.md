# Brokerage Clerk — Playbook

## Exception report triage table

Filled example from a settlement-cycle exception report, triaged by type and priority:

| Break ID | Security | Type | Break amount | Days to settlement | Priority |
|---|---|---|---|---|---|
| B-4471 | MNO Inc. | Price mismatch | $250.00 | 1 (T+1) | High — same-day resolve |
| B-4472 | RST Corp | Quantity mismatch | $18,400.00 | 1 (T+1) | Critical — desk escalation |
| B-4473 | XYZ Ltd | Settlement date | $0.00 (date only) | 0 (T+1 today) | Critical — calendar error |
| B-4474 | ABC Co | Price mismatch | $4.10 | 1 (T+1) | Low — within $10 tolerance, close after single re-check |

Priority order: (1) anything past or at the T+1 cutoff, (2) quantity mismatches over $1,000 — these are more likely to reflect a real erroneous trade than a booking-formula error, (3) price mismatches over the firm's stated tolerance, (4) everything else.

## Weighted-average price recomputation (filled example)

Order: buy 12,000 shares, filled across three prints.

| Fill | Shares | Price | Value |
|---|---|---|---|
| 1 | 4,000 | $52.10 | $208,400.00 |
| 2 | 5,000 | $52.25 | $261,250.00 |
| 3 | 3,000 | $52.40 | $157,200.00 |
| **Total** | **12,000** | — | **$626,850.00** |

Weighted-average price = $626,850.00 ÷ 12,000 = $52.2375/sh.

Common booking-system defect: some legacy blotter templates average the *distinct print prices* ($52.10, $52.25, $52.40) rather than weighting by shares — (52.10+52.25+52.40)/3 = $52.25/sh, total $627,000.00, a $150.00 overstatement. Always recompute from the fill-ticket table, not from a system-generated average field, until that field's calculation method is confirmed.

## Corporate-action cost-basis adjustment (filled example)

Client holds 400 shares of DEF Corp, original cost basis $60.00/share ($24,000.00 total). DEF announces a 3-for-2 stock split, record date 03/15, payable 03/29.

**Step 1 — adjust share count:** 400 × (3/2) = 600 shares.

**Step 2 — adjust cost basis per share:** $60.00 ÷ (3/2) = $40.00/share.

**Step 3 — verify total cost basis unchanged:** 600 × $40.00 = $24,000.00 — matches original $24,000.00. If the recomputed total doesn't match the pre-split total exactly, the adjustment was applied to only one of share count or cost basis, not both.

**Fractional-share handling:** if the client had held 401 shares, 401 × 1.5 = 601.5 shares. The 0.5 fractional share is cashed out at the post-split closing price (per the corporate-action notice's terms), not rounded up or down. If notice terms specify "round down, cash-in-lieu for the fraction," book 601 shares plus a cash-in-lieu payment for 0.5 share at the stated reference price.

## DK (don't-know) resolution sequence

Fallback order when a DK notice arrives from a contra broker:

1. Check the order management system for a matching order at the same security, quantity, and approximate execution time. If found, the DK is likely a booking-side mismatch (wrong account or settlement instructions) — correct and resend the confirmation.
2. If no matching order exists, check whether the trade was executed by a different desk or under a different account number at the same firm — internal misrouting is more common than an entirely fabricated confirmation.
3. If neither turns up a match, treat the trade as genuinely unmatched. Do not book it provisionally. Notify the trading desk that a purported execution has no corresponding internal record.
4. Escalate to the executing broker's operations desk with the trade details (security, quantity, price, time) and request their fill-ticket-level confirmation before any booking occurs.
