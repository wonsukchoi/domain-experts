# Artifacts

Filled calculations and templates for the deliverables a cartographer/photogrammetrist produces and QA-tests. Numbers below are the worked figures from the SKILL.md example (40 sq mi county orthophoto/DTM block, ASPRS 2014 Horizontal/Vertical Accuracy Class 10 cm) unless stated otherwise.

## 1. GSD-to-flying-height back-solve

Formula: `H (m AGL) = GSD (m) × focal length (m) / pixel pitch (m)`, using the sensor's current calibration-certificate values, not the nominal spec sheet.

| Target GSD | Camera (pixel pitch / calibrated focal length) | Flying height AGL | Typical use |
|---|---|---|---|
| 3 in (7.5 cm) | 4.6 µm / 100.5 mm | 1,638.6 m (5,376 ft) | 1"=100' planimetrics, 2 ft-class contours |
| 2.4 in (6 cm) | 4.6 µm / 100.5 mm | 1,310.9 m (4,301 ft) | Accuracy Class 10 cm project (worked example) |
| 1 in (2.5 cm) | 4.6 µm / 100.5 mm | 546.2 m (1,792 ft) | Corridor/utility survey-grade mapping |
| 12 in (30 cm) | 4.6 µm / 100.5 mm | 6,554.3 m (21,503 ft) | Regional/statewide reconnaissance orthophoto |

Image footprint and flight-line spacing for the 6 cm GSD case (sensor array 13,080 × 7,652 px, representative of a medium-format aerial mapping camera):

- Across-track footprint = 13,080 px × 0.06 m = 784.8 m. At 30% sidelap, flight-line spacing = 784.8 m × 0.70 = **549.4 m**.
- Along-track footprint = 7,652 px × 0.06 m = 459.1 m. At 60% endlap, air base (distance between exposures) = 459.1 m × 0.40 = **183.6 m**.
- For an 8 km (E-W) × 13 km (N-S) block: flight lines = 8,000 m / 549.4 m + 1 ≈ 15.6 → **16 lines**, oriented N-S, with a margin line on each side for edge-of-block stereo coverage.

## 2. NSSDA checkpoint accuracy test — full residual table

20 independent GNSS-RTK checkpoints, NAD83(2011) epoch 2010.00 horizontal / NAVD88 via GEOID18 vertical, never used as aerial-triangulation control. Residuals in centimeters (measured minus surveyed).

| Point | dx (cm) | dy (cm) | dz (cm) | dx² | dy² | dz² |
|---|---|---|---|---|---|---|
| CP-01 | 2 | 3 | 3 | 4 | 9 | 9 |
| CP-02 | -3 | -2 | -4 | 9 | 4 | 16 |
| CP-03 | 4 | 1 | 5 | 16 | 1 | 25 |
| CP-04 | -1 | -4 | -2 | 1 | 16 | 4 |
| CP-05 | 3 | 2 | 6 | 9 | 4 | 36 |
| CP-06 | -2 | -3 | -5 | 4 | 9 | 25 |
| CP-07 | 5 | 4 | 4 | 25 | 16 | 16 |
| CP-08 | -4 | -1 | -3 | 16 | 1 | 9 |
| CP-09 | 2 | 3 | 7 | 4 | 9 | 49 |
| CP-10 | -3 | -2 | -6 | 9 | 4 | 36 |
| CP-11 | 1 | 5 | 2 | 1 | 25 | 4 |
| CP-12 | -2 | -3 | -5 | 4 | 9 | 25 |
| CP-13 | 4 | 2 | 8 | 16 | 4 | 64 |
| CP-14 | -3 | -4 | -4 | 9 | 16 | 16 |
| CP-15 | 2 | 1 | 3 | 4 | 1 | 9 |
| CP-16 | -1 | -2 | -6 | 1 | 4 | 36 |
| CP-17 | 3 | 3 | 5 | 9 | 9 | 25 |
| CP-18 | -2 | -1 | -2 | 4 | 1 | 4 |
| CP-19 | 1 | 4 | 4 | 1 | 16 | 16 |
| CP-20 | -4 | -2 | -7 | 16 | 4 | 49 |
| **Σ** | | | | **162** | **162** | **473** |

n = 20. RMSEx = √(162/20) = 2.85 cm. RMSEy = √(162/20) = 2.85 cm. RMSEr = √(2.85² + 2.85²) = 4.03 cm. RMSEz = √(473/20) = 4.86 cm.

95%-confidence accuracy: horizontal = RMSEr × 1.7308 = 6.97 cm. Vertical = RMSEz × 1.9600 = 9.53 cm.

**Reading the table for a bias, not just the RMSE:** dx and dy alternate sign roughly evenly across points (no directional bias — consistent with correct boresight and datum handling). If instead every dz had come back negative, that pattern (not the RMSE magnitude) would be the first thing to chase — see [references/red-flags.md](red-flags.md) entry 1.

## 3. Ground control point (GCP) spacing scheme

For a block adjustment using GNSS/IMU-assisted direct georeferencing (reduces but does not eliminate GCP need):

| Zone | GCP role | Placement rule |
|---|---|---|
| Block perimeter | Horizontal + vertical control | One GCP within 1 photo base of each block corner, plus mid-edge points at intervals no wider than 4 photo bases |
| Block interior | Vertical-only or full 3D check | One point every 6-8 photo bases along interior flight lines, offset between lines to avoid a single systematic strip error going undetected |
| Independent checkpoints | Never used in AT | Minimum 20 per NSSDA, at least 5 per quadrant, none closer together than 1/10 of the block's diagonal dimension, none coincident with a GCP |

Rule of thumb: a direct-georeferencing block with a strong GNSS baseline (<20 km to base station or RTN-corrected) can drop physical GCP count by roughly half versus a GCP-only adjustment for the same accuracy class — the tradeoff is a tighter requirement on boresight calibration currency.

## 4. LiDAR point-density and classification spec (USGS 3DEP QL2 baseline)

| Parameter | QL2 (national 3DEP baseline) | QL1 (high-relief/engineering-grade) |
|---|---|---|
| Nominal point density | ≥2 points/m² (aggregate) | ≥8 points/m² (aggregate) |
| Vertical accuracy, non-vegetated (RMSEz) | ≤10 cm | ≤10 cm (same target, tighter achieved via density) |
| Vertical accuracy, vegetated (95th percentile, VVA) | ≤20 cm, tested separately from NVA | ≤20 cm, tested separately from NVA |
| Ground classification | LAS class 2 (ground); classes 3-5 (low/med/high vegetation); class 6 (building); class 9 (water) per ASPRS LAS 1.4 | Same classification scheme |
| Typical use | County/regional DTM, floodplain mapping | Corridor/utility design, high-relief terrain, forest-canopy studies |

In forested project tiles, expect ground-classified returns to run 15-30% of total returns — if a tile's ground-classified density drops well below that fraction relative to its neighbors, treat it as a canopy-density or classification-algorithm problem before accepting the bare-earth surface (see red-flags.md entry 8).

## 5. Combined scale factor — grid-to-ground reduction (State Plane example)

Combined Scale Factor (CSF) = Grid Scale Factor × Elevation Factor.

Elevation Factor = R / (R + h), using mean earth radius R ≈ 20,906,000 ft.

Worked example: site elevation h = 1,000 ft above the ellipsoid, Grid Scale Factor at the site (state plane zone, off the central meridian) = 0.999900.

Elevation Factor = 20,906,000 / (20,906,000 + 1,000) = 20,906,000 / 20,907,000 = 0.9999522.

CSF = 0.999900 × 0.9999522 = **0.9998422**.

Ground distance = Grid distance / CSF. For a 5,000.00 ft grid (digitized/photogrammetric) distance:

Ground distance = 5,000.00 / 0.9998422 = **5,000.79 ft** — a 0.79 ft discrepancy against the raw grid value, large enough to flag on a construction-staking comparison at that baseline length.

**Template line for a QA memo when this pattern appears:** "Grid-to-ground discrepancy at [site] measures [X] ft over a [Y] ft baseline (~[X/Y × 1,000,000] ppm) — consistent with an unapplied combined scale factor of [CSF]; confirm survey crew is staking from ground-adjusted, not raw grid, coordinates before remeasuring."

## 6. FGDC/NSSDA accuracy-statement template

```
POSITIONAL ACCURACY STATEMENT — [Product Name], [Block/Project ID]

Compiled to meet ASPRS Positional Accuracy Standards for Digital Geospatial
Data (2014): Horizontal Accuracy Class RMSEx = RMSEy = [N] cm;
Vertical Accuracy Class ([non-vegetated / vegetated]) RMSEz = [N] cm.

Datum: [horizontal datum + epoch] (horizontal), [vertical datum via geoid
model] (vertical).

Tested against [n >= 20] independent checkpoints not used in aerial-
triangulation or LiDAR control, distributed across all [k] block quadrants
per NSSDA guidance.

Horizontal accuracy tested [RMSEr] cm RMSEr ([RMSEr x 1.7308] cm horizontal
accuracy at 95% confidence, radial).
Vertical accuracy tested [RMSEz] cm ([RMSEz x 1.9600] cm vertical accuracy
at 95% confidence, linear).

Result: [PASS/FAIL] against contracted Horizontal Accuracy Class [N] cm
and Vertical Accuracy Class [N] cm.
```
