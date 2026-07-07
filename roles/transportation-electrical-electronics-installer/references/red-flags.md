# Transportation Electrical and Electronics Installer/Repairer — Red Flags

### Fault appears on two or more unrelated systems (e.g., lighting + HVAC) at the same moment, right after unrelated harness work nearby
- **Usually means:** a shared multiplex-bus or power-distribution fault, not two independent module failures
- **First question:** do the stored fault timestamps across the affected nodes correlate within a few seconds of each other?
- **Data to pull:** full network fault log across every node, not just the systems showing symptoms; recent repair-order history for harness work in the same area

### Backbone resistance at the diagnostic connector (ignition off) reads far from ~60 ohms
- **Usually means:** near 120Ω → missing/failed terminator; near infinite → open backbone conductor; near 0Ω → short to chassis ground
- **First question:** which end of the backbone gives the abnormal reading when measured from both directions?
- **Data to pull:** resistance measurement from each end of the backbone, network topology diagram showing terminator locations

### Intermittent fault reproduces only over rough pavement, speed bumps, or during HVAC compressor cycling
- **Usually means:** vibration-induced chafe or a loose connector/ground, not a module failure — bench testing at rest will not reproduce it
- **First question:** has a road test with a min/max-recording meter or data logger been run, or was this only bench-tested?
- **Data to pull:** min/max voltage/continuity capture during a road test over the specific trigger condition described; harness routing diagram for known vibration zones

### Battery bank open-circuit voltage reads healthy (12.6V+ per 12V battery) but the vehicle shows intermittent electronics reboot or hard-start complaints
- **Usually means:** a cell with high internal resistance that passes an at-rest voltage check but fails under cranking or hotel-load draw
- **First question:** what did the load test show, not just the open-circuit voltage?
- **Data to pull:** carbon-pile/electronic load-test result per battery, individual battery OCV comparison within the bank

### Same fault code recurs within days of a harness repair
- **Usually means:** the repair fixed the one visible break point but left the rest of the unsupported span unclamped or ungrommeted, so it chafes through again nearby
- **First question:** was the full harness span re-clamped and re-grommeted, or only the point that already failed?
- **Data to pull:** prior repair order for the same circuit, current inspection of the full span rather than just the previous repair point

### Corrosion or a greenish residue found at a bulkhead connector or splice
- **Usually means:** water intrusion at an ungrommeted or improperly sealed penetration — a common failure point on undercarriage and roof harness runs
- **First question:** is there a grommet or seal at this penetration at all, and is it intact?
- **Data to pull:** visual inspection of the penetration seal, moisture/corrosion extent along the harness on both sides of the penetration

### Wire insulation shows a flat or worn spot at a clamp, grommet, or unsupported span
- **Usually means:** chafe in progress from vibration contact with an edge or fastener — not yet a dead short, but will become an intermittent short if untouched
- **First question:** how much conductor is exposed, and is there contact with a grounded surface under any load condition?
- **Data to pull:** visual/tactile inspection of the wear point, continuity/insulation-resistance check at that point

### Charging system output reads outside the expected float/charge range for the vehicle's nominal voltage (e.g., a 24V system charging above ~28.8V or below ~27.2V)
- **Usually means:** voltage regulator or charger drift, less commonly a bad ground at the charger/alternator mounting point
- **First question:** is the reading consistent across all batteries in the bank, or does one battery drag the reading down?
- **Data to pull:** charging voltage at the battery terminals with the charger/engine running, individual battery OCV to rule out a bank imbalance masquerading as a charger fault

### A new fault appears on a shared circuit shortly after an accessory or retrofit was added (destination sign upgrade, added USB charging ports, camera system)
- **Usually means:** the added circuit shares a fuse/relay panel or harness bundle that was never re-derated for the additional load
- **First question:** was the bundle-derated ampacity recalculated for the shared run after the retrofit, or was the new circuit just tapped in?
- **Data to pull:** as-built wiring diagram before and after the retrofit, fuse/breaker rating versus actual measured load on the shared circuit

### Ampacity-marginal wire gauge found on a harness repair that matches the original gauge, but the bundle count has increased since the original build
- **Usually means:** an aftermarket accessory shares the run without anyone recalculating the bundle-derated ampacity for the added conductor
- **First question:** how many conductors are in this bundle now versus when the original ampacity was specified?
- **Data to pull:** current bundle conductor count and routing, original harness ampacity spec, wire temperature at operating load if measurable

### Fault found on one unit also exists on other units from the same production run or the same retrofit/service batch
- **Usually means:** a systemic routing or clamping defect from the build or service procedure, not an isolated one-off failure
- **First question:** which other units received the same build spec or the same service procedure in the same time window?
- **Data to pull:** fleet maintenance records cross-referenced by model year and service-order type, not just the one unit in the shop
