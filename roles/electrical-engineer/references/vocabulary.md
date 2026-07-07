# Power-systems working vocabulary

Terms an electrical engineer uses daily and precisely. Format: definition → how a practitioner says it → common misuse.

**Bolted fault current** — The theoretical maximum three-phase short-circuit current at a point in the system, assuming a zero-impedance (bolted) connection between phases with no arc resistance.
**In use:** "Bolted fault at the panel is 11,431 A — that's the number we check the breaker's AIC rating against."
**Misuse:** using bolted fault current as the input to the arc-flash calculation directly, instead of the (lower) arcing fault current an actual arc produces.

**Arcing fault current** — The current that actually flows during an arcing fault, always lower than bolted fault current because the arc itself adds impedance; the value that drives incident-energy calculations.
**In use:** "Arcing current at 15% of bolted is 1,715 A — that's the scenario that governs here, not the bolted value."
**Misuse:** assuming arcing current scales linearly with incident energy, missing that a lower arcing current can produce higher energy if it drops below a breaker's instantaneous pickup.

**%Z (percent impedance)** — A transformer's impedance expressed as a percentage of its rated voltage, used to compute available fault current on the secondary; also the common unit for combining multiple impedances on a shared base.
**In use:** "Transformer's 5% Z on a 500 kVA base converts to about 0.26% for the utility source on the same base — they add directly once you're on a common base."
**Misuse:** combining %Z values calculated on different kVA bases without first converting to a common base, which silently produces the wrong total impedance.

**Point-to-point method** — A short-circuit calculation method (Cooper Bussmann/Eaton) that combines source and transformer impedance in series to compute available fault current at a downstream point, without requiring full per-unit modeling software.
**In use:** "Point-to-point gives us 11,431 A at the panel once we add the utility source contribution to the transformer's %Z."
**Misuse:** applying only the transformer's %Z (skipping the source term) and calling it the point-to-point result — the method's entire value is combining both.

**X/R ratio** — The ratio of reactance to resistance at a fault point, which determines the asymmetry (DC offset) of the fault current waveform and affects equipment duty ratings beyond the symmetrical RMS value.
**In use:** "X/R at this bus is high enough that we need to check the breaker's asymmetrical rating, not just the symmetrical Isc."
**Misuse:** comparing a device's interrupting rating only against symmetrical fault current when the system X/R exceeds the rating's test X/R, ignoring the asymmetry adjustment.

**Incident energy** — The thermal energy (cal/cm²) an arc flash would deliver to a person at a specified working distance, the core output of an IEEE 1584 arc-flash study and the basis for PPE category assignment.
**In use:** "Incident energy comes out to 14.8 cal/cm² at the 15% arcing-current case — that's Category 3."
**Misuse:** reporting incident energy from only the 100%-bolted-fault scenario, missing a higher reduced-current result.

**Arc flash boundary** — The distance from an arc-flash source at which incident energy equals 1.2 cal/cm² (the threshold for a just-curable second-degree burn) — the distance inside which PPE is required.
**In use:** "Arc flash boundary is 6.2 ft on this panel — inside that, PPE per the label is required."
**Misuse:** confusing the arc flash boundary (thermal hazard) with the shock approach boundaries (electrical contact hazard) — they're calculated independently and are rarely the same distance.

**PPE category** — A standardized tier (per NFPA 70E Table 130.7(C)(15)(a)) mapping a range of incident energy to a required minimum arc-rated PPE ensemble.
**In use:** "This panel's 14.8 cal/cm² puts it in Category 3, not Category 2 — the ensemble changes at that boundary."
**Misuse:** picking a PPE category from a device's voltage class or a rule of thumb instead of the actual calculated (or table-method) incident energy for that specific location.

**Instantaneous pickup** — The current threshold above which a breaker trips with no intentional time delay (typically 1-3 cycles); below this threshold, clearing shifts to the slower short-time or long-time-delay bands of the curve.
**In use:** "Arcing current at the 15% case falls below CB-12's 3,000 A instantaneous pickup — that's why clearing time jumps to 0.4 seconds."
**Misuse:** assuming a breaker always clears "fast" regardless of current magnitude, without checking where the actual fault current falls relative to the instantaneous pickup setting.

**Selective coordination (selectivity)** — The property of series-connected protective devices such that, on any downstream fault, only the nearest upstream device operates, leaving unaffected circuits energized.
**In use:** "Coordination margin between CB-12 and CB-2A is only 0.09 seconds at the maximum through-fault current — tight, flag it."
**Misuse:** confirming coordination only at each device's rated current instead of at the actual maximum through-fault current, where curves can converge even if they're well separated near rated current.

**Demand factor** — A code-defined ratio applied to connected load to account for non-coincident operation, producing the demand load actually used to size service and feeder equipment.
**In use:** "First 3,000 VA of general lighting gets 100%, the remainder gets 35% — that's the Table 220.42 demand factor."
**Misuse:** summing nameplate connected load without applying the applicable demand factor, producing an oversized service.

**Voltage drop** — The reduction in voltage between source and load due to conductor impedance under load current, expressed as a percentage of nominal voltage.
**In use:** "Combined feeder and branch drop comes out to 4.1% at full load — under our 5% design target."
**Misuse:** treating the 3%/5% voltage-drop figures as a hard NEC violation threshold rather than the code's informational design guidance — equipment-specific tolerances (VFDs, electronics) may require a tighter target regardless.

**AIC rating (interrupting rating)** — The maximum fault current a protective device is certified to safely interrupt; distinct from its continuous ampere (ampacity) rating.
**In use:** "This breaker's 600A continuous rating is fine for the load, but its 10kA AIC rating is below our 11,431A calculated fault current — needs a higher-rated device."
**Misuse:** confirming only that a device's continuous ampere rating matches the load, without separately checking its AIC rating against the calculated available fault current.

**Equipment grounding conductor (EGC)** — The conductor that provides a low-impedance fault-current return path to the source, sized from the overcurrent device rating per the applicable grounding table — not scaled proportionally to the ungrounded (phase) conductor.
**In use:** "EGC size comes straight off the grounding table at the 400A OCPD rating, not scaled from the 500 kcmil phase conductor."
**Misuse:** assuming EGC size scales linearly with phase conductor size at all conductor sizes, which diverges from the actual table at larger sizes.

**Power factor correction (kVAR)** — Capacitance added to a system to reduce the phase difference between voltage and current, sized in kVAR to move an existing power factor to a target value.
**In use:** "We need 110.7 kVAR to move this load from 0.82 to 0.95 PF — that's kW times the tangent difference."
**Misuse:** sizing correction capacitance by trial and error against a utility bill instead of calculating kVAR = kW × (tanθ_existing − tanθ_target), risking overcorrection into a leading PF.

**Single-line diagram** — A simplified schematic representing a three-phase power system with a single line, showing every major component (source, transformers, breakers, buses) and the impedance/rating data needed to run short-circuit and coordination studies.
**In use:** "Pull the current single-line before we start the study — if T-1's %Z on the drawing doesn't match the nameplate, the whole study is built on the wrong number."
**Misuse:** treating the single-line diagram as a static as-built drawing rather than a live input to every subsequent study — an unrevised diagram after an equipment change invalidates studies built from it.
