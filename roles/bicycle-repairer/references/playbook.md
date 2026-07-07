# Bicycle Repairer — Playbook

## Chain-wear-to-replacement decision sequence

1. **Measure elongation with a chain wear indicator, not by mileage or feel.** Park Tool CC-3.2 reads three stages directly: 0.5%, 0.75%, 1.0%.
2. **Check the drivetrain's speed count against the threshold table below** — narrower chains (11/12/13-speed) have tighter cog tolerance and hit the point of no return sooner.

| Drivetrain | Chain-only safe up to | Full drivetrain past |
|---|---|---|
| 8/9-speed | 0.75% | ~1.0% |
| 10-speed | 0.5–0.6% | ~0.85% |
| 11/12/13-speed | 0.5% | ~0.75% |

3. **If at or below the chain-only line, quote chain replacement alone** and log the reading and date for the next visit's rate-of-wear comparison.
4. **If past the chain-only line but at or below the full-drivetrain line, inspect cassette cogs under a loupe for hook/shark-fin profile** before deciding — light hook wear with a fresh reading can sometimes still take a chain-only swap; log it as a judgment call with the measured number, not a default.
5. **If past the full-drivetrain line, quote chain + cassette together**, and check chainrings separately — chainring wear lags cassette wear and often doesn't need replacement at the same visit.
6. **Compute the cost delta against the checkpoint the customer missed**, if service history shows one, and state it in the quote — this is the concrete argument for keeping future recheck intervals.

### Worked reconciliation (illustrative second case)

| Mileage | Elongation | Interval | Action taken |
|---|---|---|---|
| 900 mi | 0.30% | — | logged, no action |
| 2,100 mi | 0.55% | 1,200 mi | 10-speed: past chain-only line (0.5–0.6%), cassette inspected, cogs clean — chain-only swap, $54 |
| 3,400 mi (new chain) | 0.20% | 1,300 mi | new chain baseline confirmed low, no action |

Chain-only swap at 2,100 mi avoided the $92 full-drivetrain quote (chain $30 + cassette $50 + labor $12 extra) that a further-deferred visit would have required — the $38 difference is the value of catching it inside the chain-only window instead of past it.

## Carbon torque-spec reference (confirm against the specific component's stamped/printed spec before use)

| Interface | Typical spec (Nm) | Failure mode if wrong |
|---|---|---|
| Carbon seatpost clamp (frame or seat clamp) | 4–6 Nm | Under: post slips under pedaling load. Over: crushed fiber, post fails without warning under road shock. |
| Carbon steerer / stem clamp bolts | 4–6 Nm | Under: headset play, steering looseness. Over: crushed steerer, catastrophic failure risk at the fork. |
| Carbon handlebar clamp area | 4–6 Nm | Under: bar rotates in a crash or hard braking. Over: crushed bar wall, can fail without visible warning. |
| Carbon crank arm bolts (interface-dependent) | 12–15 Nm | Under: creaking, arm works loose over rides. Over: bearing preload distortion or crank interface damage. |
| Pedal spindle into crank arm (alloy, for reference) | 35–40 Nm | Under: pedal loosens in use. Over: threads gall, very hard to remove later. |

Every carbon figure above is a stated illustrative range — the frame, post, bar, or crank manufacturer's own stamped or printed spec always overrides this table. Use a calibrated click-type torque wrench and carbon assembly paste on every carbon interface; grease is not a substitute — it lowers the friction coefficient at the clamp face, which means the same clamp force holds less securely, encouraging either slip or the temptation to overtorque to compensate.

## Spoke-tension truing sequence

1. **True laterally on the stand first** to a rough working tolerance (~0.5 mm for a road wheel, ~1 mm for a mountain wheel) so the tension meter reads a wheel that's already close.
2. **Take tension readings at every spoke** with a calibrated meter (e.g., Park Tool TM-1), converting the deflection reading to kgf via the wheel/spoke manufacturer's chart.
3. **Compare drive-side and non-drive-side averages against the wheel's expected dish ratio.** A typical road rear wheel: drive-side ~110–130 kgf, non-drive-side ~55–70 kgf (roughly 50–55% of drive-side, reflecting dish angle) — a spoke reading well outside its side's expected band, not just "different from its neighbor," is the one to adjust.
4. **Adjust outlier spokes in small increments (quarter-turn or less), rechecking both lateral trueness and tension after each pass** — tension and trueness move together but not identically; chasing trueness alone can leave tension uneven and the wheel will go out of true again within weeks as the loose spokes fatigue faster.
5. **Stop when lateral trueness is within tolerance and no spoke reads outside roughly ±10% of its side's average** — perfect uniformity spoke-to-spoke isn't the target, avoiding a single significantly loose or tight outlier is.
6. **Log the tension readings on the work order for any wheel that had a spoke replaced or was under complaint** — this is the record that separates "trued correctly and a spoke later failed" from "trued incorrectly."

## Hydraulic brake bleed — fluid-compatibility procedure

1. **Identify the fluid family from the manufacturer before touching a bleed kit** — Shimano hydraulic disc brakes use mineral oil; SRAM, Avid, Hayes, and Formula hydraulic disc brakes use DOT fluid (commonly DOT 4 or DOT 5.1). This is a brand-and-model lookup, never an assumption from a prior job that day.
2. **Use the fluid-specific kit only** — separate funnels, syringes, and reservoir bleed blocks for DOT vs. mineral oil, physically stored apart. A residual drop of DOT fluid in a mineral-oil syringe (or the reverse) swells the wrong seal compound; the failure shows up as a leak or soft lever weeks later, not at the bench.
3. **Follow the brand-specific bleed sequence** (e.g., SRAM Bleeding Edge syringe-to-syringe method vs. Shimano funnel-and-gravity method) rather than a generic "open bleed screw, push fluid through" approach — the internal path and check-valve behavior differ enough between systems that a generic procedure leaves air trapped.
4. **Diagnose before bleeding**: a lever that firms up after several pumps indicates air; a lever that's mushy from the first pump after hard braking, or that feels normal but with weak stopping power, points to boiled/contaminated fluid or glazed pads respectively — bleed only after ruling those out, since a bleed doesn't fix boiled fluid at its old boiling point or glazed pad material.
5. **Bench-bleed a full fluid change on any brake showing discoloration or a burnt smell**, not a top-off — contaminated fluid mixed with fresh fluid in the same system still carries the degraded boiling point.
6. **Confirm firm, consistent lever feel through a full squeeze-and-release cycle** before calling the job done, and log the fluid type and bleed date on the work order for the next service interval.
