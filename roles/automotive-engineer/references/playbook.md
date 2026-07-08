# Playbook

Filled worked calculations for the three artifact types this role produces most often beyond the SKILL.md vehicle-dynamics example: a 0-60 mph powertrain-sizing calculation with a traction-versus-power-limit check, an FMVSS 208 crumple-zone crush-distance sizing, and a powertrain-mount NVH natural-frequency check. Populate with the actual vehicle's numbers; the structure and arithmetic below are real and reconcile.

## Powertrain sizing — 0-60 mph with traction-limit check (RWD)

**Vehicle:** m = 1500 kg (W = 14,715 N), wheelbase L = 2.70 m, h_cg = 0.50 m, static rear weight W_r = 6621.75 N (45%), rear-wheel drive, tire μ = 1.0, wheel radius r = 0.315 m, frontal area A = 2.2 m², drag coefficient Cd = 0.30, air density ρ = 1.225 kg/m³, rolling-resistance coefficient Crr = 0.012.

**Powertrain:** peak torque Te = 350 N·m, 1st-gear ratio Ng1 = 3.5, final-drive ratio Nfd = 3.9, driveline efficiency η = 0.90. Peak power (from torque/speed at the torque peak, 5500 rpm = 576.3 rad/s): P = Te·ω = 350 × 576.3 = **201,700 W (201.7 kW, ≈270 hp)**.

**Step 1 — engine/gearing-limited wheel force (naive read).**
F_engine = (Te × Ng1 × Nfd × η) / r = (350 × 3.5 × 3.9 × 0.90) / 0.315 = 4299.75 / 0.315 = **13,650.0 N**.
Naive a_x = F_engine / m = 13,650 / 1500 = **9.10 m/s²** → naive 0-60 mph (26.82 m/s) time = 26.82 / 9.10 = **2.95 s**. This is the number a torque-and-gearing-only calculation produces — and it is wrong, because it never checks whether the rear tires can put 13,650 N to the ground.

**Step 2 — solve the self-consistent traction-limited launch acceleration.** At launch, rear normal load is the static value plus longitudinal weight transfer at the (unknown) traction-limited a_x: Fz_r(a_x) = W_r + (a_x/g)·W·(h_cg/L). Setting traction force equal to m·a_x (traction-limited condition) and solving:
a_x = μ·W_r / [m·(1 − μ·h_cg/L)] = (1.0 × 6621.75) / [1500 × (1 − 1.0 × 0.50/2.70)] = 6621.75 / [1500 × 0.8148] = 6621.75 / 1222.2 = **5.418 m/s² (0.552g).**
Check: Fz_r at this a_x = 6621.75 + (5.418/9.81) × 14,715 × 0.1852 = 6621.75 + 0.5524 × 2725.7 = 6621.75 + 1505.8 = **8127.55 N**; Ft_max = μ × 8127.55 = 8127.55 N; a_x = 8127.55/1500 = 5.418 m/s² ✓ self-consistent.
Since 5.418 m/s² (traction-limited) < 9.10 m/s² (engine-limited), **the launch is traction-limited, not engine-limited** — the naive 2.95 s estimate is unachievable; the car cannot exceed 0.552g off the line regardless of torque.

**Step 3 — find the traction-to-power crossover speed.** Power-limited available force: F(v) = P·η/v = (201,700 × 0.90)/v = 181,530/v N. The traction ceiling at constant a_x = 5.418 m/s² is the constant 8127.55 N found above (Fz_r doesn't change with speed at constant a_x). Crossover: 181,530/v* = 8127.55 → **v* = 22.34 m/s (50.0 mph).**

**Step 4 — Phase 1 (traction-limited, 0 to 50 mph).**
t1 = v*/a_x = 22.34/5.418 = **4.124 s**; distance s1 = 0.5 × 5.418 × 4.124² = **46.08 m**.

**Step 5 — Phase 2 (power-limited, 50 to 60 mph), including rolling resistance and drag.** At midpoint speed v_mid = (22.34+26.82)/2 = 24.58 m/s: F(v_mid) = 181,530/24.58 = 7386.9 N. Rolling resistance F_rr = Crr·W = 0.012 × 14,715 = 176.6 N. Drag F_d = 0.5·ρ·Cd·A·v_mid² = 0.5 × 1.225 × 0.30 × 2.2 × 24.58² = 0.40425 × 604.2 = 244.3 N. Net force = 7386.9 − 176.6 − 244.3 = **6966.0 N**; a_x2 = 6966.0/1500 = **4.644 m/s²**.
Δv = 26.82 − 22.34 = 4.48 m/s; t2 = 4.48/4.644 = **0.965 s**.

**Deliverable — 0-60 mph acceleration memo (as filed):**

> **Naive (torque/gearing only) estimate:** 2.95 s. Not achievable — rear tires cannot deliver the 13,650 N of wheel force the powertrain can produce; traction-limited to 8127.6 N (0.552g) until the car reaches 50 mph.
> **Corrected estimate:** traction-limited phase (0-50 mph) = 4.124 s over 46.08 m; power-limited phase (50-60 mph) = 0.965 s. **Total 0-60 mph = 5.09 s.**
> **Design implication:** at this power-to-weight ratio and 45% static rear weight, the car is traction-limited for the first 4.1 s and 50 mph of the run — a limited-slip differential, launch control, or a rebalance toward a more rear-biased static weight split (or AWD) is a larger 0-60 lever than additional peak torque.

## FMVSS 208 crumple-zone crush-distance sizing

**Requirement:** FMVSS 208 full-frontal rigid-barrier test at v = 48.3 km/h (30 mph) = **13.417 m/s**, vehicle m = 1500 kg.

**Step 1 — baseline crush distance (as-designed), d = 0.65 m.**
Average deceleration: a_avg = v²/(2d) = 13.417²/(2 × 0.65) = 180.02/1.30 = **138.5 m/s² (14.12g).**
Average crush force: F_avg = m·a_avg = 1500 × 138.5 = **207,750 N**.
Energy check: KE = 0.5·m·v² = 0.5 × 1500 × 180.02 = **135,015 J**; F_avg·d = 207,750 × 0.65 = **135,037.5 J** ✓ reconciles (rounding).
Peak deceleration (haversine/half-sine pulse shape, peak ≈ (π/2) × average): a_peak = 1.5708 × 138.5 = **217.6 m/s² (22.19g).** This falls within the typical 20-30g peak range of a compliant passenger-car frontal pulse — acceptable margin against restraint-system capability (belt pretensioner + airbag ride-down is typically rated to manage chest deceleration well above this, with HIC15 ≤ 700 the governing pass/fail metric checked separately via dummy instrumentation, not derivable from this structural calculation alone).

**Step 2 — naive "stiffer is safer" design change: shorten front overhang, d reduced to 0.45 m.**
a_avg' = 180.02/(2 × 0.45) = 180.02/0.90 = **200.02 m/s² (20.39g).**
a_peak' = 1.5708 × 200.02 = **314.2 m/s² (32.03g).**
**This is worse, not better** — for the same impact energy, less crush distance raises both average and peak occupant deceleration (14.12g → 20.39g average, 22.19g → 32.03g peak, a 44% increase in peak g from a 31% reduction in crush distance). A stiffer structure that crushes less does not protect the occupant more; it protects the structure's own residual shape more, at the occupant's expense.

**Step 3 — solve for the minimum crush distance that holds peak deceleration at a 25g target** (a stated design margin below common restraint-system capability, not a regulatory number itself): a_avg,target = a_peak,target/1.5708 = 25×9.81/1.5708 = 245.25/1.5708 = **156.1 m/s².** d_min = v²/(2·a_avg,target) = 180.02/(2×156.1) = 180.02/312.2 = **0.577 m.**

**Deliverable — Crush-distance sizing memo (as filed):**

> **Target:** peak frontal-barrier deceleration ≤ 25g at the FMVSS 208 30 mph pulse, with a stated margin under restraint-system capability.
> **Minimum crush distance:** 0.577 m. **As-packaged crush distance:** 0.65 m — clears the target with 0.073 m (12.7%) of margin, average 14.12g / peak 22.19g.
> **Rejected alternative:** shortening the front overhang to 0.45 m to "stiffen" the structure raises peak deceleration to 32.03g (44% worse) for the same impact energy — the opposite of the intended effect. Crush distance, not stiffness, is the controlling lever; any packaging change that shortens it must be re-verified against the 25g target before approval.

## NVH — powertrain-mount natural frequency vs. firing-order excitation

**Powertrain:** mass m_p = 180 kg (engine + transmission), mounted on 4 elastomeric mounts, combined system stiffness k = 800,000 N/m (200 kN/m each). Engine: inline-4, 4-stroke (firing frequency = (rpm/60) × (cylinders/2)).

**Step 1 — mount-system natural frequency.**
f_n = (1/2π)·√(k/m_p) = (1/6.2832)·√(800,000/180) = (1/6.2832)·√4444.4 = (1/6.2832)·66.67 = **10.61 Hz.**

**Step 2 — excitation frequency at nominal idle (800 rpm).**
f_forcing = (800/60) × (4/2) = 13.33 × 2 = **26.67 Hz.**
Frequency ratio r = 26.67/10.61 = **2.514** (r > √2 = 1.414, isolated). Transmissibility (undamped): TR = 1/|r²−1| = 1/(6.320−1) = 1/5.320 = **0.188** — about 18.8% of engine shake force transmits to the body at nominal idle: acceptable isolation.

**Step 3 — check the worst case, not just nominal idle: lugging idle under AC load, 650 rpm.**
f_forcing' = (650/60) × 2 = 10.83 × 2 = **21.67 Hz.** r' = 21.67/10.61 = **2.043** (still > 1.414 — isolated). TR' = 1/(2.043²−1) = 1/(4.174−1) = 1/3.174 = **0.315** — 31.5% transmitted, worse than nominal idle but still within isolation (r > √2).

**Step 4 — evaluate a softer-mount proposal for further isolation, k reduced to 400,000 N/m.**
f_n' = (1/6.2832)·√(400,000/180) = (1/6.2832)·√2222.2 = (1/6.2832)·47.14 = **7.502 Hz.**
At lugging idle (21.67 Hz): r'' = 21.67/7.502 = **2.889.** TR'' = 1/(2.889²−1) = 1/(8.346−1) = 1/7.346 = **0.136** — improved to 13.6% transmitted (down from 31.5%).

**Deliverable — Powertrain-mount NVH memo (as filed):**

> **Baseline (k = 800 kN/m):** f_n = 10.61 Hz. Isolated at both nominal idle (26.67 Hz, TR = 18.8%) and lugging idle under AC load (21.67 Hz, TR = 31.5%) — the lugging-idle case is the governing (worst) condition and is the one that must clear spec, not nominal idle.
> **Softer-mount proposal (k = 400 kN/m):** f_n = 7.502 Hz, lugging-idle TR improves to 13.6% (56% reduction in transmitted force versus baseline).
> **Constraint to verify before adopting:** the softer mount roughly doubles static powertrain droop and increases torque-roll travel under wide-open-throttle load — re-check powertrain-to-chassis clearance and driveline CV-joint articulation angle at the softer stiffness before approving; an NVH win that bottoms the mount under hard acceleration is not a net improvement.
