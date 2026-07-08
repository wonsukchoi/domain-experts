# Red flags

Smell tests a QA reviewer or project lead catches before a block ships. Format for each: what it usually means, the first question to ask, and the data to pull.

## 1. Checkpoint residuals show a consistent directional bias rather than random scatter

**Usually means:** boresight/lever-arm miscalibration between the GNSS/IMU and the camera or LiDAR sensor, or an incorrect geoid model applied in the height reduction — both produce a systematic offset in one direction, not noise.

**First question:** "Plot the residual vectors on the block diagram — do they all point the same way, or cluster by flight strip?"

**Data to pull:** the full checkpoint residual table with sign; the boresight calibration report and its date relative to the mission; the geoid model version used in the height reduction.

## 2. Grid distance disagrees with a field total-station distance by more than ~20 ppm (0.02 ft per 1,000 ft)

**Usually means:** the combined scale factor (grid scale factor × elevation factor) wasn't applied when reconciling photogrammetric/GIS coordinates against a ground-based construction survey.

**First question:** "Is the survey crew staking from ground-adjusted coordinates or raw state-plane grid coordinates?"

**Data to pull:** the project's stated combined scale factor and site elevation; the coordinate system metadata on both the GIS deliverable and the survey crew's data collector.

## 3. A DTM covering heavy canopy reports only a single blended vertical RMSE, no NVA/VVA split

**Usually means:** the vertical accuracy test wasn't stratified by land cover, hiding the fact that vegetated-terrain accuracy is materially worse than the reported number.

**First question:** "Show me the vertical RMSE computed on checkpoints located specifically in forested/vegetated cover, separate from the open-terrain checkpoints."

**Data to pull:** checkpoint locations tagged by land-cover class; NVA and VVA computed and reported separately per ASPRS 2014 methodology.

## 4. One checkpoint's residual is far outside the pattern of the rest (an order of magnitude higher)

**Usually means:** a busted or disturbed monument, a transposed point ID between the field data and the AT solution, or GNSS multipath at that specific station — rarely a genuine block-wide accuracy problem.

**First question:** "Was that point re-observed, and does the field photo/description match the point ID in the deliverable?"

**Data to pull:** field observation log and site photo for the outlier point; a re-computation of RMSE with and without that point to see whether it's masking or just adding noise to the real number.

## 5. Sidelap or endlap drops below spec in a specific flight strip

**Usually means:** wind-correction (crab angle) during acquisition reduced effective overlap without the flight crew flagging it, leaving a stereo coverage gap.

**First question:** "Pull the as-flown overlap report for that strip — where specifically does it fall below the planned percentage, and by how much?"

**Data to pull:** as-flown GNSS/IMU trajectory and computed overlap per exposure; whether the AT solution shows degraded tie-point redundancy in that strip; refly cost/schedule impact.

## 6. Orthophoto seam shows ghosting or a double image through a tall structure

**Usually means:** the orthorectification used a bare-earth or surface DTM rather than a DSM with the structure modeled — relief displacement on the building wasn't corrected, which a standard (non-true) orthophoto is not designed to fix.

**First question:** "Is this deliverable specified as a standard or a true orthophoto, and does the client's use case (utility/cadastral) actually require true-ortho treatment?"

**Data to pull:** the surface model used for rectification (DTM vs DSM); the building's height and radial distance from nadir to confirm the displacement magnitude matches d = h·r/H.

## 7. Camera calibration certificate is more than ~2 years old, or the camera mount was serviced since calibration

**Usually means:** the interior orientation parameters (focal length, principal point, distortion coefficients) used in the AT solution may no longer match the sensor's actual geometry.

**First question:** "When was this camera last calibrated, and has the lens or mount been serviced or removed since?"

**Data to pull:** the calibration certificate date and issuing lab; the aircraft/sensor maintenance log for any lens or mount disturbance since that date.

## 8. Ground-classified LiDAR point density drops sharply in one tile relative to its neighbors

**Usually means:** dense canopy is starving ground returns in that tile, or the classification algorithm's parameters aren't tuned for that vegetation type — either way, the bare-earth surface there is more interpolated than measured.

**First question:** "What's the ground-classified point density in this tile versus the project average, and what's the dominant land cover?"

**Data to pull:** per-tile ground-classification density report; land-cover classification for the tile; whether a supplemental ground survey was budgeted for that area.

## 9. Deliverable metadata states a horizontal datum without an epoch

**Usually means:** the coordinates are ambiguous in any region with measurable plate motion — the same monument's NAD83(2011) coordinate genuinely differs by centimeters between epochs, and "NAD83" alone doesn't specify which.

**First question:** "What epoch was used for the horizontal control, and does it match the epoch of any legacy control being tied into?"

**Data to pull:** project metadata's stated datum/epoch; the epoch of any pre-existing site control monuments being incorporated.

## 10. Reported elevations differ from expected orthometric values by roughly 20-30 m in a way that "looks like a datum problem"

**Usually means:** ellipsoid heights (raw GNSS output) were delivered or used in a computation without applying the geoid model to convert to orthometric (NAVD88) heights — the geoid separation in the contiguous US commonly runs in that range depending on region.

**First question:** "Are these elevations ellipsoid heights or orthometric heights, and which geoid model was applied?"

**Data to pull:** the height type stated in the metadata; the geoid model version and its epoch/coverage for the project area.

## 11. Fewer than 20 independent checkpoints used for the accuracy test

**Usually means:** the test sample is below the NSSDA minimum, so the reported RMSE isn't a certifiable accuracy statement under the standard even if the number itself looks good.

**First question:** "How many independent checkpoints were used, and were any of them reused GCPs from the AT solution?"

**Data to pull:** the checkpoint list cross-referenced against the GCP list used in aerial triangulation, to confirm independence and count.

## 12. Bundle adjustment's unit-weight standard error (sigma-naught) is high relative to the sensor's expected image-measurement precision

**Usually means:** a systemic tie-point matching problem or GCP mis-weighting in the adjustment, not just normal observational noise — worth resolving before trusting any per-point residual from that solution.

**First question:** "What's this block's sigma-naught compared to our typical range for this sensor and flying height, and has anyone reviewed the tie-point residual distribution for outlier clusters?"

**Data to pull:** the AT adjustment report's sigma-naught and per-point residual list; a comparison against sigma-naught from recent blocks flown with the same sensor.
