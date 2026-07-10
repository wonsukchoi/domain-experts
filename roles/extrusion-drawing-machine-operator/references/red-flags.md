# Red flags

### Draw pass reduction calculated from diameter change alone, without converting to actual area reduction
- **Usually means:** the actual reduction may exceed the material's ductility limit even though the diameter-based figure looks safe.
- **First question:** what does the actual area reduction calculate to, versus the diameter-based figure?
- **Data to pull:** start and end diameters converted to area reduction, compared against the material's per-pass limit.

### A draw pass proceeds despite cumulative area reduction since the last anneal approaching the material's total-before-anneal limit
- **Usually means:** risk of wire/tube breakage from accumulated work hardening not yet relieved by annealing.
- **First question:** what is the actual cumulative area reduction since the last anneal, versus the material's documented limit?
- **Data to pull:** the cumulative reduction tracker since the last anneal, compared against the alloy's total-before-anneal limit.

### Extrusion die opening sized to the final target dimension with no die swell compensation
- **Usually means:** the finished profile will come out oversized once the material relaxes after exiting the die.
- **First question:** what die swell percentage is expected for this material and these process conditions?
- **Data to pull:** the die opening dimension compared against the target dimension and the material's expected swell percentage.

### Extrusion line speed increased to hit a production target without verifying cooling/sizing capacity at that speed
- **Usually means:** dimensional drift from incomplete cooling before the profile reaches the sizing tooling, independent of correct die sizing.
- **First question:** does the cooling/sizing system's rated capacity actually cover this line speed for this material?
- **Data to pull:** line speed compared against the cooling/sizing system's rated capacity for this material and profile size.

### A dimensional deviation is corrected by adjusting an unrelated process variable rather than the one most likely responsible
- **Usually means:** the actual root cause (reduction schedule, cooling rate, die sizing) goes unaddressed while an unrelated adjustment is made.
- **First question:** which specific variable — reduction schedule, cooling rate, or die dimension — is most consistent with the deviation observed?
- **Data to pull:** the deviation's characteristics (location, direction, magnitude) compared against the process variable most likely responsible.

### A material batch/lot change occurs mid-schedule without re-verifying reduction limits or die swell behavior for the new batch
- **Usually means:** parameters validated for the prior batch may not apply to a batch with different composition or finish.
- **First question:** has this new batch's ductility or swell behavior actually been verified against the parameters in use?
- **Data to pull:** batch/lot identification compared against whether a test sample or verification was run.

### Wire or tube breaks in the die during a run that was calculated as within reduction limits using diameter change only
- **Usually means:** the diameter-based calculation likely understated actual area reduction relative to the material's real limit.
- **First question:** what does the actual area-reduction calculation show for this pass, versus the diameter-based figure used?
- **Data to pull:** the actual area reduction recalculated from diameters, compared against the diameter-based figure originally used.
