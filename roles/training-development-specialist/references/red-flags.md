# Red Flags — Training and Development Specialist

Signals worth a design or LMS audit pass before a course quietly fails to transfer or the reporting silently overstates impact. Each maps to a specific pull, not a vibe.

### A course brief states a topic ("onboarding training," "leadership training") with no terminal objective in condition/behavior/criterion form
- **Usually means:** the request was accepted straight from the stakeholder without a needs-assessment or objective-writing pass, which almost always produces content nobody can evaluate.
- **First question:** "What specific, observable behavior, under what condition, at what criterion, is this course supposed to change?"
- **Data to pull:** the original course brief/request ticket and whichever design document (if any) was supposed to translate it into an objective.

### LMS completion rate is reported as the headline effectiveness metric with no Level 2/3/4 data alongside it
- **Usually means:** the evaluation plan was never built at design time, so completion — an enrollment metric — is the only number the LMS produces by default.
- **First question:** "What does completion actually measure here — viewing all slides, or passing a scored assessment?"
- **Data to pull:** the SCORM/xAPI completion-trigger configuration for the course and, if one exists, the original evaluation plan.

### A branching-scenario or knowledge-check module reports pass rates above 95% with no remediation-loop data
- **Usually means:** either the assessment items are too easy relative to the objective's criterion (testing recall when the objective calls for application), or the pass threshold was set low enough to guarantee a good-looking number.
- **First question:** "What Bloom level are the assessment items pitched at, and does that match the enabling objective's stated behavior?"
- **Data to pull:** the item-level xAPI response data (not just the pass/fail rollup) and the enabling objective each item maps to.

### An ILT-format course was chosen for a purely declarative-knowledge objective (facts, policy lookup, terminology)
- **Usually means:** format was chosen by habit or stakeholder preference rather than against the objective's required practice fidelity — an expensive, hard-to-scale delivery method for content that doesn't need live interaction.
- **First question:** "What about this objective requires live facilitation rather than a self-paced module?"
- **Data to pull:** the objective's condition/behavior/criterion statement and the per-learner delivery cost estimate for the audience size in scope.

### An eLearning module was built for an interpersonal or psychomotor objective (de-escalation, physical technique, live customer delivery) with no ILT or role-play component
- **Usually means:** the build defaulted to the cheaper, more scalable format without checking whether the objective's fidelity requirement can survive a click-through simulation.
- **First question:** "Can a learner demonstrate this specific behavior inside the module, or only recognize the correct answer in a multiple-choice format?"
- **Data to pull:** the storyboard/interaction script and the Level 3 behavior-observation instrument (if one exists) to see whether it was designed for live or simulated assessment.

### A course has been live for 60+ days with no Level 3 (behavior) or Level 4 (results) data collected
- **Usually means:** the evaluation plan specified L3/L4 instruments on paper but no one scheduled or owns collecting them — the most common gap between a documented plan and what actually gets measured.
- **First question:** "Who owns pulling the L3 observation checklist and the L4 business metric, and on what schedule?"
- **Data to pull:** the evaluation plan's data-source and schedule fields, and whatever has actually been logged against them to date.

### A needs assessment consists only of the requesting stakeholder's description, with no SME interview or task/person-level data gathered independently
- **Usually means:** the request was treated as the assessment instead of an input to one — the single most common way a course ends up solving the wrong gap.
- **First question:** "What did the SME interviews or task-analysis observation actually find, independent of what the stakeholder originally described?"
- **Data to pull:** interview notes, task-analysis documentation, or performance data (error rates, observation scores) gathered directly from the population, separate from the original request.

### A single course module exceeds roughly 9-10 discrete facts, steps, or decision branches on one screen or in one chunk
- **Usually means:** content was organized around a source document's structure (a policy manual section, a SME's mental model) rather than working-memory-appropriate chunking.
- **First question:** "Could this be split into two enabling objectives instead of one, each covering roughly half the items?"
- **Data to pull:** the storyboard or content outline, itemized by screen/chunk, with the item count per chunk.

### A mandatory, manager-accountable course shows completion under 40%
- **Usually means:** something below the expected mandatory-training completion band (60-80%) is failing — broken enrollment/assignment rules, a technical access barrier, or manager follow-through breakdown, not a content-quality issue in most cases.
- **First question:** "Is the shortfall concentrated in specific stores/teams (an assignment or access problem) or spread evenly (a content or scheduling problem)?"
- **Data to pull:** completion data segmented by manager/location/cohort, and the LMS enrollment/assignment rule configuration.

### An ADDIE-gated project has spent more than 3-4 weeks in the Analysis or Design phase for a low-stakes, non-regulated course
- **Usually means:** a linear sign-off process is being applied to a project that doesn't need documented phase gates, burning timeline that a SAM-style prototype loop would have used to ship and correct instead.
- **First question:** "Does this course have a compliance or regulatory sign-off requirement that actually needs the ADDIE phase-gate documentation trail?"
- **Data to pull:** the project's phase-gate sign-off log and whatever compliance requirement (if any) is cited as the reason for the gated process.
