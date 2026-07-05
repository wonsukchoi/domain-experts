# Red flags — what a graphic designer notices instantly

Smell tests with thresholds. Format per flag: the signal → what it usually means → first question to ask → data to pull.

### Body text under 4.5:1 contrast against its background

- **Usually means:** an accent or brand color got promoted to a text role it was never tested for, or a background image/photo was dropped behind text without a scrim.
- **First question:** "What use case was this color approved for — was it ever checked against 4.5:1 at this size?"
- **Data to pull:** the color-and-contrast table from the guideline (see `references/artifacts.md`), and a contrast-checker reading of the exact hex pair in place.

### Large-format headline text under 3:1 contrast

- **Usually means:** the same root cause as body-text failures, but on a hero/headline application where it's more visible and more damaging to brand perception on first impression.
- **First question:** "Is this size actually ≥24px/18pt regular (or ≥19px/14pt bold) — does it even qualify for the 3:1 tier, or does it need to clear 4.5:1?"
- **Data to pull:** rendered size at final output (not the design file's nominal size, which can differ after scaling for the application).

### Logo reproduced below its documented minimum size with no simplified variant

- **Usually means:** whoever placed it didn't have the guideline, or the guideline never specified a small-size variant (single-color, simplified mark) for exactly this situation.
- **First question:** "Is there an approved minimum-size or single-color variant for this use, and does the guideline actually say so?"
- **Data to pull:** the guideline's minimum-size and incorrect-usage sections; the actual output size in the shipped asset.

### A palette with three or more colors weighted roughly equally

- **Usually means:** every color got argued into the palette by a different stakeholder and none lost, producing a system with no dominant/neutral color to anchor hierarchy.
- **First question:** "Which color is meant to dominate — walk me through the 60/30/10 split as designed."
- **Data to pull:** the palette's stated usage percentages or ratios, if any exist; if none exist, that absence is itself the finding.

### A guideline rule stated as description rather than measurement ("keep space around the logo," "use tasteful colors")

- **Usually means:** the rule was written for a portfolio audience, not a production audience, and will not survive being applied by someone outside the original design conversation.
- **First question:** "If I handed this single line to a print vendor with no other context, could they execute it identically to how I intend?"
- **Data to pull:** the specific guideline section; rewrite target is a number (clear-space unit, minimum size, exact hex/CMYK) not an adjective.

### A logo file with no minimum-size or clear-space rule at all

- **Usually means:** the guideline was finished before the flagship application was tested, so nobody hit the case that would have forced the rule into existence.
- **First question:** "What's the smallest size and busiest background this mark has actually been placed on and reviewed at?"
- **Data to pull:** a mockup of the mark at its intended smallest real-world size (app icon, receipt, small-format signage).

### Client asks to enlarge the logo without a stated distance or context

- **Usually means:** a proxy for an unstated concern — shelf-presence anxiety, competitive insecurity, or a feeling that the identity looks "small" next to internal expectations rather than actual audience-facing evidence.
- **First question:** "Enlarge it relative to what — what distance or context is it being viewed from, and has that been tested at the current size?"
- **Data to pull:** a recognition-distance test or side-by-side composite against the actual competitive or environmental context the client is reacting to.

### A print file specified only in RGB/hex with no CMYK build values

- **Usually means:** the file was designed and approved entirely on-screen and never round-tripped through an actual print proof — the CMYK conversion is about to happen for the first time on press, which is the expensive place to discover a color shift.
- **First question:** "What CMYK build values are specified for this color, and has it been proofed on the actual substrate?"
- **Data to pull:** the guideline's color table CMYK column; a physical (not soft) proof if one exists.

### A brand file with no bleed or a bleed under 0.125in (3mm) for a standard print application

- **Usually means:** the file was built as a screen composition and exported for print without checking the vendor's die-cutting tolerance, risking a white sliver at the trim edge on any run with normal press variance.
- **First question:** "What bleed and safe-area tolerance does this specific vendor's die require — has it been confirmed, or assumed?"
- **Data to pull:** the vendor's die-line spec sheet; the file's actual bleed measurement.

### Feedback round with no distinction between "I don't like it" and "this doesn't work"

- **Usually means:** every comment is being treated with equal weight, which either overrides a real defect because it's framed gently, or entrenches a genuine problem because a strongly worded preference outshouted it.
- **First question:** "For this specific comment, what's the evidence it's a functional problem rather than a preference — and if there isn't any, what does the client actually value more here?"
- **Data to pull:** the client feedback triage log (see `references/artifacts.md`); whether each item has a checked-evidence entry before a resolution was proposed.
