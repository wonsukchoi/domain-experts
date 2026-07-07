# Zoologist/Wildlife Biologist — Red Flags

### Population estimate reported with no confidence interval
- **Usually means:** the estimate was computed as a simple ratio (raw Lincoln-Petersen or count-based index) without running the variance formula, or the CI was dropped in summarization for a non-technical audience.
- **First question:** "What's the recapture count (R), and did you compute Chapman's variance formula or just the point estimate?"
- **Data to pull:** the raw mark-recapture counts (M, C, R) or the distance-sampling detection-function fit output, and recompute the interval.

### Recapture count (R) under 20 in a two-occasion mark-recapture study
- **Usually means:** the standard Lincoln-Petersen ratio estimator is positively biased, and/or the resulting confidence interval will be too wide to support a precise management threshold.
- **First question:** "Was Chapman's bias correction applied, and does the study design call for a third occasion (Schnabel) to narrow the interval?"
- **Data to pull:** the M, C, R counts and a re-run using Chapman's formula; compare CI width against the decision's required precision.

### Trend claimed from counts spanning multiple years with no documented consistent effort
- **Usually means:** survey method, timing, trap type, or observer coverage changed across years, and the apparent trend may be a measurement artifact rather than a real population change.
- **First question:** "Was survey effort (trap-nights, transect length, timing) held constant across all years being compared?"
- **Data to pull:** the effort log (dates, method, personnel, coverage area) for each year in the comparison.

### Mark-recapture study spanning a season with known breeding or migration activity
- **Usually means:** the closed-population assumption is violated — births, deaths, or movement between occasions will bias a Lincoln-Petersen/Schnabel closed estimator.
- **First question:** "Does the survey window fall inside or outside the species' breeding/migration season, and was closure explicitly tested?"
- **Data to pull:** the species' life-history calendar and the survey date range; if closure is violated, flag for re-analysis with an open-population model.

### Habitat-suitability model output cited as a population or carrying-capacity estimate
- **Usually means:** the model predicts relative suitability of habitat, not abundance or carrying capacity — using it as a direct population proxy overstates confidence in a number the model was never built to produce.
- **First question:** "Has this suitability output been ground-truthed against actual occupancy or abundance data at a sample of sites?"
- **Data to pull:** field survey data from a stratified sample of predicted-suitability classes (high/moderate/low).

### PVA extinction probability reported without stating the vital-rate data window
- **Usually means:** the simulation's inputs come from a short observation period being projected far beyond that window, and the confidence in the output is overstated relative to how far the extrapolation runs.
- **First question:** "How many years of vital-rate data feed this model, and how far forward is the simulation projected relative to that?"
- **Data to pull:** the vital-rate source data (years, sample sizes, CIs) and the simulation horizon.

### IUCN Red List Criterion A (population reduction) applied to a trend under 3 generations or 10 years
- **Usually means:** the trend window is shorter than the criterion's intended timeframe, and short-window trends are prone to being driven by a single anomalous year rather than a sustained decline.
- **First question:** "How many years or generations does the trend data span, relative to the 3-generation/10-year threshold?"
- **Data to pull:** the full time series of survey estimates and the species' generation-time estimate.

### High modeled habitat suitability paired with confirmed low occupancy, and the response is to recalibrate the model
- **Usually means:** a real biotic or dispersal constraint (competition, disease, barrier) is being treated as model noise instead of investigated as a finding.
- **First question:** "Has a competing species, disease presence, or dispersal barrier been checked at the unoccupied high-suitability sites before adjusting the model?"
- **Data to pull:** camera-trap, competitor-survey, or barrier-mapping data at the discrepant sites.

### Distance-sampling detection function fit to fewer than ~60-80 total detections
- **Usually means:** the detection function (and resulting density estimate) has a wide, potentially unstable confidence interval, even if the point estimate looks precise.
- **First question:** "What's the total detection count across all transects, and what's the CV on the fitted detection function?"
- **Data to pull:** the raw detection distances and the model-fit diagnostics (AIC comparison across candidate detection functions, CV of the density estimate).

### A single-visit occupancy survey reported as presence/absence with no repeat-visit detection correction
- **Usually means:** a "not detected" result is being read as "absent" when it may simply reflect imperfect detection on that one visit.
- **First question:** "How many repeat visits were made to each site, and was an occupancy model with detection probability applied?"
- **Data to pull:** the visit-by-visit detection history per site.
