# Playbook

Operational workflows a history instructor actually runs, with filled example numbers. Starting points to adapt, not scripts.

## 1. Coverage-design decision (survey vs. seminar)

Run once per redesign cycle (new textbook adoption, or every 3-5 years), using the department's own catalog and articulation records.

**Step 1 — pull the course's institutional purpose.** Example (state university, US History I, gen-ed):

| Course | Catalog designation | Transfer-articulation topics named |
|---|---|---|
| HIST 101 (US History I) | Gen-ed historical-reasoning requirement | Colonial founding, Revolution, Constitution, slavery & sectionalism, Civil War — 5 named topics minimum per the state articulation agreement |
| HIST 340 (seminar) | Major-track methods/capstone | None — department sets outcomes internally |

**Step 2 — pick the model against that purpose:**

| Course type | Default model | Rationale |
|---|---|---|
| Gen-ed survey with named articulation topics | Breadth-first, covering the named topics plus 3-4 electives in the remaining weeks | Transfer students must show exposure to the named topics or lose credit at the receiving institution — breadth here is a contractual deliverable, not a design failure. |
| Gen-ed survey with no articulation constraint | Uncoverage — 6-8 topics in primary-source depth | Optimizes for the literacy-for-life goal most of the room actually needs; more topics in summary produces less retained reasoning skill per Calder's argument. |
| Major-track seminar/methods course | Uncoverage, skewed toward skill (sourcing, corroboration, independent archival research) over content breadth | The deliverable is a research paper, not content recall — depth of primary-source engagement is the assessed outcome. |

**Step 3 — check the skill-assignment mapping.** For any course, confirm each of the four core skills (sourcing, corroboration, contextualization, thesis construction) maps to at least one assignment that isolates it — a single term paper at the end of term tests all four at once and diagnoses none of them individually if the paper is weak.

## 2. Citation-verification workflow (run on any paper crossing the high-score threshold)

**Trigger:** paper scores 85+ on first read (department-set threshold; adjust to local norms), or an essay's primary-source engagement subscore looks disproportionately strong relative to the rest of the paper.

**Steps:**
1. Spot-check 5 primary-source citations against the actual paginated source (physical book, archival database record, or newspaper database page image) — not the citation's plausibility, the actual text at the actual page.
2. If 0-1 of the 5 fail: accept the paper's citations as verified; no further check needed.
3. If 2+ of the 5 fail: escalate to a full check of every citation in the paper.
4. For each failed citation, classify it:
   - **Fabricated** — the quoted language does not appear anywhere in the cited source, at any page.
   - **Mis-cited** — the quote exists in the source but at a different page or edition (a citation-mechanics error, not an integrity matter).
5. Recompute the primary-source engagement subscore: deduct a fixed per-citation penalty (departments vary; 3 points per unverifiable citation off a 30-point subscore, floored at 0, is a working default) for fabricated citations only — mis-cited-but-real quotes get a smaller flat deduction (1 point) for citation-mechanics error, not the fabrication penalty.
6. Refer fabricated citations to the Academic Integrity Office with the specific flagged quotes and page-mismatch documentation attached; mis-citations are a grading matter only.

**Filled example (HIST 340 paper, 15 citations, threshold triggered at 88/100):**

| Citation | Claim | Verification result | Classification | Point action |
|---|---|---|---|---|
| 1 | Newspaper editorial, correctly quoted | Verified | — | none |
| 4 | Douglass letter to Smith, p. 214 | Quote absent from cited page and index | Fabricated | -3 |
| 7 | Congressional Globe excerpt, wrong page (actual: p. 1140, cited: p. 1104) | Quote exists, wrong page | Mis-cited | -1 |
| 9 | Diary entry, correctly quoted | Verified | — | none |
| 11 | Convention proceedings, quote not in source | Fabricated | Fabricated | -3 |
| ... | (5 total fabricated, 1 mis-cited, 9 verified across the full 15) | | | |

Total deduction from fabrication: 5 × 3 = 15; from mis-citation: 1 × 1 = 1. Adjust the worked example in SKILL.md's numbers to whichever specific breakdown a real case produces — the table's job is showing the classification step, not a fixed ratio.

## 3. Primary-source sourcing exercise (lower-division, Reading Like a Historian model)

**Format:** single 50-75 minute session, one document set (2-4 short primary sources on the same event from different vantage points).

**Filled example — the Boston Massacre, two accounts:**

```
Document A: Captain Thomas Preston's deposition (British officer on trial)
Document B: A Boston town-meeting pamphlet account (colonial political leadership)

Sourcing questions (before content questions):
  - Who wrote this, and what did they have at stake in how the event is described?
  - When was it written relative to the event — same day, during a
    trial, months later for a political audience?
  - Who was the intended audience, and how would that shape what's
    included or omitted?

Corroboration question (after both documents are sourced):
  - Where do A and B agree on the sequence of events, and where do
    they diverge? Divergence on gunfire-order sequencing is the
    historically contested point — that's the target finding, not a
    "correct" combined narrative.

Contextualization question:
  - What was happening in Boston's relationship with British troops
    in the months before this event that neither document states
    outright but both assume the reader knows?
```

Grade the sourcing/corroboration/contextualization responses separately from a "what happened" content quiz — conflating the two hides whether the sourcing skill was learned or just the content was memorized.

## 4. TA rubric-anchoring session (before every essay set is graded)

**Format:** 45-60 minutes, all TAs for the course, before grading opens.

**Steps:**
1. Instructor grades 3-5 real (anonymized) essays solo first, applying the thesis gate as a separate first pass (does the paper stake a defensible, arguable claim — yes/no) before scoring the rubric.
2. TAs independently grade the same 3-5 essays.
3. Compare scores by rubric category. Any essay where TAs differ by more than 20% of a category's point value gets discussed until the group agrees on the criterion that was ambiguous, and the rubric language is amended on the spot.
4. The finalized rubric plus the 3-5 scored anchor essays are saved and reused as the calibration set next term.

**Filled example — thesis-gate criterion for a 20-point Thesis Clarity category:**

```
Thesis gate (pass/fail, checked first): does paragraph 1 state a
claim that a reasonable historian could argue against? "The Civil
War had many causes" fails the gate (not arguable — no one denies
it). "Slavery's economic centrality to the South, not states'-rights
ideology, was the proximate cause of secession" passes (a historian
could argue the reverse).

If the gate fails: Thesis Clarity caps at 8/20 regardless of prose
quality; Analysis & Argument caps at 15/30, since an argument
section can't fully succeed without a claim to argue for.

If the gate passes, score normally:
  16-20: claim is specific, arguable, and sustained across the paper
  11-15: claim is arguable but drifts into pure narrative by the
         paper's second half
  8-10: claim is present but too broad to be arguable in practice

Common TA disagreement point: whether a thesis stated only in the
conclusion (not the introduction) counts as passing the gate —
anchor decision: yes, it passes, but caps at 15/20 for structural
weakness, scored separately from the claim-quality criterion above.
```
