# Vocabulary

Terms of art a biologist uses precisely and a generalist routinely misuses — not terms a dictionary fixes, but terms whose everyday meaning is close enough to the technical one to feel safe while being wrong in a way that breaks the analysis.

**Experimental unit**
The smallest entity that could have been independently assigned to a different treatment. Set by where randomization happened, not by where a measurement was taken.
*In use:* "The experimental unit here is the cage — treatment was assigned cage by cage, not animal by animal."
*Misuse:* Generalists use it interchangeably with "sample" or "data point," so "50 measurements" gets called "50 experimental units" even when those measurements came from 5 independently-treated litters.

**Pseudoreplication**
Analyzing non-independent observations (repeat measures on one subject, multiple subjects from one treated cluster) as if each were an independent data point, inflating N and understating the true variance.
*In use:* "Five weighings per pup times two pups per litter isn't 10 independent points — that's pseudoreplication on top of pseudoreplication."
*Misuse:* Treated as a synonym for "small sample size" or "sloppy data collection." It's specifically a unit-of-analysis error — the sample can be large and still be entirely pseudoreplicated.

**Power (statistical power)**
The probability that a study design will detect a true effect of a specified size, given the sample size, variance, and significance threshold — computed before data collection, not diagnosed from the outcome.
*In use:* "At N=5 dams/arm we're sitting at ~24% power for d=0.8 — that's not evidence of no effect, it's an underpowered design."
*Misuse:* Used loosely as "how big is my dataset" or invoked post hoc ("the result wasn't powerful") to describe effect size rather than the pre-specified detection probability of the design.

**Effect size**
A standardized, unit-free measure of the magnitude of a difference or relationship (e.g., Cohen's d), stated independently of whether it reached significance — the number a power calculation is built from.
*In use:* "We're powering the study around d = 0.8, based on the pilot data and the smallest effect that would be biologically meaningful."
*Misuse:* Conflated with the p-value or with "how significant" a result was. A tiny, biologically meaningless effect can hit p<0.05 with enough N, and a huge effect can miss significance with too little.

**Achieved power**
The power actually delivered by the study as run (given its actual N and variance), reported explicitly when a study falls short of its target — distinct from a design's a priori power target.
*In use:* "We couldn't hit 26 dams/arm, so the memo states achieved power of ~45% at N=12, rather than just reporting 'not significant.'"
*Misuse:* Skipped entirely — generalists report a non-significant result as "no effect" without ever computing or disclosing what the design was actually capable of detecting.

**Mixed-effects model**
A statistical model that includes both fixed effects (the treatment of interest) and random effects (the clustering variable — litter, cage, site) so that the clustering, not the raw observation count, correctly sets the degrees of freedom.
*In use:* "Analyze it as a mixed-effects model with litter as the random effect, not a t-test on the 50 pooled pup weights."
*Misuse:* Treated as an optional refinement or "fancier statistics" rather than the structurally correct analysis whenever data has a nested/clustered origin — using a standard t-test on clustered data isn't a simpler equivalent, it's a wrong model.

**IACUC protocol**
A formal, committee-approved document specifying species, procedures, numbers, and endpoints for animal work, required before any covered work — including pilot or "just looking" work — begins.
*In use:* "We can't touch the animals until the amended IACUC protocol clears — that includes the pilot cohort."
*Misuse:* Treated as paperwork that can run in parallel with early bench work ("we'll get the protocol updated while we start the pilot"). Data collected under an unapproved or lapsed protocol is typically unusable regardless of quality, and IACUC approval is a hard gate, not a formality tracked alongside the work.

**IBC (Institutional Biosafety Committee) review**
Committee review and clearance required for work with recombinant/synthetic nucleic acids or elevated-biosafety organisms, separate from and in addition to IACUC.
*In use:* "This construct triggers IBC review on top of IACUC — both have to clear before the first injection."
*Misuse:* Assumed to be the same gate as IACUC, or assumed unnecessary because "it's just a standard plasmid" — biosafety level, not novelty of the reagent, is what determines whether IBC review applies.

**Biosafety level (BSL)**
A four-tier containment and practice classification (BSL-1 to BSL-4) assigned to an organism or agent based on its hazard, dictating the physical containment and procedural requirements for work with it — not a measure of how "dangerous" the science is subjectively.
*In use:* "The recombinant construct pushes this from BSL-1 to BSL-2 — that changes the containment requirements, not just the paperwork."
*Misuse:* Used as a vague severity adjective ("that's pretty high biosafety") rather than the specific tier that determines concrete, checkable containment requirements (ventilation, PPE, waste handling).

**Closure (in mark-recapture / population studies)**
The assumption that a population is closed — no births, deaths, immigration, or emigration — during the sampling period, required for standard mark-recapture estimators to be valid.
*In use:* "The three-week trapping window is short enough to defend closure — a full season would violate it."
*Misuse:* Confused with "the study is finished" or "the dataset is closed." It's a testable statistical assumption about the population during data collection, and violating it (open population during a long sampling window) silently biases abundance estimates rather than just adding noise.

**3Rs (Replacement, Reduction, Refinement)**
The operating ethical framework for animal research: replace animal models where possible, reduce the number of animals used to the minimum consistent with valid results, and refine procedures to minimize suffering.
*In use:* "Reduction means shrinking variance with better controls so the same power is reached with fewer animals — not choosing N=5 because it's cheaper."
*Misuse:* "Reduction" gets invoked to justify a sample size that was actually set by budget or schedule, when the framework's actual requirement is that N still be adequate for valid, powered results — reduction is a design outcome, not a shortcut to a smaller number.

**Blinding**
Concealing treatment-group assignment from whoever collects or scores the outcome measurement, to prevent (often unconscious) bias in how data is recorded.
*In use:* "The technician scoring tumor size doesn't know which animals got drug vs. vehicle — that's the blinding."
*Misuse:* Conflated with randomization ("we randomized, so it's blinded") or treated as unnecessary for "objective" measures like a body-weight scale reading — automated or numeric measurement doesn't eliminate the bias blinding is meant to control (e.g., in how borderline cases get classified or excluded).

**Replication (independent replication)**
An independently conducted study, ideally in a different lab with different reagents/animals/operators, that reproduces the original finding — distinct from running technical replicates or repeating the analysis on the same dataset.
*In use:* "It's a striking result, but it's one lab, one cohort — we're treating it as a hypothesis until it's independently replicated."
*Misuse:* Conflated with "repeating the experiment" in the same lab with the same materials, or with re-running the statistics on the same raw data — neither addresses the actual risk (a lab- or cohort-specific artifact) that independent replication is meant to catch.

**Collecting permit (federal vs. state)**
Legal authorization to take, handle, or transport wildlife or protected specimens, issued in a specific sequence — federal authorization (e.g., USFWS) generally must be in hand before a state scientific-collector permit can be issued.
*In use:* "The state won't even process our application without the federal permit number already on file — that's the actual critical path, not the state paperwork."
*Misuse:* Treated as a single generic "permit" to request whenever convenient, or assumed the state and federal applications can be submitted in parallel — the sequencing dependency (federal first) is the part that trips up a timeline, not the existence of the requirement itself.
