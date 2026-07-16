# Red Flags

Smell tests for oceanographic data, cruise plans, and public-facing readouts. Format per flag: what it usually means, the first question to ask, the check to run.

### Dissolved oxygen reading drops below 2 mg/L on a single deployed sensor with no bottle sample

- **Usually means:** optode or electrode membrane fouling (biofilm growth over weeks of deployment), which almost always biases low, before it means a real hypoxic event.
- **First question:** "When was this sensor last cross-checked against a Winkler-titrated bottle sample, and how many days has it been in the water since?"
- **Data to pull:** the sensor's deployment log and the last pre-/post-deployment calibration comparison; if none exists in the last ~2–3 weeks, treat the reading as unconfirmed.

### CTD-minus-bottle salinity offset that grows monotonically across a cruise (not scattered around a mean)

- **Usually means:** progressive conductivity-cell fouling, not random noise — a flat cruise-mean correction will under-correct the late casts and over-correct the early ones.
- **First question:** "Does the offset trend with cast number/elapsed day, or is it randomly scattered?"
- **Data to pull:** the full crossover-station table (CTD vs. Autosal salinity, cast number, date) — plot offset against cast number before applying any correction.

### A "bloom" visible in satellite ocean-color imagery with no corroborating in-situ chlorophyll or fluorometry data

- **Usually means:** either a real surface bloom, or a subsurface chlorophyll maximum artifact / atmospheric-correction error near cloud edges — satellite ocean color only sees the first optical depth.
- **First question:** "Is there an in-situ fluorometer or bottle chlorophyll sample from within the same week and area?"
- **Data to pull:** the nearest glider, mooring, or ship fluorescence profile; check mixed-layer depth for that period — a deepening mixed layer can push the real chlorophyll maximum below what the sensor sees.

### A single mooring or float record used to claim a multi-year trend

- **Usually means:** the record is too short to separate a trend from tidal, seasonal, or interannual (ENSO/PDO) variability of comparable magnitude.
- **First question:** "How does the observed anomaly compare in size to the site's own interannual standard deviation, not just to last year's value?"
- **Data to pull:** the longest available co-located time series or the relevant WOA/regional climatology; compute the anomaly in units of historical standard deviation, not raw magnitude.

### Nutrient or productivity conclusion built on a Redfield-ratio (106:16:1 C:N:P) assumption with no limiting-nutrient check

- **Usually means:** the analysis imported a stoichiometric default from a different regime — Redfield doesn't hold in iron- or silicate-limited (HNLC, some coastal upwelling) systems.
- **First question:** "Is nitrogen actually the limiting nutrient here, or is this a known HNLC or silicate-limited region?"
- **Data to pull:** the nutrient drawdown ratios from the same cruise/season, or published regional nutrient-limitation studies for the site.

### Water-mass claim made from a map or a single T/S value instead of a T-S diagram

- **Usually means:** advection was ignored — water at a given location can have traveled far from where it formed, so geographic proximity doesn't establish common origin.
- **First question:** "Where does this station's T-S curve sit relative to the known regional water-mass end-members?"
- **Data to pull:** the full-depth T-S plot for the station, overlaid on the region's reference water-mass end-member values.

### Pre-2010 (EOS-80, practical salinity) and post-2010 (TEOS-10, Absolute Salinity/Conservative Temperature) processed data merged into one density calculation without reconciliation

- **Usually means:** the resulting density field carries a spurious offset — the two equations of state are not numerically interchangeable at the precision most analyses need.
- **First question:** "Which equation of state was each dataset processed under, and has one been converted to match the other?"
- **Data to pull:** the processing metadata/header for each source dataset; convert everything to TEOS-10 (GSW toolbox) before any joint calculation.

### A cruise station plan that fills every ship-day with full-depth stations and no weather or transit buffer

- **Usually means:** the plan will fail on day one of bad weather, since full-depth CTD occupations near the shelf break or in high-latitude transits routinely lose days to sea state.
- **First question:** "What's the fallback station list if 2–3 days of weather are lost?"
- **Data to pull:** the historical weather-day loss rate for the region/season from prior UNOLS cruise reports on the same vessel class.
