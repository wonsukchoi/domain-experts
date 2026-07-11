# Red Flags

Smell tests for lab, grant, and course signals. Format per flag: what it usually means, the first question to ask, the data to pull.

### A dataset where every replicate lands within 2–3% of the mean

- **Usually means:** either a genuinely tight, well-controlled assay (rare this consistent past ~3 biological replicates) or the "replicates" are technical, not biological — same animal/culture measured three times, not three independent animals/cultures.
- **First question:** "How many independent biological units does n refer to here, versus how many times each was measured?"
- **Data to pull:** the raw lab notebook entries or ELN records for each replicate's source (animal ID, culture passage, collection date) — not just the summary spreadsheet.

### Study section percentile jumps from ~20th to ~50th between cycles with no scope change

- **Usually means:** either a genuine reviewer-panel composition change (different study section, different expertise mix) or the preliminary data in the resubmission didn't actually address the prior summary statement's core critique.
- **First question:** "Which specific critique from the last summary statement does the new preliminary data answer, point by point?"
- **Data to pull:** the prior summary statement's numbered critiques against the resubmission's introduction-to-revisions section — a resubmission that doesn't map 1:1 usually re-scores low again.

### IACUC/IBC protocol amendment pending more than 8 weeks with bench work already scheduled

- **Usually means:** either an incomplete submission cycling back for revision (most common) or a full-committee review queued behind a monthly meeting cycle the PI didn't account for.
- **First question:** "Has the compliance office sent back a revision request, or is this sitting in the queue for the next scheduled committee meeting?"
- **Data to pull:** the compliance-office correspondence thread and the committee's published meeting/submission-deadline calendar.

### A postdoc requests first authorship after being added to a project in its final three months

- **Usually means:** either a genuine late-stage contribution large enough to justify it (a key reanalysis, a decisive experiment) or authority-based pressure disconnected from the CRediT-style contribution record.
- **First question:** "Walk me through the contribution worksheet — which cells did this person's work actually fill in?"
- **Data to pull:** the authorship-contribution worksheet (see playbook.md) filled independently by every contributor before any conversation about order.

### DFW rate (D/F/withdraw) rises after switching a course to active learning

- **Usually means:** either a genuine implementation gap (activities not scaffolded, unclear expectations) or — per Freeman et al.'s meta-analysis — a normal early-semester adjustment that resolves as students calibrate to the format, showing up as lower exam scores mid-semester but not by finals.
- **First question:** "Does the DFW increase concentrate in the first third of the semester or hold through finals?"
- **Data to pull:** exam-by-exam score distributions across the semester, compared to the prior lecture-format offering's same-exam distributions where questions overlap.

### A trainee's progress reports use the same phrase ("still troubleshooting") across three consecutive lab meetings

- **Usually means:** either a genuinely hard technical blocker that needs escalation (different reagent lot, borrowed equipment time, a collaborator's help) or a scope that's grown past what was originally proposed and nobody has said so out loud.
- **First question:** "What's the single next experiment that would tell us if this is working, and what's blocking running it this week?"
- **Data to pull:** the lab notebook or ELN's last three months of dated entries — a real blocker shows repeated attempts at the same step; scope creep shows the target quietly shifting.

### A collaborator lab can't reproduce a result from your published protocol

- **Usually means:** either an underspecified methods section (a reagent lot, a timing window, an environmental condition omitted as "obvious") or a real effect that was overstated on a single run.
- **First question:** "Did the original protocol get run by anyone other than the person who generated the published data before submission?"
- **Data to pull:** the original trainee's full protocol notes (not the published methods summary) alongside the collaborator's exact deviations.

### A single reviewer's comment triggers a full re-run of an already-published figure's underlying experiment

- **Usually means:** either a legitimate concern worth addressing before a correction becomes necessary, or reviewer overreach on a point the original data already answers.
- **First question:** "Does the existing dataset already contain the control the reviewer is asking for, under a different framing?"
- **Data to pull:** the full analysis code/notebook for the original figure, checked for whether the requested control already exists unanalyzed.
