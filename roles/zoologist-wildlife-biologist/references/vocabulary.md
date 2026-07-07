# Zoologist/Wildlife Biologist — Vocabulary

### Closure assumption
The requirement that a surveyed population have no births, deaths, immigration, or emigration during the sampling period, so that the same fixed set of individuals is being sampled on each occasion.
**In use:** "The closure assumption holds here — 10 days is nothing against this species' 20-year generation time."
**Common misuse:** treated as automatically satisfied by a "short" survey window, without checking that window against the species' actual movement rate or breeding calendar.

### Detection probability
The chance that an individual present at a site is actually detected by the survey method used, always less than 1.
**In use:** "Raw count of 40 isn't the population — detection probability came out around 0.6, so the corrected estimate is closer to 65."
**Common misuse:** ignored entirely, treating a raw count as if detection probability were 1.

### Mark-recapture
A method for estimating population size by marking a sample of individuals, releasing them, then resampling and observing what fraction of the second sample bears marks.
**In use:** "We ran a two-occasion mark-recapture; recapture rate was low enough that Chapman's correction mattered."
**Common misuse:** applying the simple ratio estimator (N̂ = MC/R) as if it were unbiased at any sample size, when it's known to be positively biased at small R.

### Lincoln-Petersen estimator
The basic two-sample mark-recapture population estimator: N̂ = MC/R, assuming a closed population and equal catchability.
**In use:** "Lincoln-Petersen gives 340, but with R this small we should report Chapman's corrected 330 instead."
**Common misuse:** used without checking the closure and equal-catchability assumptions, or without the bias correction at small sample sizes.

### Chapman's correction
A modified mark-recapture estimator, N̂ = [(M+1)(C+1)/(R+1)] − 1, that reduces the positive bias of the raw Lincoln-Petersen estimator, especially important at low recapture counts.
**In use:** "With only 19 recaptures, we used Chapman's formula, not raw Lincoln-Petersen."
**Common misuse:** treated as interchangeable with Lincoln-Petersen at any sample size, when the correction matters most exactly where analysts are tempted to skip it.

### Open-population model (Jolly-Seber)
A mark-recapture framework that allows for births, deaths, immigration, and emigration between sampling occasions, used when the closure assumption doesn't hold.
**In use:** "Given the breeding-season overlap, we switched from Lincoln-Petersen to a Jolly-Seber open model."
**Common misuse:** treated as strictly "more advanced" rather than as the required model whenever closure is violated — using a closed-population model on an open population isn't a simplification, it's a wrong answer.

### Distance sampling
A survey method that records the perpendicular distance from a transect line (or point) to each detected individual, using the pattern of detection distances to estimate the probability of detection and correct density estimates.
**In use:** "Distance sampling let us estimate density without assuming we saw every animal near the transect."
**Common misuse:** perpendicular distances not recorded or estimated, collapsing the method to a simple strip count with an assumed (and usually wrong) 100% detection rate.

### Occupancy modeling
A statistical framework estimating the probability a site is occupied by a species while separately estimating detection probability, using repeat visits to the same sites.
**In use:** "One visit isn't enough — we need repeat visits to separate 'not detected' from 'absent' in the occupancy model."
**Common misuse:** single-visit surveys reported as occupancy data, conflating non-detection with absence.

### Population viability analysis (PVA)
A simulation-based method projecting a population's trajectory and extinction risk forward in time using estimated vital rates (survival, fecundity) and their variability.
**In use:** "The PVA puts quasi-extinction probability at 14% over 50 years, but that's sensitive to the juvenile-survival estimate."
**Common misuse:** presented as a confident forecast rather than a projection whose reliability degrades the further it's run beyond the observed data window.

### Habitat suitability model
A statistical model (e.g., MaxEnt) predicting the relative suitability of locations for a species based on environmental variables and known occurrence points.
**In use:** "The suitability model flags this valley as high-quality habitat, but we haven't ground-truthed occupancy there yet."
**Common misuse:** treated as a direct prediction of abundance, occupancy, or carrying capacity rather than a relative suitability surface that still needs field validation.

### Effective sample size
In mark-recapture or distance sampling, the number of independent detections or recaptures actually driving the precision of an estimate — not the same as total effort or total individuals handled.
**In use:** "We handled 200 turtles total, but effective sample size for the estimator is the 19 recaptures, and that's what's driving the wide CI."
**Common misuse:** conflated with total captures or total survey effort, obscuring how little data is actually informing the estimate's precision.

### Quasi-extinction threshold
A population size set as a functional extinction point for management purposes (e.g., below which recovery is considered biologically unlikely), used as the target threshold in a PVA rather than literal zero.
**In use:** "PVA output is probability of falling below the quasi-extinction threshold of 50, not literal extinction."
**Common misuse:** confused with true extinction (N=0), understating the risk being modeled — a population can be functionally doomed well above zero individuals.

### IUCN Red List criteria
A structured set of quantitative thresholds (Criteria A through E) used to assign a species' extinction-risk category, based on population size, trend, range, and other factors.
**In use:** "Under Criterion A, a population reduction over 3 generations or 10 years, whichever is longer, is the relevant window — our 2-year data doesn't qualify."
**Common misuse:** applied to short trend windows that don't meet the criterion's minimum timeframe, producing a risk category the data doesn't actually support.

### Coefficient of variation (CV)
A standardized measure of an estimate's precision — the standard error divided by the estimate itself, allowing comparison of precision across estimates of different magnitudes.
**In use:** "Target CV for this survey was 20%; we came in at 15%, so the design met its precision goal."
**Common misuse:** survey effort planned around "enough detections" without a stated target CV, making it impossible to know in advance whether the resulting estimate will be precise enough for the decision it's meant to inform.
