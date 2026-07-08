# Playbook

Filled worked examples for the artifact types and bench procedures this role runs most often, beyond the SKILL.md worked example: a half-split fault isolation on a signal chain, a scope probe-compensation and loading check, an ESD workstation qualification, and a load-regulation sweep on a second rail. Populate with the actual job's numbers; the structure and arithmetic below are real and reconcile.

## Half-split fault isolation — analog signal chain

**Scenario:** a sensor front-end board's output reads garbage. Signal chain, source to output: sensor → instrumentation amp (IA) → 2nd-order anti-alias filter → ADC driver → ADC digital output. 5 stages between a known-good source (bench signal generator injected at the sensor input for this test) and the known-bad output.

**Half-split, stage 1 (midpoint):** probe the anti-alias filter output (stage 3 of 5). Expected: 1.000 V for a 1.000 V injected input (IA gain ×1 for this test, filter passband gain ×1). Measured: **1.002 V** — good. Fault is downstream of the filter (stages 4-5), not upstream.

**Half-split, stage 2 (midpoint of remaining 2 stages):** probe the ADC driver output. Expected: 1.000 V (unity buffer). Measured: **0.240 V** — bad. Fault is at or before the ADC driver, and stage 3 was already confirmed good, so the fault is isolated to the ADC driver stage itself.

**Result:** 2 measurements isolated the fault to 1 of 5 stages (versus up to 4 sequential measurements walking end to end). ADC driver op-amp checked out-of-circuit on a curve tracer: output stage shows asymmetric clipping consistent with a damaged output transistor pair — pulled and replaced; unit re-tested at the ADC digital output, reads correct code for the 1.000 V reference.

## Oscilloscope probe compensation and loading check

**Scenario:** before trusting any rise-time measurement on a new probe/scope pairing, verify compensation using the scope's built-in calibration square wave (typically 1 kHz, ~5 Vpp on most bench scopes).

**Under-compensated probe (too much shunt capacitance):** waveform shows **rounded top, overshoot on the rising edge peaking at 5.6 Vpp against a 5.0 Vpp reference (12% overshoot)** — trim capacitor adjusted until the top flattens.
**Over-compensated probe (too little shunt capacitance):** waveform shows **rolled/undershot corners, settling to 4.7 Vpp with a slow rounded rise** — trim capacitor adjusted the other direction.
**Correctly compensated:** flat top within **±2% of the 5.0 Vpp reference (4.90-5.10 V), sharp corners** — probe is now trustworthy for rise-time measurements on this channel.

**Loading check, 1x vs. 10x on a fast digital line:** a 74-series logic output driving a line with a nominal 2 ns rise time is probed first with a 1x probe (input capacitance ~90-100 pF including cable) and then a 10x probe (input capacitance ~10-15 pF). Measured rise times: 1x probe = **5.8 ns** (badly distorted — the probe's own capacitance is loading the line and slowing the edge it's trying to measure), 10x probe = **2.3 ns** (close to the 2 ns nominal, remaining difference attributable to scope/probe system rise time per the quadrature relationship in SKILL.md First-principles core #2). Default to 10x per the Mental models heuristic; the 1x reading here would have been misread as a defective driver.

## ESD workstation qualification — daily verification

**Scenario:** per ANSI/ESD S20.20, an ESD-protected work area (EPA) workstation is verified before use, not assumed compliant because it was compliant last week.

| Check | Method | Spec (stated heuristic — verify site EPA compliance plan) | Measured | Result |
|---|---|---|---|---|
| Wrist strap system resistance | Wrist-strap tester, worn as during use | 0.8 MΩ – 10 MΩ (person + 1 MΩ series resistor in the strap, through the tester's reference) | 1.4 MΩ | PASS |
| Work surface (mat) resistance to ground | Surface resistance meter, two-point | ≤1×10⁹ Ω per the EPA plan's dissipative-mat spec | 6.2×10⁷ Ω | PASS |
| Mat-to-ground cord continuity | Continuity check on the common-point ground cord | <35 Ω (cord + connection) | 2 Ω | PASS |
| Ionizer balance (if used near sensitive open assemblies) | Charged-plate monitor, offset voltage | ±35 V or better per equipment spec | +12 V | PASS |

**Deliverable — EPA daily log entry:** "Workstation WS-14, [date]. Wrist strap 1.4 MΩ (spec 0.8-10 MΩ) PASS. Mat 6.2×10⁷ Ω PASS. Ground cord 2 Ω PASS. Ionizer +12 V PASS. Station qualified for ESD-sensitive device handling this shift." A FAIL on any row takes the station out of service for ESD-sensitive work until corrected — devices handled at a failed station in the interim get flagged ESD-suspect per the SKILL.md Decision framework, not silently assumed fine.

## Load-regulation sweep — second rail example (3.3 V, switching regulator)

**Setup:** onboard 3.3 V switching regulator rated 1.5 A max, datasheet load-regulation spec ≤1.5% (no-load to full-load).

**Sweep, electronic load 0 → 1.5 A, measured at the regulator's own output pin (not downstream, to isolate the regulator from any board IR-drop):**

| Load | Voltage |
|---|---|
| 0 A (no-load) | 3.312 V |
| 0.75 A (half-load) | 3.298 V |
| 1.5 A (full-load) | 3.276 V |

**Load regulation = (V_noload − V_fullload) / V_noload × 100 = (3.312 − 3.276) / 3.312 × 100 = 0.036 / 3.312 × 100 = 1.09%.**

**Result:** 1.09% is inside the 1.5% datasheet spec — the regulator itself is cleared. If a downstream node on this same rail later shows more than roughly 1.09% + a few tenths of a percent of additional sag versus the regulator-pin reading, that additional sag is attributable to the board's power path (connector/trace/via), not the regulator, and gets isolated with the node-to-node IR-drop method in SKILL.md's worked example, not by replacing the regulator.
