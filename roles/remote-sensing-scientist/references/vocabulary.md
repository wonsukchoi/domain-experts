# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Surface reflectance vs. TOA (top-of-atmosphere) reflectance

- **Definition:** TOA reflectance is radiance normalized by solar irradiance and sun angle, measured before removing the atmosphere's contribution; surface reflectance additionally removes atmospheric scattering/absorption to represent what a sensor at ground level would see.
- **Practitioner usage:** "The two dates are six months apart with different haze conditions — we need Sen2Cor surface reflectance, not TOA, or the NDVI difference is partly atmosphere."
- **Common misuse:** treating TOA reflectance as "already corrected" because it's normalized to a 0–1 reflectance-like scale — it still carries the full atmospheric signal, which varies scene to scene.

## Spatial resolution vs. minimum mapping unit (MMU)

- **Definition:** spatial resolution is the pixel's ground sampling distance (e.g., 30 m for Landsat); the minimum mapping unit is the smallest patch size the product actually claims to map reliably, which is normally several pixels, not one.
- **Practitioner usage:** "30 m resolution, but our MMU is 0.5 ha (~6 pixels) — single-pixel detections are noise we don't report as change."
- **Common misuse:** assuming a product maps individual pixels reliably just because the pixel size is stated; single isolated pixels are the most error-prone unit in any classified map.

## User's accuracy vs. producer's accuracy

- **Definition:** user's accuracy (row-based) — of everything mapped as class X, what fraction is really X (relates to commission error/false positives). Producer's accuracy (column-based) — of everything that's really class X, what fraction got mapped as X (relates to omission error/false negatives).
- **Practitioner usage:** "User's accuracy for 'forest loss' is 78% — when the map says loss, it's right 78% of the time. Producer's accuracy is 93% — we're catching 93% of real loss. Different questions, different consumers care about different ones."
- **Common misuse:** using "accuracy" unqualified when the two numbers diverge meaningfully; a credit buyer relying on the map cares about user's accuracy (how much of what's claimed is real), while a conservation monitor cares more about producer's accuracy (how much real loss is being missed).

## Overall accuracy vs. kappa coefficient

- **Definition:** overall accuracy is the simple proportion of correctly classified sample points; kappa additionally discounts the agreement expected by chance given the class proportions.
- **Practitioner usage:** "Overall accuracy 93%, kappa 0.71 — the gap tells you a chunk of that agreement is the dominant 'stable' class being easy, not real discriminative skill."
- **Common misuse:** treating either metric alone as sufficient; both can look strong while a minority class's user's accuracy is unusable — always report per-class figures alongside the summary statistics.

## Error-adjusted area estimate

- **Definition:** the classified area corrected for the classifier's known omission and commission error rates (from the confusion matrix), as opposed to the raw pixel-count area, following the stratified estimator in Olofsson et al. (2014).
- **Practitioner usage:** "The map shows 620 ha, but the error-adjusted estimate is 1,046 ha (CI 420–1,670) — the stable stratum's small false-negative rate adds up over its huge area."
- **Common misuse:** reporting pixel-count area as the final number once an accuracy assessment exists — the whole point of running the assessment is to correct the area estimate, not just certify a percentage.

## Radiometric calibration vs. atmospheric correction

- **Definition:** radiometric calibration converts sensor digital numbers to physical at-sensor radiance using the sensor's own calibration coefficients; atmospheric correction then removes the atmosphere's contribution to get surface reflectance. They are sequential, not interchangeable steps.
- **Practitioner usage:** "Radiometric calibration handles sensor drift between missions; atmospheric correction handles haze and aerosol differences between acquisition dates — skip either one and the other doesn't compensate for it."
- **Common misuse:** calling any preprocessing step "calibration" loosely, obscuring which specific source of error (sensor vs. atmosphere) has actually been addressed.

## Co-registration RMSE

- **Definition:** the root-mean-square error, in pixels, between corresponding features in two geometrically aligned images — the standard metric for how well two dates or two sensors are spatially aligned.
- **Practitioner usage:** "Co-registration RMSE is 0.8 pixels — too loose for change detection at this resolution; re-tie with more control points before differencing."
- **Common misuse:** accepting "orthorectified" as sufficient without checking the actual RMSE value or its units; sub-pixel misregistration manufactures false change concentrated at every edge in the scene.

## Spectral index (NDVI, NBR, NDWI)

- **Definition:** a normalized ratio of specific spectral bands designed to isolate a physical signal — NDVI (NIR, Red) for vegetation vigor, NBR (NIR, SWIR) for burn severity, NDWI (Green, NIR or NIR, SWIR) for water/moisture content.
- **Practitioner usage:** "dNBR between pre- and post-fire imagery gives us burn severity classes, but only after both scenes are atmospherically corrected to the same reflectance basis."
- **Common misuse:** treating an index as a direct physical measurement rather than a proxy — NDVI saturates at high biomass and is sensitive to soil background at low cover, so "NDVI = biomass" breaks down at both ends of the range.

## Change-vector analysis vs. post-classification comparison

- **Definition:** change-vector analysis differences the corrected reflectance (or index) values directly between two dates; post-classification comparison classifies each date independently and compares the resulting class labels.
- **Practitioner usage:** "Post-classification comparison is easier to explain to the client, but its error compounds — two 90%-accurate classifications only agree on true change about 81% of the time at best."
- **Common misuse:** assuming post-classification comparison inherits the accuracy of each single-date classification, when in fact multiplying two error-prone classifications together degrades the change-detection accuracy below either one alone.

## Bidirectional reflectance distribution function (BRDF) effects

- **Definition:** the dependence of measured surface reflectance on the specific sun-sensor-surface geometry (illumination angle, viewing angle) at the moment of acquisition, independent of any real change on the ground.
- **Practitioner usage:** "The two acquisitions have different off-nadir view angles — we need a BRDF normalization before trusting the index difference as a ground signal."
- **Common misuse:** ignoring BRDF effects for off-nadir or seasonally distant image pairs and attributing the resulting index shift entirely to ground change.

## Analysis Ready Data (ARD)

- **Definition:** imagery pre-processed to a standardized, documented specification (radiometric calibration, atmospheric correction, geometric registration, common grid) so analysts don't repeat the correction chain from raw data — CEOS's CARD4L is the reference specification.
- **Practitioner usage:** "We're using Landsat Collection 2 Level-2 ARD, which is already surface-reflectance and cloud-masked — that saves us the atmospheric correction step, but we still verify the RMSE and cloud mask ourselves."
- **Common misuse:** assuming "ARD" means zero further QA is needed — the ARD label guarantees a documented processing chain, not that it's error-free or optimal for every use case.
