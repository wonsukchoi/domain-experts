# Vocabulary

Terms generalists flatten together that a field environmental technician keeps sharply separate — the value is in the misuse, not the definition.

## Grab sample vs. composite sample

A **grab sample** is a single sample collected at one point in time, representing conditions only at that instant. A **composite sample** combines multiple aliquots collected over a period into one representative sample, required for parameters (BOD5, TSS) where a permit wants an average loading over time, not an instant.

**In use:** "pH has to be a grab, field-measured at the moment of collection — you can't composite a parameter that changes in the bottle."

**Common misuse:** treating a composite as automatically "more representative" and therefore always preferred — some parameters (pH, DO, residual chlorine) are specifically excluded from compositing because they change too fast for a composite to mean anything.

## Flow-proportional vs. time-proportional compositing

**Flow-proportional** compositing sizes each aliquot to the flow rate at the moment it's collected (more flow, bigger aliquot), so the composite reflects mass loading. **Time-proportional** compositing collects equal-volume aliquots at fixed time intervals regardless of flow, which is simpler but biases the composite toward whatever flow condition happened to occur most often during the sampling window.

**In use:** "The permit specifies flow-proportional — a flat time-paced sample from this stream would over-weight the low-flow overnight hours relative to the day-shift peak."

**Common misuse:** using the two terms interchangeably, or assuming any automated composite sampler is "flow-proportional" by default when many run in time-paced mode unless specifically programmed against a flow signal.

## Holding time vs. preservation

**Holding time** is the maximum elapsed time between collection and required analysis (or extraction). **Preservation** is the chemical (acid, base) or physical (cooling, freezing) treatment applied at collection to slow degradation during that window. A sample can be perfectly preserved and still invalid if it blows its holding time, and vice versa.

**In use:** "It's within the 28-day holding time, but the temperature blank came in at 12°C — the preservation failed even though the clock hasn't run out."

**Common misuse:** treating "held within time" and "properly preserved" as the same compliance check, when a lab or auditor checks both independently.

## Trip blank vs. field blank vs. equipment (rinsate) blank

A **trip blank** is lab-prepared reagent water that travels unopened with a VOC cooler, catching contamination from transport/storage. A **field blank** is reagent water opened and poured into a sample container at the site, catching ambient field contamination. An **equipment (rinsate) blank** is reagent water passed through decontaminated sampling equipment, catching contamination from the equipment itself.

**In use:** "The rinsate blank came back with a metals detect — recheck the decon procedure on the bailer before trusting any of today's metals results."

**Common misuse:** submitting only one blank type and treating it as covering all contamination sources — each blank type isolates a different point in the chain, and they aren't substitutes for each other.

## RPD (Relative Percent Difference)

The percent difference between two paired results (a field or lab duplicate pair), calculated as |result1 − result2| / ((result1 + result2)/2) × 100. It's the standard precision metric for duplicate pairs; a high RPD means the sampling or analytical process isn't reproducible for that batch, not that one of the two values is "the wrong one."

**In use:** "RPD on the duplicate pair came out at 34% against a 20% control limit — flag the batch's precision as out of control, don't just average the two numbers and move on."

**Common misuse:** averaging a duplicate pair into a single reported value without checking RPD against the control limit first, which hides a precision problem instead of flagging it.

## MDL vs. RL (Method Detection Limit vs. Reporting Limit)

The **MDL** is the statistically derived lowest concentration a method can distinguish from zero with confidence, per 40 CFR Part 136 Appendix B. The **RL** (or PQL, practical quantitation limit) is a higher, lab-chosen value above the MDL where the lab is confident in quantifying accurately, and it's the number actually used for compliance reporting.

**In use:** "It detected above the MDL but below the RL — report it as estimated/qualified, not as a clean quantified value."

**Common misuse:** treating "detected" (above MDL) and "quantified" (above RL) as the same thing, or treating a non-detect below the RL as proof of zero concentration rather than "below what this method can reliably measure."

## QAPP (Quality Assurance Project Plan)

The project-specific document that sets data quality objectives, sampling methods, QC acceptance criteria (calibration tolerances, RPD limits, blank criteria), and corrective-action procedures for a given monitoring program. It is the actual source of most numeric acceptance criteria a technician applies in the field — not a generic EPA number.

**In use:** "Don't cite '±0.1 SU' as an EPA rule — it's this project's QAPP-stated pH post-check tolerance; a different project's QAPP might set it differently."

**Common misuse:** citing a QC acceptance criterion as if it were a universal federal standard, when most (RPD limits, calibration tolerance bands, blank action levels) are QAPP-specific and vary project to project.

## Split sample

A single, homogenized sample physically divided into two or more separate containers submitted to different labs (or the same lab under different sample IDs) to check inter-laboratory or method agreement — distinct from a duplicate, which is two separately collected samples from the source.

**In use:** "Regulator wants a split on this one — pour and homogenize on site, then divide into both labs' containers from the same batch."

**Common misuse:** confusing a split sample (one collection, divided) with a duplicate (two separate collections), which measures a different source of variability (analytical/inter-lab vs. total sampling-plus-analytical).

## Isokinetic sampling

A stack-testing sampling condition where the velocity of gas drawn into the sample nozzle matches the surrounding stack gas velocity, so entrained particulate isn't biased toward or away from the sample by inertial effects. Checked after the run via the isokinetic ratio (%I), not assumed during setup.

**In use:** "Run 2 came back at 87% isokinetic — outside the 90-110% window, so it's invalid and has to be repeated, not just noted as a minor deviation."

**Common misuse:** treating isokinetic sampling as a setup condition that's either achieved or not achieved by nozzle selection alone, when it's a calculated, post-run result that depends on the actual stack conditions encountered during the run.

## As-collected vs. as-received (chain of custody context)

**As-collected** describes the sample's condition and any field observations at the moment of sampling (recorded by the technician). **As-received** describes its condition at the lab's login desk (recorded by the lab). Discrepancies between the two — a broken seal, a temperature excursion, a missing bottle — are exactly what the chain of custody exists to catch.

**In use:** "As-collected, the cooler was iced and sealed at 14:20; as-received the seal was intact but the temp blank read 9°C — that gap is a transport issue, not a collection issue."

**Common misuse:** treating the chain of custody as a formality/signature log rather than the record that pinpoints which leg of the process (field, transport, or receiving) a QC exception occurred on.
