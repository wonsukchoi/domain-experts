# Playbook

Filled templates an installation manager runs week to week. Every table below uses plausible, internally consistent example numbers — populate with real figures, don't restructure the columns.

## 1. Six-stage pipeline tracker

Tracked per job, updated daily. The install day (crew dispatch) is only stage 4 of 6 — most of a job's calendar time lives in stages 1–3 and 5–6.

| Job # | System (kW) | Stage | Days in current stage | Next action | Owner |
|---|---|---|---|---|---|
| #109 | 7.6 | 5 — inspected, failed (label) | 1 | Reinspection request, Friday | Install mgr |
| #114 | 7.6 | 2 — under plan review | 12 (SLA: 10 business days) | Call county plan-review desk | Install mgr |
| #118 | 11.2 | 6 — PTO pending | 8 | Follow up utility portal (no ack yet) | Install mgr |
| #122 | 9.4 | 4 — install in progress | 2 | Crew A assist Wed afternoon | Crew B lead |
| #126 | 6.0 | 1 — submitted | 2 | None — inside SLA | Permitting coord |
| #131 | 14.8 | 2 — under plan review | 1 | Flag: over fast-track kW threshold, expect full study | Install mgr |

Stages: 1 submitted → 2 under plan review → 3 permit approved (install-ready once materials + customer confirmed) → 4 installed, awaiting inspection → 5 inspected, awaiting PTO → 6 PTO granted (job closeable).

## 2. Daily crew reallocation log

Logged same-day, whenever a crew is moved off its originally scheduled job. Keeps the swap auditable against both jobs' budgets.

| Date | Crew | Originally scheduled | Reason not ready | Reassigned to | Hours/$ moved |
|---|---|---|---|---|---|
| Wed | Crew A | #114 (permit pending, day 12/10 SLA) | Not install-ready | #109 callback (2 hr / $275) then #122 assist (6 hr / $825) | $1,100 of $1,100 paid day captured |
| Thu | Crew C | #126 (materials delayed 1 day) | Rack delivery slipped | #131 site survey (structural calc prep for full-study interconnection) | 4 hr / $550 |

## 3. Cost-per-watt job-costing snapshot, by segment

Compared against the trailing-quarter blended figure for the same segment — never against a single company-wide average.

| Segment | Jobs closed this quarter | Budgeted $/W | Actual blended $/W | Variance |
|---|---|---|---|---|
| Residential, roof-mount | 34 | $2.85 | $2.89 | +1.4% |
| Residential, ground-mount | 6 | $3.10 | $3.05 | -1.6% |
| Commercial, roof-mount (<50 kW) | 9 | $2.20 | $2.31 | +5.0% — flag to finance |

Flag threshold: >3% unfavorable variance on a segment (not a single job) triggers a finance review of that segment's soft costs (permitting, interconnection, acquisition) before next quarter's bids.

## 4. Interconnection tier quick-reference

Populate per utility territory — thresholds vary by state and by utility even within a state; this is the shape to fill, not universal numbers.

| Utility | Fast-track threshold | Typical fast-track turnaround | Full-study turnaround (if over threshold) | Notes |
|---|---|---|---|---|
| Example Utility A | 25 kW AC, or ≤15% of feeder peak load | 10–15 business days | 6–12 weeks | Mirrors FERC SGIP tiering |
| Example Utility B | 20 kW AC | 15–20 business days | 8–16 weeks | Requires supplemental review above 10 kW on single-phase service |

## 5. Warranty/callback reserve ledger

Tracked per job, separate from new-install labor, drawn down as reinspection fixes and other post-install labor hit it.

| Job # | Contract value | Reserve % | Reserve $ | Draws | Remaining |
|---|---|---|---|---|---|
| #109 | $24,700 | 1.5% | $370.50 | $275.00 (label reposition, NEC 690.56(C)) | $95.50 |
| #096 | $31,200 | 1.5% | $468.00 | $0 | $468.00 |
| #101 | $19,800 | 2.0% (higher-risk roof type) | $396.00 | $137.50 (flashing reseal, 1 hr) | $258.50 |

A segment or crew whose draws consistently exceed its reserve percentage is the trigger for the "warranty/callback reserve utilization above 100%" red flag — investigate before the next quarter's reserve % is set, not after.
