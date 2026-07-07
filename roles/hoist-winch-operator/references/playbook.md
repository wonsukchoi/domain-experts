# Hoist and Winch Operator — Playbook

Filled reference sequences: drum layer-derating calculation, anti-two-block function test, brake holding-capacity verification, fleet-angle/spooling check, and context-specific operating parameters.

## 1. Drum layer-derating calculation

A drum hoist's nameplate rating is the layer-1 (bare drum) figure. Effective radius grows roughly one rope diameter per layer, and because the hoist is torque-limited (force = torque ÷ radius), line-pull capacity falls every layer while line speed rises by the same ratio.

**Formula:**

```
Effective radius at layer n  = bare-drum radius + rope diameter × (n − 0.5)
Capacity at layer n          = Capacity at layer 1 × (radius at layer 1 ÷ radius at layer n)
Line speed at layer n        = Line speed at layer 1 × (radius at layer n ÷ radius at layer 1)
```

**Worked figures (illustrative — confirm against the specific installed hoist's manufacturer chart):**

| Input | Value |
|---|---|
| Bare-drum radius | 5.0 in |
| Rope diameter | 0.5 in |
| Layer-1 (nameplate) capacity | 10,000 lb |
| Usable drum width | 14 in → ≈28 wraps/layer |

| Layer | Effective radius | Capacity | Cumulative rope on drum |
|---|---|---|---|
| 1 | 5.25 in | 10,000 lb (100%) | 0–77 ft |
| 2 | 5.75 in | 9,130 lb (91.3%) | 77–154 ft |
| 3 | 6.25 in | 8,400 lb (84.0%) | 154–231 ft |
| 4 | 6.75 in | 7,780 lb (77.8%) | 231–308 ft |
| 5 | 7.25 in | 7,240 lb (72.4%) | 308–385 ft |

**Working steps:**

1. Pull the manufacturer's layer-specific line-pull chart for the exact drum installed — a generic percentage table is a planning approximation only, not a substitute for the OEM chart once one is available.
2. Calculate cumulative rope length per layer from usable drum width and rope diameter (wraps per layer × circumference at that layer), to determine which layer will be active at any given point in the lift.
3. Identify the critical point of the planned lift — for a winch-up lift, that's the top of the lift (most rope wound on, highest layer, lowest capacity); for a lower/pay-out from a fully-spooled drum, the critical point is the start.
4. Compare the load against the capacity at that critical layer, not the nameplate figure — a load within the nameplate rating can exceed the actual layer-specific rating.
5. If the load exceeds the derated capacity at the critical layer, the fix is one of: a larger/differently-drummed hoist, a rigging change that reduces the effective load on the line (e.g., a block-and-tackle reeving that trades speed for capacity), or declining the lift as planned — never proceeding on the nameplate number.
6. Re-verify rope condition each time a lift approaches a new layer transition — cumulative wear is not uniform across layers, since inner layers see more total cycles over the rope's service life.

## 2. Anti-two-block (A2B) function test

Two-blocking — running the load block into the upper block, sheave, or boom tip — does not stop on its own; the rope parts, the sheave is overloaded, or the structure absorbs the impact. The A2B device is the last independent layer preventing this.

**Working steps:**

1. Before each shift, function-test the A2B device per the manufacturer's procedure: typically raising the hook slowly toward the upper block until the device trips and hoist-up motion stops, with a confirmed physical standoff distance remaining (commonly several feet, per the specific device/manufacturer spec).
2. If the device trips prematurely (nuisance trip) during normal operation, treat this as a switch, reeving, or weight-actuation problem to service — never jumper or disable the device to keep working.
3. If the device fails to trip during the pre-shift function test, stand the hoist down and tag it out until the device is repaired or replaced — do not operate "carefully" as a substitute for a functioning device.
4. Log every A2B trip (nuisance or genuine) with the load, boom/mast configuration, and hook position at the time — a pattern of trips at the same configuration points to a reeving or geometry problem, not a faulty switch.
5. On equipment without a powered A2B (some base-mounted hoists, some winches), substitute a physical hard stop or a dedicated spotter with a confirmed sightline and a stop-call protocol before the hook reaches the critical zone, and treat that spotter call with the same authority as an automatic device trip.

## 3. Brake holding-capacity verification

Lifting/lowering capacity and holding capacity are separate ratings. A load left suspended (shift change, tide cycle, maintenance window) needs the brake's holding rating confirmed independently.

**Working steps:**

1. Identify whether the hoist has one brake (motor/mechanical combined) or two independent braking means (a running/lowering brake plus a separate load-holding brake) — equipment with two independent brakes gives a genuine redundancy for a suspended load that single-brake equipment does not.
2. Confirm the holding brake's rated holding capacity from the manufacturer's documentation — commonly specified with a design margin above rated load (manufacturer figures vary; verify the specific unit's stated holding-capacity percentage rather than assuming a universal number).
3. Before releasing controls on a load that will remain suspended for more than a few minutes, set the load onto the holding brake and observe for a stated dwell period (e.g., several minutes) confirming no measurable creep (downward drift).
4. If any creep is observed, do not leave the load unattended — lower to a supported position or arrange a mechanical backup (blocking, additional rigging restraint) before leaving the load on the brake alone.
5. Re-verify holding-brake function at the interval specified in the load-test/certification record — a brake that held six months ago on a lighter load is not verified for today's load and today's brake wear.

## 4. Fleet angle and drum spooling check

The layer-capacity chart in Section 1 assumes rope lays in even, ordered wraps. Fleet angle outside tolerance produces cross-winding, which invalidates that assumption.

**Working steps:**

1. Measure or estimate fleet angle — the angle between the rope's straight-line path from the first fixed sheave to the drum and a line perpendicular to the drum axis — at the extremes of drum travel (empty and fully spooled).
2. Compare against tolerance for the drum type: commonly around 1.5° for a smooth-face (non-grooved) drum, roughly 2° for a grooved drum (per API RP 9B guidance) — confirm the specific manufacturer's stated tolerance where it differs.
3. Inspect drum grooves (where fitted) for wear, flattening, or damage that would let rope wander out of its intended path even within nominal fleet-angle tolerance.
4. If rope is observed crossing over itself, piling at one end, or riding up over a prior wrap, stop and re-spool under tension before continuing — the layer-capacity chart does not describe a cross-wound drum, and continuing risks the top wrap pinching and damaging the layer beneath it.
5. Where fitted, confirm the level-wind mechanism is tracking correctly across the full drum width; a level-wind out of sync with drum rotation produces the same cross-winding a fleet-angle violation would.

## 5. Context-specific operating parameters

| Context | Governing reference | Distinguishing operating consideration |
|---|---|---|
| Mine shaft/headframe hoist | MSHA 30 CFR Part 56/57 Subpart R | Independent braking systems and rope safety-factor requirements that step up for personnel-carrying service versus materials-only service; overspeed/overwind protection specific to shaft travel. |
| Marine cargo/mooring winch | IMCA marine winch and mooring-equipment guidance | Dynamic tension from vessel motion and current/wind loading on a moored or towed line; render-and-recover behavior under sustained tension, distinct from a static lift. |
| Construction material hoist | ANSI/ASME A10.5 | Personnel-exclusion zones at landings, platform/car overload interlocks, and a duty cycle of frequent stop-start cycles across multiple floor landings rather than a single continuous lift. |

**Working step:** before operating in an unfamiliar context, confirm which governing reference applies and pull that reference's specific inspection/duty-cycle requirements rather than defaulting to the operating discipline from a previously familiar context.
