# Astronomer — Playbook

## SNR / exposure-time worksheet

Filled example for two targets on the same 1.0-m instrument (ZP_V = 25.5, read noise 8 e⁻/pixel, sky = 21.5 mag/arcsec² at 0.4"/pixel, 3" aperture ≈ 177 pixels, negligible dark current):

| Quantity | Target A (V=17.5, bright) | Target B (V=23.0, faint) |
|---|---|---|
| Source rate (e⁻/s) | 10^(0.4·(25.5−17.5)) = 1,584.9 | 10^(0.4·(25.5−23.0)) = 10.0 |
| Sky rate, total aperture (e⁻/s) | 1,127.5 | 1,127.5 |
| Read-noise term (e⁻², fixed) | 11,328 | 11,328 |
| Dominant noise term | Source (1,584.9 ≫ 1,127.5) | Sky (1,127.5 ≫ 10.0) |
| Time for SNR=10 | ≈ 0.10 s (read-noise-limited at this SNR; use ≥ several seconds in practice to avoid saturation/readout-overhead dominating) | ≈ 1,149 s (19.2 min) |
| Time for SNR=30 | ≈ 0.9 s (as above, floor is practical minimum exposure, not this formula) | ≈ 10,340 s (2.87 hr) — note SNR=30 costs ~9x the SNR=10 time, consistent with √t scaling |

Reading the table: Target A is source-photon-limited even at short exposures, so the useful lower bound on exposure time is set by practical minimums (readout time, guiding settle), not the noise equation. Target B is sky-background-limited, so the noise equation is the binding constraint and √t scaling applies cleanly — this is the target type where the exposure-time miscalculation shown in the SKILL.md worked example actually bites.

## Error-budget table (precision time-series photometry)

Filled example for a transit-depth measurement targeting ~0.5% precision:

| Error source | Type | Estimated size | Mitigation |
|---|---|---|---|
| Photon (shot) noise, target | Statistical | 0.18% per 5-min bin | Bin more data — averages down as 1/√N |
| Sky background photon noise | Statistical | 0.05% per 5-min bin | Same — averages down |
| Flat-field residual | Systematic | 0.15%, fixed | Dither pointing across nights, re-derive flat from science frames if needed |
| Differential extinction (color-dependent) | Systematic | 0.10%, fixed per night | Use a reference star of similar color; model airmass trend and detrend |
| Detector nonlinearity near full well | Systematic | 0.20% if uncorrected | Stay below ~70% full well; apply linearity correction if not |
| **Combined statistical (added in quadrature, N=50 bins)** | — | 0.19%/√50 ≈ 0.027% | — |
| **Combined systematic (does not average down)** | — | √(0.15² + 0.10² + 0.20²) ≈ 0.27% | — |

Total reported uncertainty ≈ √(0.027² + 0.27²) ≈ 0.27% — systematic-dominated. Adding more nights of data narrows the statistical term further but barely moves the total, which is the concrete case for budgeting systematics explicitly rather than reporting photon-noise error alone once the systematic floor is comparable to or larger than the statistical term.

## Data-reduction QC checklist

1. **Bias/dark subtraction**: confirm master bias/dark frame count matches expected read-noise level within ~5%; a mismatch flags a detector setting change mid-run.
2. **Flat-field correction**: check flat-fielded science frame for residual large-scale gradient (>2% peak-to-peak across the frame) — indicates an inadequate flat or twilight-sky contamination in the flat itself.
3. **Wavelength calibration (spectroscopy)**: fit residuals between the wavelength solution and known arc-lamp/sky-emission lines; flag if RMS residual exceeds ~0.1 pixel (or the instrument's documented stability spec).
4. **Photometric zero-point solve**: fit standard-star instrumental-vs-catalog magnitudes; flag if the fit residual RMS exceeds ~0.02 mag, which usually indicates a non-photometric (thin-cloud) night.
5. **Cosmic-ray rejection**: median-combine sub-exposures or run an L.A.Cosmic-type algorithm; visually spot-check the combined frame against one raw sub-exposure for residual cosmic-ray trails.
6. **Aperture/background check**: for crowded fields, overlay the photometric aperture and background annulus on a deep reference image to confirm neither is contaminated by a neighboring source.
7. **Non-detection handling**: for any target below threshold, compute and record the 3σ flux upper limit from the local background RMS at the source position — do not leave the row blank.
