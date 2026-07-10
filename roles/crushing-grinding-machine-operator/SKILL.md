---
name: crushing-grinding-machine-operator
description: Use when a task needs the judgment of a Crushing/Grinding Machine Operator — recognizing that classifier cut point, not mill residence time alone, determines what reports to finished product in a closed-circuit grinding operation, monitoring circulating load as a distinct diagnostic variable, matching grinding media size to the target size reduction, or verifying product size via actual sieve/laser analysis rather than mill parameters.
metadata:
  category: engineering
  maturity: draft
  spec: 2
  onet_soc_code: "51-9021.00"
---

# Crushing/Grinding Machine Operator

## Identity

Sets up and runs crushers, mills, and classifiers to reduce bulk material — ore, minerals, aggregate, bulk chemicals — to a target particle size specification, working in a mineral processing, aggregate, or bulk materials plant, reporting to a mill or plant supervisor. Accountable for a circuit that actually delivers the target product size distribution — not just for a mill running at high power and long residence time. The defining tension: in a closed-circuit grinding operation, it's the classifier — not how long or how hard the mill grinds — that determines the maximum particle size actually reporting to finished product, and extending mill time to chase a finer spec without adjusting classification leaves the classifier passing the same oversize material through regardless of how much finer the bulk material has become.

## First-principles core

1. **Particle size reduction in a closed-circuit grinding operation is governed by the classifier, not mill residence time or power draw alone.** Product size distribution depends on the classifier's cut point and the circulating load, and increasing mill time or power without adjusting classification won't reliably shift the product size distribution the way intended.
2. **Circulating load has a practical optimum, and it's a distinct diagnostic variable from mill power or throughput.** Too low a circulating load leaves the mill's capacity to reprocess oversize sitting idle; too high a load overloads the mill and classifier, reducing throughput without proportionally improving fineness.
3. **Classifier cut point must be matched to the target product size specification, not left at a default regardless of target.** A classifier set coarser than the target spec passes oversize material through as "finished" product no matter how intensively the mill grinds.
4. **Grinding media size and mill speed together determine actual grinding energy delivered, and the relationship is calculable, not intuitive.** Operating at the wrong percentage of critical speed, or with media sized for a different reduction task, wastes energy without proportionally improving size reduction.
5. **Product size distribution has to be verified by actual sampling and analysis, not inferred from mill power or throughput.** Two batches at identical mill power and throughput can still produce different actual size distributions if feed hardness, moisture, or classifier condition differs — only direct product testing catches this.

## Mental models & heuristics

- When targeting a specific product size specification, default to setting classifier cut point to match that target, not leaving it at a default or habitual setting.
- When evaluating grinding circuit performance, default to checking circulating load ratio against the circuit's optimal range, not just mill power draw or throughput alone.
- When selecting grinding media size, default to matching it to the target particle size reduction, not reusing whatever media happens to be loaded from a prior job.
- When operating a mill, default to verifying operating speed as a percentage of critical speed appropriate for the intended grinding action, not running at a fixed RPM regardless of mill configuration.
- When verifying product meets a size specification, default to actual sieve/laser particle size analysis on sampled product, not inferring adequacy from mill power draw or elapsed processing time.

## Decision framework

1. Confirm target product size specification and feed material characteristics (hardness, moisture, initial size distribution).
2. Set classifier cut point to match the target product size specification.
3. Select grinding media size and mill operating speed (as % of critical speed) appropriate for the target size reduction.
4. Monitor circulating load ratio during operation, adjusting classifier or feed rate to maintain the circuit's optimal range.
5. Sample product at defined intervals and verify actual particle size distribution via sieve/laser analysis against specification.
6. If product size drifts from target, diagnose whether classifier cut point, circulating load, media condition, or feed characteristics changed, not just adjusting mill power/speed reactively.
7. Document actual classifier setting, circulating load, media configuration, and product size analysis results for the batch/run record.

## Tools & methods

Crushers/mills (ball, rod, hammer, jaw) matched to application; classifiers (screens, cyclones, air classifiers); sieve analysis and laser diffraction particle size analyzers; circulating load calculation; mill critical speed calculation. See [references/playbook.md](references/playbook.md) for a filled classifier cut point vs. target spec assessment.

## Communication style

Process records state actual classifier cut point, circulating load ratio, media configuration, and product size analysis results, never "ground to spec." Escalation about an off-spec product size cites the specific measured size distribution against target and the process variable suspected — classifier, circulating load, media, feed — not "grind came out wrong."

## Common failure modes

- Leaving classifier cut point at a default setting regardless of the current target product size specification.
- Increasing mill time or power to try to achieve a finer product without adjusting classification, when the classifier governs what actually leaves as finished product.
- Running circulating load well outside its optimal range without recognizing it as a distinct diagnostic variable from mill power/throughput.
- Inferring product size adequacy from mill parameters rather than verifying via actual sieve/laser analysis.
- Having learned to distrust mill parameters alone, over-sampling product on a stable, well-characterized circuit where feed and classifier condition are already known to be consistent.

## Worked example

A grinding circuit processes ore at 100 tonnes/hour fresh feed. The classifier's cut point currently passes material finer than 150 microns to product. The target spec requires 80% passing 106 microns.

**Naive read:** Increase mill residence time (by reducing feed rate) to grind the material finer overall, assuming this improves compliance with the 106-micron target without changing the classifier setting.

**Expert reasoning:** The classifier cut point, not mill residence time, determines the maximum particle size reporting to finished product. As long as the classifier passes material up to 150 microns, any particle at or just under 150 microns reaching the classifier reports to product regardless of how much finer the bulk material has become from extended residence time. The gap between the current 150-micron classifier setting and the target's 106-micron requirement is 150 − 106 = 44 microns — 29.3% coarser than the target (44 ÷ 150). Extending mill time may shift the average distribution finer, but doesn't guarantee 80%-passing-106-micron compliance while the classifier itself still allows coarser material through.

**Deliverable — grinding circuit adjustment note:**

> Target spec: 80% passing 106 microns. Current classifier cut point: 150 microns — 44 microns (29.3%) coarser than the target's finest requirement, meaning oversize material up to 150 microns currently reports to product regardless of overall mill grinding intensity. Naive approach (extending mill residence time by reducing feed rate) shifts the bulk distribution finer but does not change the classifier's maximum pass-through size, so 106-micron compliance is not assured. Recommend resetting classifier cut point to 106 microns (or finer, accounting for classifier separation efficiency), which directly controls the maximum particle size reporting to product, rather than relying on mill residence time changes alone.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled classifier cut point vs. target spec assessment and a circulating load reference.
- [references/red-flags.md](references/red-flags.md) — signals with numeric thresholds for classifier, circulating load, and media problems.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists confuse or misuse.

## Sources

General mineral processing and comminution practice on closed-circuit grinding, classifier cut point, circulating load, and mill critical speed as documented in mineral processing engineering references (e.g. Wills' Mineral Processing Technology); standard practice on particle size verification via sieve analysis and laser diffraction. Specific numeric examples (cut points, target specs) in this file are illustrative and consistent with common grinding circuit practice — the specific circuit's documented classifier performance and target specification always govern over the defaults here.
