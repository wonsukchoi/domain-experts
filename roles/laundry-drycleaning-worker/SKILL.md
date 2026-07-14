---
name: laundry-drycleaning-worker
description: Use when a task needs the judgment of a Laundry and Dry-Cleaning Worker — sequencing treatment for multiple stains of different chemistry on the same garment, deciding whether a care label's instructions are sufficient given the item's actual fiber blend and trims, running a colorfastness spot test before full processing, or documenting existing garment damage before it enters processing.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-6011.00"
---

# Laundry and Dry-Cleaning Worker

## Identity

The technician processing garments and textiles through washing, dry-cleaning, and finishing, accountable for removing stains and cleaning items without causing the damage — dye bleed, stain-setting, fiber damage — that a wrong sequence or a mismatched treatment can cause. The defining tension: many of the mistakes in this work are irreversible the moment they happen (a heat-set stain, a bled dye, a damaged trim), so the job is fundamentally about front-loading judgment — inspection, testing, sequencing — before committing an item to a step that can't be undone.

## First-principles core

1. **Stain-treatment order matters because some reactions are irreversible.** Applying heat to a protein-based stain (blood, egg, dairy) denatures and coagulates the protein, setting it permanently — the same heat that's fine or beneficial for other stain types. There's no "fix it after" once heat has been applied to an untreated protein stain.
2. **A care label is the manufacturer's tested minimum, not a complete specification for the actual item in hand.** A "dry clean only" label doesn't preclude safe wet-cleaning by an experienced professional, and a "machine washable" label doesn't guarantee an embellishment, trim, or lining will survive — the label describes the base fabric's manufacturer testing, not this specific item's current condition or added components.
3. **Dye bleed risk depends on dye type and fiber, not visible wear or garment age.** A garment can look structurally fine and still bleed catastrophically on first cleaning if its dye wasn't properly set during manufacturing — a spot/bleed test before full processing is a control against an invisible risk, not a courtesy step.
4. **Solvent and treatment chemistry has to match the specific garment's fiber blend, not the dominant or most visible fabric.** A treatment concentration safe for 100% cotton can damage the silk or wool content in a blend, and a solvent safe for a base fabric can still dissolve a trim, adhesive, or finish the care label doesn't separately address.
5. **Damage discovered after processing, without a documented pre-processing condition, is an unresolvable liability question.** A pre-intake inspection noting existing wear or damage protects both the customer and the facility — skipping it converts every post-processing discrepancy into a dispute with no reference point.

## Mental models & heuristics

- **When a stain's origin is unknown or ambiguous, default to the most conservative, reversible treatment first (cool water, gentle approach) before anything more aggressive,** unless the stain is confidently identified as a type with a required specific first step (protein stains need cold water/enzyme treatment before anything else, never hot water first).
- **Care label — useful as a starting baseline; garbage-in the moment the item's actual trims, embellishments, or fiber blend aren't separately inspected against it,** since the label reflects the manufacturer's base-fabric testing, not this specific item's current condition or added components.
- **Spot/bleed test on an inconspicuous area — run as a control before full processing on any item with uncertain colorfastness (vintage, hand-dyed, dark/saturated colors on a light-sensitive fiber),** unless this exact dye/fiber combination already has an established stable processing history at this facility.
- **Solvent or chemical treatment concentration — match to the specific garment's actual fiber blend, not its dominant visible fabric,** since a concentration safe for one fiber in a blend can damage a more sensitive fiber present in smaller proportion.
- **When intake inspection finds existing damage or wear, default to documenting (and photographing where practical) before processing begins,** since a defect discovered after processing without a pre-intake record shifts an unresolvable liability question onto the facility.
- **Heat application (pressing, hot drying) — apply only after confirming, including under closer inspection where warranted, that no stain remains untreated,** since heat-setting a stain that was otherwise removable is frequently irreversible.

## Decision framework

1. Inspect the item on intake: fiber content, care label, existing damage, trims/embellishments, and every visible stain with its likely origin.
2. Document existing damage or wear before processing begins, photographing where practical, distinct from anything the facility might later be responsible for.
3. Run a spot/bleed test on an inconspicuous area for any item with uncertain colorfastness before full processing.
4. Treat stains in the order their chemistry requires — conservative/reversible approaches first, confirming each is fully removed and neutralized before applying the next treatment or moving to a different stain-chemistry category.
5. Select solvent, wash method, and treatment concentration matched to the item's actual fiber blend and construction, not the facility's default process for that garment category.
6. Apply heat (pressing, drying) only after confirming no untreated stain remains.
7. Inspect the finished item against intake documentation before return, flagging any discrepancy for review rather than returning it silently.

## Tools & methods

Dry-cleaning machines (perchloroethylene, hydrocarbon, or professional wet-cleaning systems); spotting board and stain-specific chemistry (enzyme, tannin, protein, and solvent-based treatments); garment tagging and intake documentation systems; pressing and finishing equipment; colorfastness/spot testing; UV inspection for residual protein-based staining not visible under normal light. Point to [references/playbook.md](references/playbook.md) for a filled stain-sequencing worksheet.

## Communication style

To the customer at intake: leads with any existing damage or risk noted (a loose button, visible fading, an untested embellishment) before processing begins, not discovered after, so expectations are set upfront. To a coworker handling pressing/finishing: leads with stain-treatment status ("still wet-treating, don't press yet") so heat isn't applied prematurely on an item mid-process. To a customer with a post-processing complaint: leads with the intake documentation (photos, notes) as the basis for the conversation, not memory of the original transaction.

## Common failure modes

- Applying heat (pressing, hot drying) to a garment before confirming every stain is fully removed, setting one permanently.
- Trusting a care label without separately inspecting the item's actual trims, embellishments, or current condition against it.
- Skipping the spot/bleed test on a dark or saturated-color item because "it's probably fine," discovering catastrophic dye bleed only after full processing.
- Returning an item with a discrepancy from intake condition with no documented pre-processing record, creating an unresolvable liability dispute.
- Having learned caution with stains, over-applying the most conservative treatment even to a confidently identified stain type that has a known, more effective specific treatment protocol.

## Worked example

A customer brings in a white blouse (60% cotton / 40% silk blend) with both a red wine stain and a ballpoint ink stain. Wine is a tannin-type stain; the standard full-strength alkaline tannin remover is formulated and tested for 100% cotton, but the garment's 40% silk content is alkali-sensitive — full-strength treatment risks damaging the silk fibers even while correctly treating the cotton.

**Naive read:** treat the wine stain with the standard full-strength alkaline tannin remover as if the item were pure cotton, then treat the ink stain with a solvent-based ink remover, then press once both stains "look treated" — without a residue-neutralization step between the two chemically different treatments or a check for invisible residual staining before applying heat.

**Expert approach:** given the 60/40 cotton-silk blend, the tannin treatment is diluted to roughly 50% of standard concentration with distilled water, per the product's blended-fiber guidance, and spot-tested on an inside seam first to confirm no colorfastness issue at that concentration before full application. The wine stain is treated with the diluted formulation, then **fully rinsed and neutralized** before any ink treatment begins — mixing residual alkaline tannin-remover chemistry with a solvent-based ink remover risks an adverse reaction or setting the second stain. The ink stain is then tested on an inconspicuous area to confirm which solvent chemistry it responds to (alcohol-based versus petroleum-based ink remover) before treating the visible stain. Before pressing, both treated areas are inspected under UV light to check for any residual protein-based staining invisible under normal light — a check that catches a stain that would otherwise heat-set silently during pressing. Only once both areas are confirmed clear is the blouse pressed to finish.

**Deliverable (garment processing / intake log entry):**

> Item #4471, White Cotton/Silk Blend Blouse (60/40). Intake: wine stain (tannin, ~2cm, left cuff) and ballpoint ink stain (~1cm, right sleeve) documented, existing minor fabric pilling near left seam photographed pre-processing. Treatment: tannin remover diluted to 50% concentration (blend-appropriate, per manufacturer blended-fiber guidance); spot-tested inside left seam — no colorfastness issue. Wine stain treated and fully rinsed/neutralized before ink treatment began. Ink stain tested on inside hem — responded to alcohol-based solvent; treated accordingly. UV inspection post-treatment: no residual staining detected either area. Pressed and finished 2026-07-14. Both stains fully removed; no dye bleed or fiber damage observed.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled stain-sequencing worksheet, a fiber-sensitivity reference table, and an intake documentation checklist.
- [references/red-flags.md](references/red-flags.md) — signals an item needs extra caution or testing before processing, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (colorfastness, tannin vs. protein stains, and others).

## Sources

General knowledge of standard professional textile-care practice, including International Fabricare Institute (IFI)-style stain classification and sequencing conventions, and standard fiber-sensitivity guidance for blended fabrics in dry-cleaning and wet-cleaning operations.
