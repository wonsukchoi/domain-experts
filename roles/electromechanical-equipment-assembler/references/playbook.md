# Playbook

## Shaft alignment verification worksheet

Fill for any assembly with a rotating shaft coupling.

| Field | Value |
|---|---|
| Assembly | Actuator #ACT-4471, Motor-Gearbox |
| Spec max radial misalignment | 0.005" |
| Initial measured misalignment | 0.014" (2.8x spec) |
| Corrective action | Motor mount shimming |
| Post-correction measured misalignment | 0.003" (within spec) |
| Estimated bearing life at spec alignment | ~20,000 hrs |
| Estimated bearing life at 2.8x misalignment (if uncorrected) | ~8,000-10,000 hrs |
| Motor mounting bolt torque spec | 45 in-lb ± 5 |
| Actual torque applied (calibrated wrench) | 43 in-lb |

**Rule:** always measure alignment directly with a dial indicator or equivalent — a functional test (motor runs, device works) does not confirm alignment is within spec.

## Electrical-vs-mechanical diagnostic table

| Symptom | Check electrical first | Check mechanical first | Notes |
|---|---|---|---|
| Device intermittently stops/starts | Continuity, connection tightness | Binding, alignment under load | Check both — symptom is ambiguous |
| Unusual vibration or noise | Loose electrical connection causing arcing (rare) | Misalignment, bearing wear, loose mounting | Mechanical more likely, but verify electrical isn't contributing |
| Device runs but underperforms | Voltage drop, connection resistance | Mechanical binding increasing load | Measure electrical parameters AND check for mechanical resistance |
| Complete failure to start | Power supply, wiring, fuse/breaker | Mechanical seizure/lockup | Check power delivery first, then mechanical free movement |

**Rule:** don't assume domain based on the most recent similar issue — check the specific evidence (continuity test vs. alignment/binding check) for this specific occurrence.

## Torque/wire-routing verification checklist

1. Confirm the specific torque value for each fastener type/size in the assembly (not a single blanket value).
2. Apply torque using a calibrated tool, verified within its calibration date.
3. Route wiring considering the equipment's full range of motion, not just its current/static position.
4. Move the equipment through its full range of motion (where safely possible) to verify wire clearance and absence of chafing points.
5. Perform the specified functional test plan, including break-in/thermal cycling test if specified for this equipment.
6. Document torque values, alignment measurements, and all test results (not just pass/fail) before releasing the assembly.
