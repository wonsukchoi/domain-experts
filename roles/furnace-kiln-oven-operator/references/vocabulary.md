# Vocabulary

### Soak time
The duration a load is held at its target temperature after reaching set-point, required for heat to fully penetrate the load or for a chemical/physical transformation to complete throughout the material.
**In use:** "Sixty-minute soak starts when the load's slowest point hits 1550, not when the control sensor does."
**Common misuse:** Treating "temperature reached" (at the control sensor) as equivalent to "soak time can start" for the whole load — for an unvalidated load configuration, the sensor's reading doesn't confirm every part of the load has actually reached target temperature yet.

### Temperature survey (load mapping)
A validation process placing multiple temperature sensors throughout a specific load configuration to characterize actual temperature distribution and confirm (or identify gaps in) uniformity relative to the single control sensor's reading.
**In use:** "New pack density means we're not trusting the old survey — running a fresh one before we rely on this configuration's control sensor."
**Common misuse:** Assuming a temperature survey performed once for one load configuration remains valid for a meaningfully different configuration — survey validity is tied to the specific arrangement (spacing, orientation, density) it was performed under.

### Controlled atmosphere
A furnace/oven chamber atmosphere deliberately composed (inert, reducing, or a specific gas mixture) to control surface chemistry reactions (oxidation, decarburization) during a thermal process, distinct from ambient air.
**In use:** "Nitrogen atmosphere's required for this hardening cycle — any oxygen ingress risks decarburization at the part surface."
**Common misuse:** Confirming atmosphere control by checking that gas is flowing (a flow meter reading) rather than verifying actual chamber composition (an oxygen analyzer or dew point reading) — flow doesn't guarantee the chamber's actual atmosphere meets spec, especially if there's a leak or insufficient purge.

### Ramp rate
The controlled rate of temperature change (heating or cooling) per unit time, specified to prevent thermal shock damage to the material being processed.
**In use:** "Max ramp rate on this alloy is 300°F per hour — pushing it faster risks cracking, even though the equipment could technically get there quicker."
**Common misuse:** Treating ramp rate as a throughput lever to maximize using whatever speed the equipment allows — ramp rate limits are set by the material's thermal shock sensitivity, not equipment capability, and exceeding them risks real material damage.

### Thermal shock
Material damage (cracking, warping, residual stress) caused by heating or cooling too rapidly, exceeding the material's ability to expand or contract without internal stress buildup.
**In use:** "That ceramic piece cracked from thermal shock — the cool-down rate was faster than this material can tolerate."
**Common misuse:** Assuming thermal shock risk is uniform across materials — different materials have very different ramp rate tolerances, and a rate safe for one material can be damaging for another even in the same furnace.

### Set-point
The specific target temperature a control system is programmed to reach and maintain during a given phase of a thermal process cycle.
**In use:** "Set-point's 1550 for this cycle — that's the target the control loop holds during soak."
**Common misuse:** Treating set-point as the only number that matters, without accounting for ramp rate to reach it, soak time once there, or atmosphere conditions during the hold — set-point is one parameter among several that together define a complete process specification.

### Oxygen analyzer / dew point meter
Instruments measuring actual atmosphere composition inside a furnace chamber (oxygen concentration, or moisture content via dew point), used to verify atmosphere control beyond what a gas flow indicator alone confirms.
**In use:** "O2 analyzer's reading under fifty ppm — that's what confirms we're actually in spec, not just that the nitrogen line shows flow."
**Common misuse:** Treating gas flow rate as a proxy for atmosphere composition — a flowing gas line doesn't confirm the chamber has actually reached and maintained the required composition, especially with leaks, insufficient purge time, or inadequate flow rate for the chamber's actual free volume.

### Load configuration
The specific arrangement of parts within a furnace/kiln/oven — their spacing, orientation, stacking, and total density — which affects airflow, radiant heat exposure, and therefore actual temperature distribution.
**In use:** "This load's packed thirty percent denser than what we validated the process for — that's a different load configuration, not just more parts."
**Common misuse:** Treating "same parts, same furnace, same setpoint" as sufficient justification that a process transfers directly to a new load configuration — configuration changes (spacing, density, orientation) can meaningfully change heat distribution even when every other variable stays the same.

### Decarburization
The loss of carbon content at a steel part's surface layer due to reaction with an inadequately controlled atmosphere during high-temperature processing, weakening the surface hardness the process was meant to achieve.
**In use:** "Surface hardness came back low on the outer layer — checking for decarburization from an atmosphere lapse during the cycle."
**Common misuse:** Assuming a bulk mechanical property test (checking overall hardness at depth) would catch a decarburization issue — decarburization is specifically a surface-layer phenomenon and requires a surface-specific test to detect, since bulk properties can appear normal while the surface is compromised.

### Process traveler / cycle log
The documented record of a specific load's actual achieved temperature profile, soak time, and atmosphere data (not just the target setpoints), serving as the traceability record for the thermal process.
**In use:** "Cycle log shows the actual soak time and O2 reading — that's what quality reviews, not just whether the cycle 'completed.'"
**Common misuse:** Logging only that a cycle "completed" without recording the actual achieved profile data — a completion flag doesn't capture whether the actual temperature/soak/atmosphere conditions matched specification, which is the information needed to verify quality after the fact.
