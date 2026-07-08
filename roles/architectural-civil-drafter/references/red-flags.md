# Red flags

Smell tests an architectural/civil drafter catches in the first pass over a redline, a drafted sheet, or a set headed for issuance.

### Footprint plots within 0.5" or less of the sheet's usable drawing area at the directed scale

- **Usually means:** the scale was locked in on a raw geometry-fit check without budgeting clearance for dimension strings, notes, and a key plan.
- **First question:** after dimension strings, general notes, and a north arrow/key plan are placed, does the sheet still read cleanly, or is text overlapping the border?
- **Data to pull:** usable-area calculation (sheet size minus border and title block), footprint dimensions, a scale one increment down for comparison.

### Model-space text height wasn't recomputed after a scale factor change

- **Usually means:** geometry was rescaled but the annotation objects — general notes, dimension text, tick marks, hatch scale — were copied forward from the old scale factor.
- **First question:** does plotted text height still measure the firm's standard 3/32" (0.09375") at 100% plot, or does it read a different size than the rest of the set?
- **Data to pull:** the old and new scale factors, the model-space text height value on the affected objects, the plotted-size target from the firm CAD standard.

### Layer status suffix doesn't match the redline's phasing call-out (e.g., `-N` used for an existing-to-remain element)

- **Usually means:** the drafter copied an existing block/layer forward without updating the status suffix, or misread the redline's demo/existing/new call-out.
- **First question:** what does the redline explicitly say about this element's phase — new, existing to remain, or to be demolished?
- **Data to pull:** the phasing redline or demo plan, the current layer assignment, the AIA/NCS status-suffix key.

### Xref shows as attached-overlay, not bound, on a set about to be issued externally

- **Usually means:** the drafter forgot the final bind-and-clean step before transmittal, common when a set is rushed near a deadline.
- **First question:** will the recipient's CAD environment have access to the same file paths this xref currently points to?
- **Data to pull:** the xref manager panel (attach type per reference), the transmittal's file list, the project's external-issuance checklist.

### Revision cloud present on a sheet with no corresponding entry in the revision block

- **Usually means:** an edit was made after a review round without going through the formal revision-tracking step — often a "quick fix" that skipped the process.
- **First question:** was this change reviewed and approved, or is it an unreviewed edit riding along with an approved sheet?
- **Data to pull:** the revision block/history, the review markup set the cloud should trace back to, the date of the last approved issuance.

### Combined arch/civil sheet set has a viewport scale factor that doesn't match either convention's formula

- **Usually means:** an inch-based architectural scale factor formula (12 ÷ fraction) was applied to a civil, foot-based model space, or vice versa — a 12x scale error.
- **First question:** what is this drawing's base unit setting (inches or feet), and does the applied scale-factor formula match that convention?
- **Data to pull:** the file's unit setting (`INSUNITS` or equivalent), the stated scale, the computed scale factor, a second reference viewport at a known-correct scale for comparison.

### Civil elevation or benchmark cited without a stated vertical datum

- **Usually means:** the value was copied from an older survey (commonly NGVD29) without carrying forward which datum it references, or the datum was simply omitted.
- **First question:** does this elevation match NAVD88 or NGVD29, and does every other elevation on this sheet reference the same datum?
- **Data to pull:** the source survey's datum statement, NGS datum-conversion offset for the site's location, other benchmarks on the same sheet set for a consistency check.

### Cut/fill volume reported to a precision finer than the coarser of the two contour intervals feeding it

- **Usually means:** a volume calculation ran on a TIN surface built from mismatched-interval source data (e.g., 1 ft existing survey vs. 2 ft proposed grading) without flagging the precision limit.
- **First question:** what contour interval does each source surface actually carry, and does the reported volume's precision reflect the coarser one?
- **Data to pull:** both source surfaces' stated contour intervals, the TIN/volume computation report, the existing-conditions survey date.

### Stationing shows a gap or overlap at an alignment splice with no station equation noted

- **Usually means:** two survey segments were joined without reconciling their independent station numbering, producing an apparent length discrepancy.
- **First question:** does a station equation note exist at this point, and does it account for the full discrepancy?
- **Data to pull:** the alignment's station-equation notes, both source surveys' station numbering at the splice point, the total alignment length by direct measurement.

### Plot-style color assigned to a layer doesn't match the firm or project CTB/STB lineweight table

- **Usually means:** an object-level color or lineweight override was applied instead of using the layer's standard color-to-weight mapping, or the wrong color number was picked from habit on a prior project's palette.
- **First question:** what lineweight does this layer's assigned color map to in the project's actual CTB/STB file, and is that the intended weight for this element type?
- **Data to pull:** the project CTB/STB file, the layer's assigned color number, a plotted proof at 100% scale for visual comparison against adjacent elements.

### Wall assembly dimensioned to a mix of face-of-stud and centerline on the same sheet with no note explaining the switch

- **Usually means:** dimension strings were copied from a schematic sheet into a construction-document sheet without updating the dimensioning convention.
- **First question:** what does the general notes column state as the governing dimensioning convention for this sheet, and does every string on the sheet follow it?
- **Data to pull:** the sheet's general notes, a sample of dimension strings across the sheet, the project's dimensioning-standard note (often on the cover or general notes sheet).

### Sheet number doesn't follow the discipline-designator/sheet-type digit pattern the project's CAD standard specifies

- **Usually means:** the drafter defaulted to a personal or prior-project numbering habit instead of confirming which NCS version or client-specific numbering scheme this project's contract requires.
- **First question:** does the project's CAD standard document specify a sheet-numbering convention, and does this sheet number match it?
- **Data to pull:** the project's CAD standard or BIM execution plan, the sheet index, comparable sheet numbers already issued on the same project.
