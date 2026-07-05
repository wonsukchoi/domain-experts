# Site civil engineering working vocabulary

Terms a site/civil PE uses daily and precisely. Format: definition → how a practitioner says it → common misuse.

**Time of concentration (tc)** — The time for runoff to travel from the hydraulically most distant point in a drainage area to the point of analysis, summed across sheet flow, shallow concentrated flow, and channel/pipe flow segments.
**In use:** "Post-development tc dropped from 20 to 10 minutes once we piped that reach — that's what's driving the higher peak intensity, not just the imperviousness."
**Misuse:** reusing the pre-development tc for post-development conditions because it's "close enough." Conveyance path changes (curb/gutter, storm pipe) shorten tc materially and increase design rainfall intensity — skipping the recalculation understates peak flow.

**Curve Number (CN)** — The NRCS/SCS parameter (30–98) representing a soil-cover complex's runoff potential, used with the curve-number method (as opposed to the rational method) to estimate runoff depth from rainfall.
**In use:** "CN went from 61 (open space, good condition, HSG B) to 92 (impervious, HSG B) once we added the parking lot — that's the real driver of the runoff volume increase, not just C."
**Misuse:** treating CN and the rational method's C coefficient as interchangeable inputs to the same formula — they belong to different methods (curve-number/SCS vs. rational) with different theoretical bases and aren't substitutable term-for-term.

**Rational method coefficient (C)** — An empirical runoff coefficient (0–1) representing the fraction of rainfall that becomes runoff for a given land cover, used in Q=CiA.
**In use:** "Composite C for the site is 0.85 — weighted 70% roof/pavement at 0.95 and 30% landscape at 0.25."
**Misuse:** applying a single C value uniformly to a site with mixed land cover without area-weighting it, or using the rational method at all on a drainage area well beyond its ~200-acre applicability limit.

**Allowable bearing pressure vs. ultimate bearing capacity** — Ultimate capacity (qult) is the soil's theoretical failure pressure; allowable (qa) is qult divided by the geotechnical report's stated factor of safety, meant to be compared directly against actual applied pressure.
**In use:** "qa is 2,500 psf — that already has the report's 3.0 FS baked in, so we compare actual load straight against it."
**Misuse:** dividing the allowable value by an additional factor of safety ("just to be safe"), which silently produces an oversized, uneconomical foundation with no one aware an extra margin was stacked on.

**Factor of safety (FS), geotechnical context** — The ratio of ultimate capacity to the value actually relied on in design; for foundation bearing, conventionally 2.5–3.0 depending on soil variability and the consequence of failure.
**In use:** "FS on the revised footing comes out to 3.68 — comfortably above the report's 3.0 target, without over-building it."
**Misuse:** quoting FS without stating what it's a ratio of (ultimate over allowable? ultimate over actual?) — the same number means different things depending on the denominator.

**Freeboard** — The vertical distance between a design water surface elevation and the top of the containing structure (basin berm, channel bank), a margin against routing error, sedimentation, and wave action, not a substitute for correct sizing.
**In use:** "One foot of freeboard above the routed 100-yr WSEL, per the ordinance minimum — that's separate from the emergency spillway."
**Misuse:** treating freeboard as the mechanism for handling storms larger than the design event — that's what the emergency spillway is for; freeboard is margin on the design event itself.

**Detention vs. retention** — Detention temporarily stores runoff and releases it at a controlled rate to match a pre-development or ordinance-set peak; retention holds water permanently (a wet pond) or relies on infiltration, without a controlled surface discharge.
**In use:** "Soils here don't infiltrate fast enough for retention to work within the available footprint, so we're detention with a controlled orifice release."
**Misuse:** using the terms interchangeably in a report — the review agency reads them as distinct systems with different maintenance and failure modes, and mislabeling one as the other is a common review-comment trigger.

**Design storm vs. check storm** — The design storm (often 10-yr) sizes the primary system; the check storm (often 100-yr) verifies the system doesn't cause unacceptable damage or overtopping even though it isn't sized for that event.
**In use:** "Pipe network is sized to the 10-yr design storm; we ran the 100-yr check storm separately to confirm the overland flow path doesn't flood the building pad."
**Misuse:** designing only to the design storm and never running the check storm — code and prudent practice both require confirming what happens when the design event is exceeded, which is common.

**Return period / "100-year storm"** — A statistical statement (1% annual exceedance probability), not a promise of frequency; a location can see two "100-year" events in one decade without contradicting the statistic.
**In use:** "That's the 1%-annual-exceedance event — calling it 'the flood that happens once a century' is the misreading that gets people arguing with the math."
**Misuse:** treating the return period as a literal recurrence interval, which leads owners and sometimes reviewers to underestimate the real annual risk.

**RFI (request for information)** — A formal, logged construction-phase question from the contractor to the design team about a field condition, ambiguity, or conflict in the drawings, requiring a written, dated response.
**In use:** "RFI-014 flagged shallower groundwater than the boring log showed — response revised the bedding spec for that station range only."
**Misuse:** treating an RFI response as optional paperwork after a verbal field decision already happened — the written response is the record; without it, the authorized scope of a change is legally ambiguous.

**Record drawings ("as-builts")** — Drawings updated to reflect what was actually constructed, including deviations authorized by RFI response or field change, distinct from the original stamped construction documents.
**In use:** "Record drawings show the footing at 9'-0" sq. per the RFI revision — the original S-301 sheet still shows 6'-0" and is superseded."
**Misuse:** calling the original stamped set "as-built" without updating it — if construction deviated and the drawing wasn't revised, it isn't a record of what exists.

**Construction observation** — The engineer's periodic (not continuous, unless specified) site visits during construction to verify general conformance with the design intent, distinct from the contractor's own means-and-methods responsibility and from continuous inspection.
**In use:** "Observation frequency for the drainage work is weekly during grading, plus a hold point before backfilling the detention outlet structure."
**Misuse:** assuming construction observation means the engineer inspected every detail or guarantees defect-free construction — it verifies substantial conformance with design intent at defined intervals, and the scope/frequency should be explicit, not assumed.

**Value engineering (VE)** — A structured cost-reduction review of a design, properly done by testing alternatives against the same performance requirements, not by trimming the requirements themselves.
**In use:** "This VE request reduces pipe diameter without new hydrology support — that's cutting the requirement, not value-engineering it."
**Misuse:** using "value engineering" as a label for reducing a safety or code margin without new supporting analysis — genuine VE finds a cheaper way to meet the same performance target, it doesn't quietly lower the target.

**Seismic Design Category (SDC)** — An ASCE 7 classification (A through F) combining a site's seismic hazard, soil site class, and the building's risk category, which drives the structural detailing requirements — including foundation-structure interaction assumptions the civil engineer must respect.
**In use:** "This site's SDC came out higher than the last project's once we applied the actual site class from the geotech report, not the default assumption."
**Misuse:** assuming SDC transfers unchanged from a nearby or similar past project — it's a function of the specific site's soil class and the specific building's risk category, both of which vary project to project.

**Impervious cover / imperviousness** — The percentage of a site's area that prevents infiltration (roof, pavement, compacted surfaces), the primary driver of the rational method's C coefficient and of curve-number selection.
**In use:** "Conceptual design assumed 65% impervious; the final site plan came in at 70% — that 5-point shift changes the detention volume requirement and has to be reconciled before the final drainage report."
**Misuse:** carrying a conceptual-stage imperviousness estimate through to the final stamped drainage report without reconciling it against the actual final site plan.
