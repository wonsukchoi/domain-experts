# Red flags

Smell tests a wind energy engineer catches on a first pass over an AEP estimate, a layout plan, or a structural load report.

### AEP computed at the mean wind speed applied to the power curve, rather than integrated across a full Weibull distribution

- **Usually means:** the analyst evaluated the power curve at a single representative speed instead of summing power × occupancy-probability across every bin — because power scales with the cube of wind speed, this misstates AEP, and the direction of the error depends on the specific curve and distribution shape.
- **First question:** what Weibull k and c parameters were used, and was the calculation a bin-by-bin sum or a single mean-speed evaluation?
- **Data to pull:** the resource-assessment report's Weibull fit and the AEP model's calculation methodology section.

### Capacity factor assumed from a generic regional figure with no site-specific met mast or LIDAR data behind it

- **Usually means:** the AEP estimate is screening-grade, not financing-grade — a generic percentage can be badly wrong in either direction for a specific site's actual wind climate.
- **First question:** how many months of on-site (or a validated long-term-corrected) resource data support the capacity factor figure being quoted?
- **Data to pull:** met mast/LIDAR data log, the long-term correlation analysis if the on-site period is under one year.

### Turbine spacing tighter than roughly 5D with no explicit wake-loss dollar or GWh/yr figure quantified

- **Usually means:** the layout was set by land constraints without pricing the energy cost of that constraint, leaving a real revenue loss unquantified in the financing package.
- **First question:** what does a Jensen/Park (or CFD, in complex terrain) wake-loss run show for this specific spacing versus a 7D alternative?
- **Data to pull:** the wake-model run output and the layout drawing's turbine-to-turbine distances by direction sector.

### A power coefficient (Cp) figure quoted at or above roughly 0.55, or presented as constant across the full operating range

- **Usually means:** either a units/definition error, an unrealistic vendor claim, or a failure to recognize that Cp falls off above rated wind speed as pitch control throttles output — the Betz limit (0.593) is a ceiling no real rotor closely approaches.
- **First question:** at what specific wind speed is this Cp value being claimed, and is it below, at, or above the turbine's rated wind speed?
- **Data to pull:** the manufacturer's certified power curve and the corresponding Cp-vs-wind-speed curve, not a single headline number.

### Turbine IEC class selected from the site's average wind speed alone

- **Usually means:** the class rating may not cover the site's actual 50-year extreme gust or turbulence intensity, leaving structural margin unverified.
- **First question:** what is the site's measured or estimated 50-year extreme wind speed and turbulence category, independent of the average wind speed?
- **Data to pull:** the extreme-value analysis (Gumbel or similar fit) from the resource-assessment report, and the turbine's certified IEC class documentation.

### A structural load report shows a component checked against only an ultimate-load DLC or only a fatigue DLC, not both

- **Usually means:** the component is unverified for whichever load type wasn't checked — ultimate and fatigue frequently govern different components on the same structure.
- **First question:** which DLC governs this specific component's ultimate limit state, and which governs its fatigue life — are both documented?
- **Data to pull:** the IEC 61400-1 design load case summary table from the certification or engineering report.

### A financing memo quotes P50 AEP with no stated uncertainty stack or exceedance level

- **Usually means:** the lender or offtake counterparty can't tell how conservative the number is, or whether it's the expected value versus a bankable floor.
- **First question:** what is the total uncertainty (σ) behind this P50, and what P90/P99 figure does it imply?
- **Data to pull:** the uncertainty-component breakdown (resource, wake, availability, electrical) and the exceedance-level calculation.

### Wake modeling done with a flat-terrain model (Jensen/Park) on a site with significant elevation change or forest canopy

- **Usually means:** the model's core assumption doesn't hold, and a CFD or Gaussian wake model would produce a materially different — usually larger — wake-loss figure.
- **First question:** has a CFD or terrain-aware wake model been run to cross-check the Jensen/Park result for this specific site?
- **Data to pull:** site topography data (elevation model, roughness/land-cover classification) and, if available, a CFD cross-check run.

### A power-curve warranty comparison uses a single average-output figure instead of a wind-speed-binned, air-density-corrected comparison

- **Usually means:** the comparison can hide a shortfall concentrated in a specific wind-speed band (commonly near rated, where pitch-control tuning issues show up) behind an acceptable overall average.
- **First question:** does the comparison follow IEC 61400-12-1's binning methodology, and has the measured data been corrected to the turbine's reference air density?
- **Data to pull:** the IEC 61400-12-1 test report's binned power table, the reference air density used, and the site's actual measured air density during the test period.

### Met mast or LIDAR data covers less than one full year

- **Usually means:** the dataset doesn't capture a full seasonal wind cycle, and the Weibull fit derived from it may not represent the site's true annual distribution.
- **First question:** does the data cover at least one full annual cycle, and if not, what long-term reference station correlation extends it?
- **Data to pull:** the resource campaign's start/end dates and, if under a year, the long-term correlation methodology and reference station data.

### Foundation load calculation states a design moment or force with no partial safety factor applied, or doesn't state which DLC and safety-factor category (normal vs. abnormal) it used

- **Usually means:** the number reported may be an unfactored characteristic load rather than the design load the foundation actually needs to be sized against.
- **First question:** which IEC 61400-1 Table 3 partial safety factor (1.35 normal, 1.1 abnormal) was applied, and to which DLC's characteristic load?
- **Data to pull:** the load-case summary showing characteristic load, applied γf, and resulting design load side by side.
