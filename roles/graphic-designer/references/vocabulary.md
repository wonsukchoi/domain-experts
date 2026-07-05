# Graphic designer working vocabulary

Terms a graphic designer uses precisely and daily. Format: definition → how a practitioner says it → common misuse.

**Modular scale** — A fixed multiplicative ratio (e.g., 1.25, 1.333, 1.5) applied to a base size to generate every type size in a system, so all sizes stay in a defined relationship to each other.
In use: "We're locked at 1.333 off a 16px base — the headline steps to 28.4, not 30, because 30 isn't on the scale."
Misuse: treating it as a one-time calculation instead of a constraint — picking scale-derived sizes for the first pass, then eyeballing "close enough" adjustments afterward that quietly break the relationship the scale existed to protect.

**Clear space** — The minimum empty margin required around a logo, defined in a unit derived from the mark itself (a letterform's cap-height, the mark's own width) rather than a fixed measurement.
In use: "Clear space is 1x cap-height on all sides — at any size, measure it off the wordmark, not a ruler."
Misuse: specifying it as a fixed inch or pixel value, which is correct at one size and wrong at every other size the mark is ever reproduced at.

**Contrast ratio** — A calculated relationship (per WCAG, using relative luminance) between a foreground and background color, expressed as a ratio like 4.5:1; the basis for legibility thresholds, not a subjective "readable enough" judgment.
In use: "That copper on cream measures 3.8:1 — fine for a headline, fails for body copy."
Misuse: eyeballing contrast ("it looks readable to me") instead of measuring it, especially on unusual backgrounds like photography, textured stock, or gradients where the eye is a poor judge.

**Bleed** — The area of artwork extending past the trim line, printed and then cut off, so that no unprinted sliver appears at the edge if the cut shifts slightly during production.
In use: "Extend the background color 0.125in past trim for bleed — don't just fill to the trim line."
Misuse: assuming bleed is optional for small print runs or digital-adjacent print jobs; press and cutting tolerance don't scale down with run size.

**Safe area** — The inset margin from the trim line inside which nothing critical (logo, required copy, legal text) should sit, protecting against minor cutting variance.
In use: "Keep the logo and price at least 0.125in inside trim — that's the safe area, not just a suggestion."
Misuse: conflating safe area with bleed; bleed extends outward past trim, safe area pulls content inward from trim — they solve the same cutting-variance problem from opposite directions.

**CMYK vs. RGB** — CMYK (cyan/magenta/yellow/key-black) is a subtractive color model for reflected-ink printing; RGB is an additive model for transmitted light on screens. The two have different gamuts — some RGB colors, especially saturated blues and greens, cannot be reproduced in CMYK.
In use: "That blue looks great in RGB but it's out of CMYK gamut — proof it before you promise the client that exact hue on the printed piece."
Misuse: treating conversion as automatic and lossless, or building brand colors in RGB only and discovering the print mismatch after a run is already at the vendor.

**Spot color (Pantone) vs. process color** — Spot color is a single pre-mixed ink printed as its own plate for exact, consistent color match; process color is built from CMYK dots and can vary slightly by press, run, and operator.
In use: "Use the Pantone spot for the 2-color letterhead run, but the CMYK build for the full-color packaging — they're close but not identical, and the guideline should say which to request."
Misuse: assuming a Pantone number and its CMYK "equivalent" will look identical printed side by side; they're a documented close approximation, not a guarantee.

**Kerning vs. tracking** — Kerning adjusts the space between a specific pair of letters; tracking adjusts spacing uniformly across a whole word, line, or block of text.
In use: "The logotype needs kerning between the R and the V specifically — don't just track the whole wordmark tighter."
Misuse: using the terms interchangeably, or fixing a single awkward letter-pair gap by tracking the entire line, which introduces new gaps everywhere else.

**Baseline grid** — A grid of horizontal lines, spaced at a fixed increment, that all text baselines align to across a layout, keeping multi-column or multi-element text visually synchronized.
In use: "Body copy sits on an 8px baseline grid — when we add the pull-quote, its leading has to divide evenly into that or the columns drift out of alignment."
Misuse: applying a grid to a headline's overall block position while ignoring whether its actual text baseline lands on the grid, which produces the drift the grid was meant to prevent.

**Type pairing** — Selecting two (rarely three) typefaces for a system that contrast enough to signal distinct roles (display vs. body) without competing for the same visual attention.
In use: "Fraunces carries the personality for headlines, Inter is the neutral workhorse for body copy — one expressive face, one that gets out of the way."
Misuse: pairing two display faces (which compete) or two neutral faces (which give no contrast, reading as an accident rather than a decision).

**Brand equity** — The accumulated recognition value a mark, color, or logotype has built through consistent exposure over time, which a redesign spends down whether or not the new design is objectively better.
In use: "The old brown has 8 years of recognition in this market — retiring it isn't free even though the new palette tests better."
Misuse: treating equity as a reason to never change anything, or treating a redesign as costless because the new version tests well in isolation — both ignore that recognition is cumulative and a reset has a real cost.

**Die line** — The vector outline marking exactly where a package or printed piece will be cut, folded, or scored, separate from the printed artwork layer.
In use: "Send the vendor the die line as a separate non-printing layer — don't bury the fold marks inside the artwork file."
Misuse: treating the die line as a rough guide rather than the exact production geometry; artwork that doesn't precisely respect the die line's fold and cut positions misregisters on the finished piece.

**Legibility vs. readability** — Legibility is whether individual letterforms can be distinguished (a typeface property); readability is whether extended text is comfortable to read (a layout property — line length, leading, contrast).
In use: "The typeface is legible at 9pt, but the readability's poor — the line length is too long for that size, that's a layout fix, not a font fix."
Misuse: treating them as the same problem, which leads to swapping typefaces to fix what's actually a line-length or leading issue.
