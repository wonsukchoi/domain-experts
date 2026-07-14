# Red flags

### Spindle RPM held constant across a stepped part with meaningfully different diameters
- **Usually means:** surface speed varies significantly between sections, producing inconsistent cutting conditions and finish.
- **First question:** was RPM recalculated for each distinct diameter section to maintain consistent surface speed, or held constant throughout?
- **Data to pull:** RPM used at each section, target surface speed, calculated actual surface speed at each diameter.

### A precision turning operation started without verifying workpiece runout
- **Usually means:** an eccentric or out-of-round part could result even with a correctly programmed toolpath and sharp tool.
- **First question:** was runout checked with a dial indicator before starting, or assumed acceptable from standard chucking procedure?
- **Data to pull:** runout measurement if performed, the operation's runout tolerance requirement.

### A long, slender workpiece run with standard cutting parameters used for shorter, rigid workpieces
- **Usually means:** chatter/vibration risk from reduced workpiece rigidity hasn't been accounted for.
- **First question:** does this workpiece's length-to-diameter ratio call for reduced parameters or additional support (steady rest, tailstock)?
- **Data to pull:** workpiece length-to-diameter ratio, cutting parameters used, presence/absence of support fixtures.

### Surface finish measured rougher than specification despite feed rate already reduced
- **Usually means:** the finish issue may be driven by tool nose radius or cutting speed, not feed rate, and reducing feed alone didn't address the actual cause.
- **First question:** have tool nose radius and actual surface speed been checked, or was feed rate the only parameter adjusted?
- **Data to pull:** tool nose radius, actual surface speed used, feed rate history for this operation.

### A critical turned dimension checked only visually or at the end of a long run
- **Usually means:** tool-wear-driven dimensional drift could have developed mid-run without being caught.
- **First question:** was the dimension measured periodically during the run, or only inspected visually/at completion?
- **Data to pull:** in-process measurement records if any, tool usage/wear status.

### A part showing chatter marks or vibration-related surface defects
- **Usually means:** workpiece rigidity (length-to-diameter ratio) or cutting parameters exceeding what the setup can support without vibration.
- **First question:** does the workpiece's length-to-diameter ratio and current cutting parameters match what's appropriate, or is chatter risk being ignored?
- **Data to pull:** workpiece dimensions, cutting parameters, support fixture usage.

### A new material or tool combination run using surface speed values carried over from a different material/tool setup
- **Usually means:** the optimal surface speed for this specific material/tool pairing may differ from what was previously used.
- **First question:** does the current material/tool combination match what the surface speed value was originally established for?
- **Data to pull:** current material/tool specification, surface speed reference used.

### Multiple parts from the same job showing a similar dimensional or finish issue
- **Usually means:** a systematic cause (chucking method, RPM/surface speed miscalculation, tool wear) rather than isolated part-to-part variation.
- **First question:** do the affected parts share a common setup, tool, or process step?
- **Data to pull:** affected parts' common process characteristics, setup/tool history.

### A chuck or workholding fixture not recently inspected for wear affecting its centering accuracy
- **Usually means:** the fixture itself may no longer center a workpiece as accurately as when originally qualified.
- **First question:** when was this specific chuck/fixture last verified for centering accuracy?
- **Data to pull:** fixture inspection/verification log.

### A dimensional or finish defect diagnosed and "fixed" without checking chucking, surface speed, chatter, and tool wear as distinct possible causes
- **Usually means:** the actual root cause among several possible distinct causes may not have been correctly identified.
- **First question:** were each of these potential causes checked individually, or was one assumed without ruling out the others?
- **Data to pull:** the diagnostic steps actually taken, the specific corrective action applied.
