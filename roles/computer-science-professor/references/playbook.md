# Playbook: Course Redesign, TA Staffing, Integrity Investigation, Tenure Dossier

Filled process for the four recurring executions of the role. Reference context throughout: a large public R1 CS department, CS1 enrollment in the 200–260 range per semester.

## 1. Course-Redesign Diagnosis (filled example)

Trigger: CS1 Fall 2024 DFW rate 40.9% (96/235), up from a 34% three-year average.

**Step 1 — pull the split.** Break the 96 DFW students into "low across the board" vs "competent on iterative work, failed the high-stakes instrument":

| Segment | Count | Lab avg | Final avg |
|---|---|---|---|
| Low everywhere | 35 | 41% | 38% |
| Lab-competent, exam-failed | 61 | 76% | 44% |

**Step 2 — item analysis on the final** (14 questions, 235 students):

| Question | Format seen before exam? | % correct |
|---|---|---|
| Q1–Q9 (topics tested weekly in labs) | Yes | 71% avg |
| Q10 (recursion, lab-format identical) | Yes | 68% |
| Q11 (pointer aliasing, exam-only format) | No | 34% |
| Q12 (Big-O comparison, exam-only format) | No | 29% |

**Step 3 — decide the lever.** Q11/Q12's low scores concentrate in the "lab-competent" segment (61 students), and those two questions are the only ones never seen in lab format — points to assessment-format transfer, not content gap. Lever: reduce single-instrument weight, add low-stakes practice in the exact format that will appear on the final.

**Step 4 — the change, with weights before/after:**

| Component | Before | After |
|---|---|---|
| Midterm 1 | 15% | 12% |
| Midterm 2 | 15% | 12% |
| Midterm 3 (new) | — | 12% |
| Final exam | 40% | 25% |
| Labs | 15% | 15% |
| Weekly peer-instruction quizzes (new) | — | 10% |
| Participation | 15% | 14% |

**Step 5 — track next cycle.** Fall 2025: DFW 68/248 = 27.4%. Logged regardless of direction; a null or negative result would also be reported to the committee, not quietly dropped.

## 2. TA Staffing Plan (filled example)

Course: CS1, 248 students, 1 large lecture + 8 lab sections of ~31 each.

- Target ratio: 1 TA per 20–25 students for grading load → 248/22 ≈ 11.3, round up: **12 TA slots** (mix of full 20hr/wk grad TAs and 10hr/wk undergrad graders).
- Split: 4 grad TAs run lab sections (2 sections each, ~62 students/TA total across labs + office hours); 8 undergrad graders handle homework/lab grading only, no lecture duties, capped at 25 students' worth of grading each (≈248/8 = 31 nominal, adjusted down where a grader also TAs a lab).
- Autograder coverage: any assignment with a deterministic correctness check (unit tests, expected stdout) goes through the autograder first; TAs grade only style/design rubric items on the autograded subset, and the full rubric on free-response/design questions. This is what keeps the 1:22 ratio sustainable — without autograding the sustainable ratio drops closer to 1:12–15.
- Calibration: all 12 TAs grade the same 5 sample submissions independently before grading opens; disagreements over 1 rubric point on a 4-point scale get a 15-minute norming discussion before grading the real batch.

## 3. Academic-Integrity (MOSS) Investigation Workflow (filled example)

Trigger: MOSS run on Assignment 4 (248 submissions) returns 14 pairs above 60% similarity.

**Step 1 — separate boilerplate from substance.** Re-run MOSS with the provided starter-code file explicitly excluded from comparison (`-b` flag equivalent / base-file exclusion). Of the 14 pairs, 9 drop below 40% once starter code is excluded — false positives from shared scaffolding, no further action.

**Step 2 — review the remaining 5 pairs manually.** Read the actual diffs, not just the percentage: identical variable-naming idiosyncrasies, identical comment typos, or identical unusual-but-wrong approaches are stronger intent signals than high percentage alone. Of the 5, 2 pairs show independently-plausible convergent solutions (a common textbook approach) at 63–68% similarity — no action, logged only. 3 pairs show shared typos and identical dead code — escalate.

**Step 3 — escalate the 3.** Meet with each student individually (not jointly) before filing, per most institutional academic-integrity procedures; ask for their process (version-control history, draft files) before presenting the similarity evidence. Only file the formal report after this conversation, since first-offense conversations catch legitimate collaboration-policy misunderstandings that a straight report to the integrity office would not.

**Step 4 — fix the assignment, not just the students.** Log that this is the third semester this exact assignment prompt produced flagged pairs; rotate in a modified variant (different starter data, different edge cases) next offering rather than reusing the identical prompt a fourth time.

## 4. Tenure Dossier Structure (filled example)

Case: 6th-year (final probationary year) tenure-track assistant professor, R1 department, standard research + teaching + service split.

**Section order** (per AAUP-style institutional norms):

1. **CV** — publications, grants (PI/co-PI, amounts, funding agency), courses taught with enrollment and evaluation-score trend.
2. **Research statement** — 3–5 pages: the throughline connecting the publication record, not a list; explicit forward agenda for the next 5 years.
3. **Teaching statement + evidence** — annotated syllabi for 2–3 courses showing an explicit before/after change tied to outcome data (the DFW-redesign format above is exactly this kind of evidence); peer-observation letters from 2+ colleagues; student evaluation trend (not a single semester's raw score, which is noisy at n<40).
4. **Service record** — committee work, journal/conference reviewing, outreach — kept brief; service is rarely the deciding factor but its absence is a flag.
5. **External letters** — typically 5–8 solicited from full professors at peer or aspirant institutions, arm's-length (no co-authors, no advisors). The candidate proposes a list; the department adds names independently — a list built entirely of the candidate's own suggestions weakens the letters' evidentiary weight.

**Common dossier failure:** a research statement that reads as a list of paper abstracts instead of a throughline — external reviewers are evaluating trajectory and independent identity (distinct from the PhD advisor's agenda), not paper count alone.
