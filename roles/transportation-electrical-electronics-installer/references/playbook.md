# Transportation Electrical and Electronics Installer/Repairer — Playbook

Filled reference sequences: multiplex node-vs-bus fault isolation, battery-bank load-test thresholds, and harness ampacity/chafe-protection routing standards for vibration-heavy vehicle environments.

## 1. Multiplex node-vs-bus fault isolation sequence

Work in this order — bus-level checks are faster than swapping components and rule out most of the wrong branch before it costs a part.

| Step | Action | Pass criterion | If fail |
|---|---|---|---|
| 1 | Pull the full fault log across every node on the network, not just the one reporting the symptom | No correlated fault timestamps on unrelated nodes | Correlated timestamps across unrelated nodes → suspect shared bus/power fault, skip to step 3 |
| 2 | Disconnect the suspect node and re-check the reported symptom | Symptom clears with the node removed | Symptom persists with the node removed → it's bus-side, move to step 3 |
| 3 | Measure backbone resistance at the diagnostic connector, ignition off | ~60 ohms (two 120-ohm terminators in parallel) | Reading near 120Ω → missing/failed terminator. Reading near infinite → open backbone conductor. Reading near 0Ω → short to chassis ground |
| 4 | Trace the backbone physically for chafe, corrosion, or a loose ground at every bulkhead penetration and known vibration zone (door hinges, suspension mounts, roof HVAC bay) | No visible insulation wear, corrosion, or loose fastener | Found → repair per chafe-protection spec (section 3), re-clamp full span, not just the break point |
| 5 | If bus checks all clear, verify power and ground at the suspect node's connector before condemning the module | Voltage/ground within spec at the connector | Out of spec → trace the power/ground circuit, not the module |
| 6 | Only after steps 1–5 clear bus, power, and ground as causes, replace the node/module | Fault clears and stays clear over a 15+ min road test that reproduces the original trigger condition | Recurs → escalate to full harness inspection or a second suspect node |

**Bus resistance quick reference (SAE J1939-style two-terminator backbone):**

| Reading at diagnostic connector, ignition off | Likely cause |
|---|---|
| ~60 ohms | Normal — both 120Ω terminators present, backbone continuous |
| ~120 ohms | One terminator missing or open |
| Near infinite (open circuit) | Backbone conductor broken/disconnected somewhere on the network |
| Near 0 ohms | Short to chassis ground or shorted terminator |

## 2. Battery-bank load-test thresholds

Never clear a battery-bank complaint on open-circuit voltage (OCV) alone — OCV screens out the obviously dead but passes a marginal cell that fails under load.

| Check | Method | Pass criterion | If fail |
|---|---|---|---|
| Open-circuit voltage, 12V battery, rested 1+ hr | Digital multimeter across terminals | 12.6V = ~100% SOC, 12.4V = ~75%, 12.0V = ~50% (SAE J537 correlation) | Below ~11.8V → charge and retest before load-testing |
| Load test | Carbon-pile or electronic load tester at ~50% of CCA rating for 15 sec | Voltage holds above ~9.6V per 12V battery under load at 21°C | Drops below 9.6V → replace that battery, not the whole bank blind |
| Bank balance (series-parallel banks) | Individual battery OCV comparison within the bank | All batteries within ~0.2V of each other | One battery reading low relative to the rest → isolate and load-test it individually before assuming the whole bank is bad |
| Charging system output, 24V system | Multimeter at battery terminals, engine/charger running | ~27.2–28.8V float/charge range (system-specific, confirm against OEM spec) | Outside range → voltage regulator/charger fault, not a battery fault |

**Example:** a bus with an intermittent "electronics reboot" complaint reads 12.6V OCV on all four batteries (healthy-looking). Load test drops battery #3 to 8.9V under a 15-second load — that battery is bad despite passing the OCV check. Replacing only battery #3 (not the bank) and rechecking bank balance resolves the complaint.

## 3. Harness ampacity derating and chafe-protection routing

**Ampacity derating (SAE J1128 baseline, illustrative — confirm exact values against the current-year table for the wire type in use):**

| Condition | Derate from unbundled open-air rated ampacity |
|---|---|
| Single conductor, free air, ambient ≤25°C | 0% — full rated ampacity applies |
| Bundled with 2–4 other conductors | ~10–15% derate |
| Bundled with 5+ other conductors | ~20–30% derate |
| Routed through high-ambient zone (roof HVAC bay, underfloor exhaust-adjacent run) | Additional 10–15% derate on top of bundle derate |

Rule: when a repair adds a conductor to an existing bundle (e.g., an aftermarket accessory sharing a run), recompute the bundle-derated ampacity for every conductor in that bundle — not just the new one.

**Chafe-protection routing standard:**

| Point | Requirement |
|---|---|
| Bulkhead/sheet-metal penetration | Grommet or edge-protection bushing at every penetration, no exceptions for "small" one-off wires |
| Unsupported harness span | Clamp at OEM-specified interval, or a default of every 12–18 in absent an OEM spec |
| Sharp edge within 2 in of a harness run | Convoluted tubing/split-loom over the run, or reroute away from the edge |
| Service loop at a connector | Enough slack for the full range of relative motion at that point (door hinge, suspension travel) without tension on the connector at either extreme |

**Failure signature:** a harness rubbing on an unrounded edge or an unsupported span typically fails at the exact rub point, producing an intermittent short that only shows under vibration (over bumps, at idle with HVAC compressor cycling) — not a constant fault, and often not reproducible on a bench test at rest.

## 4. Fleet-pattern check

Whenever a chafe or ampacity-marginal fault is found, check whether the same harness routing exists on other units of the same build (same model year, same retrofit/service history). A chafe point caused by a specific service procedure (e.g., a door-actuator harness reroute) is often present on every unit that received that same service, not unique to the one vehicle in the shop.
