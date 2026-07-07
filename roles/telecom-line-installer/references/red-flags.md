# Red flags

Smell tests an outside-plant technician or splicing lead catches before a closure is sealed, an OTDR trace is accepted, or a pole is attached.

### Single splice event on the OTDR trace exceeds ~0.3dB

**Usually means:** a bad cleave angle, fiber-end contamination, or a mismatched fiber type at the splice, not acceptable variance — modern fusion splices typically run 0.02–0.05dB.
**First question:** "What did the splicer's own loss estimate say at the time, and does the field OTDR reading match it or diverge?"
**Data to pull:** the fusion splicer's logged loss estimate for that splice, the OTDR trace file, and the cleave-angle reading if the splicer records one.

### Bidirectional OTDR readings for the same splice differ by more than roughly 0.1–0.2dB

**Usually means:** a "gainer" or "loss" artifact from a mismatched fiber core/mode-field diameter at the joint, or a directional reflectance issue — the true splice loss is the average of both directions, and a large spread signals a joint that needs attention even if one direction looks fine.
**First question:** "What's the averaged bidirectional loss, not just the direction that happened to be tested first?"
**Data to pull:** both-direction OTDR trace files and the averaged value calculation.

### New or existing attachment measured inside the communication worker safety zone on a joint-use pole

**Usually means:** either the pole's voltage class was misread, the attachment was made before make-ready confirmed the required clearance, or a prior attacher's relocation never happened.
**First question:** "What's the actual measured distance from this attachment to the lowest power conductor, and what does the pole owner's engineering table require for this voltage class?"
**Data to pull:** the make-ready survey/engineering table for this specific pole, a field clearance measurement, and the pole attachment permit record.

### New attachment made before make-ready completion is confirmed by the pole owner

**Usually means:** schedule pressure pushed the crew to attach ahead of the regulatory sequence, leaving unrelocated existing attachments (and their clearance violations) still in place on the same pole.
**First question:** "Has the pole owner issued written confirmation that make-ready is complete on this specific pole, not just that the application was filed?"
**Data to pull:** the make-ready completion notice or survey sign-off, pole by pole, not a blanket project-level status.

### Fiber slack coiled visibly tighter than the cable's rated minimum bend radius to fit a closure or handhole

**Usually means:** the enclosure is undersized for the slack loop being stored, or the technician prioritized fitting the slack over the bend-radius spec under time pressure.
**First question:** "What's this cable's rated minimum bend radius at rest, and what's the actual coil diameter in this closure?"
**Data to pull:** the cable manufacturer's datasheet bend-radius figure and a physical measurement of the installed coil.

### Splice closure re-entered for a repair without replacing the gel seal or verifying reseal

**Usually means:** the technician treated the closure as "just a box to open," not a component with its own re-entry procedure needed to maintain its environmental rating — a common precursor to moisture-intrusion failures found months later.
**First question:** "What's this closure's re-entry procedure, and was it followed on this repair?"
**Data to pull:** the closure manufacturer's re-entry/reseal instructions and the job's closure-out documentation.

### Calculated loss-budget margin under 3dB against the transceiver's rated optical budget

**Usually means:** the design was built to the ceiling rather than with a maintenance reserve, and a future splice, connector swap, or seasonal attenuation drift will push the link out of spec.
**First question:** "What optics class was actually specified, and does the calculated margin leave room for at least one more splice or connector event?"
**Data to pull:** the loss-budget worksheet (fiber length, splice count, connector count, splitter ratio) and the transceiver's rated optical budget class.

### New cable overlashed onto an existing strand without checking the strand's remaining tension capacity

**Usually means:** overlash is being treated as a clearance-free shortcut because it reuses existing hardware, when the added cable weight and wind/ice loading can exceed what the original strand and attachment were engineered for.
**First question:** "What's the original strand's rated tension capacity, and has anyone recalculated loading with the new cable added?"
**Data to pull:** the original pole attachment's engineering specification and the combined-load calculation for the overlashed configuration.

### As-built splice/fiber-count records don't match the field OTDR trace at turn-up

**Usually means:** a crossed pair or a fiber assigned to the wrong strand somewhere in the splice chain — activating service on a mismatched fiber sends the wrong signal to the wrong customer or drop.
**First question:** "Does the fiber that traces to this drop match the fiber number in the as-built splice log, end to end?"
**Data to pull:** the as-built splice/fiber map and a fresh end-to-end continuity/OTDR trace for the specific fiber being turned up.
