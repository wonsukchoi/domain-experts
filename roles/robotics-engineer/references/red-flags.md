# Red flags

Smell tests a robotics engineer catches on a first pass over a torque calculation, a kinematic model, a control-loop tuning result, or a collaborative-robot deployment.

### Actuator torque checked at a single "nominal" or "home" pose, not across the full range of motion

- **Usually means:** the sizing calculation used a convenient or typical pose instead of sweeping gravity torque across the worst-case (most-extended) pose and inertial torque across the fastest commanded move — these two worst cases frequently occur at different poses.
- **First question:** what pose produces the maximum gravity torque, and what pose/acceleration produces the maximum inertial torque, and were both actually checked?
- **Data to pull:** the torque-vs-joint-angle curve across the commanded range of motion, and the motion profile's peak angular acceleration.

### Payload rating quoted without the reach or mounting orientation it was rated at

- **Usually means:** the datasheet payload figure (e.g., "5 kg payload") is specific to a stated TCP offset and orientation (per ISO 9283-style spec sheets), and applying it at a longer reach or a different orientation silently understates the actual torque demand.
- **First question:** at what tool-center-point offset and orientation is the quoted payload rated, and does the actual application match that?
- **Data to pull:** the manufacturer's payload-vs-reach derating curve, not just the headline payload number.

### Repeatability spec cited to justify an absolute-accuracy requirement

- **Usually means:** the robot's ISO 9283 repeatability figure (variance returning to a taught point) is being used to answer an accuracy question (hitting an un-taught, CAD-derived coordinate) — the two are unrelated without a kinematic calibration step.
- **First question:** is the task teach-based (repeatability governs) or CAD/vision-coordinate-based (accuracy governs), and has accuracy actually been measured or calibrated for this unit?
- **Data to pull:** the ISO 9283 test report (repeatability) versus any kinematic calibration or absolute-accuracy verification data.

### PID gains carried over from a similar joint, a different payload, or a different unit without a retune

- **Usually means:** the gains were tuned against a specific reflected inertia and friction that changed with the new payload, gearbox, or unit-to-unit manufacturing variation.
- **First question:** was the ultimate gain/period (or equivalent plant characterization) re-measured on this specific hardware and payload, or copied?
- **Data to pull:** the bump-test or step-response data the gains were actually derived from, dated and tied to the specific unit and payload.

### Cartesian trajectory planned without checking Jacobian condition number near the workspace boundary

- **Usually means:** the path planner validated reach and joint limits but not manipulability, so a path passing near a wrist, elbow, or shoulder singularity can command a joint-velocity or torque spike for a small Cartesian-space move.
- **First question:** does the planned path cross a region where the Jacobian condition number exceeds the controller's velocity/torque headroom, and if so, is it replanned in joint space through that segment?
- **Data to pull:** the manipulability index or Jacobian condition number along the planned trajectory, and the controller's velocity/torque limits.

### "Collaborative-rated" robot deployed at a new speed, payload, or tool without rerunning ISO/TS 15066

- **Usually means:** the collaborative certification was established for a reference configuration, and the force/pressure (PFL) or separation-distance (SSM) calculation was not redone for the actual tool geometry, payload, and speed of the new application.
- **First question:** has the transient/quasi-static contact force and pressure been recalculated per body region for this specific end effector and payload, or is the deployment relying on the robot's generic cobot label?
- **Data to pull:** the ISO/TS 15066 Annex A calculation (or the vendor's application-specific safety data sheet) for the actual tool and payload in use.

### Intrusion distance (C) in a separation-distance calculation left at the generic 850 mm default

- **Usually means:** the calculation used the coarse-resolution ISO 13855 default without checking whether the actual sensor's detection resolution qualifies for a smaller, less conservative C value — needlessly enlarging the exclusion zone (or, worse, using a smaller C than the installed sensor's resolution actually supports).
- **First question:** what is the installed sensor's actual detection resolution, and does the ISO 13855 table entry used for C match that resolution?
- **Data to pull:** the safety scanner's certified detection resolution (mm) and the ISO 13855 table row it maps to.

### Encoder resolution upgraded to fix a positioning error that is actually backlash

- **Usually means:** the position error only appears on load-direction reversal (the signature of backlash/hysteresis), and no increase in encoder counts-per-revolution closes a gap that is mechanical lost motion, not a measurement-resolution limit.
- **First question:** does the error appear consistently, or only when the load direction reverses — and has the gear train's backlash spec actually been measured?
- **Data to pull:** a bidirectional repeatability test isolating approach-direction error, and the gearbox's rated backlash (arcmin).

### Gear ratio selected purely to meet torque, with reflected inertia far outside a 1:1-10:1 ratio to motor rotor inertia

- **Usually means:** the ratio clears the torque requirement but leaves the servo loop hard to tune — a large inertia mismatch (load inertia many multiples of motor rotor inertia after reflection) produces poor bandwidth and amplifies any backlash or compliance in the transmission.
- **First question:** what is the reflected load inertia at the selected ratio, and how does it compare to the motor's rotor inertia?
- **Data to pull:** motor rotor inertia from the datasheet, computed link/payload inertia, and the reflected-inertia ratio at the candidate gear ratio.

### DH parameters pulled from a datasheet or CAD export without confirming classic vs. modified convention

- **Usually means:** classic (Denavit-Hartenberg) and modified (Craig) DH conventions place the frame origin and rotation order differently, and mixing a parameter table written for one convention with a solver written for the other produces a forward-kinematics chain that is wrong in a way that isn't obviously wrong (small-angle poses can look plausible).
- **First question:** which convention does the parameter table's source use, and does the kinematic solver being used match it?
- **Data to pull:** the source documentation's explicit convention statement, and a known-pose sanity check (a pose whose Cartesian position can be verified by direct measurement or a second independent method).

### Motor sized against RMS/duty-cycle-average torque with no instantaneous peak-torque check

- **Usually means:** the thermal (continuous/RMS) rating clears the duty cycle, but the calculation never confirmed the highest instantaneous torque in the profile stays under the motor's or gearbox's absolute peak rating — a single excursion above peak can strip a gear tooth or demagnetize a motor even if the average is fine.
- **First question:** what is the single highest instantaneous torque in the commanded profile, and does it clear the peak (not just continuous) rating with margin?
- **Data to pull:** the full torque-vs-time profile for the duty cycle, not just its RMS value.
