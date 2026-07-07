# Vocabulary

### Margin of safety (MS)
The ratio of allowable strength to applied load, minus one: MS = (allowable/applied) − 1, computed at ultimate (or limit) load after all knockdown factors are applied.
**In use:** "Spar cap MS is +0.20 at the root station under the 2.5g maneuver case."
**Common misuse:** treating MS=0.00 as a failure — it's the design target for an efficiently sized primary structure, not a red flag by itself.

### Ultimate load vs limit load
Limit load is the maximum load expected in service; ultimate load is limit load times a safety factor (typically 1.5 for aircraft structure). Structure must withstand ultimate load without failure, and limit load without permanent deformation.
**In use:** "We're showing positive margin at ultimate, but check the limit-load deformation case too."
**Common misuse:** quoting a single "the load" without specifying which of the two the margin was computed against.

### Knockdown factor
A multiplicative reduction applied to a material's base allowable strength to account for a specific degrading condition (fastener holes, environment, fatigue, manufacturing variability).
**In use:** "Apply the hot/wet knockdown before comparing against the applied stress, not after."
**Common misuse:** summing knockdown percentages instead of multiplying them sequentially against the running allowable, which overstates the effective allowable.

### V-n diagram
The plot of load factor (n, in g's) against airspeed defining the structural design envelope; the "corner points" of the diagram are the governing load cases for structural sizing.
**In use:** "Size the spar against the positive maneuver corner point, not the cruise 1g condition."
**Common misuse:** assuming the highest airspeed always produces the governing load, when the maneuver or gust corner points often govern instead.

### Means of compliance
The specific method (test, analysis, similarity, inspection) by which a certification requirement is shown to be satisfied, agreed with the certifying authority.
**In use:** "That requirement's means of compliance is test — we can't substitute an analysis without a DER finding."
**Common misuse:** treating "means of compliance" and "verification method" as if choosing one is purely an engineering decision, when it's a negotiated agreement with the certifying authority.

### DER (Designated Engineering Representative)
An engineer authorized by the certifying authority (FAA or equivalent) to make certain findings of compliance on the authority's behalf.
**In use:** "Get DER concurrence on the analysis-only verification before we baseline it."
**Common misuse:** assuming any senior engineer's sign-off satisfies a certification requirement — only a DER's finding, within their authorized scope, does.

### Type Certificate (TC) vs Supplemental Type Certificate (STC)
A TC certifies an original aircraft design; an STC certifies a modification to an already type-certificated aircraft.
**In use:** "That antenna installation needs an STC, not a full TC revision."
**Common misuse:** treating any post-certification change as needing the same certification weight as an original TC, when many qualify for a lighter STC or minor-change process.

### Special condition
An additional certification requirement imposed when existing regulations don't adequately address a novel design feature (new propulsion type, new materials, autonomy).
**In use:** "The electric propulsion system triggered three special conditions we need means of compliance for."
**Common misuse:** assuming existing Part 25/23 requirements automatically cover a novel system without checking whether a special condition applies.

### Weight and balance (W&B)
The tracked allocation and control of a vehicle's mass properties (weight and center of gravity) against a certified or contractual limit.
**In use:** "W&B status at DDR shows +580 lb against budget, mostly in systems and furnishings."
**Common misuse:** treating W&B as a bookkeeping exercise rather than a live design constraint that trades directly against range, payload, and fuel-burn guarantees.

### Flutter
A dynamic aeroelastic instability where structural and aerodynamic forces couple to produce self-sustaining, potentially divergent oscillation.
**In use:** "Flutter margin is cleared to 1.15x the never-exceed speed, per analysis; flight test pending."
**Common misuse:** confusing flutter margin (a dynamic stability margin) with static structural margin of safety — clearing one doesn't clear the other.

### Fatigue and damage tolerance
The design discipline ensuring structure survives cyclic loading over its service life, including with an assumed initial flaw (damage tolerance) rather than assuming pristine material.
**In use:** "The damage-tolerance analysis assumes a 0.05-inch initial flaw at every fastener hole."
**Common misuse:** treating a static-load margin of safety as evidence the structure will also survive its fatigue life — they are separate analyses with separate pass/fail criteria.

### Contingency (weight)
Unallocated weight held at the subsystem or program level specifically to absorb design growth before it threatens the overall budget.
**In use:** "Structures burned through its contingency at CDR; the overage now draws on the program pool."
**Common misuse:** treating contingency as a padding number to pad estimates with rather than a controlled, tracked reserve with an owner and a drawdown discipline.

### Center of gravity (CG) envelope
The range of longitudinal (and sometimes lateral) CG positions within which the aircraft is certified to fly safely across all loading configurations.
**In use:** "That cargo configuration puts CG at the aft edge of the envelope — recheck the loading chart."
**Common misuse:** assuming a weight change only matters in aggregate pounds, ignoring that where the weight is added shifts CG and can violate the envelope even within the weight limit.
