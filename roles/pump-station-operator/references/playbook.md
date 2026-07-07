# Playbook

Filled procedures and reference tables for the four recurring judgment calls: NPSH/cavitation margin, wet-well level control and SSO reporting, water-hammer/surge sizing, and pump-curve-to-system-curve matching.

## 1. NPSH margin calculation

NPSH available (NPSHa) — what the suction side of the system actually provides — must exceed NPSH required (NPSHr) — what the specific pump needs at that flow, from the manufacturer's curve — by a margin, not just a positive number.

**NPSHa formula:** NPSHa = Ha ± Hs − Hf − Hvp

| Term | Meaning | Example value |
|---|---|---|
| Ha | Atmospheric pressure head (at elevation, in ft of liquid) | 33.9 ft (sea level, water) |
| Hs | Static head from suction-source surface to pump centerline (+ if flooded suction, − if suction lift) | +6 ft (flooded, wet well above pump) |
| Hf | Friction losses in the suction piping at this flow | 1.9 ft |
| Hvp | Vapor pressure head of the liquid at pumping temperature | 0.5 ft (60°F water) |

NPSHa = 33.9 + 6 − 1.9 − 0.5 = **37.5 ft**

| Field | Example value | Note |
|---|---|---|
| NPSHr (from pump curve at 1,400 gpm duty flow) | 18 ft | Read off the manufacturer's curve at actual flow, not rated/nameplate flow — NPSHr rises with flow |
| NPSHa | 37.5 ft | From table above |
| Margin ratio (NPSHa / NPSHr) | 37.5 / 18 = **2.08** | Above the 1.2 minimum — healthy margin |
| Margin ratio if wet well drops 20 ft (suction lift instead of flooded) | (33.9 − 20 − 1.9 − 0.5) / 18 = 11.5 / 18 = **0.64** | Below 1.0 — NPSHa less than NPSHr, cavitation guaranteed, not just at risk |

**Rule:** margin ratio ≥ 1.2 for standard-duty pumps; high-suction-energy pumps (large impeller-eye velocity, high speed) need a materially higher ratio per the manufacturer — confirm rather than assume 1.2 covers every pump on site.

## 2. Wet well level control and SSO reporting

**Level-control elevations (example lift station, wet well floor = 0 ft):**

| Elevation | Value | Function |
|---|---|---|
| Lag pump on | 6.0 ft | Second pump starts if lead can't keep up |
| Lead pump on | 5.0 ft | Normal cycling start |
| Lead pump off | 2.5 ft | Normal cycling stop |
| High-level alarm | 7.5 ft | Dispatch/standby trigger — set to leave a working buffer before overflow |
| Rim/overflow elevation | 9.0 ft | Physical point liquid leaves containment |

Freeboard between high-level alarm and overflow: 9.0 − 7.5 = 1.5 ft. At a typical inflow rate for the station (e.g., 800 gpm during a wet-weather peak) and a wet well cross-sectional volume of 1.5 ft × 1,200 gal/ft, that 1.5 ft of freeboard represents roughly 1,800 gal ÷ 800 gpm ≈ **2.25 minutes** before overflow once both pumps are down — treat the alarm as the start of a response window measured in minutes, not a scheduling item for the next round.

**SSO reporting timeline (representative structure — confirm the applicable state program):**

| Step | Typical trigger | Typical timeline |
|---|---|---|
| Internal notification/dispatch | High-level alarm or confirmed overflow | Immediate |
| Verbal/electronic notice to state agency | Discharge reaches surface water, or exceeds a volume threshold (e.g., 1,000 gal) | Within 2–24 hours of discovery, depending on state program |
| Public health notification (if surface water reached) | Same as above | Often within 2 hours for water-contact risk |
| Written/electronic follow-up report | Any reportable SSO | Often within 3–5 business days |

**Rule:** the reporting clock starts at discovery of an actual or imminent overflow, not at confirmation of physical discharge — treat a high-level alarm with both pumps down and rising level as already inside the notification window.

## 3. Water-hammer / surge sizing

**Joukowsky surge (instantaneous or faster-than-critical-period closure):**

ΔH = a·ΔV / g (ft of head), then ΔP (psi) = ΔH × 0.433 (for water)

| Pipe material | Typical wave speed (a) |
|---|---|
| Steel, unlined | 4,000–4,500 ft/s |
| Ductile iron, cement-mortar lined | 3,500–3,900 ft/s |
| PVC/HDPE | 1,200–1,600 ft/s (much softer, lower surge for the same ΔV) |

**Critical (pipe) period:** Tc = 2L/a — the round-trip time for the pressure wave to travel to the nearest reflection point (open end, reservoir, large-diameter junction) and back.

**Closure classification:**
- Tclose < Tc → "instantaneous" closure — full Joukowsky ΔP applies.
- Tclose > Tc → "slow" closure — surge reduces roughly proportionally: ΔP_actual ≈ ΔP_instant × (Tc / Tclose).

**Filled example (booster station isolation valve):** L = 4,500 ft, a = 3,700 ft/s, ΔV = 5 ft/s.
- Tc = 2(4,500)/3,700 = 2.43 s
- ΔP_instant = (3,700 × 5 / 32.2) × 0.433 ≈ 248.8 psi
- Target ΔP_actual = 70 psi (to stay within a 150 psi-rated downstream section at 80 psi baseline)
- Required Tclose = Tc × (ΔP_instant / ΔP_actual) = 2.43 × (248.8/70) ≈ 8.6 s → set actuator to 15 s for margin

**Surge-control options, in typical preference order for a booster/lift station:**
1. Slow-closing or two-speed check valves and actuators sized against the calculated Tc.
2. VFD-controlled soft-start/soft-stop on pumps to ramp velocity change instead of stepping it.
3. Surge (hydropneumatic) tanks or air/vacuum valves at high points, where closure-time control alone can't meet the pressure rating.
4. Pipe/fitting upgrade to a higher pressure class, as a last resort when none of the above brings the transient within rating.

## 4. Dry-run / loss-of-prime protection

| Condition | Typical trip point | Consequence if unprotected |
|---|---|---|
| Suction pressure | Trip below ~5 psi or per manufacturer minimum | Seal faces run without lubricating film |
| Seal-chamber temperature | Trip above manufacturer limit (often 200°F region for elastomer components) | Elastomer/O-ring damage, face cracking on hard-face seals |
| Time to seal damage once dry | Seconds to low minutes, not a full round-length | No time for a manual response after the fact |

**Rule:** automatic instrumented trip on suction pressure or seal temperature, not operator judgment — the damage window is shorter than the interval between rounds or SCADA polling in many configurations, so detection must be automatic and the trip must stop the pump before restart is attempted.

## 5. Pump curve vs. system curve

| Flow (gpm) | Pump head (ft, from curve) | System head required (static + friction, ft) | Note |
|---|---|---|---|
| 800 | 145 | 95 | Pump can deliver far more head than the system needs at this flow |
| 1,200 | 128 | 118 | Approaching intersection |
| 1,400 | 118 | 118 | **Duty point** — where pump curve meets system curve |
| 1,600 | 104 | 132 | Pump can't meet system demand past this flow |

**BEP and operating region:** if this pump's best efficiency point is 1,450 gpm, the duty point (1,400 gpm) sits at 1,400/1,450 ≈ 96.6% of BEP — inside the 70–120% preferred operating region. If a downstream valve is throttled and the system curve steepens, pushing the duty point down to 900 gpm (900/1,450 ≈ 62% of BEP), that falls below the preferred region even though the pump is still "delivering flow" — expect increased radial thrust, vibration, and reduced bearing/seal life, and treat it as a system-curve problem (valve position, downstream demand) rather than a pump problem.
