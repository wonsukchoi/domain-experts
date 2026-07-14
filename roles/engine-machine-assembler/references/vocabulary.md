# Vocabulary

### Torque sequence
The specified order and staging (e.g., a cross or star pattern applied in percentage stages) for tightening a multi-bolt joint, distinct from and as important as the final torque value itself.
**In use:** "We're at the seventy-percent stage on the cross pattern now — not just torquing each bolt to final value one at a time."
**Common misuse:** Treating a multi-bolt joint as correctly assembled once every bolt reaches its final torque value, regardless of the order used to get there — sequence affects how evenly clamping load distributes across the joint, and a wrong sequence can warp a component even with a correct final torque on every fastener.

### Plastigauge
A measurement material (a thin plastic strip) used to indirectly measure bearing clearance by compressing it between two surfaces and comparing its resulting width against a reference scale, providing a practical field measurement method.
**In use:** "Plastigauge measured three-point-one thousandths — outside our spec, even though the crank turns freely."
**Common misuse:** Substituting a free-rotation check for actual plastigauge (or equivalent) clearance measurement — a bearing can be out of spec on either the tight or loose side while still allowing the component to turn freely by hand, especially on the loose side.

### Bearing clearance / preload
The precisely specified gap (or interference) between a bearing and its mating surface, a functional parameter requiring direct measurement rather than assumed from successful installation.
**In use:** "Clearance spec is fifteen to twenty-five ten-thousandths — that's what we're measuring for, not just whether it assembles."
**Common misuse:** Assuming successful assembly (parts fit together, shaft turns) confirms clearance is within spec — clearance is a specific dimensional value requiring direct measurement, and successful assembly alone doesn't confirm it falls within the functional range.

### Sub-assembly testing
Verifying a component sub-assembly's function independently before integrating it into the complete machine, catching defects at the cheapest possible point in the build process.
**In use:** "Testing the pump end on its own stand before it goes into the full unit — much easier to fix an issue now than after final assembly."
**Common misuse:** Deferring all testing to final assembly, treating sub-assembly testing as redundant or unnecessary — a defect caught at final test after integration requires disassembling everything built on top of the faulty sub-assembly to access and correct it.

### Break-in procedure
A specified initial operating period or load profile allowing certain components (piston rings, bearings) to properly seat through controlled initial wear, distinct from simply starting and running the machine.
**In use:** "Full break-in cycle before we load-test this unit — skipping straight to full load risks the rings never seating properly."
**Common misuse:** Treating break-in as an optional or compressible formality rather than a functional requirement — some wear-in behavior specifically requires the controlled initial operating period to occur correctly, and skipping or rushing it can cause a performance or wear issue that a quick initial test wouldn't reveal.

### Tolerance stack-up
The cumulative combined effect of multiple individually-toleranced components' dimensional variation on a final assembled clearance or fit, which can be out of functional spec even when every individual component is within its own tolerance.
**In use:** "Every part passed its own inspection, but the stack-up on this specific combination put us outside the functional clearance spec."
**Common misuse:** Assuming an assembly's critical clearance is automatically correct because each individual component passed its own dimensional inspection — an unfavorable combination of individually-in-tolerance parts can still produce an out-of-spec assembled result.

### Clamping load (uniformity)
The distribution of compressive force across a multi-bolt joint's mating surface, which must be applied evenly to prevent warping or an uneven seal, directly affected by torque sequence.
**In use:** "Uneven clamping load from that sequential torquing is exactly what caused the head to warp, even though every bolt read the right final torque."
**Common misuse:** Assuming clamping load is automatically uniform as long as final torque values are correct on every bolt — the sequence used to reach those values determines how evenly the load actually distributes across the joint during the tightening process.

### Component seating (break-in)
The physical process by which mating surfaces (piston rings against cylinder walls, bearing surfaces) conform to each other through controlled initial wear, establishing the surface contact pattern needed for proper long-term operation.
**In use:** "Rings need this break-in period to seat against the cylinder wall properly — rushing to full load before that happens can leave them never seating correctly."
**Common misuse:** Assuming components are "seated" simply because the machine starts and runs — proper seating is a physical process that occurs over the specified break-in period, not an instantaneous condition present at first startup.

### Stack-up verification (assembled measurement)
Directly measuring a critical clearance or dimension on the actual assembled components, rather than calculating or assuming it from each individual component's nominal or tolerance-range value.
**In use:** "We're measuring the actual assembled clearance, not calculating it from the nominal dimensions of each part — that's what catches an unfavorable stack-up."
**Common misuse:** Relying on calculated or nominal dimensions from individual component specifications to infer assembled clearance, rather than measuring the actual assembled result — calculation from nominal values misses the real-world tolerance stack-up that occurs when actual parts (each somewhere within their own tolerance range) are combined.
