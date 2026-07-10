# Political Scientist — Artifacts

## Poll-weighting worksheet (filled)

**Question:** State Attorney General race, 14 days out. Six polls released in the last 10 days.

| Poll | House | n | Mode | Sponsor | Quality weight | Margin (A − B) | n × weight |
|---|---|---|---|---|---|---|---|
| P1 | Meridian Research | 900 | Live-caller | None (media) | 1.0 | +5 | 900 |
| P2 | Cobalt Insights | 650 | IVR/text | None (media) | 0.85 | +1 | 552.5 |
| P3 | Harbor Analytics | 700 | Online panel | Candidate A's campaign | 0.3 | +9 | 210 |
| P4 | Pinegrove Polling | 1,100 | Live-caller | None (university) | 1.0 | +3 | 1,100 |
| P5 | Redline Metrics | 480 | Online panel | None (media) | 0.6 | −2 | 288 |
| P6 | Cobalt Insights (repeat) | 600 | IVR/text | None (media) | 0.85 | +2 | 510 |

**Weighted margin:**

```
Σ(n × weight × margin) = 900(5) + 552.5(1) + 210(9) + 1,100(3) + 288(−2) + 510(2)
                        = 4,500 + 552.5 + 1,890 + 3,300 − 576 + 1,020
                        = 10,686.5
Σ(n × weight)           = 900 + 552.5 + 210 + 1,100 + 288 + 510 = 3,560.5
Weighted margin          = 10,686.5 / 3,560.5 = +3.0
```

**Nominal-vs-effective uncertainty:** average reported MOE across the six polls ≈ ±3.8. Per Shirani-Mehr et al. (2018), treat effective SE on the margin as roughly double the sampling-only figure once nonresponse and weighting error are folded in — use ≈±6.5 for the win-probability calculation, not the ±3.8 nominal figure.

**Win probability:** z = 3.0 / 6.5 = 0.46, Φ(0.46) ≈ 0.68 — call it "lean A," not "toss-up" and not "safe."

**Rule for excluding vs. downweighting a sponsored poll:** downweight (0.2–0.4×) rather than drop entirely if the house also publishes independent, non-sponsored work with a track record; drop entirely only if the house has no track record outside campaign-commissioned work, since there's then no basis for any quality weight above zero.

## Most-similar-systems comparison table (filled)

**Question:** Does compulsory voting increase policy responsiveness to low-income voters' stated preferences?

Case selection: pairs of countries similar on federalism, party-system type, and development level, differing on compulsory-voting status.

| Dimension | Australia (compulsory) | Canada (voluntary) | Chile pre-2012 (compulsory) | Chile post-2012 (voluntary) |
|---|---|---|---|---|
| Federal structure | Federal | Federal | Unitary | Unitary |
| Party system | Two-and-a-half party | Multi-party, regionalized | Multi-party coalition blocs | Multi-party coalition blocs |
| GDP per capita band | High-income | High-income | Upper-middle→high | Upper-middle→high |
| Turnout | ~91% (2019) | ~62% (2021) | ~87% pre-2012 | ~47% post-2012 |
| Income-turnout gap (top vs. bottom quintile) | ~4pp | ~19pp | ~6pp pre-2012 | ~24pp post-2012 |

**Within-case leverage:** Chile's own 2012 reform (compulsory → voluntary, same institutions, same party system) is the strongest cell in the table — it isolates the compulsory-voting variable from every cross-national confound the Australia/Canada pair still carries. Lead with the Chile before/after comparison; use Australia/Canada as corroborating cross-national evidence, not the primary claim.

**Reported finding (illustrative structure, not a live estimate):** income-turnout gap widened from ~6pp to ~24pp after Chile's 2012 switch to voluntary voting — consistent with the compulsory-voting-narrows-the-gap hypothesis, though the reform also coincided with an automatic-registration change that itself could explain part of the shift; the writeup states this confound explicitly rather than absorbing it into the topline number.

## Process-tracing evidence log (filled)

**Case:** Did austerity conditionality (vs. domestic fiscal preference) drive Country X's 2015 pension-age increase?

| Evidence | Type | Result | Interpretation |
|---|---|---|---|
| Finance ministry internal memo (leaked, dated 4 months pre-reform) already modeling pension-age increase before creditor talks began | Hoop test (necessary for "domestic-driven" story) | Passed | Domestic-driven hypothesis survives; doesn't confirm it, but its absence would have killed it |
| Creditor negotiation transcript explicitly listing pension age as a named, numbered conditionality term | Smoking-gun test (sufficient for "conditionality-driven" story) | Passed | Strong confirming evidence for conditionality having independent causal weight, regardless of the domestic memo |
| Public statements from ruling coalition citing pension age as a longstanding manifesto commitment | Straw-in-the-wind (weak on its own) | Present | Corroborating but not probative alone — cheap talk in the run-up to negotiations |

**Conclusion drafted from the log:** both hoop and smoking-gun tests passed — the evidence supports a **conjunctural** account (domestic preference pre-existed and provided the reform the government wanted anyway; conditionality provided the political cover and the specific numeric target) over either single-cause story. State this as the finding rather than picking the more dramatic single-cause narrative the straw-in-the-wind evidence alone would suggest.
