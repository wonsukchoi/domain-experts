### Coordinate reference system (CRS)
A defined framework (including a datum and, for projected systems, a projection) that specifies how coordinates relate to actual locations on the Earth's surface.
**In use:** "These two datasets need to be reconciled to a common CRS before we run the intersection."
**Common misuse:** Assuming two datasets share a CRS because they display correctly together on screen, when GIS software commonly reprojects on the fly for viewing regardless of the underlying data's actual coordinate system.

### Datum
The reference model of the Earth's shape and position (e.g., NAD83, WGS84) that a coordinate reference system is built on — datasets on different datums can be offset even within the same nominal coordinate system.
**In use:** "Even though both files claim to use similar coordinates, one is on NAD27 and the other on NAD83 — that offset needs correcting."
**Common misuse:** Treating "same coordinate values" as sufficient confirmation of alignment without checking whether the underlying datum also matches.

### Projected coordinate system
A CRS that mathematically transforms the Earth's curved surface onto a flat plane using a specific projection, producing coordinates in linear units (feet, meters) suitable for accurate area and distance measurement.
**In use:** "We reprojected into State Plane (feet-based) before calculating acreage."
**Common misuse:** Calculating area or distance directly from an unprojected geographic (lat/long) coordinate system, where the units aren't equal-length and don't support accurate linear measurement.

### Geographic coordinate system
An unprojected CRS expressing locations in angular units (degrees of latitude and longitude), suited for global reference but not for direct area/distance calculation.
**In use:** "The flood zone data came in as unprojected WGS84 — it needs reprojecting before we measure anything."
**Common misuse:** Using geographic coordinates directly for area or distance calculations, introducing systematic measurement error since degrees aren't equal-length units.

### Topology (GIS)
The set of spatial relationships (adjacency, connectivity, containment) between features in a dataset, and the validation process that checks for errors like gaps, overlaps, and dangling nodes.
**In use:** "Topology validation found three sliver gaps between adjacent parcels that needed correcting before the area totals could be trusted."
**Common misuse:** Running area, adjacency, or network analysis on polygon/line data without first validating topology, letting undetected errors silently distort the results.

### Sliver gap / overlap
A small, often unintended gap or overlap between adjacent polygon features, typically resulting from digitizing imprecision, that distorts area calculations and adjacency analysis if left uncorrected.
**In use:** "The sliver gaps between these parcels were small individually but added up to a meaningful area discrepancy across the dataset."
**Common misuse:** Dismissing small topology errors as negligible without checking their cumulative effect on area totals or downstream analysis.

### Geocoding match type
The precision level of a geocoded address point — rooftop (highest precision), street-interpolated (estimated position along a street segment), or ZIP/area centroid (lowest precision) — reflecting how accurately the point represents the actual address location.
**In use:** "This dataset is mostly ZIP-centroid matched, which isn't precise enough for the parcel-level proximity analysis being requested."
**Common misuse:** Treating all geocoded points as equally precise regardless of match type, introducing real positional error into analyses that require fine-grained accuracy.

### Spatial overlay / intersection
An analysis operation combining two or more spatial layers to find where their features spatially coincide, commonly used to calculate area of overlap or combined attribute relationships.
**In use:** "The overlay of parcels and flood zones gives us the acreage within the flood risk area."
**Common misuse:** Running an overlay/intersection on datasets with mismatched CRS or uncorrected topology, producing a result that looks like a legitimate calculation but is actually built on misaligned or flawed input geometry.

### Scale / generalization (cartographic)
The level of detail and simplification a dataset was created for, appropriate to its intended display or analysis scale — data generalized for a broad-scale map loses positional precision relevant to a finer-scale analysis.
**In use:** "This dataset was digitized for a national-scale map — it's not precise enough for a parcel-level boundary determination."
**Common misuse:** Using a dataset at a much finer analysis scale than its original generalization level supports, treating simplified approximations as if they carried fine-grained positional accuracy.

### Spatial join
An operation that combines attribute data from one layer to another based on their spatial relationship (e.g., which polygon contains which point), rather than a common key field.
**In use:** "We used a spatial join to attach the flood zone classification to each parcel based on which flood zone polygon it falls within."
**Common misuse:** Running a spatial join on datasets with mismatched CRS, producing incorrect attribute assignments even though the operation appears to complete without error.
