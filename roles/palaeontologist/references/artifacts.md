# Palaeontologist artifacts — templates with real structure

Working templates an agent can fill in. Numbers below are independent worked examples (different localities/taxa from the SKILL.md worked example) so the reasoning pattern can be checked against a second instance.

## 1. Fossil-prep triage table under a fixed lab-hour budget

A field season returns 11 jackets to the prep lab against a hard budget of **220 lab-hours** for the quarter (one full-time preparator at ~55 hr/month × ~4 months, minus ~15% overhead for equipment/training). Triage ranks by diagnostic value per hour, not specimen size or exhibit appeal.

| Jacket # | Probable taxon | Element(s) | Est. prep hours | Diagnostic value | Priority tier |
|---|---|---|---|---|---|
| PMU-24-002 | cf. *Tyrannosaurus* sp. | partial dentary w/ 6 teeth in situ | 42 | High — cranial, taxon-diagnostic | 1 |
| PMU-24-007 | Ceratopsidae indet. | juvenile frill w/ epoccipitals | 30 | High — ontogenetic series value | 1 |
| PMU-24-011 | cf. *Edmontosaurus* sp. | partial braincase | 35 | High — cranial | 1 |
| PMU-24-004 | Hadrosauridae indet. | associated forelimb (radius, ulna, mc) | 26 | Medium — postcranial, referable | 2 |
| PMU-24-009 | Testudines indet. | partial carapace | 18 | Medium — taxon-referable | 2 |
| PMU-24-013 | cf. *Tyrannosaurus* sp. | isolated shed tooth | 4 | Medium — confirms taxon presence | 2 |
| PMU-24-001 | Dinosauria indet. | isolated rib shaft fragment | 20 | Low — not diagnostic below Dinosauria | 3 |
| PMU-24-005 | Dinosauria indet. | vertebral centrum, eroded | 16 | Low — non-diagnostic | 3 |
| PMU-24-014 | Dinosauria indet. | long-bone shaft fragment | 22 | Low — non-diagnostic | 3 |
| PMU-24-008 | Dinosauria indet. | rib fragment | 14 | Low — non-diagnostic | 3 |
| PMU-24-012 | Dinosauria indet. | indeterminate bone fragment | 10 | Low — non-diagnostic | 3 |

**Tier 1 total:** 107 hrs. **Tier 1+2 total:** 155 hrs. **All 11 jackets:** 237 hrs — 17 hrs over budget.

**Triage decision:** fully prep Tier 1 (107 hrs) and Tier 2 (48 hrs) = 155 hrs, leaving 65 hrs. Of Tier 3 (82 hrs total), prep only PMU-24-001 and PMU-24-005 (36 hrs, the two largest/most complete fragments, kept as locality-presence vouchers) and leave PMU-24-014, PMU-24-008, PMU-24-012 (46 hrs) in stabilized, unopened jackets in long-term storage with full field data attached, flagged for next season — never discarded, since a fragment non-diagnostic today can become referable once better material from the same taxon is described.

## 2. Age-reconciliation worksheet (blank-filled template, second locality)

For a section with two dated ash beds bracketing a fossil horizon:

| Field | Value |
|---|---|
| Ash bed below (age, method) | 34.812 ± 0.015 Ma, CA-ID-TIMS U-Pb zircon |
| Ash bed above (age, method) | 34.298 ± 0.021 Ma, CA-ID-TIMS U-Pb zircon |
| Stratigraphic thickness, ash-below to ash-above | 41.6 m |
| Fossil horizon height above lower ash | 9.8 m |
| Fraction of interval | 9.8 / 41.6 = 0.2356 |
| Interpolated age | 34.812 − 0.2356 × (34.812 − 34.298) = 34.812 − 0.1211 = **34.69 Ma** |
| Biostratigraphic zone estimate (independent) | 34.9–34.5 Ma (regional mammal biozone) |
| Reconciled? | Yes — interpolated age (34.69 Ma) falls inside the independent biozone range; no reworking flag needed. |

**Rule:** run this reconciliation *before* publication whenever a fossil-bearing horizon has both a radiometric bracket and a biostratigraphic estimate — report the interpolated age as primary and the biozone as a corroborating check, never average the two.

## 3. Taxonomic-assignment memo: ontogeny vs. new species (morphometric)

**Setup.** Twelve new trilobite specimens (Family Phacopidae) are recovered spanning multiple growth (instar) stages, alongside the known comparison species *Eldredgeops rana*, whose glabella length/width (L/W) ratio at maturity (holaspid stage) is documented in the literature as 1.15–1.35 (n = 45 measured specimens, published range). The new material's holaspid-stage mean L/W = 1.48 (n = 5, SD 0.06) — outside the published range for *E. rana*, prompting a draft manuscript proposing a new species.

**Ontogenetic series measured across all 12 specimens:**

| Instar stage | n | Mean glabella L/W | SD |
|---|---|---|---|
| Early meraspid | 2 | 1.71 | 0.04 |
| Late meraspid | 3 | 1.59 | 0.05 |
| Early holaspid | 2 | 1.53 | 0.03 |
| Mature holaspid | 5 | 1.48 | 0.06 |

**Reasoning.** The L/W ratio decreases monotonically and smoothly across every growth stage (1.71 → 1.59 → 1.53 → 1.48), consistent with a continuous allometric growth trajectory, not a step change. Comparing against *E. rana*'s own published ontogenetic series (not just its adult range) shows the same allometric slope and a parallel, offset trajectory — the new material's holaspid ratio sits about 0.13–0.15 above *E. rana*'s at every equivalent stage, a consistent offset rather than a convergent endpoint. Because the offset holds across the entire growth series rather than appearing only in one stage, ontogeny alone does not explain it — this is evidence for a genuine, stable interspecific difference, not an artifact of comparing mismatched growth stages.

**Deliverable — taxonomic memo excerpt:**

> **Memo: Species Status of the [Locality YY] Phacopid Material**
>
> Twelve specimens spanning four growth stages show a glabella L/W trajectory (1.71 → 1.48 across meraspid to mature holaspid) parallel in slope to, but offset by 0.13–0.15 from, the published *Eldredgeops rana* ontogenetic series at every equivalent stage. Because the offset is consistent across the full growth series rather than confined to one stage, it cannot be attributed to comparing mismatched ontogenetic stages or to normal intraspecific allometric variation.
>
> **Conclusion:** the sample supports recognition as a distinct species. A new species diagnosis is warranted, conditioned on (a) designating the most complete mature holaspid specimen (field no. [XX]) as holotype, and (b) explicitly figuring the full ontogenetic series in the description so future workers can replicate the growth-trajectory comparison rather than relying on adult measurements alone.
