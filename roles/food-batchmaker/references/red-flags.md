# Red flags

### A production-scale batch behaving differently than pilot despite correctly scaled ingredient ratios
- **Usually means:** a process parameter (working time, mixer shear rate, dwell time before the next step) didn't scale proportionally with the ingredient weights.
- **First question:** how does the elapsed time from mix completion to the next process step compare between pilot and production scale?
- **Data to pull:** pilot vs. production working-time logs, mixer speed/shear settings at both scales.

### A time-sensitive ingredient (leavening, enzyme, live culture) scaled by the same ratio as bulk ingredients with no process-timing check
- **Usually means:** the scale-up assumed linear ingredient scaling was sufficient without verifying the ingredient's functional behavior at the new process timing.
- **First question:** has this specific ingredient's functional behavior been verified at the actual production-scale working time, or only at pilot scale?
- **Data to pull:** ingredient's functional/reactivity data sheet, pilot vs. production working-time comparison.

### Mixing stopped at a fixed elapsed time rather than a verified consistency/development endpoint
- **Usually means:** equipment condition (blade wear, speed calibration) has changed since the time-based setpoint was established, so the same elapsed time no longer produces the same result.
- **First question:** does this mixer's current output match the target consistency at this elapsed time, or has that relationship drifted?
- **Data to pull:** mixer maintenance/calibration log, consistency test result at the current time setpoint.

### Water activity reading missing or substituted with a moisture-percentage check alone
- **Usually means:** a shelf-stability assessment relied on a proxy measurement instead of the actual relevant indicator.
- **First question:** does this formulation's shelf-stability requirement actually specify a water activity threshold, and has it been measured?
- **Data to pull:** formulation's shelf-stability spec, water activity meter reading for this batch.

### An allergen-containing batch inserted into the schedule outside its normal sequence
- **Usually means:** a supply, equipment, or scheduling disruption forced a reorder, creating pressure to shorten the changeover/clean.
- **First question:** has the full changeover/clean protocol been completed and verified before and after this batch, regardless of the schedule disruption?
- **Data to pull:** changeover/clean verification log, allergen sequencing schedule for the day.

### A weight or ingredient deviation flagged on a safety-critical ingredient (preservative, acid/pH-affecting, allergen-declared)
- **Usually means:** this deviation carries more consequence than a similar-magnitude deviation on a bulk structural ingredient would.
- **First question:** does this specific ingredient's tolerance reflect its safety/regulatory risk category, or was a blanket tolerance applied?
- **Data to pull:** the formulation's ingredient-specific tolerance spec, the batch's actual measured weight for that ingredient.

### A reformulated recipe running its first full production batch without a pilot verification at production-scale timing
- **Usually means:** time pressure skipped the pilot-at-scale verification step for a change assumed to be minor.
- **First question:** has this exact formulation been tested at actual production-scale working time and mixing conditions, or only at bench/pilot scale?
- **Data to pull:** pilot test records for this formulation, production-scale working-time data.

### A finished batch's consistency, color, or texture visibly different from a reference standard
- **Usually means:** a mixing, ingredient, or process-timing deviation occurred somewhere in the batch that wasn't caught by weight verification alone.
- **First question:** were mix time, temperature, and ingredient weights all within spec, or does one of them show a deviation?
- **Data to pull:** batch record for mix time/temp/weights, reference standard for comparison.

### Two consecutive batches on the same line showing a similar unexplained deviation
- **Usually means:** a shared root cause (equipment drift, an ingredient lot issue, a process-timing change) rather than two independent, unrelated events.
- **First question:** do both batches share the same equipment, ingredient lot, or schedule position?
- **Data to pull:** batch records for both batches, equipment and ingredient lot data common to both.

### A batch record missing a documented corrective action for a logged deviation
- **Usually means:** the deviation was noted but not actually investigated or resolved before the batch proceeded.
- **First question:** does the batch record show what caused the deviation and what was done about it, or just that it occurred?
- **Data to pull:** the batch record's deviation entry, any supporting investigation notes.
