# Crane and Tower Operator — Playbook

Filled reference sequences: wind-derate calculation for sail-area-heavy loads, load-chart check against a fixed installed configuration, blind-lift radio protocol, and two-crane load-share math.

## 1. Wind-derate calculation for a specific load

OEM charts commonly state the in-service wind rating as a 3-second gust at the jib head, calibrated to a reference wind-exposed-area-to-weight ratio (illustrative figure, always confirm the actual installed crane's chart):

| Chart input | Example value |
|---|---|
| Rated in-service gust limit (chart flat number) | 9 m/s (≈20 mph) |
| Reference sail-area-to-weight ratio the rating assumes | 1.2 m²/tonne |
| Out-of-service (free-slew/weathervane) limit | commonly 2–3x the in-service figure, confirm per model |

**Working steps:**

1. Compute the load's actual sail-area-to-weight ratio: wind-exposed area (m²) ÷ load weight (tonnes). Include any large-surface rigging (spreader frames, vacuum lifters) in the area figure, not just the load itself.
2. Divide the load's ratio by the chart's reference ratio to get the ratio multiple (e.g., 4.8 ÷ 1.2 = 4.0x).
3. Take the square root of that multiple — wind force scales with velocity squared and directly with area, so holding force constant means allowable velocity scales inversely with the square root of the area multiple.
4. Divide the chart's flat gust rating by that square-root factor to get the load-specific derated limit (e.g., 9 m/s ÷ 2.0 = 4.5 m/s).
5. Compare the derated limit against the current 3-second gust peak at the jib head — not a sustained average, and not a ground-level reading, which reads materially lower than conditions at hook height.
6. If the load's ratio is at or below the chart's reference ratio, the flat chart rating applies unmodified — this derate only matters once a load's sail area is materially disproportionate to its weight.

**Reference ratio table for common load types (illustrative — always confirm against the load's actual dimensions):**

| Load type | Typical sail-area-to-weight ratio |
|---|---|
| Compact steel member, precast beam | 0.3–0.8 m²/t |
| Chart's typical reference load | ~1.2 m²/t |
| Glazed curtain-wall panel | 3–6 m²/t |
| Plywood/MDO formwork panel, empty basket | 6–15 m²/t |

## 2. Load-chart check against the installed configuration

A tower crane's chart is a function of the jib length and counterweight set actually erected — not a menu the operator can pick from mid-job:

| Installed configuration | Max radius (jib tip) | Max capacity at 12 m (near mast) | Capacity at 40 m |
|---|---|---|---|
| 60 m jib, 6-block counterweight (illustrative) | 60 m | 12,000 kg | 4,300 kg |
| 60 m jib, 8-block counterweight (illustrative) | 60 m | 12,000 kg | 5,100 kg |

**Working steps:**

1. Confirm which counterweight set is actually installed (physical block count, not the erection drawing) before pulling a chart page — a chart page for a different counterweight configuration does not apply, even on the same jib length.
2. Read the exact radius the load requires; tower crane charts are non-linear between listed radii the same way a mobile crane's is — read the actual line, never interpolate.
3. Net the load against listed capacity after rigging deductions (hook block, spreader, slings), same convention as any crane chart.
4. If the required radius exceeds what the installed configuration supports, the fix is one of: (a) a documented reconfiguration (adding counterweight, if the mast and foundation are engineered for it), (b) substituting a different lift method for that specific pick (mobile crane, material hoist), or (c) declining the pick as planned. There is no "reposition the crane" option once erected.
5. Log any chart-fit failure with the specific radius and configuration to the crane engineer or erector immediately — a documented reconfiguration takes engineering lead time, so early flagging matters more on a fixed installation than on a mobile crane that can solve it same-shift.

## 3. Blind-lift radio protocol

1. Before the pick starts, confirm with the signal person which segments of the path are blind to the cab (pick point, path, set point — independently, since a load can be visible mid-swing and blind at either end).
2. For every blind segment, require a distinct call-and-repeat exchange for each motion type (raise, slew, trolley-in/out, lower) — the signal person calls the motion and the specific action ("slew right, five degrees"), the operator repeats it back before executing, and only then moves.
3. Treat a single "you're clear" issued once at the start of a multi-motion blind segment as covering that moment only — it does not certify motions that follow, since conditions (a worker stepping into the zone, wind shifting the load) can change between calls.
4. If radio contact is lost at any point during a blind segment, hold all motion immediately and do not resume until contact is confirmed restored — a motion "already started" on an earlier confirmed call is not validated for conditions since that call.
5. If the signal person's own sightline is lost (obstruction, distance, low light), the signal person calls a hold, not a best-guess continuation — the operator has no independent way to know the sightline was lost unless told.
6. Log any blind-segment near-miss (missed repeat-back, radio drop, sightline loss) immediately with the specific segment and motion, not a general note — this is the data that changes the crew's radio discipline going forward.

## 4. Two-crane (tandem) load-share calculation

For a shared pick between Crane A and Crane B, with pick points a known distance apart and the load's center of gravity (CG) somewhere between them:

```
Crane A share = Total load weight × (distance from CG to Crane B's pick point ÷ total distance between pick points)
Crane B share = Total load weight − Crane A share
```

**Worked figures (illustrative):**

- Total load: 18,000 kg precast wall panel.
- Pick points 10 m apart; CG measured 4 m from Crane A's pick point (6 m from Crane B's).
- Crane A share = 18,000 × (6 ÷ 10) = 10,800 kg.
- Crane B share = 18,000 − 10,800 = 7,200 kg.

**Working steps:**

1. Confirm CG location from the engineered rigging plan, not a field estimate — a shifted CG estimate changes both cranes' share numbers, not just one.
2. Calculate each crane's share using the formula above before either crane takes tension.
3. Check each crane's share against its own chart capacity at its own working radius, derated to a ceiling below 100% (commonly 75% of chart capacity per crane, tighter if the CG estimate carries stated uncertainty) — the derate absorbs the risk that the actual CG differs from the engineered estimate once the load comes off the ground.
4. If either crane's share exceeds its derated ceiling, the fix is repositioning pick points to shift the geometry (if achievable) or bringing in a higher-capacity crane for that position — never proceeding on the assumption that "it'll settle out even."
5. Coordinate hook speed between the two operators throughout the pick — one crane hoisting faster than the other shifts the load's effective angle and can silently transfer more of the actual load onto whichever crane is lagging, regardless of the calculated share.
6. Log the calculated share, the derated ceiling, and each crane's actual working radius before the lift begins, so both crews are executing against the same numbers.
