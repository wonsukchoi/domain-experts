# Red Flags

Smell tests for remote sensing products and accuracy claims. Format per flag: what it usually means, the first question to ask, the data to pull.

### Overall accuracy reported above 90% with no per-class breakdown

- **Usually means:** a dominant, easy-to-classify stable class (e.g., "not forest loss") is inflating the weighted average while the class that actually matters has a much lower user's accuracy.
- **First question:** "What's the user's and producer's accuracy for the target class specifically, and what's its share of the sample?"
- **Data to pull:** the full confusion matrix, not just the accuracy scalar; recompute per-class accuracy from raw counts.

### Multi-date NDVI (or other index) comparison with no stated atmospheric correction method

- **Usually means:** the "change" signal includes atmospheric haze, sun-angle, or sensor-calibration differences between acquisition dates, not just ground change.
- **First question:** "Were both dates corrected to surface reflectance with the same algorithm and version, or compared as TOA/DN?"
- **Data to pull:** processing metadata for both scenes; if absent, treat the index difference as unverified until reprocessed.

### Geometric RMSE not reported, or reported without units/pixel reference

- **Usually means:** co-registration quality was never checked, and edge-adjacent "change" in the product is misregistration, not real change.
- **First question:** "What was the RMSE in pixels for the orthorectification and, separately, for co-registration between dates?"
- **Data to pull:** the tie-point residuals report from the orthorectification/co-registration software; re-run if missing.

### Cloud cover fraction over the study area exceeds ~20% and isn't mentioned

- **Usually means:** cloud/shadow contamination is masquerading as valid pixels, especially at cloud edges where partial contamination isn't flagged by a binary mask.
- **First question:** "What fraction of the study area (not the whole scene) is actually cloud-free after masking?"
- **Data to pull:** the scene classification layer or Fmask output clipped to the study area boundary, not the scene-wide cloud percentage in the metadata header.

### Accuracy assessment reference points drawn from a simple random sample across a highly imbalanced map

- **Usually means:** the rare class (often the one driving the decision — burn scar, illegal clearing, invasive species patch) has too few reference points for its accuracy estimate to have a usable confidence interval.
- **First question:** "How many reference points landed in the class we actually care about, and what's the CI on its accuracy?"
- **Data to pull:** the per-stratum sample allocation; if the target class has fewer than ~30 points, the accuracy estimate for it is not reliable enough to report as a point value.

### Reference data pulled from pixels near the training set

- **Usually means:** spatial autocorrelation between training and "independent" reference pixels is inflating the accuracy estimate — neighbors of training pixels are systematically easier to classify correctly.
- **First question:** "How were reference points selected, and what's their minimum distance from any training pixel?"
- **Data to pull:** the reference point selection methodology and a map of reference points overlaid on the training set footprint.

### Mapped (pixel-count) area reported without an error-adjusted estimate or confidence interval

- **Usually means:** the reported area is biased by the classifier's omission/commission error, potentially by tens of percent, and its precision is unstated.
- **First question:** "Has the error-adjusted area estimator been run on the confusion matrix, and what's the 95% CI?"
- **Data to pull:** the confusion matrix and stratum weights needed to compute the Olofsson-style estimator.

### Change detected concentrated at scene edges or tile boundaries

- **Usually means:** mosaic seams, edge-effect radiometric differences between adjacent processing tiles, or orthorectification error concentrated at scene margins — not real ground change.
- **First question:** "Does the change pattern follow tile/scene boundaries rather than terrain or land-use boundaries?"
- **Data to pull:** the tile/scene footprint overlay against the change-detection output.

### A trained classifier (random forest, CNN) used when a threshold rule wasn't tried first

- **Usually means:** added complexity and validation burden with no demonstrated accuracy gain over a simpler, auditable method.
- **First question:** "What accuracy did a spectral-index threshold achieve on the same validation set, and by how much did the trained classifier beat it?"
- **Data to pull:** a side-by-side accuracy comparison; if the gap is small, the simpler method should ship.

### Product delivered without correction-chain or classification metadata

- **Usually means:** the product can't be audited, reproduced, or trusted by the next analyst — a common shortcut under deadline pressure.
- **First question:** "Can I reproduce this exact product from the metadata alone?"
- **Data to pull:** the deliverable checklist (sensor/date, correction chain + version, cloud fraction retained, RMSE, classification method, confusion matrix, error-adjusted area with CI, MMU); flag every missing field.

### Same reported accuracy number used across map revisions or years without re-assessment

- **Usually means:** the accuracy figure from an initial validation is being carried forward as if it still applies after reprocessing, a sensor change, or a new study area — accuracy is scene- and date-specific, not a property of the algorithm in general.
- **First question:** "When was this accuracy number measured, on which scene(s), and does it still apply to the current product?"
- **Data to pull:** the date and scene ID of the original accuracy assessment versus the current product's acquisition date.
