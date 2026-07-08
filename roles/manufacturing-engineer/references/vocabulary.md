# Vocabulary

Terms generalists flatten together that a manufacturing engineer keeps sharply separate — the value is in the misuse, not the definition.

## Cpk vs. Ppk

**Cpk** uses within-subgroup standard deviation (σ_within = R̄/d2) and assumes the process is already in statistical control — it answers "given this process stays as stable as it's been, how capable is it?" **Ppk** uses overall sample standard deviation with no in-control assumption — it answers "how did this specific run of parts actually perform?" Ppk is always equal to or lower than Cpk on the same data, because overall variation includes between-subgroup shifts that within-subgroup variation excludes.

**In use:** "This is a PPAP initial study — report Ppk, not Cpk, we don't have long-term control data yet."

**Common misuse:** using the two interchangeably, or reporting Cpk on an initial short-run study where the process hasn't demonstrated the long-term stability Cpk assumes.

## MMC / LMC

**Maximum Material Condition (MMC)** is the size limit where a feature contains the most material — the smallest permitted hole, or the largest permitted shaft/pin. **Least Material Condition (LMC)** is the opposite — the largest permitted hole, the smallest permitted shaft. GD&T position tolerances called out "at MMC" gain bonus tolerance as the feature departs from MMC toward LMC.

**In use:** "The hole's MMC is 0.375 — that's the smallest it's allowed to be, and it's the number the virtual condition calc starts from."

**Common misuse:** assuming MMC means "nominal" or "basic" size — it's a size *limit*, and for a hole that limit is the minimum, not the design target.

## Virtual condition

The worst-case boundary a mating part (or a fixture locator) must clear, combining a feature's MMC (or LMC) with its geometric tolerance at that material condition. For a position-toleranced hole: VC = MMC − position tolerance.

**In use:** "Size the locating pin to the hole's virtual condition, not its nominal diameter, or it'll bind on a part using its full bonus tolerance."

**Common misuse:** sizing a fixture locator or a mating part to the feature's nominal or basic dimension instead of its virtual condition, which doesn't account for the worst-case combination of size and position error the print actually permits.

## Bonus tolerance

Additional positional (or other geometric) tolerance a feature earns as its actual produced size departs from MMC toward LMC — because a larger-than-MMC hole has more room to accommodate position error before interfering with a mating part.

**In use:** "The hole measured 0.0015 over MMC, so it's carrying 0.0015 of bonus tolerance on top of the basic 0.008 position callout — total available is 0.0095."

**Common misuse:** treating the basic tolerance on the drawing as the only tolerance available, ignoring that an at-size or oversize feature (relative to MMC) is entitled to more.

## Datum reference frame (DRF)

The set of mutually perpendicular planes established by a part's designated datum features (A, B, C, in stated precedence), which fixes the coordinate system every other dimension and tolerance on the print is measured against.

**In use:** "The DRF is A primary, B secondary, C tertiary — the fixture has to lock those degrees of freedom in that order, not clamp wherever's convenient."

**Common misuse:** treating any three mutually perpendicular surfaces as equivalent to "the datums," when the print specifies which surfaces are A, B, and C and in what order they're applied — substituting a different surface changes what every other dimension is measured relative to.

## 3-2-1 locating principle

A workholding scheme that removes all six degrees of freedom from a part using three locators on the primary datum plane (removing 3 DOF), two on the secondary datum (removing 2 more), and one on the tertiary datum (removing the last), applied in that precedence.

**In use:** "Three buttons on datum A, the VC-sized pin in datum B, one edge locator on datum C — that's the full 3-2-1 scheme for this part."

**Common misuse:** describing any six-point-of-contact fixture as "3-2-1" without checking that the contact points actually correspond to the print's A/B/C datums in the correct precedence.

## GR&R (Gauge Repeatability & Reproducibility)

A structured study (per AIAG MSA) that separates total measured variation into part-to-part variation, repeatability (same operator, same gauge, same part, variation across trials), and reproducibility (different operators, same gauge and part, variation across operators) — expressed as %contribution or %study variation of the measurement system against total variation.

**In use:** "GR&R came back at 34% — requalify the gauge before we trust this capability study."

**Common misuse:** running a capability study first and only checking GR&R after the Cpk comes back marginal, instead of qualifying the measurement system up front — by then it's unclear whether the marginal number is the process or the gauge.

## PFMEA vs. RPN

A **Process FMEA** is a structured worksheet identifying process failure modes, their effects, and their causes, scored on severity, occurrence, and detection. **RPN (Risk Priority Number)** is the product of those three scores (1–1000) — a rough prioritization aid across failure modes of comparable severity, not a validated risk metric and not, on its own, a gate for whether an action is required.

**In use:** "Don't sort the PFMEA by RPN alone — pull every severity 9 or 10 line first, those need an action regardless of where they rank."

**Common misuse:** treating a single RPN threshold as the action trigger, which lets a high-severity, low-occurrence failure mode (low RPN, high consequence) slip through unaddressed.

## PPAP (Production Part Approval Process)

The AIAG-defined submission package (up to 18 elements, including the initial capability study, control plan, and dimensional results) a supplier submits to a customer to demonstrate a new or changed process is capable and ready for production.

**In use:** "This is a Level 3 PPAP submission — full package, including the Ppk study and the control plan, not just a sample and a cover sheet."

**Common misuse:** treating PPAP as a one-time paperwork event rather than a process-approval gate that gets re-triggered by significant process, material, or tooling changes (a PPAP-triggering event, per the customer's specific requirements).

## OEE (Overall Equipment Effectiveness)

A single metric decomposing equipment throughput loss into three independently diagnosable factors: Availability (downtime), Performance (speed loss), and Quality (defects/rework) — OEE = Availability × Performance × Quality.

**In use:** "OEE's at 70%, but Availability is fine at 0.85 — it's Performance and Quality dragging it down, so the fix is fixturing and capability, not a second machine."

**Common misuse:** treating OEE as a single number to improve in the abstract, rather than decomposing which of the three factors is actually binding before proposing a fix — the three losses have different root causes and different owners.

## Worst-case vs. RSS tolerance stacking

**Worst-case** tolerance stacking sums the absolute value of every contributor's tolerance (Σ|T_i|), guaranteeing fit across 100% of the population regardless of distribution. **RSS (root-sum-square)** stacking (√ΣT_i²) assumes each contributor is normally distributed and centered, and yields a smaller, statistically defensible stack — but only when every contributor has demonstrated capability to support that assumption.

**In use:** "All four contributors in this stack are running Cpk 1.4+, so RSS is defensible here — worst-case would be over-tightening tolerances a capable line doesn't need."

**Common misuse:** applying RSS by default without checking that every contributor actually has the capability data to support the normal-distribution assumption it relies on — RSS on an uncapable contributor understates real stack-up risk.

## DFM (Design for Manufacturability)

A structured review of a design against the capability of the candidate manufacturing process, before tooling or process commitment — checking whether called-out tolerances, features, and materials are achievable at the process's demonstrated capability.

**In use:** "DFM flagged this true-position callout as tighter than our milling process has ever demonstrated on a feature this size — escalate to design before we order the fixture."

**Common misuse:** running DFM as a one-time checklist pass at design release instead of a producibility check tied to actual capability data for the specific process and feature class being proposed.
