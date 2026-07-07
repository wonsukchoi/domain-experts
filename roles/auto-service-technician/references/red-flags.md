# Red flags

Smell tests for a repair order, a technician's comeback history, or a shop's efficiency report.

### Comeback rate above ~3% for a technician over a rolling quarter
- **Usually means:** diagnosis is being rushed to protect flat-rate efficiency, or a specific code family (commonly fuel-trim/misfire pairs) is being parts-cannoned instead of confirmed.
- **First question:** "Pull the last 90 days of comebacks for this technician — do they cluster around a code type or a job type?"
- **Data to pull:** comeback log by technician and code, original RO vs. comeback RO diagnostic notes, whether freeze frame/confirming-test data exists on the original RO.

### Diagnostic billed at or under the posted flat-rate time on a multi-code, cross-system complaint
- **Usually means:** the diagnostic stopped at "code retrieved" rather than "cause confirmed" — a genuine multi-code fuel-trim/misfire workup routinely exceeds the posted 1.0-hour diagnostic allotment.
- **First question:** "What live-data values or confirming test are documented, beyond the code numbers themselves?"
- **Data to pull:** the RO's diagnostic notes section, freeze frame data if recorded, whether a confirming test (smoke, voltage-drop, waveform) is named.

### Code cleared before freeze frame or trim data was recorded
- **Usually means:** either an oversight or an attempt to move to the repair quickly — either way, the evidence of the fault's operating conditions is now gone.
- **First question:** "Was freeze frame data captured before the codes were cleared, and is it on the RO?"
- **Data to pull:** scan-tool session log/timestamp if the tool retains one, the RO's documented data fields.

### Part replaced matches the code's plain-language description with no confirming test noted
- **Usually means:** parts-cannon diagnosis — the code named a system, and the tech replaced the component most associated with that system's name rather than testing which component actually failed.
- **First question:** "What test confirmed this specific part, as opposed to another component in the same circuit?"
- **Data to pull:** the confirming-test result (waveform, resistance, voltage-drop reading), whether other components in the same circuit were ruled out.

### Same code returns within 30–90 days of a "completed" repair
- **Usually means:** the original repair addressed a symptom the code described, not the underlying cause — treat this as a diagnostic do-over, not a new billable complaint.
- **First question:** "What was tested and ruled out on the first visit, versus what was actually replaced?"
- **Data to pull:** original RO diagnostic notes, parts installed, freeze frame comparison between the two visits.

### Technician sustaining well above ~130–150% flagged-hours-to-clock-hours efficiency specifically on diagnostic-heavy jobs
- **Usually means:** on routine maintenance, high efficiency is normal and desirable; on ambiguous multi-system diagnostic jobs specifically, sustained high efficiency more often means confirming tests are being skipped.
- **First question:** "Break the efficiency number down by job type — is the outperformance concentrated in diagnostics or in routine work?"
- **Data to pull:** flagged vs. clock hours by job category, comeback rate cross-referenced against the same technician and job type.

### Recommended-services line blends a confirmed repair with advisory wear items
- **Usually means:** either a documentation shortcut or a deliberate blur so the customer can't distinguish what caused today's complaint from what's merely worth watching.
- **First question:** "Which of these line items is the confirmed fix for today's complaint, and which are advisories the customer can decline?"
- **Data to pull:** the RO's line-item breakdown, the diagnostic data supporting each item individually (crack count, percentage of rated spec, mileage vs. interval).

### Warranty labor rate applied on a job that's actually outside the manufacturer's coverage window, or vice versa
- **Usually means:** a mileage/date boundary wasn't checked before the RO was opened, or a used vehicle's remaining factory or powertrain coverage wasn't verified against the VIN.
- **First question:** "What's this VIN's in-service date and mileage against the applicable warranty term, and was that checked before quoting?"
- **Data to pull:** VIN warranty-status lookup, original in-service date, current mileage, whether a prior owner's repairs affected remaining coverage.

### No post-repair verification (drive cycle or re-scan) recorded before the vehicle was released
- **Usually means:** the shop is trusting that the repair worked rather than confirming it — the fastest way to convert a correct diagnosis into an avoidable comeback anyway.
- **First question:** "What verification was run after the repair, and what were the resulting trim/monitor values?"
- **Data to pull:** post-repair scan data, drive-cycle completion status, technician sign-off timestamp relative to release time.

### "Maintenance package" recommended with no matching mileage interval or inspection finding cited
- **Usually means:** a menu upsell being sold on cadence (e.g., every visit past a round-number mileage) rather than on an actual measured condition.
- **First question:** "What specific inspection finding or manufacturer interval calls for this now, for this VIN's mileage?"
- **Data to pull:** OEM maintenance schedule for the VIN, the specific measurement or visual finding cited (if any) on the RO.
