# Red Flags

Smell tests for population projections, rate comparisons, and small-area estimates. Format per flag: what it usually means, the first question to ask, the check to run.

### A multi-decade population projection built by extrapolating a single 5-year growth rate forward

- **Usually means:** the base period's growth rate includes a one-time driver (a migration surge, a base closure, a large development coming online) that won't repeat, and the age structure behind that growth is about to change.
- **First question:** "What was actually driving that growth rate — was it births, deaths, or migration, and is that specific driver expected to continue?"
- **Data to pull:** the cohort-component decomposition (births/deaths/migration) for the base period, not just the topline growth percentage.

### Total population reported as growing while no age-band breakdown is shown

- **Usually means:** the growth is concentrated in one or two cohorts (commonly working-age in-migration) while a decision-relevant cohort (school-age, elderly) is flat or declining — the aggregate number is hiding the answer the client actually needs.
- **First question:** "Which age bands are driving this growth number, and is the one my decision depends on among them?"
- **Data to pull:** the full age-band table for both the base year and the projection year, not just the total.

### A year-over-year change reported for a small city, tract, or ZIP using ACS 1-year estimates

- **Usually means:** the reported change is smaller than the estimate's own margin of error, so the "trend" is statistical noise from the survey's sampling design, not a real shift.
- **First question:** "What's the margin of error on each of these two estimates, and does the difference between them exceed the combined MOE?"
- **Data to pull:** the ACS estimate and MOE for both years; switch to the 5-year pooled estimate if the geography is under roughly 65,000 population (the threshold below which 1-year ACS estimates aren't published).

### Sub-replacement TFR cited as evidence the population is about to decline

- **Usually means:** the analysis is ignoring population momentum (the existing age structure's large not-yet-childbearing cohort) and/or net migration, both of which can keep a sub-replacement-fertility population growing for decades.
- **First question:** "What's net migration doing, and how does the current age structure compare to a stationary population's?"
- **Data to pull:** net migration by age band for the geography, and the current population pyramid shape versus a stable-population reference.

### Crude death (or birth) rate compared across two places or time periods with very different age structures

- **Usually means:** the comparison is conflating an actual rate difference with an age-structure difference — an older population has a higher crude death rate even at identical age-specific mortality.
- **First question:** "Has this been age-standardized, and against what reference population?"
- **Data to pull:** age-specific rates for both populations and a standard reference population (e.g., the 2000 US standard population) to compute standardized rates or an SMR.

### Births, deaths, and migration estimates that don't reconcile against the next decennial or postcensal control total

- **Usually means:** at least one component estimate (most often net migration, the hardest to measure directly) is off, and the discrepancy is being silently absorbed rather than reported.
- **First question:** "Does births minus deaths plus estimated migration equal the independently measured population change — and if not, what's the residual?"
- **Data to pull:** the vital-statistics births/deaths series, the migration estimate, and the control-total population change for the same period; compute and report the residual explicitly.

### An undercount or overcount claim for a specific subgroup based on a single enumeration

- **Usually means:** a single count has no internal way to reveal its own coverage error — the claim needs an independent cross-check, not just a comparison against expectations.
- **First question:** "What's the dual-system or demographic-analysis estimate for this subgroup, and does it corroborate the claimed under/overcount?"
- **Data to pull:** Census Coverage Measurement or demographic-analysis results for the relevant geography and demographic group, if available.

### A population projection presented as a single point number with no scenario range

- **Usually means:** the deliverable is hiding how sensitive the conclusion is to the fertility, mortality, or (usually largest source of error) migration assumption behind it.
- **First question:** "What does this number look like under a low- and high-migration scenario, and does the decision change between them?"
- **Data to pull:** the same cohort-component run with the migration (and, if relevant, fertility) assumption varied to a plausible low/high bound.

### The last decennial census count used as "current population" more than 2–3 years after the census

- **Usually means:** the analysis is using a stale count instead of the current vintage postcensal estimate, which matters most in fast-growing or fast-declining geographies where the gap compounds quickly.
- **First question:** "Is this the decennial count or the current-vintage postcensal estimate?"
- **Data to pull:** the Census Bureau Population Estimates Program's latest vintage estimate for the geography.
