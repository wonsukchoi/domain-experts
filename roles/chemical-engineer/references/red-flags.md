# Chemical Engineer — Red Flags

### Adiabatic temperature rise (ΔT_ad) exceeds 50°C for a semi-batch addition
- **Usually means:** the reaction has runaway potential if cooling or agitation is lost mid-addition; second most likely — the exotherm was characterized at a scale where it was self-limiting and hasn't been re-checked at target scale.
- **First question:** what is the time-to-maximum-rate under adiabatic conditions (TMRad), and is it longer than the time to detect and respond to a cooling failure?
- **Data to pull:** reaction calorimetry data (RC1/ARC), adiabatic temperature rise calculation, TMRad curve.

### Scale-up factor exceeds 10x in volume with no intermediate pilot run
- **Usually means:** the controlling regime (kinetics vs. heat/mass transfer) assumed at bench has not been verified to hold at the new scale.
- **First question:** was the bench result kinetics-limited or transfer-limited, and how was that distinguished?
- **Data to pull:** bench mixing/agitation rate vs. reaction rate data, Damköhler number if calculated, pilot-scale cooling capacity calculation.

### HAZOP finding marked "closed" with no corresponding document change
- **Usually means:** administrative closure without an engineering fix, procedure revision, or P&ID update — the hazard is still present.
- **First question:** which specific drawing, procedure, or setpoint changed as a result of this finding?
- **Data to pull:** HAZOP action-item tracker, revision history of the referenced P&ID or SOP.

### Relief valve sized only against the fire case for a vessel with credible reaction runaway
- **Usually means:** relief sizing basis didn't consider the runaway scenario, or assumed vapor-only (single-phase) flow when the reacting fluid can foam or two-phase during venting.
- **First question:** was the relief load calculated for the runaway scenario per DIERS methodology, and is it single- or two-phase?
- **Data to pull:** relief sizing calculation package, DIERS vent-sizing worksheet if applicable.

### Two protection layers in a LOPA scenario share one sensor or logic solver
- **Usually means:** the layers aren't independent — a single failure (the shared sensor) defeats both simultaneously, so the calculated risk reduction is overstated.
- **First question:** trace each counted layer's sensor, logic solver, and final element back to the initiating cause — do any two layers share a component?
- **Data to pull:** instrument loop diagrams for each counted layer, LOPA worksheet.

### Degrees of freedom (DOF) not verified before trusting a solved mass/energy balance
- **Usually means:** the balance was solved with an underspecified system (DOF>0, curve-fit to whatever was measured) or an overspecified one (DOF<0, conflicting data averaged away).
- **First question:** how many independent equations and how many unknowns does this balance node have?
- **Data to pull:** the balance model's stream table with measured vs. calculated flags on every value.

### New reagent or waste stream co-mingled without a documented compatibility check
- **Usually means:** nobody checked reactivity compatibility because the new stream "looked similar" to an existing one.
- **First question:** has this specific pairing been checked against a chemical compatibility/reactivity reference?
- **Data to pull:** compatibility chart lookup (e.g., NOAA CAMEO Chemicals), MSDS/SDS reactivity sections for both streams.

### Management of change (MOC) not initiated for a setpoint or procedure change
- **Usually means:** the change was judged "minor" without a documented risk-ranking, bypassing the review that would have caught an interaction with an existing safeguard.
- **First question:** does this change alter any assumption underlying an existing HAZOP finding or LOPA layer?
- **Data to pull:** MOC log, the specific HAZOP/LOPA record referencing the affected equipment.

### Process safety information (PSI) package incomplete within 30 days of planned startup
- **Usually means:** documentation (P&IDs, relief basis, material hazard data) is being assembled reactively rather than maintained as design progresses.
- **First question:** which specific PSI element (chemistry, technology, or equipment) is missing, and who owns closing it?
- **Data to pull:** PSI checklist per OSHA 1910.119(d), open-item tracker with owners and dates.

### Jacket or cooling-loop U-value used in scale-up calc taken from bench data unchanged
- **Usually means:** overall heat-transfer coefficient at plant scale is assumed equal to bench, ignoring reduced turbulence/mixing efficiency typical at larger vessels.
- **First question:** was U re-estimated for the plant vessel's agitation and jacket configuration, or copied from the bench number?
- **Data to pull:** vessel agitation design (impeller type, tip speed), correlation used for U at each scale.
