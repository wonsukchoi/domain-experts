# Red flags

Smell tests a transportation engineer catches in the first pass over a traffic impact study, geometric design, or capacity analysis.

### Available sight distance measured below the AASHTO SSD table value for the governing design speed

- **Usually means:** a horizontal curve, vertical crest, or roadside object (sign, vegetation, retaining wall) obstructs the required line of sight at the access point.
- **First question:** does relocating the access point along the frontage solve it without requiring a design exception?
- **Data to pull:** field SSD measurement, AASHTO Green Book SSD table for the governing design speed, as-built survey/geometry.

### Computed LOS lands within roughly 2 seconds of the next-worse grade boundary

- **Usually means:** the result is sensitive to a single input assumption (peak hour factor, heavy-vehicle percentage, saturation flow rate) rather than a robust finding.
- **First question:** which single input, if adjusted within its plausible range, flips the grade?
- **Data to pull:** field count sheets, PHF calculation, saturation-flow field study if one exists.

### Left- or right-turn volume exceeds the design-speed-specific turn-lane nomograph threshold but no turn lane is proposed

- **Usually means:** the capacity/LOS check was treated as the only required analysis, and the separate turn-lane warrant was never run.
- **First question:** has the volume-speed nomograph actually been checked for this specific approach and design speed?
- **Data to pull:** turning-movement counts, posted/design speed, NCHRP 279 or the state DOT's turn-lane warrant chart.

### ITE trip generation rate applied is an "average rate" pulled without checking the underlying equation's sample size or fit

- **Usually means:** a small sample size or a poorly fitting regression is producing an unreliable estimate for this land use and size range.
- **First question:** does the Trip Generation Manual flag this land-use code/size range with a low sample size or an R² below roughly 0.75?
- **Data to pull:** ITE Trip Generation Manual data plot, equation-vs-average-rate comparison, a local trip generation study if one exists for a comparable site.

### Pass-by trip reduction is applied to driveway or turn-lane volume numbers

- **Usually means:** the analyst reduced the turning movements at the site access itself, not just the corridor-level new-trip total the reduction is meant for.
- **First question:** is the driveway/turn-lane analysis using the pass-by-reduced number or the full driveway volume?
- **Data to pull:** trip generation worksheet showing the reduction step, driveway volume breakdown by movement.

### Crash history at the study location shows a concentrated pattern with no Highway Safety Manual or CMF-based countermeasure evaluation attached

- **Usually means:** the study ran capacity analysis only and skipped the safety review entirely.
- **First question:** what crash pattern (angle, rear-end, left-turn) dominates, and does it match a documented CMF countermeasure?
- **Data to pull:** state crash database (3–5 yr), collision diagram, applicable Highway Safety Manual CMF.

### Geometric design checks use posted speed with no field-measured 85th-percentile speed study behind it

- **Usually means:** the analyst defaulted to the easy, available number instead of checking actual operating speed.
- **First question:** has an 85th-percentile spot-speed study been run on this segment, and does it match the posted speed?
- **Data to pull:** spot-speed study data, functional classification, the jurisdiction's design-speed policy.

### Multiple closely-spaced signalized intersections analyzed independently with deterministic HCM/Synchro rather than microsimulation

- **Usually means:** queue interaction or spillback between intersections is invisible in the independent LOS output.
- **First question:** does the 95th-percentile queue length at any approach exceed the storage or spacing to the next intersection?
- **Data to pull:** 95th-percentile queue length output, intersection spacing, available storage/bay lengths.

### A turn lane or signal is recommended solely because a warrant is "met," with no discussion of secondary effects

- **Usually means:** the engineering-judgment step was skipped in favor of a checkbox pass/fail result.
- **First question:** what happens to pedestrian crossing exposure or approach speeds if this improvement is built?
- **Data to pull:** pedestrian volume/crossing data, approach speed data, before/after studies for the same treatment at comparable sites.

### Turning-movement count used for a design-year capacity analysis is a single short count with no growth rate applied

- **Usually means:** the design-year (often 10–20 year horizon) volumes are understated relative to what will actually be there.
- **First question:** what background annual growth rate does the agency's travel demand model or historical count trend support?
- **Data to pull:** historical count trend, MPO travel demand model output, agency-published growth rate.

### Assumed superelevation rate for a horizontal curve exceeds the jurisdiction's e_max for that facility's location

- **Usually means:** a rural design standard was applied to an urban/suburban facility, or vice versa.
- **First question:** what is the governing agency's e_max policy for this facility type and location?
- **Data to pull:** AASHTO Green Book superelevation table, the agency's design manual.

### Proposed turn-lane storage length is shorter than the 95th-percentile queue length from the capacity analysis

- **Usually means:** the geometric layout was value-engineered or laid out before the capacity analysis was finalized, and never reconciled against it.
- **First question:** does the 95th-percentile queue length from the LOS output actually fit in the proposed storage bay?
- **Data to pull:** HCM 95th-percentile queue output, proposed geometric plan dimensions.
