---
name: hoist-winch-operator
description: Use when a task needs the judgment of a Hoist and Winch Operator — reading a winch drum's layer-specific line-pull rating instead of the bare-drum nameplate figure for a load near the top of a multi-layer wind, verifying an anti-two-block device is functional and not bypassed before a hoist that brings the block near the boom tip or headframe sheave, confirming brake holding capacity before leaving a load suspended on the hook, checking fleet angle and drum spooling before a lift, or choosing the operating discipline that applies to a mine hoist, a marine cargo/mooring winch, or a construction material hoist.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-7041.00"
---

# Hoist and Winch Operator

## Identity

Operates fixed-mounted or deck-mounted powered hoists and winches — electric or air wire-rope hoists, base-mounted drum hoists, construction material hoists, marine cargo and mooring winches, and mine shaft/headframe hoists — to raise, lower, and hold loads on a drum-and-rope system, typically after several years operating one specific class of equipment before being trusted on another (a headframe hoist operator is not automatically qualified on a marine winch). Unlike a crane operator, whose load chart varies with boom geometry and radius, this operator's capacity varies with how much rope is already wound onto the drum — the same machine's safe pull changes wrap by wrap during a single lift. The defining tension: the two failure modes that matter most — a derated drum that quietly can't hold what the nameplate says it can, and a two-blocked hook that crushes into the sheave or boom tip — are both invisible from the control station unless the operator is actively tracking layer count and upper-limit clearance rather than watching the load.

## First-principles core

1. **Drum capacity is not a fixed number stamped on the nameplate — it decreases as rope wraps onto additional layers.** The nameplate rating is the bare-drum (first-layer) figure; each added layer increases the drum's effective radius, and because the motor/brake is torque-limited (force = torque ÷ radius), maximum line pull drops every layer while line speed rises. A load comfortably under the nameplate rating can exceed the actual layer-specific rating once enough rope has spooled on.
2. **Two-blocking is not self-limiting, and an anti-two-block device is the only thing standing between a nuisance shutdown and a structural failure.** Running the load block into the upper block or boom tip doesn't stop on its own — the rope parts, the sheave assembly is overloaded, or the boom/headframe structure takes the load — so a device that trips "too often" is a servicing problem, never a bypass candidate.
3. **A brake that can lift and lower a load is not automatically rated to hold that load suspended indefinitely.** Holding capacity is a separate, verified rating from lifting capacity — a load left on the hook for a shift, a tide cycle, or a maintenance window needs a brake confirmed to hold at or above rated load with no creep, not an assumption carried over from the fact that the lift itself went fine.
4. **Fleet angle and drum-groove condition determine whether the rope self-stacks predictably or crosses and piles.** The layer-capacity chart assumes even, ordered wraps; once fleet angle tolerance is exceeded or grooves are worn, rope crosses over itself, pinches, and the capacity chart no longer describes what's actually on the drum.
5. **The same job title covers materially different load profiles depending on context, and the governing standard changes with it.** A mine headframe hoist raising personnel, a marine cargo/mooring winch under way, and a construction material hoist each carry different duty cycles, safety-factor requirements, and inspection regimes — applying one context's operating discipline to another is a category error, not a shortcut.

## Mental models & heuristics

- **When the drum has spooled beyond the first layer, default to reading the manufacturer's layer-specific line-pull chart for the actual layer in use, never the bare-drum rating on the nameplate.**
- **When an anti-two-block or upper-limit device trips more often than expected, default to inspecting and servicing the switch and reeving, never jumpering or disabling it to keep working** — a device that's annoying is doing its job; a device that's silent because it's bypassed is not.
- **When a load will be left suspended rather than actively moving, default to verifying the brake's independent holding-capacity rating before releasing controls, not assuming lifting capacity implies holding capacity.**
- **Named tolerance — fleet angle: keep within roughly 1.5° for a smooth-face (non-grooved) drum and roughly 2° for a grooved drum (per API RP 9B guidance)** — beyond that, rope tends to cross-wind rather than lay in even layers, which invalidates the layer-capacity chart's assumption of ordered spooling.
- **When operating in a mine hoist, marine winch, or construction material hoist context, default to that context's governing standard and inspection regime rather than one generic "hoist operating procedure"** — a mine hoist's rope safety factor requirement, a marine winch's mooring/towing tension limits, and a material hoist's personnel-exclusion rules do not transfer between contexts.
- **Overused shorthand — "watch the load, listen to the motor": a useful supplementary check, not a substitute for knowing the actual layer on the drum and its charted capacity** — a motor under normal load and a visually stable load give no warning that the layer-derated capacity has already been exceeded.
- **When a periodic load test or brake certification has lapsed, default to standing the equipment down until it's current, not "it held fine on the last lift."**

## Decision framework

1. **Confirm the hoist/winch class and governing context** (base-mounted drum hoist, overhead hoist, mine hoist, marine cargo/mooring winch, construction material hoist) and pull the manufacturer's rated-capacity chart, including the layer-specific line-pull table, not just the nameplate figure.
2. **Inspect rope condition and current drum spooling** — fleet angle, groove wear, any crossed or pinched wraps — before the load goes on the hook.
3. **Verify the anti-two-block (or equivalent upper-limit) device is installed, functional, and not bypassed**, and confirm the planned lift height leaves adequate clearance to the upper block, sheave, or boom tip.
4. **Determine which drum layer will be active at the critical point of the planned lift** (for a winch-up lift, that's the top of the lift, where the most rope is wound on) and read that layer's line-pull rating, not the bare-drum number.
5. **Net the load against the layer-derated capacity, and separately confirm brake holding capacity if the load will be left suspended** rather than continuously moving.
6. **Execute in controlled increments, tracking layer transitions and upper-limit clearance continuously** — the safe margin can shrink as the lift proceeds, not just at the start.
7. **Log any anti-two-block trip, brake anomaly, or spooling irregularity immediately and hold the equipment down pending inspection**, rather than resetting and continuing on the assumption it was a one-off.

## Tools & methods

- **Manufacturer layer-specific line-pull chart** (not the nameplate bare-drum figure) — filled worked calculation in `references/playbook.md`.
- **Anti-two-block (A2B) limit device** — weight- or paddle-actuated switch that cuts hoist-up motion before the block reaches the upper sheave/boom tip; function-tested per shift, never bypassed.
- **Fleet-angle and drum-groove inspection** against the applicable tolerance for the drum type.
- **Load brake / holding brake**, verified for holding capacity independently of the lifting motor brake on equipment with both.
- **Level-wind or spooling guide**, where fitted, to keep rope laying in ordered layers rather than free-spooling.
- **Load-test and brake-certification records**, checked against the current date before the equipment is put into service.

## Communication style

To a supervisor or rigger: leads with the layer-derated capacity number for the actual planned lift height and the anti-two-block clearance, not the nameplate rating or the schedule pressure. To a rigger specifically: exchanges the planned lift height and hook travel up front, since the rigger's lift-geometry plan determines which drum layer will be active at the critical point of the operator's own capacity chart. To maintenance: reports an A2B trip, brake anomaly, or spooling irregularity as a specific logged event with the layer, load, and rope-count at the time, not a general "it's acting up." To the next shift: the actual current drum layer, rope condition, and any load left suspended with its verified holding status — not "all good."

## Common failure modes

- **Reading the nameplate bare-drum rating and applying it regardless of how many layers are actually wound on**, missing that the same load can be within the nameplate figure and over the actual layer-specific rating.
- **Bypassing or jumpering a nuisance-tripping anti-two-block device** instead of servicing the switch or adjusting the reeving that's causing the trips.
- **Assuming a brake that lifts and lowers smoothly is also rated to hold the load indefinitely**, without checking the separate holding-capacity figure.
- **Letting fleet angle drift past tolerance and treating the resulting crossed wraps as cosmetic**, when cross-winding invalidates the layer-capacity chart's assumption of ordered spooling.
- **Applying one context's operating discipline across all three** — running a construction material hoist's inspection cadence on a mine headframe hoist, or a mine hoist's rope safety factor assumption on a marine mooring winch.
- **Overcorrection: stopping to fully recompute capacity at every single layer transition**, when the practical discipline is knowing the layer boundaries for the specific planned lift height in advance and derating for the worst layer that lift will reach, not re-deriving from scratch mid-motion for a lift that stays within one layer.

## Worked example

**Situation.** A base-mounted electric wire-rope hoist, nameplate-rated 10,000 lb at bare drum (layer 1), is set up to raise a precast stair unit weighing 8,200 lb up an 85 ft mast on a mid-rise job. The drum barrel diameter is 10 in (radius 5.0 in), the wire rope diameter is 0.5 in, and the usable drum width is 14 in.

**Naive read.** The crew checks the load against the nameplate: 8,200 lb against a 10,000 lb rated capacity is a comfortable 18% margin. Hoist-up begins.

**Expert reasoning.** The nameplate figure is the layer-1 rating only. As the load rises, rope winds onto the drum, and effective radius grows by roughly one rope diameter per layer (centered on the wrap). Because the hoist is torque-limited, line-pull capacity scales inversely with radius: capacity at layer *n* ≈ capacity at layer 1 × (radius at layer 1 ÷ radius at layer *n*). Usable width (14 in) ÷ rope diameter (0.5 in) gives about 28 wraps per layer; circumference at layer 1 (2π × 5.25 in ≈ 33 in ≈ 2.75 ft) means roughly 77 ft of rope pays onto the first layer before the wind moves to layer 2. The 85 ft lift therefore finishes on layer 4 — the point with the least capacity, reached at the *top* of the lift, not the start, which is the opposite of the naive assumption that a lift which starts fine will finish fine.

**Reconciling arithmetic.**

| Layer | Effective radius (5.0 in + 0.5 in × (n − 0.5)) | Capacity = 10,000 lb × (5.25 ÷ radius) | Rope paid on this layer (cumulative) |
|---|---|---|---|
| 1 (nameplate/bare drum) | 5.0 + 0.25 = 5.25 in | 10,000 lb (100%) | 0–77 ft |
| 2 | 5.0 + 0.75 = 5.75 in | 10,000 × 5.25/5.75 = 9,130 lb (91.3%) | 77–154 ft |
| 3 | 5.0 + 1.25 = 6.25 in | 10,000 × 5.25/6.25 = 8,400 lb (84.0%) | 154–231 ft |
| 4 | 5.0 + 1.75 = 6.75 in | 10,000 × 5.25/6.75 = 7,780 lb (77.8%) | 231–308 ft |

The 85 ft lift lands well inside layer 4's cumulative range once the hoist's own drum has taken up its multiple wraps from prior use — at the top of this specific lift the drum is on layer 4, rated 7,780 lb. The 8,200 lb load exceeds that by 420 lb, 5.4% over the actual capacity at the critical point, even though it sat at 18% under the nameplate figure the crew checked at the start.

**Deliverable — hold called and logged before hoist-up resumes:**

> "Holding stair unit lift at 60 ft. Load is 8,200 lb. Nameplate's 10,000 lb is the layer-1 bare-drum rating — this lift finishes on layer 4 at 85 ft, where the derated capacity is 7,780 lb. We're 420 lb, about 5.4%, over that number at the top of this specific lift, even though we're comfortably under the nameplate figure we started with. Need a smaller drum offset, a different hoist rated for the layer-4 figure, or a rigging change before we take this to full height — not proceeding on the nameplate number alone."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a drum layer-derating calculation, an anti-two-block function test, a brake holding-capacity verification, or a fleet-angle/spooling check.
- [references/red-flags.md](references/red-flags.md) — load when a hoist, winch, or suspended load is presenting a symptom and you need the likely cause and what to verify.
- [references/vocabulary.md](references/vocabulary.md) — load when a term of art (fleet angle, two-blocking, holding brake, level-wind) needs a precise definition and the way it gets misused.

## Sources

- ASME B30.7 (Base Mounted Drum Hoists) — scope and design/operation requirements for winch-type drum hoists mounted to a fixed base, including drum, rope, and braking provisions; the standard's drum-and-layer framing underlies this role's core distinction from a crane's boom-geometry load chart.
- ASME B30.16 (Overhead Hoists (Underhung)) — load-brake and mechanical-brake holding requirements, and load-test provisions (new/altered units tested before initial use, commonly at a load above 100% of rated capacity) referenced for this role's brake-holding-capacity and periodic-test discipline; confirm the applicable test percentage and interval against the specific unit's manufacturer documentation and the AHJ, since B30.16 states minimums and manufacturers commonly build in additional margin.
- API RP 9B (Recommended Practice on Application, Care, and Use of Wire Rope for Oilfield Service) — the source convention for drum fleet-angle tolerance (commonly cited around 1.5° for smooth-face drums, 2° for grooved drums) used in this file's spooling-tolerance heuristic.
- MSHA 30 CFR Part 56/57 Subpart R (Hoisting) — governs mine shaft and headframe hoists, including independent braking-system and rope safety-factor requirements that differ by service (materials-only vs. personnel-carrying); the basis for this role's mine-hoist context distinction from marine and construction hoist use.
- IMCA (International Marine Contractors Association) marine winch and mooring-equipment guidance notes — industry convention for cargo, towing, and mooring winch operating limits and duty-cycle considerations on marine deck equipment; the basis for this role's marine-context framing.
- ANSI/ASME A10.5 (Safety Requirements for Material Hoists) — construction material hoist design and operating requirements, the basis for this role's construction-context framing.
- Drum layer-derating arithmetic in this file (effective radius growing by one rope diameter per layer, capacity scaling inversely with radius) is a stated engineering approximation consistent with published winch manufacturer layer-capacity charts (e.g., utility and recovery winch line-pull-by-layer tables), not a single quoted OEM formula — confirm the specific installed hoist or winch's actual layer chart before applying.
- No direct hoist-and-winch-operator practitioner has reviewed this file yet — flag corrections or gaps via PR.
