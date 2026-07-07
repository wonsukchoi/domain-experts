# Geoscientist — Red Flags

### Reserve figure reported without an SPE-PRMS category (1P/2P/3P)
- **Usually means:** the analyst is reporting a single deterministic number where a probabilistic range belongs, or is deliberately obscuring low confidence behind a clean-looking figure.
- **First question:** "Is this 1P, 2P, or 3P — and what well/production density supports that category?"
- **Data to pull:** the well-control map for the compartment and any production or pressure-test history.

### Correlation panel built from only two wells with no seismic tie
- **Usually means:** the tie is one plausible hypothesis among several (fault offset vs. facies change vs. simple dip) that hasn't been discriminated yet.
- **First question:** "What third dataset — a third well, seismic, or a laterally traceable marker — would confirm or break this tie?"
- **Data to pull:** any available seismic line crossing the interval; nearby well data even if outside the immediate compartment.

### Porosity averaged across the full gross logged interval, no cutoff mentioned
- **Usually means:** net pay hasn't been isolated from non-reservoir shale/tight streaks, inflating the volumetric.
- **First question:** "What porosity and Vshale cutoffs were applied before this average was computed?"
- **Data to pull:** the raw log curves and the cutoff parameters used (or absent).

### Recovery factor cited without naming its source
- **Usually means:** it's borrowed from an analog field and being presented as if compartment-specific.
- **First question:** "Which analog field, and does its drive mechanism and rock quality actually match this compartment?"
- **Data to pull:** the analog field's production history and reservoir-quality comparison.

### Hazard communication states a recurrence interval as a predicted date ("due for a major event")
- **Usually means:** a probabilistic result is being mis-translated into deterministic language, likely to either alarm or falsely reassure the audience.
- **First question:** "Is this being reported as an annual probability, or as a countdown?"
- **Data to pull:** the original paleoseismic or hydrologic study's stated confidence interval on the recurrence estimate itself.

### Facies model extrapolated across a fluvial or deltaic system from a single core or outcrop
- **Usually means:** lateral continuity is being assumed rather than tested, in an environment known for lateral discontinuity.
- **First question:** "How far from this data point does the model extend, and what supports continuity over that distance?"
- **Data to pull:** any additional wells, outcrop exposures, or seismic amplitude data within the extrapolated area.

### Volumetric estimate used past 12+ months of production without a material-balance cross-check
- **Usually means:** the static model hasn't been reconciled against actual flow behavior, and may be systematically over- or under-stating the reservoir.
- **First question:** "Does the material-balance or decline-curve estimate from production data agree with the volumetric within a reasonable range?"
- **Data to pull:** production history (rate, cumulative volume, pressure) for the compartment.

### Structure map shows a closure with no discussion of fault-seal risk
- **Usually means:** the trap's integrity is assumed rather than evaluated — a mapped closure with a leaking fault seal holds no recoverable volume regardless of how good the volumetric math is.
- **First question:** "What is the fault-seal analysis (shale gouge ratio or juxtaposition) for the bounding fault?"
- **Data to pull:** fault throw and juxtaposition data across the seal, and any offset-well pressure data indicating communication or isolation.

### Water saturation computed with default Archie parameters (a=1, m=2, n=2) with no calibration noted
- **Usually means:** the parameters weren't validated against core data for this specific rock type, which can shift Sw meaningfully in low-porosity or shaly sands.
- **First question:** "Has core data calibrated these Archie parameters for this formation, or are they textbook defaults?"
- **Data to pull:** core-derived cementation exponent (m) and saturation exponent (n) if available.

### Deliverable presents a single point estimate with no stated uncertainty range
- **Usually means:** the probabilistic nature of the underlying geologic model has been stripped out for presentation, misleading the reader into treating it as deterministic.
- **First question:** "What's the P10/P50/P90 range behind this number?"
- **Data to pull:** the Monte Carlo or scenario inputs (if run) or, at minimum, the low/high case parameters used.
