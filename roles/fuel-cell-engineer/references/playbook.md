# Fuel Cell Engineer — Playbook

## Voltage-decay triage worksheet

Fill this before naming a mechanism. Each row is a discriminator, not a suggestion.

| Signal | Membrane crossover | Start-stop (carbon corrosion) | Cold-start (freeze) |
|---|---|---|---|
| HFR (high-frequency resistance) trend | Rising steadily | Stable | Stable, sudden step at cold-soak boundary |
| Decay timing | Continuous, accelerates over time | Confined to shutdown/startup transients | Confined to sub-freezing startup events |
| ECSA (electrochemical surface area) loss | Moderate, gradual | Sharp drop correlated with key-cycle count | Minimal — pore blockage, not catalyst loss |
| Crossover current (H2 permeation test) | Elevated, rising | Normal | Normal |
| Fastest confirming test | Open-circuit voltage (OCV) hold + crossover current measurement | 200-cycle key-cycle stress test, ECSA before/after | Startup time-to-rated-power at target sub-zero temp |
| Typical fix | Reinforced/thinner-crossover-resistant membrane, humidity control | Corrosion-resistant carbon support, fast anode purge, or current-bypass device | Antifreeze shutdown purge + elevated startup current density |

**Decision rule:** if HFR is stable and decay is confined to shutdown events → start-stop. If HFR is stable and decay is confined to sub-zero startups → cold-start. Otherwise, rising HFR with continuous decay → membrane, run the crossover-current confirming test before committing budget to a membrane change.

## Accelerated stress test (AST) selection and logging table

| Question | Protocol | Conditions | Acceleration factor | What it does NOT test |
|---|---|---|---|---|
| Catalyst/support durability? | U.S. DRIVE FCTT catalyst-AST | 0.65–0.9 V square wave, 3 s/step, H2 anode/N2 cathode, 80°C, 100% RH | ~25× vs. real-world catalyst decay | Membrane durability, start-stop, cold-start |
| Membrane durability? | Modified wet drive-cycle, low-humidity phase | Alternating high/low RH phases, continuous load | Not a single multiplier — phase-specific | Start-stop transients (protocol has none) |
| Start-stop durability? | Supplementary key-cycle stress test | N key-cycles (H2/air front transient each cycle), rated-power voltage checkpoint every 50 cycles | Per-cycle decay rate (mV/event), not a single AF | Continuous-load catalyst/membrane decay |
| Cold-start capability? | Sub-zero startup sweep | Soak at target temp (e.g., −20°C, −30°C) ≥4 h, then startup with time-to-rated-power measured | N/A — pass/fail against a time threshold, not an AF | Long-term durability at any temp |

**Logging fields per AST run (fill every time, no exceptions):** protocol name, cycle/hour count at test end, rated-power cell voltage at cycle 0 and at test end, HFR at cycle 0 and at test end, ECSA at cycle 0 and at test end, ambient RH/temp, catalyst loading (mg_PGM/cm²). A durability number without these fields is not comparable to any target.

## Stack compression (torque) sweep protocol

1. Set torque wrench to the low end of the literature starting bracket: **80 psi overall clamping pressure** (or ~3 MPa local at GDL contact points) as the first sweep point — not a final spec.
2. Run a polarization curve (IV sweep, 0.05 A/cm² increments) at each torque step. Minimum 4 points across the bracket, e.g., 80 / 110 / 140 / 160 psi (or the oz-in equivalent for the fixture's torque spec).
3. Plot peak power density vs. torque. Expect an inverted-U: rising contact quality (falling ohmic resistance) at low torque, falling gas-diffusion performance (GDL porosity choke) at high torque.
4. Identify the peak and the two adjacent points that show measurable decline (>2% power density drop from peak) — this brackets the stack's own optimum, not a portable number.
5. Re-run the peak-torque point a second time to confirm repeatability (±1.5% power density) before locking the build spec.
6. Record per stack build: fixture type, torque tool, measured peak, and decline bracket. Every new stack design (new bipolar plate, new GDL) restarts this sweep — the sources' own comparison (36 oz-in / 10 oz-in / 4 oz-in peaks across three different stack builds) is why an imported number is a starting bracket, never a spec.

Example filled sweep (illustrative — replace with this stack's measured data):

| Torque | Peak power density (W/cm²) | Δ from peak |
|---|---|---|
| 80 psi | 0.61 | −4.7% |
| 110 psi | 0.64 | 0% (peak) |
| 140 psi | 0.62 | −3.1% |
| 160 psi | 0.57 | −10.9% |

## Start-stop mitigation selection

| Duty cycle profile | Preferred mitigation | Why | Fallback |
|---|---|---|---|
| High key-cycle frequency (>8 starts/operating day), material change is fundable | Corrosion-resistant carbon support (graphitized or non-carbon support) | Attacks the mechanism at the electrode, no added mass/cost per cycle | Fast anode purge (shrink H2/air front dwell time) |
| High key-cycle frequency, hardware retrofit is cheaper than a materials qualification cycle | Auxiliary-load current-bypass device | Suppresses the reverse-current condition without touching the MEA | Fast anode purge, combined with purge-timing optimization |
| Low key-cycle frequency (<2 starts/operating day) | Fast anode purge alone, monitor and re-assess at next qualification cycle | Mitigation cost should scale with exposure — full support-material change is overkill below this threshold | None — re-evaluate if duty cycle changes |

## Cold-start mitigation decision sequence

1. Confirm the requirement: what is the coldest specified startup temperature, and what is the required time-to-rated-power at that temperature?
2. If target ≥ −20°C: elevated startup current density alone is often sufficient — verify with the sub-zero startup sweep before adding shutdown procedures.
3. If target < −20°C: add antifreeze-based shutdown purge (residual water displaced before soak) as the first-line intervention, layered under elevated startup current density.
4. Only after both of the above are verified insufficient (time-to-rated-power still exceeds spec) should membrane or catalyst-layer changes (e.g., altered pore-former ratio) be considered — those are the most expensive, slowest-to-qualify lever and should be last, not first.
5. Re-verify with a full sub-zero startup sweep (≥3 consecutive cold-soak/startup cycles) before declaring the mitigation adequate — a single successful cold start is not a qualification.

## Simultaneous-target readout template

Fill and report as one table per qualification run — never as separate line items from different runs.

| Target | 2025 DOE value | This run's result | Same run as others? | Met? |
|---|---|---|---|---|
| Efficiency (peak, %) | 65 | *(fill)* | Y/N | *(fill)* |
| Durability (h to 10% decay) | 5,000 | *(fill)* | Y/N | *(fill)* |
| Power density (W/cm²) | *(fill target)* | *(fill)* | Y/N | *(fill)* |
| Cost ($/kW, projected at volume) | *(fill target)* | *(fill)* | Y/N | *(fill)* |

If any "Same run as others?" column reads N, the readout must say so explicitly before any "Met?" column is presented upstream — a target met on a different test run than the others is not a simultaneous result.
