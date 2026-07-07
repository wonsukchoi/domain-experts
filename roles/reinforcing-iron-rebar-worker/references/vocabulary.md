# Vocabulary

Terms generalists flatten together that a rebar worker keeps sharply separate — the value is in the misuse, not the definition.

## Development length (ld) vs. lap splice length

**Development length** is the embedment length a single bar needs to develop its full yield strength in the surrounding concrete. **Lap splice length** is a separate, longer quantity — ld multiplied by a class factor (1.0 or 1.3) — because two overlapping bars have to transfer force to each other through the concrete and bar deformations, not just anchor one bar's own force.

**In use:** "ld for this bar's 38 in — but the splice is Class B, so it's 1.3 times that, 50 in, not 38."

**Common misuse:** using the bare development length as the splice length, undercutting the required lap by the class multiplier.

## Class A vs. Class B splice

**Class A** (1.0 × ld) applies only when ≤50% of the bars in a section are spliced within the required lap length *and* the steel area provided is at least twice the area required. **Class B** (1.3 × ld) applies to all other cases and is the correct default whenever those two conditions haven't been actively confirmed.

**In use:** "Don't assume Class A just because it's shorter — check the splice percentage and the area ratio first, or it's Class B by default."

**Common misuse:** applying Class A as a general shortcut without verifying either of its two required conditions.

## Top bar vs. bottom bar (ψt factor)

A **top bar** is horizontal reinforcement placed with more than 12 in of fresh concrete cast beneath it before the pour reaches it — settlement and bleed water weaken the bond, so it carries a higher ψt factor (1.3) and a longer required development length. A **bottom bar** sits below that condition and uses ψt = 1.0. The distinction is about pour geometry and depth of concrete below the bar, not simply which mat (top or bottom of the slab) the bar belongs to.

**In use:** "That bar's technically in the top mat, but it's got less than 12 inches of concrete under it at this thickness — ψt is 1.0, not 1.3, here."

**Common misuse:** assuming "top mat" and "top bar" (in the ψt sense) are always the same thing, missing thin sections where the 12 in threshold isn't actually met.

## Grade mark (mill mark)

The rolled-in marking system on a bar identifying producer, size, type (A615 or A706), and grade — a numeral or a system of continuous lines stamped into the bar itself, independent of any paper delivery ticket or bundle tag.

**In use:** "Ticket says Grade 60, but check the mark on the bar — if it's got a line rolled in, it's 75, and that changes the lap length."

**Common misuse:** trusting the delivery ticket or tag as proof of grade instead of reading the mark rolled into the steel.

## Slab bolster (SB) vs. high chair (HC/CHC)

A **slab bolster** is a continuous, low-profile support for a bottom mat, running the length of a bar run. A **high chair** (individual, HC, or continuous, CHC) elevates a top mat to its required height above the bottom mat or form, in taller stock heights than a bolster. Confusing the two on an order means the wrong support height ends up under the wrong mat.

**In use:** "Bottom mat's on 2-inch SB, top mat needs a 5¾-inch CHC — don't order high chairs for the bottom run, they're the wrong profile for that cover."

**Common misuse:** treating "chair" as one generic category and ordering by height alone without matching the support type to which mat and cover condition it's serving.

## Cover vs. clear spacing

**Cover** is the distance from the outer surface of the bar to the nearest face of the concrete. **Clear spacing** is the distance between adjacent bars (or bar surfaces), which separately affects the ψe epoxy factor and the favorable/unfavorable development-length case — the two aren't interchangeable inputs even though both get called "spacing" loosely on site.

**In use:** "Cover's fine at 2 inches, but check clear spacing too — if it's under 6 bar diameters, ψe jumps to 1.5 and the lap length gets longer."

**Common misuse:** treating cover and clear spacing as the same number, or checking only one when both independently affect the required development length.

## Epoxy factor (ψe) and "holiday"

**ψe** is the development-length multiplier applied to epoxy-coated bars (1.5 or 1.2, depending on cover/spacing) because the coating reduces bond with the concrete. A **holiday** is a coating discontinuity — a pinhole, scrape, or gap in the epoxy exposing bare steel — the specific defect the damage-threshold rules exist to catch.

**In use:** "It's epoxy-coated, so ψe applies regardless of holidays — but if the holidays add up past the threshold, the bar needs patching or rejection on top of that."

**Common misuse:** treating ψe as a coating-condition penalty (i.e., assuming a damaged bar gets a different ψe) rather than a bond-property factor that applies to any epoxy-coated bar regardless of damage, with damage handled as a separate accept/patch/reject decision.

## Bar-bending schedule (BBS)

The fabrication-level document listing every bar's mark number, size, grade, cut length, bend shape, and quantity — distinct from the placing drawing, which shows where each marked bar goes in the structure. A field conflict gets resolved by cross-checking both, not either alone.

**In use:** "Mark 214 on the BBS is a #6 with a 90-degree hook — cross-check the placing drawing to confirm which wall it lands in before cutting the run."

**Common misuse:** treating the BBS as sufficient on its own for field placement, missing the placing drawing's location and orientation information.

## Mechanical splice (coupler) vs. lap splice

A **mechanical splice (coupler)** joins two bar ends with a threaded, swaged, or grip-type device rated to develop the bar's full tensile capacity, used where congestion or bar size makes lapping impractical. A **lap splice** relies on the concrete itself to transfer force between overlapping bars over a calculated length. They are not interchangeable defaults — a coupler substitutes for lap-length math entirely but has its own rated capacity that must match the bar.

**In use:** "Too congested to lap these #11s — spec calls for a mechanical coupler here instead, rated for full tension, not a partial-capacity splice."

**Common misuse:** assuming any coupler is equivalent to any lap splice without checking the coupler's own tested and rated capacity against the bar size and grade in use.

## As-built deviation

A documented departure from the original placing drawing — a relocated splice, a substituted grade, a rerouted bar around an embed — approved by the engineer of record and recorded on the as-built set, distinct from an undocumented field improvisation that happens to look similar.

**In use:** "That Grade 75 substitution is logged as an as-built deviation with the EOR's sign-off — it's not just something we did in the field and hoped was fine."

**Common misuse:** treating any field adjustment as automatically covered "as long as it's noted somewhere," without engineer-of-record approval actually on record.

## Rebar congestion

A section where the volume and spacing of specified reinforcement approaches or exceeds what standard bar sizes and lap splices can physically fit while maintaining clear spacing and cover — a design and constructability problem flagged before tying, not a fitting problem solved by field improvisation once the mat is underway.

**In use:** "This beam-column joint is congested enough that lapping isn't going to work — flag it now, before we're mid-tie and forcing bars into gaps that don't exist."

**Common misuse:** discovering congestion only while physically trying to tie the section, instead of catching it during the placing-drawing review where a coupler or detail change can still be requested.
