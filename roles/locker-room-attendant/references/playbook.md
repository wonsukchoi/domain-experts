# Playbook

Filled operational tools an attendant or shift lead actually runs, not descriptions of them.

## 1. Claim-check setup (event coat check)

Set up before doors, not during rush.

**Ticket/tag pairing:** sequential numbered tags, two-part (stub to patron, matching tag pinned/clipped to the item). Never reuse a number within the same event, even if an item is retrieved early — pull that number from rotation for the night.

**Staffing table (example: 300-guest gala, 8pm–1am):**

| Window | Expected activity | Attendants on |
|---|---|---|
| 7:30–8:45pm | Intake surge, ~250 of 300 items checked | 4 |
| 8:45–11:30pm | Steady trickle, early departures | 2 |
| 11:30pm–12:15am | Retrieval surge, ~70% of items reclaimed in 45 min | 4 |
| 12:15–1:00am | Final retrieval, reconciliation | 2 |

Ratio used: ~1 attendant per 75 items at intake and retrieval peaks, dropping to 1:150 during the steady middle window.

**High-value item protocol:** if a patron discloses a valuable at check-in (fur, watch left visible, a bag they mention contains jewelry), offer the separate high-value tag: item goes in a locked cabinet or safe, cross-referenced on both the item tag and a duplicate log with a manager's initials. A declined offer is noted on the standard tag ("HV declined, initials ___") — this note is what makes the liability cap defensible later.

**Damage-at-intake note:** any pre-existing damage (torn lining, missing button) gets written on the tag itself in front of the patron before the item leaves their hands. Skipping this is the single most common cause of a disputed damage claim at pickup.

## 2. Par-level worksheet (towels, robes, linens)

Formula: **Par = (Daily usage ÷ laundry cycles per open day) × 1.20–1.25 buffer**

Filled example, health club locker room:

| Item | Daily uses (avg) | Cycles/day | Baseline (uses ÷ cycles) | Par (×1.25) | On-hand target |
|---|---|---|---|---|---|
| Bath towels | 480 | 4 | 120 | 150 | 150 |
| Hand towels | 300 | 4 | 75 | 94 | 95 |
| Robes (spa) | 60 | 2 | 30 | 38 | 40 |

**Reorder trigger:** flag to laundry vendor or purchasing when on-hand count drops below 60% of par mid-cycle (e.g., bath towels below 90 before the next scheduled pickup) — waiting until the count hits zero means the shortfall is already visible to members.

**Seasonal/event adjustment:** tournament days, holiday weekends, or any day with >130% of average daily visits: recalculate using that day's projected usage, not the trailing-30-day average — a standing par sized for a normal Tuesday will run out by mid-morning on a peak day (see SKILL.md worked example).

## 3. Incident report template (filled — theft/loss)

```
INCIDENT REPORT — [Venue] Locker Room / Coat Check
Date: [date]          Time reported: [time]          Attendant on duty: [name]

CUSTODY CLASSIFICATION (check one):
[ ] Attended/bailed — house held item behind counter or in staffed cage
[X] Self-service — patron controlled own lock/key, no staff custody
[ ] High-value disclosed item, separate tag/safe

ITEM: [description, patron's stated value]
LOCATION: [locker # / coat tag # / row]
TIME WINDOW: item last confirmed present [time] — reported missing [time]

PATRON ACCOUNT: [verbatim or close paraphrase, get it in writing/signed if possible]

INTAKE RECORD CHECK: [does the intake log show any pre-existing note, damage,
  disclosure, or HV-declined mark for this item/locker?]

CAMERA COVERAGE: [requested Y/N, from whom, timeframe]

LIABILITY POSITION: [state law/policy basis — e.g., "self-service, no bailment
  created, posted signage at [location] disclaims liability; no reimbursement
  offered pending evidence of staff negligence or forced entry"]

NEXT STEPS: [police report offered Y/N, security footage review, follow-up owner]
FILED BY: [name]                REVIEWED BY: [manager, date]
```

## 4. Shift-close reconciliation sheet

Run every shift, coat check or locker room, no exceptions:

```
Tickets issued: [count]        Tickets returned/matched: [count]
Unclaimed items remaining: [count] → logged to lost & found with date + 
  retention deadline (standard: 30 days before donation/disposal, 90 days 
  for anything above the HV threshold)
Cash/tip pool collected: $[amount]   Attendants sharing pool: [count]
  → Per-attendant tip share: $[amount ÷ count]
  → Hourly tip rate: $[per-attendant share ÷ hours worked]
  → Combined with base wage: confirm total meets or exceeds applicable
    minimum wage before applying any tip credit
Discrepancies (ticket count vs. items on hand): [count, and note whether
  investigated same shift or escalated]
Signed off: [attendant] / [supervisor]
```

**Worked example (referenced in SKILL.md):** 3 attendants, 5-hour gala shift, $186 tip pool collected. Per-attendant share: $186 ÷ 3 = $62. Hourly tip rate: $62 ÷ 5 hours = $12.40/hr. Base wage $16/hr. Combined effective rate: $16 + $12.40 = $28.40/hr — logged on the reconciliation sheet so payroll can confirm the tip credit math against the jurisdiction's minimum-wage floor.
