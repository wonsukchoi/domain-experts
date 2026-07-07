# Hydrologist — Red Flags

### Design flood reported as the historical maximum on record, with no return period stated
- **Usually means:** whoever pulled the number skipped the frequency analysis and just reported the biggest value in the gage record.
- **First question:** "What return period does this number correspond to?" — if there's no answer, the number isn't usable for a regulatory design.
- **Data to pull:** the full annual peak-flow series and run (or request) a Log-Pearson Type III fit.

### Station skew used alone with fewer than ~25 years of record
- **Usually means:** the analyst didn't apply Bulletin 17C's weighted-skew procedure, producing a noisy tail estimate.
- **First question:** "Was the skew weighted against the regional skew study, and what's the effective record length behind the regional value?"
- **Data to pull:** the state or USGS regional skew map/study and its documented mean-square error.

### Water balance residual (P - ET - Q - ΔS) exceeds ~10% of precipitation with no explanation
- **Usually means:** an error in the ET estimate (the hardest term to measure directly) or an unaccounted groundwater inflow/outflow across the basin boundary.
- **First question:** "Which term has the least direct measurement support?"
- **Data to pull:** the ET data source and method, and a check for interbasin groundwater flow potential from the regional geology.

### Transmissivity or storativity reported without the type-curve match-point values
- **Usually means:** the number came from software output without the analyst verifying the match, or the early-time/boundary effects weren't screened out.
- **First question:** "What u and W(u) match point, or what straight-line slope, produced this number?"
- **Data to pull:** the raw drawdown-vs-time data and the fitted type curve or straight-line plot.

### A single K (hydraulic conductivity) value applied across an entire basin or model domain
- **Usually means:** only one aquifer test exists and its result was extended beyond what the test can support, or the model wasn't zoned by lithology.
- **First question:** "How many tests inform this K value, and what's the lithologic basis for extending it spatially?"
- **Data to pull:** all available aquifer-test locations and results, plus a geologic/lithologic map of the domain.

### Curve Number (SCS-CN) method applied to a watershed over roughly 5-10 square miles or with highly variable antecedent moisture
- **Usually means:** CN was chosen for convenience rather than appropriateness — CN was developed and validated on small, relatively homogeneous agricultural watersheds.
- **First question:** "Was a continuous or event-based calibrated model considered, and why was CN chosen instead?"
- **Data to pull:** drainage area, land-use heterogeneity, and any available calibration data (gage record) for the basin.

### "Fully allocated" water rights presented as equivalent to "no water physically available"
- **Usually means:** a legal-allocation number is being conflated with a hydrologic-availability number.
- **First question:** "What does the actual gage record show for flow in a representative year, independent of the paper rights?"
- **Data to pull:** the water-rights priority list with decreed quantities and priority dates, separately from the streamflow record.

### Confidence interval on a flood-frequency estimate not reported, especially for return periods beyond 2-3x the period of record
- **Usually means:** the deliverable presents a point estimate as if it were exact, hiding how much extrapolation uncertainty is in play.
- **First question:** "What's the 90% (or 95%) confidence interval on this estimate, and how does it compare to the period of record?"
- **Data to pull:** the frequency-analysis software's confidence-limit output or a manual calculation per Bulletin 17C Appendix guidance.

### Hydrograph shape matches visually but no mass-balance closure check was performed
- **Usually means:** the model is calibrated with compensating errors — e.g., an overestimated infiltration parameter offset by an underestimated baseflow contribution.
- **First question:** "Does the modeled water balance close within a few percent over the simulation period?"
- **Data to pull:** the model's simulated P, ET, Q, and storage-change outputs summed over the full period.

### Regional regression equation applied outside its documented range of drainage area or physiographic region
- **Usually means:** the analyst used a convenient equation without checking its applicability limits, which are usually stated explicitly in the source study.
- **First question:** "Does this site's drainage area and physiographic setting fall inside the regression equation's calibration range?"
- **Data to pull:** the source regional regression study (often a USGS Scientific Investigations Report) and its stated range of applicability.
