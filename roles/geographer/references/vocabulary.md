# Vocabulary

Terms generalists flatten together or misuse when discussing spatial analysis.

## Tobler's First Law

The observation that "everything is related to everything else, but near things are more related than distant things" — the foundational reason spatial data violates the independence assumption of classical statistics.

*In use:* "We can't treat these county rates as i.i.d. observations — Tobler's First Law is exactly why we ran Moran's I before the regression."

*Common misuse:* citing it as a vague justification for "spatial things matter" rather than as the specific reason independence-assuming statistical tests are inappropriate on unadjusted spatial data.

## Spatial autocorrelation / Moran's I

The tendency of a variable's value at one location to correlate with its value at nearby locations. Moran's I is the standard global test statistic, ranging roughly from -1 (perfect dispersion) to +1 (perfect clustering), with an expected value of -1/(n-1) under the null of no spatial pattern.

*In use:* "Global Moran's I came back at 0.27 against an expected -0.14 — that's real positive autocorrelation, not just visual clustering."

*Common misuse:* treating any positive Moran's I value as automatically "significant" without checking it against a permutation test or the expected value under the null, or treating a significant global I as telling you *where* the clusters are (it doesn't — that's what LISA/Gi* are for).

## Modifiable Areal Unit Problem (MAUP)

The finding that statistical results computed from spatially aggregated data (correlations, rates, regression coefficients) change depending on how the study area is partitioned into units — both the *zoning effect* (different boundary configurations at the same number of zones) and the *scale effect* (different numbers/sizes of zones).

*In use:* "The county-level correlation was 0.6, but at the census-tract level it dropped to 0.2 — that's MAUP, and it means the county-level number isn't a robust finding on its own."

*Common misuse:* treating MAUP as an obscure edge case rather than a default expectation for any aggregated spatial statistic — it should be tested, not assumed away.

## Ecological fallacy

The error of inferring an individual-level relationship from an area-level (aggregate) correlation. A strong area-level correlation between two variables does not establish that the same relationship holds for individuals within those areas.

*In use:* "The county-level correlation between income and mortality doesn't tell us that poor individuals in that county are the ones dying — that's the ecological fallacy, we'd need individual-level records to say that."

*Common misuse:* using it interchangeably with "MAUP" — MAUP is about aggregation *choice* changing results; ecological fallacy is about the *level of inference* being wrong regardless of which aggregation was used.

## LISA (Local Indicators of Spatial Association)

A local, unit-by-unit decomposition of a global spatial autocorrelation statistic (Anselin 1995), classifying each unit as High-High, Low-Low, High-Low, or Low-High relative to its neighbors, each with its own significance test.

*In use:* "Run a LISA cluster map before naming specific counties — global Moran's I tells you clustering exists, LISA tells you which counties are actually significant."

*Common misuse:* reading every colored unit on a LISA map as individually significant without checking that unit's own p-value/z-score — adjacency to a significant cluster doesn't make a unit itself significant.

## Getis-Ord Gi*

A local statistic that tests whether the sum of a variable's values within a unit's neighborhood (including the unit itself) is significantly higher or lower than expected under spatial randomness, expressed as a z-score. The standard hot/cold-spot mapping statistic when the outcome variable is expected to concentrate (e.g., disease counts, crime, retail sales) rather than merely correlate.

*In use:* "Gi* z of 2.19 at County F clears the 95% threshold — that's a confirmed hot spot, not just a visually dark county."

*Common misuse:* using Gi* and Moran's I interchangeably — Moran's I is a single global test of overall clustering; Gi* is a per-unit local test that tells you which specific units are hot or cold.

## Jenks natural breaks / goodness-of-variance-fit (GVF)

A classification method (Jenks 1967) that chooses class boundaries to minimize within-class variance and maximize between-class variance, i.e., it finds the data's real gaps. GVF = (SDAM - SDCM)/SDAM quantifies how well a given classification explains the total variance (SDAM = total sum of squared deviations from the overall mean; SDCM = summed within-class sum of squared deviations); GVF near 1.0 is a strong fit.

*In use:* "Jenks at k=3 gives a GVF of 0.994 versus quantile's 0.776 at the same class count — Jenks is finding this dataset's real structure, quantile is imposing an arbitrary equal-count split."

*Common misuse:* treating "natural breaks" as a method-agnostic descriptive phrase rather than the specific Jenks optimization; also failing to report GVF, which is the actual evidence the classification fits the data.

## Kernel density estimation (KDE)

A method for converting a discrete set of point locations into a continuous density surface by summing a kernel function (typically Gaussian) centered on each point, producing smoother, more visually interpretable hot-spot surfaces than raw point counts or fixed-grid binning.

*In use:* "The KDE surface peaks right at the 340-380m cluster on the corridor — but re-run it at half and double the bandwidth before we name that segment, the peak's exact location is bandwidth-sensitive."

*Common misuse:* treating the density surface as inherently statistically significant — KDE describes *where* density is high, it doesn't by itself test whether that density is higher than a random point pattern would produce (that requires a separate significance test, e.g., a permutation-based hot-spot test).

## Bandwidth (kernel/KDE and GWR)

The distance parameter controlling how much smoothing a kernel-based method applies — how far a point's influence extends in KDE, or how large a local neighborhood is used to fit each local coefficient in geographically weighted regression (GWR).

*In use:* "Silverman's rule of thumb gives us h ≈ 193m for this point set — that's our starting bandwidth, sensitivity-check it at 0.5h and 2h."

*Common misuse:* picking a bandwidth by eye to make the output "look right" rather than via a defensible rule (Silverman's rule of thumb for KDE; cross-validated AICc for GWR) — the bandwidth choice materially changes where clusters or local coefficients appear.

## Geographically weighted regression (GWR)

A local form of regression that fits a separate set of coefficients at every location, weighted by nearby observations, revealing whether a relationship's sign or strength varies across the study area (spatial non-stationarity) rather than assuming one global coefficient applies everywhere.

*In use:* "The global OLS coefficient says income and mortality are weakly related, but the GWR surface shows that relationship is strongly negative in the rural counties and near zero in the urban ones — the global number was averaging over two different local stories."

*Common misuse:* running GWR as a default upgrade from OLS without first checking whether non-stationarity is actually present (via a LISA/Gi* map of the OLS residuals or a GWR-vs-OLS model comparison) — GWR trades interpretability and sample size per local estimate for local specificity, and isn't free.

## Tissot's indicatrix

A device for visualizing map projection distortion: a small circle of constant true-earth radius, drawn at multiple points across a projection, that appears as an ellipse where the projection distorts shape and/or area — its shape and size at any point shows exactly what that projection is distorting there.

*In use:* "Plot the Tissot indicatrix for both candidate projections before picking one — it'll show exactly where each one trades shape for area."

*Common misuse:* assuming a projection is "basically fine" without checking how its distortion varies across the specific study area's extent — a projection acceptable at the equator can be badly distorted at the latitudes actually being mapped.

## Equal-area vs. conformal projection

An equal-area projection (e.g., Albers Equal-Area Conic) preserves true relative area at the cost of shape/angle distortion away from its standard lines; a conformal projection (e.g., Web Mercator, Lambert Conformal Conic) preserves local shape and angles at the cost of area distortion that grows with distance from its standard lines. No projection does both (Gauss's Theorema Egregium).

*In use:* "This is a choropleth where area comparison is the whole point — equal-area, not conformal, even though conformal is what the web basemap defaults to."

*Common misuse:* using a conformal web-tile basemap (Web Mercator) as the default projection for a thematic/statistical map without checking whether the map's argument depends on area, distance, or shape being preserved.

## Empirical Bayes rate smoothing

A method for stabilizing rates computed from small event counts by shrinking each unit's raw rate toward the overall (global) mean, weighted by how much the estimated between-unit variance exceeds that specific unit's own sampling variance — units with few events shrink more; units where true geographic variation dominates sampling noise shrink less.

*In use:* "County D's raw rate of 15 only smooths to 20.6 after empirical Bayes — the between-county variance here is large enough that the low rate looks like a real pattern, not just three deaths' worth of noise."

*Common misuse:* assuming smoothing always pulls small-count rates heavily toward the mean — the shrinkage weight depends on the ratio of between-to-within variance, and a dataset with large true geographic variation will preserve small-area extremes rather than erasing them.

## Spatial lag vs. spatial error model

Two ways to extend regression to spatially autocorrelated data. A spatial lag model includes neighboring observations' *dependent variable* values as a regressor (models diffusion/spillover in the outcome itself). A spatial error model puts the spatial dependence in the error term (models an unobserved, spatially structured omitted variable). Lagrange Multiplier diagnostics on the OLS residuals indicate which fits better.

*In use:* "Robust LM-lag is significant and robust LM-error isn't, so we're fitting a spatial lag model — the outcome itself looks like it's diffusing across county lines."

*Common misuse:* choosing between the two based on which one is easier to interpret rather than which one the LM diagnostics actually support — the two models encode different causal stories about *why* the autocorrelation exists.
