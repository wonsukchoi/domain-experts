# Fast food station playbook

Filled reference tables and worked drills for a franchise grill/fry/assembly station. Numbers are representative build-to-spec figures drawn from published QSR operations literature and equipment-industry guidance, not one specific chain's proprietary manual — recalibrate against the store's actual posted spec sheet.

## Build card — "Classic Cheeseburger" (worked example)

| Step | Action | Spec detail | Tolerance |
|---|---|---|---|
| 1 | Toast bun crown | 350°F platen, 12–15 sec | Visual: light gold, no dark edges |
| 2 | Drop patty | Clamshell grill, both sides simultaneously | 90 sec total, 400°F platen |
| 3 | Squeeze sauce (crown) | Ring pattern, edge to center | ~0.5 oz, full ring coverage |
| 4 | Place cheese | On patty immediately off grill | 1 slice, corner-to-corner square |
| 5 | Place pickles | 2 slices, centered | ± 0 — short a pickle is a remake, not a judgment call |
| 6 | Place onion (if spec'd) | Diced, 1 portion-scoop | Scoop-level, not "a pinch" |
| 7 | Close and wrap | Heel first, crown last | Wrap within 30 sec of patty coming off grill |

The sequence matters independent of taste: sauce goes on the crown *before* the bun sits in a warming cabinet or holding bin, because sauce-then-hold changes moisture absorption into the bun in a way the reverse order doesn't — the audit checks the assembled sandwich against a reference photo, and a reversed layer order is visible in cross-section on a photo-match check even when the flavor is identical.

## Hold-timer reference table

Every batch gets a timer or colored sticker set at the moment it finishes cooking, not at the moment it's bagged.

| Item | Hold start trigger | Quality-hold window | Action at expiration |
|---|---|---|---|
| French fries | Basket pulled from oil | ~7 min | Discard — no exceptions without a logged equipment-fault note |
| Grilled beef patty (under heat lamp/holding bin) | Off the grill | ~20 min | Discard |
| Breaded/fried chicken patty or tenders | Off the fryer | ~45 min | Discard |
| Assembled sandwich (wrapped, in bin) | Wrap complete | ~10 min | Discard — separate from the patty's own hold clock |
| Hash browns (breakfast daypart) | Off the fryer/griddle | ~15 min | Discard |

These windows are shorter than the food-safety cumulative-time limit (TCS food between 41–135°F: 2 hours to use or refrigerate, 4 hours to discard, per ServSafe/FDA Food Code) because the hold-timer is a *quality* control, not a safety control — a fry held at 135°F+ is still legally safe well past 7 minutes, but it's no longer the product the brand sells.

## Fryer oil TPM reference

| TPM% reading | Status | Action |
|---|---|---|
| Under 16% | Fresh/good | No action |
| 16–20% | Degrading, still serviceable | Monitor, plan next scheduled change |
| 20–24% | Approaching threshold | Schedule oil change at next lull |
| 24%+ | At/past discard threshold | Change before the next basket drops, no exceptions except a logged short-cycle-to-finish-forecast exception |

Test with a handheld TPM meter dipped directly into the vat, not by color or a fixed hours-of-use count — two fryers running identical hours can read 6 points apart in TPM depending on what's been fried in them (breaded/battered items break oil down faster than plain fries).

## Drive-thru queue math (worked drill, second scenario)

Lunch rush, single lane, 75 cars over 45 minutes (75 ÷ 45 = 1.67 cars/min, or one every 36 seconds). Store's total-time target: ≤180 seconds. A mid-rush spot-check clocks the last 10 cars at an average total time of 165 seconds.

Applying Little's Law (L = λW): average cars in the system at once = λ × W = (75 ÷ 45) × 165 = 1.67 × 165 = 275.5 car-seconds ÷ 60 = 4.6 ≈ 5 cars in the system on average (in line, at the window, or at the payment station) — consistent with what the lane camera shows (typically 4–6 cars visible across the ordering, paying, and presenting stages during this rush).

If the same 10-car sample instead averaged 220 seconds (over target), the same formula gives L = 1.67 × 220 = 367 ÷ 60 = 6.1 ≈ 6 cars — visibly longer line, and the store's scorecard would flag the rush as a speed-of-service miss even though the total car count (75) didn't change. This is the number a shift lead pulls to decide whether to add a second window runner *before* the line visibly backs up onto the street, not after.

## Shift log entry (filled example)

```
Date: Fri PM rush, 5:00–6:00
Cars served: 90 | Fry orders: 45 | Baskets dropped: 5 (12-min cadence)
Timer exceptions: 1 (basket #2, discarded 1 min past 7-min window; override request from shift lead declined, logged)
Speed-of-service: avg total time 178 sec (2 cars affected by basket-gap, est. ~360 sec each)
TPM at close: 19% — no change needed
Build-card deviations: none
Next-shift note: consider staggering basket #2 drop 2 min earlier to build slack before the historically busy 5:15–5:30 stretch
```
