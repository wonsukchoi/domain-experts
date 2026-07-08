# General Engineer — Red Flags

### Submittal or shop-drawing note reads "same capacity/hardware, just more buildable" with no re-derivation of the load path it touches
- **Usually means:** the fabricator or contractor changed how a load or signal travels through the assembly (split a continuous member into two, rerouted a connection) while believing unchanged part specs mean unchanged behavior — the Hyatt Regency hanger-rod shape.
- **First question:** "Trace this exact load from its source to its final support with the new detail — does any single connection now carry more than it did in the original design?"
- **Data to pull:** the original design's load-path calculation next to the proposed submittal, redrawn with the new geometry.

### Recomputed factor of safety lands within 10% of the code-mandated minimum and is presented as the sign-off basis
- **Usually means:** the review stopped at "passes code" instead of asking what unmodeled load case (quartering wind, a field substitution, a construction-sequence load) could still exceed it — Petroski's factor-of-ignorance framing.
- **First question:** "What load case does this code minimum not model, and does this design see it?"
- **Data to pull:** the governing load case behind the code-minimum FoS and any deviation between that assumption and actual site/service conditions.

### A load path, unit convention, or data format crosses a contractor/team boundary with no Interface Control Document in place before integration starts
- **Usually means:** each side assumes the other is using the same convention because nobody was assigned to own the seam — the Mars Climate Orbiter shape (newton-seconds vs. pound-force-seconds, a 4.45x mismatch).
- **First question:** "Who signed the ICD for this specific interface, and does it name the units, tolerances, and format explicitly rather than by reference to 'standard practice'?"
- **Data to pull:** the ICD itself, or its absence, plus each side's independent spec sheet for the interface in question.

### A downstream joint or connection-type substitution (bolted for welded, one material grade for another) is accepted on the basis that it's "the same category" as the original
- **Usually means:** buildability or cost pressure is being treated as design-neutral without re-running the calculation the substitution actually touches — the Citicorp Center shape, where a bolted-joint swap was never re-checked against quartering winds (a 40% wind-load, 160% connection-load increase the original calc never covered).
- **First question:** "What specific load case or wind direction does the original design assume this joint sees, and has the substituted joint been checked against that same case?"
- **Data to pull:** the original connection calculation and the substitution's own capacity data under the same load case, not a generic allowable-stress table.

### A problem sits outside the five-of-seven OPM core competency areas (statics/dynamics, strength of materials, fluid mechanics, thermodynamics, electrical fields/circuits, materials science, or a comparable area) and is being reasoned through by analogy instead of routed
- **Usually means:** the generalist is pattern-matching to a discipline they know rather than admitting the problem needs one they don't — useful for the lightest problems, unreliable the moment a discipline-specific failure mode is in play.
- **First question:** "Which of your five core areas does this actually fall under, and if none, who's the named specialist you're routing it to?"
- **Data to pull:** the specialist bench list and whether this problem class has a named owner on it already.

### Requirements traceability matrix has a requirement with an empty verification-or-validation column
- **Usually means:** either the requirement is genuinely untested (a real gap) or it was never testable as written and should have been reclassified, not left dangling — the INCOSE V-model's left-leg-to-right-leg link broken.
- **First question:** "Is this requirement unverifiable as stated, or verifiable but simply not yet tested?"
- **Data to pull:** the traceability matrix and the requirement's original acceptance-criterion wording.

### A safety-relevant professional disagreement is escalated verbally, with no dated written record
- **Usually means:** the engineer raised the concern but didn't create the record NSPE Canon 1 actually requires — a verbal aside doesn't establish that the employer or client was formally notified before the decision proceeded.
- **First question:** "Where's the timestamped memo or email that documents this notification, separate from the meeting where it was discussed?"
- **Data to pull:** the written escalation record, or its absence, and the date it was sent relative to the decision it concerns.

### A field retrofit or fix is executed without a documented update to the original governing calculation
- **Usually means:** the fix was scoped to make the immediate symptom go away rather than to close the gap between the as-built condition and the design basis — the kind of unlogged night-time correction that leaves the next reviewer trusting a calculation that no longer matches the structure.
- **First question:** "Does the design calculation on file reflect what's actually built now, or what was built before this retrofit?"
- **Data to pull:** the as-built drawing set and the design calculation's revision history.

### A design change is proposed after verification testing or analysis has already started, with no documented impact assessment
- **Usually means:** schedule pressure is treating the change as small enough to fold in without asking which already-completed verification steps it invalidates.
- **First question:** "Which specific verification or analysis activities does this change actually touch, and have those been rerun?"
- **Data to pull:** the change-request record and the re-verification scope decision tied to it, if one was made.

### An Interface Control Document exists but hasn't been re-issued after a vendor or contractor change order that touches it
- **Usually means:** the ICD is being treated as a one-time artifact instead of a living document, so it now describes an interface that no longer matches either side's as-built state — worse than having no ICD, because it reads as current when it isn't.
- **First question:** "What's the date of the most recent change order on either side of this interface, and does it postdate the ICD's last revision?"
- **Data to pull:** the ICD's revision history next to each side's change-order log.
