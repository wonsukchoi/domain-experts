# Red flags

Smell tests a mining/geological engineer catches on a first pass over a slope monitoring trend, a ground-control plan, a reserve model, or a ventilation plan.

### Slope prism/radar displacement trending past roughly 2 mm/day with an accelerating (not linear) rate

- **Usually means:** progressive failure has begun and the slope is moving from creep into the accelerating-creep stage the inverse-velocity (Fukuzono) method is built to catch — the linear-to-accelerating transition is the actionable signal, not the absolute displacement.
- **First question:** is the velocity trend linear, decelerating, or accelerating over the last 3–5 readings, and does an inverse-velocity plot project a time-to-failure inside the current mining schedule?
- **Data to pull:** the full displacement time series (not just the latest reading), rainfall/blast timing overlay, and the last geotechnical inspection of tension cracks at the crest.

### Stability sign-off reports a single FS number with no mention of a trial-surface search

- **Usually means:** the analyst ran one assumed circular (or planar) surface instead of letting the software (or a manual search) find the minimum-FS surface, and a lower-FS surface may exist elsewhere in the slope.
- **First question:** how many trial surfaces were searched, and is the reported FS confirmed as the minimum across that search?
- **Data to pull:** the limit-equilibrium output file/summary showing the search grid and the ranked list of trial-surface FS values.

### Ground support pattern unchanged across a mapped geologic domain or structural boundary

- **Usually means:** the RMR/Q classification wasn't re-run at the boundary, and a pattern designed for one domain's rock mass is being carried into a different (often weaker) one without re-justification.
- **First question:** was RMR/Q re-scored on the far side of the boundary, and does the support pattern there still match the resulting class?
- **Data to pull:** the geologic domain map, scanline/cell mapping data on both sides of the boundary, and the support-as-built record.

### Cutoff grade unchanged for more than roughly 2 years despite a metal price move of 20% or more

- **Usually means:** the cutoff was set once at feasibility and never re-optimized, silently sending economic ore to the waste dump (price up, cutoff too high) or uneconomic rock to the mill (price down, cutoff too low).
- **First question:** what price and cost basis was the current cutoff calculated on, and how far has the actual price/cost moved from that basis?
- **Data to pull:** the cutoff-grade calculation sheet (price, recovery, payability, cost inputs) and the current metal price/cost trend.

### Diesel equipment added or upgraded on a heading without a re-run ventilation quantity calculation

- **Usually means:** the airflow requirement was sized to the original equipment fleet, and the added horsepower now exceeds the split's delivered air without anyone re-checking.
- **First question:** what is the combined rated horsepower of diesel equipment now operating in this split, and does the last ventilation survey's measured airflow still clear the 100 cfm/bhp requirement?
- **Data to pull:** current equipment roster with rated horsepower by split, and the most recent anemometer/ventilation survey for that split.

### A slope or pit design more than roughly 2–3 years old with no piezometer coverage in the domain

- **Usually means:** the stability analysis was run dry (or with an assumed ru) because no groundwater data existed, and the assumption has never been checked against measurement.
- **First question:** what pore-pressure assumption underlies the current FS, and is there piezometer data anywhere in the domain (even a nearby one) to sanity-check it?
- **Data to pull:** the geotechnical design report's stated pore-pressure assumption and any piezometer/monitoring well records in or near the domain.

### RMR and Q classifications for the same rock mass disagree by more than about one support class on the standard correlation

- **Usually means:** one of the two ratings was scored inconsistently — most often groundwater condition or joint condition/alteration, the two subjective inputs most prone to rater disagreement.
- **First question:** which specific sub-rating differs most between the two scoring sheets, and does a second mapper's independent rating agree with either one?
- **Data to pull:** both rating sheets with sub-scores itemized, and the mapping geologist's field notes for the disputed parameter.

### Underground opening span increased (widened) without re-checking bolt length against the span-dependent ESR formula

- **Usually means:** the original bolt length was specified for a narrower design span, and L = 2 + 0.15B/ESR increases with span — a wider opening under the old bolt length has less than the design margin.
- **First question:** what span was the current bolt length designed for, and what is the actual as-mined span at the location in question?
- **Data to pull:** the original ground support design basis (span, ESR, calculated L) and as-built survey of actual opening dimensions.

### Mill-reported head grade and block-model-predicted grade diverge systematically (not randomly) by more than roughly 10%

- **Usually means:** either the resource model has a bias (drill-spacing/estimation-method issue, or a domain boundary misplaced) or mining dilution/ore-loss in practice differs from the dilution factor assumed in reserve conversion.
- **First question:** is the divergence one-directional (model consistently over- or under-calls grade) across many stopes/blocks, or randomly scattered — a systematic bias points at the model or the dilution assumption, scatter points at short-term grade control noise.
- **Data to pull:** a reconciliation report (model grade vs. mill-received grade by period) and the dilution/mining-recovery factors used in reserve conversion.

### Radon or methane readings trending upward without a corresponding increase in ventilation quantity

- **Usually means:** gas liberation has increased (advancing into a new zone, increased exposed rock surface, or a ventilation short-circuit) faster than the airflow was adjusted to dilute it.
- **First question:** has the airflow in this split been re-measured since the gas trend started, and does the current dilution still clear the regulatory or internal threshold at the new liberation rate?
- **Data to pull:** the gas monitoring time series, the split's most recent measured airflow, and the ventilation network's current regulator/fan settings for that split.

### Stope or pillar design uses domain-average strength/grade inputs with no flag for known local weak structure (fault gouge, clay seam)

- **Usually means:** the design calculation pulled the average RMR/UCS for the domain rather than the locally weaker value where a mapped fault or clay seam intersects the stope, understating risk at that specific location.
- **First question:** does the stope or pillar in question intersect any mapped structure with a rating materially below the domain average, and was that structure's rating used at that location instead of the domain average?
- **Data to pull:** the structural geology map overlaid on the stope/pillar layout, and the site-specific (not domain-average) rock mass rating at the intersection.
