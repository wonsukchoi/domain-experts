# Bellhop / Baggage Porter Playbook

Filled templates and worksheets for the situations that come up every shift: loading a cart, tracking custody of a stored bag, staffing a surge, and splitting a tip pool.

## Cart load-order table

Applied top-to-bottom as items get loaded; guest-requested-accessible items override position regardless of category.

| Position | Item type | Reasoning |
|---|---|---|
| Base (bottom, centered over axle) | Hard-shell cases, trunks, golf/ski bags | Rigid, tolerates weight on top, lowest center of gravity for cart stability |
| Lower-middle | Standard soft-sided suitcases, duffels | Bulk of the weight, still low enough to keep the cart from tipping on a ramp |
| Upper-middle | Garment bags, boxed items, gift bags | Lighter, damage-prone if crushed — sits above the rigid base, not under it |
| Top | Backpacks, small carry-ons, anything guest flagged as "need this on arrival" | Loaded last, off first, no risk of crush damage from items above it |
| Never on the cart | Loose/unbagged fragile items (framed art, instruments without a hard case) | Hand-carried separately regardless of space on the cart |

**Stability check before moving:** cart height should not exceed the pusher's shoulder line; if it does, split into two cart trips rather than stack higher.

## Claim-ticket / storage-room log template

Two-part numbered ticket: stub A stays on the bag in storage, stub B goes to the guest. Log entry at intake:

| Ticket # | Guest name / room (if known) | Item description | Condition noted at receipt | Time in | Staff initials | Time out | Released to |
|---|---|---|---|---|---|---|---|
| 4471 | Guest, R. — Rm TBD (walk-in group) | Black hard-side, 24", small scuff pre-existing on left corner | Photographed, scuff pre-existing | 3:04pm | JT | — | — |
| 4472 | Guest, R. — Rm TBD | Navy duffel | No visible damage | 3:04pm | JT | 3:38pm | Delivered, Rm 412 |

**Reconciliation rule:** at shift change, every ticket with a "Time in" and no "Time out" must correspond to a bag physically present in the storage room. Any mismatch gets escalated to the bell captain before the outgoing shift leaves, not logged for the next shift to discover.

## Group-arrival staffing math worksheet

Fill in before the first cart moves, not after the queue has already built.

```
Total bags expected:            [guest count] x [avg bags/guest] = ___
Cart capacity (bags/trip):      ___
Cart trips needed:              total bags / cart capacity = ___
Avg cycle time (load+deliver+return, min): ___
Total staff-minutes required:   trips x cycle time = ___
Staff currently on floor:       ___
Clearance time at current staffing: staff-minutes / staff on floor = ___ min
Property delivery-time target:  ___ min
Exceeds target? (clearance time > target):  Y / N
If Y — call-in threshold check:  bags in arrival window vs. property threshold
```

**Worked instance (from SKILL.md's example):**

```
Total bags expected:            40 guests x 3 bags = 120
Cart capacity:                  6 bags/trip
Cart trips needed:              120 / 6 = 20
Avg cycle time:                 8 min
Total staff-minutes required:   20 x 8 = 160
Staff currently on floor:       3
Clearance time at current staffing: 160 / 3 = 53.3 min
Property delivery-time target:  20 min
Exceeds target?                 Y — call on-call staff, apply triage
With on-call (4 staff):         160 / 4 = 40 min — still triage the priority tier first
```

**Common call-in thresholds by bell-stand size** (stated heuristics — calibrate to the property's own historical volume, not a universal rule):

| Bell stand size | Call-in trigger |
|---|---|
| 1–2 staff | ~20 bags in 30 minutes |
| 3 staff | ~40 bags in 30 minutes |
| 4+ staff | ~70 bags in 30 minutes |

## Surge triage priority order

When clearance time exceeds the delivery-time target, dispatch carts in this order, not arrival order:

1. Guests with a documented mobility-assist or medical-need flag on the reservation.
2. Top-tier loyalty members (property's highest published tier) and any guest with a same-day time-sensitive commitment noted at check-in (event, flight connection).
3. Standard loyalty members.
4. Walk-in / no-tier guests, remaining group bags to secure storage with claim tickets, rolling delivery.

## Tip-pool points formula (filled example)

Pool splits by points, not flat headcount, to credit peak-shift load and supervisory duty.

```
Base point per hour worked:           1.0
Bell captain / dispatch duty bonus:   +0.25 per hour in that role
Peak-shift multiplier (surge/group arrival hours, as logged): x1.5 on those hours only
```

**Worked instance — one day's pool of $840, three staff:**

| Staff | Hours | Role | Points |
|---|---|---|---|
| Marcus (on-call, surge coverage) | 4 (all surge) | Bellhop | 4 x 1.0 x 1.5 = 6.0 |
| JT | 8 (2 surge, 6 regular) | Bellhop | (2 x 1.5) + (6 x 1.0) = 9.0 |
| Dana | 8 (2 surge, 6 regular), also ran dispatch 3 hrs | Bell captain | (2 x 1.5) + (6 x 1.0) + (3 x 0.25) = 9.75 |

Total points = 6.0 + 9.0 + 9.75 = 24.75
Value per point = $840 / 24.75 = $33.94

Payout: Marcus = 6.0 x $33.94 = $203.64 · JT = 9.0 x $33.94 = $305.45 · Dana = 9.75 x $33.94 = $330.92 (sum reconciles to $840.01, rounding).
