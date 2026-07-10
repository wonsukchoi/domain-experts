# Playbook

Filled checklists and worked procedures, not descriptions of them. Deviate consciously and document why.

## 1. UAS multispectral acquisition planning

For a 340-acre agricultural NDVI mapping job, deliverable spec: 5 cm GSD, ASPRS QL3-equivalent horizontal accuracy, five-band multispectral (blue/green/red/red-edge/NIR).

1. **Flight altitude from GSD.** Pinhole geometry: GSD = pixel_pitch × (altitude / focal_length), all in consistent length units. For a sensor with 5.5 µm (0.0055 mm) pixel pitch and 8 mm focal length, solving for a 5 cm (50 mm) GSD gives altitude = GSD × focal_length / pixel_pitch = 50 × 8 / 0.0055 ≈ 72,727 mm ≈ **73 m AGL**. Round down to 70 m to leave margin, and confirm it clears the FAA Part 107 400 ft (122 m) AGL ceiling for the class of airspace — this mission has plenty of headroom.
2. **Overlap.** 75% front / 65% side overlap minimum for structure-from-motion tie-point density on low-texture crop canopy — bare soil and uniform canopy need more overlap than urban/structured scenes, not less.
3. **GCP layout.** Minimum 5 GCPs for a block this size, plus 5 independent checkpoints not used in the bundle adjustment — checkpoints used as GCPs don't test anything, they just get absorbed into the solution. Distribute across the block, not clustered near the launch point.
4. **Radiometric calibration.** Fly over (or place in-frame at start/end) a calibrated reflectance panel with known spectral values per band; capture panel images in the same lighting as the mission, not a different time of day.
5. **Pre-flight calibration currency check.** Confirm the sensor's dark-current/vignetting calibration file is within its stated validity window (typically 6–12 months per manufacturer spec); if expired, run a fresh lab or field radiometric calibration before flying, not after processing shows a spectral anomaly.
6. **Weather window.** Wind <15 kt sustained, no precipitation, solar elevation angle >30° to limit shadow length and BRDF effects on reflectance — log actual conditions at flight time in the mission metadata.

## 2. Correction chain — QA gate at every stage

Each stage has its own pass/fail metric checked before the output feeds the next stage.

| Stage | QA metric | Threshold (spec-dependent example) | If it fails |
|---|---|---|---|
| Radiometric calibration | Panel-derived reflectance vs. known panel values, per band | Within ±5% reflectance | Recheck exposure settings / re-fly panel captures; don't proceed to geometric correction on uncalibrated radiance |
| Geometric correction / bundle adjustment | Mean reprojection error (SfM) or boresight residual (airborne) | <1 px reprojection error; boresight residual <0.02° | Re-run bundle adjustment with tie-point cleanup; check GCP coordinate entry for transposed digits before blaming the sensor |
| Orthorectification | GCP residuals (checkpoints excluded) | Consistent with target horizontal accuracy class (e.g., RMSEx/y ≤ 1.4 × QL3 GSD) | Check DEM/DSM source used for rectification — a coarse or stale elevation surface under high-relief terrain is the most common cause |
| Mosaicking / seamlining | Visible seamline artifact count, band-to-band offset at seams | No visible seam on a false-color composite at full resolution | Adjust seamline placement away from high-contrast edges; re-check color balancing didn't use a cloud-contaminated tile as reference |
| Point-cloud classification (LiDAR) | Ground-point density, checkpoint RMSEz per land-cover class | Meets QL vertical spec per class (see §3) | Reprocess with adjusted ground-filter parameters for the affected tile only — don't reprocess the whole block for a localized defect |

## 3. LiDAR checkpoint accuracy computation (full worked procedure)

Given *n* independent vertical checkpoints with residuals *e_i* (LiDAR-derived elevation minus surveyed elevation):

1. **Separate by land cover** — non-vegetated (bare earth, low grass, urban) vs. vegetated (dense grass, brush, forest canopy gaps). Different formulas apply; do not pool them into one number.
2. **Non-vegetated: RMSEz = √( Σe_i² / n )**, then **Accuracy_z (95% CI) = RMSEz × 1.9600** (assumes normally distributed errors — verify with a normal-probability plot on n ≥ 20 points before trusting the multiplier).
3. **Vegetated: Accuracy_z (95%) = 95th percentile of |e_i|** across vegetated checkpoints (minimum 5 per ASPRS 2014 guidance) — do not apply the RMSE × 1.9600 formula here; vegetated LiDAR errors are typically right-skewed (canopy penetration bias), not normal.
4. **Investigate before excluding.** Any residual beyond 3× the running RMSE is a defect-investigation trigger, not an automatic exclusion. Pull the classified point cloud at that location; check for ground/vegetation misclassification, a checkpoint survey error (independently verify the checkpoint's own closure), or a genuine terrain feature (retaining wall, culvert) the DEM legitimately can't represent at this resolution.
5. **Document every exclusion** with its specific cause in the delivery metadata. An accuracy report with checkpoints removed and no stated cause fails standards review even if the resulting number looks good.

## 4. Sensor calibration currency decision

- **Within validity window and last mission's checkpoint accuracy passed with margin (>20% below threshold):** fly as scheduled, no recalibration needed.
- **Within validity window but last mission's accuracy passed with <10% margin:** recalibrate before this mission — drift is eating the margin even though the file hasn't technically expired.
- **Past validity window, any margin:** recalibrate before flying, full stop — flying past-window and hoping QC catches it wastes the flight if it fails.
- **Mid-mission sensor event (hard landing, lens fogging, temperature excursion beyond spec):** ground the sensor, do not resume acquisition on the same calibration file even if still within its window — physical events invalidate a time-based calibration window immediately.
