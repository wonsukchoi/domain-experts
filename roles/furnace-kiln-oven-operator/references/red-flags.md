# Red flags

### A load configuration different from the previously validated setup (denser packing, different orientation, different quantity)
- **Usually means:** the existing temperature profile and soak time may not represent actual conditions at the load's slowest-heating point.
- **First question:** has this specific configuration been temperature-surveyed, or is the prior validation being assumed to still apply?
- **Data to pull:** the original validation's load configuration details, the current load's actual configuration.

### Soak time measured only from when the control sensor reaches set-point
- **Usually means:** the load's slowest-heating point may not have reached temperature yet when the soak clock starts, under-soaking part of the load.
- **First question:** has a temperature survey confirmed the control sensor's reading represents the whole load, or just its own location?
- **Data to pull:** temperature survey data if available, control sensor position relative to the load's densest/most shielded area.

### An atmosphere-sensitive cycle verified only by gas flow indication, not actual composition
- **Usually means:** gas is moving through the system, but the chamber's actual atmosphere composition hasn't been confirmed.
- **First question:** does an oxygen analyzer or equivalent composition measurement confirm the atmosphere meets spec, or only the flow meter?
- **Data to pull:** oxygen analyzer or composition reading, flow meter reading, spec requirement for this process.

### Heating or cooling ramp rate run faster than the material's specified rate to save cycle time
- **Usually means:** throughput pressure led to treating ramp rate as a variable to maximize rather than a fixed material specification.
- **First question:** does this material's specification allow the ramp rate actually being used, or is it exceeding a documented limit?
- **Data to pull:** material's specified maximum ramp rate, actual ramp rate achieved this cycle.

### A cycle ended immediately upon reaching set-point temperature
- **Usually means:** "temperature reached" was treated as equivalent to "process complete" without accounting for required soak time.
- **First question:** does this process specify a soak time, and was it completed after set-point was reached?
- **Data to pull:** the process specification's soak time requirement, actual time held at temperature.

### A part or load failing a downstream property test (hardness, surface condition) despite a "cycle complete" log entry
- **Usually means:** the logged cycle completion doesn't necessarily reflect what the load's slowest-heating point or most atmosphere-exposed surface actually experienced.
- **First question:** does the cycle's actual achieved profile (not just target) account for load configuration and atmosphere at the specific failed location?
- **Data to pull:** the full cycle's temperature/atmosphere log, the failed part's position within the load.

### A new material or process run on equipment without checking its specific ramp rate/atmosphere sensitivity
- **Usually means:** settings from a previous, different material are being carried over without verification.
- **First question:** does this specific material's process specification match what's currently programmed into the equipment?
- **Data to pull:** the current material's process specification, the equipment's actual programmed settings.

### A temperature survey performed once and never repeated despite later load configuration or equipment changes
- **Usually means:** the original survey's validity may no longer hold if anything about the load or equipment has changed since.
- **First question:** has anything about the load configuration, equipment (heating elements, insulation), or process changed since the last survey?
- **Data to pull:** date and conditions of the last survey, any equipment maintenance or configuration changes since.

### An oxygen analyzer or atmosphere monitoring instrument not recently calibrated
- **Usually means:** the atmosphere composition readings being relied on for process control may not be accurate.
- **First question:** when was this instrument last calibrated/verified?
- **Data to pull:** calibration log for the atmosphere monitoring equipment.

### A shift handoff describing a cycle in progress without specifying its actual phase (ramp/soak/cool) or load specifics
- **Usually means:** the incoming operator lacks the specific information needed to correctly manage the cycle's remaining steps.
- **First question:** does the handoff specify exactly where in the profile the cycle currently is, and any load-specific details?
- **Data to pull:** the handoff record, current cycle status from the control system.
