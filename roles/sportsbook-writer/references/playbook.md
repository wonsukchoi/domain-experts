# Sports book writer playbook

Filled, executable procedures — populate with real numbers, don't describe them.

## 1. Ticket-write checklist (window)

For every wager, in order:

1. Confirm the event is on the board (not circled, not past cutoff, not already graded).
2. Read the live number off the board at the moment of the bet: spread/total/moneyline + juice.
3. Confirm bet type and stake with the patron verbally before keying it in: *"Cowboys minus 3, minus 110, for how much?"*
4. Key the ticket, print, and hand the patron copy over — the book copy and system record are the control; the printed ticket is the patron's only proof.
5. For a same-game or correlated multi-leg ticket, confirm the system's correlation block didn't silently reject a leg — a parlay that printed with fewer legs than requested is a write error, not an accepted smaller parlay.

## 2. Standard fixed-odds parlay/teaser payout card

Widely used baseline (per-leg −110 spread/total convention; a book's actual posted card is the source of truth and can differ):

| Teams | Payout (to 1) |
|---|---|
| 2 | 13/5 (2.6) |
| 3 | 6/1 |
| 4 | 10/1 |
| 5 | 20/1 |
| 6 | 40/1 |
| 7 | 75/1 |
| 8 | 150/1 |

**Push-inside-a-parlay rule:** a push leg is removed and the parlay reprices to the next-lower team count at the *original stake* — a 4-team parlay with one push becomes a 3-team parlay at the card's 3-team number, not a cancelled ticket and not a straight recompute of the 4-team price minus one leg.

Worked example: $20, 5-team parlay, one leg pushes. Repriced as a 4-team parlay at 10/1: payout = $20 × 10 = $200 win + $20 stake = $220 total, versus what a junior might wrongly do — drop straight to the 5-team number pro-rated, which isn't how the card works.

## 3. Moneyline payout quick math

- **Negative odds (favorite),** e.g. −150: win = stake × (100 / 150). A $150 bet at −150 wins $100.
- **Positive odds (underdog),** e.g. +240: win = stake × (240 / 100). A $50 bet at +240 wins $120.
- **Implied probability** — negative odds: |odds| / (|odds| + 100). Positive odds: 100 / (odds + 100). A −110/−110 two-sided line implies 52.4% + 52.4% = 104.8%, i.e., a ~4.8% book hold (vig) built into a standard spread line.

## 4. W-2G two-part test worksheet

Run both lines for every win; a "yes" on only one line does not trigger the form.

| Ticket | Wager | Winnings | Winnings ≥ $2,000? | Winnings ÷ Wager ≥ 300x? | W-2G? |
|---|---|---|---|---|---|
| A | $500 | $2,750 | Yes | 5.5x — No | **No** |
| B | $10 | $400 | No | 40x — No | **No** |
| C | $8 | $2,400 | Yes | 300x — Yes | **Yes** |
| D | $2,500 | $7,500 | Yes | 3x — No | **No** (but check $5,000/24% backup-withholding rule separately) |

Row D shows the second, independent trigger: winnings clearing the $5,000 mark carry a 24% federal backup-withholding question even when the 300x multiplier test (and therefore the W-2G reporting test) fails — the two rules are checked separately, not as one combined threshold.

## 5. Betting cutoff / past-posting control

- Posted cutoff time for each event is set before the event and displayed on the board — not "kickoff" or "first pitch" from memory.
- At cutoff, the event moves to "off the board" in the system; the system should block further ticket writes, but the writer is still the last check — a system lag is not authorization to write a late bet.
- Any request to write a bet after off-the-board status, regardless of the reason given, gets declined and logged (patron, time, event, reason given) — the log matters even when nothing was written, because a pattern of attempts is itself the signal.

## 6. Shift open/close reconciliation

**Open:** count incoming bank against prior shift's close and the ticket log; resolve any discrepancy before accepting the window.

**During shift:** every ticket written increases outstanding liability; every ticket graded and paid reduces it. Outstanding liability = sum of all unsettled tickets' potential payout, tracked continuously, not estimated at close.

**Close:** reconcile cash on hand against (opening bank + cash accepted on wagers − cash paid on graded winners − transfers to cage), and separately reconcile the open-ticket log against the system's outstanding-liability report. A cash variance and an open-ticket variance are two different problems — don't let one investigation stand in for the other.

Worked example: opening bank $5,000. Wagers accepted (cash) $18,400. Winning tickets paid $14,600. Transfer to cage $3,000 mid-shift. Expected close: 5,000 + 18,400 − 14,600 − 3,000 = **$5,800**. If the physical count is $5,750, the $50 shortage gets retraced against the ticket log by time before it's escalated — most variances trace to a specific mis-keyed ticket, not theft.

## 7. Layoff request

When a book's exposure on one side of an event exceeds its internal limit (set by the book manager, not the writer), the writer routes a layoff request up the chain rather than declining further action outright: state the event, the side, the current handle imbalance, and the amount needed to lay off. Example escalation note: *"Chiefs −3 handle is $42,000 to $11,000 Broncos side; requesting authorization to lay off $8,000 of Chiefs exposure before we move the number."* The decision to move the line, cut the limit, or lay off is the book manager's call — the writer's job is surfacing the imbalance with the actual numbers, not sitting on it.
