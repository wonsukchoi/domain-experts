# Vocabulary

### WPS (Welding Procedure Specification)
The qualified document specifying the parameter range — process, material, filler, amperage, voltage, travel speed, preheat — a welder must follow for a given joint.
**In use:** "WPS-117 qualifies 20 to 35 kJ/in for this joint — stay in that band regardless of how the bead looks."
**Common misuse:** Treating it as a general guideline rather than a binding qualified range; welding outside it is unqualified work even if the result looks acceptable.

### PQR (Procedure Qualification Record)
The test record documenting that a specific set of welding parameters was actually tested and produced welds meeting required mechanical properties.
**In use:** "That WPS is only valid because it traces back to a PQR with tensile and Charpy results on file."
**Common misuse:** Assuming a WPS is valid because its parameters "look reasonable," when only an actual PQR with tested results backs the procedure's claimed properties.

### Heat input
The energy delivered per unit length of weld (commonly kJ/in or kJ/mm), calculated from voltage, amperage, and travel speed.
**In use:** "Recompute heat input before accepting that pass — travel speed went up but nobody adjusted amperage."
**Common misuse:** Judging weld quality from bead appearance alone; heat input is invisible externally but is what actually correlates with heat-affected-zone mechanical properties.

### Carbon equivalent (CE)
A formula combining a steel's alloy content (carbon, manganese, chromium, molybdenum, vanadium, nickel, copper) into a single number predicting susceptibility to hydrogen cracking.
**In use:** "CE comes out to 0.37 on this heat — under the 0.40 threshold, so we're clear on preheat for this thickness."
**Common misuse:** Looking only at carbon content when judging cracking risk, ignoring that manganese and other alloying elements contribute significantly to the actual CE value.

### Preheat / interpass temperature
The minimum temperature (preheat) held before welding starts and the temperature range (interpass) maintained between passes on a multi-pass weld.
**In use:** "Preheat's holding at 225°F, but check interpass before starting pass three — it's cooled more than the WPS allows."
**Common misuse:** Treating preheat as a one-time step done only before the first pass, when interpass temperature has to be actively controlled between every subsequent pass too.

### Heat-affected zone (HAZ)
The region of base metal adjacent to a weld whose microstructure changed from welding heat without actually melting.
**In use:** "Weld metal passed the bend test, but HAZ toughness is the property this heat-input range was actually qualified for."
**Common misuse:** Assuming HAZ properties are automatically fine if the weld metal itself passes inspection; HAZ toughness is a separate property governed by heat input and cooling rate, not weld-metal quality.

### Backstep / skip welding sequence
A technique of welding short segments in a planned, non-continuous order to balance heat input and control distortion across a joint.
**In use:** "Sequence this seam as backstep — welding it straight through in one pass is what's been warping the flange."
**Common misuse:** Treating distortion as an unavoidable side effect of welding, rather than something actively controlled through sequence and fixturing planned before the arc is struck.

### Undercut
A groove melted into the base metal at the weld toe that's left unfilled by weld metal — a specific, defined defect type.
**In use:** "That's undercut past the 1/32" limit on this code — grind and reweld, not just cosmetic."
**Common misuse:** Describing any visible groove at the weld toe as "just cosmetic," when undercut reduces effective cross-section and is a specific rejectable defect above a defined depth threshold.

### Lack of fusion
A weld defect where filler metal fails to fully fuse with the base metal or a previous pass, often subsurface and invisible to the eye.
**In use:** "Surface looks fully fused, but UT is showing lack of fusion at the root — that's why we run NDT."
**Common misuse:** Assuming a weld that looks fully fused on the surface has no lack of fusion beneath it — that assumption is exactly what NDT exists to check.

### NDT (Non-Destructive Testing)
Inspection methods — radiographic (RT), ultrasonic (UT), magnetic particle (MT), dye penetrant (PT) — that detect weld defects without damaging the part.
**In use:** "This joint's code-required RT, not just visual — schedule it before final acceptance."
**Common misuse:** Treating a passed visual inspection as equivalent to passing NDT; many rejectable defects, like lack of fusion or subsurface porosity, are only detectable by NDT methods.
