# Red flags

### 8 consecutive metrology points on the same side of the SPC centerline
- **Usually means:** a systematic process drift (chamber seasoning, consumable wear, a slowly failing sensor) rather than random variation.
- **First question:** are all 8 points still within spec and control limits, or has one already crossed?
- **Data to pull:** the full SPC trend chart, chamber consumable-age/PM log, any recent tool maintenance events.

### A single metrology point beyond the 3-sigma control limit
- **Usually means:** an acute process upset (a sudden hardware fault, a gas supply interruption, a recipe load error) rather than gradual drift.
- **First question:** did the recipe loaded on the tool match the traveler's specified revision for this lot?
- **Data to pull:** recipe version log for this run, tool alarm/event log for the processing window, first-wafer metrology if available.

### 2 of 3 consecutive points beyond the 2-sigma line on the same side
- **Usually means:** an early-stage drift that hasn't yet crossed 3-sigma — often the same root cause that later triggers a full out-of-control alarm if unaddressed.
- **First question:** has this chamber shown this pattern on recent prior lots?
- **Data to pull:** SPC history for this chamber over the last 5-10 lots, consumable-age log.

### Defect map showing a consistent spatial pattern (edge ring, center-to-edge gradient, one quadrant)
- **Usually means:** tool/chamber hardware (a worn electrode, uneven gas distribution, a temperature gradient) rather than the incoming material.
- **First question:** does the same pattern appear on wafers processed on a different tool?
- **Data to pull:** defect maps from at least one other tool/chamber for comparison, chamber hardware maintenance history.

### A recipe change proposed to correct a metrology drift
- **Usually means:** a legitimate attempt to compensate for a known process shift, but needs verification it stays inside the qualified process window.
- **First question:** does the proposed parameter value fall inside the range already validated during process qualification?
- **Data to pull:** the process qualification document's parameter windows, any prior engineering change requests for this recipe.

### Two nominally matched tools showing a persistent output offset on the same recipe
- **Usually means:** chamber seasoning or consumable-age divergence between the two tools rather than a metrology calibration issue.
- **First question:** what are the current RF-hours or wafer counts since last clean/reseasoning on each tool?
- **Data to pull:** consumable-age log for both tools, most recent tool-matching qualification data.

### A lot approaching its queue-time limit while a metrology result is still under review
- **Usually means:** material degradation risk (moisture uptake, native oxide growth, resist relaxation) building while the hold decision is pending.
- **First question:** what is this specific process step's maximum allowable queue time, and how much of it remains?
- **Data to pull:** the step's specified queue-time limit, timestamp the lot entered hold.

### A lot advanced past a hold point without a documented disposition
- **Usually means:** a hold was cleared informally without the required investigation or sign-off being completed.
- **First question:** does the MES record show a disposition entry matching the timestamp the lot moved forward?
- **Data to pull:** MES lot history for the hold and release timestamps, disposition sign-off record.

### A tool returning to production immediately after PM without a qualification run
- **Usually means:** the tool's post-maintenance state hasn't been verified to match its pre-maintenance qualified condition.
- **First question:** has a qualification lot or test wafer run cleared this tool since the PM was completed?
- **Data to pull:** PM completion timestamp, qualification/test-wafer run log since that timestamp.

### Cleanroom particle count trending upward without a corresponding change in traffic or activity
- **Usually means:** a filter, interlock, or tool seal degrading rather than a procedural gowning lapse.
- **First question:** which specific tool or zone is closest to the particle counter showing the trend?
- **Data to pull:** particle count trend by zone/counter location, filter and interlock maintenance status for tools in that zone.
