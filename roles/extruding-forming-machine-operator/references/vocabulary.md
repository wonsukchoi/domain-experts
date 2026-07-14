# Vocabulary

### Die swell
The expansion of a polymer melt's cross-section after exiting an extrusion die, caused by viscoelastic recovery of the material's molecular orientation under flow, meaning the extrudate is larger than the die opening itself.
**In use:** "Die's set at 3.850 for a target of 4.000 OD — the difference is expected swell, not a mistake in the die dimension."
**Common misuse:** Setting a die's opening dimension equal to the target final part dimension — the die opening and the finished part's dimension are related but not identical, and the gap between them (swell, plus draw-down effects) is a real, material-specific value that needs to be characterized, not assumed to be zero.

### Draw-down ratio
The ratio between the extrudate's velocity at the die exit and its velocity after being pulled by the takeoff/puller equipment, which determines how much the extrudate is stretched and thinned before it solidifies.
**In use:** "Bumping takeoff speed without adjusting extrusion rate increases draw-down ratio — that's what thinned the wall, not a sizing problem."
**Common misuse:** Treating takeoff speed as a simple output-rate control independent of dimensional effects — changing takeoff speed alone changes draw-down ratio, which directly affects wall thickness even when a downstream sizing system holds outer diameter to spec.

### Residence time
The duration material spends inside the extruder barrel and die at processing temperature, which — combined with melt temperature — determines exposure to thermal degradation risk.
**In use:** "Slower line speed means longer residence time in the barrel — we're watching for any degradation signs at this new rate."
**Common misuse:** Treating melt temperature as the only variable relevant to degradation risk — residence time compounds with temperature, so a temperature that's safe at normal line speed can become risky at a slower speed that extends how long material sits in the hot zone.

### Sizing calibration (calibrator, vacuum sizing)
Equipment downstream of the die that constrains the still-soft extrudate to its final target dimension as it cools, typically using vacuum or mechanical constraint — the actual point where final outer dimension is locked in.
**In use:** "Sizing tank's the real dimensional control here — the die gets us close, but the calibrator sets what actually solidifies."
**Common misuse:** Treating the die as the primary or sole determinant of final part dimension — sizing/calibration equipment is what constrains the extrudate to its actual final shape after die swell and draw-down have already occurred, making it at least as important a control point as the die itself.

### Melt homogeneity
The uniformity of temperature, mixing, and material consistency within the molten polymer as it's processed through the extruder, affecting both flow behavior and final part quality.
**In use:** "We need enough temperature and screw work to get proper melt homogeneity — but not more than that, since extra heat just adds degradation risk without adding benefit."
**Common misuse:** Assuming more heat or longer mixing always improves melt quality — once homogeneity is adequate, additional temperature or residence time provides no further benefit and only adds degradation risk.

### Wall thickness (vs. outer diameter)
Two related but distinct dimensional measurements on a hollow extruded product (like pipe) — outer diameter describes the outside dimension, wall thickness describes the material thickness between inner and outer surfaces, and one can be in spec while the other isn't.
**In use:** "OD's fine, but check wall thickness separately — draw-down affects the two differently."
**Common misuse:** Treating outer diameter as a proxy for overall dimensional health, assuming wall thickness follows automatically if OD is in spec — sizing equipment specifically constrains OD, but wall thickness depends on how much material was present per unit length before that constraint was applied, which is a separate variable.

### Screw wear (extruder)
Gradual physical degradation of an extruder's screw (flight wear, reduced compression ratio) that changes the machine's actual output and mixing behavior over time, independent of programmed setpoints.
**In use:** "Output's drifted down over the past few weeks at the same screw speed setting — that tracks with screw wear, not a material change."
**Common misuse:** Assuming a machine's output and mixing performance stay constant over time as long as setpoints are unchanged — mechanical wear changes actual performance gradually, in a way that a fixed setpoint doesn't account for or reveal directly.

### Process characterization
The documented, validated relationship between a specific material, die, and process settings that establishes the correct compensation (for swell, draw-down, and other effects) needed to hit a target final dimension.
**In use:** "We're not guessing at die dimension — this is from the process characterization run we did when this material/die combination was first qualified."
**Common misuse:** Assuming process characterization from one material or die transfers directly to a different material or die combination — the swell and draw-down relationships are specific to the actual material and tooling combination, not a universal constant.

### Compaction (powder compacting)
The process of pressing powdered material (metal, ceramic) into a coherent shape under pressure, typically followed by a sintering step, where compaction density and pressure directly affect the final part's structural properties.
**In use:** "Compaction pressure's set to hit target green density before sintering — too low and we get porosity issues downstream."
**Common misuse:** Treating a compacted "green" part's visual completeness as sufficient confirmation of quality — density and structural integrity depend on actual compaction pressure achieved, which isn't necessarily visible by looking at the pressed part before sintering.
