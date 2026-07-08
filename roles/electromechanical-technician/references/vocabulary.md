# Vocabulary — terms generalists misuse

Terms an electromechanical technician uses precisely, and where a blurred distinction changes the diagnosis.

## Polarization Index (PI) vs. Insulation Resistance (IR) floor

**IR floor** is the minimum acceptable 1-minute megger reading, per IEEE 43: rated voltage in kV + 1 MΩ (460 V motor → 1.46 MΩ). **PI** is a different measurement on the same test — the ratio of the 10-minute reading to the 1-minute reading (PI = R₁₀ / R₁) — capturing absorption *trend*, not an absolute value.
**In use:** "IR passed at 3.2 MΩ against a 1.46 MΩ floor, but PI came back 1.28 — that's contamination, not a clean winding."
**Common misuse:** treating "cleared the floor" and "insulation is fine" as the same sentence, and applying a flat "1 MΩ is good" rule from memory instead of the voltage-indexed floor.

## Forcing (I/O force)

A PLC feature that overrides the physical state of an input or output point at the hardware level, independent of what the ladder logic internally computes for that same tag.
**In use:** "The output's forced true, but the internal logic bit downstream still reads false — forcing changed the physical point, not the processor's math."
**Common misuse:** assuming a forced point makes every rung referencing it behave as if genuinely true — it doesn't propagate through internal logic the way a real transition does.

## JSR (Jump to Subroutine) vs. MCR (Master Control Reset)

**JSR** is the ladder instruction that calls a subroutine during a scan; a routine present in the project but never called by a JSR never executes. **MCR** is a zone-control instruction pair that de-energizes every non-retentive output between it and its END-MCR when the MCR condition is false — regardless of what each individual rung says.
**In use:** "The rung reads correct, but it's either dead code with no JSR calling it, or sitting behind an MCR that dropped on the E-stop — check both before assuming a logic bug."
**Common misuse:** reading correct-looking ladder and assuming it runs because it's present in the project, or troubleshooting rung-by-rung and missing that an MCR block kills a whole downstream zone.

## Pressure decay test vs. ultrasonic leak detection

**Decay test** pressurizes a component to a set value and measures pressure drop over time, isolating *internal* leakage (past a piston seal). **Ultrasonic leak detection** listens for the high-frequency hiss of gas escaping an external orifice, localizing *external* leakage. They answer different questions and neither substitutes for the other.
**In use:** "Decay test showed 3 psi drop in 60 s — internal bypass. Ultrasonic then pinpointed a separate external leak at the rod-end fitting."
**Common misuse:** using "decay test" and "leak test" interchangeably, or running whichever test is familiar instead of the one that matches internal vs. external.

## Zone (ISO 10816/20816) vs. broadband/spectral (FFT) vibration analysis

**Zone** (A–D) classifies *overall* broadband RMS velocity by machine class; A/B = acceptable, C = plan corrective action, D = stop and repair. **Broadband** is that single overall number; **spectral/FFT** breaks the signal into discrete frequency components to identify a specific fault (bearing, gear mesh, imbalance).
**In use:** "2.6 mm/s puts a Class II machine in Zone B — acceptable overall, but that's not a fault-frequency finding; pull an FFT before clearing a suspected bearing defect."
**Common misuse:** treating "in Zone A or B" as "no problem, full stop" — zone reads severity only, not fault location, and an early-stage defect can sit in Zone A/B while already visible in an FFT spectrum.

## Motor current signature analysis (MCSA) sideband

A frequency component at f₁(1 ± 2s) around line frequency in a motor's current spectrum (f₁ = line frequency, s = slip), indicating broken rotor bars; analogous BPFI/BPFO-modulated sidebands indicate bearing race defects.
**In use:** "Sideband at f₁(1±2s) is up 8 dB from baseline — consistent with a developing rotor bar crack, not load variation."
**Common misuse:** treating MCSA as an overall current-magnitude check — the diagnostic content is in the sideband frequency structure, and a normal-looking RMS current can still carry one.

## RPM-indexed alignment tolerance

A shaft alignment acceptance table whose angular/offset tolerance tightens as RPM increases, distinct from the generic rule-of-thumb figure (~0.5 mils/inch angular) that applies loosely across all speeds.
**In use:** "It passed the mils/inch rule of thumb, but at 3,600 RPM the actual table tolerance is tighter — recheck against the RPM-indexed number before calling it aligned."
**Common misuse:** using the rule of thumb as the accept/reject criterion instead of a first-pass screen — why some alignments "pass" and then keep vibrating.

## Pull test (crimp)

A destructive or proof-load test applying axial tension to a crimped termination at a controlled rate (~25 mm/min), measuring force at failure against IPC/WHMA-A-620 class and wire-gauge minimums.
**In use:** "Crimp looked tight by eye, but it pull-tested at 60% of the class-2 minimum for 20 AWG — reject and re-crimp."
**Common misuse:** accepting a crimp by visual/tactile inspection, which cannot detect an under-crimped strand count or insertion-depth issue that only shows up under tensile load.

## Incident energy vs. PPE category (arc flash)

**Incident energy** (cal/cm²) is the calculated/measured thermal energy at a working distance from an arc-flash event. **PPE category** (CAT 1–4, NFPA 70E Table 130.7(C)(15)(a)) is a simplified lookup mapping equipment type/voltage/fault-current class to a minimum PPE rating without a site-specific calculation.
**In use:** "No incident-energy study on file, so default to the category table — CAT 2 for this equipment class, not CAT 1 because it's 'just a control cabinet.'"
**Common misuse:** selecting PPE by panel size or habit — a compact 480 V MCC bucket can carry a higher incident energy than a large low-fault-current panel.

## De-energized verification (vs. LOTO alone)

The step of confirming zero energy state with a rated meter *after* LOTO is applied and *before* contact — LOTO isolates the source, de-energized verification confirms the isolation worked on this specific point.
**In use:** "LOTO's applied, but verify de-energized at the terminals with the meter before you touch anything — don't assume the lock means zero volts here."
**Common misuse:** treating "LOTO is on" as equivalent to "the circuit is dead" — LOTO can be applied to the wrong disconnect, or miss a back-fed circuit or a charge-holding capacitor.
