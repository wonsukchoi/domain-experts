# Vocabulary

Terms generalists conflate that a pump station operator keeps sharply separate. Each: definition, a sentence a practitioner would actually say, and the common misuse.

### NPSHa vs. NPSHr

**NPSHa** (Net Positive Suction Head available) is what the suction side of the system actually provides at the pump inlet, calculated from atmospheric pressure, static head, friction losses, and vapor pressure. **NPSHr** (required) is the minimum the specific pump needs at a given flow to avoid cavitation, read from the manufacturer's curve. Cavitation risk is about the *margin* between them, not either number alone.

**In use:** "NPSHa is 37 ft but NPSHr at this flow is 18 — margin ratio's over 2, we're fine even though the wet well's down a couple feet."

**Common misuse:** checking NPSHr against rated/nameplate flow instead of actual current flow — NPSHr rises with flow, so a margin that looks safe at rated flow can vanish at a higher actual flow.

### Wet well vs. dry well

The **wet well** is the chamber that receives incoming wastewater and holds the working liquid level the pumps draw from. The **dry well** (in a dry-pit station) houses the pumps and motors themselves, kept separate from the liquid to allow maintenance access. Not every station has both — submersible stations have no dry well.

**In use:** "Alarm's on wet well level, not dry well sump — that's an inflow/overflow issue, not a pump-room flooding issue."

**Common misuse:** using "wet well" loosely to mean the whole station, obscuring whether an alarm concerns liquid level (wet well) or equipment-space flooding (dry well sump).

### SSO vs. sewer backup (SSB)

An **SSO** (sanitary sewer overflow) is an unintended discharge of wastewater from the collection system to the environment — a ditch, storm drain, or waterway — and is a regulatory reporting event. A **sewer backup (SSB)** is wastewater coming back up into a building through a fixture or drain, a property-damage and customer-service event with different (though sometimes overlapping) notification obligations.

**In use:** "This is an SSO — it reached the drainage ditch — so the state notification clock started at discovery, separate from the backup claim at the Elm Street property."

**Common misuse:** treating every reported "spill" the same way; an SSO to surface water and a backup into a single building trigger different reporting paths and different urgency.

### BEP vs. duty point vs. AOR/POR

**BEP** (best efficiency point) is the flow at which a specific pump curve is most efficient. The **duty point** is where the pump curve actually intersects the system curve under current conditions — it moves as the system changes even though the pump doesn't. **AOR/POR** (allowable/preferred operating region, Hydraulic Institute) are the flow bands around BEP within which running the pump is considered acceptable (AOR, wider) or ideal (POR, narrower, often ~70–120% of BEP).

**In use:** "Duty point's drifted to 62% of BEP since that valve got throttled — still inside AOR, but outside POR, and it'll show up in bearing life before it shows up in flow."

**Common misuse:** treating "the pump is meeting its curve" as sufficient, when the relevant question is where the duty point sits relative to BEP, not whether the pump can technically produce that flow.

### Water hammer vs. normal pressure surge

**Water hammer** specifically refers to the transient pressure wave from a sudden velocity change (valve closure, pump trip) reflecting through a closed or bounded pipe system, governed by the Joukowsky relation and the pipe's wave speed. A **normal pressure surge** (e.g., pump start ramping up to operating pressure over several seconds under VFD control) changes system pressure gradually and doesn't excite the same reflected-wave physics.

**In use:** "That's water hammer from the valve, not just the pump coming up to pressure — the check valve slam is the tell."

**Common misuse:** calling any pressure change "water hammer," which obscures whether the closure/stop time was actually fast relative to the pipe's critical period or whether it was a normal, gradual pressure rise.

### Prime vs. dry run

A centrifugal pump is **primed** when its casing and suction line are full of liquid, which is required for it to develop flow at all. **Dry run** means the pump is operating (or attempting to) without that liquid present — no priming, or prime lost mid-operation — and the pumped liquid that would normally cool and lubricate the mechanical seal faces is absent.

**In use:** "Pump lost prime when the wet well dropped below the suction bell — it's been dry-running for maybe 40 seconds, kill it now before the seal goes."

**Common misuse:** treating "loss of prime" as a flow problem to troubleshoot at normal pace, when it's a seal-damage clock running in the background from the moment prime is lost.

### Force main vs. gravity sewer

A **force main** is a pressurized pipe carrying wastewater from a lift station's discharge to a downstream point, sized and rated for the pump's discharge pressure and subject to surge analysis. A **gravity sewer** relies on slope alone, flows partially full, and carries no equivalent pressure-transient risk.

**In use:** "Surge calc only applies from the station to the force main's discharge point — once it hits the gravity sewer, that pressure risk is gone."

**Common misuse:** applying gravity-sewer intuitions (partial flow, no pressure rating concerns) to force main sections, where the pipe is full and pressurized and surge/water-hammer rules apply.

### Check valve slam

The audible impact of a check valve's disc or flapper closing abruptly against its seat when flow reverses, typically at pump shutdown — a local, repeated instance of the same pressure-reversal mechanism that a full surge (water-hammer) study addresses.

**In use:** "That check valve's been slamming every shutdown for weeks — that's chronic water hammer on a small scale, not just an annoying noise."

**Common misuse:** dismissing check valve slam as a nuisance or a valve-maintenance-only issue, rather than a symptom worth including in the pump's shutdown-sequence and surge review.

### Critical period (pipe period) vs. valve closure time

The **critical period** (Tc = 2L/a) is a property of the pipe itself — the round-trip travel time of a pressure wave to the nearest reflection point and back. **Valve closure time** is an operational setting the operator or actuator controls. Whether a closure counts as "instantaneous" (full surge) or "slow" (reduced surge) depends entirely on how the closure time compares to Tc, not on the closure time in isolation.

**In use:** "Two seconds sounds fast, but Tc for this run is 2.4 seconds — we're on the wrong side of the line, full surge applies."

**Common misuse:** judging a closure time as "fast" or "slow" against intuition rather than against the calculated Tc for that specific pipe length and material.

### Total dynamic head (TDH) vs. static head vs. friction head

**Static head** is the elevation difference the pump must lift liquid against. **Friction head** is the energy lost to pipe friction and fittings at a given flow, which rises with flow squared. **TDH** is their sum — the total head the pump curve must meet at the operating flow, and the number that actually defines the system curve.

**In use:** "Static head hasn't changed, but friction head's up because that line's scaling — TDH at the same flow is higher than it was a year ago, which is why the duty point moved."

**Common misuse:** citing static head alone (the more intuitive, sometimes only measured, quantity) as if it defined the system curve, ignoring that friction head — and therefore TDH — changes with flow and with pipe condition.

### Flooded suction vs. suction lift

**Flooded suction** means the liquid source sits above the pump centerline, so gravity assists suction. **Suction lift** means the source is below the pump, so the pump must draw liquid up against atmospheric pressure — reducing NPSHa and making priming and NPSH margin materially more sensitive to source-level changes.

**In use:** "We went from flooded suction to a lift condition when that wet well level dropped — that's why the margin ratio fell off a cliff, not because the pump changed."

**Common misuse:** using the same NPSH-margin comfort level for both conditions, when a suction-lift configuration has far less tolerance for source-level drop or added friction than a flooded one.

### VFD soft-start/soft-stop

A variable-frequency drive (VFD) ramps a pump's motor speed up or down over a set time rather than switching it directly across the line, which ramps the velocity change (and therefore the surge potential) gradually instead of as a step change.

**In use:** "Put the soft-stop ramp on this pump at eight seconds — that alone knocks the surge down without touching the valve at all."

**Common misuse:** assuming a VFD soft-stop alone solves surge risk across the whole system, when it only controls the pump end — a fast valve closure elsewhere on the same pipe run still produces its own surge independent of how the pump ramped down.
