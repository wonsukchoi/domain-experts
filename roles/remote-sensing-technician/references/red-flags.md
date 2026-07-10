# Red Flags

Smell tests for acquisition and processing defects. Format per flag: what it usually means, the first question to ask, the data to pull.

### One checkpoint residual >3x the running RMSE

- **Usually means:** a localized classification or GCP-entry defect (most common), or a genuine unrepresentable terrain feature at that spot (less common).
- **First question:** "Is this a data problem local to one tile, or a systematic problem across the whole block?"
- **Data to pull:** the classified point cloud or raw imagery at that exact coordinate, plus the checkpoint's own survey closure/RMS to rule out a bad checkpoint.

### Reprojection error or boresight residual passes, but the delivered orthomosaic still looks geometrically wrong on the ground

- **Usually means:** the DEM/DSM used for rectification is stale or too coarse for the terrain relief — a bundle adjustment can converge cleanly while rectifying onto the wrong elevation surface.
- **First question:** "What elevation source and resolution was used for orthorectification, and how old is it relative to the current ground surface?"
- **Data to pull:** the rectification DEM's source/date and its resolution vs. the target GSD; compare against a recent LiDAR or photogrammetric DSM if one exists.

### Colored fringing on high-contrast edges in a multispectral composite

- **Usually means:** band-to-band misregistration, not atmospheric correction error — the fringe is directional and edge-localized, which atmospheric effects are not.
- **First question:** "Does the fringe direction and offset match the platform's flight-line heading or sensor mounting geometry?"
- **Data to pull:** per-band tie-point residuals from the co-registration step; check if the affected bands share a sensor head or capture timing offset.

### Sudden NDVI or reflectance shift at a flight-line seam

- **Usually means:** radiometric normalization used a cloud-shadowed or off-angle tile as its reference, or lighting changed materially between flight lines (passing cloud, different time of day).
- **First question:** "What time was each flight line captured, and was the reference tile for normalization verified clear?"
- **Data to pull:** capture timestamps per line, sun-angle log, and the specific tile used as the radiometric reference.

### Checkpoint accuracy report with fewer checkpoints delivered than planned

- **Usually means:** one or more checkpoints were quietly excluded to make the accuracy statement pass — a standards violation if undocumented.
- **First question:** "Which checkpoints are missing from this report versus the acquisition plan, and where's the documented cause for each?"
- **Data to pull:** the original checkpoint plan/count vs. the final report's checkpoint list; the metadata's stated exclusion reasons, if any.

### 94%+ ground-point classification with no visible bare-earth gaps under dense canopy

- **Usually means:** the ground filter is too aggressive and is pulling low vegetation or understory returns down into the ground class, not that the terrain is genuinely well-sampled under canopy.
- **First question:** "What's the ground-point density specifically under the canopy-covered portion of the block, compared to the open portion?"
- **Data to pull:** ground-point density raster split by land-cover mask; a cross-section profile through a known canopy area.

### GNSS fix type drops from RTK-fixed to float or autonomous mid-flight-line

- **Usually means:** base-station dropout, multipath from terrain/structures, or baseline length exceeding the RTK correction's effective range.
- **First question:** "What was the baseline distance to the base station at the point the fix degraded, and did it exceed the correction service's rated range?"
- **Data to pull:** the GNSS log's fix-type time series for the affected line; baseline distance at the degradation timestamp.

### Calibration file more than one validity cycle old still in use

- **Usually means:** the field team is reusing "last known good" calibration past its currency window because recalibration wasn't scheduled, not because it's still accurate.
- **First question:** "When was this calibration file generated, and what's the manufacturer's stated validity window for this sensor?"
- **Data to pull:** calibration file metadata timestamp; the two most recent missions' checkpoint accuracy margins to see if drift is already visible.

### A processing run that finished with zero software errors but the client flags the product as "off" on inspection

- **Usually means:** the pipeline executed successfully on a bad input (dropped IMU epoch, transposed GCP coordinate, corrupted band) that no software-level error check catches.
- **First question:** "What does the independent checkpoint QC say — was it actually run, or did the delivery skip straight from processing to packaging?"
- **Data to pull:** the checkpoint QC log for this specific delivery; confirm it exists and wasn't copied forward from a prior, unrelated job.
