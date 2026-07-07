# Playbook

Filled worksheets for the three recurring physical-verification problems: hand-brake sufficiency against grade and tonnage, switch-point-lock verification, and derail placement/verification. Numbers below are stated industry practice and the regulatory thresholds cited in `SKILL.md`'s Sources, not a substitute for a carrier's approved securement instructions or a specific track's profile — those always control over this worksheet.

## 1. Hand-brake sufficiency worksheet

**Method, in order:**
1. Pull the actual grade for the specific track segment (track profile/employee timetable), not the yard's general reputation for being "pretty flat."
2. Pull the cut's trailing tonnage and car count.
3. Look up the required hand-brake percentage from the grade/tonnage band; multiply by car count and round up.
4. Apply that count, then run the effectiveness test: release all air (automatic and independent), observe for the carrier-specified interval, confirm no movement.
5. If any movement is observed, add hand brakes and re-run the test — do not average "how close it was" into a judgment call.

**Grade/tonnage table (illustrative — carrier instructions under 49 CFR 218.95 supersede this):**

| Grade | Minimum hand brakes (% of cars, rounded up) | Effectiveness-test wait |
|---|---|---|
| 0.0–0.9% | 15%, minimum 1 | ~3 min |
| 1.0–1.8% | 25% | ~5 min |
| 1.9–3.0% | 50% | ~8 min |
| >3.0% | 100% | ~10 min |

**Worked example — 30-car mixed-freight cut, 2.2% grade, average 90 tons/car loaded:**

| Quantity | Value |
|---|---|
| Cars | 30 |
| Average tonnage/car | 90 tons |
| Total trailing tonnage | 2,700 tons |
| Grade | 2.2% (1.9–3.0% band) |
| Required hand-brake percentage | 50% |
| Required hand-brake count | 15 cars (50% of 30) |
| Habitual "standard cut" count (crew's usual on this yard) | 6 cars (20%) |
| Shortfall vs. requirement | 9 cars under-secured |

At 2.2%, this cut lands in the 50% band specifically because it's a steeper grade than the yard's usual flat-track sidings — a habitual count carried over from a 15-car cut on a 0.5% track (2–3 brakes) is 9 cars short of what this specific segment requires. **Decision rule:** recompute for every new track/grade/tonnage combination; a count that was sufficient on a different siding is not evidence about this one.

## 2. Switch-point-lock verification checklist

**What "verified" means, as distinct from "looks lined":**
1. Confirm the point rail is fully seated against the stock rail with no visible gap at the point of closest contact — 49 CFR 213.135 sets point/stock-rail fit tolerances by track class; a gap that would fail the track-class tolerance is a defect regardless of what the target shows.
2. Physically check the switch stand's connecting rod and lock — hasp closed and padlocked (or the spring mechanism seated, for a spring switch) — not just that the target/lamp reads the expected color or letter.
3. Confirm the switch is in the position the move actually requires (normal or reverse) before any equipment moves over it, independent of what position it was in on the last move.
4. On a switch left in a non-normal position for any length of time (a siding move, a temporary lineup), re-verify before every subsequent move over it rather than trusting the state from the last check.

**Worked example — hand-thrown switch reversed for a siding pull, left unattended 40 minutes before the next move:**

| Check | Result |
|---|---|
| Target reads reverse | Yes |
| Point-to-stock-rail gap, visual + hand check | Point not fully seated — ~3/16 in gap, ice in the flangeway |
| Stand lock engaged | Padlock present, hasp closed over an unseated point |
| Conclusion | Switch reads correctly but is not verified — ice cleared, point reseated, gap rechecked at 0 before authorizing the move |

**Decision rule:** a locked hasp over an unseated point is not a passed check — the lock secures whatever position the points happen to be in, seated or not. Clear the obstruction and recheck the physical fit before trusting the lock at all.

## 3. Derail placement and verification

**Function:** a derail intentionally derails a car onto the ground before it reaches a point where it would foul or run onto a main track — a deliberate, planned failure chosen over an uncontrolled car reaching through traffic.

**Placement, in order:**
1. Confirm the derail sits far enough from the clearance point/switch to stop a car before it can foul the adjoining track, accounting for the grade behind it — a common field practice is the greater of one car length or the distance a rolling car could cover given the grade and any residual momentum, not a fixed "one car length always" rule.
2. Confirm the derail's default state matches the carrier's standing instruction for that spur — typically locked in the derailing (protecting) position when the track isn't in active use, mirroring "locked normal" practice for a switch.
3. Before any move onto or off the protected track, physically confirm the derail is in the position (on/protecting or off/cleared) the move requires, and locked there — the same visual-plus-physical standard as a switch point.
4. Restore the derail to its protecting position and lock it immediately after the move clears it — not at the end of the shift, not "when we get back to it."

**Worked example — portable derail on a 1.5% industry spur feeding a mainline crossing 60 ft away:**

| Quantity | Value |
|---|---|
| Spur grade | 1.5% |
| Distance from derail to mainline fouling point | 60 ft |
| Standard placement distance for this grade band [carrier practice, illustrative] | ≥1 car length (≈50 ft) plus margin for grade — 60 ft placement is within the margin, not against the minimum |
| Default state | Locked in derailing (on) position when spur not in active use |
| Verification before a move onto the spur | Confirm derail off, unlocked, oriented correctly — logged before crew proceeds |
| Verification after move clears | Derail restored to on/locked within the same work cycle, not deferred |

**Decision rule:** the placement distance is a function of grade and car-stopping behavior on that grade, not a fixed number reused across spurs — a spur at 1.5% needs more margin than a level spur of the same length, because a car that gets past the derail point still has grade working on it.
