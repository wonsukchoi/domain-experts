# Playbook

Filled operational templates a pit boss runs every shift. Starting points to adapt to a specific property's MICS and signing-authority policy, not scripts.

## 1. Shift-open inventory count

Done at the table before the first hand, with the outgoing/incoming dealer or a witness present — never solo.

```
TABLE: 8 (Pit 2, 6-deck BJ, $25 min)          SHIFT: Swing, 15:00
OPENING INVENTORY (by denomination):
  $100 (black):  40 chips = $4,000
  $25  (green):  80 chips = $2,000
  $5   (red):   400 chips = $2,000
  $1   (white): 400 chips = $  400
  TOTAL:                    $8,400
COUNTED BY: dealer (incoming)      WITNESSED BY: pit boss (signature)
DISCREPANCY vs. prior shift close: $0 — cleared
```

**Tolerance:** any discrepancy over $25 at open or close gets a written note and a call to the shift manager before the table opens — not "we'll true it up later." Recurring small discrepancies (three or more shifts in a rolling two weeks) on the same table or dealer escalate regardless of individual size.

## 2. Fill/credit authority ladder

Signing authority is cumulative and per-session, not just per-slip — a pattern of maximum-size requests exceeds authority even if each slip is individually within the dollar limit.

| Request | Pit boss alone | Requires shift-manager co-sign | Requires cage/credit manager |
|---|---|---|---|
| Single fill/credit ≤ $2,500 | Yes | — | — |
| Single fill/credit $2,501–$5,000 | — | Yes | — |
| Single fill/credit > $5,000 | — | Yes | Yes |
| 3rd+ fill on one table in a session with fill:credit ratio ≥ 3:1 | — | Yes (regardless of dollar size) | — |
| New marker or credit-line increase | — | — | Yes |
| Marker draw against existing approved line | Yes, if within line | — | — |

**Rule of thumb:** the dollar threshold governs the routine case; the *pattern* threshold (repeated max fills, one dealer, no surveillance note) governs the case the dollar limit alone would wave through.

## 3. Dealer rotation schedule

Built around 20–40 minute deal windows on active games, break windows staggered so no table drops below minimum staffing.

```
PIT 2 — SWING SHIFT (15:00–23:00), 4 tables, 5 dealers on roster

15:00–15:40  Table 6: Dealer A   Table 7: Dealer B   Table 8: Dealer C   Table 9: Dealer D
15:40–16:20  Table 6: Dealer B   Table 7: Dealer C   Table 8: Dealer D   Table 9: Dealer E
16:20–17:00  Table 6: Dealer C   Table 7: Dealer D   Table 8: Dealer E   Table 9: Dealer A
  (Dealer A: 20 min break)
...continues in rotation, 20-min deal / break offsets staggered by table...

HIGH-LIMIT TABLE OVERRIDE: Table 9 rotates every 20 min, not 40 —
  high-limit games get the shorter window regardless of volume.
```

**Fatigue check:** if a dealer's hands-per-hour drops more than ~20% below their rolling average mid-window, pull them for the next scheduled break early rather than holding them to the clock.

## 4. Incident escalation matrix

| Signal | Stays at pit level | Shift manager | Security / surveillance formally |
|---|---|---|---|
| Dealer misdeals, minor procedure slip, corrected same hand | Yes (coach + log) | — | — |
| Payout dispute, trivial amount (< ~$25), dealer certain | Yes (rule + log) | — | — |
| Payout dispute, > ~$25 or either party disagrees | — | Yes | Footage pull only |
| Fill/credit pattern flag (3:1 ratio, no prior note) | — | Yes | Footage pull |
| Suspected past-posting / dealer procedure breach, single incident | — | Yes | Yes |
| Suspected collusion, team play, or advantage-play scheme | — | Yes | Yes, formal report |
| Structuring pattern on MTL (repeated sub-$10k buy-ins, same patron) | — | Compliance notified | — |

## 5. Theoretical-win (ADT) rating table

Filled example for a comp decision — rate the session, not the buy-in.

```
PLAYER: Card #4471   GAME: 6-deck BJ, Table 8   SESSION: 2.5 hrs
Average bet (observed, per hand):        $150
Hands per hour (table average):           65
House edge (basic strategy assumed):    0.75%

Theoretical win = $150 × 65 × 2.5 × 0.0075 = $182.81

COMP GUIDELINE: table games reinvest 15–30% of theo depending on tier.
  Mid-tier player → 20% → comp value ≈ $36.56 for this session.

CROSS-CHECK: buy-in this session was $2,000 — buy-in size alone would
  over-rate this player by roughly 11x theo. Rate off average bet and
  duration, never off buy-in.
```

**Escalation trigger:** any single session theo over the property's high-roller threshold (commonly $2,500+/hour) routes the comp decision to the host/casino manager rather than the pit boss approving it directly.
