# Vocabulary

Terms of art generalists misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

### GSD (Ground Sample Distance)

The real-world size of one pixel on the ground, determined by sensor pixel pitch, focal length, and flight altitude.
**In use:** "We need 5 cm GSD for this NDVI job — that means 85 m AGL with this sensor's optics, not the 120 m we flew last time for the 10 cm job."
**Common misuse:** treating GSD and "resolution" as interchangeable with image sharpness. A sensor can deliver a small GSD number and still produce a blurry product if motion blur, focus, or atmospheric haze degrades it — GSD is a geometric spec, not a quality guarantee.

### Orthorectification

Geometric correction that removes both sensor-perspective distortion and terrain-relief displacement, so every pixel sits at its correct map position regardless of terrain height.
**In use:** "The block orthorectified clean on the flat half but the checkpoint residuals blow out over the ridge — check what DEM we rectified against."
**Common misuse:** confusing orthorectification with simple georeferencing (assigning coordinates without terrain correction). Georeferencing alone leaves relief displacement uncorrected — buildings and terrain lean outward from the image center — which is invisible on flat terrain and a serious accuracy defect on relief.

### RMSEz / RMSEx / RMSEy

Root-mean-square error of a set of checkpoint residuals in the vertical (z), easting (x), or northing (y) direction — the basis for ASPRS/NSSDA accuracy statements.
**In use:** "RMSEz came out at 5.5 cm on the non-vegetated checkpoints, so Accuracy_z at 95% confidence is 10.8 cm — inside the QL2 spec."
**Common misuse:** reporting RMSE itself as "the accuracy," or quoting it to the client without applying the confidence-level multiplier (1.9600 for normal vertical error, 1.7308 for radial horizontal error) — RMSE is an intermediate statistic, not the accuracy statement standards require.

### Boresight calibration

Calibration of the fixed angular offset between a sensor's optical/scan axis and the platform's IMU-defined body frame, required before raw sensor data can be geometrically corrected using the platform's trajectory.
**In use:** "The new LiDAR head needs a fresh boresight before this mission — it wasn't recalibrated after the sensor swap."
**Common misuse:** assuming a boresight calibration from one platform/sensor pairing carries over to a different sensor or mount, or skipping reverification after any physical remount — a boresight offset is specific to the exact mechanical mounting, not the sensor model in general.

### Land-cover-stratified accuracy assessment

Reporting positional accuracy separately for different land-cover classes (typically vegetated vs. non-vegetated) because error distributions differ meaningfully between them.
**In use:** "We report RMSEz-based accuracy for the open-ground checkpoints and 95th-percentile accuracy for the vegetated ones — pooling them would understate the vegetated error."
**Common misuse:** pooling all checkpoints into a single RMSE-based number regardless of land cover, which masks a real accuracy problem in vegetated terrain behind a passing blended average.

### Bundle adjustment

The simultaneous least-squares solve that refines camera positions/orientations and 3D tie-point locations from overlapping imagery, tying the whole block together geometrically.
**In use:** "Reprojection error came back at 1.4 px after the bundle adjustment — check the tie points around the water body, that's usually where it degrades."
**Common misuse:** treating a low reprojection error as proof of absolute accuracy. Bundle adjustment can converge to an internally consistent but absolutely shifted solution if GCPs are sparse, wrong, or unweighted — internal consistency and ground-truth accuracy are different claims.

### NDVI (Normalized Difference Vegetation Index) and other band-ratio indices

An index computed from calibrated reflectance in two or more bands (NDVI = (NIR − Red) / (NIR + Red)) used as a vegetation-vigor proxy.
**In use:** "NDVI's only meaningful here because we ran the radiometric calibration against the panel first — raw digital-number NDVI from two different flight lines isn't comparable."
**Common misuse:** computing an index from uncalibrated digital numbers (raw sensor counts) instead of calibrated surface reflectance, then comparing values across flight lines or dates as if lighting and sensor gain hadn't changed.

### Ground control point (GCP) vs. checkpoint

A GCP is a surveyed point used *in* the geometric solution (bundle adjustment or orthorectification); a checkpoint is an independent surveyed point withheld from the solution and used only to test the result.
**In use:** "We've got 5 GCPs for the solve and 5 separate checkpoints for QC — don't let the field crew mix them up, a checkpoint used as a GCP stops testing anything."
**Common misuse:** using the same points as both GCPs and accuracy checkpoints, which reports the accuracy of the fit to itself rather than an independent measure of real-world accuracy.

### QL (Quality Level) — ASPRS LiDAR classes

A tiered specification (QL0 highest through QL3) defining point density and vertical accuracy thresholds for LiDAR acquisitions, replacing older ad hoc "high/medium/low density" language.
**In use:** "Client asked for 'high-resolution LiDAR' — get them to state a QL class in writing, because 'high-resolution' isn't a spec we can QC against."
**Common misuse:** accepting a colloquial density or accuracy descriptor from a client instead of pinning it to a specific QL class with its stated point spacing and vertical accuracy threshold.

### Radiometric normalization

Adjusting pixel values across multiple images or flight lines so that the same ground feature reads the same reflectance/DN regardless of which image it came from, correcting for lighting, sensor gain, or atmospheric differences between captures.
**In use:** "The seam is visible because line 4 was captured 40 minutes later under thinner cloud — normalize line 4 to the reference tile before mosaicking, don't just feather the seam."
**Common misuse:** treating seamline feathering (blending pixel values at the boundary) as equivalent to radiometric normalization — feathering hides a seam visually without correcting the underlying reflectance mismatch, which reappears in any quantitative index computed from the mosaic.

### Point density vs. point spacing

Point density is points per unit area (points/m²); point spacing is the average linear distance between points, which does not scale linearly with density.
**In use:** "QL1 calls for a nominal pulse spacing of 0.35 m — that's roughly 8 points/m², not the 4 points/m² someone might assume from a quick halving."
**Common misuse:** converting between density and spacing with a linear assumption; spacing scales with the inverse square root of density, so a client asking for "double the density" needs roughly 1.4x tighter spacing, not half.
