# Red flags

Smell tests a manufacturing engineer catches on a first pass over a capability study, a fixture design, a PFMEA, or a capacity request.

### Cpk reported from a control chart with an out-of-control point, a 7+-point run, or a visible trend

- **Usually means:** the process hasn't finished changing (tool wear progressing, a shift not yet root-caused), and the index will move once it settles — the number reported today isn't the number that will hold next week.
- **First question:** is the underlying Xbar-R (or Xbar-S) chart actually in statistical control — no points beyond the control limits, no non-random pattern?
- **Data to pull:** the control chart itself (not just the summary Cpk value), subgroup-by-subgroup data.

### Fixture locates the part on a surface that isn't the print's datum A/B/C

- **Usually means:** the fixture was designed for clamping convenience, not against the GD&T datum reference frame — parts will read in tolerance on the fixture but not locate correctly in the assembly or downstream operation the datums actually reference.
- **First question:** what surfaces does the print call out as datums A, B, and C, and does the fixture's locating scheme touch those specific surfaces in that precedence order?
- **Data to pull:** the print's datum feature callouts, the fixture design drawing's locator scheme.

### Locating pin diameter equals the hole's nominal or basic dimension, not its virtual condition

- **Usually means:** the pin was sized from the drawing's basic dimension instead of MMC minus position tolerance, so it will jam on a worst-case part or under-locate one using its full bonus tolerance.
- **First question:** what is this hole's virtual condition (MMC − position tolerance), and is the pin sized at or below that, minus a stated running clearance?
- **Data to pull:** the position tolerance callout and material condition modifier, the pin print.

### GR&R %contribution exceeds roughly 30% alongside a marginal or failing Cpk

- **Usually means:** the measurement system, not the process, is driving the "failure" — process changes made in response will not move a number the gauge itself can't resolve.
- **First question:** what percentage of total variation does the GR&R study attribute to the measurement system versus part-to-part variation?
- **Data to pull:** the GR&R study (AIAG MSA format), the capability study's raw data source.

### PFMEA has a severity 9 or 10 line item with no assigned action because its RPN scored low

- **Usually means:** RPN was used as a single ranking gate instead of AIAG-VDA's severity-first action-priority table, letting a high-severity, low-occurrence failure mode sit unaddressed.
- **First question:** does any severity ≥9 item lack an assigned action, regardless of its RPN?
- **Data to pull:** the PFMEA worksheet, sorted by severity independent of RPN.

### OEE performance factor under roughly 0.75 while availability is above roughly 0.85, paired with a request for a second machine

- **Usually means:** the constraint is speed (micro-stops, suppressed cycle time), not machine-hours; a second machine running at the same suppressed speed doesn't close the gap the request claims to solve.
- **First question:** what specifically drives the gap between ideal cycle time and actual cycle time — tool changes, misloads, jams — and has that been investigated before the capital request?
- **Data to pull:** cycle-time log, downtime/micro-stop code Pareto for the line.

### Control plan's standing reaction to an SPC out-of-control signal is "100% sort," unchanged across multiple occurrences

- **Usually means:** containment has been substituted for corrective action — the same signal keeps firing because nothing upstream of the sort has changed.
- **First question:** is there a closed corrective action (8D or equivalent) tied to this specific SPC signal, or only a sort log?
- **Data to pull:** the SPC alarm log and its linked corrective-action record, if one exists.

### Worst-case tolerance stacking used on a high-volume assembly where every contributor has demonstrated Cpk ≥ 1.33

- **Usually means:** tolerances are tighter than the demonstrated process capability requires, driving avoidable scrap or cost with no corresponding reliability gain.
- **First question:** does every contributor in this stack have capability data supporting statistical (RSS) tolerancing, and if so, why is worst-case still the standard?
- **Data to pull:** capability data for each individual stack contributor, the current tolerance stack-up calculation sheet.

### Tooling ordered before a DFM review checked the process against the print's tightest tolerance

- **Usually means:** the process route was assumed capable rather than verified, and a mismatch surfaces only at first-article inspection — after the tooling is already cut.
- **First question:** what process capability data supports the selected process holding this specific tolerance, and was that checked before tooling was released to the vendor?
- **Data to pull:** the DFM checklist (or its absence), historical capability data for the same feature type on the same process class.

### PPAP submitted with Cpk instead of Ppk on a process with fewer than roughly 300 parts of production history

- **Usually means:** the study is being treated as a long-term ongoing-capability study when it's actually an initial/short-run study, which should use Ppk (overall variation, no in-control assumption) rather than Cpk.
- **First question:** how many production parts has this process actually run, and is the submitted index appropriate for that study's maturity?
- **Data to pull:** the capability study's sample size and collection window, the PPAP submission level required by the customer.
