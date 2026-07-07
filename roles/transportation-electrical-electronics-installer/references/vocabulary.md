# Transportation Electrical and Electronics Installer/Repairer — Vocabulary

### Multiplex network (databus)
A shared electrical backbone (commonly SAE J1939-based on transit buses, proprietary on many rail cars) that lets multiple control modules exchange data over one or two twisted-pair conductors instead of a dedicated wire per signal.
**In use:** "The lighting and HVAC symptoms hit at the same second — that's the multiplex bus, not two separate module failures."
**Common misuse:** Treating the body multiplex network as interchangeable with an engine-control J1939 network; they may share the same protocol but are physically separate buses with separate nodes and separate failure domains.

### Node
An individual control module or device connected to the multiplex network (a door controller, an HVAC controller, a lighting control unit).
**In use:** "Disconnect the door node first and see if the bus traffic clears up before we start pulling the backbone apart."
**Common misuse:** Assuming a fault logged against a node means that node's hardware is bad, when the node is often just the first thing to report a problem caused elsewhere on the shared bus or a shared power/ground circuit.

### Termination resistor
A resistor (120 ohms in SAE J1939-style networks) installed at each physical end of the backbone to prevent signal reflection; two in parallel give the network's expected end-to-end resistance.
**In use:** "We're reading 120 ohms at the connector instead of 60 — one of the terminators is open."
**Common misuse:** Measuring bus resistance with the ignition on (module outputs interfere with the reading) or from only one end of the backbone, missing a location-specific open.

### Bus-off state
A condition where a node stops transmitting/receiving on the network after accumulating too many communication errors, distinct from a hardware failure of that node.
**In use:** "The HVAC controller went bus-off twice in the log at the exact same timestamps as the lighting flicker — that's a bus-level problem, not a bad HVAC controller."
**Common misuse:** Treating a bus-off event in the fault log as proof the reporting module's hardware failed, instead of a symptom that the module correctly detected a bad bus.

### Chafe
Wire insulation wearing through from repeated contact with an edge, fastener, or another harness under vibration, eventually exposing bare conductor.
**In use:** "It's not a connector problem — the backbone pair is chafed against the bulkhead edge where the door harness got rerouted."
**Common misuse:** Attributing an intermittent short to "a bad connector" or "a bad module" without physically tracing the harness for a chafe point at clamps, grommets, and sharp edges.

### Ampacity derating
Reducing a wire's usable current rating below its open-air catalog rating to account for the number of conductors bundled together and the ambient temperature of the routing.
**In use:** "Same gauge as before, but we added a camera circuit to that bundle — recheck the derated ampacity before we call it done."
**Common misuse:** Matching a replacement wire's gauge to the original without checking whether the bundle count or routing environment changed since the original build, silently pushing an already-marginal run past its real rated capacity.

### Grommet / bulkhead penetration protection
A rubber or plastic fitting that protects a wire or harness passing through a metal panel from abrading against the cut edge.
**In use:** "That's an ungrommeted penetration — the backbone pair's been rubbing raw metal every time the panel flexes."
**Common misuse:** Treating a grommet as optional on a "small" one-off wire pass, when any unprotected penetration in a vibration environment is a future chafe point regardless of wire count.

### Wiggle test
Physically flexing or tapping a harness, connector, or component while monitoring live data (voltage, continuity, or scan-tool traffic) to reproduce an intermittent fault.
**In use:** "Bench-testing it clean doesn't mean anything — do a wiggle test on the harness while watching the live PID."
**Common misuse:** Skipping the wiggle/road test and clearing a part as "no fault found" from a static bench check, when the fault only appears under motion or vibration.

### State of charge (SOC) vs. load test
Open-circuit voltage estimates a battery's state of charge; a load test measures whether the battery can actually deliver current under a simulated cranking or hotel-load draw.
**In use:** "OCV reads 12.6 on all four, but pull a load test before you clear the bank — one of them's probably dropping under load."
**Common misuse:** Clearing a battery-bank complaint on an open-circuit voltage reading alone, without a load test, which lets a marginal cell pass inspection.

### Battery bank
Multiple batteries wired in series and/or parallel to produce the vehicle's nominal system voltage (commonly 12V or 24V) and total capacity, rather than a single battery.
**In use:** "Check bank balance — if one battery in the series-parallel group is out of line with the rest, that's the one dragging performance down."
**Common misuse:** Testing only the bank's overall terminal voltage and treating it as a single unit, instead of checking individual battery balance within the bank.

### Ground return / bonding jumper
The conductor or strap that provides the low-voltage system's return path to the vehicle chassis, distinct from the positive supply wiring.
**In use:** "Voltage at the node is fine, but the ground strap at that mounting point reads high resistance — that's the actual fault."
**Common misuse:** Assuming a ground connection is good because it's visually intact, without measuring its resistance under load; a corroded or loose bonding jumper can pass a visual check and still cause voltage drop faults.

### Body builder module / vehicle interface unit
A module that translates chassis-level signals (ignition state, speed, door status) into the format the body equipment's multiplex network expects, common on transit buses built on a separate chassis and body.
**In use:** "The destination sign fault traces back to the interface unit losing the door-status signal from the chassis side, not the sign controller itself."
**Common misuse:** Diagnosing the body equipment (sign, lighting, HVAC) in isolation without checking whether the chassis-to-body interface unit is passing the signals it depends on correctly.

### Convoluted tubing / split loom
Flexible slotted tubing wrapped around a harness bundle to protect it from abrasion where it crosses an edge or another component.
**In use:** "Route it through split-loom past that bracket — that edge is exactly where the last harness chafed through."
**Common misuse:** Using split-loom as a substitute for proper clamping at the correct interval, rather than as additional protection alongside adequate support — loose tubing over an unclamped span still lets the harness move and chafe inside the tubing.

### Fleet-pattern fault
A fault caused by a systemic issue in a build or service procedure that is likely to recur across every unit that shares that build spec or service history, not just the one vehicle in the shop.
**In use:** "This chafe point is right where the door-actuator service reroutes the harness — check every bus that got that same service in the last month."
**Common misuse:** Closing out a repair order on the one vehicle in the shop without checking whether the same root cause exists on other units built or serviced the same way.
