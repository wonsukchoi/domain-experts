# Red flags

### A station's cycle time consistently exceeding or running under takt time
- **Usually means:** a process, tooling, or material change has affected the station, requiring investigation rather than individual compensation.
- **First question:** has anything about the parts, tooling, or process at this station changed recently?
- **Data to pull:** cycle time trend for the station over the shift, any recent material/tooling/supplier changes.

### A worker intermittently skipping or rushing through a standard work step to keep pace
- **Usually means:** an unreported line-balance problem is being individually compensated for in a way that creates a hidden quality risk.
- **First question:** is a step actually being skipped, and if so, does that step affect a safety- or function-critical feature?
- **Data to pull:** standard work instructions for the step, production sequence log to identify affected units if skipping is confirmed.

### An upstream station's output looking different from the normal pattern
- **Usually means:** a developing issue at that station (tooling wear, a part quality shift, an operator deviation) that hasn't yet been caught there.
- **First question:** does this variation fall within a documented acceptable range, or is it genuinely outside normal appearance?
- **Data to pull:** the documented acceptable-variation range/limit samples for this feature, recent history of similar observations.

### A missing or defective part substituted with an available-but-different part to keep the line moving
- **Usually means:** schedule pressure led to a workaround instead of an escalation, risking an undocumented deviation reaching the finished product.
- **First question:** was this substitution documented and escalated, or made silently to avoid stopping the line?
- **Data to pull:** parts issue log, any escalation record for this specific shortage.

### Stop-the-line/andon not pulled despite a suspected defect being verbally mentioned
- **Usually means:** hesitation due to proximity to a break, shift-end target, or social pressure not to stop the line.
- **First question:** was the suspected defect actually verified and contained, or just mentioned and left unresolved?
- **Data to pull:** andon pull log for the relevant time period, any verbal reports not matched by a formal stop.

### A worker using a personally-developed method different from documented standard work
- **Usually means:** either a genuine improvement not yet formalized, or an undocumented deviation that removes the comparison baseline for detecting real problems.
- **First question:** has this method been proposed and approved through the standard work update process, or is it being used informally?
- **Data to pull:** current approved standard work document, any pending standard work change proposals.

### A quality escape traced back to a period of known line-balance disruption
- **Usually means:** the disruption period itself needs containment review, since other units from the same window may share the same risk.
- **First question:** what other units were produced during the same disruption window, and have they been identified and checked?
- **Data to pull:** production sequence log for the disruption period, containment/rework status for units from that window.

### Station rotation happening without the incoming operator being told about recent issues at that station
- **Usually means:** handoff at rotation isn't including issue-specific context, just task assignment.
- **First question:** does the rotation handoff include any recent anomalies or issues specific to this station, or just "here's your station"?
- **Data to pull:** station-specific issue log, rotation handoff record if one exists.

### A recurring near-miss or close-call at the same station across multiple shifts
- **Usually means:** an underlying condition at that station hasn't been addressed, and each occurrence is being treated as isolated.
- **First question:** does the issue log show a pattern across shifts at this specific station, or does each report stand alone?
- **Data to pull:** station-specific issue/near-miss log across recent shifts.

### A team member observed making the same standard-work deviation repeatedly
- **Usually means:** either insufficient training on the correct method, or an unaddressed underlying reason (time pressure, tooling difficulty) driving the deviation.
- **First question:** does the worker understand the correct standard work, or is there a structural reason they're deviating from it?
- **Data to pull:** training record for this worker/station, any prior coaching or correction for this specific deviation.
