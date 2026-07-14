# Red flags

### Placed image resolution below 300 dpi at final print size
- **Usually means:** the source image was captured or supplied at a lower resolution than the placement size requires, or was scaled up in the layout program without adding real detail.
- **First question:** what is the image's actual pixel dimension versus its placed size on the page?
- **Data to pull:** the image file's native pixel dimensions, the layout's placement scale percentage.

### File supplied in RGB for a job printing CMYK
- **Usually means:** the file originated in a screen-first design tool without a print-specific export step.
- **First question:** has this file been through any color conversion yet, or is it still in its original color space?
- **Data to pull:** the file's embedded color profile metadata, the job's specified press/paper profile.

### Zero or insufficient bleed margin against the job's trim specification
- **Usually means:** the file was built to trim size only, without accounting for mechanical trimming tolerance.
- **First question:** what bleed dimension does this job's trim/finishing spec require, and what does the supplied file actually measure?
- **Data to pull:** the job ticket's bleed requirement, the supplied file's actual page dimensions.

### Small black text or fine lines built as a rich-black CMYK combination
- **Usually means:** the file was built using a default "black" swatch that isn't pure K, common when a design tool's default black setting wasn't checked.
- **First question:** is this a large solid black area (where rich black may be intentional) or small text/fine lines (where it risks registration fringing)?
- **Data to pull:** the specific ink build values (C/M/Y/K percentages) on the flagged element.

### A color-critical job approved from a screen preview with no contract proof generated
- **Usually means:** time pressure or an assumption that "the file looks right" skipped the standardized proofing step.
- **First question:** does this job's color sensitivity (brand colors, skin tones, critical photography) actually require a contract proof, or is a soft proof genuinely sufficient for this job type?
- **Data to pull:** the job's color-criticality classification, prior proofing requirements for this client/job type.

### A generic or default ICC profile applied instead of the press/paper-specific profile
- **Usually means:** the RIP or conversion software's default setting wasn't overridden for this specific press and stock combination.
- **First question:** what profile does this specific press and paper stock require, and what was actually applied?
- **Data to pull:** the job ticket's specified press/paper combination, the conversion log showing which profile was applied.

### A file changed after proof approval, with the changed file routed directly to plate output
- **Usually means:** a late correction was made and assumed "minor enough" to skip a new proofing cycle.
- **First question:** does the file sent to plate match, byte-for-byte or version-for-version, the file the client actually approved?
- **Data to pull:** the approved proof's file version/timestamp, the plate-output file's version/timestamp.

### Trapping applied uniformly across all color boundaries in a design
- **Usually means:** a default trapping setting was used without evaluating which specific color combinations and press tolerances actually needed it.
- **First question:** which color boundaries in this design actually have registration risk given this press's typical tolerance?
- **Data to pull:** the press's documented registration tolerance, the specific ink combinations at each trapped boundary.

### Fonts not embedded or outlined in a file headed to an external RIP or plate vendor
- **Usually means:** the file was exported without confirming font embedding, risking a font substitution at output.
- **First question:** does the export format (PDF, in this case) show all fonts as embedded or converted to outlines?
- **Data to pull:** the file's font-embedding status in the preflight report.

### Overprint settings left at a design tool's default rather than set per the job's actual ink layering needs
- **Usually means:** a knockout-vs-overprint decision defaulted to the software's setting rather than being made deliberately for this job's color combinations.
- **First question:** which elements in this design are set to overprint, and is that intentional for this specific color layering?
- **Data to pull:** the overprint preview/simulation output, the design's intended layering (which element should sit visually on top).
