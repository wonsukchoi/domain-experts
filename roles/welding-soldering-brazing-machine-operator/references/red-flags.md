# Red flags

### Electrode tips assessed only by visual inspection, with no weld-count-based dressing schedule
- **Usually means:** tip wear (mushrooming) could be reducing actual current density even though the tips don't look damaged.
- **First question:** what is the current weld count since the last dressing/replacement, versus the specified interval?
- **Data to pull:** weld count log, electrode dressing/replacement schedule, actual tip diameter if measured.

### Peel test or other weld quality sampling skipped or delayed due to production pressure
- **Usually means:** a verification gap exists during which a developing weld quality issue (e.g., electrode wear-driven nugget shrinkage) wouldn't be caught.
- **First question:** when was the last weld quality verification test performed, versus the specified sampling interval?
- **Data to pull:** testing log with dates/weld counts, specified sampling plan interval.

### A weld schedule reused for a different material thickness, coating, or stack-up without re-qualification
- **Usually means:** the schedule's current/time/force parameters may not be appropriate for the new configuration's different resistance characteristics.
- **First question:** does the current job's material specification match what this schedule was originally qualified for?
- **Data to pull:** the schedule's qualification record (material, thickness, coating), current job's actual specification.

### An automated weld cycle run without verifying part fit-up/positioning in the fixture
- **Usually means:** the machine will execute its schedule on whatever is actually positioned, regardless of alignment correctness.
- **First question:** was fit-up/positioning checked before the cycle, or assumed correct based on the fixture design alone?
- **Data to pull:** fit-up verification record if one exists, fixture design tolerance for misalignment.

### A weld defect discovered after a large quantity of parts have already been produced with the same setup
- **Usually means:** a setup error or process drift propagated through the entire run because first-off inspection or periodic sampling didn't catch it early.
- **First question:** was first-off inspection performed for this setup, and has periodic sampling been maintained throughout the run?
- **Data to pull:** first-off inspection record, sampling log throughout the run, quantity produced since setup.

### Weld surface appearance used as the sole quality confirmation for a structural or safety-critical joint
- **Usually means:** internal weld formation (nugget size, penetration) hasn't been verified, and visual surface acceptability doesn't confirm it.
- **First question:** does this joint's criticality require destructive or non-destructive testing, and has it been performed?
- **Data to pull:** the joint's criticality classification, testing performed vs. required per the quality plan.

### A new part or configuration introduced without a documented first-off qualification
- **Usually means:** the weld schedule's suitability for this specific new configuration hasn't been confirmed before production quantity began.
- **First question:** was a first-off part produced and tested (including destructive/non-destructive verification) before full production started?
- **Data to pull:** first-off qualification record for this specific part/configuration.

### A nugget diameter or weld strength trending downward across a production run without a corresponding process change logged
- **Usually means:** a gradual, undocumented change (electrode wear, material variation) rather than a fixed setup error.
- **First question:** does nugget diameter/strength data show a trend over the run, and does it correlate with electrode weld count?
- **Data to pull:** weld quality trend data, electrode weld count/dressing history over the same period.

### A weld schedule change made without documenting the reason or re-qualification basis
- **Usually means:** an operator adjustment may have been made informally rather than through a controlled process change.
- **First question:** does a change record exist explaining why the schedule was adjusted and what re-qualification was performed?
- **Data to pull:** schedule change log, re-qualification test results if performed.

### A part failing in service at a weld joint that passed initial visual inspection
- **Usually means:** an internal weld defect (insufficient nugget size, incomplete penetration) that visual inspection wouldn't have caught.
- **First question:** was destructive or non-destructive testing performed on parts from the same production batch as the failed part?
- **Data to pull:** the failed part's batch/lot traceability, quality testing record for that batch.
