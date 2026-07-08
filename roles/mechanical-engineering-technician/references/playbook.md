# Playbook — inspection, instrumentation, and verification worksheets

Filled worksheets, not templates to describe. Copy the row structure and substitute real numbers.

## 1. CMM true-position / MMC bonus worksheet

For a toleranced hole or pin feature with an MMC modifier, referenced to a stated datum reference frame (DRF).

**Header block (record these before any point is taken):**

| Field | Value |
|---|---|
| Drawing / rev | 7712-B, Rev C |
| Feature | Hole #1 of 4, bolt pattern |
| Datum reference frame | A\|B\|C (primary face, secondary edge, tertiary hole) |
| Fit method | Constrained (datum-simulated per print precedence) |
| CMM program / probe qual date | PROG-7712B-01 / probe qualified 2026-06-30 |

**Position calculation:**

| Item | Value |
|---|---|
| Nominal X, Y | 1.0000", 1.0000" |
| Measured X, Y | 1.0028", 1.0011" |
| dx, dy | 0.0028", 0.0011" |
| Position error = 2√(dx²+dy²) | 2√(0.0028² + 0.0011²) = 0.0060" |
| Feature size, nominal (MMC) | Ø0.2570" |
| Feature size, as-measured | Ø0.2585" |
| Bonus = as-measured − MMC | 0.0015" |
| Base position tolerance | Ø0.0100" |
| Allowable = base + bonus | 0.0115" |
| Result | 0.0060" < 0.0115" → **PASS**, margin 0.0055" |

**Rule for the modifier column:** MMC modifier present → add bonus as above. LMC modifier present → bonus is computed from the *opposite* direction (as-measured size approaching LMC grows the bonus the same way, but the base MMC/LMC size reference flips — recompute from the LMC value on the print, don't reuse the MMC formula). RFS or no modifier → allowable = base tolerance only, no bonus regardless of measured size.

**Fit-method note (mandatory in every report):** state constrained vs. best-fit explicitly. If the print has no DRF called out, the report must say "no DRF on print — best-fit alignment used" rather than silently picking one.

## 2. Strain-gauge bridge configuration and output worksheet

**Configuration selection table:**

| Config | Active gauges | Cancels temperature? | Cancels axial (in bending test)? | Sensitivity vs. quarter bridge | Output equation (Vout/Vex) |
|---|---|---|---|---|---|
| Quarter bridge | 1 | No | No | 1x | GF·ε / 4 |
| Half bridge, bending (2 opposite arms) | 2 | Yes | Yes | 2x | GF·ε / 2 |
| Half bridge, Poisson (2 adjacent arms) | 2 | Yes | No | 1 + ν (≈1.3x for ν=0.3) | (GF·ε(1+ν)) / 4 |
| Full bridge, bending (4 arms, 2 tension/2 compression) | 4 | Yes | Yes | 4x | GF·ε |
| Full bridge, axial (4 arms, all sensing axial + Poisson) | 4 | Yes | No (measures axial by design) | 2(1+ν)x | GF·ε(1+ν)/2 |

**Filled example — full bridge, bending configuration:**

| Item | Value |
|---|---|
| Gauge factor (GF) | 2.06 |
| Excitation voltage (Vex) | 10.000 V |
| Predicted moment (M = F·L) | 45 lbf × 4.0" = 180 in-lbf |
| Section modulus term (c/I) | 0.125" / 0.0013021 in⁴ = 95.99 in⁻³ |
| Predicted stress (σ = Mc/I) | 180 × 95.99 = 17,280 psi |
| Predicted strain (ε = σ/E) | 17,280 / 10.0×10⁶ = 1,728 µε |
| Predicted Vout/Vex (full bridge = GF·ε) | 2.06 × 0.001728 = 0.003559 |
| Predicted Vout | 0.003559 × 10.000 V = 35.59 mV |
| Measured Vout | 36.10 mV |
| Measured ε = (Vout/Vex)/GF | 0.003610 / 2.06 = 1,752 µε |
| Measured σ = E·ε | 10.0×10⁶ × 0.0017524 = 17,524 psi |
| Delta vs. predicted | (17,524 − 17,280)/17,280 = +1.4% |

**Rule for configuration choice:** default full bridge for any test where both bending and axial/thermal contamination are plausible; half-bridge bending only when gauge count or space forces it; quarter bridge only as a last resort, and flag the reading as uncorrected for axial/thermal cross-talk in the record.

## 3. Load cell / reference verification worksheet

| Item | Value |
|---|---|
| Load cell capacity / rated output | 100 lbf / 2.0000 mV/V |
| Reference standard | Calibrated dead-weight, 45.00 lbf, cert traceable, current |
| Expected output at reference load | (45/100) × 2.0000 = 0.9000 mV/V |
| Measured output | 0.8987 mV/V |
| Error | (0.9000 − 0.8987)/0.9000 = 0.14% |
| Class spec (example Class C) | ±0.25% |
| Result | Within spec → **verified for use at this load point** |
| Coverage note | Only verified up to 45.00 lbf — a test point above this load is unverified until a higher reference check is run, unless the manufacturer's documented linearity spec explicitly covers the extension |

## 4. Thermal data reduction — cold-junction compensation

| Item | Value |
|---|---|
| Thermocouple type | Type K |
| Measured junction voltage | 4.096 mV |
| DAQ cold-junction reference temperature | 23.4 °C (measured at terminal block) |
| Equivalent voltage of CJ temp (Type K table) | 0.936 mV |
| Corrected voltage (measured + CJ equivalent) | 4.096 + 0.936 = 5.032 mV |
| Corresponding temperature (Type K table, reverse lookup) | 122.3 °C |

**Rule:** always add the cold-junction reference's table-equivalent voltage before converting back to temperature — reading the raw thermocouple voltage against a 0°C reference table without the CJ correction understates temperature by the CJ reference's own equivalent, commonly 15-25°C at room-temperature terminal blocks.

## 5. First-article deviation log — entry format

| Field | Example |
|---|---|
| Item | Bracket mounting foot, left side |
| Observation | 0.015" gap under foot at assembly, not on print as a toleranced flatness callout |
| Toleranced? | No — flatness not called out on this face |
| Functional relevance | Foot doesn't seat before torquing; may pre-load bracket in service |
| Disposition routed to | Design engineer, next-rev flatness callout under evaluation |

**Rule:** log every real deviation this way, toleranced or not — an untoleranced observation that's functionally relevant still gets logged and routed, not dropped because it "passed" on paper.
