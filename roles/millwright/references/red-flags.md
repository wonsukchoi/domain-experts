# Red flags

Smell tests a millwright or install inspector catches in the first pass over a job — during the install itself or when diagnosing a post-startup problem.

### Vibration climbs weeks after startup with no process change

- **Usually means:** grout hadn't reached full cure/strength before final alignment and torque were locked in, or anchor-bolt torque relaxed as the grout finished curing and the base shifted slightly under the running machine.
- **First question:** what was the interval between grout pour and final alignment, versus the manufacturer's specified cure-to-alignment milestone?
- **Data to pull:** grout pour ticket and ambient-temperature log during cure, date of final alignment, current alignment reading versus as-left reading, anchor-bolt torque check.

### Sling angle under 30° from horizontal on a load using more than half the sling's rated capacity

- **Usually means:** the rigger chose a convenient anchor point over correct geometry, or headroom constraints weren't surveyed before the lift was planned.
- **First question:** what's the actual included angle, and does the recalculated per-leg tension still fall inside the sling's rated capacity at that angle?
- **Data to pull:** rigging plan/sling-angle diagram, sling WLL tag and certification, headroom/clearance survey, recalculated per-leg tension.

### Laser alignment offset changes by more than ~1 mil between two consecutive checks with no work performed between them

- **Usually means:** soft foot wasn't corrected before the readings, the base wasn't fully torqued, or one check was cold and the other was at operating temperature.
- **First question:** was soft foot checked and corrected at every foot, and were both readings taken at the same machine temperature?
- **Data to pull:** soft-foot readings per foot, anchor-bolt torque log, machine temperature at each check, time elapsed between checks.

### Gearbox running noticeably hotter or noisier within the first week

- **Usually means:** backlash set too tight (binding from an over-corrected alignment) or output-shaft alignment to driven equipment is outside OEM spec.
- **First question:** what backlash and alignment readings were recorded at handoff, and how do they compare to the OEM spec range?
- **Data to pull:** backlash dial-indicator readings at multiple rotational positions, OEM backlash spec sheet, final alignment report, oil/bearing temperature trend since startup.

### Foundation elevation survey shows more than 1/16 in of settling difference across the base within 30 days

- **Usually means:** soil or foundation wasn't adequately consolidated before the pour, or the grout didn't fully fill under the baseplate, leaving voids that compress under load.
- **First question:** was a soil test or preload/surcharge performed, and is there evidence of grout voids?
- **Data to pull:** pre-pour soil report, elevation survey history, grout pour records, sounding/tap test or core-sample results.

### Crane pick point wasn't calculated against a verified center of gravity for an asymmetric skid

- **Usually means:** the rigger used the geometric center or a convenient lug location instead of computing CG from vendor weight and dimension data — risking the load tipping or overloading one sling leg during the lift.
- **First question:** what's the calculated CG location from vendor data, and does it match the pick point actually used?
- **Data to pull:** vendor weight/dimension data per component, CG moment calculation, bridle/sling configuration used, tilt readings during the test lift.

### As-left alignment numbers sit exactly at the tolerance limit for the coupling's RPM, not comfortably inside it

- **Usually means:** the crew stopped as soon as the reading technically passed, leaving no margin for thermal growth in operation or for settling still in progress in a recently poured foundation.
- **First question:** is the reading in the "excellent" band or merely at the edge of "acceptable" for this RPM, and has the base fully cured and stabilized?
- **Data to pull:** the alignment tolerance chart for this coupling's operating RPM, cure-completion date, hot (running) alignment check if one hasn't been done yet.

### Drive-train alignment measured with a tape measure and eyeball instead of laser or dial instrumentation

- **Usually means:** schedule pressure, or the crew defaulting to a method appropriate for a low-speed, non-critical application on a drive that actually needs precision instrumentation.
- **First question:** what RPM and tolerance band does this drive actually require, and does the method used resolve to that precision?
- **Data to pull:** OEM tolerance spec for the coupling, measurement method and instrument used, as-left readings, RPM/HP nameplate data.

### Anchor bolts torqued to full spec before the grout has reached the manufacturer's minimum cure strength for that action

- **Usually means:** schedule pressure overrode a cure hold point; the load path through the grout may not develop as the design assumes.
- **First question:** what compressive strength has the grout reached at the time of torquing, versus the data sheet's minimum for full torque?
- **Data to pull:** grout cure log with temperatures, manufacturer strength-versus-time curve, cube/cylinder break test results if taken, torque log with timestamps.

### Gearbox backlash measured at only one rotational position

- **Usually means:** gear or coupling eccentricity and shaft runout are masked by a single-point reading, giving false confidence in a number that varies significantly elsewhere in the rotation.
- **First question:** was backlash checked at a minimum of four rotational positions, and how much variation showed up between them?
- **Data to pull:** multi-position backlash log, shaft runout measurement, OEM/AGMA backlash tolerance range.
