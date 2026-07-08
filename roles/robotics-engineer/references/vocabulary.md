# Vocabulary

Terms generalists flatten together that a robotics engineer keeps sharply separate — the value is in the misuse, not the definition.

## Repeatability vs. accuracy

**Repeatability** (ISO 9283) is the variance in position when the robot returns to the same taught point many times. **Accuracy** is the absolute error between a commanded coordinate (from CAD, vision, or a calculation) and the position the robot actually achieves — dominated by kinematic-model error, not repeatability.

**In use:** "The spec sheet's ±0.02 mm is repeatability — for vision-guided picking off an un-taught coordinate we need the accuracy number, and that's usually an order of magnitude worse before calibration."

**Common misuse:** citing a repeatability figure to justify a task that requires accuracy (hitting a computed, not taught, coordinate), when the two numbers can differ by 10x or more on an uncalibrated arm.

## Payload vs. rated payload

**Payload** informally means "how much it can carry." **Rated payload** is a specific number tied to a stated tool-center-point offset and orientation on the datasheet — the same robot's usable payload drops as reach from the flange increases, per the manufacturer's payload-vs-reach derating curve.

**In use:** "5 kg rated payload is at 50 mm from the flange, vertical mount — our gripper puts the load center 180 mm out, so we're pulling the derating curve, not the headline number."

**Common misuse:** applying the headline rated-payload figure at an arbitrary tool offset or orientation without consulting the derating curve.

## Degrees of freedom (DOF) vs. redundancy

**Degrees of freedom** is the count of independently controllable joints. **Kinematic redundancy** means the arm has more DOF than the task space requires (more than 6 for a general 6D pose task) — the extra DOF gives a null-space of solutions that can be used to avoid obstacles or singularities without changing the end-effector pose.

**In use:** "It's a 7-DOF arm on a 6-DOF pick task — we use the redundant axis to steer the elbow away from the fixture, not to change where the gripper ends up."

**Common misuse:** treating "more DOF" as simply "more capable" without recognizing redundancy specifically buys null-space maneuverability, which needs its own resolution method (e.g., pseudoinverse with null-space projection) to exploit.

## Forward kinematics vs. inverse kinematics

**Forward kinematics** computes end-effector pose from known joint angles — always a single, well-defined answer. **Inverse kinematics** computes joint angles from a desired end-effector pose — can have zero, one, or multiple valid solutions (elbow-up vs. elbow-down, for example), and the solver must pick a branch.

**In use:** "FK gave us the wrist center for a sanity check; the IK solve returned two valid elbow solutions and we picked elbow-down to stay clear of the fixture."

**Common misuse:** assuming inverse kinematics always has a unique answer, or ignoring which solution branch a solver returned when multiple are valid.

## Kinematic singularity

A configuration where the manipulator Jacobian loses rank, so some Cartesian-space velocity direction becomes unachievable no matter how fast the joints move — near a singularity, a small commanded Cartesian velocity can demand very large joint velocities. Common types: wrist singularity (last three axes align), elbow/boundary singularity (arm fully extended), shoulder singularity (wrist center crosses the axis-1 line).

**In use:** "The path grazes a wrist singularity at that pose — replanning through it in joint space instead of holding a Cartesian-space line."

**Common misuse:** treating singularities only as workspace-boundary edge cases irrelevant to normal operation, when a poorly planned interior path can pass close enough to one to spike joint velocity mid-motion.

## Jacobian / manipulability

The **Jacobian** maps joint velocities to end-effector velocity; its condition number (or a derived manipulability index) quantifies how far a configuration is from a singularity — a well-conditioned Jacobian means commanded Cartesian velocities map to joint velocities without amplification.

**In use:** "Manipulability index drops below 0.05 near the boundary of this workspace — that's our replanning trigger, not just staying inside the reach circle."

**Common misuse:** using reach (a purely geometric workspace boundary) as the only path-planning constraint, ignoring that manipulability can collapse well before the geometric reach limit.

## Denavit-Hartenberg (DH) parameters — classic vs. modified

A four-parameter (a, α, d, θ) convention for describing consecutive joint-axis frames along a serial-link chain, used to build the forward-kinematics transform chain. The **classic** (Denavit-Hartenberg) and **modified** (Craig) conventions place the frame origin and rotation order differently, and a parameter table written for one produces a wrong chain if fed into a solver built for the other.

**In use:** "This vendor's URDF export uses modified DH — confirm the solver matches before trusting the FK output on an asymmetric pose."

**Common misuse:** copying a DH table from one source into a solver built for the other convention without checking, producing forward-kinematics results that look plausible at small angles but diverge at larger ones.

## Reflected inertia

The load-side inertia as it appears at the motor shaft, scaled by the square of the gear ratio (I_reflected = I_load / N²) — a small physical load inertia can dominate or be dominated by the motor's own rotor inertia depending on the gear ratio chosen.

**In use:** "At 250:1 the payload's inertia reflects down to almost nothing at the motor — we picked the ratio for torque, but check the reflected-inertia ratio before assuming the loop will tune easily."

**Common misuse:** selecting a gear ratio purely to satisfy a torque requirement without checking the resulting reflected-inertia ratio against the motor's rotor inertia, which governs how tunable the servo loop actually is.

## Safety-rated Monitored Stop (SRMS) vs. Category 0/1 stop

A **Category 0 stop** (IEC 60204-1) removes power immediately (uncontrolled coast/brake); a **Category 1 stop** decelerates under power then removes it. A **Safety-rated Monitored Stop** holds servo position with power still applied and motion actively monitored — the robot doesn't move, but power isn't removed, which matters for collaborative applications where a person can approach a "stopped" but still-powered robot.

**In use:** "It's an SRMS, not a Category 0 stop — the joints are still under servo control, so verify the safety function actually detects any motion, not just that the robot looks still."

**Common misuse:** assuming any "stopped" robot has had power removed, when an SRMS-stopped robot is fully energized and will resume motion the instant the monitored condition clears.

## Performance Level (PLr) vs. SIL

**Performance Level required (PLr)**, per ISO 13849-1, is the safety-integrity target (a-e) for a machinery safety function, derived from severity, exposure, and avoidability of the hazard. **SIL** (IEC 61508/62061) is the analogous electrical/electronic safety-integrity target used more in process-industry and complex electronic safety systems. They use different derivation methods and aren't a direct 1:1 mapping despite rough equivalence tables.

**In use:** "The risk assessment calls for PLr = d on this guard interlock — confirm the safety relay's rated PL, not just its SIL number, since the standards aren't derived the same way."

**Common misuse:** treating a component's SIL rating as automatically satisfying a PLr requirement (or vice versa) without checking the actual mapping and the specific safety function's architecture.

## Power and Force Limiting (PFL) vs. Speed and Separation Monitoring (SSM)

The two collaborative-operation modes under ISO/TS 15066. **PFL** allows contact between robot and human but limits transient/quasi-static force and pressure per body region to Annex A thresholds. **SSM** avoids contact entirely by maintaining a continuously recalculated protective separation distance, slowing or stopping the robot as a person approaches.

**In use:** "This end effector can't clear PFL's pinch-point pressure limit at the gripper jaw — falling back to SSM with a computed separation distance instead."

**Common misuse:** assuming a robot certified for PFL under one tool automatically satisfies PFL with a different, un-tested end effector, instead of rerunning the biomechanical limit check for the actual tool.

## Protective separation distance

The minimum distance (per ISO/TS 15066 Annex A) that must be maintained between a person and a robot operating under SSM, computed from human approach speed, robot speed and stopping distance, sensor intrusion distance, and position uncertainties — not a fixed, robot-independent number.

**In use:** "Dropping the SSM-mode speed from 0.5 to 0.25 m/s shrinks the protective separation distance from 1.315 m to about 1.24 m — worth it if the cell layout is tight."

**Common misuse:** treating the separation distance as a fixed property of the robot model rather than a calculation that changes with speed, payload, sensor resolution, and end-effector geometry.

## Workspace envelope vs. reach

**Reach** is the maximum radial distance the wrist center or TCP can achieve from the base axis. **Workspace envelope** is the full 3D (or 2D, for a planar mechanism) volume the TCP can actually occupy across all joint combinations, which is not a simple sphere or circle of the reach radius — it excludes regions blocked by joint limits, self-collision, or singular configurations.

**In use:** "The reach spec says 850 mm, but the actual workspace envelope has a dead zone directly overhead where the wrist can't maintain the required tool orientation."

**Common misuse:** assuming any point within the reach radius is reachable at any orientation, when joint limits and orientation constraints carve unreachable pockets out of the nominal reach sphere.

## Backlash vs. hysteresis

**Backlash** is the mechanical lost motion in a gear train — the angular gap the input can move before the output responds, on direction reversal. **Hysteresis** is the broader, more general phenomenon of output lagging input differently depending on direction of travel, of which backlash is one mechanical cause (others include compliance and friction stiction).

**In use:** "The position error only shows up on direction reversal — that's backlash, not encoder noise, and no amount of encoder resolution fixes it."

**Common misuse:** diagnosing a direction-reversal position error as a sensor or control-tuning problem and increasing encoder resolution or loop gain, when the root cause is mechanical lost motion in the transmission.

## Tool Center Point (TCP) vs. flange frame

The **flange frame** is the fixed mechanical reference at the robot's mounting face for the end effector. The **Tool Center Point** is a user-defined frame, offset from the flange, representing the functional point of the tool (a gripper's fingertip contact point, a welder's arc point) — all motion commands and payload/reach specs are relative to whichever frame is actually configured.

**In use:** "Confirm the TCP offset is set to the gripper's actual contact point before trusting the reach or payload numbers — they're meaningless relative to the bare flange."

**Common misuse:** running reach, payload, or accuracy calculations against the flange frame instead of the configured TCP, producing numbers that don't match the tool's actual working point.

## Duty cycle rating (S1-S9)

IEC 60034-1 motor duty-type classification describing the load-time pattern a motor's thermal rating assumes — S1 is continuous duty at rated load, S3 is intermittent periodic duty at a stated on-time percentage, and so on. A motor's continuous torque rating is only valid under the duty cycle it was rated for; a higher-duty-cycle application than the rating assumes will overheat the motor even under an apparently acceptable average torque.

**In use:** "The continuous torque spec assumes S1 — our actual duty cycle is closer to S3 at 40% on-time, so check whether the thermal model actually allows the higher instantaneous torque we're commanding."

**Common misuse:** comparing an application's average commanded torque directly against a motor's continuous (S1) rating without checking whether the datasheet number assumes a duty cycle the application doesn't match.
