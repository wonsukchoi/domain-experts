# Occupational Health and Safety Technician — Field Playbook

## 1. Calibration drift decision table (air sampling pumps)

Formula: **Drift % = (Pre-cal flow − Post-cal flow) / Pre-cal flow × 100**

| Pre-cal (L/min) | Post-cal (L/min) | Drift | Action |
|---|---|---|---|
| 1.70 | 1.69 | 0.6% | Use average flow, no flag |
| 1.70 | 1.64 | 3.5% | Use average flow, no flag |
| 1.70 | 1.58 | 7.1% | Use average flow, **flag as reduced-confidence** |
| 1.70 | 1.61 | 5.3% | Use average flow, **flag as reduced-confidence** |
| 1.70 | 1.49 | 12.4% | **Void sample — redeploy** |

**Corrected sample volume** = average(pre, post flow) × sample duration (min). Never use pre-cal flow alone once a post-cal reading exists, even if it "looks fine" — the average is the correction, not an approximation of it.

## 2. Batch QC ratios (AIHA convention)

| Batch size (personal samples) | Minimum field blanks | Minimum duplicates |
|---|---|---|
| 1–9 | 1 | 0 (recommended for batches ≥5) |
| 10–19 | 2 | 1 |
| 20–29 | 3 | 2 |
| 30+ | ~10% of batch, rounded up | ~10% of batch, rounded up |

**Blank correction:** corrected sample mass = raw filter mass gain − average field blank mass. If a single blank reads more than 2× the average of the other blanks in the batch, exclude it as an outlier and document why, don't silently average it in.

## 3. Minimum detectable concentration (MDC)

Formula: **MDC = Analytical LOD (µg/filter) / Sample volume (m³)**

| Analyte | Method | LOD (µg/filter) | Sample volume | MDC |
|---|---|---|---|---|
| Respirable crystalline silica | NIOSH 7500 | 5 | 0.787 m³ | 6.4 µg/m³ |
| Lead | NIOSH 7300 (ICP) | 1 | 0.960 m³ | 1.0 µg/m³ |
| Toluene (charcoal tube) | NIOSH 1501 | 2 | 0.060 m³ | 33.3 µg/m³ |

**Reporting rule:** a lab result below MDC is reported as "< MDC value," never as "0" or "not detected" without the number — the floor of what the method could have seen matters to anyone reading the result later.

## 4. Quantitative fit test (QNFT) — pass criteria and margin table

Per OSHA 29 CFR 1910.134 Appendix A, minimum overall fit factor:

| Respirator class | Minimum fit factor | Example result | Margin | Call |
|---|---|---|---|---|
| Half-face (elastomeric or filtering facepiece) | 100 | 340 | 240% headroom | Clean pass |
| Half-face | 100 | 115 | 15% headroom | **Marginal — note and consider refit** |
| Full facepiece | 500 | 1,850 | 270% headroom | Clean pass |
| Full facepiece | 500 | 540 | 8% headroom | **Marginal — note and consider refit** |

Protocol: 4 exercises minimum per OSHA generic protocol (bending, talking, head side-to-side, head up-and-down), each timed, individual exercise fit factors recorded alongside the overall harmonic mean — a single low-exercise score inside an otherwise high overall average still gets noted, since it points at a specific seal weakness (usually jaw movement or bridge-of-nose gap).

**Qualitative fit test (QLFT)** — used only where QNFT equipment isn't required/available and the respirator class allows it (not permitted for negative-pressure respirators above certain APF classes). Saccharin/Bitrex threshold check, then pass/fail on whether the test subject detects the aerosol during all exercises — binary, no margin to report.

## 5. Noise dosimetry deployment checklist

1. Pre-cal dosimeter with acoustic calibrator (typically 114 dB @ 1000 Hz reference tone) — verify reading within ±0.5 dB before mounting.
2. Mount on shoulder/collar within 2 inches of the ear, criterion level 90 dBA, threshold 80 dBA, exchange rate 5 dB (OSHA methodology) unless the plan specifies ACGIH parameters (85/80/3) for a non-compliance comparison.
3. Log shift start/end and dosimeter on/off times — target ≥70% shift coverage; below that, disclose the coverage gap and note whether missing time was assumed non-exposed (break room, PPE removed) or unaccounted for.
4. Post-cal at retrieval — same tolerance as pre-cal; if outside ±0.5 dB, flag and consider void depending on magnitude of drift.
5. Dose (%) converts to TWA via: **TWA = 16.61 × log10(Dose/100) + 90**. Example: Dose 118% → TWA = 16.61 × log10(1.18) + 90 = 16.61 × 0.0719 + 90 = **91.2 dBA** — over the 90 dBA PEL.

## 6. Chain-of-custody template (filled example)

```
CHAIN OF CUSTODY — Air Sample Media
Sample ID: SIL-0447          Method: NIOSH 7500
Collected by: [tech name/ID]  Date: [date]  Location: Concrete Cutting, Bay 3
Media: 10-mm nylon cyclone + 5-µm PVC filter, lot #CY-2291
Pre-cal flow: 1.70 L/min (Gilibrator, cal cert #GB-0819, exp [date])
Post-cal flow: 1.58 L/min

Custody transfer log:
  1. [tech name] → sealed media, [time/date], field
  2. [tech name] → shipping courier, [time/date], signature on file
  3. [lab intake tech] → received intact/sealed, [time/date], signature on file

Seal status at lab intake: intact / broken (circle one) — if broken, void
pending investigation before analysis proceeds.
```

A gap in any numbered step above — no signature, no timestamp, an unsealed cassette accepted without note — is grounds for an opposing expert to exclude the result; complete the form in the field, not from memory later.
