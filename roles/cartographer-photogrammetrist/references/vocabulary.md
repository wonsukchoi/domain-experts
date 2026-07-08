# Vocabulary

Terms generalists flatten together that cartographers and photogrammetrists keep sharply separate.

## Ground sample distance (GSD)

The ground-projected size of one pixel in a digital image, determined by sensor pixel pitch, focal length, and flying height. It describes resolution — what can be visually distinguished — not positional accuracy.

*In use:* "We're flying 6 cm GSD, but that's a resolution choice, not the accuracy class — the checkpoint test is what proves the 10 cm RMSE requirement."

*Common misuse:* treating a finer GSD as automatically meaning better accuracy. A well-controlled block at coarser GSD can out-perform a poorly controlled block at finer GSD on the actual RMSE test.

## RMSE vs. NSSDA accuracy (95% confidence)

RMSE (root mean square error) is the raw statistic computed directly from checkpoint residuals. The NSSDA "accuracy at 95% confidence" figure is RMSE multiplied by a fixed factor (1.9600 for vertical/linear error, 1.7308 for horizontal/radial error) to express the value a reader can interpret as a 95%-confidence bound. They are not the same number, and a report that quotes "accuracy" while showing RMSE math (or vice versa) without the multiplier is internally inconsistent.

*In use:* "RMSEz came back at 4.86 cm — multiply by 1.96, that's a 9.53 cm vertical accuracy statement at 95% confidence, that's the number that goes in the metadata."

*Common misuse:* quoting RMSE and calling it "the accuracy" without applying the confidence multiplier, or applying the wrong multiplier (horizontal and vertical use different ones because one is radial/2D and the other is linear/1D).

## NVA / VVA (Non-vegetated / Vegetated Vertical Accuracy)

ASPRS 2014's two-part vertical accuracy test for elevation data: NVA is RMSE-based accuracy measured on checkpoints in open, non-vegetated terrain; VVA is a 95th-percentile accuracy measured separately on checkpoints in vegetated terrain, because LiDAR canopy penetration is incomplete and the error distribution there isn't well-modeled by a simple RMSE-times-multiplier approach.

*In use:* "NVA passed at 8 cm, but VVA under the forest canopy came in at 22 cm — report both, don't average them into one number."

*Common misuse:* reporting a single blended vertical accuracy for a project with mixed land cover, which conceals that the surface is measurably worse under canopy than the headline number suggests.

## Relief displacement

The radial displacement of a point's image position, proportional to the point's height above the reference datum and its distance from the photo's nadir, inversely proportional to flying height: d = h·r/H. It explains why tall objects lean away from the photo center in unrectified imagery and why that lean grows toward the frame edges.

*In use:* "That tower's leaning 40 pixels in the raw frame — that's relief displacement, not a georeferencing error, and it corrects out in the standard ortho for ground features but not for the tower itself."

*Common misuse:* attributing displacement of tall features in a raw (non-orthorectified) image to a georeferencing or datum error, when it's a predictable geometric consequence of photographing a 3D object in central projection.

## Standard orthophoto vs. true orthophoto

A standard orthophoto is rectified against a bare-earth or general surface DTM, which corrects ground relief displacement but leaves buildings, towers, and other above-ground structures displaced and can show occlusion gaps behind tall features. A true orthophoto is rectified against a DSM (including building models) with occluded areas filled from adjacent imagery, correcting structure displacement as well.

*In use:* "The utility company needs true ortho for this urban core — standard ortho will still show the building facades leaning, and that's the exact detail they're trying to measure."

*Common misuse:* assuming "orthophoto" always means fully rectified for every feature in the scene; the standard product only guarantees ground-level correctness.

## Interior orientation vs. exterior orientation

Interior orientation (IO) is the camera's internal geometry — calibrated focal length, principal point offset, lens distortion coefficients — fixed for a given camera/lens combination until recalibrated. Exterior orientation (EO) is each individual photo's position and attitude in space (X, Y, Z, omega, phi, kappa) at the moment of exposure, solved per-image in the bundle adjustment.

*In use:* "IO comes off the calibration certificate and doesn't change photo to photo; EO is what the bundle adjustment is actually solving for on every frame."

*Common misuse:* using "orientation" generically without distinguishing which one a given error source affects — an outdated calibration certificate is an IO problem, a bad GNSS/IMU trajectory is an EO problem, and they're diagnosed differently.

## Bundle adjustment / aerial triangulation (AT)

The simultaneous least-squares solution for the exterior orientation of every image in a block, using tie points between overlapping images plus ground control and/or GNSS/IMU observations as constraints. Its output includes per-point residuals at every control and check point, which is the primary QA artifact for the block.

*In use:* "Run the bundle adjustment before we finalize control — if the GCP residuals blow up, we find out now, not after the ortho is delivered."

*Common misuse:* treating AT as a one-time automated step rather than an adjustment whose residual report needs human review before the block is accepted.

## Boresight calibration / lever-arm offset

The measured angular (boresight) and linear (lever-arm) offset between the GNSS/IMU reference frame and the camera or LiDAR sensor's own reference frame, required to correctly translate the GNSS/IMU trajectory into sensor exterior orientation. Must be calibrated per mobilization or after any physical disturbance to the mount.

*In use:* "Checkpoint residuals are all shifted the same direction across the whole block — that's a boresight problem, re-run the calibration flight before reprocessing."

*Common misuse:* assuming a systematic, block-wide directional offset is a survey or control error, when a consistent-direction bias across an entire block is the signature of an uncalibrated or mis-applied boresight/lever-arm value.

## Combined scale factor (grid-to-ground)

The product of the state-plane grid scale factor (distortion from the map projection) and the elevation factor (reduction for the site's elevation above the ellipsoid), used to convert between grid distances (as used in GIS/CAD coordinate systems) and ground distances (as measured with a total station).

*In use:* "The digitized distance won't match the field tape measurement until you apply the combined scale factor — at this elevation and zone that's about 158 ppm."

*Common misuse:* assuming grid and ground distances should match directly, or applying only the elevation factor and skipping the grid scale factor component (or vice versa).

## Orthometric height vs. ellipsoid height

Orthometric height (e.g., NAVD88) is elevation relative to a gravity-based geoid model, the "on the ground, usable for drainage" height. Ellipsoid height is elevation relative to a purely mathematical reference ellipsoid (e.g., raw GNSS/GPS output), which does not follow gravity and is not directly usable for engineering grading or hydrology without conversion via a geoid model.

*In use:* "That's an ellipsoid height straight off the rover — run it through GEOID18 before it goes in the DTM, or the elevations will be off by the local geoid separation."

*Common misuse:* treating raw GNSS elevation output as ready-to-use engineering elevation without applying the geoid model conversion.

## Nominal Pulse Spacing (NPS) / point density

Two ways of expressing the same LiDAR sampling rate: NPS is the average linear spacing between laser pulses on the ground (meters), point density is pulses per unit area (points/m²) — inversely related (density ≈ 1/NPS²), and project specs may state either one.

*In use:* "QL2 spec calls for roughly 2 points per square meter — that's about 0.71 m nominal pulse spacing, don't quote the two numbers as if they're independent requirements."

*Common misuse:* treating NPS and point density as two separate deliverable requirements to satisfy independently, rather than two expressions of the same underlying acquisition parameter.

## Endlap / sidelap

Endlap (forward overlap) is the percentage of image overlap between consecutive photos along a flight line; sidelap is the overlap between adjacent flight lines. Both drive tie-point redundancy in the bundle adjustment and stereo coverage for compilation.

*In use:* "Bump sidelap to 60% for this block — the terrain relief is enough that 30% is going to starve tie points between lines."

*Common misuse:* treating the commonly cited 60%/30% figures as fixed requirements rather than a floor that needs to increase for high relief, dense urban cores, or LiDAR-integrated capture.

## Ground control point (GCP) vs. checkpoint

A GCP is a surveyed point used as an input constraint in the aerial triangulation or LiDAR adjustment. A checkpoint is a surveyed point deliberately withheld from that adjustment and used only afterward, to independently test the finished product's accuracy. Using the same point as both invalidates the accuracy test.

*In use:* "That point's already in the AT solution as a GCP — it can't also count toward our 20 independent checkpoints."

*Common misuse:* padding the checkpoint count with points that were also used as control, which produces an artificially low (optimistic) RMSE because the adjustment was already fit to those points.

## Datum epoch (e.g., NAD83(2011) epoch 2010.00)

The specific point in time a geodetic datum realization's coordinates are pinned to. In regions with measurable tectonic plate motion, the same physical monument's coordinate in that datum genuinely changes over time relative to the fixed epoch, so "NAD83(2011)" alone is incomplete without stating which epoch the coordinates are expressed in.

*In use:* "State the epoch on every control sheet — NAD83(2011) epoch 2010.00, not just NAD83(2011) — or the Pacific coast monuments won't reconcile with anything surveyed five years later."

*Common misuse:* treating a datum name alone as sufficient metadata, omitting the epoch, which is only harmless in tectonically stable regions and a real source of error elsewhere.
