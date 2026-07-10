# Vocabulary

### Area reduction
The percentage decrease in a wire or tube's cross-sectional area from one draw pass, the actual figure that governs work hardening and breakage risk.
**In use:** "Diameter change looks like 10%, but the actual area reduction comes out to 19% — that's the number that matters here."
**Common misuse:** Using diameter change as a proxy for area reduction, when area scales with diameter squared and the two percentages are never equal.

### Draw ratio
The ratio of a wire or tube's cross-sectional area before and after a draw pass (or across a full schedule), used to quantify total reduction.
**In use:** "Total draw ratio across this schedule works out to about 3.5:1 in area before the next anneal is due."
**Common misuse:** Calculating draw ratio from diameter values directly instead of the corresponding area values.

### Cumulative reduction (before anneal)
The total area reduction accumulated across multiple draw passes since the last annealing step, tracked against the material's documented limit before it must be relieved.
**In use:** "We're at 62% cumulative reduction since the last anneal — two more passes at this rate would exceed the limit."
**Common misuse:** Checking only each individual pass's reduction against the per-pass limit without tracking the running cumulative total against its own separate limit.

### Work hardening (cold work)
The increase in a metal's hardness and decrease in its remaining ductility caused by plastic deformation, such as drawing, at temperatures below recrystallization.
**In use:** "This wire's work-hardened enough that it needs annealing before the next pass, not just a smaller reduction."
**Common misuse:** Assuming a material's ductility stays constant across a multi-pass draw schedule, ignoring that each pass accumulates hardening that reduces what the next pass can safely do.

### Annealing (intermediate)
A heat treatment step performed between draw passes to relieve accumulated work hardening and restore ductility before further reduction.
**In use:** "Scheduled an intermediate anneal here — cumulative reduction was approaching the limit for this alloy."
**Common misuse:** Treating annealing as an optional step to skip if the wire "still looks like it's holding up," rather than a scheduled point tied to a calculated cumulative reduction limit.

### Die swell
The expansion of extruded plastic beyond the die opening's dimension after exiting, caused by viscoelastic recovery of the polymer.
**In use:** "Die swell on this resin runs about 8% at this line speed — the opening's sized smaller to compensate."
**Common misuse:** Sizing a die opening to the exact final target dimension, ignoring that the material will expand beyond that opening after exiting.

### Sizing tooling (extrusion)
Equipment downstream of an extrusion die that constrains and cools the profile to lock in its final dimension as it solidifies.
**In use:** "Profile's oversized — check sizing tooling cooling capacity before assuming it's a die problem."
**Common misuse:** Assuming the die opening alone determines final dimension, when sizing tooling's cooling and constraint action is what actually locks the dimension in.

### Line speed (extrusion/drawing)
The rate at which material moves through the process — drawing dies or extrusion/cooling line — measured per unit time.
**In use:** "Increasing line speed to hit the shift target, but check the cooling system can still keep up at that rate."
**Common misuse:** Treating line speed as freely adjustable to hit a production target without checking whether downstream cooling or sizing capacity can still perform correctly at that speed.

### Temper (metal)
A material's specific hardness/ductility condition resulting from its processing history (cold work, heat treatment), which determines how much further reduction it can safely tolerate.
**In use:** "This coil's already in a harder temper than the last one — the per-pass reduction limit is tighter."
**Common misuse:** Assuming a material's temper is fixed by its alloy designation alone, without accounting for how prior processing (like accumulated cold work) has already shifted its actual condition.

### Viscoelastic recovery
The tendency of a polymer melt to partially "spring back" toward its prior molecular configuration after being forced through a die, the underlying cause of die swell.
**In use:** "Viscoelastic recovery is why this resin swells more than the last one — different molecular weight, different recovery behavior."
**Common misuse:** Treating die swell as a fixed universal percentage applicable to any plastic, when it actually depends on the specific polymer's molecular characteristics and process conditions.
