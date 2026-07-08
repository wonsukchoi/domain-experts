# Red flags

Smell tests a solar energy systems engineer catches on a first pass over a PV design package, a yield estimate, or an interconnection application.

### String voltage calculated only at STC, with no cold-temperature Voc correction shown

- **Usually means:** the designer sized modules-per-string against 25°C Voc and never ran the NEC 690.7 correction, leaving the string's real cold-morning voltage unknown and likely over the inverter's maximum DC input rating.
- **First question:** what is the string's Voc at the site's ASHRAE 99% extreme minimum design dry-bulb temperature, using the module's actual temperature coefficient?
- **Data to pull:** module datasheet temperature coefficients, the site's ASHRAE Fundamentals Handbook design-temperature entry, the inverter's maximum DC input voltage rating.

### Conductor ampacity sized using only one of NEC 690.8's two 125% factors

- **Usually means:** the designer applied the 690.8(A) irradiance-enhancement factor (Isc x 1.25) but not the 690.8(B) continuous-duty factor on top of it, undersizing the conductor by roughly 20% relative to the code-required 1.5625x combined multiplier.
- **First question:** does the calculation show Isc x 1.25 x 1.25, or just a single 1.25 multiplier?
- **Data to pull:** the conductor sizing calculation sheet, module Isc rating, the specific NEC edition cited.

### Annual yield estimate computed as nameplate DC capacity times peak-sun-hours with no loss stack

- **Usually means:** the estimate skips temperature, soiling, shading, mismatch, wiring, inverter, and availability losses entirely, typically overstating annual output by 15-25%.
- **First question:** what performance ratio does this yield number imply, and does that PR fall inside the 0.75-0.85 range normal for the array's configuration and climate?
- **Data to pull:** the full loss-stack breakdown behind the number, or the 8760-hour simulation output if one exists.

### DC/AC ratio above roughly 1.3 with no hourly clipping simulation behind the number

- **Usually means:** clipping loss is a threshold effect concentrated in a small number of midday summer hours, and an annual-average heuristic at this ratio systematically understates it — the yield number may be optimistic by several percent.
- **First question:** was clipping estimated from an 8760-hour simulation (PVsyst/Helioscope/SAM), or from a flat annual assumption?
- **Data to pull:** the simulation run file or output report showing hourly clipped energy.

### Partial shading present on a string design with a single string inverter and no module-level power electronics

- **Usually means:** the string's output is capped by its worst-shaded module, producing a loss disproportionate to the shaded area — a shading loss that looks like 5% of array area can cost 15%+ of string output.
- **First question:** what fraction of the string's modules experience shading at any point in the day, and was a microinverter or DC-optimizer alternative costed against the string-inverter design?
- **Data to pull:** the shading analysis (3D model or on-site SunEye/solar-pathfinder survey), string layout diagram.

### Yield model quotes a single flat number for every year of a 10+ year PPA or financing term

- **Usually means:** the model uses year-1 performance-ratio yield without applying the module's linear warranty degradation curve, overstating cumulative revenue over the contract term.
- **First question:** what annual degradation rate is applied, and does it match the module manufacturer's warranty schedule (commonly a first-year step plus ~0.4-0.5%/yr linear thereafter)?
- **Data to pull:** the module manufacturer's power warranty schedule, the financing model's year-by-year yield table.

### Financing package presents only a single-point (P50) yield estimate with no exceedance-probability range

- **Usually means:** the debt-sizing basis has no stated confidence level, which a lender or investor typically requires (commonly P50 and P90, sometimes P99) to size coverage ratios against weather-year variance.
- **First question:** what exceedance probability does the quoted number represent, and is a P90 or P99 figure available from the same simulation?
- **Data to pull:** the simulation software's Monte Carlo or weather-year variance output, not just the median-case run.

### Inverter's per-MPPT maximum input current not checked against combined string Imp for that input

- **Usually means:** multiple strings landing on one MPPT input can exceed the inverter's rated input current for that channel even though each individual string is within its own conductor's ampacity — a design-level oversight, not a wiring-level one.
- **First question:** how many strings combine onto each MPPT input, and does their combined Imp (or Isc x 1.25 per 690.8(A)) stay under the inverter's documented per-input maximum?
- **Data to pull:** inverter datasheet's per-MPPT-input maximum current rating, the string-to-MPPT-input wiring diagram.

### Module temperature coefficient sourced from a marketing spec sheet summary instead of the certified datasheet table

- **Usually means:** a rounded or generic coefficient is being used instead of the specific model's certified value, introducing error into both the cold-temperature Voc calculation and the temperature loss term of the PR model.
- **First question:** does the temperature coefficient used trace to the specific module model's certified datasheet (IEC 61215 test report), or a generic "typical crystalline silicon" placeholder?
- **Data to pull:** the module's IEC 61215-certified datasheet with the specific temperature coefficients (Voc, Vmp, Isc, Pmax).

### Interconnection application's inverter settings don't cite a specific IEEE 1547-2018 / UL 1741-SA configuration

- **Usually means:** the ride-through, voltage/frequency trip, and grid-support settings haven't been documented to the utility's required standard, which commonly stalls or rejects the interconnection application.
- **First question:** what specific IEEE 1547-2018 category and UL 1741-SA settings profile is the inverter configured to, and does it match the utility's interconnection requirements?
- **Data to pull:** the inverter's grid-support settings configuration file or commissioning report, the utility's interconnection technical requirements document.
