# Logging Operations Playbook

Operational sequences with real thresholds and worked numbers. Defaults, not laws — deviate consciously and log why in the shift report.

## 1. Slope/soil classification protocol (before equipment enters a block)

Run this before assigning machines to any new zone, and re-run after any rain event.

1. **Pull the harvest-plan slope classification** (LiDAR-derived, usually from the dry-season flyover). Treat it as a starting hypothesis, not a fact.
2. **Ground-truth with a walk-through**, checking both directions of slope separately — side-slope (perpendicular to the direction of travel) is the tipping-risk axis for wheeled machines; longitudinal slope (up/down the direction of travel) governs traction and braking. A block can be "22% average" on the map while its side-slope in one draw is 34%.
3. **Bin each sub-zone against these defaults:**

   | Zone class | Side-slope | Equipment default |
   |---|---|---|
   | Ground-based, wheeled OK | < 30% (~17°) | Standard wheeled skidder/forwarder |
   | Ground-based, tracked only | 30–40% (~17–22°) | Tracked feller-buncher/harvester; wheeled extraction needs winch-assist |
   | Winch-assist required | 40–100% (~22–45°) | Tethered ground machine, anchor machine or tree rated for the tether load |
   | Cable/skyline only | > 100% (~45°) or unstable/wet soil at any grade | Yarder (highlead or skyline); no ground equipment |

4. **Check bearing capacity, not just grade**, after rain: a 25% slope on saturated clay soil can behave like a 35%+ dry slope. If the last 48 hours had measurable rain, downgrade the zone one tier until a fresh walk confirms otherwise.
5. **Log the classification with a date** — it expires. Re-classify before moving equipment into a zone that hasn't been worked in the current weather window.

## 2. Cut-to-length vs. whole-tree system selection

Work the decision in this order — each factor can override the previous one.

1. **Average merchantable stem size.** Under ~0.2 tons/stem (small-diameter pulpwood): default whole-tree (feller-buncher + grapple skidder). A harvester head's cycle time is dominated by boom repositioning between stems, not processing — small stems multiply that overhead. Over ~0.4 tons/stem (larger sawtimber): cut-to-length's per-stem value recovery (accurate bucking-to-length at the stump) usually wins.
2. **Soil sensitivity.** Wet, fine-textured, or erosion-prone soils: default cut-to-length — the forwarder carries wood fully loaded off the ground, versus a skidder dragging whole trees, which roughly doubles ground-contact passes and rutting risk on the same tonnage.
3. **Sawlog:pulp ratio.** Sawlog-heavy stands reward cut-to-length's onboard bucking optimization (the harvester head's computer matches each stem's taper and defects to the mill's length/grade instructions in real time); pulp-heavy stands don't benefit enough to offset CTL's higher cost-per-ton on small wood.
4. **Distance to landing.** Beyond ~1,500 ft skid distance, forwarder (carries a full load, one trip) starts beating skidder (drags, more resistance, more trips) on a per-ton basis; under that distance the gap narrows enough that stem size and soil usually decide it first.
5. **Reconcile before committing crew and equipment** — write the one-sentence override if any factor conflicts (e.g., "soil says CTL, stem size says whole-tree — soil sensitivity wins because the tract borders a stream buffer").

## 3. Hang-up (hung tree) protocol

Set this before the first cut of the shift, not improvised mid-block.

1. **Mechanical pulldown first, always.** Use the feller-buncher's grapple or the winch-assist tether to pull the hung tree free. This is the entire point of mechanization — never send a person on foot to push, pry, or wedge a hung tree.
2. **If the grapple can't reach or the tether can't generate enough pull**, back the machine off, mark the tree's GPS location, and continue elsewhere. Do not attempt a second machine maneuver into the same hazard zone without a fresh read on the lean and remaining hinge wood.
3. **Escalate unresolved hang-ups to a certified manual faller**, treated as a distinct task with distinct PPE and training — not something the equipment operator handles on foot, however routine it looks.
4. **Track hang-up frequency per shift.** More than ~3 hang-ups/shift on the same block usually means the felling head's cut pattern or lean-reading needs adjustment, not that the trees are unusually difficult — investigate the cutting technique before accepting it as terrain variance.

## 4. Daily cost-per-ton worksheet (by zone, not blended)

Formula: **zone cost/ton = (sum of active machine-hour rates in that zone) ÷ (zone production rate in tons/hr)**.

Worked example (see SKILL.md worked example for the full scenario):

| Zone | Active machines & hourly rates | Bottleneck rate (tons/hr) | Cost/hr | Cost/ton |
|---|---|---|---|---|
| Flat (84 ac, 1,848 tons) | Feller-buncher $165, skidder ×2 $95 ea, landing $70 | 45.5 (feller-buncher-bound) | $425 | $9.34 |
| Steep (36 ac, 792 tons) | Feller-buncher $165, skidder ×1 $95, winch-assist $50, landing $70 | 26.7 (tethered-skidder-bound) | $380 | $14.23 |

**Rules for the worksheet:**
- Identify the bottleneck machine in each zone before computing cost/ton — it's whichever machine's tons/hr is lowest among the chain, not the felling machine by default.
- Never blend zones into one average until every zone's individual cost/ton has cleared the target rate; a blended number hides which zone is losing money.
- Recompute the bottleneck whenever equipment count changes (e.g., pulling a skidder to winch-assist duty in a steep pocket changes both the burn rate and the throughput rate simultaneously).
- Compare zone cost/ton against the contracted delivered rate daily, not at job close — a zone running under margin needs a decision (requote, reroute to cable yarding, or walk away) while machines are still mobilizable, not after the job is done.

## 5. Winch-assist rigging checklist

Before tethering a ground machine for steep-slope work:

1. Confirm the anchor (stationary anchor machine or anchor tree) is rated for the tether load at the steepest point of the planned path, not just the average slope.
2. Route the tether to avoid crossing the planned travel path of any other machine in the zone.
3. Budget the cycle-time penalty (~15–25% versus untethered operation on the same slope) into the day's production target before the shift starts, not as an excuse after it falls short.
4. Re-anchor before the tether angle from anchor point to machine exceeds roughly 30° off the machine's line of travel — a sharply angled tether reduces effective pull and increases side-load on the anchor.
5. Log actual cycle times against the budgeted penalty; if it's running worse than 25% slower, the anchor placement or path is wrong, not the machine.
