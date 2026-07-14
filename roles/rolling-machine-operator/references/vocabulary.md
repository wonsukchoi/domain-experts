# Vocabulary

### Roll crown (camber)
A deliberate curvature built into a rolling mill's rolls, designed to counteract the roll's own deflection under load, keeping the gap effectively uniform across the material's width during rolling.
**In use:** "Crown's set for a narrower job than this one — that's why we're getting a thick center on this wider strip."
**Common misuse:** Assuming a single crown setting works correctly across any width or load — crown is calculated to counteract deflection at a specific combination of load and width, and using it outside that combination produces an uneven thickness profile.

### Cumulative reduction
The total percentage reduction in thickness a material has undergone across multiple rolling passes since its last anneal (or since starting stock), used to track approach toward a work-hardening-driven anneal trigger.
**In use:** "We're at 29% cumulative since the last anneal — getting close to the 35-40% trigger where we need to anneal before continuing."
**Common misuse:** Tracking only per-pass reduction percentage without tracking the cumulative total — a per-pass percentage that was safe early in a schedule can become unsafe later, precisely because cumulative reduction (and the resulting work hardening) has been building across passes.

### Work hardening (cold rolling)
The progressive increase in a metal's hardness and decrease in its ductility caused by cold plastic deformation, accumulating with each rolling pass until relieved by an anneal.
**In use:** "This coil's work-hardened enough after two passes that the same eighteen percent reduction that was fine on pass one would crack it now."
**Common misuse:** Treating each rolling pass as if the material starts in the same condition as the original stock — work hardening accumulates, meaning the material's actual capacity to tolerate further reduction decreases with each pass, even without any change to the rolling process itself.

### Intermediate anneal
A heat treatment step performed between rolling passes to relieve accumulated work hardening and restore ductility, allowing further cold rolling reduction to proceed safely.
**In use:** "Scheduling the anneal before pass three, not after we see cracking — cumulative reduction's already telling us we need it."
**Common misuse:** Scheduling an anneal reactively, after a defect (like edge cracking) has already appeared, rather than proactively at the material's specified cumulative reduction trigger point — by the time cracking appears, material may already be compromised.

### Edge cracking
A defect where the edges of rolled material develop cracks or tears, typically caused by exceeding the material's capacity to deform in a given pass, especially when combined with accumulated work hardening.
**In use:** "Edge cracking on pass three, not one or two — that's the work-hardening signature, not a sudden material defect."
**Common misuse:** Assuming edge cracking always indicates a material quality problem — it's frequently a process signature of exceeding the material's actual (work-hardening-adjusted) reduction capacity for that specific pass, which is a schedule issue rather than a material defect.

### Inter-stand tension
The tension (or compression) in material as it passes between consecutive stands in a multi-stand rolling mill, determined by the relative speed matching between those stands.
**In use:** "Speed mismatch between stands two and three is creating excess tension — that's what's necking the strip there."
**Common misuse:** Adjusting a single stand's speed to address a local issue without checking its effect on tension to the adjacent stands — stand speeds function as a coordinated system, and a change at one point ripples to its neighbors.

### Pass schedule
The planned sequence of rolling passes, including reduction per pass, cumulative reduction tracking, and any scheduled intermediate anneals, designed to reach a target final thickness without exceeding the material's capacity at any point.
**In use:** "Pass schedule calls for an anneal after pass two on this material — that's not optional scheduling flexibility, it's built around the work-hardening curve."
**Common misuse:** Treating the pass schedule as a rough guideline that can be compressed or reordered for convenience — the schedule is built around the material's actual, cumulative-reduction-dependent capacity, and deviating from it risks defects the schedule was specifically designed to avoid.

### Thickness profile (across width)
The measured thickness of rolled material at multiple points across its width, used to detect crown-mismatch-driven unevenness that a single-point measurement would miss.
**In use:** "Profile's showing thick in the center, thin at the edges — that's an under-crowned condition for this load."
**Common misuse:** Relying on a single center-point (or any single-point) thickness measurement to confirm the material meets spec — crown mismatch specifically produces a variation across width, invisible to a check that only samples one location.

### Roll gap
The physical distance between a rolling mill's work rolls, set to achieve a target reduction, though actual output thickness also depends on roll deflection under the specific load being rolled.
**In use:** "Gap's set the same as last time, but the load's different this run — checking actual output thickness rather than assuming the gap alone determines it."
**Common misuse:** Treating roll gap setting as a direct, one-to-one determinant of output thickness regardless of load — roll deflection under different rolling forces changes the actual effective gap, meaning the same nominal gap setting can produce different output thickness under different conditions.

### Hardness testing (rolling verification)
A measurement used to verify a rolled material's actual work-hardened state or confirm an anneal successfully restored ductility, providing objective data beyond assuming a process step achieved its intended effect.
**In use:** "Confirming the anneal actually worked with a hardness check before we resume rolling — not just assuming the furnace cycle did its job."
**Common misuse:** Assuming a completed anneal furnace cycle automatically means the material's ductility was restored — actual material hardness/ductility should be verified, since a furnace cycle that ran but didn't achieve the correct temperature/time still shows as "complete" without confirming the underlying material property change.
