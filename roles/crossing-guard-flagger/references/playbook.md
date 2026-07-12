# Playbook

Filled worksheets and protocols a guard or flagger actually runs on site — starting points to adapt to the specific location, not scripts to follow blind.

## 1. Taper length and device count, by speed

Formula selection: **S ≥ 45 mph → L = W × S**. **S < 45 mph → L = W × S² ÷ 60.** W = width of the offset in feet, S = operating speed in mph (posted, 85th-percentile, or anticipated — whichever is higher). Device spacing within the taper is capped at S feet (e.g., 40 mph → 40 ft max spacing).

| Offset W (ft) | Speed S (mph) | Formula | Taper length L | Max device spacing | Devices (L ÷ spacing + 1) |
|---|---|---|---|---|---|
| 10 | 25 | WS²/60 | 10×625/60 = 104 ft | 25 ft | 5 |
| 12 | 35 | WS²/60 | 12×1225/60 = 245 ft | 35 ft | 8 |
| 12 | 45 | W×S | 12×45 = 540 ft | 45 ft | 13 |
| 12 | 50 | W×S | 12×50 = 600 ft | 50 ft | 13 |
| 11 | 60 | W×S | 11×60 = 660 ft | 60 ft | 12 |

Shifting tapers use L/2; shoulder tapers use L/3 — but the merging taper length L is always computed first from the full offset width, then halved or thirded, never estimated directly.

**Check before placing a single cone:** does the calculated L actually fit the available sightline (no blind curve/crest inside that distance)? If not, the fix is moving the advance warning sign further upstream — the taper length itself doesn't shrink to match a bad sightline.

## 2. Two-flagger radio protocol

Used whenever a closure has two control points without unbroken line of sight (curve, grade, or closure length beyond visual signal range — roughly 1,000 ft as a practical ceiling for hand-signal visibility in daylight).

**Fixed call sequence (both flaggers use the same script every cycle):**

```
Downstream flagger (controls release into the work space):
  "Downstream clear, ready for release" — when work space is empty and safe to receive traffic.

Upstream flagger (controls the stopped queue):
  "Upstream releasing, [N] vehicles" — states the count being sent through, so downstream
  knows when the group has fully cleared before calling the next release.

Downstream flagger, after the stated count has passed:
  "Group clear, standing by" — confirms receipt before upstream repeats the cycle.
```

**Rule:** upstream never releases a second group before downstream confirms "group clear" for the first — this is what prevents a queue-to-queue pileup in the activity area when one flagger can't see the other's queue.

**If radio contact is lost:** both flaggers default to full stop and hold until contact is restored or a third person relays by sight between them. Never resume alternating release on assumption.

## 3. School-crossing gap-count worksheet (filled example)

Used to decide whether a crossing needs an adult guard, a signal, or neither. Run during the actual arrival or dismissal window (not an off-peak count) for 15–30 minutes.

```
LOCATION: Maple St / 4th Ave, elementary school west crosswalk
WINDOW: 7:40–8:00 AM (20 min), dismissal counted separately at 3:00–3:15 PM
POSTED SPEED: 25 mph   MEASURED 85th PCTL: 29 mph

Vehicle count (both directions):        142 vehicles / 20 min
Pedestrian groups waiting to cross:      31 groups / 20 min
Safe gaps observed (≥ group's crossing
  time with no vehicle approaching):     14 gaps / 20 min → 0.7 gaps/min

THRESHOLD: 1.0 safe gap/minute (ITE School Trip Safety Program Guidelines)
RESULT: 0.7 < 1.0 → crossing does NOT reliably self-clear during the peak window.

RECOMMENDATION: Assign adult crossing guard for AM and PM windows.
Reassess in one semester; if 85th-percentile speed measurement rises above
29 mph or gap rate drops further, escalate to signal-warrant study —
a guard is a staffing fix for a marginal shortfall, not a substitute for
an engineering fix if the shortfall is severe or worsening.
```

## 4. Speed-and-visibility device selection table

Run this before every new site assignment, not just once per program:

| Operating speed | Apparel class | Taper formula | Notes |
|---|---|---|---|
| Any speed, dusk/dawn/low visibility | Class 3 | per speed below | Visibility overrides the speed threshold |
| < 45 mph, daylight | Class 2 (min.) | WS²/60 | Class 3 always acceptable as an upgrade |
| ≥ 45 mph | Class 3 | WS | No exceptions for daylight at this speed |

## 5. Pre-shift station checklist (filled)

```
SITE: [location]                DATE/SHIFT: [___]
[ ] Operating speed confirmed (posted / 85th-pctl / anticipated): ___ mph
[ ] Sightline walked both directions — obstruction noted: ___
[ ] Device set matches speed/visibility table above
[ ] Taper length and spacing calculated (not estimated) and marked
[ ] Escape route identified and clear at each station
[ ] Second station in radio contact (if applicable) — call sequence confirmed
[ ] Fixed reference point selected for judging vehicle speed/compliance
[ ] Prior incident log reviewed for this location before shift start
```
