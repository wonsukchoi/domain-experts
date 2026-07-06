# Mathematician artifacts — filled deliverable shapes

Three recurring outputs: a referee report that separates local from global errors, an NSF DMS Project Description skeleton (15-page cap), and an MCM/ICM-style modeling-paper summary. Example numbers below are internally consistent within each artifact.

## 1. Referee report — local vs. global error separation

Submitted for a 34-page paper claiming a new bound on the spectral gap of a random regular graph ensemble. Structure below is the actual section order; do not reorder.

```
Report on "<paper title>", submitted to <venue>
Referee: <role, not name, if double-blind>
Recommendation: Major revision

SUMMARY OF CLAIM
The paper claims (Theorem 1.2) that for d-regular random graphs on n
vertices, the second eigenvalue λ2 satisfies λ2 ≤ 2√(d-1) + ε with
probability 1 - O(n^-1/6), improving the exponent from the prior
n^-1/12 bound (Friedman 2008) via a new moment-method argument (Section 4).

GLOBAL ASSESSMENT
The overall architecture is sound: the trace-method setup (Sections 2-3)
and the closing probabilistic argument (Section 5) are standard and
correctly executed. The paper's central claim stands PENDING the local
issue below, which is load-bearing — every subsequent bound in Sections
5-6 cites Lemma 4.3 directly, so an error there propagates to the
paper's entire quantitative claim, not just to Section 4.

LOCAL ISSUES (paper survives a fix; listed by dependency order)

1. [MAJOR, load-bearing] Lemma 4.3, inequality (4.7): the union bound
   over closed walks of length 2ℓ assumes ℓ = O(log n), but the moment
   computation in (4.5)-(4.6) only controls walks up to ℓ = O(log n /
   log log n). This gap affects every walk-counting step downstream
   (Lemmas 4.4, 4.6, and Theorem 1.2 directly cite 4.3).
   Fix path: either (a) show the moment bound extends to the full
   log n range via a second-moment truncation argument, or (b) restate
   Theorem 1.2 with the weaker n^-1/8 exponent, which the current proof
   does support.

2. [MINOR, cosmetic] Equation (3.14): sign error, propagates only to
   the constant in Corollary 3.2, not to any downstream inequality
   (Corollary 3.2 is not cited again). Does not affect Theorem 1.2.

3. [MINOR, cosmetic] Notation: d used for both graph degree (Section 2)
   and metric distance (Section 6) — no mathematical consequence, but
   confused this referee for a full read-through.

REQUIRED BEFORE ACCEPTANCE
Item 1 must be resolved one of the two ways above. Items 2-3 are
copyediting, not conditions of acceptance.

VERIFICATION STATEMENT
I re-derived Sections 2, 3, and 5 independently by hand. For Section 4
I checked each step's local validity but did not independently
re-derive the moment bound in (4.5)-(4.6) from scratch — I verified it
is plausible and internally consistent, not that it is correct from
first principles. This report certifies "no error found beyond Item 1
on a careful read," not "independently re-derived in full."
```

Rule: the "load-bearing" tag on Item 1 is what justifies major-revision over minor-revision — a referee report that lists errors without tagging which are load-bearing gives the editor no way to weigh severity.

## 2. NSF DMS Project Description skeleton (15-page cap, PAPPG format)

Applies to standard DMS core-program proposals. Page budget below is a working allocation, not a rule — but blowing past it on any one section without cutting elsewhere is the most common desk-reject trigger cited by program officers.

| Section | Page budget | Contents |
|---|---|---|
| 1. Overview | 1 | The exact result(s) targeted, stated as falsifiable claims, not a survey of the field |
| 2. Intellectual Merit | 5–6 | Background (1p) + specific aims (1p) + technical approach per aim (3–4p) — each aim gets a named method and a stated fallback if the primary approach stalls |
| 3. Broader Impacts | 1.5–2 | Concrete, checkable commitments (e.g. "two REU students per year, summer 2027–2029" not "will engage undergraduates") |
| 4. Results from Prior Support (if PI funded in past 5 yrs) | 1 | Prior award number/dates + Intellectual Merit outcomes (papers, with venue) + Broader Impacts outcomes, separately labeled |
| 5. Timeline | 0.5–1 | Year-by-year aims, e.g. Y1: Aim 1 complete + submit; Y2: Aim 2 + conference; Y3: Aim 3 + synthesis paper |
| 6. Management/Feasibility for multi-aim or multi-PI | 0.5 | Who owns which aim; what happens if Aim 2 depends on Aim 1's unproven step |
| **Total** | **~9.5–11.5** | (leaves ~3.5–5.5p margin under the 15p cap) |

**Specific Aims block (filled example, condensed matter/PDE proposal):**

```
Aim 1 (Y1): Prove existence of weak solutions to the modified
  Navier-Stokes system (1.3) under the boundary condition (1.4), for
  initial data in H^1(Ω). Approach: Galerkin approximation + compactness
  (Aubin-Lions). Fallback if compactness fails: restrict to data in
  H^2(Ω), which recovers strong compactness at the cost of a narrower
  class of initial data.

Aim 2 (Y2): Establish uniqueness under the additional regularity
  assumption ∇u ∈ L^4(0,T; L^4(Ω)) (a Prodi-Serrin-type condition).
  Approach: energy-method Gronwall argument, adapting Escauriaza-
  Seregin-Šverák (2003) to the modified boundary term.

Aim 3 (Y3): Numerical validation of the Aim 1-2 theory against a
  finite-element solver (FEniCS), checking predicted blow-up-time
  bounds against computed solutions for 3 benchmark geometries.
```

Rule: every aim states both the primary approach and the fallback if it stalls — a proposal whose aims have no stated fallback reads to a program officer as the PI not having tried the approach yet.

## 3. MCM/ICM-style modeling-paper summary sheet

One page, written last, read first by judges — non-analytic, tiered judging with no per-section rubric means the summary sheet disproportionately sets the anchor score before the judge reads page 2. 25-page total cap; summary does not count against it but is judged as part of "Team Control Number" quality.

```
Team #: <control number>            Problem: <letter>

SUMMARY

We model the spread of <phenomenon> using a compartmental SEIR
variant with a time-varying transmission rate β(t) fit to <data
source, n=<count> observations>. Our central result: under the
current intervention schedule, peak prevalence occurs at day 47
(95% CI: day 41-54) at 8.2% of the population, versus day 31 at
14.1% with no intervention — a 5.9 percentage-point reduction.

We validate the model against held-out data from <region/period>,
achieving a mean absolute percentage error of 6.8% over the
validation window, and perform sensitivity analysis on the three
most consequential parameters (β0, intervention start day, and
recovery rate γ), finding the peak-day estimate is most sensitive
to intervention start day (±3 days shifts peak by ±9 days) and
least sensitive to γ (±10% shifts peak by <1 day).

Limitations: the model assumes homogeneous mixing, which likely
understates peak severity in the sub-population with contact rate
>2x the mean; we bound this effect in Section 5 but do not fully
resolve it.

[Recommendation to <stated audience>, 1-2 sentences, stated as a
decision, not a summary of findings: "We recommend maintaining the
current intervention through day 60, after which our model shows
< 2% marginal reduction in peak prevalence per additional week."]
```

Rule: the summary states the result and its uncertainty (CI, validation error) before the method — a judge who reads only the summary sheet across 20+ papers rewards the one that answers "what did you find and how sure are you," not "what technique did you use."
