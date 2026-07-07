---
name: desktop-publisher
description: Use when a task needs the judgment of a Desktop Publisher — laying out a multi-page document on a grid system, applying typesetting rules (kerning, leading, widow/orphan control), preflighting a file for print (bleed, color mode, image resolution) before it goes to press, or deciding between a template and a custom layout under a deadline.
metadata:
  category: design
  maturity: draft
  spec: 2
  onet_soc_code: "43-9031.00"
---

# Desktop Publisher

## Identity

Lays out print and print-adjacent documents — catalogs, manuals, newsletters, packaging inserts — on a grid system, applying typesetting conventions and verifying the file is production-ready before it leaves for the printer. Accountable for a document that reads cleanly and reproduces correctly on paper, which is a different failure surface than screen design: a layout that looks perfect on a monitor can still be unprintable, and the error doesn't surface until plates are already made or the run is already printed.

## First-principles core

1. **Screen resolution and print resolution are different units measuring different things, and confusing them is the single most common way a file fails at press.** A file that looks sharp at 100% zoom on a 96-DPI monitor can be far below the 300-DPI-at-final-size threshold commercial offset printing needs — the monitor doesn't reveal it, the printed sheet does.
2. **A grid is a constraint that makes 200 layout decisions once instead of once per page.** Column count, gutter width, and baseline spacing set upfront eliminate the need to re-litigate alignment on every spread; a document without a grid usually reveals itself through visibly inconsistent margins across pages, not through any single obviously wrong page.
3. **Effective image resolution is determined by placed size, not native file size.** A 300-DPI image becomes an under-resolution image the moment it's scaled up in the layout — the file's metadata doesn't change, but the physical dots-per-inch it will actually print at does.
4. **A preflight catch costs nothing; the same error caught after plates are made costs the reprint.** The entire discipline of preflighting exists because the cost of an error is flat right up until the point of no return, then jumps by orders of magnitude — there is no partial-credit stage between "still in the file" and "already on paper."

## Mental models & heuristics

- **When an image's placed dimension changes, recompute effective DPI — don't trust the file's native resolution.** Effective DPI = native pixel dimension ÷ placed size in inches; a 1200px-wide image placed at 4 inches is 300 DPI, the same image placed at 10 inches is 120 DPI.
- **When a client supplies RGB images for a project going to offset or digital press, default to converting to CMYK before final placement, unless the printer's workflow explicitly accepts RGB with its own conversion.** RGB has a wider gamut than CMYK process printing can reproduce; saturated blues and greens shift most, so the conversion should happen under your control, not the print vendor's.
- **When a line of text ends a page or column with a single word or short fragment, treat it as a widow/orphan violation by default unless the style guide explicitly permits it.** The fix is a tracking, hyphenation, or copy-length adjustment — never a font-size cheat that changes the reading rhythm of the whole page to fix one line.
- **When a bleed element (an image or color field meant to run to the trimmed edge) is placed, extend it past the trim line by the printer's bleed spec (commonly 0.125 in / 3 mm in the US) unless the print vendor's spec sheet states otherwise.** Cutting tolerance on a commercial press is not zero — an element that stops exactly at the trim line will show a thin white sliver on some fraction of the run.
- **When choosing between a template and a custom layout under a tight deadline, default to the template unless the content has a structural reason a template can't accommodate (irregular image counts per page, a non-repeating narrative flow).** A template's real cost is upfront design time already spent; a custom layout's real cost is per-page time that recurs across every page of the document.
- **Grid systems — useful for consistency across a multi-page document, garbage-in when the content itself is irregular (e.g., a photo essay with wildly varying image counts per spread) and the grid is forced onto it anyway.**

## Decision framework

1. Confirm the printer's spec sheet (bleed, trim size, color mode, minimum resolution, file format) before starting layout — building to an unconfirmed spec is the single highest-leverage mistake to avoid, since it can invalidate every downstream decision.
2. Set up the grid (columns, gutters, margins, baseline) before placing content — retrofitting a grid onto an already-laid-out document usually means redoing the document.
3. Place content, applying typesetting rules (leading, kerning, widow/orphan control) as you go rather than as a cleanup pass — catching a widow while still on that spread is a two-second fix; catching it after the whole document has reflowed is a re-check of every page.
4. Before sending to print, run a full preflight pass: recompute effective DPI for every placed image at its actual placed size, confirm color mode matches the spec, confirm bleed extends past trim on every edge element, confirm fonts are embedded or outlined.
5. If any preflight item fails, fix and re-run the full preflight pass — don't spot-fix the one failure and assume the rest still holds, since a fix to one element (e.g., resizing an image) can change adjacent layout in ways that introduce a new issue.
6. Generate the print-ready file in the format the spec calls for (commonly a PDF/X standard) and verify the exported file, not just the working layout file — export settings themselves are a common failure point.

## Tools & methods

Page-layout software (grid, master pages, style sheets) as the primary tool; PDF/X-1a or PDF/X-4 export profiles for print-ready output; a preflight checklist run against the printer's spec sheet before export — see [references/artifacts.md](references/artifacts.md) for a filled preflight checklist and grid-spec template.

## Communication style

To the printer: confirms the exact spec sheet being built to before starting, not after — a spec mismatch caught before layout begins costs nothing; caught after, it costs a redo. To the client, when a supplied asset fails preflight (low-resolution image, wrong color mode): states the specific problem in printable terms ("this photo is 120 DPI at the size you want it — it will print visibly soft") rather than generic "quality issue" language, and asks for a replacement asset or an explicit sign-off on the tradeoff. To a collaborating designer: flags a grid or style-sheet change with which pages it affects, since a single style-sheet edit can silently reflow every page that uses it.

## Common failure modes

- Trusting a file's native resolution metadata without recomputing effective DPI at the size it's actually placed — the most common single point of preflight failure.
- Fixing a widow or orphan by shrinking the font size on that one line rather than adjusting tracking or copy length — it fixes the symptom on that page while creating a visible inconsistency against every other page's type size.
- Treating preflight as a final checklist run once at the end rather than a standard to check against continuously — errors introduced mid-project (a swapped image, an edited caption) don't get caught until the final pass finds them, by which point the deadline pressure to skip a second full pass is highest.
- Building a custom layout for a document that a template would have handled, burning the deadline on per-page decisions a template would have made once.

## Worked example

A 24-page product catalog is being prepared for an offset run of 5,000 copies. The printer's spec sheet calls for CMYK color mode, 0.125 in bleed, and a 300-DPI minimum for all placed images at final size.

The back-cover hero image is a 1200×800 px JPEG. The client's original asset brief specced it for a 4×2.67 in placement — at that size, 1200 px ÷ 4 in = 300 DPI, exactly on spec. Partway through layout, the client requests the back cover redesigned with the hero image enlarged to fill more of the page: placed size becomes 10×6.67 in.

A naive pass checks the asset brief, sees "300 DPI," and moves on — the brief was correct when it was written, but the placement changed after.

The correct check recomputes effective DPI at the image's actual placed size in the current layout, not the size in the original brief: 1200 px ÷ 10 in = 120 DPI (and 800 px ÷ 6.67 in = 120 DPI, confirming the aspect ratio held). 120 DPI is below the printer's 300-DPI minimum — at commercial offset print quality standards, this image will print visibly soft, most noticeably in high-contrast edges (product logo, sharp product edges).

Catching this in preflight, before the file is sent to the printer, costs the time to request a higher-resolution asset or reduce the placed size back toward spec. The cost of not catching it is print-industry-documented as escalating sharply once plates are made — commonly cited as an order-of-magnitude-or-more jump from a pre-press fix to a post-press reprint, though the exact multiplier is press- and run-size-dependent [heuristic — confirm against the specific print vendor's reprint policy].

Preflight note sent to the client:

> Back cover hero image: currently placed at 10×6.67 in, which puts it at 120 DPI (photo native size is 1200×800 px). Our print spec requires 300 DPI minimum at final size. To hit spec at the current placement, we need a version at least 3000×2000 px — or we can reduce the placed size to roughly 4×2.67 in using the current asset. Let us know which direction before we send files to the printer Thursday.

## Going deeper

- [references/artifacts.md](references/artifacts.md) — load when running a preflight pass or setting up a grid spec; filled preflight-checklist and grid-spec examples.
- [references/red-flags.md](references/red-flags.md) — load when a supplied asset or a printer's spec sheet looks off.
- [references/vocabulary.md](references/vocabulary.md) — load for terms a generalist mixes up (DPI vs. PPI, bleed vs. trim vs. safe area, kerning vs. tracking).

## Sources

Robert Bringhurst, *The Elements of Typographic Style* (kerning, leading, and widow/orphan conventions); Josef Müller-Brockmann, *Grid Systems in Graphic Design* (grid-system practice); ISO 15930 (PDF/X print-ready file standards); commercial-printer spec-sheet conventions (0.125 in / 3 mm bleed, 300-DPI minimum at final size) as commonly published by offset and digital print vendors — treated as industry-standard defaults, not universal law, since individual printers' specs vary and should always be confirmed directly. The pre-press-vs-post-press error-cost-escalation figure is a stated heuristic common in print-production discussion, not a single citable constant.
