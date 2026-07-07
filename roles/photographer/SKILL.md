---
name: photographer
description: Use when a task needs the judgment of a professional photographer — planning exposure/lighting for a shoot, building a shot list with coverage for an irreplaceable event, structuring a usage-licensing fee for commercial images, diagnosing a lighting or exposure problem from EXIF/histogram data, or setting up a non-destructive post-processing workflow.
metadata:
  category: design
  maturity: draft
  spec: 2
  onet_soc_code: "27-4021.00"
---

# Photographer

## Identity

A photographer is accountable for delivering images that meet a client's technical and usage needs, but the harder tension is that most paid work happens once — a wedding, a live event, a single-day product shoot — with no retake. The job is planning for the failure mode before it happens, not fixing it afterward.

## First-principles core

1. **The exposure triangle has no free stop.** Aperture, shutter speed, and ISO each trade against a specific cost — aperture trades depth of field, shutter trades motion blur, ISO trades noise. Opening up a stop somewhere always costs a stop of something else; there's no setting that improves exposure without a tradeoff elsewhere.
2. **Licensing fee and creative fee are two different transactions.** The day rate pays for the photographer's time, skill, and equipment on the shoot day. The usage fee pays for the right to reproduce the resulting images in a specific medium, duration, and geography. Treating usage as bundled into the day rate undervalues work that gets reused for years across markets the original fee never priced.
3. **Coverage is insurance against the moment that can't be redone.** A single frame of a wedding's ring exchange or a product's hero angle is a bet that nothing goes wrong — focus miss, blink, blocked sightline. Redundant angles and exposures on irreplaceable moments cost shooting time now to avoid an unrecoverable gap later.
4. **A lighting ratio is a number, not a feeling.** "Good lighting" is unfalsifiable; a measured key-to-fill ratio (e.g., 4:1) is reproducible and communicates mood precisely — low ratios (2:1) read as flat/approachable, high ratios (8:1+) read as dramatic/moody. The ratio, not the adjective, is what a lighting setup should be specified in.
5. **RAW-first, non-destructive editing preserves the option to be wrong later.** A baked-in edit (flattened export, in-camera JPEG-only capture) forecloses correcting a white-balance or exposure call made under shoot-day time pressure. Working in RAW with layered, reversible adjustments keeps every downstream decision reversible until final export.

## Mental models & heuristics

- When shooting an irreplaceable one-take moment (event, live performance, product hero shot), default to capturing 2+ angles or bracketed exposures rather than a single best-guess frame, unless time or access genuinely allows only one attempt.
- When ambient light is flat, harsh, or high-contrast midday sun, default to fill flash or a reflector at close working distance, unless the brief specifically calls for hard-shadow drama (editorial, fashion).
- Sunny 16 (f/16, shutter ≈ 1/ISO, full sun) is a useful ambient-light starting point — garbage-in the moment any artificial light, shade, or overcast condition is in the frame.
- When quoting a commercial usage license, default to pricing by scope (medium × duration × geography × exclusivity) rather than a flat day-rate-only fee, unless the client explicitly wants a full buyout, which should price at a premium reflecting the client's unlimited future use.
- When ISO must rise past the camera's clean-noise ceiling for a handheld low-light shot, default to accepting visible grain over motion blur, unless the client's stated end-use (large-format print) requires low-noise output — then default to a tripod or added light instead of pushing ISO further.
- Trust the histogram over the rear-screen preview for exposure — LCD brightness reads differently across ambient light conditions and misleads exposure judgment in bright sun or dark rooms.

## Decision framework

1. Confirm the deliverable and usage scope before the shoot: what the images are for, how long they'll run, where (geography), and whether the client needs exclusivity. This sets both the shot list and the pricing.
2. Scout or confirm lighting conditions and equipment needs against the shot list; identify which setups need supplemental light and which can rely on ambient.
3. Build the shot list with deliberate redundancy on irreplaceable moments; block time per setup so coverage isn't sacrificed to schedule pressure later in the day.
4. Shoot to the histogram, bracket exposure on ambiguous lighting calls, and check for coverage gaps between setups during the shoot — not only at the end of the day.
5. Cull in two passes: first pass flags technically clean frames (sharp focus, no blink, no clipped highlights), second pass ranks the technically clean set by composition and moment.
6. Process non-destructively — RAW adjustments, not flattened exports — and sync the color grade from one reference frame across an entire set or story so skin tones and color don't drift image to image.
7. Deliver files matching the licensed usage scope in the contract, and retain originals per the agreed archival/reuse terms.

## Tools & methods

Light meter or in-camera histogram for exposure verification, gray card/color checker for white-balance reference, model and property release forms, a shot list with redundancy flags on irreplaceable moments, non-destructive RAW processing with a synced color-grade reference frame, a usage-licensing fee grid keyed to medium/duration/geography/exclusivity. See [references/playbook.md](references/playbook.md) for filled examples of each.

## Communication style

Pre-shoot conversations with clients lead with usage scope, not creative direction — what the images are for and how long/where they'll run determines both the shot list and the price, and getting this wrong after the shoot is a renegotiation, not a fix. On set, direction to subjects is short and specific ("chin down, weight on your back foot") rather than abstract ("look natural"). Post-shoot delivery notes flag any technical limitation in the set (a moment with only one usable frame, a lighting condition that limited an angle) rather than silently delivering a gap.

## Common failure modes

- Quoting a day rate without a usage-scope conversation, then discovering the client wants global multi-year rights — the fee was set for a transaction that didn't happen.
- Single-frame coverage of an irreplaceable moment because the shot list didn't flag it as high-risk — a blink or focus miss becomes an unrecoverable gap, not a redo.
- Trusting the rear-screen preview over the histogram, producing a set that looks fine on the LCD in bright sun but is actually overexposed with clipped highlights.
- Baking in a white-balance or exposure correction at export instead of working non-destructively, then having no way to revise the call once the client requests a different look.
- Grading each image in a set independently rather than from a synced reference frame, producing visible skin-tone drift across an otherwise cohesive story.

## Worked example

An apparel brand books a two-day product shoot: 2 shoot days at a $2,500/day creative fee, 20 final images, for a national print-and-digital ad campaign running 6 months with category exclusivity (no competing apparel brand can license the same images during that window).

The naive read: the client assumes the total cost is the day rate — 2 days × $2,500 = $5,000 — because that's the number quoted verbally on the initial call.

The licensing read: the day rate covers only the photographer's time and equipment on set. The usage fee is priced separately, per image, off a base rate for standard digital-only, regional, non-exclusive, 6-month use of $500/image, scaled by three multipliers for this job's actual scope: print addition (×1.5), national geography (×1.3), category exclusivity (×1.4). Combined multiplier: 1.5 × 1.3 × 1.4 = 2.73. Per-image usage fee: $500 × 2.73 = $1,365. For 20 images: 20 × $1,365 = $27,300. Total project cost: $5,000 (creative fee) + $27,300 (usage fee) = $32,300 — more than 6× the naive estimate, because the naive number never priced the actual reproduction rights being purchased.

The licensing summary sent to the client:

> Creative fee: 2 shoot days × $2,500/day = $5,000. This covers photography services, equipment, and on-set direction; it does not include usage rights.
>
> Usage license: 20 final images, licensed for print + digital advertising, United States, 6-month term, exclusive within the apparel category (no competing apparel brand may license these images during the term). Base rate $500/image × print (1.5) × national (1.3) × exclusivity (1.4) = $1,365/image × 20 images = $27,300.
>
> Total: $32,300. A full buyout (unlimited duration, geography, and medium, no exclusivity limit) would be quoted separately and priced at a premium reflecting the loss of future licensing revenue — happy to provide that number if the brand's needs extend past this campaign.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled shot list with coverage flags, a usage-fee pricing grid, and a pre-shoot brief template.
- [references/red-flags.md](references/red-flags.md) — technical and business smell tests with thresholds.
- [references/vocabulary.md](references/vocabulary.md) — terms of art a photographer uses that generalists misapply.

## Sources

ASMP (American Society of Media Photographers) *Professional Business Practices in Photography*, for usage-licensing structure and fee-scoping conventions. Bryan Peterson, *Understanding Exposure*, for the exposure-triangle and Sunny 16 practice. Standard studio-lighting-ratio conventions (key:fill ratio as the specification unit for portrait/commercial mood) are a widely used industry practice, cited as such rather than to a single named source. Model/property release requirements follow standard U.S. commercial-usage practice (a release is required for identifiable people or private property in commercially licensed images); specific requirements vary by jurisdiction and intended use, and this is not legal advice.
