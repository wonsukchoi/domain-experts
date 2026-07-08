# Playbook

Filled worked calculations for the three artifact types this role produces most often: a DH-parameter forward/inverse kinematics derivation, an encoder-resolution selection against an end-effector accuracy budget, and an ISO/TS 15066 protective separation distance for a collaborative deployment. Populate with the actual robot's numbers; the structure and arithmetic below are real and reconcile.

## DH-parameter forward and inverse kinematics — 3-DOF articulated (RRR) arm

**Structure:** waist yaw (θ1), shoulder pitch (θ2), elbow pitch (θ3), solving to the wrist center. Classic Denavit-Hartenberg table:

| i | αi-1 | ai-1 | di | θi |
|---|---|---|---|---|
| 1 | 0 | 0 | d1 = 0.30 m | θ1 (variable) |
| 2 | -90° | 0 | 0 | θ2 (variable) |
| 3 | 0 | a2 = 0.40 m | 0 | θ3 (variable) |
| wrist offset | 0 | a3 = 0.35 m | 0 | 0 (fixed) |

Chaining the DH transforms for this shoulder-offset-free articulated geometry reduces to the standard closed form (Spong et al.):

```
r = a2·cos(θ2) + a3·cos(θ2 + θ3)      # horizontal reach in the arm's vertical plane
z = d1 + a2·sin(θ2) + a3·sin(θ2 + θ3) # height
x = r·cos(θ1)
y = r·sin(θ1)
```

**Forward kinematics, given θ1 = 30°, θ2 = 45°, θ3 = -30°:**

θ2 + θ3 = 15°.
r = 0.40·cos(45°) + 0.35·cos(15°) = 0.40 × 0.7071 + 0.35 × 0.9659 = 0.28284 + 0.33807 = **0.62091 m**.
z = 0.30 + 0.40·sin(45°) + 0.35·sin(15°) = 0.30 + 0.28284 + 0.09059 = **0.67343 m**.
x = 0.62091 × cos(30°) = 0.62091 × 0.8660 = **0.53772 m**.
y = 0.62091 × sin(30°) = 0.62091 × 0.5000 = **0.31046 m**.

Wrist center: **(x, y, z) = (0.5377, 0.3105, 0.6734) m.**

**Inverse kinematics — solving back from (0.5377, 0.3105, 0.6734):**

θ1 = atan2(y, x) = atan2(0.31046, 0.53772) = **30.00°** ✓ (arctan(0.31046/0.53772) = arctan(0.5773) = 30.00°)

r = √(x² + y²) = √(0.28925 + 0.09639) = √0.38564 = 0.62100 m ✓ matches forward result within rounding.
s = z - d1 = 0.67343 - 0.30 = 0.37343 m.

Law of cosines for the elbow angle: D = (r² + s² - a2² - a3²) / (2·a2·a3) = (0.38564 + 0.13945 - 0.16 - 0.1225) / (2 × 0.40 × 0.35) = 0.24259 / 0.28 = **0.86639**.
θ3 = atan2(-√(1 - D²), D) = atan2(-√(1 - 0.75063), 0.86639) = atan2(-0.49937, 0.86639) = **-29.99°** ✓ matches the original -30° (elbow-down branch selected to match; the elbow-up branch atan2(+0.49937, 0.86639) = +29.99° is the other valid solution for this reach).

θ2 = atan2(s, r) - atan2(a3·sin(θ3), a2 + a3·cos(θ3)) = atan2(0.37343, 0.62100) - atan2(0.35 × sin(-30°), 0.40 + 0.35 × cos(-30°)) = 31.02° - atan2(-0.175, 0.70310) = 31.02° - (-13.98°) = **45.00°** ✓ matches the original θ2.

Forward-then-inverse reconciles exactly to the original (θ1, θ2, θ3) = (30°, 45°, -30°), confirming the DH table and both kinematic chains are consistent with each other.

## Encoder resolution — end-effector accuracy budget through a gear ratio

**Requirement:** end-effector position accuracy ≤ ±0.05 mm at an effective reach of L = 0.75 m from the shoulder axis (assembly task tolerance). Joint gear ratio N = 250:1, encoder mounted on the motor shaft (upstream of the gearbox).

**Step 1 — convert linear accuracy to joint-angle resolution at the output.**
Δθ_out(max) = Δx / L = 0.00005 m / 0.75 m = **6.667 × 10⁻⁵ rad** (0.00382°).

**Step 2 — refer that requirement back through the gear ratio to the motor shaft** (encoder resolution needed before reduction is coarser by a factor of N):
Δθ_motor(max) = Δθ_out(max) × N = 6.667 × 10⁻⁵ × 250 = **0.016667 rad** (0.9549°).

**Step 3 — convert to minimum encoder counts per revolution:**
counts_min = 2π / Δθ_motor(max) = 6.2832 / 0.016667 = **376.9 counts/rev minimum.**

**Step 4 — select a standard part and verify margin.** A 1024-line incremental encoder with quadrature (×4) decoding gives 4096 counts/rev.
Δθ_motor(actual) = 2π / 4096 = **0.0015340 rad**.
Δθ_out(actual) = Δθ_motor(actual) / N = 0.0015340 / 250 = **6.136 × 10⁻⁶ rad**.
Δx(actual) = Δθ_out(actual) × L = 6.136 × 10⁻⁶ × 0.75 = **0.0000046 m = 0.0046 mm**.

0.0046 mm against the 0.05 mm requirement is an **10.9x margin** — the 1024-line/×4 encoder clears the accuracy budget with room for the kinematic-model error and thermal drift the resolution calculation doesn't capture. Note this budget is resolution only; it does not close a backlash-driven position error on load reversal, which is a separate mechanical spec (see red-flags.md).

## ISO/TS 15066 protective separation distance — Speed and Separation Monitoring (SSM)

**Deployment:** a robot joint operating at a reduced SSM-mode speed near a safety-rated laser scanner, no power/force-limiting compliance established for this tool — separation distance must be maintained instead. Protective separation distance per ISO/TS 15066 Annex A:

```
S(t0) = Sh(t0) + Sr(t0) + Ss(t0) + C + Zd + Zr
```

| Term | Meaning | Value | Basis |
|---|---|---|---|
| Sh | Human approach contribution, Vh × Ts | 1.6 m/s × 0.15 s = **0.240 m** | Vh = 1.6 m/s default human speed (ISO 13855/ISO TS 15066); Ts = 0.15 s combined scanner detection + safety-PLC processing time |
| Sr | Robot motion during its own reaction delay, Vr × Tr | 0.5 m/s × 0.10 s = **0.050 m** | Vr = 0.5 m/s commanded SSM-mode speed; Tr = 0.10 s time from stop command to start of deceleration (robot's safety-rated monitored-stop spec) |
| Ss | Robot stopping distance during braking, Vr²/(2a) | 0.5² / (2 × 5) = **0.025 m** | a = 5 m/s² safety-rated deceleration at this speed/payload per manufacturer spec |
| C | Intrusion distance | **0.850 m** | ISO 13855 default for the scanner's detection-zone resolution used in this cell (reducible with finer sensor resolution — see red-flags.md) |
| Zd | Detection-system position uncertainty | **0.100 m** | Scanner measurement tolerance per datasheet |
| Zr | Robot position uncertainty | **0.050 m** | Encoder/servo tracking error at the tool center point |

S(t0) = 0.240 + 0.050 + 0.025 + 0.850 + 0.100 + 0.050 = **1.315 m minimum protective separation distance.**

**Reading:** the scanner's warning/protective field boundary must be set at least 1.315 m from the robot's reachable envelope at this speed, payload, and sensor configuration. If the robot instead scales speed down dynamically as a person approaches (true dynamic SSM rather than a single fixed zone), recompute S(t0) at each candidate Vr — dropping Vr to 0.25 m/s shrinks Sr to 0.025 m and Ss to 0.00625 m, tightening S(t0) to roughly 1.24 m, trading cycle time for a smaller exclusion zone. Re-run this calculation for any change to speed, payload (which changes a and Tr), scanner resolution (which changes C), or end-effector geometry.
