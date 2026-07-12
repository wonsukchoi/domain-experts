# Solar Energy Installation Manager — Vocabulary

### Solar access
The percentage of incident solar energy a location receives accounting for shading over a full year, as calculated by a shading tool (Solmetric SunEye, Aurora Solar) — distinct from raw shade-free roof area.
**In use:** "That string is reporting 82% solar access — under our 85% threshold, so it's flagged for module-level power electronics before we finalize the layout."
**Common misuse:** Treated as interchangeable with "percent of roof that's shade-free," when solar access is a time-weighted energy calculation that can be much lower than a simple visual read of shaded roof area suggests.

### Rapid shutdown boundary
The line, typically 1 foot inside the array's physical edge, that separates conductors required to drop to ≤80V within 30 seconds (inside) from those required to drop to ≤30V (outside), per NEC 690.12.
**In use:** "Confirm the disconnect label sits right at the rapid shutdown boundary, not just somewhere near the array edge."
**Common misuse:** Assumed to be the array's visible physical edge itself, when it's a defined offset the code specifies — placing shutdown equipment at the wrong line is a labeling failure inspectors catch on site, not one the design software flags.

### AC428 margin
The ICC-ES AC428 test protocol requirement that a fastener withstand 1.5× its stated design load without permanent deformation — the allowable design load is therefore nominal capacity ÷ 1.5, not the nominal capacity itself.
**In use:** "Nominal capacity is 485 pounds at that embedment, so the AC428-allowable is 323 pounds — that's the number we check the redistributed load against, not the 485."
**Common misuse:** Confused with the fastener's rated withdrawal capacity, leading someone to compare a redistributed load directly against the manufacturer's nominal number and clear a fastener that actually fails once the 1.5x margin is applied.

### Embedment depth
The actual measured length of a fastener's threaded portion seated into the rafter, used to calculate nominal withdrawal capacity — distinct from the manufacturer's spec-sheet minimum.
**In use:** "Pull embedment depth from what was actually measured on site today, not the 2.5-inch minimum off the install manual."
**Common misuse:** Assumed to equal the spec-sheet minimum by default, when actual on-site embedment can run shorter (rafter width, drill stop error) and using the spec minimum overstates real capacity.

### Withdrawal capacity
A fastener's rated resistance to being pulled straight out of the substrate, expressed per inch of thread penetration (e.g., ~194 lbs/inch for a #14 lag) — a per-inch rate, not a fixed per-fastener number.
**In use:** "At 194 pounds per inch and 2.5 inches of actual embedment, that lag's nominal capacity is 485 pounds — before we even get to the AC428 margin."
**Common misuse:** Quoted as a flat per-fastener rating without multiplying by actual embedment, which silently overstates capacity whenever the on-site embedment is shorter than assumed.

### Row-level loss
The engineering reality that dropping one module or one attachment point from a row typically forces losing the entire row (or redistributing the entire row's load), because racking rail continuity, setback pathways, and per-string electrical design don't tolerate a mid-row gap.
**In use:** "That vent stack doesn't cost us one module — it's a row-level loss, four modules gone, not one twenty-eighth."
**Common misuse:** Read as a proportional, module-by-module fraction (1 of 28 modules = 3.6%), when rail splicing and string voltage recalculation usually force dropping the whole row instead of just the affected unit.

### Derate stack
The sequence of four multiplicative corrections — NEC 690.8(A) continuous-current factor, 690.8(B) safety factor, ambient-temperature correction, and conduit-fill/bundling adjustment — all applied in order to size a conductor, not any single one of them alone.
**In use:** "Don't stop at the 690.8 multiplier — run the full derate stack through ambient and conduit-fill before you size the wire."
**Common misuse:** Treated as satisfied by applying only the 125% continuous-current multiplier and calling the circuit sized, which is the single most common electrical permit-review miss on this checklist.

### Competent person
An OSHA-defined designation: a specific individual named and accountable for identifying site hazards and authorizing corrective action that day — not a general reference to anyone experienced on the crew.
**In use:** "Who's the competent person on this roof today — name them on the log, not just 'the foreman.'"
**Common misuse:** Used loosely to mean "an experienced installer," when it's a named, documented, per-job-site designation OSHA inspectors specifically ask for by name, separate from any certification a crew member holds.

### Infrequent and temporary exemption
A narrow OSHA fall-protection carve-out from tie-off requirements that only applies when BOTH a written 15-foot no-approach rule exists AND that rule is actively enforced — not merely that the job is short in duration.
**In use:** "You can't invoke infrequent-and-temporary just because the job's two hours — where's the written, enforced 15-foot rule?"
**Common misuse:** Cited based on job duration alone, satisfying only the "infrequent" half while skipping the paired requirement that a documented, enforced no-approach rule also be in place — the exemption is invalid without both.

### NABCEP JTA (Job Task Analysis)
A certification competency baseline covering individual technical skill for installers, foremen, designers, and project managers — not a substitute for a site-specific safety-supervision designation.
**In use:** "Everyone on this crew is NABCEP-certified, but that doesn't answer who's the competent person for today's fall-protection call."
**Common misuse:** Treated as sufficient proof that site supervision is covered, when the JTA validates individual technical competence, not who owns the site-specific, day-of safety and schedule authority.

### Permission to Operate (PTO)
The utility's formal authorization to energize an interconnected system, granted on a utility-specific timeline that varies by configuration (solar-only vs. solar-plus-storage) — not a single industry-wide average.
**In use:** "This utility runs 4-6 weeks solar-only but 8-12 for storage — quote the customer off that split, not a national median."
**Common misuse:** Quoted from a generic national median or from memory of a different utility's timeline, producing customer-facing dates that don't match the actual interconnecting utility's published range.

### Change order (survey-driven)
A signed, dollar-quantified revision to the sold contract triggered by a site-survey finding that alters scope — required before crew mobilization, not a verbal heads-up or an assumed approval.
**In use:** "The change order's drafted and priced, but we don't mobilize the crew until it's signed, not just sent."
**Common misuse:** Treated as complete once sent to the customer, when the operative gate is signature received — proceeding on the assumption of approval is a documented driver of disputed invoices later.

### Setback (fire code)
The mandated clearance distance — typically 18 to 36 inches depending on jurisdiction — that must be kept clear around a roof's ridge, eaves, and edges for firefighter access, independent of any shading or structural concern.
**In use:** "That row violates setback on the ridge side — we drop the row, we don't shrink individual module footprints to squeeze under the line."
**Common misuse:** Assumed to be a single national number, when the actual clearance is set by the locally adopted fire code and varies by jurisdiction — designing to a remembered number from a prior job's AHJ produces a rejected permit here.

### Torque spec (fastener)
A manufacturer-defined range with two independent failure directions: under the floor value voids the warranty and invalidates the AC428 test basis, while over the ceiling ruptures the washer or flashing seal — not a single minimum to clear.
**In use:** "Log the actual torque applied at every point — under 15 ft-lb voids the basis, over 20 ruptures the seal, both are a fail."
**Common misuse:** Treated as a single floor to hit ("tighten it enough"), when over-torquing past the manufacturer's ceiling is an equally real failure mode that damages the flashing seal.
