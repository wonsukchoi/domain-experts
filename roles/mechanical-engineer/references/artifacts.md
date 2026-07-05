# Mechanical engineering artifacts — templates with real structure

Filled examples for the 4140 steel clevis bracket (B-104) referenced in `SKILL.md`'s worked example. Numbers are illustrative and internally consistent with that example; treat material properties, Marin factors, and FS targets as application-specific inputs to re-derive, not fixed values.

## 1. Stress report — calc package skeleton

**Header block:** part number/revision, load case description, material and heat-treat condition, engineer of record, date, FEA solver and mesh version if applicable.

**Section A — Load and geometry inputs**

| Parameter | Value |
|---|---|
| Load type | Pulsating axial tension, R = 0 (0 to Pmax) |
| Pmax | 9,000 lbf |
| Duty cycle | ~1,800 cycles/day |
| Design life | 10 years → ~6.6 × 10⁶ cycles (high-cycle fatigue regime) |
| Section (reduced) | w = 1.5 in, t = 0.375 in |
| Fillet radius (as-designed) | 0.125 in |
| Material | 4140 steel, Sy = 60,000 psi, Su = 95,000 psi |

**Section B — Nominal and notch-corrected stress**

| Quantity | Formula | Value |
|---|---|---|
| σ_nom,max | P / (w × t) | 9,000 / 0.5625 = 16,000 psi |
| σ_nom,alt, σ_nom,mean (R=0) | σ_nom,max / 2 | 8,000 psi each |
| D/d, r/d | 2.5/1.5, 0.125/1.5 | 1.67, 0.083 |
| Kt (Peterson, stepped flat bar, tension) | chart lookup | 2.1 |
| Actual peak stress | Kt × σ_nom,max | 33,600 psi |
| FS on yield (actual peak) | Sy / peak | 60,000 / 33,600 = 1.79 |

**Section C — Fatigue check**

| Quantity | Formula | Value |
|---|---|---|
| Notch sensitivity q | chart, material + radius | 0.80 |
| Kf | 1 + q(Kt − 1) | 1 + 0.80(1.1) = 1.88 |
| σ_a, σ_m (notch-corrected) | Kf × σ_nom,alt / mean | 15,040 psi each |
| Se′ (rotating-beam baseline) | 0.5 × Su | 47,500 psi |
| ka (surface, machined) | Marin chart | 0.75 |
| kb (size) | Marin chart | 0.85 |
| kc (load type, axial) | Marin chart | 0.85 |
| Se (part-corrected) | ka × kb × kc × Se′ | 25,740 psi |
| Goodman sum | σ_a/Se + σ_m/Su | 0.584 + 0.158 = 0.742 |
| **FS_fatigue** | 1 / Goodman sum | **1.35** — below 2.5 target, flag for redesign |

**Section D — Conclusion (as-designed, flagged)**

> "Bracket B-104 as designed (0.125 in fillet) clears static yield (FS = 1.79 on actual notch-corrected peak stress) but does not clear the fatigue target for this cyclic, undetected-failure-mode application (FS_fatigue = 1.35 vs. 2.5 target). Recommend fillet radius increase per Section E before release."

**Section E — Redesign iteration**

| Quantity | As-designed | Redesigned |
|---|---|---|
| Fillet radius | 0.125 in | 0.3125 in |
| Surface finish | Machined | Ground |
| Kt | 2.1 | 1.6 |
| q | 0.80 | 0.83 |
| Kf | 1.88 | 1.50 |
| ka | 0.75 | 0.90 |
| Se | 25,740 psi | 30,890 psi |
| σ_a = σ_m | 15,040 psi | 12,000 psi |
| Goodman sum | 0.742 | 0.515 |
| FS_fatigue | 1.35 | **1.94** |

> "Increasing the fillet radius from 0.125 in to 0.3125 in and specifying a ground finish at the fillet raises FS_fatigue from 1.35 to 1.94, meeting the 2.0–2.5 target for this load case with no change to the static FEA result (FS = 3.57 on nominal-mesh yield, unaffected). No change to part width, thickness, or material. Estimated cost impact: none — radius change uses the same tooling; ground finish adds a single secondary operation at this feature only."

## 2. DFM review memo

**Header:** part number/revision, target process (3-axis CNC milling), reviewer, date.

| Finding | Location | Issue | Recommended fix | Cost/schedule impact if not fixed |
|---|---|---|---|---|
| Internal corner radius 0.020 in | Pocket P-3, base plate | Smallest standard end mill for this depth/diameter ratio is 0.0625 in; as-drawn radius requires EDM | Increase corner radius to 0.0625 in minimum, or accept EDM | EDM adds ~$40/part and 2 days lead time at this volume (500 units/mo) |
| Tolerance ±0.0015 in | Bore Ø0.750, non-mating | No functional requirement drives this tolerance; nearest mating part has 0.010 in clearance | Relax to ±0.005 in (standard reaming tolerance) | Forces 100% CMM inspection; est. $6/part in inspection labor for no functional gain |
| Blind tapped hole, depth 1.25 in in a 0.375 in thread | 4x M6 bosses | Thread depth exceeds 2x diameter without a specified tap-drill relief; tap breakage risk in production | Reduce to 1.5x diameter (0.5 in) or add relief groove | Tap breakage scrap rate historically ~4% at this depth per supplier data |
| Undercut feature behind a through-hole | Bracket arm, Rev B | Requires a form tool or 5-axis setup; part was designed 3-axis machinable in Rev A | Redesign the undercut as a two-piece bolted joint, or confirm 5-axis capacity/cost with supplier before release | 5-axis setup adds ~$180 NRE and $12/part vs. 3-axis baseline |

**Memo conclusion:**

> "Three of four findings are zero-cost fixes (radius, tolerance, thread depth) if corrected before release; the undercut finding changes the fabrication process and should be resolved with the supplier before quoting, not after. Recommend holding release pending the undercut decision."

## 3. Tolerance stack-up sheet — worst-case and RSS

**Assembly:** shaft-and-bearing-bore alignment, 4-part stack (housing bore location, bearing OD tolerance, bearing bore-to-OD concentricity, shaft OD).

| Component | Dimension | Tolerance (±) |
|---|---|---|
| Housing bore location | 2.000 in | 0.003 in |
| Bearing OD fit | 1.000 in | 0.0005 in |
| Bearing bore concentricity | — | 0.0008 in |
| Shaft OD | 0.998 in | 0.0004 in |

**Worst-case stack** (sum of absolute tolerances): 0.003 + 0.0005 + 0.0008 + 0.0004 = **±0.0047 in** total possible misalignment.

**RSS stack** (statistical, assumes independent normal distributions): √(0.003² + 0.0005² + 0.0008² + 0.0004²) = √(0.000009 + 0.00000025 + 0.00000064 + 0.00000016) = √0.00001005 = **±0.00317 in**.

**Rule applied:** this is a bearing alignment dimension where misalignment drives bearing life directly (safety/function-critical, only 4 parts in the stack) — use the worst-case number (±0.0047 in) for the design clearance check, not the RSS number, even though RSS is 33% tighter. RSS is reserved for stacks of 6+ independently toleranced, high-volume parts where the worst-case number would force uneconomical tolerances with no real functional benefit.
