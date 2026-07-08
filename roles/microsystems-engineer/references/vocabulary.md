# Vocabulary

Working terms of art that generalists (or engineers new to MEMS) routinely misuse — not terms you could just look up and get right, but terms whose common usage papers over a distinction that changes the design or the failure diagnosis.

**Pull-in (electrostatic instability point)**
Definition: The displacement (≈g/3 for a parallel-plate actuator with linear spring) past which the electrostatic force gradient exceeds the mechanical restoring-force gradient, so the plate accelerates uncontrollably to contact regardless of further voltage change.
In use: "Size the sense range to stay under pull-in — x_pi = g/3 for this gap, not the full physical gap."
Misuse note: Generalists use "pull-in" and "snap-down" interchangeably, or conflate pull-in with "hitting the mechanical stop." Pull-in is an instability *threshold* — a point where control is lost — not a contact event. A design can pull in and never touch a physical stop if the stop is misplaced past x_pi, which is precisely the stiction failure mode in this role's worked example.

**Snap-down**
Definition: The physical contact event that follows pull-in — the plate accelerating from the pull-in point to the opposing surface or stop under the now-unbalanced electrostatic force.
In use: "The 9% self-test failures are snap-down events triggered because the stop sits past pull-in, not at it."
Misuse note: Treated as a synonym for pull-in. Keeping them distinct matters for diagnosis: pull-in is the geometric/electrical threshold you compute at design time; snap-down is the observed physical event during failure analysis. A report that says "pull-in occurred" when it means "the part snapped down and stuck" obscures whether the root cause is instability (wrong stop placement) or something else (voltage transient).

**Hermeticity**
Definition: A package's tested leak rate as measured against a specific standard method's detection floor — a pass/fail result relative to that method's resolving power, not an absolute statement about the seal.
In use: "The package passed Method 1014, but hermeticity here is bounded by the test's ~5×10⁻¹¹ atm·cm³/s resolution floor, not the actual leak rate."
Misuse note: Generalists treat "hermetic" (passed the test) and "sealed" (no meaningful leak path exists) as the same claim. For a cavity under ~10⁻³ cm³, a real leak can sit an order of magnitude below what the standard test can detect — "passed hermeticity" is a statement about test resolution, not proof of a sealed package.

**Leak-tightness**
Definition: The cavity's actual physical leak rate, independent of whether any given test method can resolve it.
In use: "Leak-tightness for this cavity volume needs a tracer/accumulation method — Method 1014 can't resolve it."
Misuse note: Used loosely as a synonym for "hermeticity" when it should be the thing hermeticity testing is trying (and sometimes failing) to measure. Separating the two forces the question "does our test method actually resolve the leak rate this cavity needs?" instead of stopping at "did it pass."

**Aspect ratio (DRIE, process-tier-qualified)**
Definition: The etch depth-to-width ratio a given fabrication process can reliably achieve, which is not a single number for a process — it drops from roughly 80:1 at R&D/lab scale to ~60:1 at development scale to ~40:1 at mass production.
In use: "That trench validates at 75:1 in the lab run, but the target foundry's production-tier capability is 40:1 — it won't hold at volume."
Misuse note: Generalists quote a single "the foundry's aspect ratio" figure, usually the best demonstrated (R&D) number, and layout-freeze against it. The number that matters is the number for the *production tier the part will actually ship on* — a feature that survives only at lab-scale capability isn't manufacturable yet, even though it etched fine in the qualification run.

**MPW (multi-project wafer) shuttle**
Definition: A scheduled foundry run where multiple customers' designs share a single maskset and wafer lot, splitting NRE cost across tenants in exchange for a fixed process offering and shared schedule.
In use: "Run the first prototype on the next MPW shuttle instead of a dedicated lot — it's the same process baseline for a fraction of the NRE."
Misuse note: Non-specialists treat "shuttle" as simply "the cheap option" without weighing the constraint it buys: a shuttle run locks you to the foundry's standard process offering. If the design needs any deviation from that standard process, the shuttle isn't actually available to you at any price — the choice isn't cost vs. no-cost, it's "does my design fit the standard process" first.

**NRE (non-recurring engineering)**
Definition: The one-time cost to set up a fabrication run — mask sets, process qualification, tooling — distinct from the marginal per-wafer or per-die cost that scales with volume.
In use: "The stop-geometry fix is a mask-layer revision on the existing baseline, so it's inside the current lot's NRE budget, not a new qualification."
Misuse note: Generalists use "NRE" loosely to mean "the expensive part" without distinguishing it from per-wafer cost, which matters when deciding whether a design change requires a full new dedicated-process qualification (new NRE) or fits within an existing baseline (per-wafer cost only). Conflating the two makes every re-spin look like the same size decision when they aren't.

**Stiction**
Definition: Adhesion between two microstructure surfaces in contact (or near-contact, via capillary/van der Waals/electrostatic forces) sufficient to prevent release under the device's normal restoring force.
In use: "The self-test failures present as stiction, but the root cause is geometric — the stop is past pull-in — not surface chemistry."
Misuse note: Used as if it names a single cause (usually assumed to be surface chemistry or humidity), when it's a description of an *outcome* that geometric (uncontrolled pull-in contact), chemical (surface energy, contamination), and environmental (moisture ingress) causes can all produce. Reaching for a hydrophobic coating before checking stop-geometry-vs-pull-in-margin is the textbook misdiagnosis this term invites.

**Hinge memory / creep**
Definition: Cumulative plastic deformation of a flexure or hinge under sustained, one-sided (asymmetric) actuation at operating temperature, producing a residual set that grows with duty cycle and thermal exposure — distinct from instantaneous mechanical overload.
In use: "Peak-voltage overload testing won't catch hinge memory — it only shows up under prolonged asymmetric drive, so model duty cycle and temperature explicitly."
Misuse note: Generalists fold this into generic "fatigue" or assume a part that passes overload/shock qualification is reliable for lifetime. Hinge memory is a slow, duty-cycle-and-temperature-driven mechanism that a peak-voltage-only test plan structurally cannot exercise — passing overload qual says nothing about it.

**Duty cycle (for reliability, not just power)**
Definition: In this domain, the fraction of time and the directional symmetry of actuation drive — not just an average power/on-time metric — because sustained one-sided drive is what produces hinge memory, while symmetric or intermittent drive at the same average duty cycle may not.
In use: "Flag the actuator for creep modeling because its duty cycle is asymmetric and sustained, not because the number is high."
Misuse note: Treated as a single scalar ("80% duty cycle") that can be compared across parts. What matters for creep risk is asymmetry and sustained direction, not just time-on — over-margining every high-duty-cycle actuator, including ones with a genuinely intermittent or symmetric drive profile, is a documented overcorrection failure mode in this role.

**Qualification (vs. verification)**
Definition: Qualification is passing a defined standard test (e.g., JEDEC JESD22-B104 shock, Method 1014 hermeticity) at its stated parameters; verification is confirming the part meets its actual design requirement, which the qualification test may or may not fully resolve.
In use: "It's qualified per Method 1014, but we still need to verify leak-tightness with a higher-resolution method before closing this out."
Misuse note: Used interchangeably in casual engineering conversation. The distinction is the entire point of flagging small-cavity hermeticity as a known gap — a part can be fully qualified (passed the named standard) while remaining unverified against the requirement that standard was supposed to stand in for.

**Process capability (tier-qualified, not single-valued)**
Definition: A foundry's demonstrated manufacturing performance (aspect ratio, layer thickness/count, minimum feature size, critical-dimension tolerance) stated per production tier — R&D, development, mass production — rather than as one number for "the process."
In use: "Check the layout against the foundry's mass-production process capability, not the demonstrated R&D capability."
Misuse note: Generalists ask "what's this foundry's process capability" expecting a single figure, then design against whichever number the sales deck or a best-case datasheet cell happens to show — usually the R&D-tier best case, which is the wrong number for a part intended to ship at volume.

**Overload stop (vs. pull-in limit)**
Definition: A designed mechanical feature that physically arrests structure overtravel at a chosen displacement — a deliberate design element, not a physics limit like pull-in, and its correctness depends entirely on where it's placed relative to the pull-in limit.
In use: "Move the overload stop to 0.6 µm, 25% margin below the 0.8 µm pull-in limit, so the stop — not electrostatic snap-down — always arrests overtravel."
Misuse note: Assumed to be inherently protective simply because it exists inside the physical gap. A stop placed *past* the pull-in limit provides no protection — the structure goes unstable and snaps to contact before ever reaching the stop, which is exactly the geometry defect in this role's worked failure analysis.
