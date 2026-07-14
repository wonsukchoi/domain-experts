# Red flags

### A visible streak or defect line at one fixed position across the fabric width, running the full roll length
- **Usually means:** a single outlier warp end or needle tension, not a beam-wide or machine-wide tension issue.
- **First question:** does the defect appear at a single fixed cross-width position, or does it vary/affect the whole width?
- **Data to pull:** tension gauge readings at the specific position and at several surrounding positions for comparison.

### A defect repeating at a regular, fixed interval along the fabric length
- **Usually means:** a specific mechanical element (a needle, heddle, or cam) tied to that interval in the machine's cycle.
- **First question:** does the defect's interval match a known mechanical cycle length for this machine (needle count, pick repeat, cam rotation)?
- **Data to pull:** the measured defect interval, the machine's mechanical cycle specifications.

### A defect appearing randomly with no consistent interval or position
- **Usually means:** yarn quality (weak spots, inconsistent twist) or an intermittent tension source rather than a fixed mechanical element.
- **First question:** does the defect correlate with a specific yarn lot or supply spool change?
- **Data to pull:** yarn lot/spool records for the affected run segment, yarn quality test data if available.

### A new pattern or gauge setup run to full production length without a test-length inspection
- **Usually means:** time pressure skipped the verification step for a new or changed configuration.
- **First question:** was a test length run and inspected against this specific setup's expected effect before the full run started?
- **Data to pull:** test-length inspection record (if one exists), setup configuration log against the job specification.

### Yarn break frequency rising over the course of a shift
- **Usually means:** a developing mechanical issue (a wearing component, a misaligned guide) or a yarn quality problem building rather than isolated random breaks.
- **First question:** are the breaks clustering at the same machine position, or scattered across different positions?
- **Data to pull:** break log with position and timestamp for the shift, maintenance history for the machine.

### Yarn breaks clustering at the same needle, end, or machine position
- **Usually means:** a specific mechanical component at that position (a worn guide, a damaged needle) rather than a general yarn or tension issue.
- **First question:** what mechanical component is specifically located at the clustering position?
- **Data to pull:** break log positions, maintenance/inspection history for that specific component.

### Overall machine tension adjusted in response to a defect without first checking individual end/needle tension
- **Usually means:** a local (single-end) problem may have been masked rather than fixed by a global adjustment.
- **First question:** was individual tension checked at the defect's specific position before the overall adjustment was made?
- **Data to pull:** individual tension gauge readings before and after the adjustment, defect recurrence status after the change.

### A finished roll passing visual inspection but showing gauge or count deviation on measurement
- **Usually means:** a subtle setup error (needle selection, stitch density setting) that isn't visually obvious but affects the fabric's specified gauge.
- **First question:** does the measured gauge/count match the job specification, or has it drifted from the intended setting?
- **Data to pull:** gauge/count measurement across the roll, setup configuration log for this job.

### A knot, splice, or repair point on a warp end showing repeated tension issues at the same location
- **Usually means:** the repair itself is the source of ongoing slack or inconsistent tension, not a new independent issue.
- **First question:** does the tension problem trace back to a specific repair point on this end?
- **Data to pull:** repair log for this end, tension readings before and after the repair was made.

### A machine returning to production after maintenance without a post-maintenance test run
- **Usually means:** the machine's post-maintenance configuration hasn't been verified to match its pre-maintenance qualified setup.
- **First question:** has a test length been run and inspected since the maintenance was completed?
- **Data to pull:** maintenance completion log, test-length inspection record since that maintenance.
