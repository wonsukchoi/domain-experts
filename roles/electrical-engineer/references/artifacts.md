# Filled artifacts

Real structures with plausible numbers — populate directly, don't restate as description.

## NEC Article 220 demand-load worksheet (commercial office, 40,000 sq ft)

| Load category | Connected VA | NEC demand factor | Demand VA |
|---|---|---|---|
| General lighting (3.5 VA/sq ft × 40,000) | 140,000 | first 3,000 @ 100%, remainder @ 35% (Table 220.42, other-than-dwelling) | 3,000 + (137,000 × 0.35) = 3,000 + 47,950 = **50,950** |
| Receptacle load (1 VA/sq ft, general office) | 40,000 | first 10,000 @ 100%, remainder @ 50% (Table 220.44 note) | 10,000 + (30,000 × 0.50) = **25,000** |
| HVAC (largest motor at 125%, others at 100%) | 85,000 | non-coincident with heating; largest unit 25,000 VA taken at 125% | 25,000 × 1.25 + 60,000 = 31,250 + 60,000 = **91,250** |
| Kitchen equipment (Table 220.56, 6 units) | 60,000 | 65% demand factor at 6 units | 60,000 × 0.65 = **39,000** |
| **Total demand load** | 325,000 | — | **206,200 VA** |

**Service size check:** 206,200 VA / (1.732 × 480) = **248.2 A** at 480Y/277V, 3-phase → select a 400A service (next standard size with margin for future load), not a 250A service sized to the connected-load sum's naive 391 A.

## Short-circuit / arc-flash study excerpt (multi-bus)

| Bus | Source | Bolted Isc (100%) | Governing arcing-current scenario | Incident energy | PPE category |
|---|---|---|---|---|---|
| MSB (utility side) | Utility, 191 MVA avail. | 22,950 A | 100% (device is instantaneous across full range) | 3.1 cal/cm² | 1 |
| T-1 secondary (500 kVA, 5% Z) | MSB | 11,431 A | 15% (1,715 A) — below CB-12's 3,000A pickup | 14.8 cal/cm² | 3 |
| Panel P-7 (fed from P-4, 100 ft #4/0 feeder) | Panel P-4 | 8,220 A | 100% (fuse, no instantaneous delay band) | 2.4 cal/cm² | 1 |
| MCC-2 (motor control center) | T-1 secondary | 10,890 A | 85% (9,257 A) — closest to CB coordination gap | 6.7 cal/cm² | 2 |

**Coordination check (CB-12 upstream of MCC-2 feeder breaker CB-2A):** at MCC-2's maximum through-fault current of 10,890 A, CB-2A's TCC clears in 0.06 s; CB-12's TCC does not begin its instantaneous band until 0.15 s at that same current — **0.09 s of margin**, adequate separation (target ≥0.1 s at 480V board-to-board; borderline here, flag for review before final release).

## Arc-flash label content (per panel, posted at equipment)

```
WARNING — ARC FLASH AND SHOCK HAZARD
Appropriate PPE Required
Panel: P-4 (T-1 secondary)
Incident Energy: 14.8 cal/cm² (governing case: 15% arcing current)
PPE Category: 3
Arc Flash Boundary: 6.2 ft
Working Distance: 18 in
Shock Hazard: 480V — Limited Approach 3 ft 6 in, Restricted Approach 1 ft
Equipment Label Date: study current as of [date]; revalidate on any upstream change
```

## Power-factor correction sizing

Facility billed load: 300 kW at existing PF = 0.82 (θ1 = 34.9°, tanθ1 = 0.698). Utility penalty threshold: PF < 0.90. Target PF = 0.95 (θ2 = 18.2°, tanθ2 = 0.329).

kVAR required = kW × (tanθ1 − tanθ2) = 300 × (0.698 − 0.329) = 300 × 0.369 = **110.7 kVAR**.

Select standard capacitor bank: 3 × 40 kVAR steps = 120 kVAR installed → resulting PF = corrected via tanθ_new = tanθ1 − (kVAR_installed / kW) = 0.698 − (120/300) = 0.698 − 0.400 = 0.298 → PF = cos(atan(0.298)) = **0.958**, above target with one step held in reserve for load growth.
