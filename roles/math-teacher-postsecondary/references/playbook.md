# Playbook

Filled procedures for the three recurring executed processes: gateway-course DFW triage, TA/multi-section exam norming, and placement/corequisite calls. Populate the tables with your own course's numbers — the structures below are the pattern, not a description of one.

## 1. Gateway-course DFW triage

Run this whenever a multi-section course's DFW rate moves against its own history, or before proposing any redesign.

**Step 1 — pull the three-term trend, not one term:**

| Term | Enrollment | DFW % | Placement cut score | Sections | Notes |
|---|---|---|---|---|---|
| Fall 2024 | 248 | 22% | 65 (ALEKS PPL) | 8 | baseline |
| Spring 2025 | 231 | 24% | 65 | 7 | — |
| Fall 2025 | 252 | 31% | 65 | 8 | flag: +7pt jump, cut score unchanged |

A jump this size with a stable placement cut score rules out "weaker incoming cohort" as the primary explanation — move to Step 2.

**Step 2 — split the DFW number by cause, not just by section:**

| Cause bucket | Count | % of DFW total |
|---|---|---|
| Failed final only (passing before final) | 12 | 15% |
| Withdrew before week 6 (never engaged) | 19 | 24% |
| Withdrew after first exam (exam 1 < 60%) | 31 | 40% |
| Failed on cumulative low grades, no single trigger | 16 | 21% |
| **Total DFW** | **78** | **100%** |

Withdrew-after-exam-1 at 40% is the largest bucket — points at an early-diagnosis and intervention gap, not a final-exam design problem. If "failed final only" were the largest bucket instead, the diagnosis would point at final-exam weighting or timing, not early intervention.

**Step 3 — match intervention to the largest bucket, in this preference order:**

1. Early-warning + mandatory advising contact triggered by exam-1 score < 60% (targets the 39% bucket directly; lowest cost, one term to pilot).
2. Workshop/small-group problem sessions (Treisman-model: 3-4 hrs/week structured group work with peer presentation), added as a co-requisite lab section (targets delivery/engagement; costs TA or peer-leader hours — budget ~1 TA line per 2 workshop sections of 20).
3. Milestone restructuring — replace one 40%-weighted final with three 15%-weighted exams plus a 10% final (targets assessment-timing bottleneck; zero marginal cost, requires syllabus and department sign-off).
4. Corequisite support section for students below a placement threshold, run concurrently with the credit-bearing course rather than as a prerequisite term (targets placement bottleneck; requires a placement-policy change, longest lead time).

Do not run more than two interventions in the same term — a DFW change with two simultaneous causes can't be attributed to either.

**Step 4 — set the leading indicator before the term starts:** exam-1 pass rate target (e.g., "no worse than 70%, versus 61% last term") checked at week 4, so a failing redesign is caught with 8+ weeks left to add support, not discovered in the final grade report.

## 2. TA / multi-section exam norming

Run before any TA begins grading a shared exam's free-response or proof questions.

**Step 1 — write the rubric at the logical-step level, not the topic level:**

Bad: "Q6 (8 pts) — prove injectivity, award partial credit for reasonable attempts."

Good:
| Component | Points | Award if |
|---|---|---|
| Correct definition of injective (or logical equivalent) | 2 | Any of: ker(T)={0}⟹x=0 stated correctly, OR T(x)=T(y)⟹x=y stated correctly |
| Correct proof direction chosen | 3 | Assumes x∈ker(T) and derives x=0, or assumes T(x)=T(y) and derives x=y — either valid |
| Algebraic justification complete | 2 | Each step follows from linearity properties, no unjustified jump |
| Correct conclusion statement | 1 | States what was shown implies injectivity, not just "QED" |

**Step 2 — norm on a blind sample before scale grading.** Pull 3-5 exams per grader (minimum 15 total), strip visible scores, have every grader score the same 5-exam subset independently, then compare:

| Grader | Exam 1 | Exam 2 | Exam 3 | Exam 4 | Exam 5 | Avg | Spread from group mean |
|---|---|---|---|---|---|---|---|
| TA A | 7 | 8 | 6 | 8 | 7 | 7.2 | +0.7 |
| TA B | 6 | 8 | 7 | 8 | 6 | 7.0 | +0.5 |
| TA C | 5 | 6 | 4 | 6 | 5 | 5.2 | -1.3 |

(Group mean = average of the three TA averages = 6.47.)

A grader more than ~1 point off the group mean on an 8-point item, before real grading starts, gets a rubric walkthrough on the specific exams where the gap appeared — not a general "grade more generously" instruction, which doesn't transfer.

**Step 3 — after full grading, re-check the same statistic on real section averages.** A spread under ~0.5-1.0 point (out of 8) across sections on the same question is normal variation; wider than that triggers a targeted re-grade of the low or high outlier section using the blind-sample method from Step 2, scaled to the full section.

**Step 4 — document the norming decision in the rubric itself** ("definition need not match lecture phrasing if logically equivalent — see Fall 2025 norming note") so the next term's TA team doesn't re-litigate the same ambiguity from scratch.

## 3. Placement / corequisite call

For a student whose diagnostic score falls in the ambiguous band around a prerequisite course's cut score.

| Diagnostic result | Default placement | Override condition |
|---|---|---|
| Score clears cut score by ≥1 sub-band | Credit-bearing course, no support | — |
| Score within 1 sub-band below cut score, gap is broad (multiple skill areas) | Standalone remedial prerequisite | If institution has no corequisite-support capacity this term |
| Score within 1 sub-band below cut score, gap is broad | Credit-bearing course + corequisite support section | Preferred default — evidence favors this over standalone remediation for completion and time-to-credit |
| Score below cut, but gap is narrow (one specific skill, e.g. only algebraic-fraction manipulation) | Credit-bearing course + short bridge module (2-3 week) targeting that skill, no full extra course | If the gap is genuinely narrow on diagnostic subscores, not just aggregate score |
| Score far below cut score (bottom band) | Standalone remedial sequence | Corequisite support isn't designed to close a gap this large in one term |

The corequisite-over-prerequisite default holds specifically for the "broad but not severe" band — it is not a blanket recommendation to eliminate standalone remediation.
