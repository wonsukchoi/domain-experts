# Vocabulary

### Shaft misalignment
The deviation of a rotating shaft coupling from perfect axial or radial alignment with its mating component, which can pass an initial functional test while still causing accelerated bearing/seal wear over the equipment's service life.
**In use:** "Measured point-zero-one-four radial misalignment against a point-zero-zero-five spec — that's not something a power-on test would catch, but it's a real bearing-life problem."
**Common misuse:** Confirming a shaft coupling's acceptability based on the motor running smoothly at initial test — misalignment's damage accumulates over service time and often isn't detectable by a simple functional check at the moment of assembly.

### Torque specification
The precise rotational force value a fastener must be tightened to, distinct from a "feels secure" tactile judgment, because both under- and over-torque produce distinct, real failure modes.
**In use:** "Spec's forty-five inch-pounds plus or minus five — checking with the calibrated wrench, not going by feel."
**Common misuse:** Tightening a fastener until it "feels right" by hand rather than to its specified value with a calibrated tool — under-torque risks vibration-driven loosening in service, over-torque risks stripped threads or cracked housings, and neither failure mode is reliably judged by feel.

### Strain relief
Hardware or routing technique that prevents mechanical stress (from motion, vibration, or flexing) from being transferred directly to a wire or cable's connection points or insulation.
**In use:** "Strain relief here needs to account for the full swing of this arm, not just where it sits when the unit's powered off."
**Common misuse:** Designing or verifying strain relief only for an equipment's static, at-rest position — the relevant stress condition is the full range of motion and vibration the wire will experience during actual operation.

### Break-in test / thermal cycling test
A verification step exposing an assembled unit to a period of operation or a temperature range beyond initial cold power-on, catching defects (marginal connections, thermally sensitive issues) that don't appear at the moment of assembly.
**In use:** "Cold power-on passed, but the break-in cycle is what would catch a connection that loosens with thermal expansion."
**Common misuse:** Treating a successful initial cold power-on test as complete functional verification — some failure modes specifically require thermal cycling or an operating period to manifest, and skipping this step misses an entire category of real defects.

### Root cause domain (electrical vs. mechanical)
The classification of a malfunction's actual underlying cause as either electrical (connections, continuity, insulation) or mechanical (alignment, binding, wear), which can present identical symptoms but require entirely different diagnosis and correction.
**In use:** "Symptom looks the same either way — checking continuity first, then alignment, before assuming which domain this actually belongs to."
**Common misuse:** Assuming a malfunction belongs to one domain based on habit or the most recent similar issue, without actually checking both — an intermittent electrical connection and a mechanical binding issue can look identical from the "device doesn't run smoothly" symptom alone.

### Dial indicator (alignment verification)
A precision measurement instrument used to directly quantify shaft or coupling alignment, providing an objective measurement distinct from a subjective visual or "runs fine" assessment.
**In use:** "Dial indicator gives us the actual number — point-zero-one-four inches — not just a visual sense that it looks aligned."
**Common misuse:** Relying on visual inspection or the equipment running smoothly to judge alignment adequacy — meaningful misalignment can exist well within what looks visually acceptable or what allows normal initial operation, and only a direct measurement confirms actual alignment.

### Vibration-driven loosening
A gradual fastener failure mode where cyclic vibration during normal equipment operation causes an under-torqued fastener to progressively loosen over time, distinct from an immediate assembly failure.
**In use:** "That's vibration-driven loosening — the bolt was under-torqued from the start, and it took weeks of operation for it to actually back out enough to matter."
**Common misuse:** Assuming a loose fastener discovered in service indicates a defective part or a sudden event — vibration-driven loosening from an under-torqued initial assembly is a gradual, time-delayed failure mode, and the root cause traces back to the original assembly torque, not a later event.

### Range of motion (equipment design)
The full extent of movement a piece of electromechanical equipment's moving components will experience during normal operation, relevant to wire routing, strain relief, and clearance verification.
**In use:** "Checking wire routing through the full range of motion, from fully retracted to fully extended, not just the position it's in right now."
**Common misuse:** Verifying wire routing, clearance, or strain relief only in the equipment's current or resting position during assembly — the relevant verification is across the full operational range of motion, since a routing that clears at one position can bind or chafe at another.
