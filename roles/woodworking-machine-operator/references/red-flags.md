# Red flags

### Burning or scorching appearing partway through a production run
- **Usually means:** progressive cutter dulling, not a feed rate that was always too slow — the run started clean, so something changed mid-run.
- **First question:** what is the cutter's hours/usage since last sharpening, versus its service interval?
- **Data to pull:** cutter usage hours, service interval, chip load calculation for current feed/RPM settings.

### Feed rate reduced in response to a burning or finish-quality issue without checking cutter sharpness first
- **Usually means:** if the actual cause is a dulling cutter, reducing feed rate lowers chip load further and can worsen burning rather than fix it.
- **First question:** has cutter condition been checked, or was feed rate reduced as a first response?
- **Data to pull:** cutter condition/hours, chip load before and after the feed rate change.

### Tearout occurring at a specific location on a workpiece, not uniformly along its length
- **Usually means:** a grain reversal point where feed direction that worked for the rest of the piece is now against the grain.
- **First question:** does the tearout location correspond to a visible grain direction change on the workpiece?
- **Data to pull:** grain pattern of the specific workpiece, feed direction used.

### A part machined to precise spec showing warping or dimensional shift after some time in storage/use
- **Usually means:** moisture equilibration to a different environment, not a machining error at the time of production.
- **First question:** what is the moisture content history of this part, and does its storage/use environment differ from its machining environment?
- **Data to pull:** moisture content at time of machining, current storage/use environment humidity.

### Wood stock machined to final dimension without checking moisture content against the part's intended use environment
- **Usually means:** the part may be dimensioned correctly for its current moisture state but will move once it reaches a different-humidity use environment.
- **First question:** does current stock moisture content match what's appropriate for this part's final use environment?
- **Data to pull:** current moisture meter reading, target moisture content for the intended use environment.

### A chip load calculation not performed when feed rate or cutter RPM changes
- **Usually means:** an assumption that feed rate alone determines finish quality, without accounting for its relationship to RPM and edge count.
- **First question:** has chip load been recalculated for the current feed rate/RPM/edge count combination?
- **Data to pull:** current feed rate, RPM, cutter edge count, resulting chip load calculation.

### A cutter/blade used well past its typical service interval based on hours or parts produced
- **Usually means:** dulling-related defects (burning, tearout) may already be developing even if not yet visually obvious on the tool.
- **First question:** what is the actual usage count/hours on this specific cutter versus its specified service interval?
- **Data to pull:** cutter usage log, service interval specification.

### A customer/downstream complaint about a warped part attributed immediately to a machining defect
- **Usually means:** the actual cause may be moisture equilibration in the part's storage/use environment rather than the original machining.
- **First question:** what has the part's environment (humidity) been since it left machining, and does that differ significantly from machining conditions?
- **Data to pull:** part's environmental history if traceable, original machining moisture content record.

### A new wood species or grain pattern run with unchanged feed technique from a prior, different material
- **Usually means:** grain behavior (density, figure, reversal tendency) can differ meaningfully between species, and technique validated for one may not suit another.
- **First question:** has this specific species/grain pattern been evaluated for feed direction and chip load requirements, or is a prior material's settings being reused?
- **Data to pull:** current material's characteristics, prior settings being applied.

### A finished part inspected only immediately after machining, with no moisture-stability consideration before shipping/storage
- **Usually means:** dimensional stability over time hasn't been considered, only the immediate post-machining measurement.
- **First question:** does the part's specification or shipping/storage plan account for moisture equilibration risk before reaching its final use environment?
- **Data to pull:** part's moisture content at machining, planned storage/shipping conditions.
