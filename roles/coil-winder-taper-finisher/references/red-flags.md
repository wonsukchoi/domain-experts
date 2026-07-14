# Red flags

### A mechanical turn counter never cross-checked against an independent counting method
- **Usually means:** an undetected counter slip or drift could be producing a systematically wrong turn count across every coil wound on that machine.
- **First question:** when was this counter last cross-checked against an independent method (layer-count calculation, secondary counter)?
- **Data to pull:** cross-check log/frequency, counter calibration history.

### A coil's inductance reading close to the edge of its specification range
- **Usually means:** a turn count error, even a small one, since inductance scales with the square of turn count and a small count deviation can produce a proportionally larger inductance deviation.
- **First question:** does the inductance deviation correspond to a plausible turn-count discrepancy given the turns-squared relationship?
- **Data to pull:** measured inductance, target inductance and tolerance, turn count verification method used.

### Wire tension set by operator feel rather than to a specified range for the wire gauge/insulation
- **Usually means:** risk of either insulation damage (too tight) or loose, unstable windings (too loose).
- **First question:** does actual tension match the specified range for this wire gauge and insulation type?
- **Data to pull:** tension setting used, specification for this wire/insulation combination.

### A coil passing visual/mechanical inspection with no post-winding electrical test performed or sampled
- **Usually means:** turn count accuracy, insulation integrity, and electrical characteristics haven't actually been verified.
- **First question:** was electrical testing (resistance, inductance, hi-pot) performed per the specified test plan, or skipped/under-sampled?
- **Data to pull:** the specified test/sampling plan, actual testing performed on this coil/batch.

### A hi-pot/dielectric test failure with no investigation into wire handling technique
- **Usually means:** an insulation nick or scratch during winding, likely from wire handling rather than a material defect.
- **First question:** does the winding process involve any contact points or guides that could nick insulation during handling?
- **Data to pull:** hi-pot test failure location/pattern if determinable, wire handling/guide equipment condition.

### A winding pattern deviating from the specified layering approach
- **Usually means:** possible wire crossover or inconsistent spacing affecting electrical characteristics even with correct total turn count.
- **First question:** does the actual winding pattern match the specification, or did the technician deviate from it?
- **Data to pull:** the specified winding pattern, visual inspection of actual pattern.

### A recurring electrical test failure across multiple coils from the same winding machine or wire lot
- **Usually means:** a systematic cause (counter slip, tension control issue, wire lot defect) rather than isolated coil-to-coil variation.
- **First question:** do the failing coils share a common machine, operator, or wire lot?
- **Data to pull:** failure pattern across coils, machine/lot traceability data.

### A coil rewound or reworked after an initial failure without re-verifying tension, turn count, and electrical test from scratch
- **Usually means:** an assumption that a partial fix addresses the issue without confirming all relevant parameters are correct after rework.
- **First question:** was the rewound/reworked coil fully re-verified (tension, turn count, electrical test), or only the specific issue addressed?
- **Data to pull:** rework record, post-rework verification results.

### A field failure traced to a coil that passed all documented tests at time of manufacture
- **Usually means:** a latent insulation defect (a nick that didn't cause an immediate short but failed later under stress) not caught by the original test parameters.
- **First question:** does the original test record show hi-pot/dielectric testing at a voltage/duration adequate to catch a marginal insulation defect?
- **Data to pull:** original test parameters and results, the failure mode observed in the field.

### A high-turn-count coil counted manually without a verified counting method
- **Usually means:** manual tally is error-prone at high turn counts, and a miscount may not be visually detectable on the finished coil.
- **First question:** was a mechanical/electronic counter used and cross-checked, or was the count tracked manually?
- **Data to pull:** the counting method used, turn count relative to the threshold where manual tally becomes unreliable.
