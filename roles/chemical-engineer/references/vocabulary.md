# Chemical Engineer — Vocabulary

### Degrees of freedom (DOF)
The number of unknowns in a mass/energy balance model minus the number of independent equations relating them. A solvable, trustworthy balance has DOF=0.
**In use:** "We can't trust that yield number yet — the balance has DOF=1 until we measure the vent composition."
**Common misuse:** treating a balance that "closes" (inputs equal outputs numerically) as proof of correctness without checking DOF — a balance can close by construction even when underspecified, because unmeasured streams get back-calculated to force closure.

### HAZOP (Hazard and Operability study)
A structured, node-by-node review using guide words (more, less, no, reverse, other than) applied to process parameters to identify deviations, causes, consequences, and safeguards.
**In use:** "That reverse-flow scenario on the feed line didn't come up until we hit the HAZOP guide word for it."
**Common misuse:** running HAZOP once at design and treating it as permanently valid — any management-of-change should trigger a re-review of the affected nodes.

### LOPA (Layer of Protection Analysis)
A semi-quantitative method that estimates the frequency of a hazardous event after crediting independent protection layers, each with a probability of failure on demand (PFD).
**In use:** "The mitigated frequency comes out to 1e-4 per year, which is 10x over our target — we need another independent layer, not a re-check of the existing ones."
**Common misuse:** counting a protection layer that shares a sensor, logic solver, or final element with another counted layer — independence is a strict requirement, not a formality.

### Management of Change (MOC)
A documented, risk-ranked review process required before implementing any change to process chemistry, equipment, procedures, or organization that could affect safety.
**In use:** "That setpoint change needs an MOC — it touches the same interlock we just closed a HAZOP finding on."
**Common misuse:** skipping MOC for changes labeled "temporary" or "minor" without a documented risk assessment — temporary changes are exactly where PSM incidents cluster.

### Adiabatic temperature rise (ΔT_ad)
The temperature increase a reaction mixture would experience if all reaction heat stayed in the system with no cooling — the theoretical worst case for a cooling failure.
**In use:** "ΔT_ad comes out to 90°C — well above our 50°C flag, so we need TMRad data before scaling this."
**Common misuse:** treating ΔT_ad as a design number rather than a worst-case screening number — it's meant to trigger further characterization (TMRad, relief sizing), not to be engineered against directly.

### TMRad (Time to Maximum Rate under adiabatic conditions)
The time between a cooling-failure event and the reaction reaching its maximum self-heating rate, under the assumption no heat escapes.
**In use:** "TMRad is 40 minutes at process temperature — that's enough time for the operator to respond to the high-temp alarm before runaway."
**Common misuse:** confusing TMRad with time-to-detect — the relevant safety margin is TMRad minus detection-and-response time, not TMRad alone.

### DIERS (Design Institute for Emergency Relief Systems) methodology
An industry-standard approach for sizing emergency relief for runaway reaction scenarios, explicitly accounting for two-phase (vapor-liquid) flow during venting.
**In use:** "The relief valve was sized single-phase — we need a DIERS two-phase recalculation before we trust that number for the runaway case."
**Common misuse:** applying standard single-phase vapor relief sizing (adequate for the fire case) to a runaway-reaction case where the vented fluid foams or entrains liquid — this systematically undersizes the relief device.

### Controlling regime
Whichever step — reaction kinetics, heat transfer, or mass transfer — actually limits the observed rate of a process.
**In use:** "Bench was mass-transfer-limited because the small reactor mixes fast; at plant scale with slower relative mixing, the controlling regime shifts and the rate assumption breaks."
**Common misuse:** assuming the controlling regime is fixed by the chemistry and carries unchanged across scales — it's a property of the whole system (chemistry + equipment), and equipment changes with scale.

### Process Safety Information (PSI)
The documented technology, equipment, and chemical-hazard basis (per OSHA 1910.119(d)) that must exist before a covered process starts up.
**In use:** "We can't schedule startup until the PSI package — relief basis, material hazard data, PFDs — is signed off."
**Common misuse:** treating PSI as paperwork assembled after design is "done" rather than a living reference updated through every MOC.

### Independent Protection Layer (IPL)
A safeguard credited in LOPA that is independent of the initiating cause and of every other credited layer for the same scenario.
**In use:** "The relief valve counts as an IPL here because it's mechanically independent of the control system entirely."
**Common misuse:** crediting the same physical instrument or logic solver twice under different names (e.g., "alarm response" and "interlock") as if they were separate layers.

### Basic Process Control System (BPCS) vs. Safety Instrumented System (SIS)
BPCS is the normal operating control loop; SIS is a functionally and often physically separate system dedicated to safety interlocks, rated to a Safety Integrity Level (SIL).
**In use:** "That high-temp trip needs to be on the SIS, not just a BPCS alarm, if we want to credit it as an independent layer."
**Common misuse:** using a BPCS alarm and manual operator response as if it carries the same risk-reduction credit as a SIS-rated interlock — LOPA typically credits BPCS+operator response far lower (e.g., PFD 0.1) than a properly rated SIS (PFD 0.01 or better).

### Scale-up factor
The ratio of target scale to reference scale, usually expressed by volume, that determines how strongly area-scaling effects (like jacket cooling) diverge from volume-scaling effects (like heat release).
**In use:** "At a 1,000x scale-up factor, jacket area only grows 100x — that mismatch is the whole cooling problem."
**Common misuse:** using scale-up factor only to size equipment (bigger reactor, bigger pump) without recomputing the heat-transfer-area-to-volume ratio it implies.

### Reactive incompatibility
A hazardous reaction (heat release, gas generation, explosion) between two chemicals that were not intended to react, often discovered at a waste-stream or storage co-mingling point.
**In use:** "The waste-stream mixing incident traced back to reactive incompatibility between the quench acid and a chlorine-bearing solvent nobody flagged."
**Common misuse:** assuming compatibility because two streams have "similar" chemical classes without checking a specific reactivity reference — similarity in class does not imply compatibility.

### Vent sizing basis
The specific worst-case scenario (fire, cooling failure, runaway, blocked outlet) that a relief or vent system is sized against.
**In use:** "The vent sizing basis on that vessel is fire only — we need to add the runaway case and take the larger of the two."
**Common misuse:** assuming a relief device sized for one scenario automatically covers all others — different scenarios can require entirely different vent areas.
