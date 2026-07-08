# Fuel Cell Engineer — Red Flags

### Efficiency or durability target reported as "met" without the other DOE-class metrics from the same qualification run
- **Usually means:** the readout is a single-metric win being sold as full-spec compliance — efficiency, durability, power density, and cost were not all demonstrated simultaneously on one system, the way DOE's own status records explicitly caveat.
- **First question:** were efficiency, durability, power density, and cost all measured on this same stack in this same test run, or are they being stitched together from different builds/tests?
- **Data to pull:** the qualification test report for all four metrics with run ID/date, DOE 2025/ultimate target table for comparison.

### Durability figure (hours to 10% voltage decay) quoted without catalyst loading (mg_PGM/cm²) or test protocol stated
- **Usually means:** the number is being treated as universally comparable when it's only valid for the loading and protocol it was measured under — a 4,130 h fleet figure at unstated loading doesn't validate a 0.125 mg_PGM/cm² target design.
- **First question:** what catalyst loading and AST/drive-cycle protocol produced this durability number, and does it match the target design's loading?
- **Data to pull:** MEA catalyst loading spec sheet, AST protocol name and parameters used to generate the durability figure.

### Voltage decay rate projects >10% of BOL rated-power voltage before the stated service-life target, using a continuous-only AST
- **Usually means:** the continuous-cycle acceleration test never exercised start-stop (reverse-current carbon corrosion) or cold-soak (freeze) stress, so the projected durability excludes the fleet's dominant real-world degradation mode.
- **First question:** does the fleet's actual duty cycle include start-stop or cold-start events, and were those events represented in the AST that produced this projection?
- **Data to pull:** decay-rate calculation and its source AST protocol, fleet duty-cycle log (events/day), a supplementary start-stop or cold-start stress-test result if one exists.

### Stack clamping torque/compression spec imported from another build or a single datasheet psi number, with no torque sweep on this stack
- **Usually means:** compression has no portable optimum — it's build-specific (three tested stacks peaked at 36, 10, and 4 oz-in respectively) — so a copied number is as likely to be past this stack's optimum as at it.
- **First question:** was a torque sweep with a polarization curve at each step run on this specific stack build, or is the number copied from elsewhere?
- **Data to pull:** torque-sweep polarization-curve data set (voltage vs. torque at fixed current), the source of the imported spec if one was used.

### Voltage decay diagnosed as membrane crossover without checking whether HFR is stable and decay is confined to shutdown/cold-soak events
- **Usually means:** all three major decay mechanisms (membrane crossover, start-stop carbon corrosion, cold-start ice blockage) look like generic "voltage decay" on a summary chart, and defaulting to membrane crossover skips the signature check that would catch the other two.
- **First question:** is HFR stable or rising, and is the decay continuous or concentrated at shutdown/cold-soak transitions?
- **Data to pull:** HFR (EIS) trend over the test, polarization-curve delta timestamped against shutdown/cold-soak events.

### An AST acceleration factor from one named protocol applied to a different degradation mechanism than it was validated for
- **Usually means:** the U.S. DRIVE catalyst-AST's cited 25× acceleration factor is specific to catalyst/support degradation — applying it to membrane or cold-start durability claims a speed-up the protocol was never shown to produce for that mechanism.
- **First question:** which mechanism was this acceleration factor derived for, and is that the same mechanism being projected here?
- **Data to pull:** the AST protocol document naming its target mechanism and reported acceleration factor, the mechanism signature (HFR/ECSA trend) of the actual decay being projected.

### Cold-start spec colder than −20°C addressed only through membrane or catalyst material changes
- **Usually means:** below roughly −20°C, cold-start failure is dominated by ice physically blocking cathode catalyst-layer pore volume — a transport/thermal problem — not a materials-degradation problem, so a materials-only fix leaves the actual failure mode unaddressed.
- **First question:** has the ice-blockage mechanism been separated from materials degradation by cold-soak startup data, or is the fix based on materials debugging alone?
- **Data to pull:** cold-soak startup current-density/voltage trace, shutdown-storage strategy documentation (antifreeze/purge), startup current-density profile used.

### Start-stop mitigation hardware/material chosen without reference to the fleet's key-cycle frequency (events/day)
- **Usually means:** corrosion-resistant carbon support and fast anode purge suit high-key-cycle fleets, while an auxiliary current-bypass device suits fleets where hardware is cheaper than a materials change — picking one without the duty-cycle number is a guess, not a sizing decision.
- **First question:** what is this fleet's measured or projected start-stop events per operating day, and does the chosen mitigation's cost/benefit match that frequency?
- **Data to pull:** fleet duty-cycle log (start-stop events/day), cost/degradation-per-event comparison for the candidate mitigations.

### Reverse-current cathode potential exceeding 1.5 V during a shutdown H2/air transient not flagged or measured
- **Usually means:** an unmeasured shutdown transient above 1.5 V is the specific condition that drives carbon-support corrosion — if it isn't instrumented, start-stop degradation is accumulating unseen even while continuous-AST numbers look fine.
- **First question:** is cathode potential instrumented and logged during shutdown transients, and has it been checked against the 1.5 V corrosion threshold?
- **Data to pull:** shutdown-transient cathode-potential trace, ECSA (electrochemical surface area) loss trend as a corroboration signal.

### Light-duty durability figure (8,000 h ultimate target) scaled linearly to a heavy-duty claim (25,000 h ultimate target)
- **Usually means:** heavy-duty/long-haul durability is a distinct, unmet frontier problem, not a multiple of the light-duty number — a linear scale-up overstates confidence in a duty cycle and thermal/load profile that hasn't actually been tested.
- **First question:** has this stack been tested under a heavy-duty-representative duty cycle, or is the 25,000 h figure derived by scaling the light-duty result?
- **Data to pull:** the heavy-duty test protocol and duty-cycle profile actually used (if any), the calculation basis for any scaled projection.

### HAZOP-style compression range (80–160 psi / 3–4 MPa literature bracket) treated as a hard target rather than a sweep starting bracket
- **Usually means:** overcorrecting against "imported specs aren't portable" into refusing any starting reference, which wastes sweep time re-deriving a range from zero instead of using the literature bracket to bound the search.
- **First question:** is the literature range being used as the initial sweep bracket (with measurement to find this stack's actual optimum), or as a value to hit directly without measurement?
- **Data to pull:** the torque-sweep test plan showing the bracket used and the measured optimum found within or outside it.
