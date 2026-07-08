# Mechatronics Playbook

Operational templates with concrete steps, thresholds, and filled numbers. Defaults, not laws — deviate consciously and say why in the design file.

## 1. V-model requirement-to-verification traceability (filled example)

System: inkjet service-station wiper axis (the SKILL.md worked example). Every row starts as a requirement and ends as a measured, signed-off number — no row ships without both ends filled.

| Req ID | Requirement (customer/system level) | Functional spec | Logical/physical implementation | Verification method | Measured result | Status |
|---|---|---|---|---|---|---|
| R-01 | Wiper stops within ±0.5 mm of target, both directions | Closed-loop position control, settle time ≤300 ms | Motor-side rotary encoder, 1000 counts/mm load-equivalent, 500 Hz servo loop, reversal-dither compensation | Repeat-position test, 50 cycles/direction, dial indicator | ±0.42 mm worst-case (n=100) | PASS |
| R-02 | Gear-train backlash characterized and compensated | Compensation move = `B_raw` + 0.1 mm margin, capped ±0.2 mm | 2.2 mm reversal-dither (2.1 mm `B_raw` + 0.1 mm margin), calibrated per unit at final test | Backlash gauge measurement pre- and post-compensation | 2.1 mm `B_raw` measured, 2.2 mm programmed | PASS |
| R-03 | Axis stable under full seal/bearing wear range (EOL condition) | Structural resonance ≥3× velocity-loop BW, ≥6× position-loop BW | Velocity loop 40 Hz BW, position loop 20 Hz BW, structural resonance measured 150 Hz | Bode sweep at build and at simulated EOL (loosened bearing preload) | 150 Hz new (3.75×/7.5× velocity/position margins), 128 Hz at EOL simulation (3.2×/6.4× velocity/position margins) | PASS |
| R-04 | EMC: no false-trigger of home-sensor optocoupler from motor commutation noise | Shield termination at controller end only; 0.1 µF + 47 µF bypass at each driver IC | Twisted-pair shielded motor leads, single-point shield ground, local bypass caps per IC power pin | Radiated/conducted susceptibility bench test + 500-cycle home-sensor false-trigger count | 0 false triggers / 500 cycles | PASS |
| R-05 | Field serviceability: compensation value re-verifiable without full teardown | Compensation value stored in accessible service register, re-calibration procedure ≤15 min | Non-volatile register + guided calibration routine in service menu | Bench timing of calibration routine by non-engineer technician | 11 min average (n=5 technicians) | PASS |

**Rule:** a requirement without a verification row is not done, regardless of how confident the design review was. A verification result that fails gets a new row (R-01a, etc.) tracing the fix back to the same requirement — never silently overwritten.

## 2. Backlash-compensation calibration procedure

Applies whenever the sensor sits upstream (motor-side) of a compliant/backlash-bearing mechanism (gear train, belt, worm drive) and load-side resensing wasn't chosen.

1. **Measure raw backlash per unit at end-of-line test**, not from the drawing tolerance. Drive the load against a hard stop in direction A, zero the reading, then drive in direction B until motion is first detected at the load (dial indicator or load-side reference encoder used only for this calibration step). Record as `B_raw`.
   - Example: nominal drawing backlash 1.5–2.5 mm; measured unit `B_raw` = 2.1 mm.
2. **Add a process margin, not a repeat of the measurement.** Compensation move = `B_raw` + 0.1 mm (approx. 5% margin, capped at ±0.2 mm tolerance band per R-02). Do not compensate to exactly `B_raw` — undershoot leaves residual backlash error, overshoot drives the load past target and re-opens backlash the other way.
3. **Program the compensation as a directional pre-move**, executed only on a sensed direction reversal (compare commanded direction to the direction of the immediately preceding move): drive `B_raw` + margin at maximum safe velocity before resuming normal closed-loop position control toward the actual target.
4. **Verify at three points across the travel range** (near-limit, mid-travel, opposite-limit), 20 reversal cycles each. Threshold: worst-case stopping error ≤ tolerance budget (here ±0.5 mm) at all three points, not just the average.
5. **Store the calibrated value in non-volatile, per-unit memory** — never as a firmware-wide constant. Backlash varies unit-to-unit with gear tolerance stack-up (observed spread on this program: 1.6–2.6 mm across 40 units, a 1.0 mm range against a 2.0 mm nominal).
6. **Set a re-verification interval tied to wear rate, not an arbitrary calendar date.** Default: re-check at the PM interval where bearing/gear wear is expected to add ≥25% of the original compensation value (on this program, 6 months / ~500k cycles, from accelerated life test data). Flag re-verification failures (measured drift beyond ±0.3 mm of the stored value) as a maintenance action, not a redesign trigger, unless drift recurs after two consecutive recalibrations — then escalate to gear-train wear-rate investigation.

**Fallback order if compensation alone can't hold tolerance:** (1) tighten the dither margin and re-verify motor current headroom — larger dither moves need more torque margin near travel limits; (2) add a load-side reference sensor used only for periodic re-zeroing (cheaper than full load-side closed-loop); (3) full load-side encoder retrofit, only after 1–2 are shown insufficient on data, since it's the highest-cost option and was the one value-engineered out originally.

## 3. Inertia-ratio and gearbox sizing worksheet

Use before locking a gear ratio on a coupled servo axis.

**Inputs (example axis — a pick-and-place rotary joint):**
- Load inertia at the joint, `J_load` = 0.048 kg·m²
- Candidate motor rotor inertia, `J_motor` = 0.0006 kg·m²
- Candidate gearbox ratio, `G` = 20:1
- Required peak acceleration at load = 40 rad/s²
- Motor peak torque rating = 3.2 N·m

**Step 1 — Reflect load inertia to the motor shaft.** A gear ratio of `G` divides reflected inertia by `G²`:

`J_reflected = J_load / G² = 0.048 / 20² = 0.048 / 400 = 0.00012 kg·m²`

**Step 2 — Compute inertia ratio.**

`ratio = J_reflected / J_motor = 0.00012 / 0.0006 = 0.20 → 0.2:1`

Result is well under the 5:1 default ceiling (10:1 acceptable-but-tune-carefully limit) — this ratio is servo-friendly; no rework needed. If the same axis used `G` = 5:1 instead: `J_reflected` = 0.048/25 = 0.00192 kg·m², ratio = 0.00192/0.0006 = 3.2:1 — still under 5:1, but closer to the ceiling, and the design margin against tolerance stack-up (bearing wear, coupling wind-up) shrinks accordingly.

**Step 3 — Check torque headroom against required acceleration.**

Required motor torque = (`J_motor` + `J_reflected`) × required accel at motor shaft, where motor-shaft accel = load accel × `G` = 40 × 20 = 800 rad/s².

`T_required = (0.0006 + 0.00012) × 800 = 0.00072 × 800 = 0.576 N·m`

Against 3.2 N·m peak rating: headroom = 3.2 / 0.576 ≈ 5.6× — comfortable margin for load variation, friction, and dynamic disturbances (target minimum: ≥2× at worst-case load condition, not nominal).

**Step 4 — Decision table**

| Reflected inertia ratio | Action |
|---|---|
| ≤5:1 | Proceed; standard autotuning expected to converge without gain scheduling |
| >5:1 and ≤10:1 | Proceed with caution; plan for extended commissioning time, verify resonance margin (§ tools/methods) before sign-off, expect gain scheduling may be needed across the travel range |
| >10:1 | Do not proceed on the current ratio — increase `G` (inertia drops with `G²`, so even a modest ratio bump helps disproportionately), or move to direct-drive/torque-motor topology if the mechanical package allows it |

**Common sizing mistake:** picking `G` to hit the desired output speed/torque only, then discovering the inertia ratio afterward. Size `G` against both constraints simultaneously — output kinematics and inertia ratio — because a ratio chosen purely for speed frequently lands in the >10:1 band on lightweight rotary joints with small motors.
