# Research Playbook

Operational sequences with concrete steps and thresholds. Defaults, not laws — deviate consciously and log why.

## 1. IRB submission and amendment workflow

### Determining review pathway

1. **Check exemption first.** Under 45 CFR 46.104, categories most relevant to social-science RA work: (2) educational tests/surveys/interviews/observation of public behavior with no more than minimal risk and no readily identifiable/sensitive linkage, (4) secondary use of identifiable data if publicly available or recorded so subjects can't be identified. Exempt still requires an IRB determination — self-certifying exemption is not a real category at almost any US institution.
2. **Expedited review** covers minimal-risk research not meeting an exempt category — most survey/interview studies with identifiable data land here. Turnaround is typically 1–3 weeks depending on the board's queue; budget for it in a study timeline, don't assume same-week approval.
3. **Full board review** applies to greater-than-minimal-risk studies (vulnerable populations, sensitive topics with legal/reputational risk if disclosed, deception without adequate debrief plan). Budget 4–8 weeks and a live committee meeting slot, not just a submission date.

### Amendment triggers — file before implementing, not after

- Any change to recruitment materials, wording, or venue.
- Any added, removed, or reworded survey/interview item.
- Any change to incentive type or amount.
- Any change to the data-retention or data-sharing plan.
- Any new research staff member gaining access to identifiable data (they need CITI training on file before access, not after).

### Continuing review / annual renewal

- Track the expiration date at protocol activation, not at the deadline. Most boards require the renewal submitted 4–6 weeks before expiration.
- **If the approval lapses while data collection is active: stop enrolling and stop collecting new data immediately.** Data already collected under a valid approval is fine; anything collected after lapse is a reportable violation, not a deviation.

### Reporting a deviation

Log: what happened, when, who was affected (how many participants), why it happened, and the corrective action taken. Report to the IRB per the institution's timeline (commonly within 5–10 business days for non-serious deviations; immediately for anything affecting participant safety). Do not wait for the next continuing-review cycle to bundle it in.

## 2. Reliability-check gate — worked thresholds

**Before starting bulk coding**, pre-register: subsample size (commonly 10–20% of total, minimum ~20 items for a stable estimate), which statistic (Cohen's kappa for 2 coders, Krippendorff's alpha for 3+ coders or mixed missing data), and the pass threshold.

| Statistic | Band | Interpretation (Landis & Koch 1977 / Krippendorff 2018) |
|---|---|---|
| κ or α | < 0.00 | Poor — worse than chance |
| κ or α | 0.00–0.20 | Slight |
| κ or α | 0.21–0.40 | Fair |
| κ or α | 0.41–0.60 | Moderate — below most labs' bar for proceeding |
| κ or α | 0.61–0.80 | Substantial — typical minimum bar (κ ≥ 0.70) to proceed to single-coding |
| α (Krippendorff specific) | ≥ 0.80 | Acceptable for confirmatory use; 0.667 is the floor for exploratory/hypothesis-generating coding only |

**Gate procedure:**

1. Draw the subsample at random from the full dataset — never the first N items collected (early responses are systematically different) and never a "let's use ones I already looked at" convenience pick.
2. Double-code independently, no discussion until both coders submit.
3. Compute the statistic. If it clears the threshold, proceed to single-coding the rest, still spot-checking a smaller ongoing sample (5%) through the run to catch drift.
4. If it fails: pull the confusion matrix, find where disagreements concentrate (usually 1–2 category pairs, rarely uniformly spread). Revise the decision rule for that pair specifically — don't rewrite the whole codebook. Recode only the disputed items under the new rule and recompute.
5. If a second pilot also fails: escalate to the PI before spending more coder-hours; the categories may need a genuine redesign, which is a scope conversation, not a coding-technique fix.

## 3. Data cleaning and de-identification

1. **Separate identifiers from response data at entry, not at export.** Use a study ID as the join key; keep the name/contact crosswalk in a separate file with tighter access, held by the PI or a single designated RA.
2. **De-identification checklist** before any dataset leaves the lab (share with a co-author, upload to a repository, submit to a journal): direct identifiers removed (name, email, phone, SSN); indirect identifiers assessed for re-identification risk in combination (zip + birthdate + rare demographic combination can re-identify even with no name attached) — coarsen (age in 5-year bands, 3-digit zip) rather than drop entirely if the variable is needed for analysis.
3. **Double data-entry** on any manually transcribed data (paper surveys, handwritten forms): two independent entries, automated diff, discrepancy rate computed. **Threshold: >1% discrepancy on a batch → re-verify the entire batch against source**, not just the rows the diff flagged — a >1% rate usually means the entry process itself is producing errors the diff tool doesn't catch symmetrically (e.g., both entrants misreading the same ambiguous handwriting).
4. **Data dictionary ships with every handoff**: variable name, label, type, valid range/values, missing-code convention, and derivation formula for any computed variable. A cleaned dataset without one isn't actually usable by anyone but the person who cleaned it.

## 4. Literature search and screening funnel

For a targeted background search (not a formal systematic review):

1. Define 2–4 search strings from the PI's actual question, run across 2–3 relevant databases (PsycINFO, Web of Science, Google Scholar as a supplement, not a primary source).
2. Screen title/abstract against explicit inclusion/exclusion criteria (population, study design, date range, language) — this is the pass that should eliminate 70–90% of raw hits.
3. Full-text screen the survivors against the same criteria plus any deeper ones (methodology quality, relevance to the specific claim being supported).
4. For anything labeled "systematic," log the search string, database list, date range, and hit counts at each stage — this is what makes it reproducible and is the PRISMA-flow-diagram minimum, not optional documentation.

**Scoping rule:** if the destination is a background paragraph (2–4 citations) or a hypothesis justification (5–10 citations), stop at the title/abstract pass augmented by 2–3 known anchor papers the PI already cited — a full systematic pipeline for a paragraph is over-scoped effort nobody asked for.
