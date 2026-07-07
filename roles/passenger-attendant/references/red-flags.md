# Red Flags — Passenger Attendant

### Securement logged as complete in under 60 seconds from bridge-plate/ramp deployment to stow
- **Usually means:** one or more of the four straps or the lap belt was skipped to make a scheduled dwell; second most likely: the attendant is estimating the time rather than reading it off the actual sequence, and the true elapsed time was longer than logged.
- **First question:** "Walk me through each strap and the belt in order — what time did each one actually land?"
- **Data to pull:** the securement log timestamp, radio traffic (or absence of it) requesting a dwell extension, the rider's own account if available.

### A mobility-assist boarding or detraining with no radio call to the conductor/train operator, despite a dwell deficit on the worksheet
- **Usually means:** the attendant absorbed the deficit by rushing the sequence instead of requesting a hold; second: the call was made informally (in person, off-radio) and never logged, so there's no record it happened.
- **First question:** "Given the scheduled dwell and the securement time, where's the hold request?"
- **Data to pull:** scheduled dwell for the stop, estimated securement time from the worksheet, radio log or its absence.

### A securement estimate or actual time exceeding 90 seconds with no supervisor/dispatch authorization on file
- **Usually means:** the attendant treated the 90-second figure as a soft target rather than the threshold requiring sign-off; second: an unusual rider/device combination (bariatric wheelchair, non-standard attachment points) genuinely needed longer and nobody flagged it in advance.
- **First question:** "Was this expected to run over 90 seconds before boarding started, and who signed off?"
- **Data to pull:** securement time log, dispatch/supervisor authorization record, device type noted on the manifest.

### Manifest count reconciled only at end of run, not at each stop
- **Usually means:** reconciliation was treated as an end-of-shift paperwork step rather than a per-stop safety check; second: the attendant is confident in memory and skipping the explicit count-and-log step.
- **First question:** "At which stop was the count last actually checked against the manifest, not just remembered?"
- **Data to pull:** stop-by-stop manifest log, boarding/detraining timestamps, any discrepancy note.

### Assistance provided doesn't match the rider's manifest-certified service level (curb-to-curb vs. door-to-door)
- **Usually means:** the attendant used in-the-moment judgment about what seemed reasonable rather than checking the certified service level; second: the manifest itself has a stale or incorrect service-level flag that was never corrected after an eligibility redetermination.
- **First question:** "What does the manifest say this rider is certified for, and does that match what was actually provided?"
- **Data to pull:** trip manifest service-level field, eligibility certification record, any prior complaint on this rider's account.

### A symptom beyond minor cuts/simple fainting handled without an EMS or dispatch medical-line call
- **Usually means:** the attendant made an independent judgment call that the presentation "wasn't serious enough" to escalate; second: the attendant attempted a call that didn't connect and proceeded without separately documenting why waiting wasn't an option.
- **First question:** "What made this presentation something you could fully assess without a medical consult?"
- **Data to pull:** incident log, call-attempt timestamp (if any), the specific presentation described.

### A refused securement component (belt or strap) with no documented refusal on the incident log
- **Usually means:** the attendant skipped the step under time pressure and is retroactively calling it a refusal; second: the rider did refuse, but the refusal was never written down, so there's no record distinguishing rider choice from attendant omission.
- **First question:** "Where's the logged refusal, and when relative to the securement was it recorded?"
- **Data to pull:** incident/refusal log, securement sequence log, any witness account.

### A paratransit pickup running past the promised window (commonly 30 minutes after scheduled time) with no dispatch call logged
- **Usually means:** the lateness wasn't reported in real time, so dispatch has no record to reconcile against a rider complaint; second: the attendant assumed the driver/dispatcher would handle the report and didn't confirm it happened.
- **First question:** "At what point past the window was dispatch actually notified, and by whom?"
- **Data to pull:** scheduled pickup time, actual arrival time, dispatch call log.

### An extended-dwell request pattern that recurs at the same stop across multiple days
- **Usually means:** the scheduled dwell at that stop is structurally too short for the actual mobility-assistance demand there, not an attendant performance issue; second: a specific rider's device or needs at that stop consistently exceed the standard time estimate and the schedule hasn't been adjusted to reflect it.
- **First question:** "Is this the same stop and roughly the same estimated time every time, or is it a new one-off each day?"
- **Data to pull:** hold-request log filtered by stop, scheduling department's dwell-time assumptions for that stop, any prior request to adjust the schedule.
