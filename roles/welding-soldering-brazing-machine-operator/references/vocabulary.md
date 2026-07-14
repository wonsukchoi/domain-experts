# Vocabulary

### Current density (resistance welding)
The amount of electrical current passing through a given area of contact at the weld interface, the actual driver of weld formation — distinct from total programmed current, which stays constant even as contact area changes.
**In use:** "Current's still set at 9,000 amps, but tip wear's increased contact area — that means current density at the weld is actually lower than when the tips were new."
**Common misuse:** Assuming a fixed current setting produces consistent weld quality over the electrode's service life — as electrode tips wear and their contact area grows, the same current setting delivers progressively lower current density, weakening welds even with unchanged displayed parameters.

### Weld schedule
The complete set of programmed parameters (current, time, electrode force) for a resistance weld, or the equivalent parameter set for other welding/brazing/soldering processes, qualified for a specific material and configuration.
**In use:** "This schedule's qualified for two-sheet 0.040-inch steel — a different stack-up needs its own qualification, not a borrowed schedule."
**Common misuse:** Reusing a weld schedule qualified for one material thickness, coating, or stack-up on a different configuration — resistance and heat transfer characteristics change with these variables, and an unqualified schedule can produce weak or defective welds even though the machine executes it exactly as programmed.

### Nugget diameter
The size of the fused metal region formed at a resistance spot weld, the primary indicator of weld strength, verified through destructive testing (peel test) since it isn't visible from the weld's exterior.
**In use:** "Peel test shows nugget diameter dropped to point-one-four-five — well under our point-one-eight-oh spec."
**Common misuse:** Assuming a weld's surface appearance (indentation, discoloration) correlates reliably with nugget size — nugget formation happens beneath the surface, and only destructive testing (or specific non-destructive methods) actually confirms it.

### Electrode dressing
The process of resurfacing or reshaping a worn welding electrode tip to restore its original contact geometry and diameter, performed on a schedule tied to weld count rather than visual condition alone.
**In use:** "Dressing's due at twenty-five hundred welds on this application — that's before the tip visibly looks worn, which is exactly the point."
**Common misuse:** Waiting for an electrode tip to visually appear worn or damaged before dressing it — meaningful current-density-reducing wear (mushrooming) can occur before it's visually obvious, making a weld-count-based schedule more reliable than visual judgment alone.

### First-off inspection (first-part qualification)
A thorough inspection — including destructive or non-destructive testing where required — of the first part produced from a new or changed setup, confirming the setup is correct before production quantity proceeds.
**In use:** "First-off on this new part config includes a peel test, not just a visual check — we need to confirm the schedule's actually right for this stack-up."
**Common misuse:** Treating first-off inspection as a visual/dimensional check alone for a weld-critical part — an automated process will repeat any undetected setup error identically across the entire run, making thorough first-off verification (including destructive/non-destructive testing where warranted) disproportionately valuable compared to a manual process.

### Peel test / chisel test
Destructive tests used to verify resistance spot weld quality by physically separating the welded joint and measuring or inspecting the resulting nugget, providing direct confirmation of internal weld formation.
**In use:** "Pulling a peel test sample every five hundred welds — that's our window into what's actually happening inside the joint."
**Common misuse:** Treating destructive testing as optional extra verification for a "routine" job — internal weld quality genuinely can't be confirmed any other way for many joint types, making periodic destructive sampling a necessary part of ongoing quality control, not a one-time qualification step.

### Fit-up (part positioning)
The physical alignment and gap condition of parts as positioned in a welding fixture before the weld cycle begins, a factor the automated machine doesn't independently verify.
**In use:** "Machine will weld whatever's in the fixture — checking fit-up ourselves before we run the cycle, since it won't catch a misalignment on its own."
**Common misuse:** Assuming an automated welding machine has some inherent ability to detect or compensate for poor part fit-up — unless specifically equipped with fit-up sensing (which many systems aren't), the machine executes its programmed weld cycle on whatever is physically present, correct or not.

### Non-destructive testing (NDT) for welds
Testing methods (ultrasonic, radiographic) that verify internal weld quality without destroying the part, used when destructive sampling isn't practical for every unit or when 100% inspection of a critical joint is required.
**In use:** "This is a pressure-critical joint — ultrasonic NDT on every unit, not just periodic destructive sampling."
**Common misuse:** Treating NDT and destructive testing as interchangeable for all applications — the appropriate method and inspection rate depend on the joint's criticality, and a pressure- or safety-critical application may require 100% NDT rather than periodic destructive sampling of a subset.

### Weld count (tooling life tracking)
A running total of welds performed since a specific electrode or tooling component was last serviced, used as the basis for scheduled maintenance rather than relying on visual condition.
**In use:** "We're tracking weld count per electrode, not calendar time — that's what actually correlates with wear."
**Common misuse:** Scheduling electrode maintenance by elapsed calendar time rather than actual weld count — wear accumulates with usage, not time, and a high-volume period can wear electrodes out faster than a calendar-based schedule would anticipate.
