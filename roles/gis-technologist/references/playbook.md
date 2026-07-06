# GIS Technologist — Playbook

## CRS reconciliation and reprojection checklist

1. Identify the native CRS and datum of every dataset involved in the analysis.
2. Determine the appropriate target CRS for the specific analysis (equal-area projection for area calculations, appropriate conformal/equidistant projection for distance calculations, local projected system for display/measurement precision).
3. Reproject any dataset not already in the target CRS.
4. Verify reprojection succeeded by spot-checking known reference points or distances against an independent source.
5. Only proceed to analysis (overlay, intersection, buffer) once all datasets share the confirmed common CRS.

## Flood zone/parcel overlap calculation — before and after reprojection (filled example)

| Step | Value |
|---|---|
| Parcel data CRS | State Plane (NAD83, feet) |
| Flood zone data CRS (as delivered) | Unprojected WGS84 (geographic) |
| **Uncorrected intersection result** (no reprojection, layers appear visually aligned) | **0.3 acres** |
| Topology validation on flood zone layer | 3 sliver gaps found and corrected |
| Flood zone data reprojected to | State Plane (NAD83, feet) — matching parcel CRS |
| **Corrected intersection result** | **4.82 acres** |
| **Discrepancy** | Uncorrected result understated true overlap by ~94% (16x difference) |

**Use:** Always reproject to a common CRS and validate topology before trusting an intersection/overlap calculation — a visually aligned map is not evidence that the underlying calculation is correct.

## Topology validation checklist

1. Check for gaps between adjacent polygons that should share a boundary.
2. Check for unintended overlaps between polygons that should be mutually exclusive.
3. Check for dangling nodes in line data (endpoints that should connect to another line but don't).
4. Correct identified errors (snapping, gap closure) before running area, adjacency, or network analysis on the dataset.

## Geocoding precision assessment table

| Match type | Typical precision | Suitable for |
|---|---|---|
| Rooftop | Highest — actual building location | Parcel-level proximity, fine-grained boundary determination |
| Street-interpolated | Moderate — estimated position along street segment | Neighborhood-level analysis, general routing |
| ZIP/area centroid | Lowest — center of a broad area | Regional-level aggregation only, not fine-grained proximity |

**Use:** Check the match-type distribution of a geocoded dataset before using it for an analysis that requires fine-grained precision — a dataset heavy in ZIP-centroid matches isn't fit for a parcel-level proximity determination, regardless of how many total points it contains.

## Scale/generalization compatibility check

1. Identify the dataset's original digitizing or generalization scale (often noted in metadata, e.g., "1:100,000 scale source").
2. Compare it against the current analysis's required scale (e.g., parcel-level, site-specific).
3. If the analysis scale is significantly finer than the data's source scale, flag false-precision risk and consider sourcing a finer-scale dataset instead.

## Spatial analysis findings memo — filled example

> **Flood Zone Overlap Analysis — Parcel Group [ref]**
> Initial analysis (uncorrected CRS): flood zone/parcel overlap calculated at 0.3 acres — flood zone data was in unprojected WGS84 while parcel data was in State Plane (feet), producing a misaligned intersection despite the map appearing visually correct.
> Corrected analysis: flood zone data reprojected to State Plane (NAD83, feet), 3 topology gaps in the flood zone layer corrected, intersection recalculated at **4.82 acres**.
> **Finding: The uncorrected analysis understated flood zone exposure by roughly 94% (0.3 vs. 4.82 acres). All spatial layers must be reprojected into a common CRS and topology-validated before any area/intersection calculation is treated as reliable.**
