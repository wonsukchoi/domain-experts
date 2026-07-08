# Red flags

### Hole pattern dimensioned with ± coordinate tolerances instead of true position
- **Usually means:** the drafter defaulted to linear dimensioning habit instead of GD&T, or is copying an older legacy drawing forward without updating the tolerancing scheme.
- **First question:** what's the actual mating fastener and clearance — does a square tolerance zone under- or over-constrain relative to the round functional interface?
- **Data to pull:** the mating part's fastener clearance-hole diameter and the functional gage (if one exists) used to check the pattern.

### Worst-case stack-up exceeds spec by any margin, even 0.001"
- **Usually means:** one or more links in the chain were toleranced independently without checking the reconciled total against the functional requirement.
- **First question:** which single link carries the highest leverage (largest tolerance ÷ total worst-case tolerance), and can that one be tightened within the existing process's capability?
- **Data to pull:** the full stack-up worksheet (nominal, tolerance, sign per link) and the process capability (Cpk) data for the highest-leverage link if RSS is being considered instead.

### GD&T position callout with no modifier (MMC/RFS/LMC) specified
- **Usually means:** the drafter defaulted to RFS by ASME Y14.5 convention without evaluating whether the interface would benefit from bonus tolerance at MMC.
- **First question:** is this a clearance-fit interface (bolt through a clearance hole) where bonus tolerance is functionally free, or a precision locating feature where it isn't?
- **Data to pull:** the mating fastener/pin size and the nominal clearance between fastener and hole at MMC.

### Drawing has no projection-angle symbol
- **Usually means:** the drafter's CAD template defaulted the symbol off, or the drawing was copied from a source using the other convention without re-verification.
- **First question:** is this drawing going to an ISO/European fabricator (first-angle expected) or a US/ASME shop (third-angle expected), and does the part have any feature whose mirrored placement would actually matter (asymmetric geometry)?
- **Data to pull:** the customer's or supplier's drawing standard requirement (often stated in a PO or supplier quality agreement).

### Surface finish called out finer than 0.8 µm Ra on a static, non-sealing surface
- **Usually means:** the drafter over-specified "to be safe" without checking whether the surface is dynamic, sealing, or load-bearing.
- **First question:** does this surface slide, seal a dynamic interface, or carry a rolling/sliding load — or is it just a face that bolts to another face and never moves?
- **Data to pull:** the assembly section view showing what mates to this surface and whether relative motion exists across it.

### BOM item number reused across a design revision that changes form, fit, or function
- **Usually means:** a revision was treated as a minor edit when it actually broke interchangeability with previously shipped stock.
- **First question:** would an old-rev part, installed today, still meet the functional spec — dimensionally, materially, and in fit?
- **Data to pull:** the revision's engineering change order (ECO) description and the specific dimensions or materials it altered.

### Datum reference frame references a feature that isn't how the part is actually held in the machine or fixture
- **Usually means:** datums were picked for drawing convenience (a visually obvious face) rather than by matching the actual fixturing/assembly sequence.
- **First question:** when this part sits in the mill vise or the assembly fixture, which face contacts first, second, third — does that match datum A, B, C on the drawing?
- **Data to pull:** the shop's fixture drawing or setup sheet, if one exists, or a conversation with the machinist about how the part is actually held.

### Dimension is doubly defined — both explicitly toleranced and covered by the title-block general tolerance
- **Usually means:** a dimension was explicitly toleranced during a redline pass without checking whether it duplicates or conflicts with the general tolerance block.
- **First question:** do the two stated tolerances agree, and if they don't, which one governs on this drawing (usually the explicit callout, but confirm the title block's stated precedence note)?
- **Data to pull:** the general tolerance block text and the specific dimension's explicit tolerance, side by side.

### Assembly drawing balloon has no corresponding BOM row, or a BOM row has no balloon
- **Usually means:** a part was added or removed from the assembly late and the BOM/balloon set wasn't re-synced.
- **First question:** was the last edit to this assembly a geometry change, a BOM edit, or both — and did both actually get touched?
- **Data to pull:** the assembly drawing's balloon list against the BOM table, row by row.

### RSS stack-up is cited as the sole justification for a spec that fails worst-case
- **Usually means:** RSS was used to make a marginal design "pass" without process-capability evidence to support the statistical assumption.
- **First question:** is there a Cpk study (or equivalent SPC data) for every link in the chain supporting the independence and normal-distribution assumption RSS requires?
- **Data to pull:** the process capability report for each toleranced dimension in the chain, or, absent that, treat the design as worst-case-only until it exists.

### Sheet-metal part dimensioned without a bend-relief or K-factor note
- **Usually means:** the part was modeled as a solid and flattened without carrying forward the bend allowance the fabricator needs to verify the flat pattern.
- **First question:** does the flat-pattern dimension on the drawing match what the fabricator's brake and material thickness would actually produce?
- **Data to pull:** the material thickness, bend radius, and K-factor (or bend-deduction table) used to generate the flat pattern.
