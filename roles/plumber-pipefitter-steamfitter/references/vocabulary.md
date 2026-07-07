# Vocabulary

Terms generalists and junior plumbers flatten together that a licensed practitioner keeps sharply separate — each with the misuse that leads to a code violation or a wrong diagnosis.

## DFU vs. WSFU

**DFU (drainage fixture unit)** measures a fixture's contribution to drainage load, used to size DWV pipe. **WSFU (water-supply fixture unit)** measures a fixture's contribution to supply demand, used to size water-supply pipe. They use different tables and different values for the same fixture — a water closet is 4–6 DFU on the drain side but only about 2.2 WSFU on the supply side.

**In use:** "Don't size the supply main off the DFU count — pull the WSFU table, they're not the same number."

**Common misuse:** using one fixture-unit number to size both the drain and the supply piping, or assuming a fixture with a high DFU load also has a high WSFU load.

## Trap-to-vent distance (critical distance)

The maximum allowed horizontal (plus limited vertical) run from a trap's weir to its vent connection, set by pipe size — not a slope requirement, a separate distance limit that exists because venting has to equalize drainage-induced negative pressure before it siphons the trap dry.

**In use:** "Slope's fine at a quarter-inch per foot, but at ninety inches this trap arm is three times over its distance max — that's the actual defect."

**Common misuse:** treating correct slope as proof the trap arm is code-compliant, when the maximum distance to the vent is the binding constraint being missed.

## Air gap vs. RPZ vs. DCVA vs. AVB/PVB

**Air gap** is a physical, unobstructed vertical separation — the strongest protection, no moving parts to fail. **RPZ (reduced-pressure-zone assembly)** protects against both backpressure and back-siphonage via a mechanically relieved zone — used for health-hazard connections. **DCVA (double-check valve assembly)** protects against backpressure only — used for non-health-hazard connections. **AVB/PVB (atmospheric/pressure vacuum breaker)** protect against back-siphonage only, installed above the flood-level rim.

**In use:** "That's a health-hazard connection with backpressure exposure — it needs an RPZ, a DCVA won't cover the back-siphonage side."

**Common misuse:** treating all backflow devices as interchangeable "backflow preventers" instead of matching device class to the specific hazard and exposure type present.

## Health hazard vs. non-health hazard (cross-connection)

**Health hazard** means a cross-connection that could introduce a substance capable of causing illness or death if it backflowed into the potable supply (chemicals, sewage, boiler treatment additives). **Non-health hazard** means backflow would only degrade aesthetic quality (odor, color) without a health risk. The classification, not the fixture type alone, drives device selection.

**In use:** "The boiler makeup line is a health hazard because of the treatment chemicals — that's an RPZ, not a DCVA."

**Common misuse:** classifying by fixture type from habit (assuming all irrigation is non-health, for example) rather than checking whether a chemical injection or other additive changes the classification for that specific connection.

## Backpressure vs. back-siphonage

**Backpressure** is downstream pressure exceeding supply pressure, pushing contaminated water backward (e.g., a pump or elevated tank on the customer side). **Back-siphonage** is a vacuum condition on the supply side (main break, high-demand draw) pulling contaminated water backward through a submerged or below-flood-level outlet. Different device classes protect against each.

**In use:** "This connection only sees back-siphonage risk from a submerged hose end, not backpressure — an AVB is enough, we don't need the full RPZ."

**Common misuse:** assuming any backflow-rated device protects against both exposure types, when several common devices (DCVA, AVB) are each rated for only one.

## Self-scouring / flow depth

The design assumption behind minimum (and maximum) drainage slope: at the correct slope and pipe size for the fixture-unit load, flow depth stays high enough to carry solids along the pipe wall rather than letting them settle. Both undersized slope and oversized pipe (which drops flow depth for a given load) defeat it.

**In use:** "This branch clogs because it's oversized for its DFU load, not because it's dirty — flow depth's too shallow to scour anything."

**Common misuse:** assuming bigger pipe always drains better; past the fixture-unit table's intended size, bigger pipe lowers flow depth and worsens solids transport.

## Wet vent vs. dry vent vs. individual vent vs. common vent

**Wet vent** is a pipe that serves as both a drain for one fixture and a vent for another. **Dry vent** carries only air, never drainage flow. **Individual vent** serves a single trap. **Common vent** serves two fixtures on the same level connecting at the same point. Each has its own sizing and connection rules — they are not interchangeable terms for "the vent."

**In use:** "We can wet-vent the lav through the shower's drain here, but that doesn't mean the same pipe works as a dry vent for the water closet."

**Common misuse:** calling any vent pipe a "dry vent" regardless of whether drainage flow passes through it, which misapplies the sizing and slope rules that only govern true dry vents.

## Water-hammer arrestor sizing (fixture-unit load)

A water-hammer arrestor's size (per PDI-WH201, rated AA through F) is selected by the fixture-unit load of the quick-closing valve group it protects, not by pipe size or a single generic "add one" placement — an arrestor sized for a light load doesn't meaningfully absorb a heavier valve group's pressure spike.

**In use:** "That's a bank of three flush valves — that's a C or D rated arrestor, not the AA we'd use for a single washer box."

**Common misuse:** installing one arrestor centrally on the main sized by guess, instead of one per valve group sized to that group's actual fixture-unit load.

## Thermal expansion tank / closed system

A **closed system** exists whenever a check valve, PRV, or backflow preventer sits on the cold main, removing the water heater's ability to relieve expanding heated water back into the street main. A **thermal expansion tank**, sized to the heater's volume and system pressure, is the code-required control for that condition.

**In use:** "The PRV we just added made this a closed system — the expansion tank isn't optional now, it's required the moment that valve went in."

**Common misuse:** treating the expansion tank as an optional upgrade rather than a trigger that fires automatically the instant a closed-system device is installed.

## Working pressure vs. test pressure

**Working pressure** is the system's normal operating pressure. **Test pressure** is the elevated pressure (often 1.5x working pressure, or a flat minimum for low-pressure systems) applied during commissioning specifically to reveal leaks that wouldn't show at normal operating conditions.

**In use:** "Working pressure here is 65 psi post-PRV, so test pressure is 100 psi for the hold — testing at 65 wouldn't prove anything."

**Common misuse:** testing at the system's normal working pressure instead of the required elevated test pressure, which can pass a joint that would leak under any pressure excursion above normal operation.

## Flood-level rim

The highest point of a fixture at which water would overflow onto the floor or surrounding area — the reference point for backflow-device installation height (AVBs and similar devices must be installed a minimum distance above it) and for defining what counts as a submersion hazard.

**In use:** "That vacuum breaker's only four inches above the rim — code wants at least six, move it up."

**Common misuse:** measuring device height from the floor or counter instead of from the fixture's actual flood-level rim, which can understate or overstate the real clearance.

## Trap seal

The standing water held in a trap's bend that blocks sewer gas from entering the occupied space — typically 2–4 in. deep, and the entire reason trap-arm venting rules exist: anything that siphons, evaporates, or blows out this seal defeats the trap regardless of how correctly the drain otherwise functions.

**In use:** "The trap seal's gone on that floor drain — it's not used often enough, that's evaporation, not a vent problem."

**Common misuse:** assuming any sewer-gas odor traces to a vent or slope defect, when infrequently used fixtures (floor drains, guest bathrooms) lose their seal to evaporation alone and need a trap primer, not a re-vent.

## Fixture branch vs. stack vs. building drain vs. building sewer

**Fixture branch** connects one or more fixtures to a stack. **Stack** is the vertical main carrying drainage (and often venting) between floors. **Building drain** is the horizontal piping inside the building collecting all stacks. **Building sewer** is the piping from the building drain to the public sewer or private disposal system, outside the building. Each level has its own sizing table and, often, different code jurisdiction (building drain is plumbing code; building sewer may cross into site/civil requirements).

**In use:** "That backup is in the building drain, not the sewer lateral — different fix, different permit if it turns out to be the lateral."

**Common misuse:** using "the drain" or "the sewer" interchangeably when diagnosing a backup, which points the fix at the wrong segment and the wrong permit scope.
