# Gambling Surveillance Officer and Gambling Investigator — Playbook

## Incident report template (filled example)

**Incident #:** SR-2024-0612 | **Table:** Mini-Baccarat 8 | **Shift:** Night, 6/12
**Camera(s):** PIT3-11 (primary overhead), PIT3-14 (perimeter, corroborating)
**Classification:** Suspected past-posting (cheating), single documented incident, no prior watch-list match

| Field | Detail |
|---|---|
| Pre-deal wager confirmed | $100, Player spot, frozen frame at "no more bets" call, 21:04:29 |
| Result | Player wins (3rd card exposed 21:04:37.3) |
| Anomaly observed | $500 chip added to Player spot at 21:04:39.6, patron hand entry confirmed on both angles |
| Payout made | $600 (1:1 on apparent $600 wager), 21:04:44 |
| Correct payout | $200 ($100 wager + $100 win) |
| Overpayment | $400 |
| Patron ID | Confirmed via player-tracking sign-in; no prior watch-list match |
| Retention action | Flagged for extended retention same shift; standard 7-day purge does not apply |
| Escalation | Internal security — trespass/ban, watch-list entry. No external referral at this time (single incident, below property felony-referral guidance threshold). Will escalate on repeat. |

**Rule applied:** every field traces to a specific timestamp and camera ID; no field states intent beyond what the two corroborating angles directly show.

## Camera-coverage and retention matrix (filled example)

| Zone | Coverage requirement | Retention baseline | Extension trigger |
|---|---|---|---|
| Table games (each spot) | 2+ angles, chip-denomination legible | 7 days | Any reportable event ($2,500+ dispute, any suspected cheating regardless of amount) |
| Cage windows | Full transaction visibility, currency-count legible | 7 days | Any structuring pattern or CTR-adjacent transaction |
| Count room (soft/hard count) | Continuous, no gaps during active count | 7 days minimum, per-property policy often longer | Any count discrepancy versus expected drop |
| Cage-to-pit chip/cash transport corridors | Full corridor coverage | 7 days | Any single-person ("walked") transport exception |
| High-limit pit | 3+ angles, dedicated dome per table | 7 days | Standing extended-retention policy for all high-limit play regardless of incident |

**Rule applied:** the retention baseline is a floor, not a target — any table or zone touching a reportable-event trigger gets flagged the same shift the trigger occurs, independent of when the report is finished.

## Advantage play vs. cheating — evidence checklist

| Suspected technique | What actually proves it | What does NOT prove it |
|---|---|---|
| Card counting | Bet-size correlation with running count across a statistically meaningful hand sample (hundreds of hands minimum) | A wide bet spread alone, or one lucky session |
| Shuffle tracking | Bet-size correlation with shoe position/clump location post-shuffle | Same as counting — correlation, not spread size, is the evidence |
| Hole-carding | Documented dealer procedural flaw (exposed edge, consistent tell) reproducible on review | The player simply winning at a higher rate than average |
| Past-posting / capping | Frame-by-frame chip movement after result exposure, 2+ angles | A payout that's merely larger than expected without the frame showing the added chip |
| Pinching | Frame-by-frame chip removal from a losing spot before dealer registers the loss | A closing tray shortfall alone, without the specific removal frame |
| Marked cards / daubing | Physical exam of cards flagged from play, correlated with the suspected player's handling | Player behavior alone, however unusual |
| Dealer-player collusion | Repeated pattern (same dealer + same player, multiple shifts) plus a specific missed-collection or overpay frame | A single missed collection, which is more often training error |

**Escalation split:** the left column's first three rows (counting, tracking, hole-carding) route to floor game-protection — a service, bet-spread limit, or dealer-procedure fix, never an accusation. The remaining rows route to security and, once the pattern or amount crosses the property's referral guidance, to law enforcement or the gaming control board.

## AML / structuring notification checklist (surveillance-spotted)

Surveillance frequently sees a structuring pattern on camera — a patron moving between cage windows — before the cage's own end-of-day aggregation system flags it. When observed:

1. Note the patron's identity (player-tracking sign-in or cage ID), each transaction amount, and the window/timestamp for each.
2. Aggregate across the current gaming day and all cage stations — structuring is evaluated against the full-day total, not any single window's transaction.
3. If the aggregate crosses $10,000, or the pattern shows deliberate sub-threshold splitting regardless of the daily total, notify the property's Title 31/compliance officer the same day — do not wait for the cage's own end-of-shift reconciliation.
4. Preserve the camera footage of each transaction window under the same extended-retention rule as any other reportable event.
5. Document the notification (time, recipient, summary) in the surveillance log — the notification itself is part of the evidentiary record if a SAR is ultimately filed.

**Filing clock reference:** a SAR (Suspicious Activity Report) is due within 30 calendar days of the date the pattern was initially detected — the compliance officer owns the filing, but the detection-date clock starts at surveillance's first flagged observation, not at the compliance officer's later review.
