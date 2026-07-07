# Commercial/Industrial Designer — Vocabulary

### DFM (Design for Manufacturability)
A review discipline checking whether a design's geometry can be produced by the intended manufacturing process without excess cost or defect risk.
**In use:** "We're not releasing to tooling until DFM signs off on the wall-thickness transitions."
**Common misuse:** Treated as a one-time gate at the end of design instead of a continuous constraint checked from the first sketch — leads to late, expensive redesigns.

### Draft angle
The slight taper applied to vertical faces of a molded part so it releases cleanly from the tool without dragging or damage.
**In use:** "That boss needs at least 1.5° of draft or it'll gouge the cavity on ejection."
**Common misuse:** Assumed to be a tooling-shop concern that can be "added later" — draft angle changes the part's surfaces and must be built into the CAD geometry, not patched in afterward.

### Undercut
A geometric feature that prevents a part from releasing straight out of a simple two-piece mold, requiring a side-action, slide, or lifter to produce.
**In use:** "The snap clip is an undercut — it'll need a slide, and that's a tooling cost adder."
**Common misuse:** Treated as purely a cosmetic or minor detail; an undercut is a specific, quotable cost and lead-time impact, not a footnote.

### Tolerance stack-up
The cumulative dimensional variation across multiple mating parts or features, which can exceed any single part's individual tolerance.
**In use:** "Each part is within spec individually, but the tolerance stack-up across the four-part assembly could still cause an interference fit."
**Common misuse:** Checking each part's tolerance in isolation without summing the stack across an assembly — a common source of "parts that measure fine individually but don't fit together."

### Material index
A ranking metric (e.g., strength-to-weight, fatigue-life-to-cost) derived from a part's dominant load case, used to shortlist candidate materials objectively.
**In use:** "For a part that's flexed repeatedly, fatigue life is the material index that matters, not raw stiffness."
**Common misuse:** Ranking materials by a generic property (like tensile strength) instead of the index that actually matches the part's real loading condition.

### Soft tooling vs. hard tooling
Soft tooling (aluminum, sometimes 3D-printed inserts) is cheaper and faster to build but wears out after a limited number of shots (often <25,000-100,000); hard tooling (hardened steel) costs more and takes longer but lasts for high-volume production runs.
**In use:** "At 8,000 units for year one, an aluminum soft tool makes sense — we'll requalify for steel if year two volumes justify it."
**Common misuse:** Assuming "tooling" always means the expensive steel option, or conversely assuming soft tooling is always the cheap safe default regardless of volume.

### Anthropometric percentile
A statistical range (e.g., 5th to 95th percentile) of a human body dimension used to set design constraints for fit, reach, or grip.
**In use:** "We're designing the grip diameter to the 5th-percentile female hand to the 95th-percentile male hand range."
**Common misuse:** Designing to a single "average" (50th percentile) figure, which by definition excludes roughly half the target population on that dimension.

### Living hinge
A thin, flexible section of plastic (typically in polypropylene) molded as an integral part of a component, designed to flex repeatedly without fatigue failure.
**In use:** "The living hinge is rated for thousands of open-close cycles as long as we stay in PP — ABS would crack after a few hundred."
**Common misuse:** Specifying a living hinge in a material chosen for other properties (like ABS for its rigidity elsewhere in the part) without checking that material's fatigue behavior at the hinge specifically.

### Snap-fit
A mechanical joining feature where a flexible arm or tab deflects to engage a mating undercut, then returns to hold the assembly together without fasteners.
**In use:** "The battery door uses a cantilever snap-fit — we calculated the deflection force to land in the 20-40N range for one-handed release."
**Common misuse:** Sizing the snap geometry by visual proportion instead of calculating the actual deflection force, resulting in either field failures (too weak) or user frustration (too stiff).

### Ejector-pin witness mark
A small visible circular mark left on a molded part's surface where an ejector pin pushed the part out of the tool.
**In use:** "Locate the ejector pins on the interior ribs so witness marks don't show on the cosmetic face."
**Common misuse:** Overlooked during design review and only discovered on the first molded sample, when relocating pins requires a tool modification.

### Parting line
The line on a molded part where the two (or more) halves of the tool meet, often visible as a fine seam on the finished part.
**In use:** "We pushed the parting line to the back edge so it doesn't cross the logo on the front face."
**Common misuse:** Left to the mold designer to place without design input, resulting in a visible seam crossing a cosmetically sensitive surface.

### Rapid prototyping tier
The specific fabrication method (SLA, FDM, CNC, soft tooling) chosen to match the fidelity and material properties needed to answer a particular design question.
**In use:** "We only need an FDM print to check the button spacing — save the SLA budget for the finish-critical review."
**Common misuse:** Defaulting to the highest-fidelity/most expensive prototyping method available regardless of what question the prototype actually needs to answer.
