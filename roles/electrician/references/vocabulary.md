# Vocabulary — terms of art generalists misuse

### Ampacity
The maximum current a conductor can carry continuously under stated conditions without exceeding its temperature rating — a function of conductor size, insulation rating, ambient temperature, and how many other current-carrying conductors share the same raceway.
**In use:** "The 6 AWG is rated 65A at 75°C, but we're in an 8-conductor conduit, so it derates to 70% before I'll call it good for this OCPD."
**Common misuse:** Treating ampacity as a fixed property of the wire gauge alone, quoted from a manufacturer's chart, without applying ambient-temperature correction or conduit-fill adjustment for the actual installation.

### Demand factor
A percentage applied to connected load in an NEC load calculation, reflecting that not all loads run at full nameplate simultaneously — codified in specific tables (220.42, 220.53, 220.54, 220.55), not a general "engineering judgment" discount.
**In use:** "Three fixed appliances doesn't hit the four-unit threshold in 220.53, so we don't get the 75% demand factor — full nameplate on all three."
**Common misuse:** Applying a demand factor to any load that "probably won't run at full power," rather than only to the specific load categories the code tables actually cover.

### Continuous load
A load expected to run at maximum current for 3 hours or more, which the code requires be sized at 125% for both the conductor and the overcurrent device (not the load itself run at 125%).
**In use:** "EVSE is a continuous load under Article 625 — we size the breaker and conductor at 125% of the charger's rated current, not the rated current itself."
**Common misuse:** Assuming "continuous" just means "runs a long time" in casual speech, and skipping the 125% multiplier on anything that isn't obviously a motor or lighting load — most EV chargers and HVAC compressors qualify and are commonly under-sized this way.

### Multiwire branch circuit (MWBC)
Two ungrounded conductors on different phases (or legs of a split-phase system) sharing a single neutral, which carries only the unbalanced current between them.
**In use:** "This is a shared-neutral MWBC feeding two receptacle circuits — they need a common disconnect or handle-tie per 210.4(B), or a de-energized neutral becomes a shock hazard on whichever leg is still live."
**Common misuse:** Calling any circuit with a neutral and two hots an MWBC without checking that the hots are actually on opposite legs — two hots on the same leg sharing a neutral is a wiring error, not a legitimate MWBC.

### Bonding
Connecting normally non-current-carrying metal parts (panel enclosures, conduit, equipment frames) together and to the grounding electrode system so a fault finds a low-impedance path back to the source, tripping the breaker instead of energizing the metal.
**In use:** "The main bonding jumper goes at the service disconnect only — this subpanel needs an isolated neutral bar, not another bond, or we've created a parallel path for neutral current on the equipment ground."
**Common misuse:** Using "bonding" and "grounding" interchangeably — grounding connects the system to earth for voltage stabilization and lightning/surge dissipation; bonding is what actually makes a fault trip the breaker. Conflating the two is how a subpanel ends up incorrectly re-bonded.

### Arc fault vs. ground fault
An arc fault is current jumping an air gap (a damaged cord, a nail through a cable) that AFCI protection detects by its signature waveform; a ground fault is current leaking to a grounded surface (often through a person) that GFCI protection detects by a current imbalance between hot and neutral — they protect against different failure modes and are not interchangeable devices.
**In use:** "This is a combination AFCI/GFCI breaker because 210.12 requires arc-fault protection here and 210.8 requires ground-fault protection in the same location — one device covering both required zones."
**Common misuse:** Assuming a GFCI breaker also provides arc-fault protection (or vice versa) because both trip on a "fault" — they sense different physical phenomena and a code section requiring one doesn't satisfy the other.

### Service (as in "service size" or "service upgrade")
The conductors, equipment, and main disconnect that bring utility power into the building and establish the point of demarcation between the utility's responsibility and the building's — sizing it is a function of the calculated demand load, not the panel's slot count or bus rating alone.
**In use:** "The panel has open slots, but the service itself is what's undersized — a 150A service caps total demand at 150A no matter how many breakers physically fit in the can."
**Common misuse:** Treating "the panel has room" as evidence the service has capacity — panel slot availability and service ampacity are unrelated constraints that happen to live in the same box.

### Voltage drop
The reduction in voltage along a conductor run due to its resistance, proportional to current and one-way distance and inversely proportional to conductor cross-sectional area (circular mils).
**In use:** "At 80 ft and 48A on 6 AWG copper, that's 1.57% drop — well inside the 3% guideline, no upsizing needed."
**Common misuse:** Citing the 3%/5% voltage-drop thresholds to an inspector as a code violation — in most jurisdictions it's an informational note (a recommendation), not an enforceable requirement, unless the local AHJ has specifically adopted it.

### Lockout/tagout (LOTO)
The procedure of physically isolating an energy source (locking a breaker off) and tagging it to prevent re-energization while work is performed, paired with test-known-live-test verification before contact.
**In use:** "Lock it out, tag it, then test-known-live-test before you touch that splice — don't trust that the breaker labeled 'kitchen' is actually the one feeding this circuit."
**Common misuse:** Treating "I flipped the breaker" as equivalent to LOTO — without a lock, a tag, and a verified-dead test with a meter, there's nothing preventing someone else from re-energizing the circuit or a mislabeled panel from leaving it live.

### Nameplate rating vs. calculated demand
A device's nameplate states its maximum rated draw under full operation; calculated demand is what the load calculation assigns it after applicable code demand factors — the two numbers are often intentionally different by design, not an error.
**In use:** "The range's nameplate says 12kW, but Table 220.55 assigns it an 8,000 VA demand for a single range — that's the number that goes into the service calc, not the nameplate figure."
**Common misuse:** Summing nameplate ratings directly into a load calculation instead of applying the code's demand-factor tables, which produces a service-size recommendation far larger (and more expensive) than actually required.
