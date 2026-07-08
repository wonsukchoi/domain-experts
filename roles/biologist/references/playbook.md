# Biologist — Playbook

Filled worksheets for the three recurring executed processes: power analysis before locking sample size, IACUC/IBC/permit sequencing before scheduling work, and unit-of-analysis assignment before running statistics.

## 1. Power-analysis worksheet

Fill every row before a sample size goes into a protocol or grant. Two-sample comparison, α = 0.05 two-tailed, target power = 0.80 unless stated otherwise.

| Field | Entry (worked example: prenatal exposure / brain weight) |
|---|---|
| Outcome measure | Offspring brain weight (mg), one value per litter |
| Experimental unit | Dam/litter (treatment randomized at the dam) |
| Prior/pilot SD (pooled) | σ = 18 mg, from a prior cohort (n = 6 litters, unpublished pilot) |
| Minimum effect of interest | Δ = 14.4 mg → Cohen's d = 14.4 / 18 = **0.8** |
| α (two-tailed) | 0.05 |
| Target power | 0.80 |
| Required N per arm (table/software lookup) | **≈26** |
| N actually available (budget/animal cap) | 5 dams/arm (initial ask) |
| Achieved power at available N | δ = d·√(n/2) = 0.8·√(5/2) = 1.265; z = 1.265 − 1.96 = −0.695; power ≈ Φ(−0.695) ≈ **0.24** |
| Decision | Under-powered — escalate to ≥26/arm, or accept and report ≈24% achieved power explicitly, never as "adequately powered" |

Quick-reference table, two-sample t-test, α = 0.05 two-tailed, power = 0.80 (standard benchmark, not derived per-study):

| Cohen's d | Required N per arm |
|---|---|
| 0.2 (small) | ≈393 |
| 0.5 (medium) | ≈64 |
| 0.8 (large) | ≈26 |
| 1.0 (very large) | ≈17 |

Fallback ladder when the table N exceeds what's fundable/ethical, in preference order:
1. Reduce variance first — tighter husbandry/protocol control, repeated-measures or crossover design, better instrument precision — then recompute required N.
2. Increase the minimum effect of interest only if a smaller true effect genuinely wouldn't matter biologically or clinically — never inflate it just to shrink the N formula spits out.
3. Accept the achievable N and report the achieved power number in the protocol and any resulting manuscript, flagged as a design limitation.
4. Propose a multi-site or multi-cohort pooled design (with site/cohort as a random effect) to reach N without exceeding any single site's animal cap.

## 2. IACUC / IBC / permit sequencing checklist

Sequence — not parallel tracks. Each gate blocks the step below it; nothing below a gate starts before that gate clears.

| Step | Action | Typical lead time | Gate before next step |
|---|---|---|---|
| 1 | Draft protocol: species, procedures, endpoints, N with power-analysis justification, 3Rs statement | 1–2 weeks to draft | Internal PI/co-author review sign-off |
| 2 | Submit to IACUC (vertebrate/invertebrate animal work) | 4–8 weeks committee review, full-board if >minimal pain/distress | IACUC approval letter with protocol number |
| 2b | If recombinant/synthetic nucleic acids or BSL-2/BSL-3 organism involved: submit to IBC in parallel with IACUC (independent committees, can run concurrently with each other, not with bench work) | 3–6 weeks | IBC approval letter with registration number |
| 3 | If field sampling from wildlife: submit federal collecting permit (USFWS ePermits or equivalent) + biologist resume/CV | **≥30 days before planned start date** — hard floor, not a target | Federal permit number issued |
| 4 | Submit state scientific-collector permit, citing the federal permit number from step 3 | 2–4 weeks after federal permit in hand | State permit issued |
| 5 | Order animals/reagents, schedule facility time, train personnel on approved procedures | — | All applicable approvals (IACUC + IBC + federal + state, as relevant) on file |
| 6 | Begin data collection | — | — |

Red-line rule: any data collected before the relevant protocol number/permit number is issued is presumptively unusable for publication or regulatory submission, regardless of scientific quality — do not backdate a schedule to make step 6 look like it followed step 2/3/4.

## 3. Unit-of-analysis worked table

Use to convert raw measurements into the correct N before running any test. Worked example continues the prenatal-exposure study: 5 dams/arm, 2 pups sampled per litter, each pup's brain weighed 5 times.

| Level | Count | Independent? | Use in analysis? |
|---|---|---|---|
| Raw weighings | 5 dams × 2 pups × 5 weighings = 50/arm | No — same pup, same brain, repeat instrument reads | No — collapse to one value per pup first (mean of 5 reads) |
| Pups | 5 dams × 2 pups = 10/arm | No — littermates share genetics + prenatal environment | No — collapse to one value per litter, or model as a random effect nested in litter |
| Litters (dams) | 5/arm | **Yes** — treatment was randomized at the dam | **Yes — this is N** |

Two acceptable analysis paths, in preference order:

1. **Litter-mean approach (simple, low power):** average the 10 pup-level means (each itself an average of 5 weighings) up to one number per litter → 5 values per arm → two-sample t-test or Mann-Whitney on n=5 per arm.
2. **Mixed-effects model (preferred when litter-level N is small and pup-level covariates matter):** `brain_weight ~ treatment + (1 | dam_id)`, fit in R (`lme4::lmer`), with litter/dam as the random-effect grouping variable. Denominator degrees of freedom for the treatment effect come from the number of dams, not from 50 pooled weighings: 5 dams/arm × 2 arms = 10 dams total, minus 2 (one per group mean) = **8 dam-level df** (Satterthwaite/Kenward-Roger approximation) — reviewers should see this df explicitly stated, since a df near 50 in the model output is a tell that pseudoreplication leaked back in.

Common wrong model to flag in review: `lm(brain_weight ~ treatment)` fit directly on the 50-row pooled dataset — this returns a treatment-effect p-value with df = 50 − 2 = 48, which overstates precision by roughly 6x relative to the true 8 dam-level degrees of freedom.
