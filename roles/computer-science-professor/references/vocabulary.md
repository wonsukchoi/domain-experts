# Working vocabulary — terms a CS professor uses precisely

Format: definition → how a practitioner says it → common misuse.

**DFW rate** — The percentage of enrolled students who receive a D, an F, or withdraw from a course; the standard department-level metric for course health, not just "the fail rate."
In use: "CS1's DFW rate is at 41% this term, well above our three-year baseline of 34%."
Misuse: treating any DFW figure as self-evidently a student-preparation problem, without checking whether it's an assessment-structure artifact first.

**CS1 attrition** — The specific, well-studied phenomenon of high fail/withdraw rates in the first programming course, distinct from attrition in later CS courses, which has different causes (workload, major-fit, not novice-programmer struggle).
In use: "That's a CS1 attrition pattern — it doesn't generalize to what we're seeing in the 300-level courses."
Misuse: applying CS1-specific fixes (peer instruction, novice-misconception scaffolding) to an upper-level attrition problem that actually has a different root cause.

**Item analysis** — Breaking exam or quiz results down by individual question (and the concept it targets) rather than reading only the aggregate score, to find which specific concept or format is the actual gap.
In use: "The exam mean looks fine, but item analysis shows Q11 and Q12 — both exam-only formats — dragging two subgroups down."
Misuse: reading only the overall percentage and concluding the exam "went well" or "went poorly" without checking whether the mean is masking a concentrated gap.

**Peer instruction** — An active-learning technique (Mazur; adapted to CS by Simon & Bailey Lee) where students answer a conceptual question individually via clicker, discuss with a neighbor, then re-vote — designed to surface and correct misconceptions in real time rather than at exam time.
In use: "We're running peer instruction on the pointer-aliasing concept specifically because that's where the misconception cluster showed up last term."
Misuse: calling any small-group discussion "peer instruction" — the technique specifically requires the individual-vote / discuss / re-vote structure; skipping the first vote removes the diagnostic signal that makes it work.

**Novice misconception** — A specific, recurring, and often internally-consistent wrong mental model a beginning programmer holds (e.g., believing a variable "remembers" its old value alongside the new one), distinct from simply "not knowing" the material.
In use: "That's not a knowledge gap, that's the classic 'variable as container with memory' misconception — reteaching the definition won't fix it, they need a counterexample that breaks the model."
Misuse: treating every wrong answer as a knowledge gap to be re-lectured, instead of diagnosing whether it's a specific, nameable misconception that needs to be directly confronted.

**Specification grading** — A grading scheme where each assignment or exam item is graded against a specific bar (met/not met) rather than partial-credit points, usually paired with multiple attempts or a token/redo system.
In use: "We moved the labs to specification grading — it's pass/revise/fail per objective, not points, so a near-miss doesn't quietly average out to a B."
Misuse: assuming it's just pass/fail grading in general; the defining feature is objective-level granularity plus a defined revision path, not the absence of partial credit alone.

**Curriculum mapping / student outcomes** — The formal table linking each course's learning objectives to a program's accreditation-defined student outcomes (per ABET CAC criteria), used to justify that graduates meet the program's stated competencies.
In use: "Before we drop the concurrency unit, check the outcomes-mapping table — that might be the only course covering outcome 4."
Misuse: treating curriculum mapping as bureaucratic paperwork disconnected from actual teaching decisions, rather than the record that determines whether removing a topic breaks accreditation.

**Similarity threshold (MOSS)** — The percentage token-overlap score a code-similarity tool reports between two submissions; a triage signal for further review, not a determination of academic-integrity violation by itself.
In use: "It's flagging at 63% after excluding the starter file — that's above our informal 60% look-closer line, but I still need to read the actual diff before deciding anything."
Misuse: treating any high percentage as proof of copying without excluding shared starter/boilerplate code first, which routinely inflates the score for innocent submissions.

**Teaching load (e.g., 2-2, 3-3, 4-4)** — Shorthand for the number of courses taught per semester across an academic year; research-intensive (R1) institutions commonly run 2-2, teaching-focused institutions 3-3 or 4-4.
In use: "I'm on a 2-2 this year, so the DFW redesign has to fit inside one of two course preps, not become a third."
Misuse: comparing teaching-portfolio expectations across institutions without accounting for the load difference — a 4-4 teaching record is not directly comparable to a 2-2 record for volume or scope.

**Course release** — A reduction in teaching load (e.g., from 2-2 to 2-1) granted in exchange for another obligation — a large grant's buyout clause, an administrative role, or a curriculum-development project — negotiated explicitly, not assumed.
In use: "The NSF grant includes a course release for the PI in year two — that's the semester to run the redesign pilot."
Misuse: assuming any grant or service role automatically comes with a course release; it has to be negotiated and funded (grant buyout rate or departmental approval), not inferred from the role's importance.

**Tenure clock** — The fixed probationary period (commonly six years) before the mandatory up-or-out tenure review; can be paused ("stopped") for specific, usually policy-defined reasons (parental leave, documented hardship).
In use: "That's a year-three project — fine on the tenure clock. A five-year redesign commitment isn't, unless it produces something publishable along the way."
Misuse: treating the tenure clock as a soft deadline that can absorb open-ended commitments; the review date is fixed regardless of how a given project is going.

**Adjunctification** — The department-level trend of covering an increasing share of course sections with contingent (adjunct/lecturer) faculty rather than tenure-track lines, with direct consequences for course consistency and curriculum continuity.
In use: "Three of CS1's eight sections are adjunct-taught this term — that's the adjunctification pattern behind the section-to-section variance we're seeing."
Misuse: using the term as a generic complaint about adjunct faculty quality, rather than what it actually names — a staffing-structure trend with measurable continuity and consistency effects.

**External tenure letters** — Solicited evaluation letters from senior faculty at peer or aspirant institutions, arm's-length from the candidate (no co-authors, no former advisors), assessing the candidate's standing in the field.
In use: "We need at least half the external-letter list to be names the department added independently, not just the candidate's suggestions."
Misuse: treating the letters as a formality or as equivalent regardless of who proposed the names; a list built entirely from the candidate's own suggestions is read by a tenure committee as weaker evidence.
