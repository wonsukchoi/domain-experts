# Red flags

Smell tests an engine-room watchkeeper or chief engineer catches before a machinery casualty, a life-safety shortcut, or a compliance violation happens. Format for each: what it usually means, the first question to ask, and the data to pull before committing to an action.

### Cooling-water or lube-oil parameter climbing steadily over 3+ readings while still below the alarm setpoint

- **Usually means:** the trend, not the absolute value, is the actual signal — waiting for the alarm or shutdown setpoint to fire discards the window the design margin was built to give.
- **First question:** "What's the rate of change over the last three readings, and when does that trend actually hit the shutdown setpoint if nothing changes?"
- **Data to pull:** AMS trend log for the parameter, last three to four timestamped readings, extrapolated time-to-threshold.

### Oil content meter reading between 10-15 ppm, or drifting/inconsistent near the 15 ppm limit

- **Usually means:** a fouled coalescer element or a miscalibrated sensor, not a marginal-but-acceptable discharge.
- **First question:** "Is this reading stable and trusted, or drifting — and when was the OCM last calibrated?"
- **Data to pull:** OCM calibration record, coalescer maintenance history, repeat sample result.

### A temporary hose, portable pump, or unlogged piping modification near the OWS overboard discharge line

- **Usually means:** a bypass ("magic pipe") is being rigged or has been rigged around the separator — the specific setup behind every documented MARPOL bypass prosecution.
- **First question:** "Where does that line actually discharge, and is it logged anywhere?"
- **Data to pull:** current piping diagram for the bilge/OWS system, any recent unlogged modification, Oil Record Book entries for the relevant period.

### CO2 muster headcount doesn't reconcile with the watch/duty roster before release

- **Usually means:** someone expected in the space hasn't been positively confirmed clear — the release is not yet authorized regardless of how the fire looks.
- **First question:** "Who's unaccounted for right now, and where were they last confirmed?"
- **Data to pull:** current watch/duty roster, muster-station headcount, last known position of any unconfirmed person.

### Fixed CO2 release authorized without the mandatory pre-discharge alarm being sounded first

- **Usually means:** time pressure from a visibly worsening fire is overriding the life-safety sequence rather than the sequence being followed under pressure.
- **First question:** "Was the pre-discharge alarm actually sounded and given its full duration before the release?"
- **Data to pull:** CO2 panel activation log/timestamp, alarm sound duration versus the vessel's fire control plan requirement.

### Generator load restored in one step after a black-start instead of in blocks

- **Usually means:** the restoration is racing to get everything back online at once, risking a frequency/voltage dip that trips the generator and resets the recovery.
- **First question:** "What percentage of rated capacity did that last step add, and did we confirm stability before adding it?"
- **Data to pull:** switchboard load log during restoration, generator rated capacity, frequency/voltage trend through each step.

### Emergency generator fails to reach full emergency load within 45 seconds of main power loss

- **Usually means:** a starting-battery, air-start, or auto-start control fault that will show up again in a real blackout, not a one-off slow start.
- **First question:** "Was this confirmed against the actual 45-second SOLAS requirement, or just noted as 'eventually came up'?"
- **Data to pull:** emergency generator start-sequence log/test record, most recent statutory test result.

### Same alarm acknowledged/silenced more than once in a watch without a corrective action logged

- **Usually means:** the alarm is being managed as a nuisance rather than as a symptom of an unresolved casualty in progress.
- **First question:** "What corrective action was actually taken between the first and second acknowledgment, if any?"
- **Data to pull:** alarm history log with acknowledgment timestamps, engine log entries for corrective actions in the same window.

### Oil Record Book entries written or backdated after the watch instead of during it

- **Usually means:** the entry is being reconstructed from memory rather than recorded contemporaneously — the exact pattern port-state control and class surveyors are trained to flag.
- **First question:** "When was this entry actually written relative to the operation it describes?"
- **Data to pull:** Oil Record Book entry timestamps versus operation timestamps, watch handover log.

### Bilge holding tank level projected to exceed capacity before the next port call

- **Usually means:** either the discharge/treatment plan needs to change now, or an out-of-spec discharge is about to be tempting later in the transit.
- **First question:** "At the current accumulation rate, what's the projected level at arrival, and does it clear capacity with margin?"
- **Data to pull:** current tank sounding, daily accumulation rate, days to next port, tank capacity.

### Crankcase oil mist detector alarm reset without an inspection

- **Usually means:** a developing bearing or liner fault that can progress to a crankcase explosion is being cleared rather than investigated.
- **First question:** "Was the crankcase actually inspected, or was the alarm just reset?"
- **Data to pull:** oil mist detector alarm log, most recent crankcase inspection record, recent lube-oil analysis (iron content, particle count).

### Standby equipment (second separator coalescer, standby sea-water pump, second generator) not proven ready this watch

- **Usually means:** the planned maintenance system shows it as available, but actual readiness hasn't been confirmed recently enough to trust in a casualty.
- **First question:** "When was that standby unit last actually run or tested, not just logged as available?"
- **Data to pull:** PMS readiness record, last test/run date for the standby unit, any open deficiency against it.
