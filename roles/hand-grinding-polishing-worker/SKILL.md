---
name: hand-grinding-polishing-worker
description: Use when a task needs the judgment of a Hand Grinding and Polishing Worker — deciding whether sustained grinding contact on hardened material risks invisible temper drawing, following an abrasive grit progression without skipping stages, checking dimensions frequently on a tight-tolerance part during hand-finishing, or dedicating grinding media to a specific metal type to prevent cross-contamination corrosion.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-9022.00"
---

# Hand Grinding and Polishing Worker

## Identity

The worker manually grinding and polishing parts to a specified dimension and surface finish, accountable for a finished surface that's both dimensionally correct and free of hidden defects a visual pass wouldn't catch — heat-induced softening on hardened steel, cross-contamination corrosion between dissimilar metals, or a scratch pattern buried under a polished-looking surface. The defining tension: hand work is inherently less precise and less controlled than machine processing, and the temptation to work faster with heavier, sustained contact directly increases the risk of defects that don't show up until well after the part passes its immediate visual and dimensional check.

## First-principles core

1. **Hand grinding generates localized heat that can alter material properties invisibly.** Sustained contact or excessive pressure on hardened steel can locally draw temper — soften the material — at the exact spot ground, producing a part that looks and measures correctly but has reduced hardness at that specific location, undetectable without a hardness test.
2. **Abrasive grit sequence must progress through intermediate steps, not jump from coarse to fine.** Each grit stage removes the scratch pattern left by the previous, coarser stage; skipping a step leaves scratches too deep for the next, much finer grit to remove efficiently — producing a surface that looks polished on top while retaining defects underneath.
3. **Material removal by hand is imprecise compared to machine grinding, and this imprecision compounds on close-tolerance parts.** Uneven pressure or dwell time can remove more material in one area than another, and on a part with tight dimensional tolerance, this variability itself can push the part out of spec even if the "average" material removed seems correct.
4. **Cross-contamination between dissimilar metals via shared grinding media causes a specific, delayed failure mode.** Using the same wheel or belt on both carbon steel and stainless steel embeds iron particles into the stainless surface, which later rust — visible surface corrosion appearing even though the stainless part itself hasn't structurally failed.
5. **A part's surface finish specification and dimensional tolerance can interact, and both under- and over-finishing create problems.** An under-finished surface fails functional spec; over-finishing wastes time and can remove more material than a tight tolerance allows — treating finish and dimension as independent constraints misses this interaction.

## Mental models & heuristics

- **When hand-grinding hardened steel, default to light, intermittent contact and checking for heat buildup rather than sustained heavy pressure,** since localized overheating can draw temper invisibly — the absence of visible discoloration doesn't guarantee no heat-affected softening occurred.
- **Abrasive grit progression — follow the specified sequence without skipping stages, even when a coarser jump seems like it would save time,** since skipping a stage leaves a scratch pattern the next stage can't efficiently remove.
- **When hand-finishing a part with a tight dimensional tolerance, default to more frequent dimensional checks during the process rather than relying on visual/tactile judgment alone,** since hand-grinding's inherent unevenness compounds on tight-tolerance work.
- **Grinding/polishing media — dedicate specific media to specific metal types rather than sharing across dissimilar metals,** since cross-contamination causes a delayed corrosion defect that isn't visible until well after the part ships.
- **When a part has both a surface finish spec and a tight dimensional tolerance, default to treating them as interacting constraints — the finishing process has to stay within the dimensional allowance,** rather than optimizing surface finish without checking its cumulative effect on dimension.

## Decision framework

1. Confirm the part's material, dimensional tolerance, and surface finish specification before starting, along with whether the material is heat-sensitive (hardened/tempered).
2. Select and dedicate grinding/polishing media appropriate to this specific material, avoiding any media previously used on a dissimilar metal.
3. For heat-sensitive material, use light/intermittent contact and monitor for heat buildup throughout grinding.
4. Follow the specified abrasive grit progression in sequence without skipping stages.
5. For tight-tolerance parts, check dimensions frequently during the process, not only at the end, to catch excessive or uneven material removal early.
6. Finish to the specified surface roughness/grit target — neither stopping short nor continuing past it, especially where dimensional tolerance constrains how much finishing is possible.
7. Document material, media used, and any heat/dimensional checks performed per the job's quality record.

## Tools & methods

Hand-held grinders; polishing wheels and belts with graduated abrasive grits; surface roughness comparators or profilometers; hardness testing for heat-sensitive material verification; dimensional gauging; dedicated media tracking by material type. Point to [references/playbook.md](references/playbook.md) for a filled heat-sensitive grinding checklist and grit progression reference table.

## Communication style

To quality: leads with actual surface finish measurement and any dimensional check results, not just "part looks polished." To the next worker continuing a multi-stage finishing job: leads with the current grit stage completed and any known heat-sensitive areas already worked. To a supervisor if a heat-sensitive part shows discoloration: leads with the specific location and immediately flags for hardness verification before the part proceeds.

## Common failure modes

- Applying sustained heavy pressure on hardened steel, risking invisible temper drawing at the ground location.
- Skipping an abrasive grit stage to save time, leaving a scratch pattern the next stage can't efficiently remove.
- Relying on visual/tactile judgment alone for material removal on a tight-tolerance part instead of frequent dimensional checks.
- Using the same grinding/polishing media across dissimilar metals, causing cross-contamination corrosion.
- Having learned to check for heat buildup, over-pausing/under-working non-heat-sensitive materials out of unnecessary caution, reducing productivity without a corresponding quality benefit.

## Worked example

A hardened tool steel part (spec hardness Rockwell C 58-62) requires hand-finish grinding to remove 0.003" of stock per side on a critical surface after heat treatment, held to ±0.001" dimensional tolerance, followed by polishing to a specified 16 Ra surface finish.

**Naive read:** the worker applies firm, sustained pressure with a hand grinder to remove stock quickly, working one small area continuously for an extended period without pausing, reasoning that since there's no visible discoloration, the part isn't overheating. Stock removal completes at 0.003" (within tolerance) in an estimated 90 seconds of continuous contact, and the part passes visual and dimensional inspection before polishing.

**Expert approach:** sustained heavy grinding contact on hardened tool steel risks localized temper drawing even without visible discoloration — visible tempering colors (blue, straw) typically indicate temperatures already well past the point where some softening has occurred, and modern high-speed grinding can generate brief, very localized high temperatures that produce heat-affected softening without any visible color change. Light, intermittent contact is used instead, with frequent lift-off allowing heat to dissipate and periodic touch-checks for excessive heat (too hot to comfortably touch = stop and cool). The same 0.003" stock removal is achieved over roughly **4 minutes of intermittent contact — about 2.7x longer** than the naive continuous approach — a real time cost accepted specifically to avoid an undetected soft spot. Because this is a critical hardness-spec surface, the part is also flagged for a hardness verification check (a Rockwell test at an inconspicuous location per the quality plan) before release, rather than relying on dimensional and visual pass alone.

**Deliverable (quality/finishing log entry):**

> Part #TS-4471, Hardened Tool Steel, Critical Surface. Stock removal: 0.003"/side (spec, ±0.001" tolerance) via light/intermittent hand grinding contact, ~4 min total with cooling pauses (vs. estimated 90 sec if run continuously — time cost accepted to avoid heat-affected softening risk). No visible discoloration observed at any point. Post-grind hardness verification: Rockwell C 60 at ground surface (spec: 58-62) — CONFIRMED, not assumed from absence of discoloration alone. Cleared for polishing per grit progression 220→400→600→800 (16 Ra target). Dedicated stainless-safe media used throughout — no cross-contamination risk (this part is carbon tool steel; media not shared with any stainless-steel jobs on this bench).

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled heat-sensitive grinding checklist, a grit progression reference table, and a media dedication tracking guide.
- [references/red-flags.md](references/red-flags.md) — signals a heat, grit-sequence, or cross-contamination issue needs attention before a part is released, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (temper drawing, Ra roughness, cross-contamination, and others).

## Sources

General knowledge of standard hand-finishing, grinding, and polishing practice in metalworking, including heat-affected zone risk in hardened steel grinding and cross-contamination corrosion conventions in stainless steel finishing.
