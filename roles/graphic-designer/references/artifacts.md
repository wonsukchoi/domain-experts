# Graphic designer artifacts — templates with real structure

Filled examples from the Ridgeline Coffee Roasters rebrand (see `SKILL.md` worked example): a regional coffee roaster moving from café-only sales to 40-store grocery wholesale. Numbers throughout are internally consistent with that example and computed against real WCAG contrast math, not estimated.

## 1. Brand guideline document — table of contents and what each section must contain

A guideline that only shows the logo "looking nice" fails the handoff test. Each section below states the rule as a measurement, not a description.

| Section | Must contain (not just describe) |
|---|---|
| Logo construction | Locked vector master reference, proportions grid showing mark-to-wordmark ratio |
| Clear space & minimum size | Clear space in a self-referential unit; minimum size in both px (digital) and in/mm (print) |
| Color system | Every color in hex + RGB + CMYK + Pantone (if spot printing is used), plus a contrast table by use case (below) |
| Typography | Locked scale ratio and every step's size; pairing rule; what each face is licensed for (headline-only vs. body-approved) |
| Incorrect usage | Rendered examples of the specific violations most likely to happen (stretch, recolor, low-contrast placement, drop shadow) — not a generic "don't misuse the logo" line |
| Applications | The flagship application in full production spec (below), plus at least one secondary application showing the system holds |

## 2. Color-and-contrast table (the section most guidelines skip)

Every color gets a computed contrast ratio for each use case it's approved for — not just a swatch.

| Color | Hex | RGB | CMYK | On white | On cream (#F5F0E6) | Approved for |
|---|---|---|---|---|---|---|
| Ridgeline Green (primary) | #1F3A2E | 31,58,46 | 78,25,55,45 | 12.33:1 | 10.86:1 | Body text, headlines, logo, backgrounds |
| Copper (secondary/accent) | #B5652D | 181,101,45 | 8,60,90,10 | 4.32:1 | 3.8:1 | Headlines ≥28px/18pt, decorative marks, UI accents — **not body text** |
| Cream (ground) | #F5F0E6 | 245,240,230 | 2,2,7,0 | — | — | Background only |
| Old brown (legacy, retired) | #6F4E37 | 111,78,55 | 0,30,50,56 | — | 6.55:1 | Retired — kept here only to document why it was replaced (see rationale below) |

**Rationale row:** old brown cleared body-text contrast (6.55:1) — the rebrand didn't retire it for legibility, it retired it for differentiation: composite shelf mockups showed 3 of 4 direct competitors already using brown/tan-dominant palettes, so brown carried no recognition value on-shelf regardless of its contrast performance. This line exists in the guideline specifically so a future team doesn't "fix" the color back to brown for readability reasons that were never the actual problem.

## 3. Type scale table

Ratio: 1.333 (perfect fourth). Base: 16px / 12pt. Pairing: Fraunces (display serif, headlines and logotype only) + Inter (grotesque, body copy, ingredient lists, spec sheets — chosen because it holds up at the small sizes a wholesale spec sheet requires).

| Step | Size (px) | Size (pt, print) | Typical use |
|---|---|---|---|
| −1 | 12.0 | 9 | Legal/fine print, nutrition panel |
| 0 (base) | 16.0 | 12 | Body copy, ingredient list |
| 1 | 21.3 | 16 | Subhead, callout |
| 2 | 28.4 | 21 | Section head — minimum size copper is approved at |
| 3 | 37.9 | 28 | Page/panel head |
| 4 | 50.5 | 38 | Pouch front headline |
| 5 | 67.3 | 50 | Hero / signage |

Rule attached: any size request outside this table gets rounded to the nearest step, not custom-sized — a "slightly bigger" headline moves from step 3 to step 4 (37.9 → 50.5px), never to an arbitrary in-between value, or the system drifts one exception at a time until it has no scale left.

## 4. Print production spec — 12oz kraft stand-up pouch (flagship application)

| Spec | Value | Note |
|---|---|---|
| Trim size | 5.5in × 8.75in flat (stand-up pouch die) | Confirm against vendor's exact die before finalizing art |
| Bleed | 0.125in (3mm) beyond trim on all sides | Default; some pouch vendors require 0.1875in on the fold — check vendor spec sheet |
| Safe area | 0.125in inset from trim | Nothing critical (logo, required copy) inside this margin |
| Color mode | CMYK, US Web Coated (SWOP) v2 profile | Never hand off RGB/hex values for flexo print — convert and proof first |
| Resolution | 300dpi minimum at output size | A logo file fine on a 96ppi screen is not automatically print-ready; check actual pixel dimensions at 300dpi for the panel size |
| Proofing | Physical press proof on the actual kraft stock before full run | Kraft's brown substrate shifts light colors warmer than a coated-stock or on-screen soft proof shows |
| Spot vs. process | Ridgeline Green available as Pantone 5477 C for 2-color runs; CMYK build (78,25,55,45) for full-color runs | The two are visually close but not identical — guideline states which to request for which press setup |

## 5. Client feedback triage log (the artifact that makes the taste/defect split auditable)

One row per feedback item, filled at the moment feedback is received — not reconstructed later.

| Item | Client's words | Preference or defect? | Evidence checked | Resolution |
|---|---|---|---|---|
| 1 | "Make the logo bigger on the bag" | Preference (framed as defect) | 6ft recognition-distance test at spec size: passed | Kept mark size; increased surrounding negative space instead |
| 2 | "Go back to the old brown" | Preference | Shelf-composite mockup vs. 3 competitors, 3 of 4 already brown/tan-dominant | Kept green; showed composite as evidence |
| 3 | "Origin line is hard to read in that copper" | Defect | Contrast check: copper on cream at body size = 3.8:1, below 4.5:1 body-text minimum | Moved origin line to Ridgeline Green (10.86:1); copper restricted to accent dot only |

**Rule attached:** every row gets an evidence column filled *before* a resolution is proposed — a resolution proposed without a checked-evidence column is a guess dressed as a decision, and it's the thing that erodes client trust when it turns out wrong on the next round.
