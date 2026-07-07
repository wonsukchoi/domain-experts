# Vocabulary

Terms generalists (and some adjusters) conflate that practitioners keep sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## Position statement vs. repair procedure

A **position statement** is a manufacturer's blanket policy on a class of repair or material (e.g., "do not section ultra-high-strength steel components without an explicitly published procedure"). A **repair procedure** is the specific, step-by-step instruction for one operation on one component, often citing the position statement as its governing rule.

*Practitioner usage:* "The position statement rules out sectioning this steel class at all — I don't need the specific procedure to know we're replacing the assembly."

*Common misuse:* treating the absence of a position statement as permission. No published statement means no authorized repair method exists yet, not that any method is acceptable.

## Sectioning vs. splicing vs. panel replacement

**Sectioning** cuts and rejoins a structural component at an OEM-specified location, leaving part of the original panel in place. **Splicing** is a form of sectioning, sometimes used specifically for non-structural or cosmetic panel joins. **Panel replacement** removes the entire component and installs a new one at the original factory seams.

*Practitioner usage:* "This rail is sectionable at the OEM cut line, but the door ring in front of it isn't — that's full-assembly replacement only."

*Common misuse:* assuming sectioning is always the cheaper, faster default and only escalating to replacement when sectioning proves difficult, rather than checking the OEM procedure first to see whether sectioning was ever authorized for that part.

## Pull vs. replace

**Pull** means straightening a structural member back to OEM measurement tolerance using a bench or tower system, preserving the original steel. **Replace** removes the deformed component entirely. The dividing line is not "how far out of spec" — it's whether the steel is kinked, cracked, or torn.

*Practitioner usage:* "It's 7mm out, which is more than tolerance, but there's no kink — pull it, re-measure, and it's a valid repair."

*Common misuse:* treating "far out of tolerance" as automatically requiring replacement, or treating "within tolerance" as automatically meaning no kink exists — tolerance and steel integrity are two separate checks, both required.

## Datum vs. centerline

The **datum** is the full set of OEM-published reference points (X/Y/Z coordinates) a measuring system compares actual body dimensions against. The **centerline** is one specific reference line — the vehicle's longitudinal axis — used to confirm the body hasn't shifted side to side before trusting any other measurement.

*Practitioner usage:* "Centerline reads true, so the datum points we're measuring off it are trustworthy — if centerline were off, every other reading downstream would be meaningless."

*Common misuse:* measuring damage-zone points first and treating clean readings as proof of an undamaged vehicle, without first confirming the centerline itself wasn't shifted by the collision.

## UHSS / AHSS / boron steel

**AHSS** (advanced high-strength steel, roughly 340-780 MPa) and **UHSS** (ultra-high-strength steel, roughly 780 MPa and up) are strength classes defined by tensile rating. **Boron-alloyed (hot-stamped) steel**, often around 1,500 MPa, is a specific UHSS subtype requiring the most restrictive repair treatment — commonly no sectioning, no heat straightening at all.

*Practitioner usage:* "It's boron, not just UHSS generally — no heat, no sectioning, full assembly replacement is the only path regardless of how minor the deformation looks."

*Common misuse:* using "high-strength steel" as one undifferentiated category. The repair rules tighten sharply at each strength tier, and boron sits in its own, more restrictive tier above generic UHSS.

## Static calibration vs. dynamic calibration

**Static calibration** aims a sensor against fixed OEM-specified targets in a controlled, level bay at exact measured distances. **Dynamic calibration** requires driving the vehicle at a specified speed under specified road and lane-marking conditions while the system self-calibrates. Many vehicles require both, in a specific order.

*Practitioner usage:* "This system needs static first to get the camera roughly aimed, then dynamic to fine-tune against real lane data — skip the static step and the dynamic drive won't converge."

*Common misuse:* treating a test drive as an acceptable substitute for a required static calibration, or vice versa, rather than checking which the specific OEM procedure requires and in what sequence.

## Not-included operation

A repair step that estimating platforms (Mitchell, CCC ONE, Audatex) don't automatically add when a related operation is selected — the technician or estimator must add it manually because the database's default labor time assumes it isn't needed. ADAS calibration after bumper or glass work is the most commonly missed example.

*Practitioner usage:* "Calibration is a not-included operation on this line code — if we don't add it manually, the estimate ships without it and the insurer never sees the requirement."

*Common misuse:* assuming that because the estimating platform didn't prompt for an operation, the vehicle doesn't need it. The platform's silence reflects a database gap, not an OEM requirement.

## Supplement

An additional, itemized claim submitted after the original estimate, covering damage or required operations found during teardown or repair that weren't visible or known at the time of the first write. Distinct from a revised estimate, which restates the whole job — a supplement adds to what's already approved.

*Practitioner usage:* "The supplement is three lines, each sourced to a photo or measurement — it's not a renegotiation of the whole estimate, just the delta the teardown found."

*Common misuse:* submitting a supplement as a single bigger total rather than itemized, sourced additions, which reads as a markup attempt instead of documented findings.

## Blueprinting

The pre-repair process of full teardown, measurement, and OEM-procedure lookup that produces a complete, accurate repair plan before major parts ordering or panel work begins — distinct from the initial insurance estimate, which is typically written without a teardown.

*Practitioner usage:* "We blueprint before we order a single part on anything structural — otherwise we're ordering against a guess."

*Common misuse:* treating blueprinting as optional on "obviously cosmetic" jobs, which is exactly where hidden structural or sensor-mount damage gets missed because no one looked past the visible panel.

## Total loss threshold / ACV

The **actual cash value (ACV)** is the insurer's determined pre-loss value of the vehicle. The **total loss threshold** is the state-specific percentage of ACV (commonly in the 70-80% range, formula varies by state) at which repair cost triggers a mandatory total-loss determination rather than repair authorization.

*Practitioner usage:* "We're at 74% of ACV with the structural line added — that's past this state's threshold, so this becomes a total-loss claim regardless of whether we could physically fix it."

*Common misuse:* assuming total-loss decisions are negotiable shop-versus-insurer calls. Once repair cost crosses the state-formula threshold, the determination is largely mechanical, not a judgment call on repairability.

## Cycle time vs. touch time

**Cycle time** is the total calendar days from intake to delivery, including waiting on parts and approvals. **Touch time** is the actual hours a technician spends working on the vehicle. A long cycle time with short touch time points to a process stall (parts, supplement approval), not a labor problem.

*Practitioner usage:* "Touch time on this job is maybe six hours — the other nine days are the supplement sitting with the adjuster, not us being slow."

*Common misuse:* using cycle time alone to judge technician performance, when the gap between cycle time and touch time usually points to an external bottleneck instead.
