# Playbook

## Casting shrinkage calculation (filled example)

Molar crown coping, base metal alloy, die margin dimension 8.000mm, alloy shrinkage rate 1.5%.

| Step | Value |
|---|---|
| Die margin dimension (target after casting) | 8.000mm |
| Alloy shrinkage rate | 1.5% |
| Wax pattern dimension | 8.000 × 1.015 = 8.120mm |
| Result if wax built to naive 8.000mm dimension | 8.000 / 1.015 ≈ 7.882mm — undersized ~0.118mm (118 microns) |
| Commonly cited clinically acceptable margin gap threshold | ~50–120 microns (outer limit) |

**Result:** The naive approach's 118-micron undersizing sits right at or beyond the outer edge of commonly cited acceptable marginal gap thresholds — and that's before accounting for any additional fit tolerance elsewhere in the restoration.

**Comparison across alloy classes (same 8.000mm die dimension):**

| Alloy class | Typical shrinkage rate | Wax pattern dimension |
|---|---|---|
| Base metal (Ni-Cr, Co-Cr) | 1.5% | 8.000 × 1.015 = 8.120mm |
| High-noble (gold-based) | 1.3% | 8.000 × 1.013 = 8.104mm |
| Zirconia (milled, sintering shrinkage) | ~20–25% (sintering, not casting) | Design file scaled 8.000 × 1.20–1.25 = 9.600–10.000mm pre-sinter |

Note: zirconia's shrinkage figure reflects sintering shrinkage (a much larger percentage) rather than metal casting shrinkage — a fundamentally different process requiring its own compensation data, not the metal-alloy figures above.

## Margin-fit tolerance check (filled example)

| Restoration | Measured margin gap (under magnification) | Acceptable threshold | Status |
|---|---|---|---|
| Tooth #14, distal margin | 45 microns | ≤ 50–120 microns | Within tolerance |
| Tooth #19, mesial margin | 150 microns | ≤ 50–120 microns | **Out of tolerance — reject, recast or re-fit** |
| Tooth #30, buccal margin | 80 microns | ≤ 50–120 microns | Within tolerance |

Tooth #19's 150-micron gap exceeds even the outer edge of the commonly cited acceptable range — flag for recasting rather than accepting on the basis that the rest of the restoration looks well-made.

## Value-priority shade matching worksheet (filled example)

Target shade: A2 (per shade guide). Fabricated restoration measured with spectrophotometer:

| Parameter | Target (A2) | Measured (restoration) | Match assessment |
|---|---|---|---|
| Value (lightness) | Medium-light | Noticeably darker | **Mismatch — most visually significant** |
| Hue | Yellow-based | Yellow-based | Match |
| Chroma (saturation) | Moderate | Moderate | Match |

**Correction priority:** Even though hue and chroma both match the target, the value mismatch is the one a patient or observer will notice first from a distance — correct the value (lightness) before making any further hue/chroma adjustments.
