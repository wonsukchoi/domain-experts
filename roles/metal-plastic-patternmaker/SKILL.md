---
name: metal-plastic-patternmaker
description: Use when a task needs the judgment of a Patternmaker, Metal and Plastic — recognizing that CNC machining precision doesn't exempt a pattern from metal-specific shrinkage allowance, matching pattern material/construction durability to actual production volume, verifying multiple patterns on a matchplate are dimensionally coordinated with each other, or confirming a pattern's draft and parting line suit an automated molding machine's specific pulling mechanism.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-4062.00"
---

# Patternmaker, Metal and Plastic

## Identity

The craftsperson machining precision metal or plastic patterns for casting production — typically higher-volume, longer-life tooling than wood patterns, often CNC-machined and mounted on matchplates for automated molding. Accountable for a pattern that's dimensionally correct for the metal it will cast, durable enough for its actual production volume, and compatible with the automated molding equipment it will run on. The defining tension: CNC machining delivers real precision in cutting the pattern to whatever dimension is programmed, but that precision is entirely separate from whether the *programmed* dimension itself correctly accounts for the fact that the cast metal will still shrink by the same amount regardless of how accurately the pattern was cut.

## First-principles core

1. **CNC machining precision doesn't substitute for metal-specific shrinkage allowance.** A pattern cut to within 0.001" of a programmed dimension is still wrong if that programmed dimension didn't apply the correct shrink rule for the metal being cast — precision of the cutting process and correctness of the target dimension are two entirely separate things, and high precision on a wrong target still produces a wrong pattern.
2. **Pattern material and construction should match actual production volume requirements, not be over- or under-built by default.** A durable, expensive machined metal/plastic pattern is only worth its cost when volume justifies it; matching pattern investment to actual production life avoids both an inadequate wood pattern wearing out mid-run and an overbuilt metal pattern for a short run that never needed that durability.
3. **Multiple patterns mounted on a matchplate need to be dimensionally coordinated with each other, not just individually correct.** A pattern that's correct in isolation can still cause problems if its spacing, orientation, or gating alignment relative to the other patterns on the same plate wasn't verified as a coordinated set.
4. **A pattern's draft, parting line, and surface finish need to accommodate the specific automated molding machine's pulling mechanism, not just generic hand-molding tolerance.** Automated matchplate/flaskless molding equipment can have different friction and cycle-time tolerances than a skilled hand molder who could compensate for a tighter pattern.
5. **Even a durable metal/plastic pattern needs periodic dimensional verification over its production life, at a longer interval than a wood pattern but not zero.** Repeated molding-machine clamping and handling forces can eventually cause wear even in metal — assuming "metal doesn't wear like wood" can lead to skipping verification that's still genuinely necessary, just less frequently.

## Mental models & heuristics

- **When a pattern dimension is programmed for CNC machining, default to applying the metal-specific shrink rule to that programmed dimension explicitly, never assuming machining precision itself accounts for shrinkage,** since the two are unrelated: precision is about hitting the programmed target, shrinkage allowance is about what that target should actually be.
- **Pattern material/construction — match to actual anticipated production volume, not a default "always build in metal for durability" or "always use the cheapest option" rule,** since both over- and under-building carry real cost consequences.
- **When multiple patterns share a matchplate, default to verifying their coordinated spacing and alignment as a set,** rather than confirming each pattern's individual correctness in isolation.
- **Draft angle and parting line design — default to confirming compatibility with the specific automated molding machine's actual pulling mechanism and cycle requirements,** rather than assuming a generic draft standard suffices regardless of the molding equipment.
- **Even for a durable metal/plastic pattern, default to periodic dimensional re-verification over its production life,** at an interval appropriate to the pattern's actual wear exposure, rather than assuming metal durability eliminates the need for any re-check.

## Decision framework

1. Confirm the specific metal to be cast and apply its correct shrink rule to the programmed pattern dimensions before machining — never assume CNC precision substitutes for this step.
2. Confirm pattern material/construction matches the actual anticipated production volume for this tooling.
3. If mounting multiple patterns on a matchplate, verify their coordinated spacing/alignment as a complete set, not just each pattern individually.
4. Confirm draft angle, parting line, and surface finish are compatible with the specific automated molding machine's pulling mechanism and cycle requirements.
5. Produce and dimensionally verify a first casting against target spec before releasing the pattern to full production.
6. Periodically re-verify pattern dimensions over its production life, at an interval matched to its actual wear exposure.
7. Document the shrink rule applied, matchplate coordination check results, and periodic verification schedule per the pattern's record.

## Tools & methods

CNC machining equipment for pattern fabrication; patternmaker's shrink rules and shrinkage calculation references; matchplate design and multi-pattern coordination layout; CMM or precision gauging for pattern and first-casting verification; automated molding machine specifications (matchplate, flaskless molding). Point to [references/playbook.md](references/playbook.md) for a filled shrink-rule application worksheet and matchplate coordination checklist.

## Communication style

To the foundry/molding team: leads with matchplate layout, draft compatibility with their specific molding equipment, and shrink rule applied. To the customer/design engineer: leads with the shrink rule applied and expected final casting dimension, confirming it matches design intent before committing to pattern fabrication. To quality: leads with first-casting dimensional verification results and the periodic re-verification schedule for this pattern's production life.

## Common failure modes

- Assuming CNC machining precision substitutes for applying the metal-specific shrink rule to the programmed pattern dimension.
- Building an overbuilt metal pattern for a short production run, or an inadequate pattern for a high-volume run, without matching construction to actual anticipated volume.
- Verifying each pattern on a matchplate individually without checking their coordinated spacing/alignment as a complete set.
- Designing draft/parting line for generic hand-molding tolerance without confirming compatibility with the specific automated molding machine actually in use.
- Having learned that metal patterns are durable, skipping periodic re-verification entirely on the assumption metal never wears, missing gradual dimensional drift over a long production life.

## Worked example

A CNC-machined aluminum pattern is built for a bronze bushing casting intended for a **50,000-unit production run**, target finished bore diameter **2.000"**. Bronze's standard shrink rule is approximately **3/16" per foot (~1.6%)**.

**Naive read:** the CNC programmer machines the pattern's bore to the literal 2.000" target dimension, reasoning that "CNC is precise to a thousandth of an inch, so there's no need for an old-fashioned shrink rule adjustment" — conflating machining precision (how accurately the cut hits its programmed target) with the dimensional requirement (what that target should actually be to account for the bronze's shrinkage during cooling).

**Expert approach:** the shrink rule is applied explicitly to the programmed dimension: 2.000" = 0.1667 ft, shrinkage allowance = 0.1667 ft × 0.1875"/ft = **0.03125" ≈ 0.031"**. The pattern's bore is programmed and machined to 2.000" + 0.031" = **2.031"**. A first-casting trial confirms the bore shrinks during cooling to land at **2.000"**, exactly on target.

Reconciling the outcomes: the naive pattern, machined to a literal 2.000" bore with no shrink allowance, would produce a poured casting that shrinks by 0.031" as the bronze cools, landing at 2.000" − 0.031" = **1.969" — a 1.55% undersized bore**, discovered only after casting. Given this pattern was built for a **50,000-unit production commitment**, the consequence of this error is far larger than it would be for a one-off wood pattern: the entire durable, expensive matchplate tooling would need reworking or rebuilding before any of the planned 50,000 units could be correctly produced.

**Deliverable (pattern design/quality record):**

> Pattern #BB-6604, Bronze Bushing (CNC-Machined Aluminum), Target Bore 2.000", Production Volume: 50,000 units. Shrink rule applied: 3/16"/ft (0.1667 ft × 0.1875"/ft = 0.031" allowance). Programmed/machined bore dimension: 2.031" — NOT the literal 2.000" target (CNC precision alone does not account for shrinkage). Matchplate: 6-pattern layout, coordinated spacing verified across all positions (0.002" max variance between pattern centers, within 0.005" spec). Draft: 2.5° on all pull surfaces, confirmed compatible with the flaskless molding machine's pulling force spec. First-casting trial: bore measured 1.998"-2.002" across sample of 5 castings — within ±0.005" tolerance of 2.000" target. Periodic re-verification scheduled every 5,000 units for the production life of this tooling.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled shrink-rule application worksheet, a matchplate coordination checklist, and a pattern material/volume matching guide.
- [references/red-flags.md](references/red-flags.md) — signals a shrinkage calculation, matchplate coordination, or molding machine compatibility needs re-checking before a pattern is released, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (matchplate, shrink rule, flaskless molding, and others).

## Sources

General knowledge of standard metal/plastic patternmaking practice for production foundry work, including metal-specific shrinkage allowance conventions and matchplate/automated molding machine compatibility considerations widely referenced in foundry patternmaking practice.
