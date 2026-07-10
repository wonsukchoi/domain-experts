# Processing Playbook

Operational sequences with concrete steps and thresholds. Defaults, not laws — deviate consciously and say why in the product metadata.

## 1. Sensor selection matrix

Match the phenomenon's characteristic timescale and required minimum mapping unit against sensor tradeoffs before acquiring anything.

| Sensor | Spatial res. | Revisit | Bands | Best fit | Weak fit |
|---|---|---|---|---|---|
| Landsat 8/9 (OLI/TIRS) | 30 m (15 m pan) | 16 days (8 days combined) | 11, incl. thermal | Multi-decade land-cover change, thermal | Fast-moving events, persistent cloud regions |
| Sentinel-2 (MSI) | 10–20 m | ~5 days (2-satellite) | 13, red-edge bands | Agriculture, vegetation stress, near-term change | Thermal-dependent work (no TIR) |
| MODIS/VIIRS | 250 m–1 km | Daily | 36 (MODIS) | Continental-scale monitoring, fire/burn detection, daily NDVI time series | Parcel-level or sub-hectare change |
| Planet (Dove/SkySat) | 3–5 m (Dove), 0.5 m (SkySat) | Daily (Dove) | 4–8 | Rapid-change tropical monitoring under persistent cloud | Multi-decade archives (short mission history), spectral analysis needing narrow bands |
| SAR (Sentinel-1) | 10 m | 6–12 days | C-band | Cloud-penetrating change detection, flood mapping, subsidence | Vegetation species discrimination, requires speckle filtering |

**Decision rule:** compute the phenomenon's minimum detectable interval (e.g., a fire scar that regrows spectral signal within 30 days needs a revisit shorter than 30 days with margin for cloud loss). Cross-check against the study area's historical cloud-cover frequency (pull from Sentinel-2/Landsat archive metadata) — a nominal 5-day revisit in a region with 60% average cloud cover behaves like a 12+ day effective revisit.

## 2. Correction chain, in order — each step is a prerequisite for the next

1. **Radiometric calibration** — DN → at-sensor radiance using the sensor's published gain/bias or rescale coefficients (Chander, Markham & Helder 2009 for legacy Landsat; current-mission metadata files for OLI/MSI). Skipping this step means any later index or classification is calibrated to sensor drift, not ground reflectance.
2. **Atmospheric correction** — radiance → surface reflectance. Dark Object Subtraction (DOS) is an acceptable quick correction for single-scene qualitative work; 6S, LaSRC/Fmask (Landsat Collection 2), or Sen2Cor (Sentinel-2) are required for any multi-date or multi-sensor comparison. Record the correction method and version in product metadata — different atmospheric correction algorithms produce measurably different reflectance values for the same scene.
3. **Cloud/shadow/cirrus masking** — apply Fmask (Landsat) or Sen2Cor's scene classification layer (Sentinel-2) before any pixel is used downstream. **Threshold: discard scenes with >20% cloud cover over the study area for change detection work** unless the study area is small enough to hand-verify the clear fraction.
4. **Geometric correction / orthorectification** — rectify against a DEM (SRTM 30 m minimum, higher resolution if terrain relief exceeds ~100 m within a scene) and ground control points. **Threshold: RMSE < 0.5 pixel** for any product feeding change detection; document the RMSE achieved, not just "orthorectified."
5. **Co-registration** — for multi-date comparison, register the later date to the earlier (or both to a common reference) using tie points in stable, unchanged features (roads, building corners) — never tie points inside the area expected to change. Re-verify RMSE < 0.5 pixel after co-registration, separately from the orthorectification RMSE.
6. **BRDF/illumination normalization** — required when comparing index values across dates with meaningfully different sun-sensor geometry (different season, different off-nadir angle); a c-factor or MODIS-BRDF-based normalization brings index values onto a comparable footing before differencing.

## 3. Classification and change detection

- **Method escalation, cheapest first:** spectral index thresholding (NDVI/NBR/NDWI cutoff) → decision tree → random forest → deep learning (CNN/U-Net). Escalate only when the cheaper method fails to meet the accuracy requirement on a held-out validation set — a threshold rule that clears the bar ships faster and is auditable by a non-specialist.
- **Post-classification comparison vs. direct change detection:** post-classification comparison (classify each date independently, then compare) is more interpretable but propagates error multiplicatively — if each single-date classification is 90% accurate, agreement-based change accuracy can fall below 81%. Direct change detection (image differencing, change-vector analysis on the corrected reflectance) avoids compounding two classification errors but requires the two dates to be radiometrically consistent (steps 1–2 done correctly) or the "change" signal is partly atmospheric artifact.
- **Minimum mapping unit (MMU):** state it explicitly (e.g., "changes under 0.5 ha, or ~6 contiguous 30 m pixels, are not mapped") — an unstated MMU makes single-pixel noise indistinguishable from real small-patch change.

## 4. Accuracy assessment and error-adjusted area estimation

1. **Design the sample before classifying**, or at minimum before drawing reference data: stratify by mapped class, allocate at least 50 samples per stratum for classes of policy/decision interest (Congalton & Green 2019 recommends 50–100 per class as a practical minimum for a multi-class map with modest class-level precision needs).
2. **Reference data must be independent of training data** — different source imagery (higher spatial resolution, different date near the classification date), field visits, or an independently produced validated product. Never draw reference points from pixels adjacent to the training set; spatial autocorrelation inflates the accuracy estimate.
3. **Build the confusion matrix** (reference in rows, map in columns is the ASPRS/Congalton convention) and report per-class **user's accuracy** (row-based: of what was mapped as class X, how much is really X) and **producer's accuracy** (column-based: of what's really class X, how much got mapped as X) — never only overall accuracy.
4. **Compute the error-adjusted area estimate** (Olofsson et al. 2014):
   - Stratum weight: `W_i = N_i / N` (mapped pixel count in stratum i ÷ total pixels).
   - Estimated proportion of true area for target class k: `p̂_k = Σ_i W_i × (n_ik / n_i)` where `n_ik` is the count of reference-class-k samples within mapped-stratum i, `n_i` is the sample size in stratum i.
   - Standard error: `SE(p̂_k) = √[ Σ_i W_i² × (n_ik/n_i)(1 − n_ik/n_i) / (n_i − 1) ]`.
   - 95% CI: `p̂_k × total_area ± 1.96 × SE(p̂_k) × total_area`.
5. **Report both numbers, labeled**: the naive pixel-count area, and the error-adjusted area with its 95% CI. If only one number can be reported, it is the error-adjusted one.
6. **Kappa** as a secondary summary only — report it, but lead with per-class user's/producer's accuracy in any written readout.

## 5. Deliverable checklist

Every product ships with: sensor(s) and acquisition date(s), correction chain and software/version, cloud-cover fraction retained, geometric RMSE, classification method, confusion matrix with per-class accuracies, error-adjusted area with CI, and minimum mapping unit. A product missing any of these fields is not reproducible or auditable by the next analyst.
