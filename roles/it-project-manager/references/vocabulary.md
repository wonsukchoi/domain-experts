# IT Project Manager — Vocabulary

### Float (slack)
The amount of time a task can slip without delaying the project end date, computed from the critical path network.
**In use:** "The QA task has 6 days of float, so a 3-day slip there doesn't touch the go-live date."
**Common misuse:** Treating any task that "feels behind" as urgent, regardless of float — a task with 10 days of float slipping by 3 days is not a fire; a critical-path task slipping by 1 day is.

### Critical path
The longest sequence of dependent tasks through the project network — its total duration sets the minimum possible project length, and any slip on it slips the end date directly.
**In use:** "Data migration is on the critical path now that the vendor hardware delay ate the integration team's float."
**Common misuse:** Assuming the critical path is fixed at baseline — it shifts whenever a near-critical task's float gets consumed, and must be recalculated after material changes, not just at the monthly review.

### Crashing
Adding resources to a critical-path task to shorten its duration, at additional cost.
**In use:** "We can crash the migration task with one more senior engineer for $18K and buy back two weeks."
**Common misuse:** Treated as a free lever — coordination overhead and ramp-up time mean crashing has diminishing, sometimes negative, returns past roughly two added resources on most software tasks.

### Fast-tracking
Running normally sequential tasks in parallel to shorten the schedule, accepting increased rework risk.
**In use:** "We fast-tracked UAT to start before the last integration build was frozen — accepted the rework risk to hit the date."
**Common misuse:** Confused with crashing — fast-tracking costs schedule risk, not (necessarily) money; crashing costs money, not necessarily added risk to unrelated tasks.

### Baseline
The formally approved scope, schedule, and budget plan against which all future variance is measured.
**In use:** "We haven't re-baselined since the change request, so this SPI is measuring against a plan we've already agreed is outdated."
**Common misuse:** Treating the baseline as permanent — it should be formally revised (re-baselined) when cumulative approved changes make the original comparison meaningless, otherwise every subsequent status report misleads.

### Earned Value (EV)
The budgeted value of work actually completed, measured against objective milestones — not the amount spent, and not the percent-complete self-reported by the task owner.
**In use:** "Two of those seven 'nearly done' tasks don't have a passed test yet, so EV is lower than the team's self-report implies."
**Common misuse:** Confusing EV with actual cost (AC) — a project can spend a lot (high AC) while producing comparatively little earned value, which is exactly what a bad CPI reveals.

### CPI (Cost Performance Index)
EV divided by AC; a ratio below 1.0 means less value is being produced per dollar spent than planned.
**In use:** "CPI of 0.86 means we're getting 86 cents of planned work for every dollar spent."
**Common misuse:** Reading CPI in isolation without SPI — a low CPI with a high SPI (ahead of schedule) is a different, less alarming situation than low CPI with low SPI.

### SPI (Schedule Performance Index)
EV divided by PV; a ratio below 1.0 means the project is producing work more slowly than the schedule baseline planned.
**In use:** "SPI of 0.92 says we're running about 8% behind planned pace."
**Common misuse:** Treating SPI as a direct measure of calendar delay — it's a value ratio, not a day count; the actual schedule slip has to come from re-running the critical path, not from SPI alone.

### Change control board (CCB)
The formal body (often the sponsor or steering committee) that approves or rejects scope/schedule/budget changes against the baseline.
**In use:** "That's a scope change — it needs to go through the CCB, not get agreed in the hallway."
**Common misuse:** Bypassing the CCB for "small" asks that cumulatively erode the baseline without ever showing up as a tracked, approved change.

### RAID log
A consolidated tracking artifact for Risks, Assumptions, Issues, and Decisions — the single source of truth superseding ad hoc lists.
**In use:** "Log that as a risk in the RAID, not just a note in the meeting minutes — it needs an owner and a review date."
**Common misuse:** Maintaining separate, disconnected risk lists and decision logs, which lets items fall through without a single place anyone reviews on a cadence.

### Work breakdown structure (WBS)
The hierarchical decomposition of total project scope into discrete, assignable work packages.
**In use:** "EVM only works because the WBS is fine enough that each package has an objective completion milestone."
**Common misuse:** Building a WBS coarse enough that "percent complete" per package is still a subjective guess — which quietly reintroduces the self-report optimism problem EVM exists to remove.

### Estimate at Completion (EAC)
The current forecast of total project cost, computed as Budget at Completion divided by CPI (when the current cost-performance trend is expected to continue).
**In use:** "At today's CPI of 0.86, EAC comes out to $1.12M against a $960K baseline — that's the number the sponsor needs, not the original budget."
**Common misuse:** Continuing to report the original budget as the expected final cost after CPI has clearly diverged from 1.0 for multiple periods.
