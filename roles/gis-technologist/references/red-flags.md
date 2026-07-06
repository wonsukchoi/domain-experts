### Two datasets appear visually aligned on a map but haven't had their CRS/datum explicitly checked
- **Usually means:** The software may be reprojecting on the fly for display while the underlying geometry used for calculations is still in mismatched coordinate systems, producing silently wrong analysis results.
- **First question:** What is each dataset's actual native CRS and datum, and have they been reconciled (reprojected to a common system) before any calculation?
- **Data to pull:** Each dataset's metadata/CRS definition.

### An area or distance calculation is performed on unprojected (geographic, lat/long) coordinates
- **Usually means:** The result is likely systematically inaccurate, since degrees of latitude/longitude aren't equal-length units suited for direct measurement.
- **First question:** Has the data been reprojected into an appropriate projected CRS (equal-area for area, suitable conformal/equidistant for distance) before this calculation?
- **Data to pull:** Current CRS of the dataset used for the calculation.

### A spatial intersection or overlap calculation returns a suspiciously small or zero result
- **Usually means:** This is a common symptom of a CRS/datum mismatch causing the layers to be effectively misaligned in the underlying geometry, not necessarily a true finding about minimal overlap.
- **First question:** Do all layers involved in this calculation share the same CRS, confirmed explicitly rather than assumed from visual alignment?
- **Data to pull:** CRS of each layer in the calculation, the raw intersection result before and after reprojection.

### Polygon or line data hasn't been checked for topology errors before a derived analysis
- **Usually means:** Gaps, overlaps, or dangling nodes could be silently distorting area totals, adjacency results, or network routing calculations.
- **First question:** Has topology validation been run on this dataset, and were any errors found and corrected?
- **Data to pull:** Topology validation report (or its absence) for the dataset.

### Geocoded address data is used in a fine-grained proximity or boundary analysis without checking match type
- **Usually means:** A low-precision match (e.g., ZIP-centroid) could introduce significant positional error if treated as if it had rooftop-level accuracy.
- **First question:** What match type does each geocoded point in this dataset carry, and is that precision level sufficient for this specific analysis?
- **Data to pull:** Geocoding match-type breakdown for the dataset used.

### A dataset is being analyzed at a finer scale than its apparent original digitizing/generalization level
- **Usually means:** Features may have been simplified for a broader display scale, introducing false precision if analyzed at a much finer scale (e.g., parcel-level).
- **First question:** What scale was this dataset originally digitized or generalized for, and does it match the current analysis's required precision?
- **Data to pull:** Dataset metadata indicating source scale or generalization tolerance.

### A spatial analysis report presents a final number (acreage, distance, boundary determination) with no stated CRS or precision limitations
- **Usually means:** The result may be relied upon beyond what the underlying data actually supports, without the reader knowing what precision or validation steps were (or weren't) applied.
- **First question:** Does the report explicitly state the CRS used, topology validation status, and any known precision limitations?
- **Data to pull:** The analysis report's methodology/metadata section (or its absence).

### A significant discrepancy exists between two independently sourced area or distance figures for the same feature
- **Usually means:** A CRS mismatch, topology error, or scale/generalization difference between the two sources is a likely explanation, worth checking before concluding one source is simply "more accurate."
- **First question:** Do the two sources use the same CRS, topology validation approach, and comparable digitizing scale?
- **Data to pull:** CRS, topology status, and scale metadata for both sources being compared.
