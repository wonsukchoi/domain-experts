# Red flags

### Climb milling selected without checking this specific machine's backlash characteristics
- **Usually means:** risk of an uncontrolled dig-in if the machine's feed mechanism has meaningful backlash.
- **First question:** has this machine's backlash been characterized, and does it support climb milling safely for this operation?
- **Data to pull:** machine backlash specification/history, milling direction selected.

### Workholding confirmed only by a static "is it clamped" check, not evaluated against expected cutting forces
- **Usually means:** the workpiece could shift during cutting even though it appeared securely held before the cut started.
- **First question:** has the fixture/clamping been evaluated for the specific lateral forces this operation will generate, or just confirmed as "clamped"?
- **Data to pull:** expected cutting force for this operation, fixture/clamp rating.

### A dimensional error found post-cut with no corresponding pre-cut setup issue identified
- **Usually means:** the workpiece likely shifted during cutting from inadequate workholding rigidity, since the setup looked fine beforehand.
- **First question:** does the error pattern suggest workpiece movement during the cut (a shift or twist) rather than a programming/tool issue?
- **Data to pull:** the dimensional error's location/pattern, workholding force analysis for this operation.

### A long, narrow end mill run at standard depth-of-cut parameters for a short, rigid cutter
- **Usually means:** cutter deflection risk hasn't been accounted for, producing a tapered or bowed cut wall.
- **First question:** does this cutter's length-to-diameter ratio at full stickout call for reduced parameters or multiple passes?
- **Data to pull:** cutter length-to-diameter ratio, depth of cut/pass strategy used.

### A deep pocket or slot attempted in a single pass rather than a roughing-then-finishing sequence
- **Usually means:** elevated risk of tool breakage and deflection-driven dimensional/finish defects.
- **First question:** does the total depth relative to the cutter's diameter/rigidity call for a multi-pass strategy?
- **Data to pull:** total depth, cutter diameter, pass strategy used.

### A milled slot or pocket showing measurable taper (narrower or wider at depth than at the surface)
- **Usually means:** cutter deflection under load, likely from an excessive single pass or an insufficiently rigid cutter for the depth attempted.
- **First question:** was the feature cut in a single deep pass, and does the cutter's length-to-diameter ratio suggest deflection risk?
- **Data to pull:** measured taper, pass strategy, cutter length-to-diameter ratio.

### A critical deep/narrow feature's dimensions confirmed only by trusting the programmed toolpath, not direct measurement
- **Usually means:** actual cutter deflection during the cut wouldn't be caught, since the program doesn't reflect real-world deflection.
- **First question:** was the actual cut dimension measured, or was the programmed toolpath assumed to represent the actual result?
- **Data to pull:** in-process or post-cut measurement data if performed.

### Tool breakage occurring on a deep pocket/slot operation
- **Usually means:** excessive single-pass depth or cutting force for the cutter's rigidity, rather than a random tool defect.
- **First question:** does the pass strategy and depth of cut match what this specific cutter's geometry can support?
- **Data to pull:** pass strategy/depth used, cutter specification.

### A new material or cutter combination run using milling direction/parameters carried over from a prior, different setup
- **Usually means:** settings validated for a different material/cutter combination may not be appropriate for the new one.
- **First question:** were parameters (milling direction, depth strategy) re-verified for this specific material/cutter combination?
- **Data to pull:** current material/cutter specification, parameters used.

### A recurring dimensional issue across multiple parts from the same setup
- **Usually means:** a systematic cause (workholding, climb/conventional mismatch, cutter deflection at a consistent depth) rather than isolated part-to-part variation.
- **First question:** do the affected parts share a common setup, cutter, or milling direction?
- **Data to pull:** affected parts' common process characteristics.
