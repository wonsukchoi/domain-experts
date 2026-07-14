# Playbook

## Preflight checklist

Run in full before any manual correction or plate output; log results on the job ticket.

| Check | Requirement | Fail action |
|---|---|---|
| Color space | CMYK (or job-specific spot colors) | Flag; convert using press/paper-matched ICC profile |
| Image resolution | ≥300 dpi at final placed size (adjust for large-format viewing distance) | Flag; request replacement, do not upsample |
| Bleed | Matches job ticket's bleed spec (commonly 0.125") | Flag; request corrected file |
| Fonts | Embedded or outlined | Flag; request embedded/outlined version |
| Black builds | Small text/fine lines = 100% K; large solid areas may use rich black | Flag rich-black text for correction |
| Trapping | Set per actual color combinations and press tolerance | Adjust; avoid uniform default trapping |
| Overprint/knockout | Deliberately set per element, not left at default | Review and correct per intended layering |
| Proof status | Contract proof generated and signed for color-critical jobs | Hold plate output until signed proof on file |
| File version match | Plate-output file matches the approved proof's version/timestamp | If mismatched, generate and secure new proof before proceeding |

## Dot-gain reference table (illustrative — always use the press's current characterized profile)

| Stock type | Typical dot gain at 50% tint | Notes |
|---|---|---|
| Coated sheetfed offset | ~13-16% | Lower gain; finer detail holds better |
| Coated web offset | ~16-20% | Higher speed/heat than sheetfed increases gain |
| Uncoated offset (sheetfed or web) | ~20-26% | Higher ink absorption; midtones need more compensation |
| Newsprint | ~26-30%+ | Highest gain; requires the most aggressive tone-curve compensation |

Values are illustrative examples consistent with typical GRACoL/SWOP characterization ranges — always confirm against the specific press's current characterized ICC profile rather than these figures directly.

## Bleed/trap decision table

| Job type | Bleed | Trapping consideration |
|---|---|---|
| Business card, standard trim | 0.125" typical | Minimal — usually simple color blocks, low registration risk |
| Full-page magazine ad | 0.125"-0.25" per publication spec | Check publication's specific press tolerance; follow their supplied spec, not a generic default |
| Large-format signage/banner | Varies by finishing method (grommets, hemming) — confirm with finishing spec, not print bleed alone | Lower registration risk at large scale; trapping less critical than at small text scale |
| Packaging / die-cut piece | Set by the die line, confirm with structural design file | High — die-cut edges and fold lines are especially registration-sensitive |
