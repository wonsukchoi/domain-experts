# Vocabulary

### Dot gain
The phenomenon where a printed halftone dot appears larger on the finished sheet than its specified size in the file, because ink spreads on contact with paper — magnitude varies by paper stock (uncoated stock typically shows more gain than coated).
**In use:** "This job's on uncoated stock, so we're compensating for a bigger dot gain curve than we'd use on the coated job next to it."
**Common misuse:** Treating dot gain as a fixed, universal percentage rather than a value specific to the press-and-paper combination — applying a coated-stock gain curve to an uncoated job shifts the resulting midtones off target.

### Trapping
A deliberate slight overlap applied between two abutting colors printed by different plates, to prevent a visible white gap or gap-and-halo artifact if the plates register slightly out of alignment on press.
**In use:** "We're trapping the logo's red into the background blue by a quarter point — enough to cover typical registration drift on this press without creating visible ghosting."
**Common misuse:** Applying trapping uniformly to every color boundary in a design regardless of the actual colors and press tolerance involved — over-trapping creates its own visible ghosting artifact where none was needed.

### Rich black
A black created by combining CMYK inks (e.g., a mix of cyan, magenta, yellow, and black) rather than using 100% K alone, producing a deeper, denser black on large solid areas.
**In use:** "That headline's set in rich black — fine for the big background panel, but we're flagging it for the body text, which should just be 100% K."
**Common misuse:** Using rich black indiscriminately on small text or fine lines, where any registration mis-fit between the four separate ink plates shows as visible color fringing around the letterforms.

### ICC profile
A standardized data file describing how a specific device (a monitor, a printer, a press-and-paper combination) renders color, used to convert color accurately between devices or color spaces.
**In use:** "We're converting with the press's actual characterized ICC profile for this stock, not the generic default the software ships with."
**Common misuse:** Assuming any CMYK profile produces equivalent output — a profile characterizes a specific press-and-paper combination's actual ink behavior, and using the wrong one introduces a color shift that isn't visible until the proof.

### Contract proof
A physical or standardized-digital proof produced under controlled, repeatable viewing conditions, serving as the documented, disputable basis for what a client approved before a full press run.
**In use:** "Client signed the contract proof on the 12th — that's what we're matching on press, not whatever was in the email thread."
**Common misuse:** Treating an emailed screen preview or a casual soft proof as equivalent to a contract proof — screen rendering varies by monitor and viewing conditions in ways a standardized contract proof specifically controls for.

### Bleed
Extra image or color extending beyond the trim line, added to a file so that mechanical trimming's real-world tolerance doesn't expose an unprinted edge or clip content.
**In use:** "Standard bleed on this job is an eighth inch all around — the file's coming in flush to trim with none at all."
**Common misuse:** Treating bleed as an arbitrary convention that can be skipped for a "simple" job — the trimmer's actual cut tolerance is a physical constant regardless of the job's complexity.

### Preflight
The systematic check of a file's technical readiness for print — resolution, color space, fonts, bleed, trapping/overprint settings — performed before any output.
**In use:** "Preflight caught three issues before this ever got near plate — bleed, resolution, and an RGB image."
**Common misuse:** Skipping a full preflight on a "simple" or repeat job — a font substitution, dropped bleed, or color-space change can enter a file between approved rounds without being visible at normal screen magnification.

### Overprint vs. knockout
Two ways adjacent inks can interact: overprint prints one ink directly on top of another (the layers combine); knockout removes (knocks out) the area under the top element so only the top ink prints there.
**In use:** "That yellow highlight needs to overprint the black text underneath it, not knock it out, or the text disappears."
**Common misuse:** Leaving overprint/knockout at a design tool's default setting rather than deciding it deliberately per element — the wrong setting can make an element disappear or produce an unintended color mix on press.

### CTP (Computer-to-Plate)
The process of imaging a printing plate directly from a digital file, without an intermediate film step, using a plate-setter/imagesetter.
**In use:** "Plates are going straight to CTP once the client signs off on the proof — no film step to double-check against anymore."
**Common misuse:** Assuming CTP output is inherently error-free because it skips a manual film step — CTP removes one potential error source but doesn't replace the need for preflight and proofing before the file reaches the plate-setter.

### RIP (Raster Image Processor)
The software/hardware that converts a vector/page-description file (like a PDF) into the raster (dot pattern) data a plate-setter or digital press actually outputs.
**In use:** "Check the RIP settings before this job runs — the trapping and screening values are set per press, not a universal default."
**Common misuse:** Assuming the RIP's default settings are already correct for every job — screening angle, trapping, and color conversion settings in the RIP need to match the specific job and press, not just whatever the software ships with.
