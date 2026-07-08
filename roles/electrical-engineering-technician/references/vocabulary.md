# Vocabulary

Terms generalists flatten together that a bench test/debug technologist keeps sharply separate — the value is in the misuse, not the definition.

## DUT / UUT (Device Under Test / Unit Under Test)

The specific physical item currently being tested or debugged, as distinct from "the design" or "the product line" in general. A DUT can fail while every other unit of the same design passes — the fault is in this instance, not necessarily in the design.

**In use:** "The DUT failed load regulation, but we haven't shown that's a design issue yet — pull two more units off the same lot before escalating to the design engineer."

**Common misuse:** treating a single DUT's failure as proof of a design flaw (or, in the opposite direction, dismissing a repeatable DUT failure as "just this unit" without checking a second sample).

## Rise time vs. bandwidth (oscilloscope)

**Rise time** is the time for a signal to transition between two amplitude thresholds (commonly 10%-90%). **Bandwidth** is the frequency at which the scope's measured amplitude of a sine wave rolls off by 3 dB. The two are linked by the approximation BW ≈ 0.35/T_rise (T_rise in the scope's own response) — they are not independent specs to be read off a datasheet separately and reasoned about separately.

**In use:** "This is rated 200 MHz, so its own rise time is about 0.35/200MHz = 1.75 ns — that's the number to combine with the signal's real rise time before trusting anything faster than a few nanoseconds."

**Common misuse:** reading a scope's bandwidth number as a pass/fail gate ("200 MHz is plenty for a 100 MHz signal") without computing the actual rise-time contribution and combined measurement error for the specific edge being characterized.

## Ground vs. return vs. chassis ground

**Ground** in a schematic is a reference node, not a guaranteed zero-ohm, zero-voltage physical point. **Return** is the specific current path back to the source for a given signal or rail — on a multi-layer board, different nets can have physically different return paths even if they're drawn to the same schematic "GND" symbol. **Chassis ground** is a mechanical/safety reference, often deliberately isolated from signal ground by design (single-point or capacitive coupling).

**In use:** "The scope probe's ground clip landed on chassis ground, not this rail's return — that's why the noise floor looked 40 mV higher than it should."

**Common misuse:** clipping a probe ground to whatever metal is convenient, assuming all "grounds" on a board are the same electrical node.

## Kelvin (4-wire) sensing vs. 2-wire measurement

**2-wire** measurement uses the same pair of leads to source current and sense voltage, so lead and contact resistance add directly to the reading. **4-wire (Kelvin)** measurement uses separate current-source and voltage-sense leads, so the sense leads carry negligible current and lead resistance drops out of the reading.

**In use:** "We're hunting a 0.4 Ω joint — 2-wire leads alone can contribute 0.05-0.1 Ω of error, so this one gets Kelvin-sensed."

**Common misuse:** using 2-wire measurement for sub-ohm resistance hunts and treating the reading as precise, when the lead/contact resistance can be a large fraction of the value being measured.

## Root cause vs. corrective action vs. containment

**Root cause** is the specific physical mechanism that produced the failure. **Containment** is the immediate action that stops the specific failing unit(s) from causing further harm (quarantine, rework, scrap). **Corrective action** is the process change that prevents recurrence across future units — it requires the root cause to be known, not just the symptom.

**In use:** "Containment is done — the lot is quarantined. Root cause is the via/joint defect from the reflow profile drift. Corrective action is the profile fix plus a first-article recheck on the next lot."

**Common misuse:** calling a containment step ("we reworked the failed units") a corrective action, when nothing has changed about the process that produced the defect in the first place.

## NFF (No Fault Found)

A disposition stating that a unit returned as failed could not be made to reproduce the reported failure under the test conditions applied. It is a statement about the test's coverage, not proof the unit is defect-free — a high NFF rate on a given fault report usually means the test conditions don't capture the field trigger condition, not that field reports are wrong.

**In use:** "NFF rate on this failure mode is running 30% across the last quarter — that's a test-coverage problem, not 30% of customers imagining a defect."

**Common misuse:** treating NFF as equivalent to "unit is good," closing the loop with no attempt to widen trigger/environmental conditions to actually search for the fault (SKILL.md First-principles core #5).

## Latent defect vs. patent (obvious) defect

A **patent defect** is immediately observable — the unit fails functional test outright. A **latent defect** exists but doesn't yet produce an observable failure; it may develop into one under stress (thermal cycling, vibration, further ESD exposure) after the unit has already shipped or passed inspection.

**In use:** "It passed functional test clean, but the ESD-handling gap on intake means we can't rule out a latent defect that shows up after a few thermal cycles."

**Common misuse:** treating "passed test" as equivalent to "no defect present," when a latent defect is by definition one that current testing doesn't catch.

## IPC-A-610 Class 1 / 2 / 3

The acceptance-criteria tier a build is held to for solder joints and assembly conditions. **Class 1** (general consumer) tolerates cosmetic imperfections that don't affect function. **Class 2** (dedicated service) requires higher reliability appearance and cosmetic standards. **Class 3** (high-reliability, e.g., life-support or mission-critical) has the tightest acceptance criteria, rejecting conditions Class 1/2 would pass.

**In use:** "This is a Class 2 build — that fillet height is acceptable at Class 2 even though it would get flagged at Class 3."

**Common misuse:** applying one class's criteria to a build contracted at a different class, or citing "IPC standard" without specifying which class governs this build.

## Golden unit (reference/known-good board)

A specific unit verified against the full spec and set aside as the comparison baseline for troubleshooting other units of the same design — used to get real, measured "expected" values at every test node instead of relying only on the schematic's nominal/ideal values.

**In use:** "Nominal says 3.30 V at that node, but the golden unit reads 3.28 V under the same load — use the golden unit's number as the real baseline, not the schematic's rounded nominal."

**Common misuse:** treating the schematic's nominal value as the expected value at every node, when component tolerance and board-specific effects mean the golden unit's actual measured value is the more reliable comparison baseline.

## ICT (in-circuit test) vs. FCT (functional test)

**ICT** uses a bed-of-nails fixture to probe individual components and nets directly, checking for shorts, opens, and component values in isolation from the rest of the circuit's operation. **FCT** powers the board and exercises it through its actual operating modes, checking system-level behavior. A board can pass ICT (every component measures correctly in isolation) and still fail FCT (the components don't work correctly together), or vice versa for defects ICT's fixture can't reach.

**In use:** "It passed ICT clean — every net and component checked — so the FCT failure is an interaction or timing issue, not a populated-wrong-part or solder-short problem."

**Common misuse:** treating ICT pass as equivalent to "board is functionally good," skipping or deprioritizing FCT coverage that catches a different class of defect.

## ESD models — HBM / CDM / MM

Standardized ESD stress models used to characterize a component's or assembly's susceptibility. **HBM (Human Body Model)** simulates a charged person touching a device. **CDM (Charged Device Model)** simulates the device itself being charged (e.g., by sliding across a surface) and then discharging through a pin to ground. **MM (Machine Model)** simulates a charged machine or tool contacting the device. A device can be robust against one model and fragile against another — they are not interchangeable proxies for "ESD-safe."

**In use:** "This part's HBM rating is 2 kV, but its CDM rating is only 250 V — the automated pick-and-place handling on the line is a CDM-relevant exposure, so the CDM number is the one that matters here, not HBM."

**Common misuse:** citing a single ESD kV rating as if it covers all exposure modes, when a device's HBM, CDM, and MM susceptibility are measured separately and can differ by an order of magnitude.
