# Vocabulary

Terms of art a generalist typically misuses — not because the definition is hard to find, but because the word gets used loosely in a way that erases a distinction this role depends on.

## HFR (high-frequency resistance)

**Definition.** The real-axis intercept of the impedance spectrum at high frequency (typically ~1 kHz) during EIS, isolating the ohmic (membrane + contact) resistance from the charge-transfer resistance that dominates at lower frequencies.

**In use:** "HFR was stable across the 1,200 h run, so the 14 mV decay isn't a membrane-conductivity story — look at charge-transfer resistance instead."

**Misuse note.** Generalists use "resistance" as a single undifferentiated number pulled off a polarization curve's slope. HFR is specifically the ohmic component isolated by EIS; treating overall cell resistance and HFR as interchangeable erases exactly the distinction that tells you whether decay is membrane-thinning (HFR rises) or catalyst/support-related (HFR flat, charge-transfer resistance rises).

## ECSA (electrochemically active surface area)

**Definition.** The catalyst surface area actually available for the reaction, measured via cyclic voltammetry (hydrogen underpotential deposition charge), as opposed to the total or geometric catalyst area loaded onto the electrode.

**In use:** "ECSA loss consistent with a carbon-support corrosion signature — the Pt is still there, but the support it's sitting on has washed away."

**Misuse note.** People conflate ECSA loss with "less catalyst" (i.e., Pt dissolution or loss of loading). ECSA loss is equally and often primarily driven by carbon-support corrosion stranding still-present Pt particles so they're no longer electrically connected — same measured signature, different mechanism and different fix.

## AST (accelerated stress test)

**Definition.** A named, standardized protocol (e.g., the U.S. DRIVE FCTT catalyst-AST or modified wet drive-cycle) engineered to accelerate one specific degradation mechanism through a defined electrical/thermal/humidity waveform, with a stated acceleration factor for that mechanism only.

**In use:** "The catalyst-AST reports 25× acceleration for catalyst/support degradation — it says nothing about membrane durability."

**Misuse note.** Generalists treat "AST" as a generic label for "we ran it hard" or "we sped up the clock," implying the results generalize to overall durability. An AST is mechanism-specific: passing the catalyst-AST tells you nothing about membrane crossover or cold-start survivability, because those need their own AST with a different waveform.

## Cell reversal

**Definition.** A cell within a stack going to negative voltage because it runs out of reactant (fuel starvation) while forced to carry the stack's common current — the cell is driven to oxidize its own carbon support or electrolyze water to source protons/electrons instead of consuming H2.

**In use:** "Check for localized fuel starvation before assuming this is uniform start-stop corrosion — cell reversal produces a single-cell voltage signature, not a stack-wide one."

**Misuse note.** People use "reversal" as a synonym for "any big voltage drop." It specifically means a cell forced negative by starvation under common-current constraint, and it's diagnosed cell-by-cell (not from stack average voltage) — averaging across the stack can hide the one starved cell producing it.

## Stoichiometry ratio (stoich)

**Definition.** The ratio of reactant gas actually supplied to the theoretical amount consumed by the current draw (e.g., stoich of 1.5 means 50% excess flow) — set independently for anode (H2) and cathode (air) to manage water balance and starvation margin, not just to "feed the reaction."

**In use:** "Cathode stoich was cut to chase efficiency, but that's exactly the trade that starves cells under transient load spikes."

**Misuse note.** Generalists treat stoich purely as a fuel-efficiency knob (lower stoich = less waste = better economy). It's also the starvation safety margin and the primary lever for membrane water balance — cutting it for efficiency without checking transient-load starvation risk is how "efficiency improvement" becomes a reversal/carbon-corrosion root cause months later.

## BOP (balance of plant)

**Definition.** Every subsystem in the fuel cell system other than the stack itself — cathode air path (filter, MAF sensor, compressor, heat exchanger, humidifier), anode recirculation blower and purge valve, coolant loop, and controls — that determines what the stack actually experiences as its operating conditions.

**In use:** "Before blaming the membrane, check the BOP — a humidifier fault would produce the same dry-out decay signature."

**Misuse note.** "BOP" gets used as a dismissive catch-all ("just balance-of-plant stuff," implying it's secondary to the "real" stack engineering). In practice BOP failures (humidification, purge scheduling, air supply) produce decay signatures that mimic stack-intrinsic degradation — ruling out BOP is a required diagnostic step, not an afterthought.

## Compression / clamping pressure

**Definition.** The mechanical force (expressed as assembly torque, or resulting psi/MPa) holding stack layers together, which sets GDL-to-bipolar-plate contact resistance on one side and GDL porosity/gas-diffusion path on the other — with a stack-specific optimum, not a portable target.

**In use:** "Stack 3's torque-sweep optimum was 4 oz-in, degrading above 6 — don't import Stack 1's 36 oz-in spec onto this build."

**Misuse note.** Generalists treat clamping pressure as a single "more is better" (tighter = better contact = better performance) or reach for a datasheet psi number as a spec to hit. Both directions of error are real: under-torque raises contact resistance, over-torque chokes GDL porosity — and the optimum doesn't transfer between stack designs, so a psi number from another program is a starting bracket, never a target.

## MEA (membrane electrode assembly)

**Definition.** The catalyst-coated membrane plus adjacent gas-diffusion layers, bonded as a unit — the layer where crossover, catalyst degradation, and water transport all physically occur, as distinct from the bipolar plates and flow fields that sandwich it.

**In use:** "The MEA supplier's datasheet loading was 0.4 mg-Pt/cm², not the 0.125 target this durability number assumes."

**Misuse note.** People use "MEA" and "stack" interchangeably when describing where a failure occurred. Degradation mechanisms (crossover, ECSA loss, carbon corrosion) are MEA-level phenomena; compression and contact-resistance issues are stack-assembly-level — conflating the two sends a materials problem to the mechanical-build team or vice versa.

## PGM loading (catalyst loading)

**Definition.** The mass of platinum-group metal per unit active area (mg-PGM/cm²), a cost and durability lever reported alongside — never as a substitute for — any durability figure, since a given decay rate at 0.4 mg/cm² does not predict the decay rate at the 0.125 mg/cm² DOE target loading.

**In use:** "The 4,130 h NREL figure didn't report catalyst loading, so it can't be directly compared against a 0.125 mg-PGM/cm² target stack."

**Misuse note.** Generalists read "loading" as a cost/spec detail incidental to the durability headline number. It's a load-bearing caveat: lower loading generally degrades faster per unit time, so a durability hour-count without the accompanying loading figure is not comparable to a target defined at a specific loading.

## Decay rate (mV/h or mV/1000h)

**Definition.** The linear or projected rate of rated-power cell-voltage loss over time under a specified test protocol, used to extrapolate a failure-threshold hour count — meaningless without stating which protocol and duty-cycle mix produced it.

**In use:** "0.01167 mV/h under the continuous drive-cycle AST projects to ~5,829 h — but that protocol has zero start-stop events, so it isn't the fleet's real decay rate."

**Misuse note.** People extrapolate a single decay rate measured under one protocol (e.g., continuous operation) to the vehicle's whole service life, silently assuming the missing stress types (start-stop, cold-start) contribute nothing. Decay rate is protocol-conditional, not a stack-intrinsic constant — combining decay rates from different stress types requires adding their contributions, not picking the worse single number.

Cold-start and the start-stop reverse-current mechanism are covered in SKILL.md First-principles #2 and worked through in `playbook.md`'s triage table and mitigation sequences — not re-glossed here to avoid restating the same mechanism a third time.
