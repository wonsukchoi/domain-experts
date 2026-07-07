# Genetic Counselor — Playbook

## Bayesian risk-calculation worksheet template

| Step | Field | Value |
|---|---|---|
| 1 | Hypothesis A (e.g., "carrier") | — |
| 2 | Hypothesis B (e.g., "non-carrier") | — |
| 3 | Prior probability, Hypothesis A | — |
| 4 | Prior probability, Hypothesis B | — |
| 5 | Conditional evidence (what was observed) | — |
| 6 | P(evidence \| Hypothesis A) | — |
| 7 | P(evidence \| Hypothesis B) | — |
| 8 | Joint A = prior A × conditional A | — |
| 9 | Joint B = prior B × conditional B | — |
| 10 | Total = Joint A + Joint B | — |
| 11 | Posterior A = Joint A / Total | — |

## Scenario 1 — X-linked recessive, obligate carrier mother, unaffected sons

Consultand's mother is a confirmed obligate carrier. Consultand has *n* unaffected sons, no testing done on consultand herself.

- Prior (consultand is carrier): 1/2
- Conditional (n unaffected sons | carrier): (1/2)ⁿ
- Conditional (n unaffected sons | non-carrier): 1
- Posterior = (1/2 × (1/2)ⁿ) / [(1/2 × (1/2)ⁿ) + (1/2 × 1)]

| n (unaffected sons) | Posterior carrier risk |
|---|---|
| 1 | 1/3 ≈ 33.3% |
| 2 | 1/5 = 20.0% |
| 3 | 1/9 ≈ 11.1% |
| 4 | 1/17 ≈ 5.9% |

Each additional unaffected son moves the posterior meaningfully but never to zero — X-linked pedigree evidence alone cannot rule out carrier status, only reduce its probability. Direct carrier testing is the only way to reach near-certainty.

## Scenario 2 — Autosomal dominant with reduced penetrance

Consultand's parent carries a pathogenic variant with 70% penetrance by age 60 (i.e., 30% of carriers never develop the condition even by that age). Consultand is 45, unaffected, has not been tested.

- Prior (consultand inherited variant): 1/2 (standard AD transmission)
- Conditional (unaffected at 45 | carrier, using an age-adjusted penetrance curve — assume 40% penetrance by 45 for this condition): 1 − 0.40 = 0.60
- Conditional (unaffected at 45 | non-carrier): 1

| Hypothesis | Prior | Conditional | Joint |
|---|---|---|---|
| Carrier | 0.5 | 0.60 | 0.30 |
| Non-carrier | 0.5 | 1.00 | 0.50 |
| **Total** | | | **0.80** |

Posterior (carrier) = 0.30 / 0.80 = **37.5%**, down from 50% but still substantial — being unaffected at 45 in an incompletely penetrant condition is much weaker evidence than being unaffected in a fully penetrant one. Do not report this as "risk reduced to near zero"; the age-adjusted penetrance curve, not the observation alone, sets the ceiling on how much the unaffected status can move the number.

## Scenario 3 — Negative test result, no known familial variant

Consultand has a family history suggestive of hereditary breast/ovarian cancer syndrome, but no relative has had genetic testing (no known familial variant). Consultand undergoes a multi-gene panel; result is negative.

- Pretest risk (from pedigree/family-history risk model, e.g., Tyrer-Cuzick or similar): stated as a lifetime risk percentage from the model, not from panel results.
- Panel detection rate for the clinically suspected syndrome (varies by gene and syndrome; illustrative range 50–90% depending on which genes are covered and the family's specific presentation).
- Residual risk after negative panel = pretest risk × (1 − detection rate), **not** pretest risk × 0.

**Reporting rule:** state the residual risk explicitly ("your risk is reduced but not eliminated — approximately X% residual, because our panel does not explain all cases matching your family history") rather than "negative" alone, which most patients correctly hear as "no longer a concern."

## Cascade-testing / disclosure planning checklist

1. Identify every first- and second-degree relative for whom the result is actionable (would change their own testing or surveillance decision).
2. Ask the consultand who they plan to tell, in what order, and whether they want counselor-drafted family letters to share.
3. Flag relatives the consultand is estranged from or reluctant to contact — this is the most common point where cascade testing fails silently.
4. Note (verbally and in the chart) that most US jurisdictions impose no legal duty on the counselor to contact relatives directly; the consultand's own disclosure is the operative mechanism.
5. Offer a follow-up contact point in case a relative wants to reach the genetics service directly once informed.
