# Preventive medicine playbook

Filled examples for the three recurring work products: a screening-program go/no-go evaluation, an outbreak investigation sequence, and an occupational surveillance program structure.

## 1. Screening-program evaluation table

Populate this before recommending a screening program launch or continuation. Numbers below are a worked example for a hypothetical colorectal-cancer screening expansion in a 50,000-person county population, ages 45–75 (n = 14,200 eligible).

| Wilson–Jungner criterion | This program | Meets? |
|---|---|---|
| Condition is an important health problem | Colorectal cancer, county incidence 42/100,000/yr | Yes |
| Detectable latent/early symptomatic stage | Adenoma-to-carcinoma sequence, 10–15 yr window | Yes |
| Natural history adequately understood | Yes, well-characterized | Yes |
| Acceptable test to the population | FIT (fecal immunochemical test), no bowel prep | Yes |
| Test has acceptable sensitivity/specificity | Sens. ~79%, Spec. ~94% (single round) | Yes |
| Acceptable treatment exists for detected disease | Colonoscopy + resection, established | Yes |
| Cost is balanced against benefit | See CEA row below | Under review |
| Case-finding is a continuous process | Annual FIT built into program | Yes |

**Absolute-number translation (do this before any relative-risk claim reaches a readout):**

- Eligible population: 14,200. At 60% uptake: 8,520 screened.
- Expected FIT-positive at 5% positivity: 426 referred to colonoscopy.
- Expected colonoscopy yield at 3.5% PPV for advanced neoplasia in this population: ~15 true advanced neoplasia cases found; ~411 false positives absorbing a colonoscopy's small but real complication risk (perforation ~1/1,000–2,000 procedures).
- NNS (number needed to screen to prevent one CRC death over 10 years, per pooled FIT-program data): ~850–1,000.
- Cost-effectiveness: program cost per participant ~$45/yr (kit + follow-up colonoscopy allocation); modeled cost per QALY gained ~$18,000–$28,000 — inside the $50k–$150k benchmark band, supports launch.

**Verdict line (the actual deliverable for this table):** "Recommend launch at 60% uptake target. NNS ~900 over 10 years, cost/QALY ~$22,000, inside benchmark range. Primary risk is colonoscopy-arm capacity — 426 expected referrals/yr requires confirming GI endoscopy slots before public rollout, not after."

## 2. Outbreak investigation — CDC sequence with decision thresholds

Run in this order; each step's output gates the next. Do not skip to hypothesis testing before the denominator and case definition are locked.

1. **Establish the diagnosis** — confirm a consistent clinical/lab picture across the first 5–10 reported cases before calling it one entity.
2. **Verify the outbreak exists** — compare current case count against the same period's baseline for the prior 3–5 years; a rise inside normal seasonal variance is not an outbreak, it's a headline.
3. **Define a case** (confirmed / probable / suspect), fixed for the duration of the investigation — changing the definition mid-investigation without a documented note invalidates trend comparisons before and after the change.
4. **Find and count cases**, build the line list — one row per case, minimum fields: onset date, demographic, exposure history, lab status.
5. **Describe by person, place, and time** — construct the epidemic curve first. A single tight spike (one incubation period wide) → point-source hypothesis. A tail with secondary peaks spaced roughly one incubation period apart → propagated (person-to-person) hypothesis.
6. **Develop hypotheses** — from the descriptive data and open-ended interviews with the first 10–15 cases (hypothesis-generating, not confirmatory).
7. **Test hypotheses** — cohort study if the exposed population is well-defined and small (e.g., a wedding, a workplace); case-control if the exposed population is large or undefined (e.g., a community-wide foodborne event). Report odds ratio/relative risk with confidence interval, not a bare "associated with."
8. **Refine and re-test** as needed if the initial hypothesis doesn't explain the full case distribution.
9. **Implement control measures** — in practice these start as soon as a plausible vehicle/source is identified (step 6), not after step 8 confirms it; control and investigation run in parallel once a plausible mechanism exists.
10. **Communicate findings** — a written report to the health department/regulator with case definition, denominator, epi curve, hypothesis-testing result (OR/RR + CI), and control measures taken.

## 3. Occupational surveillance program structure — lead example

| Element | Specification |
|---|---|
| Action level | Airborne lead ≥30 µg/m³ (8-hr TWA) triggers periodic monitoring and medical surveillance enrollment |
| PEL | Airborne lead ≥50 µg/m³ (8-hr TWA) — engineering/administrative controls mandatory above this |
| Biological monitoring cadence | Every 6 months if BLL <40 µg/dL; every 2 months if BLL ≥40 µg/dL, until two consecutive results <40 |
| MRP trigger 1 | Single BLL ≥60 µg/dL |
| MRP trigger 2 | Average of last 3 BLLs ≥50 µg/dL, unless most recent single result ≤40 µg/dL |
| Return-to-exposure | Two consecutive BLLs ≤40 µg/dL |
| Rate/benefit protection during removal | Up to 18 months at full rate/benefits, per 1910.1025(k)(2) |
| Program review cadence | Quarterly comparison of site OSHA recordable incidence rate against NAICS benchmark, not against the site's own prior year alone |

**Escalation fallback order when a worker's BLL trend is rising but no single trigger has fired yet:** (1) shorten retest interval below the standard 6-month/2-month cadence; (2) request an industrial-hygiene exposure reassessment of that specific line/task; (3) recommend voluntary temporary reassignment while monitoring; (4) formal MRP removal once a trigger fires. Skipping straight to step 4 without documenting 1–3 invites a grievance that the removal was punitive rather than medically indicated; skipping 1–3 entirely when the trend is clearly rising is the more common and more dangerous failure.
