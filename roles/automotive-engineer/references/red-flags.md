# Red flags

Smell tests an automotive engineer catches on a first pass over a vehicle-dynamics calculation, a powertrain-sizing estimate, a crash-structure design, or an NVH result.

### Friction-circle check run against static (not dynamic) tire normal loads

- **Usually means:** the combined lateral/longitudinal demand was checked against a nominal or static Fz, missing that weight transfer under the actual maneuver (braking, cornering, or acceleration) shifts load away from one or more tires — often the tire closest to saturating.
- **First question:** what is each tire's dynamic normal load at the specific combination of a_x and a_y being checked, not the vehicle's static or average value?
- **Data to pull:** the weight-transfer calculation (longitudinal and lateral) at the exact maneuver condition, and the per-tire Fz it produces.

### Brake or torque distribution set by a single fixed ratio (e.g., "60/40") with no load-sensitivity

- **Usually means:** the proportioning matches the static weight split, which is only correct at zero lateral and longitudinal acceleration — any real maneuver with combined demand shifts the load, and a fixed ratio over-demands the lightest-loaded corner.
- **First question:** does the proportioning (mechanical valve or EBD) respond to real-time or estimated per-corner load, or is it a single calibrated ratio?
- **Data to pull:** the proportioning valve's or EBD controller's calibration table across the vehicle's g-g envelope, not just its nominal setpoint.

### 0-60 or acceleration time computed from engine torque and gear ratio with no traction-limit check

- **Usually means:** the calculation assumes all available wheel force reaches the road, ignoring that the drive axle's dynamic normal load caps the deliverable force — common on high-torque, rear- or lightly-loaded-drive-axle vehicles.
- **First question:** at the computed acceleration, does the drive axle's dynamic load (static plus longitudinal weight transfer) actually support the claimed wheel force via μ·Fz?
- **Data to pull:** the drive-axle static load, wheelbase and CG height for the weight-transfer term, and the assumed tire-road friction coefficient.

### Crash-pulse deceleration reported only as an average, with no peak or pulse-shape stated

- **Usually means:** the average (v²/2d) figure is being used as if it were the number injury or component criteria are judged against, when many are peak- or short-duration-clip-based and a typical crash pulse peaks 1.5-2x the average.
- **First question:** what pulse shape (triangular, haversine, measured) is assumed, and what is the resulting peak, not just the average?
- **Data to pull:** the actual barrier-test accelerometer trace (or its assumed idealized shape) and the peak value it implies.

### Crush distance shortened for packaging without recomputing occupant deceleration

- **Usually means:** a styling, wheelbase, or overhang change reduced available crush distance, and the team is treating this as a packaging-only decision — for a fixed impact energy, less crush distance always raises occupant deceleration.
- **First question:** what is the new average and peak deceleration at the reduced crush distance, and does it still clear the target margin under restraint-system capability?
- **Data to pull:** the before/after crush-distance figures and the recomputed a_avg = v²/(2d) and peak estimate.

### Structure "strengthened" in response to a crash-test or simulation failure

- **Usually means:** the fix increased material stiffness rather than crush distance or crush-force uniformity, which for a fixed impact energy can raise occupant deceleration even as it improves structural integrity — stiffness and occupant protection are not the same objective.
- **First question:** does the proposed change increase crush distance or make the crush-force pulse more uniform (a lower, longer plateau), or does it just add stiffness without changing how much distance is used to absorb the energy?
- **Data to pull:** the force-deflection curve (not just peak force) before and after the proposed structural change.

### Powertrain-mount NVH check run only at nominal idle rpm

- **Usually means:** nominal idle (e.g., 800 rpm) clears the isolation check, but a lower sustained idle state (AC load, cold-start fast idle held long, engine lugging) pulls the excitation frequency down toward the mount system's natural frequency, and that condition was never checked.
- **First question:** what is the lowest sustained rpm the engine operates at in normal use (not just the nominal idle spec), and what is the frequency ratio r at that condition?
- **Data to pull:** the engine's idle rpm range across accessory-load states, and the mount system's measured (not just nominal datasheet) natural frequency.

### Mount stiffness reduced for NVH isolation without checking powertrain-travel clearance

- **Usually means:** a softer mount lowers the natural frequency and improves transmissibility, but also increases static droop and torque-roll travel under acceleration — a softer mount can bottom out against the chassis or over-articulate a driveline CV joint under load the NVH calculation didn't check.
- **First question:** what is the powertrain's static and dynamic (wide-open-throttle) travel at the proposed stiffness, and does it clear the physical clearance and CV-joint angle limits?
- **Data to pull:** the powertrain-mount travel measurement or simulation at full-throttle torque reaction, and the packaged clearance to the chassis and driveline articulation limit.

### Rolling resistance and aerodynamic drag omitted from a top-speed or steady-cruise force balance

- **Usually means:** these terms are correctly negligible at launch (tens to low hundreds of newtons against thousands of newtons of available force) but become first-order near top speed or steady highway cruise, where they're the terms actually being balanced against available power.
- **First question:** at the speed this calculation is evaluating, are rolling resistance and drag a small or a dominant fraction of the total force balance?
- **Data to pull:** the drag coefficient, frontal area, and rolling-resistance coefficient used, and the resulting force magnitude relative to available engine/traction force at that speed.

### Tire friction coefficient assumed at a single generic value (e.g., μ = 1.0) with no surface or tire-type qualifier

- **Usually means:** μ varies substantially with surface (dry asphalt vs. wet vs. gravel) and tire compound/type (performance summer vs. all-season vs. winter) — a generic "1.0" or "0.9" carried through a safety-relevant calculation without stating the assumed condition silently narrows or invalidates the result's applicability.
- **First question:** what surface and tire condition is this μ value assumed for, and is that the governing (often worst-case, not best-case) condition for the requirement being checked?
- **Data to pull:** the tire manufacturer's or test program's measured μ for the specific surface/condition pairing being designed against.

### Weight-transfer or friction-circle calculation that doesn't reconcile per-tire loads to total vehicle weight

- **Usually means:** an arithmetic or sign error in splitting longitudinal and lateral transfer across the four tires — the four dynamic Fz values must sum exactly to total vehicle weight regardless of the maneuver, and a mismatch means the transfer terms were double-counted, dropped, or misassigned to the wrong tire.
- **First question:** do the four computed per-tire normal loads sum exactly to the vehicle's static weight?
- **Data to pull:** the full per-tire Fz breakdown with the reconciliation sum shown, not just the final numbers used in the friction-circle check.

### Engine peak power or torque used directly in a mid-speed force calculation without accounting for where in the rpm range it occurs

- **Usually means:** peak torque and peak power occur at different rpm, and using peak power's implied force (P/v) at a speed where the engine is not actually near that rpm (wrong gear, off the power peak) overstates available force at that specific speed.
- **First question:** at the vehicle speed and gear this calculation applies to, what rpm is the engine actually at, and is that near the torque or power peak the calculation assumed?
- **Data to pull:** the full torque-vs-rpm curve and the gear/speed-to-rpm mapping for the specific point in the calculation.
