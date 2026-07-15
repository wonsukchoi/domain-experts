# Design critique artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Usability test cost/impact comparison (filled — see Worked example in SKILL.md for full narrative)

| | Skipped 5-user test | Post-launch discovery |
|---|---|---|
| Cost | $650 ($500 testing panel + $150 designer review time) | $357,000/month lost revenue + $4,200 hotfix engineering cost |
| Timing | Before dev handoff | 1 week after launch |
| Root cause visibility | Would likely have surfaced the required/optional field ambiguity | Discovered via support ticket spike and abandonment data |

**Reading it:** the skipped $650 check cost roughly 550x its price in the first month alone once the actual abandonment and revenue impact were quantified.

## 2. Heuristic evaluation (filled example, Nielsen's 10 heuristics applied to a checkout flow)

| Heuristic | Finding | Severity |
|---|---|---|
| Visibility of system status | Loading state after "place order" click has no visible feedback for ~2 seconds | Minor (workaround: users generally wait) |
| Match between system and real world | "Billing address" step uses internal field ordering that doesn't match how most users read a physical form (name before address) | Minor |
| User control and freedom | No way to edit cart from the billing step without losing entered address data | Major (blocks efficient task completion) |
| Error prevention | Optional field has no visual distinction from required fields | **Major — root cause of the abandonment spike** |
| Recognition rather than recall | Saved payment methods are shown as a visible list, not requiring re-entry | No issue — done well |

**Rule applied:** the error-prevention finding (optional/required field ambiguity) was flagged as major in this evaluation — a heuristic pass before launch would have caught this at $0 marginal cost beyond the review time already budgeted.

## 3. Usability test plan (filled example)

| Field | Content |
|---|---|
| Objective | Confirm the redesigned checkout flow's billing-address step doesn't introduce new completion friction |
| Method | Unmoderated task-based test, 5 participants unfamiliar with the product |
| Task | "Complete a purchase using the provided test payment details" |
| Success metric | Task completion without unprompted hesitation >5 seconds on any single field |
| Recruitment | General consumer panel matching target demographic, no prior exposure to this flow |

## 4. Severity-scored findings log (filled example)

| Finding | Severity | Fix priority |
|---|---|---|
| Optional field visually indistinguishable from required | Major | Immediate — before launch |
| Loading state feedback delay (~2s) | Minor | Next sprint |
| Cart edit requires re-entering address | Major | Before launch if feasible, else flagged as known risk |
| Slight color contrast issue on secondary button | Cosmetic | Backlog |

**Rule applied:** fix priority follows severity, not ease of implementation — the cosmetic contrast issue (easy fix) doesn't jump ahead of the major cart-edit issue (harder fix) in priority.
