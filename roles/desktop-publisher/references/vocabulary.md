# Desktop Publisher — Vocabulary

### DPI (dots per inch) vs. PPI (pixels per inch)
DPI technically refers to a printer's physical ink-dot output resolution; PPI refers to an image file's pixel density. In practice the two terms are used interchangeably in most print-production conversation, but the number that matters for preflight is effective PPI at placed size.
**In use:** "This image is 120 effective DPI at the size you've got it placed — it needs to be closer to 300."
**Common misuse:** Treating a file's native resolution (as stated in its metadata or the original asset brief) as fixed and permanent, without recomputing it against the image's actual current placed size in the layout.

### Bleed
Content that extends past the trim line, so that any tolerance in the physical cutting process doesn't leave an unwanted white sliver at the edge. Commonly specified as 0.125 in (US) or 3 mm past trim.
**In use:** "Extend that background color 0.125 inches past the trim on all four sides — it's a full-bleed page."
**Common misuse:** Assuming bleed means "make the file bigger" generally, rather than a precise extension of specific edge-touching elements past a specific trim line by a specific spec'd amount.

### Trim size vs. safe area
Trim size is the final cut dimension of the page. Safe area is an inset margin (commonly 0.25 in) inside the trim line, inside which no critical content should sit, because cutting tolerance can shift the actual cut line slightly.
**In use:** "Keep the page numbers inside the safe area — they're too close to trim right now."
**Common misuse:** Treating trim size as the boundary for where content can safely sit, when it's actually the boundary for where the page physically ends — safe area is the real working boundary for anything that must not be at risk of getting cut off.

### Widow and orphan
A widow is a single short line or word left alone at the top of a new page or column. An orphan is a single line stranded alone at the bottom of a page or column, separated from the rest of its paragraph. Style guides commonly prohibit both.
**In use:** "There's a widow on page 6 — 'the results.' is sitting alone at the top of the next column."
**Common misuse:** Confusing which term applies to which position (top vs. bottom), or treating the fix as always being a font-size or leading adjustment rather than considering tracking, hyphenation, or a copy-length edit first.

### Kerning vs. tracking
Kerning adjusts the space between two specific letter pairs. Tracking adjusts the spacing uniformly across a run of text (a word, line, or paragraph).
**In use:** "Tighten the tracking on that headline half a point — it's running wide."
**Common misuse:** Using the terms interchangeably; they operate at different scopes and a fix appropriate for one (a single awkward letter pair) is the wrong tool for the other (an entire line running long or short).

### Leading
The vertical space between baselines of consecutive lines of text, historically named for the strips of lead once used to add spacing in metal typesetting. Commonly expressed as a value larger than the font's point size (e.g., 10 pt type on 12 pt leading, often written "10/12").
**In use:** "Body copy is set 9 on 11.5 — bump the leading if it feels cramped."
**Common misuse:** Confusing leading with font size, or assuming tighter leading always saves space without checking that it hasn't crossed into hurting readability.

### CMYK vs. RGB
CMYK (cyan, magenta, yellow, key/black) is the subtractive color model used in most commercial print processes. RGB (red, green, blue) is the additive model used for screens. RGB has a wider color gamut than CMYK process printing can reproduce.
**In use:** "Convert those product photos to CMYK before final placement — don't let the printer's RIP do an uncontrolled conversion."
**Common misuse:** Assuming a color looks the same on screen (RGB) as it will print (CMYK) without a soft-proof or a physical proof — saturated blues, greens, and some oranges shift the most in conversion.

### Preflight
The pre-submission check of a print-ready file against a printer's technical spec (resolution, color mode, bleed, font embedding, page count/size) before sending it to press.
**In use:** "Preflight caught a resolution problem on the back cover — sending the client a note before we submit."
**Common misuse:** Treating preflight as a final one-time gate run only right before submission, rather than a standard checked continuously as content changes throughout the project.

### PDF/X
A family of ISO-standardized PDF subsets (e.g., PDF/X-1a, PDF/X-4) designed specifically for reliable print-file exchange — they constrain what can be in the file (fonts embedded, specific color-space rules) to reduce the chance of a printer-side surprise.
**In use:** "Export as PDF/X-1a per the printer's spec sheet, not a standard PDF."
**Common misuse:** Treating "PDF" as a single uniform format for print submission — a standard PDF export and a PDF/X-compliant export can differ significantly in what's guaranteed about fonts, color, and transparency handling.

### Grid system
A structural framework of columns, gutters, margins, and baseline spacing that governs where content can be placed across a multi-page document, set up before content placement begins.
**In use:** "We're on a 3-column grid with a 12pt baseline — keep new content snapped to it."
**Common misuse:** Treating the grid as a suggestion to reference loosely rather than a constraint to place content precisely against — inconsistent adherence is what produces the visibly misaligned-margins problem a grid exists to prevent.

### Master page
A template page in layout software that defines recurring elements (headers, footers, page numbers, background) automatically applied to every page linked to it; editing the master edits every linked page at once.
**In use:** "That footer typo is on the master page — fixing it once will fix all 24 pages."
**Common misuse:** Forgetting that a master-page edit is global, and not re-checking pages that might react differently to the change (e.g., a page where content already runs close to where the footer sits).
