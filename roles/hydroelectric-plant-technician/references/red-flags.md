# Red flags

### A flow rate setpoint held unchanged despite a significant reservoir head change
- **Usually means:** the previously-safe operating point may now fall outside the turbine's cavitation-safe range for the current head.
- **First question:** has the safe/efficient operating range been recalculated for the current head, or is the setpoint carried over from a different head condition?
- **Data to pull:** current reservoir level/head, the turbine's characteristic operating range at that specific head.

### Generation output optimized without first confirming mandated environmental/fish-passage flow is satisfied
- **Usually means:** a compliance violation risk exists if generation scheduling reduces flow below the required minimum.
- **First question:** has the mandated minimum flow been verified as satisfied before optimizing for power output?
- **Data to pull:** mandated minimum flow requirement, actual flow release data.

### Governor tuning assumed correct because the unit generates power normally under steady conditions
- **Usually means:** actual frequency response behavior (speed, deadband) hasn't been verified, and steady-state generation doesn't reveal a tuning issue.
- **First question:** has governor response been tested against an actual or simulated frequency deviation, or only observed under steady-state operation?
- **Data to pull:** governor tuning verification/test record, response characteristics observed.

### A unit operating at a flow rate near the edge of its characterized safe range for the current head
- **Usually means:** limited margin before cavitation risk becomes significant if head shifts further or flow increases.
- **First question:** how much margin exists between the current operating point and the edge of the safe range at this head?
- **Data to pull:** current operating point, safe range boundaries for current head.

### A scheduled runner inspection overdue or skipped
- **Usually means:** cavitation damage, if present, has had additional time to accumulate without detection.
- **First question:** when was the runner last inspected, and does current operating history suggest elevated cavitation risk since then?
- **Data to pull:** inspection schedule/history, operating point history relative to safe range.

### Reduced power output at a lower reservoir level attributed to "just how it is" without recalculating the actual safe operating range
- **Usually means:** the output reduction may not reflect the actual optimal safe point for the current head, if the range wasn't specifically recalculated.
- **First question:** was the current operating point set based on a recalculated safe range for this head, or just reduced by an arbitrary amount?
- **Data to pull:** current head, recalculated safe range, actual operating point selected.

### A unit's frequency support performance questioned by the grid operator with no recent governor verification available
- **Usually means:** governor tuning may have drifted or never been properly verified, and there's no data to confirm or rule this out.
- **First question:** when was governor response last tested, and does the data show whether it meets expected response characteristics?
- **Data to pull:** governor test history, grid operator's specific performance concern.

### Cavitation damage found at inspection with no correlation check against the operating history that preceded it
- **Usually means:** the specific operating conditions (head, flow, duration) that likely caused the damage haven't been identified, missing a chance to prevent recurrence.
- **First question:** does the operating log show periods where flow/head combinations fell outside the safe range before this damage was found?
- **Data to pull:** operating log/history, head/flow data correlated with the inspection findings.

### An environmental flow requirement treated as flexible or negotiable against generation revenue considerations
- **Usually means:** the requirement is being treated as a soft priority rather than the hard compliance constraint it actually is.
- **First question:** is the mandated flow being treated as a fixed constraint to satisfy first, or as one input balanced against generation optimization?
- **Data to pull:** the actual regulatory/permit requirement, how generation scheduling decisions are being made relative to it.
