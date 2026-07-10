# Vocabulary

### Shrink and swell
The phenomenon where a boiler drum's indicated water level rises or falls temporarily due to changing steam bubble volume during a load change, independent of the actual water mass in the drum.
**In use:** "That level rise is swell from the load ramp — check flows before touching feedwater."
**Common misuse:** Reacting to the displayed drum level alone during a load change without cross-checking the flow balance, which risks exactly the wrong corrective action.

### Feedwater/steam flow mismatch
The difference between measured feedwater flow into the drum and steam flow leaving it, used to validate whether an apparent level change reflects a true inventory change.
**In use:** "Feedwater's 30,000 lb/hr under steam flow — that's a real deficit, not just a swell artifact."
**Common misuse:** Trusting the drum-level indicator in isolation during dynamic conditions instead of cross-checking this flow balance first.

### Trip setpoint
The process value at which automatic protective action — a unit trip or shutdown — occurs.
**In use:** "We're 5 psi from the trip setpoint — that's the pre-trip alarm, act now rather than wait and see."
**Common misuse:** Treating "hasn't tripped yet" as evidence that operating near the setpoint is safe, rather than recognizing that the margin exists specifically to absorb instrumentation and process uncertainty.

### Ramp rate
The rate of change — typically °F/hour or psi/minute — at which temperature or pressure is allowed to change during startup, shutdown, or a load change, limited by the most thermally sensitive component in the path.
**In use:** "Ramp rate's set by the drum, not the turbine — that's the slowest, thickest component we've got."
**Common misuse:** Setting the ramp rate based on the fastest-responding component rather than the most restrictive, thickest-walled one that actually limits how fast the unit can safely change state.

### Dissolved oxygen (DO) / water chemistry limits
Control parameters for boiler feedwater and steam chemistry that prevent corrosion and scaling over time.
**In use:** "DO's been trending high for two shifts — that's tube corrosion accumulating, not a nuisance reading."
**Common misuse:** Treating a chemistry excursion as low priority because it doesn't cause an immediate trip, when the resulting damage compounds silently over weeks or months.

### Load following
Operating a generating unit's output to track a changing dispatch or demand instruction, rather than at a fixed steady output.
**In use:** "We're load following this shift — expect the normal ranges on everything to shift as we ramp."
**Common misuse:** Expecting process variables to hold at fixed "normal" values during load following, rather than recognizing that the normal range itself shifts with the current load level.

### Distributed control system (DCS)
The integrated computer control system used to monitor and adjust plant process variables from a control room.
**In use:** "DCS is showing the alarm, but confirm it against the redundant sensor before acting on it."
**Common misuse:** Treating the DCS display as ground truth without considering that the reading behind it could reflect an instrumentation or signal fault.

### Superheat / superheated steam
Steam heated beyond its saturation temperature at a given pressure, required for turbine efficiency and to protect turbine blades from moisture damage.
**In use:** "Superheat's dropped below spec at this pressure — that moisture risk goes straight to the turbine blades."
**Common misuse:** Assuming any steam leaving the boiler is automatically at the required superheat condition without verifying actual temperature against the saturation point at that specific pressure.

### Forced outage
An unplanned shutdown caused by an equipment failure or protective trip, distinct from a planned or scheduled outage.
**In use:** "That was a forced outage from the trip, not a scheduled maintenance day — root cause it before restart."
**Common misuse:** Treating all outages as equivalent events, when a forced outage specifically indicates an operational or maintenance gap worth investigating.

### Pre-trip alarm
An alarm set at a threshold before the actual automatic trip setpoint, intended to give the operator time to correct the condition manually.
**In use:** "That's the pre-trip alarm on drum level — this is the cue to act, not just acknowledge and move on."
**Common misuse:** Treating a pre-trip alarm as equivalent to a nuisance alarm to be acknowledged and dismissed, rather than as the intended cue to correct the condition before the actual trip activates.
