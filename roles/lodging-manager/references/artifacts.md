# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual RevPAR analysis, overbooking calc, or displacement analysis — not for general reasoning (that's `SKILL.md`).

## RevPAR / rate-change impact worksheet

```
Current state: ADR $185, Occupancy 78%, Rooms 150
Current RevPAR = $185 × 0.78 = $144.30
Current revenue (per night) = $144.30 × 150 = $21,645

Proposed rate change: -$15 (to $170)
Projected occupancy response (from historical elasticity or RMS model): +6 pts (to 84%)
Projected RevPAR = $170 × 0.84 = $142.80
Projected revenue (per night) = $142.80 × 150 = $21,420

Verdict: rate cut projected to LOWER RevPAR by $1.50/room ($225/night total) despite higher
occupancy — do not make this change unless there's a non-revenue reason (e.g., building future
loyalty, clearing distressed inventory before a hard cutoff date).
```

## Overbooking calculation

```
Date: [Saturday, 3 weeks out]
Rooms available: 150
Current bookings on the books: 138 (92% forecast occupancy)
Historical no-show/cancellation rate for this day-of-week/season: 4%
Expected no-shows = 138 × 0.04 = 5.5, round to 5-6 rooms

Overbooking recommendation: overbook to match expected no-show count (5-6 rooms), NOT beyond it
unless there's a specific reason to believe this date's no-show rate will exceed the historical
average (e.g., unusually firm demand from a local event suggests LOWER no-show rate, which argues
for LESS overbooking, not more).

Walk-guest recovery protocol (must be confirmed BEFORE overbooking, not improvised if a walk occurs):
  - Relocation partner property confirmed: [name, rate agreement]
  - Transportation to relocation property: [arranged/reimbursed]
  - Compensation tier authorized without manager approval: [e.g., one free night credit + $50 F&B]
  - Front desk script for walk conversation: [prepared]
```

## Channel net-rate comparison

```
Channel      | Gross ADR | Commission % | Net rate to property | Booking volume (room-nights)
-------------|-----------|--------------|------------------------|------------------------------
Direct       | $160      | 0%           | $160.00                | 40
OTA A        | $180      | 18%          | $147.60                | 65
OTA B        | $175      | 22%          | $136.50                | 30
GDS/corporate| $170      | 10%          | $153.00                | 25

Blended net ADR = weighted avg of net rates = 
  (160×40 + 147.60×65 + 136.50×30 + 153×25) / 160 = $150.86

Decision lens: shifting 10 room-nights from OTA B to Direct (via a direct-booking incentive costing
less than the 22% OTA B commission) improves net revenue even if it requires a modest rate
discount or loyalty incentive to achieve the shift.
```

## Group block displacement analysis

```
Group request: 20 rooms @ $145/night for [Saturday date]
Forecast transient ADR for that date (from current booking pace): $210/night
Forecast transient demand for that date (from pickup curve): sufficient to fill those 20 rooms
  at $210 with [X]% confidence based on current pace

Displacement cost = (Transient ADR − Group rate) × Room-nights
                   = ($210 − $145) × 20 = $1,300 revenue loss for the date if transient demand
                     would have filled those rooms anyway

Additional group considerations (not purely financial):
  - Group's F&B/ancillary spend: $[estimate] — may partially offset room-rate displacement
  - Relationship/future-business value of the group organizer: [qualitative]

Recommendation: decline for this specific high-demand date; offer group organizer an alternate
date with lower forecast transient demand where displacement cost is near zero.
```
