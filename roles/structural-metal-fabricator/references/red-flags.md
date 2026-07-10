# Red flags

### Root gap measures outside the WPS-specified tolerance before tacking
- **Usually means:** the joint won't weld correctly to the qualified procedure without either extra passes not covered by the WPS, or rework of the fit.
- **First question:** what does the actual applicable WPS specify for this joint's root gap?
- **Data to pull:** the WPS's joint-preparation specification compared against the measured root gap.

### Every individual segment of a multi-piece assembly passes its own square/alignment check, but no cumulative check has been run across the full assembly
- **Usually means:** worst-case error could stack beyond the assembly-level tolerance even though every individual piece passed on its own.
- **First question:** what's the per-segment tolerance, how many segments are there, and what's the overall assembly-level tolerance?
- **Data to pull:** the per-segment tolerance, segment count, and the project's stated overall assembly tolerance.

### A tack weld at a high-restraint joint shows visible cracking or is undersized
- **Usually means:** it risks becoming a crack-initiation point that the final weld pass won't fully consume.
- **First question:** what's this joint's restraint classification, and does the tack meet the same quality bar as the final weld?
- **Data to pull:** the tack-weld inspection note and the joint's restraint classification.

### A structural member shows visible camber or sweep not accounted for in the layout
- **Usually means:** the final assembly will bow or twist once fully welded unless the curvature is compensated for during fit-up.
- **First question:** was this member's curvature actually measured and deliberately oriented, or assumed straight?
- **Data to pull:** the incoming material inspection record or camber measurement for that member.

### The fitter compensates for an out-of-tolerance gap by asking the welder to "just fill it" rather than correcting the fit
- **Usually means:** a weld outside the qualified WPS parameters, and an unrecorded deviation from the intended procedure.
- **First question:** does the fit-up sign-off record match the actual as-welded joint condition?
- **Data to pull:** the fit-up sign-off record compared against the actual joint as welded.

### Layout dimensions are taken from a drawing revision that doesn't match the current issued revision
- **Usually means:** fabrication is proceeding against superseded information.
- **First question:** what revision is actually referenced on the shop floor versus what's currently issued?
- **Data to pull:** the drawing revision log compared against the revision in use at the fabrication station.

### An assembly's two diagonal measurements (racking check) differ by more than the project's stated squareness tolerance
- **Usually means:** the structure is out of square even if every individual member's length measures correctly.
- **First question:** what do both diagonal measurements actually read, and by how much do they differ?
- **Data to pull:** tape measurements of both diagonals across the assembly.
