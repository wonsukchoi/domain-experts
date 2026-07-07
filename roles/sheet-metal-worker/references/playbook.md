# Playbook

Filled reference tables and worked calculations a sheet metal worker actually runs on a job. Starting points to adapt to the specific pressure class and code edition in force — always confirm against the current SMACNA edition and local code adoption before locking a fabrication order.

## 1. Gauge selection by pressure class and dimension (galvanized steel, rectangular duct)

Per SMACNA HVAC Duct Construction Standards, minimum gauge is a function of the duct's longest side and the system's pressure class. Commonly summarized bands for low-pressure (≤2" wg) systems:

| Longest side | Minimum gauge |
|---|---|
| Up to 12" | 26 ga |
| 13"–30" | 24 ga |
| 31"–54" | 22 ga |
| 55"–60" | 20 ga |
| 61"–84" | 18 ga |

**Rule:** step up one gauge band per pressure-class increase (2" → 3" → 4" → 6" → 10" wg) at the same dimension, unless the table's specific pressure-class column says otherwise — never assume the low-pressure gauge carries over once reheat coils, VAV terminal boxes, or a fan upgrade push a segment into medium pressure. Reinforcement (cross-breaking, standing seams, tie rods) can substitute for a full gauge step on oversized sheets where SMACNA reinforcement tables permit it — that's an engineering trade, not a default.

**Worked check:** a 34"×16" return duct at 2" wg — longest side 34" falls in the 31"–54" band → 20 ga would be wrong (that band is 22 ga at low pressure); the same duct at 4" wg pressure class typically requires stepping to 20 ga. Always re-pull the table for the actual pressure class before ordering material.

## 2. Leakage class and seal class

**Formula:** CL = F ÷ ΔP^0.65, where CL = duct leakage class, F = leakage rate in cfm per 100 sq ft of duct surface, ΔP = test pressure differential in inches wg.

Rearranged for the allowable leakage at test pressure: **F = CL × ΔP^0.65**

| Leakage class | Typical use | Required seal class |
|---|---|---|
| Class 30 | Low-criticality, low-pressure, unsealed-acceptable systems | C (transverse joints only) |
| Class 24 | Standard low-pressure commercial ductwork | C or B |
| Class 12 | Medium-pressure systems, energy-code-driven low-pressure systems | B (transverse joints + longitudinal seams) |
| Class 6 | High-pressure systems; hospitals, labs, cleanrooms, other critical spaces | A (all joints, seams, and duct-wall penetrations) |
| Class 3 | Stringent — often specified by energy code on specific system types | A |

**Worked example:** a Class 6 duct segment tested at 2" wg. ΔP^0.65 = 2^0.65 ≈ 1.57. Allowable leakage F = 6 × 1.57 ≈ 9.4 cfm per 100 sq ft of duct surface at the 2" wg test pressure. A run with 400 sq ft of surface area may leak no more than ≈37.6 cfm total during the test — anything above that fails regardless of how much mastic was applied, because the failure is almost always an unsealed seam type the joint schedule should have caught, not "not enough sealant."

**Seal class decision rule:** if the pressure class is ≥3" wg, or the space served is a hospital, lab, cleanroom, or other critical-pressure-relationship space, default to Seal Class A and confirm the numeric leakage class target with the engineer before fabrication — don't wait for a failed test to discover the spec called for more than the minimum.

## 3. Transition and offset geometry

**Angle rule of thumb:** hold contraction (narrowing in the direction of flow) to ≤20° per side, and expansion (widening in the direction of flow) to ≤15° per side, to avoid flow separation and the added static pressure and noise that comes with it.

**Minimum transition length** for a given per-side dimension change d and angle limit θ:

length = d ÷ tan(θ)

| Dimension change (one side) | Contraction (20°/side) min. length | Expansion (15°/side) min. length |
|---|---|---|
| 2 in | 5.5 in | 7.5 in |
| 4 in | 11.0 in | 14.9 in |
| 6 in | 16.5 in | 22.4 in |
| 12 in | 33.0 in | 44.8 in |

If the available run is shorter than the table value for the actual dimension change, the fix isn't a steeper fitting — it's a different resize strategy (widen instead of narrow, split the change across two shallower transitions, or reroute).

## 4. Velocity and friction-rate impact of a resize

Friction rate scales approximately with velocity^1.9 for a given duct roughness. To estimate the new friction rate when velocity changes:

new friction rate ≈ old friction rate × (new velocity ÷ old velocity)^1.9

| Velocity ratio (new:old) | Approx. friction-rate multiplier |
|---|---|
| 1.2 : 1 | ~1.4x |
| 1.5 : 1 | ~2.1x |
| 2.0 : 1 | ~3.7x |
| 3.0 : 1 | ~8.0x |

**Practical noise ceiling:** hold velocity to roughly ≤1,500 fpm within about 10 ft of a diffuser, grille, or VAV box inlet to keep an occupied office space at NC-35 or better; trunk ducts further from terminals tolerate higher velocity (1,000–2,500 fpm depending on system type) before regenerated noise becomes the limiting factor rather than fan energy.

## 5. Hanger and support spacing (rectangular duct, galvanized)

Spacing tightens as duct perimeter (and therefore weight) grows — carrying over a small duct's spacing onto a much larger one under-supports it.

| Duct perimeter | Typical max hanger spacing | Support type |
|---|---|---|
| Up to ~48 in | 10 ft | Single strap hanger |
| ~49–60 in | 8 ft | Single strap hanger, heavier gauge strap |
| ~61–96 in | 8 ft | Trapeze-type support |
| Over ~96 in | Per engineered hanger schedule | Trapeze, engineered per SMACNA reinforcement tables |

## 6. Fire/smoke damper selection at a rated penetration

| Penetration type | Damper required | Typical listing | Actuation |
|---|---|---|---|
| Fire-rated wall or floor only | Fire damper | UL 555, rated to match or exceed the assembly rating (commonly 1.5-hr damper for assemblies up to 3-hr) | Fusible link, 165°F standard (212°F for kitchen/high-ambient exhaust) |
| Smoke barrier only | Smoke damper | UL 555S, leakage class rated (I/II/III) | Electric or pneumatic actuator, tied to smoke detection/fire alarm |
| Fire-rated wall that is also a smoke barrier | Combination fire/smoke damper | UL 555S (combination) | Fusible link plus actuator, both functions in one listed assembly |

**Rule:** never take "the duct is shown continuous on the mechanical set" as evidence a damper isn't needed — cross-check every duct routing line against the architectural life-safety plan's rated wall and floor lines independently, before fabrication. Confirm any claimed IBC 717 exception (e.g., single dwelling unit penetrations, specific small-opening allowances) with the code official in writing rather than assuming it applies.
