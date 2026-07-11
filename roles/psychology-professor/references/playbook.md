# Playbook

Filled examples for the recurring processes a psychology professor runs. Populate the numbers to your own case; the structures below are what a veteran actually uses.

## 1. Tenure-clock semester resourcing table

Six-year probationary clock, 3rd-year formal review, example allocation for a 2/2 teaching-load research institution:

| Semester | Teaching | Research | Service | Notes |
|---|---|---|---|---|
| Yr1 Fall | New-prep course (heavy) | Lab setup, IRB filing | 0 committees | Protect no research output expectation this term |
| Yr1 Spring | 1 new + 1 repeat prep | Pilot data collection | 1 committee (low-load) | |
| Yr2 Fall–Yr2 Spring | Repeat preps only | Data collection + first manuscript draft | 1 committee | Target: 1 manuscript submitted by end of Yr2 |
| Yr3 Fall | Repeat preps | Manuscript #2 + grant submission | 1 committee, decline new invites | 3rd-year review packet due — SET + peer observation + CV snapshot |
| Yr3 Spring | Repeat preps | Revise per review feedback | 1 committee | |
| Yr4–Yr5 | Repeat preps, 1 new elective | 2-3 more manuscripts, 1 grant resubmission if declined | 1-2 committees | Pipeline should show 1 paper/8-10 months |
| Yr6 Fall | Repeat preps | Final manuscripts submitted (not just drafted — under review counts, "in prep" barely does) | Wind down non-required service | Dossier assembly begins |
| Yr6 Spring | — | Dossier finalized | — | External letters requested by department, typically 6-8 |

**Rule of thumb:** by the 3rd-year review, a research-institution dossier needs roughly 3-4 peer-reviewed submissions (published, in press, or under review) and at least 1 external grant submission, even if unfunded — a pipeline with nothing under review at year 3 is the single most common negative-review trigger.

## 2. Power-analysis-before-you-believe-it checklist

Run this before treating any new "significant" result (yours or a mentee's) as reportable:

1. Pull n per cell/group.
2. Compute observed effect size (d for t-tests, f or η² for ANOVA, r for correlations).
3. Compute the 95% CI on that effect size — if it spans from near-zero to implausibly large, the point estimate is not trustworthy on its own.
4. Discount the observed effect by ~50% (OSC 2015 average shrinkage) to get a planning estimate for any follow-up.
5. Compute required n for 80% power at the discounted effect size (G*Power or the closed-form n/group = 2·((z₁₋α/2+z₁₋β)/d)² for a two-group t-test).
6. Compare required n to what's actually feasible this semester/academic year — if the gap is >3x the current sample, the honest answer is "underpowered, plan a replication," not "publish as exploratory."

**Worked reference table** (independent-samples t-test, α=.05 two-tailed, 80% power, n rounded up per group):

| Target d | n/group | Total N |
|---|---|---|
| 0.8 (large) | 26 | 52 |
| 0.5 (medium) | 64 | 128 |
| 0.4 | 98 | 196 |
| 0.3 | 175 | 350 |
| 0.2 (small) | 393 | 786 |

## 3. Retrieval-practice unit template

For a 3-week unit (e.g., "Memory" in Intro Psych, ~9 class sessions):

| Session | Activity | Stakes |
|---|---|---|
| 1-2 | Lecture/reading intro to encoding, storage, retrieval | none |
| 3 | 5-question low-stakes retrieval quiz on sessions 1-2 (closed-note, ungraded or 1% weight) | low |
| 4-5 | New content: forgetting curves, interference | none |
| 6 | Cumulative 8-question quiz covering sessions 1-5 (spaced retrieval of session 1-2 content) | low |
| 7-8 | New content: eyewitness memory, applied cases | none |
| 9 | Unit exam — 40% recall/short-answer (forces retrieval, not recognition), 60% application scenarios | summative |

**Rule of thumb:** at least one prior unit's material should reappear in every subsequent quiz — the spacing, not just the testing, is what drives the retention effect.

## 4. IRB amendment decision table

| Change | Amendment required? | Typical turnaround |
|---|---|---|
| Fix typo in consent form, no substantive wording change | No — administrative note sufficient | same day |
| Add a new self-report measure to an existing session | Yes — substantive | 5-10 business days (expedited) |
| Change recruitment population (e.g., adults → minors) | Yes — often triggers full-board review | 4-6 weeks |
| Increase enrollment cap within the same population/procedure | Yes — substantive | 5-10 business days (expedited) |
| Add a co-investigator with no procedural change | Yes — administrative-track substantive | 3-5 business days |
| Extend approval past expiration (continuing review) | Yes — mandatory, file 30-45 days before expiration | 2-4 weeks |

**Rule of thumb:** if the question is "would a participant who already consented need to be told about this," it's substantive — file the amendment before continuing data collection on the affected arm.

## 5. P&T dossier structure (research-institution baseline)

1. **Research narrative** (3-5 pages) — the program's throughline across projects, not a paper-by-paper recap; explicitly states the next 2-3 years' direction.
2. **Teaching narrative** (2-3 pages) — pedagogy rationale (why retrieval-based assessment, why this grading scheme), not just a course list; cites peer observation and any pre/post learning data alongside SET.
3. **Service narrative** (1 page) — what was done and its scope, not a list of committee names.
4. **CV** — full publication list, grants (funded and submitted-unfunded), courses taught with enrollment and SET summary stats, mentees and their outcomes.
5. **External letters** — department solicits 6-8, typically weighted heavily by committees who don't know the candidate's subfield; the research narrative is what lets a non-specialist committee member make sense of those letters.
