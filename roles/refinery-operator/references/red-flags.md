# Red flags

### A product quality test failing spec while all monitored process readings appear within their individual normal ranges
- **Usually means:** an interacting-variable effect (commonly a temperature-pressure relationship in a distillation column) that no single reading captures.
- **First question:** has any related variable (pressure, especially) drifted gradually enough to avoid triggering its own alarm while still shifting the true separation point?
- **Data to pull:** full trend data for all interacting variables (not just the primary one), not just current point values.

### A relief valve lift, planned or unplanned
- **Usually means:** if unplanned, an upstream control failure (a control loop malfunction, an operator action, an equipment fault) allowed pressure to exceed setpoint.
- **First question:** was this a scheduled/expected test lift, or an unplanned event requiring root-cause investigation?
- **Data to pull:** DCS alarm and trend history leading up to the lift, control loop status for the relevant system.

### Column or vessel pressure drifting gradually without triggering an alarm
- **Usually means:** a slow-developing issue (fouling, a partially blocked line) approaching but not yet crossing an alarm threshold.
- **First question:** what is the pressure trend over the full shift or longer, not just the current reading against the alarm setpoint?
- **Data to pull:** extended pressure trend data, any known equipment condition (condenser fouling, filter loading) that could explain a gradual rise.

### Tank gauge reading used for custody transfer without a documented temperature/API gravity correction applied
- **Usually means:** the raw observed volume, not the corrected standard volume, is being reported — a commercial accuracy issue.
- **First question:** does the reported figure show the correction factors applied, or just the raw gauge reading?
- **Data to pull:** raw gauge reading, temperature and API gravity data used for correction, correction calculation record.

### A standing alarm override or workaround with no recent re-verification of its original justification
- **Usually means:** the override may have outlived the condition it was meant to address, or the condition may have changed without the override being reassessed.
- **First question:** when was this override's justification last reviewed, and does the original condition still apply?
- **Data to pull:** override log with original justification date, any process changes since that date that could affect its validity.

### A proposed procedure deviation justified as a minor, clearly beneficial optimization
- **Usually means:** a real improvement idea, but one that still needs formal review against the hazard analysis before implementation.
- **First question:** has this been routed through management of change, or is it being executed on operator judgment alone?
- **Data to pull:** the documented procedure, MOC log for this or similar past changes.

### An unexpected reading or alarm occurring during a startup or shutdown sequence
- **Usually means:** the transient process has diverged from its expected path — a higher-consequence situation than the same reading during steady-state.
- **First question:** does this deviation match a known, expected transient behavior at this specific step, or is it genuinely unexpected?
- **Data to pull:** the startup/shutdown procedure's expected reading ranges for this specific step, current actual readings.

### Two consecutive shifts reporting the same "normal variation" explanation for a recurring minor deviation
- **Usually means:** a developing trend has been repeatedly explained away as routine rather than investigated as a pattern.
- **First question:** does the deviation's magnitude or frequency show an actual trend across shifts, or is it genuinely random?
- **Data to pull:** shift log entries for this deviation across the recent period, trend data if available.

### Product blending or yield shifting without a corresponding documented process change
- **Usually means:** an unrecognized process drift (feed composition change, equipment condition change) rather than an intentional adjustment.
- **First question:** has feedstock composition or any upstream process changed recently, even one not obviously connected to this unit?
- **Data to pull:** feedstock quality/composition data, upstream unit changes, blending ratio records.

### A custody transfer figure disputed by a counterparty
- **Usually means:** either a genuine measurement/correction discrepancy or a difference in gauging method/timing between the two parties.
- **First question:** were both parties' measurements taken using the same method and correction factors, and at comparable times?
- **Data to pull:** both parties' gauge readings, correction factors applied, timing of measurement relative to any transfer/temperature change.
