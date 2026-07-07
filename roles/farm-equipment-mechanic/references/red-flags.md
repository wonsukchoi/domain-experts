# Red flags

Smell tests a veteran mechanic catches at intake or mid-diagnosis. Format for each: what it usually means, the first question to ask, and the data to pull before changing anything.

### A fault code is cleared and the machine restarted without pulling freeze-frame data first

**Usually means:** the code was treated as noise rather than diagnosed, or a previous shop/operator already tried the "clear it and see" approach — which erases the freeze-frame snapshot needed to confirm root cause on the first recurrence.

**First question:** "Did anyone pull the live data or freeze frame before the code was cleared?"

**Data to pull:** stored/history codes (freeze-frame data often survives a clear even when the active code doesn't); operator's account of what the machine was doing when the code first appeared.

### Hydraulic main relief or charge pressure reads more than ~10% below OEM spec

**Usually means:** a relief valve set point drifted, an internal pump leak, or (for charge pressure specifically) a starved supply that will make every downstream component look weak even if none of them are actually faulty.

**First question:** "Is this the supply-side pressure (charge/standby) or a downstream circuit — have we tested the supply first?"

**Data to pull:** pressure reading against OEM spec sheet for that exact model/system; case-drain flow and temperature for the same circuit; hours since the relief valve or pump was last serviced.

### PTO implement rated for one speed is connected and run at the tractor's other speed setting

**Usually means:** a spline-adapter or operator error paired a 540-rated implement with a 1000-rpm output (or vice versa) — the most common precondition for driveline overspeed failure or an underpowered implement blamed on the wrong cause.

**First question:** "What speed is this implement rated for, and what speed is the tractor's PTO actually set to right now?"

**Data to pull:** implement OEM PTO speed rating; tachometer reading at the shaft (not just the dash indicator); spline count match between tractor stub and implement shaft.

### Dash-selected PTO speed doesn't match the tachometer reading at the shaft

**Usually means:** a slipping clutch pack inside the tractor's PTO engagement, not an implement problem — the dash shows the commanded speed, not the delivered speed.

**First question:** "Has anyone measured actual output speed at the shaft, or are we trusting the dash indicator?"

**Data to pull:** handheld tachometer reading at the PTO shaft under load; PTO clutch service history; engine rpm at the time of measurement.

### A precision-ag component (row-unit monitor, yield monitor, auto-steer receiver) throws an intermittent fault correlated with field bumps or turns

**Usually means:** a chafed harness, a loose or corroded connector, or a vibration-loosened ground strap — a mechanical/wiring cause wearing an electronics symptom — well before a firmware or calibration problem.

**First question:** "Does the fault correlate with motion or vibration, or does it happen at a standstill too?"

**Data to pull:** fault timestamp log against GPS/motion data if available; harness and connector inspection at known wear points; ground strap continuity.

### ISOBUS or CAN-bus fault shows as "implement not detected" across more than one connected device at once

**Usually means:** the bus itself — termination resistor, bus voltage, a damaged trunk connector — not any single implement's control module, since one implement's failure wouldn't typically take down detection of the others.

**First question:** "Is this fault isolated to one implement, or are multiple devices on the bus affected at the same time?"

**Data to pull:** bus voltage and termination resistance at both ends of the trunk line; which specific implements/displays are affected; recent physical work near the trunk connector or harness routing.

### A repair requires OEM calibration or reflash and this is discovered after the component is already removed

**Usually means:** the intake triage skipped the tool-access decision step — the shop is now committed to a teardown with the machine down until a dealer appointment opens, when the same discovery at intake could have routed the whole job to the dealer up front or avoided the teardown entirely.

**First question:** "Did we confirm calibration/reflash requirements before pulling this part, or after?"

**Data to pull:** OEM service documentation for calibration requirements on this specific component; dealer appointment availability and lead time; whether an aftermarket tool can handle the calibration step at all for this model.

### A part has been swapped once already for this fault and the fault recurred within the same shift

**Usually means:** classic parts-cannon pattern — the first swap addressed a symptom location without confirming root cause, and the actual fault (harness, ground, upstream supply) is still present.

**First question:** "What confirmed the first part as the cause — freeze-frame data, a pressure test, or just the fault code name?"

**Data to pull:** freeze-frame/live data from both before and after the first part swap; the specific diagnostic step (if any) that identified the first part as the cause.

### A breakdown occurs inside a harvest or planting window and is scheduled into the standard shop queue rather than triaged same-day

**Usually means:** intake didn't weigh the calendar — the same repair that's routine to queue in the off-season carries a field-loss or contract-penalty cost per day of delay during the window that the standard queue doesn't account for.

**First question:** "How many field-days does the customer have left before their next weather or contract deadline?"

**Data to pull:** customer's remaining acreage and machine field capacity; forecast for the relevant window; any contract deadlines or penalty clauses tied to completion date.

### Pre-season inspection was skipped citing cost, with no PM record for the unit

**Usually means:** the shop or owner is treating the inspection's small, known cost as avoidable without weighing it against the much larger and less predictable in-season failure cost for the same wear items.

**First question:** "What's the last date this unit had a hydraulic pressure test, harness inspection, and PTO/driveline check logged?"

**Data to pull:** PM/service record for the unit; hours or acres run since the last inspection; any stored (non-active) fault codes that would have been caught by an inspection.
