# Ship Captain / Deck Officer — Playbook

## Rule 18 vessel hierarchy (filled, ranked)

A power-driven vessel underway gives way to every category below it, regardless of relative bearing. This table is checked *before* any crossing/overtaking geometry.

| Rank | Category | Example | Gives way to it? (power-driven vessel) |
|---|---|---|---|
| 1 (highest) | Not under command (NUC) | Vessel with engine/steering failure, two black balls / red-over-red lights | Yes, always |
| 2 | Restricted in ability to maneuver (RAM) | Dredging, diving ops, towing that severely restricts course changes | Yes, always |
| 3 | Constrained by draft | Deep-draft vessel confined to a narrow channel by her draft | Yes, when the situation makes the constraint relevant |
| 4 | Engaged in fishing | Trawler with gear deployed, day shapes/lights per Rule 26 | Yes, always |
| 5 | Sailing vessel | Under sail alone, no engine in use | Yes, always |
| 6 (lowest, this role) | Power-driven vessel | Cargo ship, tanker, ferry | Applies Rule 13/14/15 geometry only against other power-driven vessels |

If the target is in a higher category than "power-driven," stop here — the answer is give-way, full stop. Only drop to the geometric rules below when both vessels are power-driven (or both sailing, per Rule 12).

## Geometric rules (power-driven vs. power-driven, filled)

| Situation | Rule | Definition (relative bearing) | Give-way / stand-on |
|---|---|---|---|
| Overtaking | 13 | Approaching from >22.5° abaft the other vessel's beam — i.e., at night you'd see only her sternlight, neither sidelight | Overtaking vessel always gives way, regardless of which vessel is otherwise "senior" |
| Head-on | 14 | Reciprocal or nearly reciprocal courses, each seeing the other's masthead lights in line/nearly in line and/or both sidelights | Both vessels alter course to starboard |
| Crossing | 15 | Risk of collision exists and neither vessel is overtaking or head-on | The vessel that has the other on her own starboard side is give-way; she shall avoid crossing ahead of the other vessel |

## CPA/TCPA plotting method (filled example)

Use two or more successive bearing/range observations of the same target, at least several minutes apart, from radar/ARPA or compass bearings.

| Time | Bearing (relative) | Range (nm) | Bearing change | Range change |
|---|---|---|---|---|
| T0 | 020° | 5.5 | — | — |
| T0+6 min | 021° | 4.3 | +1° | −1.2 nm |

- **CBDR check:** bearing changed only 1° while range closed 1.2 nm in 6 minutes — bearing is essentially unchanged, range is decreasing. This is CBDR under Rule 7(d)(i): treat risk of collision as established.
- **Closing rate:** 1.2 nm ÷ (6 min ÷ 60) = 12.0 kn.
- **TCPA (approx., valid when CBDR holds and closure is close to head-on/near-collision course):** current range ÷ closing rate = 4.3 nm ÷ 12.0 kn = 0.358 hr ≈ 21.5 min.
- **Action threshold:** if TCPA is inside the vessel's SMS threshold (commonly 15-20 min in open water, longer in restricted visibility or traffic separation schemes) and/or projected CPA is inside the vessel's minimum CPA (commonly 1.0 nm in open water, 2.0 nm in restricted visibility), take early, substantial action — course change of 30° or more, or a combination of course and speed, per Rule 8.
- **Confirm the action worked:** re-plot after the maneuver. Bearing should now be clearly opening (increasing or decreasing steadily, not creeping by ~1° again) — in the worked example, three minutes after a 30° stbd alteration the bearing opened from 021° to 032° at 3.9 nm, confirming CBDR was broken.

For a full ARPA vector-triangle solution (own-ship vector, target's true course/speed backed out from relative motion), use the maneuvering board or ARPA's own computed CPA/TCPA output — the range/bearing-rate method above is the manual cross-check, not a replacement for it in restricted visibility.

## GM (metacentric height) worksheet (filled example)

| Line item | Source | Value |
|---|---|---|
| KM (height of metacenter above keel) | Hydrostatic tables, at current mean draft | 9.85 m |
| KG, solid (height of center of gravity above keel) | Loading computer — lightship + cargo + ballast, VCG-weighted | 9.40 m |
| GM, solid | KM − KG | 0.45 m |
| Free-surface correction (FSC) | Sum of (tank free-surface moment ÷ displacement) across all slack tanks | −0.12 m |
| **GM, fluid (real available margin)** | GM solid − FSC | **0.33 m** |
| Regulatory minimum | 2008 IS Code, Reg 2.2 | 0.15 m |
| Company heavy-weather minimum (heuristic, varies by operator) | Vessel's SMS | 0.30 m |
| **Margin above heavy-weather floor** | GM fluid − company minimum | **0.03 m** |

A margin this thin (0.03 m against a 0.30 m operational floor, even though it clears the 0.15 m statutory floor by 0.18 m) is a real go/no-go input, not a rounding error — the fix is to remove free-surface area (top off or consolidate slack tanks) before adding speed or heading into worse sea state, not to proceed on the statutory number alone.

## Set-and-drift / DR-to-EP correction (filled worked calculation)

Intended track: course 090°T, speed 12.0 kn, for 2.0 hours.

**Step 1 — DR position (no current):**
Distance run = 12.0 kn × 2.0 h = 24.0 nm due east.
DR displacement: East = 24.0 nm, North = 0.0 nm.

**Step 2 — Current vector (observed/tabulated set and drift):**
Set = 200°T, drift = 1.5 kn, over 2.0 h → current displacement = 1.5 × 2.0 = 3.0 nm at 200°T.
East component = 3.0 × sin(200°) = 3.0 × (−0.342) = −1.03 nm.
North component = 3.0 × cos(200°) = 3.0 × (−0.940) = −2.82 nm.

**Step 3 — Resultant (estimated position, EP):**
Total East = 24.0 − 1.03 = 22.97 nm.
Total North = 0.0 − 2.82 = −2.82 nm (i.e., 2.82 nm south of the DR line).
Resultant distance = √(22.97² + 2.82²) = √(527.6 + 7.9) = √535.5 ≈ 23.1 nm.
Course made good = atan2(East, North) ≈ 097°T (the southerly set has pushed the actual track 7° south/clockwise of the intended 090°T).
Speed made good = 23.1 nm ÷ 2.0 h ≈ 11.6 kn.

**Step 4 — Correction for the next leg:**
To make good the original 090°T track against the same set and drift, steer approximately 7° up-current of the intended course — course to steer ≈ 083°T — and re-verify against the next fix, since tidal set and drift both change through the tidal cycle and this correction is only valid for the water and time window it was computed from.

## STCW rest-hour tracker (filled example, 7-day rolling window)

| Day | Rest period 1 | Rest period 2 | Total rest (h) | Longest gap between rest periods | STCW compliant? |
|---|---|---|---|---|---|
| Mon | 00:00-06:00 (6.0h) | 14:00-18:00 (4.0h) | 10.0 | 8h (06:00-14:00) | Yes |
| Tue | 00:00-06:00 (6.0h) | 15:00-19:00 (4.0h) | 10.0 | 9h | Yes |
| Wed | 01:00-06:30 (5.5h) | 16:00-20:30 (4.5h) | 10.0 | 9.5h | Yes |
| Thu | 02:00-06:00 (4.0h) | — | 4.0 | — | **No — below 10h/24h and rest not split ≥6h/1 period** |
| Fri | 00:00-08:00 (8.0h) | 16:00-18:00 (2.0h) | 10.0 | 8h | Yes (recovers Thu's shortfall going forward, but Thu itself remains a violation to log) |
| **7-day total (Mon-Fri shown)** | | | **44.0h of a 77h/7d floor pending 2 more days** | | On track if remaining 2 days average ≥16.5h combined |

Thursday's shortfall (4.0h, no ≥6h block) is logged as a rest-hour non-conformance the moment it's identified — not smoothed over by a good day later in the week. The watch-bill fix (adding a relief rotation, not just "pushing through") is the action item, raised to the master per the decision framework's escalation step.
