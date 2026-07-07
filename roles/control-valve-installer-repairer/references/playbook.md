# Playbook

Filled worksheets a valve tech actually runs, not descriptions of them — adapt the numbers to the valve and service in front of you.

## 1. Cv/Cg sizing worksheet

**Liquid service** (ISA-75.01.01 simplified form, no choked-flow correction): Cv = Q × √(SG / ΔP), Q in gpm, ΔP in psi.

Example — boiler feedwater control valve: Q = 340 gpm, SG = 0.98, ΔP = 55 psi.
Cv = 340 × √(0.98/55) = 340 × √0.01782 = 340 × 0.1335 ≈ 45.4.

**Gas service** (simplified non-choked form): Cg ≈ Q_scfh / (1360 × P₁ × √(x / (SG_g × T))), where x = ΔP/P₁ (fraction, capped at the choked-flow limit x_T for the trim, typically 0.5–0.7 for a globe valve).

Example — natural gas letdown station: Q = 850,000 scfh, P₁ = 215 psia, ΔP = 60 psi (x = 60/215 = 0.279, below a typical x_T of 0.5 so flow is not choked), SG_g = 0.60, T = 520 °R.
Cg = 850,000 / (1360 × 215 × √(0.279/(0.60×520))) = 850,000 / (292,400 × √(0.279/312)) = 850,000 / (292,400 × 0.02991) = 850,000 / 8,745 ≈ 97.2.

**Sizing-margin check:** pick trim so required Cv/Cg falls between 20% and 80% of the trim's rated (100%-travel) value at normal flow, with the maximum-flow case landing no higher than ~85–90% of rated to leave stroke margin. A required value under 20% of rated flags oversizing (see red-flags.md); over 90% at max flow flags undersizing with no turndown margin.

## 2. FCI 70-2 seat leakage class table

| Class | Allowable leakage (at specified test ΔP, per FCI 70-2) | Typical test medium |
|---|---|---|
| I | No test required — leakage rate by agreement, manufacturer's discretion | N/A |
| II | 0.5% of rated valve capacity (at full travel) | Water |
| III | 0.1% of rated valve capacity | Water |
| IV | 0.01% of rated valve capacity | Water |
| V | 5×10⁻⁴ mL/min of water per psi differential per inch of port diameter | Water |
| VI (bubble-tight) | Bubbles per minute, by seat port diameter (below) | Air or nitrogen |

**Class VI allowable bubble rate by port diameter (NPS, inches):**

| Port diameter | Bubbles/min |
|---|---|
| 1 | 1 |
| 1.5 | 2 |
| 2 | 3 |
| 2.5 | 4 |
| 3 | 6 |
| 4 | 11 |
| 6 | 27 |
| 8 | 45 |

Specify the class the *service* needs, not the tightest available — Class VI trim typically costs more, actuates with less smoothness near closed, and is more sensitive to debris than Class IV. Reserve VI for services where any measurable leak-through is a safety or product-quality event.

## 3. API 598 pressure test worksheet

| Test type | Test pressure | Purpose |
|---|---|---|
| Shell (hydrostatic) | 1.5× the valve's cold working pressure (CWP) rating per ASME B16.34 | Verifies pressure-boundary (body/bonnet) integrity |
| High-pressure closure (seat) | 1.1× CWP | Verifies seat leakage class at near-rated pressure |
| Low-pressure closure (seat), air/gas | Per manufacturer, typically 80–100 psig or lower | Verifies Class VI bubble-tight rating without over-stressing soft seats |

**Minimum hold times** (approximate size bands commonly used under API 598 — confirm exact durations against the current edition for the specific size before certifying a test):

| Valve size (NPS) | Approx. minimum hold time |
|---|---|
| ≤ 2 | 15 sec |
| 2½ – 6 | 60 sec |
| 8 – 18 | 60–120 sec |
| > 18 | Per manufacturer/owner spec |

Log the pressure-vs-time curve for the full hold, not just pass/fail at the end — a slow weep typically only shows as a pressure drop in the last third of the hold period, and that pattern is diagnostic (points to a seal/gasket/packing weep) versus an immediate drop (points to a gross defect).

## 4. Actuator thrust-margin worksheet

1. Compute the unbalanced force at worst-case shutoff ΔP: F_ΔP = ΔP_max × A_seat, where A_seat = π/4 × d² (d = orifice/seat diameter).
   Example: d = 3 in → A_seat = π/4 × 3² = 7.07 in². ΔP_max (full upstream pressure, atmospheric downstream, ESD case) = 285 psi.
   F_ΔP = 285 × 7.07 ≈ 2,015 lbf.
2. Add estimated packing friction: 150 lbf (measured or manufacturer-stated for the packing type/size in service).
   Required closing thrust = 2,015 + 150 = 2,165 lbf.
3. Compare to the actuator's rated thrust at minimum expected supply pressure (e.g., spring-return actuator thrust at a derated 60 psi supply, not the nameplate 80 psi): rated thrust = 3,000 lbf.
4. Margin = 3,000 / 2,165 ≈ 1.39 → 39% margin — within the commonly used 25–50% sizing guideline (manufacturer actuator-sizing literature, stated heuristic). Below ~25% margin, flag for actuator upsizing before the next shutdown; the shortfall won't show up until an actual upset/ESD demand.

## 5. PHMSA 49 CFR Part 192 interval-tracking worksheet

1. Pull the last documented test/inspection date for the pressure-limiting, pressure-regulating, or overpressure-protection device (§192.739, §192.743).
2. Regulatory deadline = last test date + 15 months (and no more than once per calendar year gap under the same section).
   Example: last test 2025-03-15 → hard deadline 2026-06-15.
3. Internal scheduling target = last test date + 12 months, leaving a 3-month buffer for a re-test if the device fails on first attempt.
   Example: internal target 2026-03-15.
4. For valves that might be required during an emergency (§192.745): inspect and partially operate at least once each calendar year, interval not to exceed 15 months — track on the same worksheet, separate line item per valve.
5. Any device found out of tolerance gets repaired and re-tested before the hard deadline, not scheduled to just meet it — a device that fails its only test that cycle with no time to correct is a compliance exposure, not just a maintenance backlog item.
