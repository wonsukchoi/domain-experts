# Vocabulary

### Datum
A theoretically exact reference point, line, or surface from which the dimensions of features are established, per the part's engineering drawing.
**In use:** "Every hole on this print is dimensioned from Datum A — that's what we measure from, not the previous hole."
**Common misuse:** Choosing a "datum" based on what's convenient to clamp or measure from rather than what the print actually specifies — the print's designated datum reflects the part's functional reference, and substituting a different, more convenient surface can produce a part that's accurate relative to the wrong reference.

### Chained (sequential) measurement
A layout method where each feature is measured and marked relative to the previously marked feature, rather than independently from a fixed datum.
**In use:** "That's a chained layout — Hole 4's position depends on Holes 1 through 3 all being marked exactly right, which is exactly the risk we're avoiding by referencing from Datum A instead."
**Common misuse:** Assuming chained measurement is simply a different but equally valid method — chaining causes small errors at each step to accumulate progressively, producing a larger cumulative error at the far end of the chain than datum-referenced measurement of the same features would produce.

### Machining allowance (stock allowance)
Extra material intentionally left beyond a layout's marked line, accounting for material that will be removed in a subsequent operation (grinding, finishing) before the part reaches its final specified dimension.
**In use:** "This line's marked with a sixteenth of an inch allowance — final grind brings it down to the true finished dimension."
**Common misuse:** Marking directly to the blueprint's finished dimension when a subsequent finishing operation is planned — without the allowance, the part ends up undersized once that operation removes material.

### GD&T (Geometric Dimensioning and Tolerancing)
A symbolic system (per ASME Y14.5 and related standards) for specifying a part's allowable variation in form, orientation, and location relative to its datums, more precise than simple linear dimensions alone.
**In use:** "Check the GD&T callouts, not just the linear dimensions — the datum reference frame tells you exactly what this feature's position is measured relative to."
**Common misuse:** Reading only the linear dimension numbers on a print without checking the GD&T datum reference frame — the same numeric dimension can mean something different depending on which datum(s) it's actually referenced from.

### Layout dye (machinist's blue)
A thin, opaque coating (typically blue or red) applied to a metal surface before scribing, providing contrast so scribed lines are clearly visible against the base material.
**In use:** "Dye's not fully covering this corner — recoat before scribing, or that line's going to be hard to read accurately."
**Common misuse:** Treating dye application as a purely cosmetic step rather than one that directly affects scribing accuracy — uneven or thin dye coverage can cause a scribe line to skip, blur, or be misread, introducing an error that isn't visible by looking at the finished mark alone.

### Surface plate
A flat, precisely machined reference surface (typically granite or cast iron) used as the base reference for precision layout and measurement work.
**In use:** "Wipe the surface plate down before setting the part on it — any debris underneath throws off every measurement referenced from it."
**Common misuse:** Assuming a surface plate stays accurate and clean by default without periodic checking — debris, damage, or wear on the plate itself introduces error into every layout performed on it, invisibly, until something doesn't fit downstream.

### Thermal expansion (in precision layout)
The dimensional change a workpiece or measuring tool undergoes due to temperature difference from the reference calibration temperature (commonly 68°F/20°C), which becomes significant on tight-tolerance work.
**In use:** "That part just came off the mill, still warm — letting it sit to room temperature before we lay out the tight-tolerance holes."
**Common misuse:** Ignoring thermal state on tight-tolerance work because the part and tools "look" ready — a real, calculable dimensional error can exist from thermal mismatch even when nothing about the setup looks obviously wrong.

### Edge finder / center finder
Precision tools used to accurately locate a workpiece's edge or center relative to a machine or measuring instrument's coordinate system, establishing a reliable starting reference point.
**In use:** "Used the edge finder to establish true zero on Datum A before starting any of the hole layout."
**Common misuse:** Estimating a starting reference point visually or by feel instead of using an edge/center finder — a slightly-off starting reference propagates its error into everything subsequently measured from it.

### Height gauge
A precision instrument used on a surface plate to measure and mark vertical dimensions accurately, often used to transfer or verify layout dimensions from a fixed reference.
**In use:** "Zeroing the height gauge against the standard before we start — a small zero error here would apply to every mark we make from it."
**Common misuse:** Trusting a height gauge's reading without verifying it's properly zeroed against a known standard — an unverified zero error is a systematic offset that, while less damaging than a chained/compounding error, is still a real inaccuracy worth catching before it's built into an entire layout.

### Functional reference surface
The specific surface or feature of a part that actually determines how it mates, aligns, or is measured in its real end-use application — the basis a datum selection should trace back to.
**In use:** "The bolt pattern needs to be laid out from the mounting face, because that's the functional reference surface in the actual assembly — not the rough-cut edge that's easiest to clamp against."
**Common misuse:** Selecting a datum based on which surface is easiest to clamp or measure from in the shop, without checking whether that surface is actually the part's functional reference — a part can be dimensionally accurate relative to the wrong reference and still fail to fit or function in its actual application.
