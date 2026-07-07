# Diesel Truck Mechanic — Red Flags

### DEF quality fault (SPN 3364) recurring within 500 miles of a fresh fill
- **Usually means:** contaminated or wrong-concentration DEF from an unverified roadside source, then a failing dosing valve or reductant sensor
- **First question:** what does the refractometer read right now, against the 31.8–33.2% spec?
- **Data to pull:** DEF tank sample refractometer reading, dosing valve commanded-vs-actual PID, fault code history for the last 5,000 miles

### Pushrod stroke reading at or beyond the CVSA chamber-type limit (e.g. 2 in on a Type 30)
- **Usually means:** worn slack adjuster or brake chamber, less commonly a mis-adjusted automatic slack adjuster masking real lining wear
- **First question:** is the stroke reading with the brakes fully released and air system at governor cutout pressure?
- **Data to pull:** pushrod stroke gauge measurement per axle, lining thickness, last brake service date

### NOx sensor delta between pre-SCR and post-SCR positions below the OEM conversion-efficiency spec
- **Usually means:** aging or contaminated SCR catalyst, less commonly a drifted downstream NOx sensor
- **First question:** has the DEF concentration and dosing rate already been confirmed correct?
- **Data to pull:** pre/post-SCR NOx live PIDs, catalyst mileage/age, DEF concentration reading

### DPF differential pressure trending up 15%+ over three consecutive PM intervals
- **Usually means:** upstream soot-generation problem (failing injector, exhaust leak, short-trip duty cycle preventing passive regen), less commonly a genuinely ash-loaded filter due for cleaning
- **First question:** what's the truck's typical trip length and average speed — is it accumulating enough exhaust temperature to regen passively?
- **Data to pull:** differential-pressure trend across last 3 PM visits, regen frequency/duration log, injector balance rates

### Coolant loss exceeding roughly 1 gallon per 1,000 miles with no visible external leak
- **Usually means:** EGR cooler crack (coolant entering the exhaust/intake side) or head gasket seepage
- **First question:** is there a sweet exhaust smell or white smoke under load?
- **Data to pull:** coolant system pressure test result, EGR cooler leak-down test, oil sample for coolant contamination (glycol presence)

### Oil analysis showing iron above roughly 15 ppm per 1,000-mile sample interval
- **Usually means:** accelerating cylinder liner or ring wear, less commonly a wear-metal spike from a recent overhaul breaking in
- **First question:** is this a trend across the last 2–3 samples or a single elevated reading?
- **Data to pull:** trended oil analysis history, not a single sample; blow-by rate if available

### Same defect cited on two consecutive roadside or annual inspections within 90 days
- **Usually means:** the underlying cause wasn't fixed at the prior repair, only the symptom (e.g., re-adjusting stroke instead of replacing a worn chamber)
- **First question:** what was actually done at the last repair order for this defect code?
- **Data to pull:** prior repair order for the same component/CVSA item, current measurement against the same threshold

### Fuel economy drop greater than 1.5 mpg versus the truck's trailing 3-month baseline
- **Usually means:** turbo boost leak, injector fouling, or under-inflated tires, less commonly aerodynamic changes (missing fairings) or route/load changes
- **First question:** has anything changed on the truck (tires, trailer, route) or is this the same configuration as the baseline period?
- **Data to pull:** ECM fuel economy trend log, tire pressure log, boost pressure PID under load

### Air system build time exceeding roughly 3 minutes from 85 to 100 psi
- **Usually means:** failing air compressor, clogged air dryer, or a governor cut-in/cut-out drifted out of spec
- **First question:** does the build-time problem show up cold, hot, or both?
- **Data to pull:** governor cut-in/cut-out pressures, air dryer purge cycle log, compressor discharge line temperature

### DEF consumption ratio drifting outside roughly 2–3% of diesel fuel consumption
- **Usually means:** dosing system over- or under-injecting, or a DEF quality/concentration problem masking as a consumption anomaly
- **First question:** has the DEF concentration been verified independently of the consumption-ratio calculation?
- **Data to pull:** DEF and fuel consumption logs over the same mileage window, dosing valve commanded quantity, refractometer reading
