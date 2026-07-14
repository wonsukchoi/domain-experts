# Red flags

Smell tests an experienced geography instructor catches early. Format: what it usually means, the first question to ask, the data to pull.

## 1. A spatial-analysis write-up reports |r| > 0.6 between two mapped variables and states a causal conclusion

**Usually means:** a confound variable drives both mapped patterns and was never tested — the strongest common case is a third variable correlated with both (impervious surface, elevation, income) that the student didn't think to control for.

**First question:** "What third variable, also mapped across these same units, could explain both patterns at once?"

**Data to pull:** the correlation matrix for any other available variable against both the predictor and outcome; a partial correlation or regression controlling for the top confound candidate.

## 2. A student computes area, distance, or density directly from unprojected (WGS84 / EPSG:4326) coordinates

**Usually means:** the software's default coordinate system was never changed before a calculation that requires a projected system — area and distance are numerically wrong, not just visually distorted, when computed in geographic (degree-based) coordinates.

**First question:** "What coordinate reference system was active when this area/distance was calculated, and is it a projected or geographic system?"

**Data to pull:** the layer's CRS metadata; a recomputation of the same figure in an appropriate projected system (state plane, UTM, or an equal-area projection) for comparison.

## 3. A classroom or assignment map uses a Mercator base layer for anything other than navigation

**Usually means:** the default web-map basemap (Web Mercator, EPSG:3857) was used for a thematic or area-comparison map without considering that Mercator inflates high-latitude area — Greenland reads as continent-sized next to Africa despite being about 1/14th its area.

**First question:** "Is this map being used to compare area or shape, or to navigate/show direction? If area or shape, why is this projection appropriate?"

**Data to pull:** the map's stated or default projection; the true relative areas of the two most visually distorted features on the map.

## 4. A GIS lab is graded primarily on the final map's visual polish

**Usually means:** the rubric weights output aesthetics over the methodology that produced it, rewarding a well-designed map built on the wrong scale, an unjustified projection, or a stale dataset.

**First question:** "Walk me through why this scale, this projection, and this dataset vintage were chosen for this specific question."

**Data to pull:** the rubric's point allocation across methodology vs. output categories; the dataset's citation and vintage; the projection used for any measurement task.

## 5. A demographic dataset cited in an assignment is more than one ACS 5-year release behind current

**Usually means:** a default download from an old tutorial, cached file, or prior semester's lab kit was reused without checking for a newer release.

**First question:** "What vintage is this dataset, and does the assignment's claim depend on data being current?"

**Data to pull:** the dataset's release year/vintage field; the current ACS 5-year release date; whether the assignment is a historical-change study (where the old vintage may be intentional) or a current-conditions claim.

## 6. A spatial-statistics result changes direction or magnitude noticeably when the unit of analysis changes (tract vs. county vs. ZIP)

**Usually means:** the Modifiable Areal Unit Problem — the statistical relationship is sensitive to the arbitrary boundary/scale chosen, not a robust underlying pattern.

**First question:** "Does this relationship hold up if we re-run it at one coarser and one finer spatial unit?"

**Data to pull:** the same statistic recomputed at county level and at a finer sub-tract or block-group level; the original unit's boundary-drawing rationale.

## 7. A lesson on a contested geopolitical topic (border dispute, resource-rights conflict, migration policy) cites sources from only one side

**Usually means:** the reading list defaults to whichever sources were easiest to find or most familiar to the instructor, rather than a deliberate balance of sourced positions.

**First question:** "Whose perspective is missing from this reading list, and can I name a specific credible source representing it?"

**Data to pull:** the assigned source list with each source's institutional or national origin; whether any assigned source explicitly represents the competing position.

## 8. A student's GIS project scores near-identical high marks on quantitative output and qualitative interpretation despite the assignment being GIS-heavy

**Usually means:** the interpretive-writing component was graded against the same generous rubric as the technical output, rather than assessed on its own analytical merit — common when a rubric wasn't built with separate criteria for the two skills.

**First question:** "If I strip out the map and statistics, does the written interpretation stand on its own as geographic reasoning?"

**Data to pull:** the rubric's separate (or merged) criteria for technical output vs. written interpretation; the written section graded blind to the map's quality.

## 9. A student's map or dataset carries no source citation or attribution at all

**Usually means:** the data was pulled from a quick web search or an unlicensed scrape rather than a documented, citable source (Census, USGS, a named GIS data portal) — a downstream provenance problem for any conclusion drawn from it.

**First question:** "Where did this dataset come from, and can you produce the original source page or metadata record?"

**Data to pull:** the dataset's metadata file or portal citation; whether the license permits classroom/academic use.
