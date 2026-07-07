# Vocabulary

Terms generalists conflate or misuse. Each: definition, how a practitioner actually uses it, and the common misuse.

### Galvanic corrosion
Corrosion driven by dissimilar metals connected through a common electrolyte (marina water) forming a battery, with the less-noble metal sacrificing itself to the more-noble one.

**In use:** "That's straight galvanic action — the bronze prop and the aluminum housing in the same water, and nothing's bonding them to a sacrificial anode."

**Common misuse:** using "corrosion" and "galvanic corrosion" interchangeably, when stray-current corrosion (an external current source, not a metal pairing) looks similar but has a completely different fix.

### Stray current corrosion
Corrosion driven by an external DC current leaking into the water or hull from a wiring fault, distinct from galvanic corrosion because it's powered by a fault, not by the metals themselves, and can progress far faster and more locally.

**In use:** "The anode's disappearing six times faster than it should — that's stray current from the bilge pump wiring, not a sizing problem."

**Common misuse:** treating fast anode consumption as proof the anode was undersized, when a hull-potential reading in the normal range with abnormally fast consumption points at stray current instead.

### Sacrificial anode
A less-noble metal (zinc for salt water, aluminum for brackish/fresh, magnesium for fresh water only) installed to corrode preferentially and protect the boat's more critical metal components.

**In use:** "He's in fresh water — zinc anodes will barely work there and can actually under-protect the hull; this needs magnesium."

**Common misuse:** installing the wrong alloy for the water type (most commonly zinc in fresh water), which under-protects rather than simply "working less well."

### Bonding system
The network of electrical connections tying underwater metal fittings (through-hulls, engine, shaft, tanks) to a common reference point, usually the anode circuit, so they share one protection potential rather than corroding independently.

**In use:** "Bonding continuity failed at the transom — that through-hull's been sitting unprotected on its own potential since the wire corroded off."

**Common misuse:** assuming an anode protects any metal on the boat regardless of connection, when an unbonded fitting gets none of that anode's protection no matter how large it is.

### Hull potential (reference electrode / Ag/AgCl half-cell)
A voltage measurement of a submerged metal's potential relative to a standard reference electrode, used to determine whether cathodic protection is adequate, insufficient, or excessive.

**In use:** "Reading's −0.95V against the silver/silver-chloride cell — that's within the protected band, so the anode system itself is fine."

**Common misuse:** judging protection level purely from how much of the anode is visibly consumed, instead of measuring hull potential directly — visual wear alone can't distinguish adequate-but-fast-consuming from genuinely under-protected.

### Ignition protection (SAE J1171)
A design/construction rating for electrical components confirming they cannot produce a spark capable of igniting gasoline vapor, required by ABYC E-11 for any component located in a gasoline engine compartment or fuel-tank space.

**In use:** "That bilge blower switch has to be ignition-protected per J1171 — it's in the same compartment as the tank vent, not just near it."

**Common misuse:** assuming a low-voltage or low-amperage circuit is exempt because it "can't make a big spark," when the rating is about the compartment's fuel-vapor exposure, not the circuit's power level.

### Phase separation
The breakdown of an ethanol-gasoline blend (commonly E10) once absorbed water exceeds roughly 0.5% by volume at typical ambient temperature (less at colder temperatures) — the ethanol and water drop out together as a distinct bottom layer, leaving lower-octane gasoline on top.

**In use:** "Pull a sample before you touch the carburetor — if there's a water layer in the vial, this is phase separation, not a fuel-delivery fault."

**Common misuse:** treating a fuel stabilizer as a fix once separation has already occurred; stabilizers only slow the process before it starts and do nothing to reverse a tank that's already separated.

### Gearcase / lower unit
The submerged gear housing on an outboard or sterndrive that transmits engine power to the propeller through bevel gears and a shaft seal system; its oil is a primary diagnostic sample point.

**In use:** "Pull the lower unit's drain plug first — the oil condition tells you more than the noise complaint does."

**Common misuse:** treating a gearcase oil change as routine maintenance only, rather than as the moment to check for water contamination or metal that flags a developing seal or bearing failure.

### Milky / frothy gear oil
The visual signature of water-contaminated gear lube — a failed prop-shaft or driveshaft seal (or a bad vent/fill plug O-ring) has let water emulsify into the oil.

**In use:** "That's milky, not just dark — this is a seal failure, not an overdue oil change."

**Common misuse:** simply refilling with fresh oil and returning the boat to service without pressure/vacuum testing to confirm which seal failed, which lets the same water intrusion recur immediately.

### Winterization / commissioning
The paired seasonal service events bracketing storage — winterization (fall, protecting against freeze and fuel degradation before layup) and commissioning (spring, returning the boat to service) — each with its own checklist rather than being a single "get the boat ready" job.

**In use:** "Winterization isn't done until every raw-water passage is confirmed drained or filled — commissioning next spring is when a skipped step turns into a cracked riser."

**Common misuse:** treating winterization as interchangeable across engine types, when raw-water passage layout, antifreeze needs, and fogging procedures differ by engine family and must be checked against that specific engine's service manual.

### Compression test (cylinder-to-cylinder)
A relative comparison of cranking compression across an engine's cylinders, used primarily to find an outlier cylinder rather than to match one universal absolute number.

**In use:** "Cylinder 2 is 15% under the other three — that's the one to pull, regardless of what the book says the absolute spec should be."

**Common misuse:** comparing a reading only against a generic published spec number and ignoring cylinder-to-cylinder spread, which is where an isolated ring, reed, or gasket fault actually shows up.

### Fogging oil
A corrosion-inhibiting oil sprayed or misted into an engine's air intake (and sometimes cylinders directly) during winterization to coat internal surfaces against rust during storage.

**In use:** "Fogged all three cylinders through the carb throats before pulling the plugs for the season — internals won't flash-rust over winter."

**Common misuse:** treating fogging as a substitute for draining raw-water passages or changing gear oil, when it addresses internal engine corrosion only, not water-freeze or contamination risks elsewhere in the drivetrain.

### Impeller
The rubber-vaned rotor in a raw-water pump that draws in outside water for engine cooling; a distinct wear part with its own failure signature (torn or missing vanes, overheating from reduced flow) unrelated to a belt or hose fault.

**In use:** "Overheating with good coolant level and no visible leak — pull the impeller before chasing anything else, it's a one- to two-season wear item in most saltwater use."

**Common misuse:** diagnosing an overheating complaint as a thermostat or hose issue first, when a worn or torn impeller is the more common cause in a boat running in sandy or silty water.

### Trim / tilt system
The hydraulic system positioning an outboard or sterndrive's angle relative to the transom, distinct from steering — failures show as the drive not holding a set angle or drifting down under its own weight, not as a steering complaint.

**In use:** "It's not holding trim under load — that's the tilt cylinder's seal, not the hydraulic pump, based on how slowly it's drifting."

**Common misuse:** conflating trim/tilt hydraulic faults with power-steering complaints, when the two systems are separate and diagnosed with different pressure specs and test points.

### HIN (Hull Identification Number)
The boat's federally required 12-character serial identifier (analogous to a VIN), used for parts lookup, warranty status, and manufacture-date decoding from its final characters.

**In use:** "Give me the HIN, not just the model name — the anode kit and impeller part numbers changed partway through that model year."

**Common misuse:** ordering parts off model name and year alone, when mid-year running changes on the same model can mean a different anode kit or seal part number that only the HIN disambiguates.
