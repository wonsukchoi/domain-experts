# Desktop Publisher — Red Flags

### Placed image at effective resolution below 300 DPI (or below the printer's stated minimum)
- **Usually means:** Native file resolution was correct at the size it was originally specced for, but the image was later enlarged in the layout without recomputing effective DPI at the new placed size.
- **First question:** What is the image's native pixel dimension, and what is its actual placed size right now — not what the asset brief said when it was supplied?
- **Data to pull:** Image native pixel dimensions and current placed width/height from the layout file's link/image panel.

### Bleed element stops exactly at the trim line with no extension past it
- **Usually means:** The element was placed to visually match the trim size shown on-screen without extending it into the bleed area, or the bleed guide wasn't set up before placement began.
- **First question:** Does this element touch or cross the trim edge, and if so, does it extend the full bleed spec (commonly 0.125 in) past that edge on every side it touches?
- **Data to pull:** The printer's spec sheet bleed value; the element's actual extension past trim in the layout file.

### A font shows as "missing" or "not embedded" in the export/preflight report
- **Usually means:** The font isn't installed on the machine doing the export, or the font's license doesn't permit embedding in a distributable PDF.
- **First question:** Is this a licensing restriction (needs a substitute or a licensed-embedding version) or a missing-installation issue (needs the font installed before re-export)?
- **Data to pull:** The font's license terms for embedding; whether the font is installed on the export machine.

### RGB color mode on an image or element in a file destined for offset/digital press
- **Usually means:** A supplied asset was never converted from its RGB source (photos, web graphics) to the print color space, or the layout file's color settings default to RGB.
- **First question:** Has this image been converted to CMYK under our control, or will the printer's RIP do an uncontrolled conversion on their end?
- **Data to pull:** Image color mode (checked directly in the layout software's image info, not assumed from the file source).

### A single-line widow or orphan at a page or column break
- **Usually means:** Body copy was written or edited without checking how it breaks across the current layout, or a late copy edit shifted a line count without a re-check.
- **First question:** Can this be fixed with tracking or hyphenation adjustment, or does the copy itself need to be shortened or lengthened by a line?
- **Data to pull:** The specific line and the paragraph's full copy, to evaluate tracking/hyphenation/rewrite options.

### Live text or a critical graphic element sits inside the safe-area margin (close to trim)
- **Usually means:** Content was placed against the trim guide rather than the safe-area guide, ignoring that commercial cutting has real tolerance.
- **First question:** How close is this element to the trim edge, and is it inside the safe-area inset (commonly 0.25 in)?
- **Data to pull:** Element position relative to trim edge and the printer's stated safe-area spec.

### A style-sheet or master-page edit was made after most pages were already laid out
- **Usually means:** A late design change (e.g., a heading style or column width) was applied globally without checking every page that uses it for a resulting overflow or misalignment.
- **First question:** Which pages use this style/master, and has each been re-checked since the edit?
- **Data to pull:** List of pages referencing the edited style or master page.

### The exported print-ready file hasn't been separately verified from the working layout file
- **Usually means:** The team is trusting that "the layout looked right" is the same as "the exported PDF is correct" — export settings (color profile, resolution downsampling, font embedding) are a separate failure point from the layout itself.
- **First question:** Has the actual exported file been opened and checked, not just the working file?
- **Data to pull:** The exported PDF's preflight report (color mode, embedded fonts, image resolution as exported).
