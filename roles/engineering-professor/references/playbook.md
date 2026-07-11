# Playbook

Operational playbooks with concrete steps, thresholds, and filled examples. These are defaults, not laws — but deviate consciously and say why in the record.

## 1. ABET closing-the-loop cycle (per Criterion 4)

Run this table every time a course-embedded assessment is scored, not just at self-study time.

| Field | Example entry |
|---|---|
| Outcome assessed | Outcome 1 — identify, formulate, solve complex engineering problems |
| Instrument | Embedded exam question, rubric 0–4, ENGR 214 final |
| Program threshold | Average ≥ 2.5, and ≥ 70% of students scoring ≥ 2 |
| This cycle's result | 2.33 average; 61% of students ≥ 2 — **below threshold** |
| Root cause (from disaggregation) | Concentrated in one section — not a course-wide gap |
| Action planned | Co-taught redesign of the weak section's equilibrium module next term |
| Action recorded before or after teaching? | Before — logged in the continuous-improvement minutes dated before the term starts |
| Re-assessment plan | Same instrument, same section, next offering; report both cycles side by side |

**Threshold guidance when a program hasn't set its own:** treat a rubric average of 2.5/4 ("meets expectations") and 70% of students at or above that mark as a reasonable default floor absent a program-specific standard — document that it's a default, not a citation, if used.

**The failure this table exists to prevent:** an "action taken" field that repeats the prior cycle's wording. If you can't point to a syllabus line, assignment, or class session that changed as a direct result of last cycle's data, the loop didn't close — restate the finding as still open.

## 2. D/F/W spike triage order

Cheapest and most likely explanations first, same discipline as any metric-drop investigation. Most spikes resolve at step 1 or 2.

1. **Section/instructor disaggregation.** Pull D/F/W by section for this term and the prior three years. A spike concentrated in one section (new instructor, new format, different meeting time) is the most common cause and should change the entire investigation's direction.
2. **Prerequisite-grade correlation.** Pull the D/F/W students' grades in the feeder course. If they're proportionally the same students who struggled upstream, it's a prerequisite gap, not this course's teaching — the fix is in the earlier course or the placement policy, not here.
3. **Concept-inventory pre/post, if an instrument exists for the topic.** Identical pretest means across sections rules out a cohort-quality story; divergent normalized gain across sections with identical pretest means points at delivery.
4. **Exam-item analysis.** Which specific questions or outcome-mapped items drove the drop — a single hard topic, or spread evenly across the exam. A concentrated miss on one topic is a targeted fix; a spread-out miss is a broader issue (pacing, prerequisite, exam difficulty calibration).
5. **Baseline sanity check.** Compare against a 3–5 year rolling average, not last year alone — a single prior year can itself have been an outlier, and "up from last year" is a different (weaker) claim than "up from the rolling baseline."
6. **Real course-difficulty change last.** Only after 1–5 are ruled out: did the syllabus, textbook edition, or exam difficulty actually change, and was that change intentional and calibrated against the outcome threshold.

## 3. Concept-inventory administration and gain calculation

Formula: **g = (post% − pre%) / (100% − pre%)** — Hake's normalized gain, the fraction of the *possible* improvement actually achieved. Use it, not the raw posttest score, to compare sections or terms with different incoming preparation.

Filled example (three sections of the same course, same term):

| Section | Pretest % | Posttest % | Gain (g) | Reference band |
|---|---|---|---|---|
| A | 30 | 62 | 0.46 | Interactive-engagement (~0.48) |
| B | 30 | 61 | 0.44 | Interactive-engagement (~0.48) |
| C | 30 | 43 | 0.19 | Below traditional-lecture (~0.23) |

**Reading the table:** identical pretest scores mean the sections started from the same conceptual baseline — any spread in gain is a delivery signal, not a preparation signal. A section landing below the traditional-lecture reference band despite a nominally active-learning syllabus means the activities aren't producing the cognitive engagement the label implies; audit what fraction of class time is actually instructor talk versus student-generated work before assuming the activity list itself is the problem.

## 4. Capstone sponsor intake and milestone tracker

Filled example for a single team/sponsor pairing:

| Field | Entry |
|---|---|
| Sponsor | Regional manufacturer, conveyor-sensor retrofit problem |
| Problem statement (as scoped) | Design a low-cost jam-detection retrofit for an existing conveyor line, budget ≤ $400 in parts, must not require line downtime to install |
| IP terms | Students retain rights to coursework and portfolio use; sponsor gets a non-exclusive license to any resulting design; no NDA on the underlying engineering principles, NDA only on sponsor's proprietary line specs |
| Team size / roles | 4 students — mechanical lead, electrical/sensor lead, controls/firmware lead, project manager/documentation lead |
| PDR (preliminary design review) | Week 5 — concept selection matrix, at least 3 concepts scored against weighted criteria |
| CDR (critical design review) | Week 10 — detailed design, BOM with sourced part numbers and costs, safety/failure-mode review |
| FDR (final design review) | Week 15 — working prototype demo, design report, sponsor sign-off |
| Deliverable ceiling (told to sponsor up front) | "A working prototype and a design report — not a production-ready or shippable unit" |
| Scope-change rule | Any change after CDR freezes at the last agreed milestone unless safety-critical; sponsor signs off in writing on any accepted change |
| Individual accountability | Weekly time logs (target ≥ 8 hrs/week/student) + peer evaluation at PDR, CDR, FDR — team grade weighted by peer-eval multiplier, not flat |

**Free-rider threshold:** a team member logging under roughly a third of the team's per-person average by CDR triggers an individual conversation before FDR, not after grades are due.

## 5. NSF education-grant track selection

Match the ask to the mechanism — reviewers score scope mismatch as a proposal weakness, not ambition.

| Mechanism / track | Typical budget | Typical scope |
|---|---|---|
| IUSE/PFE: RED — Track 1, Planning | Up to $75,000/year, up to 2 years | Pilot a single curricular change, collect baseline data, build the case for a larger track |
| IUSE/PFE: RED — Track 2, Adaptation & Innovation | Up to $1,000,000, up to 5 years | Adapt or extend an evidence-based approach across a department |
| IUSE/PFE: RED — Track 3, Innovation | $1,000,000–$2,000,000, up to 5 years | Novel departmental-scale restructuring with its own research agenda |
| IUSE/PFE: RED — Track 4, Innovation Partnerships | $1,500,000–$2,500,000, up to 5 years | Multi-institution collaboration |
| CAREER | Institution/discipline-dependent, 5 years | Individual early-career award requiring a single integrated research *and* education plan — not two parallel projects; reviewers explicitly check whether the education activities feed the research question and vice versa |

**Rule of thumb:** if the proposal's ambition is "restructure how the department teaches its core sequence," it's a Track 2 or 3 idea, not a Track 1 budget — write it at that scope or don't submit it as RED at all.
