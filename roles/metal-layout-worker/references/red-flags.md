# Red flags

### Multiple features marked by measuring each from the previously marked feature
- **Usually means:** a chained measurement approach is being used instead of referencing every feature from the established datum, risking compounding error.
- **First question:** does the print specify datum-relative or mate-relative dimensions for these features?
- **Data to pull:** the print's dimensioning scheme, the actual measurement method used for each marked feature.

### A layout marked directly to the blueprint's finished dimension with no machining allowance
- **Usually means:** the layout didn't account for material that will be removed in a subsequent operation (grinding, finishing).
- **First question:** does this part require further machining after this layout stage, and if so, what allowance does that require?
- **Data to pull:** the part's process routing (what operations follow this layout stage), the specified machining allowance.

### A datum selected for clamping/measuring convenience without checking the part's functional reference
- **Usually means:** the layout may produce a part that passes inspection at this stage but doesn't fit or function correctly in its actual application.
- **First question:** does the chosen datum match the surface the part actually mates from or is measured against in service?
- **Data to pull:** the print's specified datum, the part's functional mating/reference surface.

### Layout dye applied unevenly or a work surface with visible debris before scribing
- **Usually means:** the layout accuracy may be compromised in a way that won't be visible in the finished marks.
- **First question:** has the surface been cleaned and dye application verified even before marking begins?
- **Data to pull:** surface preparation record if one exists, visual/tactile check of dye coverage and surface cleanliness.

### Precision measurement taken immediately after a tool or workpiece was moved from a different thermal environment
- **Usually means:** thermal expansion/contraction hasn't equalized, introducing a real dimensional error on tight-tolerance work.
- **First question:** have the tool and workpiece both been given time to reach room/reference temperature before this measurement?
- **Data to pull:** time elapsed since the tool/workpiece was last in a different thermal environment, the tolerance being held.

### A layout error discovered partway through marking, followed by an "adjustment" to remaining marks
- **Usually means:** the discovered error is being compensated for rather than corrected at its source, risking a different kind of compounding error.
- **First question:** was the datum re-verified and marking restarted from it, or were remaining marks adjusted to compensate for the discovered error?
- **Data to pull:** the sequence of actions taken after the error was found, whether the datum itself was re-checked.

### A height gauge or precision measuring tool used without a recent zero/calibration check
- **Usually means:** a systematic offset error could be present and would apply to every measurement taken with that tool.
- **First question:** when was this specific tool last zeroed/verified against a known standard?
- **Data to pull:** tool calibration/verification log, date of last check.

### A layout for a part with tight tolerances performed without stating which datum was actually used
- **Usually means:** inspection or the downstream machinist may reference a different datum than the one actually used for layout, producing a mismatch.
- **First question:** does the layout documentation explicitly state which datum was used for every marked feature?
- **Data to pull:** layout documentation/notes, print's specified datum scheme.

### Two layout workers' marks on the same part showing inconsistent reference points
- **Usually means:** different datums or measurement methods were used by each, rather than a shared, consistent approach.
- **First question:** did both workers reference the same datum using the same method, or did each establish their own?
- **Data to pull:** each worker's layout notes, the print's specified single datum scheme.

### A layout mark that doesn't visually align with an expected symmetric or repeating pattern on the part
- **Usually means:** a possible datum, allowance, or chained-measurement error, worth verifying before cutting proceeds.
- **First question:** does re-measuring this specific feature from the datum confirm or contradict the marked position?
- **Data to pull:** re-measurement from the established datum, comparison to the print's specified position.
