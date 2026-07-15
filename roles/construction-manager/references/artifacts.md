# Schedule & contingency artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. CPM schedule excerpt with float (filled — see Worked example in SKILL.md for full narrative)

| Task | Duration | Float | Predecessor | On critical path? |
|---|---|---|---|---|
| Demolition | 5 days | 0 | — | Yes |
| Framing repair (deteriorated condition found) | 5 days (was 2) | 0 | Demolition | Yes |
| Electrical rough-in | 6 days | 0 | Framing repair | Yes |
| Plumbing rough-in | 4 days | 3 days | Demolition | No |
| Exterior painting prep | 3 days | 8 days | (parallel scope) | No |

**Rule applied:** coordination effort and crashing budget go to the zero-float row (framing repair), not to plumbing or painting, which have slack and don't affect the finish date.

## 2. Contingency tracker (filled example)

| Draw # | Reason | Amount | Running balance | % of original ($85,000) remaining |
|---|---|---|---|---|
| — | Original contingency | — | $85,000 | 100% |
| 1 | Deteriorated framing repair | $7,600 | $77,400 | 91% |
| 2 | Weekend crew schedule crash | $4,200 | $73,200 | 86% |

**Rule applied:** every draw is logged with reason and running balance — if the balance trend projects to zero before project completion at the current burn rate, that's a flag to revisit the contingency itself, not just approve draws one at a time.

## 3. RFI log (filled example)

| RFI # | Question | Opened | Blocks | On critical path? | Status |
|---|---|---|---|---|---|
| 014 | Beam connection detail unclear at column C-4 | Day 22 | Steel erection | Yes | Escalated day 28 (6 days open) — resolved day 29 |
| 015 | Paint color confirmation for exterior trim | Day 25 | Exterior painting | No (8 days float) | Open, not escalated |

**Rule applied:** RFI 014 gets escalated because it blocks critical-path work; RFI 015 doesn't need the same urgency because painting has 8 days of float to absorb a slower answer.

## 4. Schedule impact notice template (filled — see Worked example in SKILL.md for the full quoted version)

| Field | Value |
|---|---|
| Discovered condition | Deteriorated framing at [location] |
| Discovery date | Demolition, day 22 |
| Critical path? | Yes |
| Unmitigated schedule impact | +5 days |
| Mitigation | Engineer-assessed repair + weekend crew crash |
| Mitigated schedule impact | +2 days |
| Cost | $11,800 total ($7,600 repair + $4,200 crash) |
| Contingency remaining after this event | $73,200 of $85,000 (86%) |
| Recommendation | Proceed with crash — $4,200 cost avoids $6,000 in owner delay costs |
