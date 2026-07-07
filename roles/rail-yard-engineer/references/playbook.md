# Playbook

Filled worksheets for the three recurring yard-move problems: kick-speed rollout calculation for flat switching, hump-crest pacing against a tower's called spacing, and hostler terminal-servicing/securement checks. Numbers below are stated industry practice and the regulatory thresholds cited in `SKILL.md`'s Sources, not a substitute for a carrier's approved switching instructions or a specific yard's track profile — those always control over this worksheet.

## 1. Kick-speed rollout calculation (flat switching)

**Method, in order:**
1. Confirm the car will roll free — no dragging brake rigging, hand brake released, no obvious defect — before treating it as a kick candidate at all; if rollability is in doubt, couple-and-shove instead.
2. Identify the coupling-speed limit that governs: the yard's general limit, or a tighter carrier-specified limit for this commodity/car type (tank, refrigerated, high-value lading).
3. Compute required release speed: v₀ = √(v_target² + 2 × a × d), where v_target is the coupling-speed limit, a is the car's rolling-resistance deceleration, and d is the rollout distance to the standing cut.
4. Compare the computed release speed against the crew's habitual "standard kick" feel; if the standard feel exceeds the computed number, use the computed number.

**Worked example — two release speeds against the same 350 ft roll, 130-ton loaded tank car, 4 mph coupling limit:**

| Quantity | Computed (target 4 mph contact) | Habitual "standard kick" (6 mph release) |
|---|---|---|
| Release speed | 5.15 mph (7.55 ft/s) | 6.0 mph (8.80 ft/s) |
| Rolling-resistance deceleration | ≈0.032 ft/s² (2 lb/ton) | same |
| Contact speed after 350 ft | 4.0 mph (target) | 5.06 mph |
| Overage vs. 4 mph limit | 0% | 26% |
| Impact-energy ratio vs. limit (v²) | 1.00x | 1.60x |

**Decision rule:** on a rollout under roughly 500 ft, treat release speed and contact speed as nearly the same number — rolling resistance at ~2 lb/ton removes only a few ft²/s² of speed² over that distance, so there is no cushion to "add a little" into. Compute the release speed for the actual limit and actual distance; don't reuse a feel calibrated on a different car type or a longer track.

## 2. Hump-crest pacing against the tower's called spacing

**What the engineer controls vs. what the tower controls:** the tower (or hump conductor) sets classification-track routing and retarder speed control (master retarder, then group retarders per track) to produce the car-to-car separation the switches downstream need time to throw for. The engineer's job is matching the shove pace to the crest at the rate called, not independently judging spacing.

**Worked example — a 20-car cut being humped, tower calling "normal" pace:**

| Quantity | Value |
|---|---|
| Called crest speed | ~2 mph (typical humping speed, carrier-specific) |
| Minimum switch-throw interval needed downstream | ~6 seconds between successive cars routed to different tracks [heuristic — carrier/signal-system specific] |
| Car length (avg., loaded mixed cut) | ~55 ft |
| Time for one car length to clear the crest at 2 mph (2.93 ft/s) | 55 ÷ 2.93 ≈ 18.8 s |

At a called 2 mph crest speed, each car takes ≈18.8 s to clear the crest — well above the ≈6 s minimum switch-throw interval, which is why "normal" pace works without the engineer computing spacing directly. **Decision rule:** if the tower calls "ease" or "hold," that call already reflects a spacing problem building downstream (a slow-throwing switch, a car fouling a lead) — treat it as an instruction to act on immediately, not a suggestion to weigh against how the shove currently looks from the cab.

## 3. Hostler terminal-servicing move and securement check

**Before moving past any terminal boundary or into a service/fuel track:**
1. Confirm the terminal track-limits diagram's boundary for this specific track — service track, fuel rack, ready track — and that today's move stays inside it.
2. Confirm blue-signal status at the fuel rack or service point before approaching; a blue flag/light there protects a servicing crew exactly as it would on a yard classification track.
3. On leaving a unit or cut standing, apply hand brakes to the carrier's securement table for that track's grade and tonnage, then test effectiveness: apply hand brakes, release air brakes, and confirm the equipment doesn't move before leaving it unattended.

**Worked example — securement table lookup for a 4-unit locomotive consist, 340 tons, left standing on a 0.8% service-track grade:**

| Grade | Tonnage band | Minimum hand brakes required [carrier-table example, illustrative] |
|---|---|---|
| 0.0–0.5% | any | 1 per unit, minimum 1 |
| 0.6–1.0% | ≤400 tons | 2 per unit or 100% of units, whichever is greater |
| 0.6–1.0% | >400 tons | 100% of units plus effectiveness test required |
| >1.0% | any | 100% of units plus effectiveness test required |

At 0.8% grade and 340 tons, the table calls for hand brakes on 100% of units (all 4) — apply all four, release the independent and automatic brakes, and confirm the consist holds stationary before walking away. **Decision rule:** the count of hand brakes applied is not the compliance check — the effectiveness test (air released, equipment observed stationary) is. A cut secured by count alone, never tested with air released, has not been verified secure by the rule this table exists to satisfy.
