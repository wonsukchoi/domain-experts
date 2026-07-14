# Red flags

### A dimension trending in one direction across consecutive in-process measurements
- **Usually means:** progressive tool wear, even if each individual reading remains within tolerance.
- **First question:** what is the rate of drift, and when does extrapolation predict it will cross the tolerance limit?
- **Data to pull:** the full sequence of in-process measurements (not just the latest), tool part-count/hours since last change.

### A tool offset adjusted repeatedly over a short span without a corresponding tool change
- **Usually means:** wear is being compensated rather than addressed, and may be accelerating past the tool's characterized life.
- **First question:** how many offset adjustments have been made on this tool since its last replacement, and at what part-count intervals?
- **Data to pull:** offset adjustment log with timestamps/part counts, tool's characterized expected life.

### A part failing inspection with no obvious program or tool cause
- **Usually means:** a work-holding repeatability issue rather than a program or tool problem — the two can produce identical-looking dimensional symptoms.
- **First question:** does the fixture seat and clamp consistently, verified directly, or has that only been assumed?
- **Data to pull:** fixture repeatability check results, recent fixture maintenance/repair history.

### Production run started immediately after a setup change without a first-article inspection
- **Usually means:** time pressure skipped the validation step confirming program, offsets, and fixture are correct together.
- **First question:** has a first-article part actually been measured against the full print, or just visually checked?
- **Data to pull:** first-article inspection report (if one exists) for this setup.

### A machine alarm cleared and the cycle resumed without inspecting the in-process part or tool
- **Usually means:** the alarm's underlying cause (a collision, a broken tool, an out-of-tolerance condition) wasn't verified before continuing.
- **First question:** was the in-process part and the tool condition physically checked before the alarm was cleared?
- **Data to pull:** alarm log with cause code if available, inspection record (or lack of one) immediately following the alarm.

### A new material lot or supplier change with no re-verification of tool wear rate
- **Usually means:** a harder or more abrasive material lot could accelerate tool wear beyond its characterized rate for the previously qualified material.
- **First question:** has this specific material lot's hardness/composition been checked against what the tool life curve was characterized for?
- **Data to pull:** incoming material lot certification, tool wear rate observed on this lot vs. historical baseline.

### In-process sampling frequency unchanged despite a detected trend approaching the tolerance limit
- **Usually means:** the standard sampling interval doesn't provide adequate margin once a trend is confirmed, and needs tightening.
- **First question:** does the current sampling interval leave enough parts between checks that several could be produced out of tolerance before the next check catches it?
- **Data to pull:** current sampling interval, projected part count until the trend crosses tolerance.

### A fixture returning to production after repair or a long idle period without a repeatability check
- **Usually means:** the fixture's post-repair or post-idle condition hasn't been verified to match its previously qualified repeatability.
- **First question:** has a repeatability check (running multiple cycles and measuring consistency) been performed since the repair or idle period?
- **Data to pull:** fixture maintenance/repair log, repeatability check results if performed.

### A tool change made without updating the corresponding offset in the control
- **Usually means:** the new tool's actual geometry/wear state doesn't match the offset value still active in the program.
- **First question:** was the offset re-zeroed or re-measured for the new tool, or is the prior tool's offset still in effect?
- **Data to pull:** tool change log, offset values before and after the change.

### Two or more machines running the same program showing different measurement trends
- **Usually means:** a machine-specific factor (tool condition, fixture repeatability, machine calibration) rather than a program issue, since the program is identical.
- **First question:** do the machines share the same tool age/condition and fixture repeatability status, or do they differ?
- **Data to pull:** tool life status and fixture repeatability data for each machine.
