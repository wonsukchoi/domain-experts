# Red flags

### Drum level indicator changes rapidly during a load ramp while feedwater valve position is unchanged
- **Usually means:** shrink/swell masking the true water inventory trend, not an actual level change requiring the opposite correction.
- **First question:** does the steam flow versus feedwater flow trend show a deficit or surplus consistent with the apparent level move?
- **Data to pull:** steam flow and feedwater flow trend during the ramp.

### A water/steam chemistry parameter (dissolved oxygen, pH, conductivity) drifts outside its limit with no trip triggered
- **Usually means:** a slow, compounding corrosion or scaling risk being under-prioritized because nothing tripped.
- **First question:** how long has this parameter actually been outside limits, and by how much?
- **Data to pull:** chemistry trend log against the limit, and the duration of the excursion.

### A process parameter is routinely operated close to, but not past, its trip setpoint
- **Usually means:** the operating margin meant to absorb instrumentation and process uncertainty is being consumed as normal practice.
- **First question:** how often does this parameter approach the pre-trip alarm threshold during routine operation?
- **Data to pull:** the parameter's trend against its trip setpoint and alarm threshold over recent operating history.

### Startup or shutdown temperature/pressure ramp rate exceeds the limiting component's rated rate
- **Usually means:** thermal stress accumulating on a thick-walled component (drum, header, turbine rotor) that may not surface as a failure until much later.
- **First question:** what is the actual ramp rate versus the rated limit for the most restrictive component in the path?
- **Data to pull:** the actual ramp-rate trend compared against the manufacturer's rated limit for that component.

### An alarm activates that doesn't match the expected process state given recent operator actions
- **Usually means:** a possible instrumentation or signal fault rather than an actual process upset.
- **First question:** does a second, independent indicator corroborate the alarm?
- **Data to pull:** a cross-check of the alarmed instrument against a redundant sensor.

### Turbine vibration trend rises gradually over an operating period without a corresponding trip
- **Usually means:** a developing mechanical issue — bearing wear, misalignment — rather than normal variation.
- **First question:** how does the current vibration trend compare to baseline and the alarm threshold?
- **Data to pull:** the vibration trend log against baseline and the alarm threshold.

### Shift handoff log lacks specific parameter values or corrective actions for an event that occurred during the shift
- **Usually means:** the incoming shift lacks the information needed to recognize a recurring or developing issue.
- **First question:** what actually happened per the DCS alarm/event history versus what the log records?
- **Data to pull:** the shift log entries compared against the actual DCS event and alarm history for that period.
