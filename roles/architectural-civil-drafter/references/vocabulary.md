# Vocabulary

Terms generalists flatten together that an architectural/civil drafter keeps sharply separate — the value is in the misuse, not the definition.

## Model space vs. paper space

**Model space** holds the drawing at full, real-world scale (1:1) — every wall, curb, and contour drawn at its actual size. **Paper space** is a sheet-composition layout where one or more viewports display model space through a scale factor, with the title block, sheet border, and general notes living in paper space itself, not model space.

**In use:** "Draft the addition in model space at full scale — we'll set the viewport scale on the paper space sheet once the geometry's done."

**Common misuse:** drawing geometry pre-scaled down in model space to match the intended paper size, which corrupts every downstream area takeoff, dimension auto-text, and xref alignment that assumes real-world coordinates.

## Viewport scale factor

The ratio between paper space and model space in a given viewport, computed as 12 ÷ (scale fraction) for inch-based architectural model space or as the feet value directly for foot-based civil model space. Distinct from the "scale" printed on the sheet (e.g., "1/4"=1'-0""), which is the human-readable label the scale factor produces.

**In use:** "This viewport's set to SF 48 for the 1/4-inch plan — don't touch it without recomputing every text height and hatch scale on the sheet to match."

**Common misuse:** applying the architectural inches-based formula to a civil, feet-based model space (or vice versa), producing a viewport 12x off from intended.

## Annotative scale

An AutoCAD object property that lets a single text, dimension, or hatch object display at the correct plotted size across multiple viewports set to different scales, without maintaining separate copies of the object per scale. Distinct from manually setting model-space text height per scale factor, which requires a separate calculation (and often a separate object) for each scale in use.

**In use:** "Make the general notes annotative so they read correctly whether they're shown on the 1/4-inch plan or the 1-inch detail blowup — one object, two displayed sizes."

**Common misuse:** assuming annotative scale is automatically enabled project-wide; an object created without the annotative property still needs its height manually set per the scale factor of whichever viewport displays it.

## Discipline designator (NCS)

The single letter prefixing a sheet number under the National CAD Standard, identifying which discipline authored the sheet — G (general), C (civil), A (architectural), S (structural), M/E/P (mechanical/electrical/plumbing), among others. Distinct from the sheet-type digit that follows the dash, which further classifies the sheet within that discipline (plans, elevations, details).

**In use:** "That grading detail belongs on a C-5xx sheet, not an A-5xx sheet — civil discipline, details sheet type."

**Common misuse:** treating the designator letter as arbitrary or firm-specific, when it's a national standard other consultants and the AHJ expect to read without explanation.

## AIA/NCS layer status suffix

The trailing letter on an NCS-format layer name (`A-WALL-FULL-N`) indicating construction phase: N (new), E (existing to remain), D (to be demolished), F (future, outside this contract). Distinct from the Major/Minor fields preceding it, which identify *what* the element is rather than *when* it exists in the project.

**In use:** "Check the status suffix before you draft that wall — if the demo plan calls it 'to remain,' it needs the -E suffix, not -N, or the GC's takeoff software will price it as new work."

**Common misuse:** copying an element's layer assignment forward from a prior phase without updating the status suffix to match the current redline's phasing call-out.

## CTB vs. STB (plot style tables)

A **CTB** (color-dependent plot style table) maps AutoCAD's 255 built-in color numbers to plotted properties like lineweight — any object drawn in that color inherits the mapped weight. An **STB** (named/style-dependent plot style table) assigns plot properties to a named style applied directly to objects or layers, independent of the object's color. Most US AEC firms use CTB; STB is more common where color needs to remain purely visual (e.g., matching a client's screen-display standard).

**In use:** "This project's on a CTB workflow — reassign the wall cut lines to color 1, don't add a lineweight override on the object."

**Common misuse:** applying a per-object lineweight override in a CTB-based project instead of fixing the color-to-weight mapping, which means a firm-wide standards change never fully propagates.

## Xref (external reference) — attached vs. overlaid vs. bound

An **xref** links a separate drawing file into the current one without copying its geometry in. **Attached** xrefs display their own nested xrefs (chain further); **overlaid** xrefs don't, and are the common choice to avoid circular references between disciplines sharing a background. **Binding** converts a linked xref into permanent, embedded geometry — required before external transmittal so the recipient isn't dependent on the original file path.

**In use:** "Bind and clean the xrefs before this set goes out to the GC — an overlaid reference is fine internally, but it breaks the moment they don't have our server path."

**Common misuse:** issuing a final external set with xrefs still attached or overlaid rather than bound, so the file silently breaks (or shows nothing) once the source path is inaccessible.

## Delta / revision cloud

A **delta** is the small numbered or lettered symbol (often a triangle) marking a specific changed item on a sheet, cross-referenced to the **revision block**, a table in the title block logging each revision's number, date, and description. A **revision cloud** is the scalloped-line boundary drawn around the changed area, containing the delta symbol.

**In use:** "Cloud the relocated door and tag it delta 3 — log delta 3 in the revision block with today's date before this goes back out."

**Common misuse:** making a post-approval edit without a cloud or revision-block entry, which erases the record of what was actually reviewed and approved versus changed afterward.

## Stationing (civil alignments)

A linear-referencing system along a civil alignment (road centerline, pipe run, etc.), written `##+##.##` and read as (station number x 100) plus the offset in feet from a defined point of beginning. A **station equation** notes a deliberate discontinuity where two survey segments were joined without renumbering.

**In use:** "The culvert centerline crosses the road alignment at Sta. 6+42.50 — pull the invert elevation from the profile sheet at that station, not by scaling off the plan."

**Common misuse:** treating station numbers as if they were a distance from the project's overall origin rather than from that specific alignment's point of beginning, which breaks down the moment two alignments (e.g., a road and a utility run) are compared directly.

## Vertical datum (NGVD29 vs. NAVD88)

The fixed reference surface a civil elevation is measured from. **NGVD29** is the older US vertical datum; **NAVD88** is the current standard. The offset between them at a given site is not a fixed national constant — it varies by location and must be looked up, not assumed.

**In use:** "Confirm which datum the original topo survey used before comparing it to our NAVD88 grading plan — if it's NGVD29, we need the site-specific conversion offset first."

**Common misuse:** comparing or combining elevations from two datums without converting, producing an apparent discrepancy that isn't a survey error at all.

## Contour interval vs. spot elevation

A **contour interval** is the constant vertical distance between contour lines on a topographic drawing (commonly 1, 2, or 5 ft depending on site relief) — it shows overall grade shape at a fixed precision. A **spot elevation** is a single point value, typically to 0.01 ft, called out where the contour interval alone isn't precise enough (a doorway threshold, a drainage inlet).

**In use:** "The 2-foot contours show the general slope, but pull the actual spot elevation at the inlet — that's the number the drainage calc needs."

**Common misuse:** reading a precise value off an interpolated contour line instead of calling out or requesting an actual spot elevation where precision matters.

## Face-of-stud vs. centerline dimensioning

**Face-of-stud** (or face-of-CMU) dimensioning measures to the actual finished framing surface — the convention for construction documents, because it's what the framer or mason builds to. **Centerline** dimensioning measures to a wall's theoretical centerline — faster to draft and common on schematic or diagrammatic sheets, but ambiguous for actual construction since it doesn't specify which side of the wall the stated dimension resolves to.

**In use:** "This is a CD set, not a schematic — dimension to face-of-stud like the general notes specify, not centerline."

**Common misuse:** mixing the two conventions on the same construction-document sheet without a note explaining which strings use which, leaving the framer to guess.

## RFI (request for information)

A formal, logged question routed from the drafter (or contractor) to the architect or engineer of record when a redline, spec, or field condition is ambiguous or contradictory — distinct from an informal redline markup, which is direction already given, not a question being asked.

**In use:** "The grading plan's pad elevation doesn't match the architectural finished-floor elevation — that's an RFI to both EORs, not something to resolve by picking the one that looks newer."

**Common misuse:** treating an RFI as a delay to avoid, so an ambiguity gets silently resolved by drafter judgment instead of formally routed — which moves a design decision onto someone without the authority to make it.

## As-built vs. record drawing

An **as-built** drawing is field-marked during construction to show what was actually built where it deviated from the issued set — typically the contractor's redlines. A **record drawing** is the cleaned-up, formally drafted final version incorporating those as-built changes, issued as the permanent project record.

**In use:** "Don't issue the contractor's as-built markups directly as the record set — draft them into a clean record drawing first, with the deviations noted."

**Common misuse:** using "as-built" and "record drawing" interchangeably, when the as-built is raw field input and the record drawing is the finished, verified deliverable built from it.
