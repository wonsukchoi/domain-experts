# Playbook

Filled tables and sequences for the calls a MRF sorter makes every shift: bale-purity price tiers by stream, hazardous-item classification, picking-station reach/guarding limits, and the contamination-decision sequence at pick speed.

## Bale-purity / price-tier tables by material stream

Figures below follow the ISRI grade convention (percentage of prohibitive materials/outthrows tolerated per grade) with illustrative price tiers — actual dollar figures are buyer-contract-specific and move with commodity markets.

| Stream | Top-tier spec | Top-tier price (illustrative) | Mid-tier spec | Mid-tier price | Reject/low-grade threshold |
|---|---|---|---|---|---|
| PET bottles (positive sort) | ≥95% single-resin PET | $380/ton | 90-94% single-resin | $300/ton | <90% — sold as mixed plastic, ~$60/ton |
| HDPE (natural or color) | ≥95% single-resin, natural/color as specified | $420/ton (natural) | 90-94% | $340/ton | <90% — mixed-plastic rate |
| OCC (old corrugated containers) | ≤5% total outthrows/prohibitives | full index rate | 5-10% outthrows | discounted 20-40% off index | >10% — rejected, reprocess or landfill |
| Mixed/sorted office paper | ≤1-2% prohibitives | full index rate | 2-5% prohibitives | discounted rate | >5% — rejected |
| Aluminum UBC (used beverage cans) | ≥98% aluminum, <1% iron | full scrap rate | 95-97% aluminum | discounted 10-15% | <95% or visible steel-can mixing — rejected, resorted |

**Reading the table:** a purity result crossing a tier boundary changes the whole bale's price, not just the fraction of material that's actually out of spec — a bale at 89% PET purity loses the entire top-and-mid-tier premium on 100% of its tonnage, not just the 11% that's contamination. This is why a station-coverage gap or a fatigue-driven accuracy dip matters even when the raw percentage change looks small.

## Hazardous-item classification: line-stop vs. routine pull

| Item | Classification | Required action |
|---|---|---|
| Battery: swollen, leaking, smoking, hissing, or hot to the touch | Immediate line-stop | Pull E-stop cord; isolate into fire-safe sand-filled or metal lidded container, separate from routine battery bin; alert supervisor before restarting the line |
| Battery: intact, no visible damage, out-of-place single-use or rechargeable cell | Routine hazard pull, no stop | Place in designated battery collection bin; log count at end of rotation |
| Full or pressurized propane/aerosol canister | Immediate line-stop | Stop belt; clear the immediate station; alert supervisor/fire-safety officer; do not puncture, compress, or place in a standard bin |
| Empty, clearly vented aerosol can | Routine hazard pull, no stop | Place in designated metals/hazard-adjacent bin per facility protocol |
| Unlabeled or unknown liquid/chemical container | Immediate line-stop until identified | Isolate without opening; alert supervisor/HAZMAT contact; do not attempt to identify by odor or contact |
| Medical sharps/needles | Routine hazard pull, PPE required | Cut-resistant gloves on; use puncture-resistant sharps container; never hand-sort loose sharps |
| Ammunition or ordnance-like item | Immediate line-stop, evacuate zone | Alert supervisor and follow facility law-enforcement notification protocol; do not handle further |
| Broken glass | Routine pull, no stop | Designated glass residue stream; cut-resistant gloves for handling |
| Plastic film/bags in a rigid-container stream | Routine pull, no stop | Residue stream; a volume spike (not an individual bag) is the signal worth flagging upstream |

## Picking-station reach and guarding reference

| Guard/reach parameter | Convention |
|---|---|
| Fixed reach distance from working position to nearest nip point | Set so a normal working reach cannot contact the nip point; leaning or stepping past the rail to extend reach defeats this by design, not by a guard defect |
| Guard rail height at picking platform | Full-height rail at the belt-facing edge; any propped-open or removed section is a guard-defeat event, reportable regardless of whether an incident occurred |
| Belt speed vs. reaction window | At typical picking-line speeds, an item at the far edge of a station's reach zone gives roughly 1-2 seconds of decision time before it passes — this is the basis for the pull-to-reject default on ambiguous material, not a deliberation window |
| Cross-station reach | An item past your station's zone belongs to the next station or the reject stream — reaching across into a neighboring station's zone to chase a high-value item is an amputation-risk behavior, not a productivity gain |

## Contamination-decision sequence (per item, at pick speed)

1. **Classify on sight** into one of three buckets: target recyclable, contamination (quality), hazardous (safety). No fourth bucket, no "decide later."
2. **Contamination:** pull to reject/residue stream within the 1-2 second reach window. Do not inspect closely — the pull-to-reject default exists precisely so this step doesn't require deliberation.
3. **Hazardous, damaged/venting/smoking:** pull the E-stop cord immediately. Do not attempt to move the item with bare hands before the belt stops.
4. **Hazardous, intact/out-of-place:** pull to the appropriate hazard bin (battery, sharps, glass) without stopping the line.
5. **Unknown or unidentifiable item that could be either bucket:** default to the more conservative classification (hazardous) rather than the faster one (contamination) — reclassifying a false positive costs seconds; missing a real hazard does not resolve at the station.
6. **Log** every line-stop event (item, time, station) and hazard-bin tally at end of rotation. This is the data a purity or fire-risk trend traces back to, not a memory of "how the shift felt."
