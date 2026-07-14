# Vocabulary

### SPC control limits
Statistically derived boundaries (commonly ±3-sigma from the process mean) that flag when a process is drifting, set narrower than the wider spec (customer/product) limits.
**In use:** "Control limits are 485-515 on this step — tighter than our 475-525 spec, so we catch drift before it ever threatens spec."
**Common misuse:** Treating "inside spec" and "in control" as the same condition — a process can be in spec while trending out of control, and the whole point of control limits is to catch that before spec is threatened.

### Western Electric rules
A standard set of run-rule criteria (originating from the Western Electric Statistical Quality Control Handbook) for detecting non-random patterns in control-chart data — e.g., 1 point beyond 3-sigma, 2 of 3 beyond 2-sigma same side, 8 consecutive points same side of centerline.
**In use:** "That's an 8-point run above centerline — a Western Electric rule violation, not just a high reading."
**Common misuse:** Only checking the most recent point against the control limit and ignoring the broader trend — most Western Electric rules are about the pattern across several consecutive points, not any single value.

### Chamber seasoning
The gradual change in a process chamber's behavior as its interior surfaces and consumables accumulate deposition/etch byproducts over hours of use, which shifts process results predictably within a characterized window.
**In use:** "This drift matches known seasoning behavior at 480 RF-hours — not a new fault, just approaching the reseasoning point."
**Common misuse:** Treating any gradual drift as automatically "just seasoning" without checking it against the chamber's actual characterized hours and qualified window — an unexplained drift outside the known seasoning pattern needs its own investigation.

### Tool matching
The qualification process confirming that two nominally identical tools (or chambers) produce statistically equivalent results on the same recipe, verified with test data rather than assumed from identical hardware specifications.
**In use:** "These two etchers were matched at qual, but that was six months ago — let's pull current data before assuming they're still aligned."
**Common misuse:** Assuming tool matching is a permanent, one-time qualification — consumable wear and seasoning diverge over time even between originally matched tools, so matching needs periodic reverification.

### Qualified process window
The range of parameter values (temperature, pressure, RF power, time, gas flow) validated during process qualification as producing acceptable, characterized results — distinct from the wider range a tool is physically capable of running.
**In use:** "We can push etch time up, but only within the qualified window — past that, we're in unvalidated territory."
**Common misuse:** Assuming any parameter change that "should" work based on general process knowledge is safe to run on production material — only changes validated within the qualified window have confirmed downstream effects.

### Lot hold
A status placed on a wafer lot in the MES that prevents it from advancing to its next process step pending investigation or disposition.
**In use:** "Lot's on hold at etch — don't let it go to strip until engineering signs off on the disposition."
**Common misuse:** Treating a hold as equivalent to a stop of all activity on the lot — a held lot still has a queue-time clock running, and holding it too long can itself create a new problem (material degradation) even while the original issue is unresolved.

### Queue time
The maximum allowable elapsed time a lot can sit between two process steps before material degradation (moisture uptake, native oxide growth, resist relaxation) risks the process result, specific to each step.
**In use:** "We've got four hours left on queue time for this lot before oxide growth becomes a concern — the hold decision needs to happen before then."
**Common misuse:** Treating queue time as a soft guideline rather than a hard constraint tied to a specific physical/chemical degradation mechanism — exceeding it can invalidate the lot regardless of how the original metrology issue resolves.

### Split-lot / first-wafer testing
Sampling a subset of wafers (or the first wafer) from a lot for metrology before committing the full lot to the same process conditions.
**In use:** "First-wafer came back clean, releasing the rest of the lot to the same recipe."
**Common misuse:** Treating a clean first-wafer result as a guarantee for the rest of the lot — first-wafer testing catches a gross process error at the start, but a drift developing over the course of the run (seasoning, consumable depletion) can still affect later wafers in the same lot.

### Disposition
The documented decision made on a held or nonconforming lot — release, rework, or scrap — recorded in the lot's history before it's allowed to proceed.
**In use:** "Disposition on lot 4471 is release — trend's explained by known seasoning behavior, all points in spec and in control."
**Common misuse:** Clearing a hold informally (moving the lot forward) without a recorded disposition — the MES history's value depends on the disposition being logged at the time the decision is made, not reconstructed afterward.

### MES (Manufacturing Execution System)
The software system tracking a lot's status, location, process history, and hold/release state through the fab, serving as the authoritative traceability record.
**In use:** "Check the MES before you touch that lot — it shows a hold flag from second shift that hasn't been cleared."
**Common misuse:** Relying on a verbal handoff instead of checking the MES record directly — a hold or flag that wasn't verbally communicated but exists in the MES is still binding, and skipping the system check is how a hold gets missed.
