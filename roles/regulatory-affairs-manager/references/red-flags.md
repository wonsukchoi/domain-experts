# Red flags — signals a regulatory affairs manager notices instantly

Smell tests with thresholds. Any one alone can be manageable; two or more on the same submission or product line is a pattern worth escalating before it reaches the agency.

### Predicate device has an open recall or active FDA warning letter
- **Usually means:** using it invites the same scrutiny onto the new submission — reviewers cross-reference a predicate's compliance history, and an active issue reads as elevated risk by association.
- **First question:** "Is there a cleaner predicate with the same intended use and no open compliance action, even if it's a slightly weaker technological match?"
- **Data to pull:** FDA warning letter database, MAUDE adverse event reports for the predicate, recall classification and current status.

### Label claim uses broader language than the tested population, endpoint, or vendor/device compatibility
- **Usually means:** marketing or business development pushed the claim wording past what the clinical/bench study actually measured — the single most common deficiency-letter trigger.
- **First question:** "Point me to the exact data table that supports this exact claim wording — not the study in general, the specific number."
- **Data to pull:** claims-to-evidence gap matrix (see `references/artifacts.md` §2), study protocol's stated primary/secondary endpoints, subgroup analysis if the claim implies a specific population.

### Post-approval design change classified as "letter to file" without a documented decision-tree assessment
- **Usually means:** the change owner assumed "minor" without checking whether it touches intended use, sterilization, or a safety-critical software path — exactly the categories that require a new submission.
- **First question:** "Walk me through the decision tree for this specific change — which branch, and where's the signed rationale in the Design History File?"
- **Data to pull:** change description and engineering rationale, Design History File entry (or its absence), prior similar changes and how they were classified.

### Complaint or adverse-event rate trending up without a corresponding reportability-decision memo
- **Usually means:** either the trend hasn't been reviewed against the MDR/vigilance reportability criteria yet, or it was reviewed informally with no documented "file/don't file" rationale — both look identical to an auditor as "no assessment occurred."
- **First question:** "For the last five complaints in this cluster, is there a dated reportability memo for each, or just an internal Slack thread?"
- **Data to pull:** complaint trend by device/lot, reportability memos (or gap), awareness dates versus filing dates if any were filed.

### Pre-submission (Q-sub) meeting requested with less than the agency's typical scheduling lead time before a planned submission
- **Usually means:** the submission timeline was built without buffer for pre-submission feedback, which risks either skipping the meeting under time pressure or delaying the submission past its target window.
- **First question:** "If FDA's Q-sub feedback contradicts our current evidence plan, do we have runway left to act on it before the planned filing date?"
- **Data to pull:** Q-sub request submission date versus planned filing date, agency's published typical scheduling window for the meeting type, evidence-plan lock date.

### Clinical or bench study designed and locked before the classification/pathway decision was finalized
- **Usually means:** the evidence plan may not match what the eventual pathway requires — a study designed for a 510(k) substantial-equivalence argument often under-powers a De Novo's novel-device evidence bar.
- **First question:** "Was this study's endpoint and sample size sized against the pathway we're now pursuing, or against an earlier assumption?"
- **Data to pull:** study protocol version history and its date versus the pathway decision date, statistical power calculation and its stated assumptions.

### Global launch sequence files simultaneously in multiple markets rather than sequencing off a reference approval
- **Usually means:** duplicated review effort across markets that could have leveraged one reference-market decision, and inconsistent label language risk if markets approve different claim scopes at different times.
- **First question:** "Which market's approval would other regulators in this launch plan actually recognize or streamline against, and why isn't that one filed first?"
- **Data to pull:** target market list and each market's reciprocity/recognition agreements with the reference market, current filing sequence and dates.

### Submission's Additional-Information response drafted without involving the original study's statistician or lead investigator
- **Usually means:** responses risk being written to satisfy the checklist wording rather than substantively addressing the reviewer's actual statistical or clinical concern, which often triggers a second AI cycle.
- **First question:** "Did the person who ran the analysis review this response before it went out, or did regulatory affairs draft it alone?"
- **Data to pull:** AI letter and response draft, sign-off list on the response, prior AI-cycle history for this device type if any.

### Software or algorithm version deployed post-clearance without a documented change-impact assessment
- **Usually means:** treating a software update as routine IT maintenance rather than a regulated device change — this is the fastest route to an unreported/undocumented change that surfaces during an audit or a post-market event investigation.
- **First question:** "Does this version change affect model performance, training data, or any claimed specification — and is there a dated assessment either way?"
- **Data to pull:** version-change log, performance-delta testing if any, change-control decision-tree entry for this specific release.
