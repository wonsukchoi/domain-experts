# Playbook

Operational workflows an economics instructor actually runs, with filled example numbers. Starting points to adapt, not scripts.

## 1. Intro course sequencing decision

Run once per redesign cycle (new textbook adoption, or every 3-5 years), using the department's own enrollment records.

**Step 1 — pull the audience mix.** Example (state university, Principles of Microeconomics, 3-year average):

| Cohort | Share of intro enrollment | Goes on to Intermediate Micro |
|---|---|---|
| Declared econ/business majors | 22% | 85% of these |
| Gen-ed / other majors | 78% | 4% of these |

Roughly 22% × 85% + 78% × 4% ≈ **22% of the room** ever takes a second economics course. That number, not instinct, decides the sequencing bet.

**Step 2 — pick the model against that ratio:**

| Audience mix (share continuing to Intermediate) | Default sequencing | Rationale |
|---|---|---|
| <25% continue | CORE Econ ("The Economy") engagement-first | Optimizes for one-semester economic literacy; historical/data-driven entry point holds a mostly-terminal audience better than perfect-competition-first. |
| 25-50% continue | Hybrid — CORE modules 1-8 for engagement, then a Mankiw-style supply/demand/elasticity unit before midterm | Split the difference; majors still get the toolkit before Intermediate. |
| >50% continue (transfer-heavy, pre-business cohorts) | Standard Mankiw/Krugman-Wells micro-first | Majority need calculus-ready scaffolding; engagement-first sequencing would under-prepare them. |

**Step 3 — check the math prerequisite against the sequencing choice.** If Intermediate Micro is calculus-based and more than 15% of intro students have not completed (or are not concurrently enrolled in) the calculus prerequisite, flag to the curriculum committee before finalizing — a sequencing choice that assumes math the cohort doesn't have shows up 3-6 months later as an Intermediate-level DFW spike, not an intro-level complaint.

## 2. Item-analysis workflow (run after every scored exam)

**Pull, per item:** p-value (fraction of students correct) and point-biserial discrimination (correlation between getting the item right and overall exam score, excluding that item).

**Thresholds:**

| Metric | Flag condition | Action |
|---|---|---|
| p-value | < 0.30 | Check for ambiguity, miskey, or unmet prerequisite before blaming difficulty |
| p-value | > 0.95 | Fine to keep as a confidence-builder if placed early; otherwise low information, consider swapping |
| Discrimination | < 0.15 | Item is not separating strong from weak students — review wording |
| Discrimination | negative | Near-certain miskey or two defensible answers — verify against the taught method before next use |

**Filled example (30-item MC section, midterm above):**

| Item | Topic | p-value | Discrimination | Verdict |
|---|---|---|---|---|
| Q3 | Opportunity cost | 0.71 | 0.34 | keep |
| Q9 | Supply shift vs. movement | 0.58 | 0.41 | keep |
| Q14 | Elasticity (midpoint) | 0.35 | -0.09 | **miskey — regrade** |
| Q22 | Deadweight loss | 0.44 | 0.22 | keep, borderline |
| Q27 | Marginal cost recall | 0.97 | 0.06 | low information — replace next term |

Only Q14 crosses the regrade threshold; Q27 is scheduled for replacement, not regraded this term.

## 3. TA rubric-anchoring session (before every problem set is graded)

**Format:** 30-45 minutes, all TAs for the section, before grading opens — not a memo sent after.

**Steps:**
1. Instructor grades 3-5 real (anonymized) submissions solo first, assigning points against the rubric.
2. TAs independently grade the same 3-5 submissions.
3. Compare scores item-by-item. Any submission where TAs differ by more than 10% of the question's total points gets discussed until the group agrees on the criterion that was ambiguous, and the rubric language is amended on the spot.
4. The finalized rubric plus the 3-5 scored anchors are saved and reused as the calibration set next term.

**Filled example — 20-point supply/demand graphing question rubric:**

```
Q2 (20 pts): "A price ceiling is imposed below equilibrium. Graph the
market before and after, and identify the shortage quantity."

  4 pts — correct initial supply and demand curves, labeled axes
  4 pts — price ceiling drawn below equilibrium price, labeled
  4 pts — quantity supplied and quantity demanded correctly read
          at the ceiling price (not at equilibrium)
  4 pts — shortage identified as Qd - Qs at the ceiling (numeric
          or clearly marked on the graph), not just "shortage exists"
  4 pts — one sentence explaining why the shortage doesn't self-
          correct (price is not free to rise to clear the market)

  Common TA disagreement point: partial credit when quantity supplied
  and quantity demanded are swapped but otherwise correct — anchor
  decision: 2 of the 4 points (mechanics right, definition wrong).
```

## 4. Academic-integrity verification workflow (solution-bank matches)

Run when multiple submissions on the same problem set show identical non-obvious errors or identical unusual phrasing — not on a single close match, which happens by chance in numeric problem sets.

1. **Search the exact problem-set wording** (not just the numeric answer) on Chegg, Course Hero, and a general web search before assuming a match is copied — publishers sometimes reuse near-identical problems across editions, producing false positives.
2. **Confirm a shared, non-generic error**, not just a shared correct answer — a shared correct final number on a simple computation is common by chance; a shared wrong intermediate step (e.g., both used the endpoint elasticity method when midpoint was assigned, with the same rounding) is the actual signal.
3. **Check timestamps** — a posted solution predating the assignment's release is definitive; one posted after suggests a student uploaded it, which is a different (but still reportable) integrity issue.
4. **Refer to the academic-integrity process with the specific matched language and error highlighted**, not a general "suspiciously similar" claim — the referral needs the same evidentiary specificity as a grade-appeal rubric citation.
