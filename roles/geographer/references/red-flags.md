# Red flags

Smell tests before a spatial analysis, choropleth map, or spatial regression ships.

### Moran's I on regression residuals significant (|z| > 1.96) but the model was reported as plain OLS

**Usually means:** the response variable carries spatial structure the model didn't account for, so the reported standard errors and p-values are too optimistic.
**First question:** "Did you test the residuals for autocorrelation, or only the raw dependent variable?"
**Data to pull:** the OLS residual table, the spatial weights matrix definition used, and the LM-lag/LM-error diagnostic output.

### A choropleth mapped from raw counts instead of a rate

**Usually means:** larger-population units will look worse (or better) purely because they have more people, not because the underlying per-capita phenomenon is more prevalent there.
**First question:** "Is this normalized by population or area, or is it a raw count map?"
**Data to pull:** the denominator (population, area, or households) used, and the resulting rate for the 2-3 largest-population units to check the raw-count map's ranking flips once normalized.

### A rate is published from fewer than roughly 20 events in a small-population unit, with no smoothing disclosed

**Usually means:** the rate's sampling variance likely exceeds the true geographic signal — one additional or one fewer event would swing the published rate by double digits of percent.
**First question:** "What's the event count behind this unit's rate, and was any empirical Bayes or age-adjustment smoothing applied?"
**Data to pull:** raw event count and population per unit; the smoothed rate if computed, for comparison against the raw one.

### The same variable's correlation or significance flips sign or disappears when computed at a different areal aggregation

**Usually means:** a Modifiable Areal Unit Problem (MAUP) scale or zoning effect, not a change in the underlying geographic process.
**First question:** "Has this been re-run at a second aggregation level (e.g., census tract vs. county), and does the finding hold?"
**Data to pull:** the statistic recomputed at 2+ aggregation levels side by side.

### Quantile classification used on data with one clearly larger gap than the rest

**Usually means:** the classification method is forcing an equal count per class regardless of where the data's real breaks fall, merging dissimilar units into one class or splitting a natural cluster across two.
**First question:** "What's the goodness-of-variance-fit (GVF) for Jenks natural breaks at the same class count, compared to quantile?"
**Data to pull:** the sorted raw values, the class breakpoints under both methods, and each method's GVF.

### A thematic map spanning a wide latitude range is rendered in Web Mercator

**Usually means:** the map's default basemap projection was never reconsidered for the analytical (as opposed to navigational/web-tile) use case, and area comparisons across the map's latitude range are visually biased.
**First question:** "What's the map's latitude range, and is area comparison part of what the reader is meant to take away?"
**Data to pull:** the projection's areal scale factor (1/cos²φ for Web Mercator) at the map's northernmost and southernmost extent.

### An area-level finding is stated using individual-level language ("residents of high-poverty tracts are more likely to...")

**Usually means:** an ecological-fallacy overreach — the data available is area-aggregate, not individual, and the causal/associative claim being made requires individual-level data that wasn't used.
**First question:** "Is there individual-level (not area-aggregate) data backing this specific sentence, or is this an inference from an area-level correlation?"
**Data to pull:** the unit of observation actually used in the analysis (individual records vs. tract/county aggregates).

### A "hot spot" is claimed from a kernel density map alone, with no permutation or Gi* significance test run

**Usually means:** the visual density peak may be within the range a random point pattern of the same n would produce — KDE surfaces are visually persuasive regardless of statistical significance.
**First question:** "Was a Getis-Ord Gi* or Monte Carlo permutation test run on this pattern, or is the hot spot call based on the density surface's color ramp alone?"
**Data to pull:** the Gi* z-scores (or permutation p-values) for the specific location named as a hot spot.

### A Getis-Ord Gi* z-score between -1.96 and +1.96 is labeled a hot or cold spot on a published map's legend

**Usually means:** the map's classification bins (often a default 3- or 5-class "cold/neutral/hot" scheme) don't align with the actual statistical significance threshold, so non-significant units get colored as if they were confirmed clusters.
**First question:** "What z-score range does each color bin actually correspond to, and does the 'hot'/'cold' bin boundary sit at ±1.96 or somewhere else?"
**Data to pull:** the full Gi* z-score table alongside the map's legend bin definitions.

### A global regression coefficient is reported when a LISA or GWR surface shows the relationship's sign or magnitude visibly differs by region

**Usually means:** spatial non-stationarity — one global coefficient is averaging over relationships that are actually different in different places, and the average may not describe any specific place well.
**First question:** "Has a geographically weighted regression been run to check whether this coefficient's sign or magnitude is stable across the study area?"
**Data to pull:** the GWR local coefficient surface (or a LISA map of the residuals) alongside the global model's single coefficient.

### Census/ACS tract-level data from two different years is compared directly without checking for tract boundary redefinition

**Usually means:** the Census Bureau periodically redraws tract boundaries between decennial censuses; a tract-to-tract comparison across a boundary-change year is comparing two different areal units, not tracking the same place over time.
**First question:** "Did the tract boundaries change between these two years, and if so, was a crosswalk or area-weighted reallocation applied?"
**Data to pull:** the Census Bureau's relationship/crosswalk file for the two vintages being compared.
