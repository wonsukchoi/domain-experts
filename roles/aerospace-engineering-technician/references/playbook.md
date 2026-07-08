# Playbook

Filled worksheets for the four calculations this role runs most often: torque-to-preload, strain-gauge rosette reduction, wind-tunnel test-point data reduction, and NDI method selection.

## Torque-to-preload derivation (T = K·D·F)

Given a drawing torque callout, back-calculate delivered preload and check it against the joint analysis's minimum.

| Input | Value |
|---|---|
| Fastener | 1/4-28 UNJF steel bolt (D = 0.250 in) |
| Drawing torque callout | 80-95 in-lb |
| Finish | Zinc-nickel plated, dry |
| K-factor (dry, zinc-nickel) | 0.19 |
| Joint analysis minimum preload | 1,650 lbf |

Calculation, at torque midpoint T = 87.5 in-lb:

```
F = T / (K·D) = 87.5 / (0.19 × 0.250) = 87.5 / 0.0475 = 1,842 lbf
Margin = (1,842 − 1,650) / 1,650 = +11.6%
```

**K-factor reference table** (dry unless noted — verify against the fastener's actual finish spec before use):

| Finish / condition | K (dry) | K (lubricated) |
|---|---|---|
| Plain / uncoated steel | 0.20-0.30 | 0.12-0.18 |
| Cadmium plate | 0.20-0.24 | 0.13-0.18 |
| Zinc-nickel plate | 0.17-0.21 | 0.11-0.15 |
| Stainless, uncoated | 0.30-0.40 | 0.18-0.24 |
| MoS2-based anti-seize | — | 0.10-0.14 |

If the work order specifies a lubricant not in this table, use the lubricant manufacturer's published K-factor, not a default from this list — the table is a fallback when no lubricant-specific data exists.

## Strain-gauge rosette reduction (0°/45°/90°)

Uniaxial gauges only recover strain along the bonded axis. A rectangular rosette recovers the full in-plane strain state and principal stresses.

**Measured strains** (rosette at a lug fitting radius, gauges at 0°, 45°, 90° to a reference axis):

```
ε0  = 1,180 µε
ε45 =   640 µε
ε90 =  -210 µε
```

**Principal strains:**

```
εavg = (ε0 + ε90) / 2 = (1,180 + (-210)) / 2 = 485 µε

R = sqrt[ ((ε0 − ε90)/2)^2 + (2·ε45 − ε0 − ε90)^2 ] / 2
  = sqrt[ ((1,180 − (−210))/2)^2 + (2×640 − 1,180 − (−210))^2 ] / 2
  = sqrt[ (695)^2 + (310)^2 ] / 2
  = sqrt[ 483,025 + 96,100 ] / 2
  = sqrt[579,125] / 2 = 760.9 / 2 = 380.5 µε

ε1 = εavg + R = 485 + 380.5 = 865.5 µε
ε2 = εavg − R = 485 − 380.5 = 104.5 µε
```

**Principal stresses** (7075-T6 aluminum, E = 10.3×10^6 psi, ν = 0.33, plane stress):

```
σ1 = E/(1−ν²) × (ε1 + ν·ε2) = (10.3e6 / 0.8911) × (865.5e-6 + 0.33×104.5e-6)
   = 11.559e6 × (865.5e-6 + 34.5e-6) = 11.559e6 × 900.0e-6 = 10,403 psi

σ2 = E/(1−ν²) × (ε2 + ν·ε1) = 11.559e6 × (104.5e-6 + 0.33×865.5e-6)
   = 11.559e6 × (104.5e-6 + 285.6e-6) = 11.559e6 × 390.1e-6 = 4,509 psi
```

Compare σ1 against the fitting's predicted principal stress and against Fty (73,000 psi for 7075-T6) or the applicable allowable — a single uniaxial gauge bonded at 0° alone would have reported 1,180 µε → σ = E·ε = 12,154 psi *uncorrected for the biaxial state*, overstating the actual principal stress by roughly 17% relative to the rosette-derived 10,403 psi.

## Wind-tunnel test-point data reduction

Given tunnel conditions, compute dynamic pressure and Reynolds number for a test point, then non-dimensionalize a measured force.

| Input | Value |
|---|---|
| Air density, ρ | 0.002283 slug/ft³ (test-section condition) |
| Freestream velocity, V | 220 ft/s |
| Reference chord, c | 1.5 ft |
| Dynamic viscosity, μ | 3.62×10^-7 lbf·s/ft² |
| Measured lift force, L | 48.6 lbf |
| Reference wing area, S | 6.0 ft² |

```
Dynamic pressure: q = 0.5 × ρ × V² = 0.5 × 0.002283 × 220² = 0.5 × 0.002283 × 48,400 = 55.25 lbf/ft²

Reynolds number: Re = ρ·V·c / μ = (0.002283 × 220 × 1.5) / 3.62e-7
                    = 0.7534 / 3.62e-7 = 2.081×10^6

Lift coefficient: CL = L / (q × S) = 48.6 / (55.25 × 6.0) = 48.6 / 331.5 = 0.1466
```

Report CL against the predicted polar at the matched Re — a CL comparison at a mismatched Reynolds number (e.g., test Re = 2.08×10^6 vs. a flight-condition prediction at Re = 12×10^6) needs a stated caveat that boundary-layer transition behavior may differ, not a direct pass/fail read.

## NDI method-selection matrix

| Defect type | Location | Material | Method | Governing standard |
|---|---|---|---|---|
| Surface crack | Surface, accessible | Non-porous metal (Al, steel, Ti) | Liquid (dye) penetrant | ASTM E1417 |
| Surface/near-surface crack | Surface, ≤0.05 in deep | Conductive metal, coated or uncoated | Eddy current | ASTM E1004 / AMS 2630 |
| Subsurface flaw, delamination | Internal | Metal, composite laminate | Ultrasonic (pulse-echo or through-transmission) | ASTM E114 / ASTM E2533 (composites) |
| Porosity, inclusion (casting) | Internal | Cast metal | Radiographic (X-ray) | ASTM E1742 |
| Surface crack | Surface, ferromagnetic only | Steel, iron | Magnetic particle | ASTM E1444 |

Selection rule: read the drawing or process spec's called-out method first; only substitute when the print allows "or equivalent" *and* the substitute is verified sensitive to the specific defect type/size the original method would have caught, documented in the inspection record.
