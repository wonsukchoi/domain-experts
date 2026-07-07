# Red flags

Smell tests a senior tower technician catches before a climb starts or before signing off a completed job.

### NOC ticket says "power reduced" or "cleared" with no dB value stated

- **Usually means:** the reduction applied may be far less than what the job requires — a 3 dB (half-power) reduction is common as a default courtesy step but frequently insufficient to bring the work position under MPE (maximum permissible exposure).
- **First question:** "What's the actual dB reduction, and has it been confirmed against our survey reading at the work position?"
- **Data to pull:** the prior RF survey's power density at the planned work position, the occupational MPE for that frequency band, and the specific attenuation value the NOC applied.

### Only a ground-level or entry-point RF reading was taken

- **Usually means:** the survey wasn't done at the actual work position — power density falls off sharply with distance from the radiating face, so a reading at the base or an access hatch says little about exposure at the antenna mount.
- **First question:** "Where exactly was this reading taken, and how far is that from where the work happens?"
- **Data to pull:** the survey report's stated measurement location and distance from the antenna face; if unavailable, request a re-survey or use a personal RF monitor at the work position before starting.

### Co-located carrier's antenna wasn't included in the power-down request

- **Usually means:** the work order was scoped to one carrier's job, but the tower hosts other carriers' live antennas within RF range of the same work position.
- **First question:** "Which other carriers have antennas on this structure within range of the work location, and have they been contacted?"
- **Data to pull:** the tower's full antenna/sector inventory and owner-of-record for each, cross-checked against the planned work position.

### VSWR reading above 2.0:1 (return loss below 10 dB) after a "completed" installation

- **Usually means:** a connector, jumper, or weatherproofing fault introduced during installation — less commonly a defective antenna.
- **First question:** "Has the jumper and connector torque been checked before assuming the antenna itself is at fault?"
- **Data to pull:** VSWR trend if available (pre- vs. post-installation), connector torque log, weatherproofing inspection notes.

### PIM fails site spec while VSWR passes

- **Usually means:** a mechanically adequate but electrically marginal connection — micro-arcing, dissimilar-metal contact, or a corroded/rusted structural component in the RF path, not a standing-wave problem.
- **First question:** "Which connections were re-torqued or replaced most recently, and is there any rusted hardware near the RF path?"
- **Data to pull:** the site's RFDS (RF Design Sheet) PIM acceptance threshold, recent maintenance/replacement log for hardware near the antenna and grounding kit.

### Generic or site-nonspecific rescue plan on file

- **Usually means:** the rescue plan was filed at onboarding or for a different structure and never updated for this tower's actual anchor layout, obstructions, or crew composition.
- **First question:** "Has this plan been validated against this specific tower and today's crew, or is it the standing plan on file?"
- **Data to pull:** the plan's stated structure ID and last-validated date; anchor and obstruction layout for the actual tower being climbed today.

### Climber observed unclipped during a structural transition, even briefly

- **Usually means:** normalization of a short-cut during ladder-to-platform or platform-to-mount transitions — exactly where NATE's incident data concentrates, regardless of how routine the move looks.
- **First question:** "Why was that transition not covered by a continuous tie-off point or a temporary anchor?"
- **Data to pull:** the route plan's anchor-point sequence and whether a gap exists at that transition; equipment inspection tags for the gear in use.

### Fall-protection equipment tag expired or inspection undocumented

- **Usually means:** either a missed inspection cycle or shared/borrowed gear assumed good without a fresh check.
- **First question:** "When was this specific harness/lanyard last inspected, and by whom?"
- **Data to pull:** the equipment's inspection log and tag date; whether it's assigned to this climber or shared.

### Tower obstruction light outage discovered more than 30 minutes after it likely started

- **Usually means:** no outage-monitoring system in place, or the monitoring system's alert wasn't acted on promptly — relying on drive-by inspection cadence virtually guarantees missing the FCC's 30-minute FAA notification window.
- **First question:** "Do we have an active outage-monitoring system on this structure, and was an alert missed or not present?"
- **Data to pull:** the monitoring system's alert log (if any), time of last confirmed light-status check, and the FAA notification timestamp versus the estimated outage start.

### Antenna azimuth or downtilt reading off the RFDS spec at commissioning

- **Usually means:** installation error or mount hardware that shifted during final torque-down; a commonly cited field tolerance is roughly ±2–3° azimuth and a much tighter mechanical-downtilt tolerance, but the only real spec is the site's own RFDS — treat any generic tolerance as a heuristic, not the standard.
- **First question:** "What does this site's RFDS specify for azimuth and downtilt, and how far off is the as-built reading?"
- **Data to pull:** the RFDS target values, as-built survey/inclinometer reading, and mount hardware inspection for slippage.

### RF-awareness or NATE climber certification lapsed for a crew member

- **Usually means:** a scheduling gap in recertification tracking, not a deliberate skip — but it means that person isn't authorized to make independent climb/RF calls today.
- **First question:** "Is everyone on this crew currently certified, and who's tracking recert dates?"
- **Data to pull:** the crew's current certification status and expiration dates against today's roster.
