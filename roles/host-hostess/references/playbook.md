# Host stand playbook

Filled templates and worked thresholds for the tools referenced in `SKILL.md`. Numbers below are stated heuristics from full-service floor practice unless a source is named — adapt to a specific house's kitchen ceiling and section layout before relying on them.

## 1. Cover-share tracking sheet

Track covers seated per section against section capacity, updated every time a table sits or clears — not table-count turns, which hide size mismatches.

| Time | Section A (32 seats) | Section B (32 seats) | Section C (32 seats) | House total |
|---|---|---|---|---|
| 6:00 | 8 (25%) | 8 (25%) | 8 (25%) | 24/96 (25%) |
| 6:45 | 20 (63%) | 16 (50%) | 24 (75%) | 60/96 (63%) |
| 7:30 | 24 (75%) | 12 (38%) | 22 (69%) | 58/96 (60%) |
| 8:15 | 26 (81%) | 24 (75%) | 26 (81%) | 76/96 (79%) |

**Reading it:** at 6:45, C is 25 points ahead of B — the next multi-cover party goes to B regardless of which section has a physically ready table, unless a kitchen-pacing conflict overrides it (see §3). By 8:15 the sections should converge toward within ~10 points of each other over a full shift; a section still 20+ points behind by close is a rotation failure worth flagging to the manager, not a one-off.

## 2. Wait-quote calibration

Base estimate by party size, adjusted for house-wide occupancy at the moment of quoting.

| Party size | Base estimate (<70% house) | Base estimate (70–85% house) | Base estimate (>85% house) |
|---|---|---|---|
| 2 | 10 min | 15–20 min | 25–30 min |
| 3–4 | 15 min | 25–30 min | 35–45 min |
| 5–6 | 20 min | 35 min | 50–60 min |
| 7+ | ask manager — rarely walk-in-able at >70% house | | |

**Padding rule:** below 70% house, quote the low end of the range (a beaten quote reads as excellent service). Above 85% house, quote the high end and add a flat +10 minutes — the goal is a number the guest beats by walking to the table five or ten minutes early, not a number you hit exactly.

**Quote-breach check, every 5 minutes on the wait list:**

```
elapsed / quoted > 1.15  →  breach — seat at next appropriately-sized table, ahead of rotation
elapsed / quoted > 1.00  →  approaching — proactively update the guest with a revised number
elapsed / quoted ≤ 1.00  →  on track — no action
```

Example: quoted 20 minutes at 7:00, now 7:24 → 24/20 = 1.20 → breach, seat next.

## 3. Kitchen large-party spacing

Track every 6+-top ticket fired, independent of section — this is a whole-kitchen constraint, not a per-section one.

| Ticket # | Time fired | Section | Gap from prior | Status vs. 15-min floor |
|---|---|---|---|---|
| 1 | 7:05 | C | — | — |
| 2 | 7:19 | C | 14 min | -1 min (below floor, already tight) |
| 3 | 7:41 (held) | B | 22 min | +7 min (47% over floor) |

**Rule:** if the next 6+-top would fire within the stated floor (commonly 12–15 minutes for a full-service line — confirm the actual number with the kitchen, it varies by menu complexity and station count), buy the gap at the door:

- Hold the party at the stand a genuine 3–7 minutes ("let me get your table finished") rather than seating immediately.
- If holding isn't viable (party is visibly agitated, or a table opens faster than expected), flag the ticket to expo by name so the kitchen can stagger fire time instead of firing on arrival.
- Never solve a pacing conflict by moving the party to a different section — the kitchen doesn't care which section fired the ticket, only how many large tickets land in the window.

## 4. Reservation grace-period matrix

| Restaurant type | Grace period | Notes |
|---|---|---|
| Casual full-service | 15 min | Standard walk-in pressure; release and rebook to waitlist at 15. |
| Upscale/contemporary | 15 min, extendable 5 more if no comparable walk-in is waiting | Matches the worked example in `SKILL.md`. |
| Fine dining, high covers-per-hour | 10 min | Tighter turn windows make a held table more costly; call the guest at 8–9 minutes if a phone number is on file. |
| Party of 6+ | 10 min, call immediately at grace start | Large-party no-shows cost the most rotation damage; don't wait out the full window silently. |

**Fallback order when a reservation is late:** (1) call the phone number on file at grace-period start if one exists; (2) hold to grace-period end if no comparable walk-in has breached its quote; (3) release and offer the table to the longest-breached appropriately-sized walk-in; (4) if the late party arrives after release, rebook them at the next opening and apologize once, without re-litigating whose fault the timing was.

## 5. Table-combining reference

| Combine | Result | Use when |
|---|---|---|
| Two 2-tops (adjacent) | 4-top | Party of 3–4 walk-in during low occupancy; splits back to two 2-tops the moment it clears. |
| Two 4-tops (adjacent) | 6–8 top | Party of 6–8; hold one such pair per section unassigned during peak so a large-party surge doesn't strand a section without a big enough table. |
| 4-top + 2-top | 6-top (uneven, workable) | Party of 5–6 when no matched pair is free; slightly awkward seating but faster than waiting for a matched combine. |

**Rule of thumb:** never combine the *last* available pair in a section during peak unless a large party is already at the door — combinable capacity is emergency capacity, and using it early removes the fallback for the next large party that shows up unannounced.

## 6. Walk-in holdback

Even at a fully-booked reservation night, hold back roughly 15–20% of total seats as unbooked walk-in inventory (some of this is structural: reservation no-show rates commonly run in the 10–20% range without a card-on-file deposit, lower with one). A house that books 100% of seats on paper routinely ends up 10–20% empty in practice when no-shows land — and has nothing to offer the walk-in line in the meantime. Card-on-file or deposit-backed reservations reduce no-show rates and let a house safely book a higher percentage of seats.
