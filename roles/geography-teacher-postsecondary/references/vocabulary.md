# Vocabulary

Terms students and generalists conflate that a geography instructor keeps sharply separate — the value is in the misuse each entry corrects.

## Spatial autocorrelation

The degree to which values at nearby locations are more similar (positive autocorrelation) or more dissimilar (negative autocorrelation) than random chance would produce — formalized by statistics like Moran's I.

**In use:** "Before you trust that regression, check Moran's I on the residuals — if they're still spatially autocorrelated, your standard errors are wrong and the relationship might be an artifact of clustering."

**Common misuse:** treating any visually clustered map pattern as proof of a causal relationship, when spatial autocorrelation is a statistical property of the data that has to be tested for and controlled, not read off a map by eye.

## Modifiable Areal Unit Problem (MAUP)

The finding that statistical results computed on aggregated spatial units (tracts, counties, ZIP codes) can change in strength or even direction depending on how those units are drawn or scaled — a property of the aggregation, not of the underlying phenomenon.

**In use:** "That county-level correlation drops from 0.6 to 0.2 at the tract level — that's MAUP, not evidence the relationship is fake, but evidence it's scale-dependent."

**Common misuse:** assuming a spatial statistic is a fixed, objective property of the data, rather than checking whether it's sensitive to the boundary or scale chosen for aggregation.

## Equal-area projection

A map projection (Albers, Mollweide, Lambert Azimuthal Equal-Area) that preserves relative area at the cost of distorting shape, angle, or distance — the correct choice for any task comparing region sizes.

**In use:** "You're comparing deforestation acreage across three countries — reproject to Albers Equal-Area first, or your area calculations will be wrong, not just the picture."

**Common misuse:** assuming any projection is fine for any task because "it's just how the map looks," when area, shape, distance, and direction cannot all be preserved simultaneously and the wrong choice produces numerically wrong output for measurement tasks.

## Conformal projection

A map projection (Mercator, Lambert Conformal Conic) that preserves local angles and shape at the cost of area — useful for navigation and bearing, actively misleading for area comparison at high latitudes.

**In use:** "Mercator is the right call for a nautical bearing exercise; it's the wrong call for a 'which country is bigger' comparison, since it inflates high-latitude area."

**Common misuse:** using a conformal projection like Mercator as the default classroom basemap for any purpose, without considering that its area distortion actively misleads for the specific comparison being taught.

## Confounding variable

A third variable correlated with both the predictor and the outcome under study, which can produce or inflate an apparent relationship between them that isn't causal.

**In use:** "Impervious surface correlates with both canopy loss and heat — control for it before you claim canopy cover alone explains the temperature difference."

**Common misuse:** treating a strong correlation between two mapped variables as sufficient evidence of a direct causal link, without naming or testing what else varies across the same spatial units.

## Choropleth map

A thematic map that shades predefined areal units (countries, counties, tracts) by the value of a variable — a display technique, not itself a statistical test of relationship between variables.

**In use:** "The choropleth shows both variables trending together across tracts — that's a starting hypothesis for the write-up, not the write-up's conclusion."

**Common misuse:** treating visual co-occurrence of color patterns across two choropleth maps as proof of a statistical or causal relationship, rather than as a prompt to run an actual correlation or confound test.

## Scale (geographic)

The relationship between distance on a map and distance on the ground, and by extension the level of spatial aggregation (local, regional, national, global) at which a phenomenon is analyzed — not a synonym for "map size" or "zoom level."

**In use:** "The migration pattern that looks regional at the state level disappears at the national scale — pick the scale that matches the mechanism you're claiming, not the one that's easiest to map."

**Common misuse:** using "scale" to mean only the map's zoom level or physical size, rather than the analytical decision about what level of spatial aggregation is appropriate to the phenomenon being studied.

## Human geography vs. physical geography

**Physical geography** studies natural systems and processes (climate, landforms, hydrology). **Human geography** studies human systems and their spatial patterns (culture, economy, political organization, urbanization) — graded on different evidentiary standards (data/measurement vs. sourced argument).

**In use:** "Your physical-geography lab needs a reproducible measurement; your human-geography essay needs a sourced argument — don't grade the essay for lacking a p-value."

**Common misuse:** applying the quantitative rigor standard of physical geography (statistical significance, reproducible measurement) as the only valid evidence standard for a human-geography argument that is properly evaluated on sourcing and reasoning instead.

## GIS (Geographic Information System)

Software and data infrastructure for capturing, storing, analyzing, and displaying spatially referenced data — a toolset, not itself an analytical method or a guarantee of correct methodology.

**In use:** "Producing a clean map in ArcGIS doesn't mean the underlying spatial join or projection choice was correct — the software will happily execute a wrong method."

**Common misuse:** treating GIS output as inherently authoritative or correct because it came from professional software, rather than auditing the methodology (scale, projection, data source) that produced it.

## Geopolitics

The study of how geography (territory, resources, borders) shapes and is shaped by political power and international relations — a descriptive analytical frame, not itself a normative position on any specific contested claim.

**In use:** "We're analyzing the geopolitics of the water-rights dispute — that means mapping the competing claims and their stated bases, not adjudicating whose claim is correct."

**Common misuse:** treating "teaching geopolitics" as equivalent to "teaching one side's territorial or resource claim as settled fact," rather than analyzing the structure of the dispute and the sourced positions on each side.
