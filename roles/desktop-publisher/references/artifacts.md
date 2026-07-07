# Desktop Publisher — Artifacts

## Grid spec (filled example, 24-page catalog)

| Element | Value |
|---|---|
| Page trim size | 8.5 × 11 in |
| Bleed | 0.125 in all edges (trim size + bleed = 8.75 × 11.25 in working canvas) |
| Safe area | 0.25 in inset from trim on all edges (no live text/critical content closer to trim than this) |
| Columns | 3-column grid, 0.1875 in gutters |
| Margins | Top 0.75 in, bottom 0.75 in, inside (gutter side) 0.625 in, outside 0.5 in |
| Baseline grid | 12 pt increments, body text set on-baseline |

## Preflight checklist (filled example, same catalog)

| Check | Spec requirement | Found | Status |
|---|---|---|---|
| Color mode | CMYK | 3 images still RGB (pp. 14, 19, 22) | **FAIL — convert before export** |
| Bleed | 0.125 in past trim on all bleed elements | p. 24 back-cover image stops at trim, no bleed extension | **FAIL — extend image** |
| Image resolution | ≥300 DPI at placed size | p. 24 hero image at 120 DPI (1200×800 px placed at 10×6.67 in) | **FAIL — see effective-DPI note below** |
| Image resolution | ≥300 DPI at placed size | All other images pass (302–450 DPI range) | Pass |
| Font embedding | All fonts embedded or outlined | 1 font (Proxima Nova Bold, used p. 8 headline only) not embedded | **FAIL — embed or outline** |
| Widow/orphan | No single-line widows at column/page breaks | 2 found (pp. 6, 17) | **FAIL — adjust tracking/copy** |
| Trim/safe-area violations | No live text inside 0.25 in safe margin | None found | Pass |

**Effective-DPI recompute (p. 24 hero image):** native 1200×800 px; placed 10×6.67 in → 1200 ÷ 10 = 120 DPI horizontal, 800 ÷ 6.67 = 120 DPI vertical (consistent — placement preserved aspect ratio, confirms the math, not a cropping error). 120 DPI is 40% of the 300-DPI spec. Options in priority order: (1) source a higher-resolution asset (need ≥3000×2000 px to hit 300 DPI at this placed size), (2) reduce placed size to ≤4×2.67 in to bring the existing asset to spec, (3) proceed at 120 DPI only with explicit client sign-off on the visible-softness tradeoff.

## Client-facing preflight note (filled example)

> Subject: 3 items before we send to print Thursday
>
> 1. **Back cover hero image** — currently placed at 10×6.67 in, which puts it at 120 DPI (photo native size is 1200×800 px). Spec requires 300 DPI at final size. Need either a ≥3000×2000 px replacement, or we scale the placement down to ~4×2.67 in using the current asset. Which do you want?
> 2. **Page 8 headline font** — Proxima Nova Bold isn't licensed for embedding in the PDF we'd send to the printer. Can you confirm the license covers print embedding, or should we substitute a web-safe alternative for this one headline?
> 3. Pages 14, 19, 22 photos are in RGB — we'll convert to CMYK on our end before export; flagging in case the color shift (most visible in saturated blues/greens) matters for brand-color accuracy, so you can review a proof before final send.
>
> Everything else passed preflight clean. Need answers on #1 and #2 by end of day Wednesday to hit the Thursday print deadline.
