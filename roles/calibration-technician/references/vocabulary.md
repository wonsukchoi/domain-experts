# Vocabulary

Terms generalists flatten together that a calibration technologist keeps sharply separate — the value is in the misuse, not the definition.

## Accuracy vs. precision vs. uncertainty

**Accuracy** is closeness of a measured value to the true value — usually unknowable exactly, only bounded. **Precision** is closeness of repeated measurements to each other (repeatability), independent of whether they're close to the truth. **Uncertainty** is the quantified, stated parameter (a number, with a coverage factor) that bounds where the true value probably lies, combining both effects.

**In use:** "The gauge is precise — tight repeatability, s = 0.01 psi — but it reads 2 psi high every time, so precision doesn't buy you accuracy without the offset being corrected or budgeted."

**Common misuse:** using "accuracy" and "precision" interchangeably, or citing a precision (repeatability) figure as if it were the full measurement uncertainty, which omits every Type B contributor.

## Calibration vs. adjustment vs. verification

**Calibration** is the comparison of a UUT against a reference standard and the recording of the result — it does not, by itself, change the instrument. **Adjustment** is a physical or firmware change made to bring the instrument's indication closer to the reference value, performed only if calibration shows it's needed (and permitted). **Verification** is a check that an instrument is still within tolerance, sometimes with fewer test points or less rigor than a full calibration, often used between full calibrations.

**In use:** "As-found failed, so we adjusted the zero and span, then re-ran the calibration as-left — don't report the adjustment step as if it were the calibration itself."

**Common misuse:** using "calibrate" to mean "adjust," which hides whether the instrument was actually out of tolerance before the adjustment — the as-found record is what tells you that, and it must be reported separately from as-left.

## Type A vs. Type B uncertainty

**Type A** uncertainty is evaluated by statistical analysis of a series of repeated observations (a standard deviation of readings). **Type B** uncertainty is evaluated by any other means — certificates, specifications, resolution limits, published data — combined with an assumed probability distribution. The classification is about *method*, not about which is more trustworthy or "real."

**In use:** "Repeatability gave us the Type A term; the reference cert's stated uncertainty, the resolution, and the drift history are all Type B — none of them come from repeat readings, but they're just as real a contributor to the budget."

**Common misuse:** treating Type B terms as optional or as "estimates" that can be skipped when the budget is tight on time, when a budget missing significant Type B terms is understated regardless of how solid the Type A term is.

## Standard uncertainty vs. expanded uncertainty vs. coverage factor (k)

**Standard uncertainty (u)** is roughly a one-standard-deviation-equivalent value. **Expanded uncertainty (U)** is the standard uncertainty multiplied by a **coverage factor (k)** — commonly k=2, corresponding to roughly 95% confidence for a normal distribution — to give an interval more useful for reporting a pass/fail decision. A certificate's stated uncertainty is almost always the expanded value with its k stated alongside.

**In use:** "The cert says ±50 µV at k=2 — that's the expanded uncertainty, so the standard uncertainty going into our budget is 50/2 = 25 µV, not 50 µV."

**Common misuse:** pulling a certificate's expanded uncertainty straight into a combined-uncertainty root-sum-square calculation without dividing by k first, which double-counts the coverage factor once the new combined value is expanded again.

## TUR (Test Uncertainty Ratio) vs. TAR (Test Accuracy Ratio)

**TUR** is the UUT's tolerance divided by the measurement uncertainty (properly, the full expanded uncertainty of the calibration process) used to test it. **TAR** is an older, cruder version — UUT tolerance divided by the reference standard's accuracy specification alone, with no formal uncertainty analysis behind it. Z540.3 and modern accredited practice specify TUR; TAR is a legacy shorthand that undercounts real contributors.

**In use:** "That 10:1 number in the old procedure is a TAR from the manufacturer spec sheets — recompute it as a proper TUR with an actual uncertainty budget before using it to justify the reference standard choice."

**Common misuse:** citing a TAR figure as if it were a TUR, which is often optimistic because it omits resolution, drift, environmental, and repeatability contributors that a real uncertainty budget would catch.

## Guard banding

A deliberate narrowing (or occasionally widening) of the acceptance limits used for the pass/fail decision, inward from the nominal tolerance by an amount related to the measurement uncertainty, applied when the TUR is too low to trust a straight comparison against nominal tolerance.

**In use:** "TUR came in at 3.2:1 on this one, below our 4:1 default — guard-band the limits by the expanded uncertainty before calling it, per procedure."

**Common misuse:** applying guard banding uniformly regardless of TUR (over-applying it even at high TUR, generating unnecessary false rejects), or never applying it at all regardless of policy (under-applying it, hiding a genuinely uncertain call behind a clean-looking PASS).

## As-found vs. as-left

**As-found** is the instrument's condition and reading(s) exactly as received, before any adjustment. **As-left** is the condition and reading(s) after any adjustment made during the calibration. Both must be recorded separately — as-found is what actually happened in the field before this calibration; as-left is what the instrument will do until the next one.

**In use:** "As-found was 0.6% out of tolerance — that's the number that drives the impact assessment on data collected before today, regardless of what as-left shows after we adjusted it."

**Common misuse:** reporting only the as-left (post-adjustment) result on a certificate when the instrument failed as-found, which hides that an out-of-tolerance condition existed in the field and should trigger a usage-impact review.

## CMC (Calibration and Measurement Capability)

The best measurement uncertainty a lab can demonstrate and defend for a given parameter, range, and method, as stated in its ISO/IEC 17025 accreditation scope — a lab cannot claim traceable calibration at an uncertainty better than its accredited CMC for that parameter, even if a particular job's numbers look better on paper.

**In use:** "Our CMC for DC volts at 10 V is ±40 µV — if the customer needs a calibration with a stated uncertainty tighter than that, we don't have the scope to issue it, full stop."

**Common misuse:** assuming any reference standard on the bench automatically extends the lab's claimable CMC, when CMC is a formally assessed and published capability, not just whatever the best equipment on hand happens to measure that day.

## Traceability

A documented, unbroken chain of calibrations, each with a stated uncertainty, connecting a measurement back to a realization of the SI unit (via a national metrology institute like NIST, or a CIPM MRA signatory) — not merely possessing a calibration sticker or a certificate with no stated uncertainty.

**In use:** "That gauge block set has a sticker but no certificate with a stated uncertainty on file — it's not traceable as things stand, regardless of how it was labeled."

**Common misuse:** treating "has a calibration sticker" as synonymous with "is traceable," when traceability requires the documented uncertainty chain, not just evidence that a calibration event happened at some point.

## Calibration interval — Method A1 vs. Method A3 (NCSL RP-1)

**Method A1** sets or adjusts an interval by engineering judgment, review, and simple statistics when history is thin. **Method A3** adjusts an interval algorithmically from a population's accumulated in-tolerance/out-of-tolerance ratio against a target reliability, once enough history exists to trust the statistic. Applying A3 to a population with only 2-3 history points produces a statistically unstable adjustment.

**In use:** "We've only got 4 cycles of history on this new instrument model — hold the interval by Method A1 judgment until we have enough cycles for a real A3 adjustment."

**Common misuse:** running a Method A3-style calculation on a small sample and treating the resulting number as authoritative, when RP-1 itself expects a minimum population/history size before the statistic is trustworthy.

## Out-of-tolerance (OOT) vs. nonconforming

An **OOT** finding means the instrument's as-found reading fell outside its stated tolerance at calibration — a metrology fact about the instrument. **Nonconforming** (in the quality-system sense) is a broader determination about whether product, test data, or a process is affected by that OOT condition, which requires an impact assessment beyond the calibration record itself.

**In use:** "The gauge is OOT as-found — that's confirmed. Whether any lots tested with it in the last interval are nonconforming is a separate call for quality engineering, not something the calibration record alone answers."

**Common misuse:** treating an OOT finding and a full nonconformance/impact determination as the same event, when the calibration lab's job ends at reporting the OOT accurately — the downstream impact assessment is a separate, often cross-functional, process.
