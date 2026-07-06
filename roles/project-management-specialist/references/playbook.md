# Playbook — filled templates a specialist actually runs

Working artifacts with real structure and example numbers, continuing the $840K ERP-rollout project from `SKILL.md`'s worked example (BAC $840,000, 10-month plan, month-6 cutoff).

## 1. EVM status pack (work-package level, not just roll-up)

Roll-up numbers hide which package is actually bleeding. Break EVM out by work package before trusting the total.

| Work package | BAC | PV (cum.) | EV (cum.) | AC (cum.) | CV | SV | CPI | SPI |
|---|---|---|---|---|---|---|---|---|
| Data migration | $220K | $190K | $185K | $188K | −$3K | −$5K | 0.98 | 0.97 |
| Core config | $260K | $210K | $205K | $210K | −$5K | −$5K | 0.98 | 0.98 |
| Integrations (sub-vendor) | $260K | $95K | $30K | $92K | **−$62K** | **−$65K** | **0.33** | **0.32** |
| Testing/UAT | $100K | $25K | $10K | $15K | −$5K | −$15K | 0.67 | 0.40 |
| **Total** | **$840K** | **$520K** | **$430K** | **$505K** | **−$75K** | **−$90K** | **0.85** | **0.83** |

**Reading it:** the healthy-looking 0.85/0.83 total is entirely produced by one work package (Integrations) at 0.33 CPI — data migration and core config are essentially on plan. Report the package-level breakdown, not just the total; a sponsor who only sees "0.85 CPI" will ask the whole team to tighten up when the actual fix is renegotiating one sub-vendor scope.

**EAC formulas, applied per driver:**
- One-time cause, unlikely to recur: `EAC = AC + (BAC − EV)`
- Systemic cause, persists at current efficiency: `EAC = BAC / CPI`
- Both cost and schedule are structurally compromised: `EAC = AC + (BAC − EV) / (CPI × SPI)`
- `ETC = EAC − AC`
- `TCPI (to hit BAC) = (BAC − EV) / (BAC − AC)`; `TCPI (to hit EAC) = (BAC − EV) / (EAC − AC)` — the second should reconcile back to roughly the CPI used to build that EAC. If it doesn't, the EAC math has an error.

## 2. RAID log (Risks, Assumptions, Issues, Dependencies)

Score every open risk probability × impact on a 1–5 scale (25 max). **Escalate anything scoring ≥15** to the sponsor/steering committee; re-score every open item every status cycle — an unchanged score after 3 cycles means either it's stale or nobody actually re-assessed it.

| ID | Type | Description | Prob (1–5) | Impact (1–5) | Score | Owner | Status | Last moved |
|---|---|---|---|---|---|---|---|---|
| R-014 | Risk | Integration sub-vendor raises rate mid-contract, no renegotiation clause | 4 | 5 | **20** | PM Specialist | **Realized → Issue I-022** | Month 3 → 6 |
| R-015 | Risk | UAT environment shared with a parallel program, scheduling conflicts | 3 | 3 | 9 | Test Lead | Open | Month 4 |
| A-004 | Assumption | Business SMEs available 50% time through UAT | 3 | 4 | 12 | Sponsor | Open, unconfirmed | Month 5 |
| I-022 | Issue | Sub-vendor rate increase realized; integration package at 0.33 CPI | — | — | — | PM Specialist | **Open, CCB-bound** | Month 6 |
| D-007 | Dependency | Core config must complete before integration test start | — | — | — | Config Lead | On track | Month 5 |

**Rule:** a risk that materializes becomes an issue with its own ID and a cross-reference — don't overwrite the risk row, so the history (it was known, it was scored, here's when it hit) survives for the postmortem.

## 3. Schedule health check (DCMA-style, before trusting the critical path)

Run before reporting the critical path or float numbers in any status pack — a schedule with broken logic reports a critical path that isn't real.

| Check | Threshold | This schedule | Verdict |
|---|---|---|---|
| Missing logic (tasks w/o predecessor or successor) | ≤5% of tasks | 3.2% | Pass |
| Negative float (any task) | 0 tasks | 0 | Pass |
| Leads (negative lag between tasks) | 0% of relationships | 0.4% (2 relationships) | Flag — remove before next baseline |
| High float (tasks with float > 20% of remaining duration) | <5% of tasks flagged | 8% (mostly late-stage testing tasks) | Investigate — often means missing successor logic, not real slack |
| High duration (single tasks >44 days) | <5% of tasks | 2% | Pass |

**Float-consumption check (per reporting period, critical-path and near-critical tasks only):** if a task burns more than ~20% of its total float in one period with no logged, approved cause, treat it as a near-miss on the critical path in the next report, not after it actually goes critical.

## 4. Change control log

Every change gets logged whether approved, rejected, or absorbed within delegated tolerance. Delegated tolerance for this project (per charter): specialist may approve changes ≤ ±5% of BAC ($42K) or ≤2 weeks schedule impact without CCB; anything beyond routes to the CCB.

| CR # | Description | Cost impact | Schedule impact | Within tolerance? | Disposition | Approver | Date |
|---|---|---|---|---|---|---|---|
| CR-08 | Add a 3rd test environment to unblock UAT conflict (R-015) | +$18K | 0 weeks | Yes (< $42K) | Approved | PM Specialist | Month 5 |
| CR-09 | Rebaseline to $987K EAC / 12-month completion (Issue I-022) | +$147K | +2 months | **No** — exceeds $42K and 2-week tolerance | **Routed to CCB** | Sponsor (pending) | Month 6 |

**Rule:** the disposition column is never "implied by an updated schedule." If a change isn't in this log with a date and an approver, it didn't happen — the schedule doesn't get to move on its own.

## 5. Contingency and management reserve tracking

Keep these on two separate lines, never netted together. Contingency reserve is the specialist's to draw against named, quantified risks; management reserve requires sponsor sign-off to release.

| Reserve | Original | Drawn to date (Month 6) | % drawn | % complete (by EV/BAC) | Pacing verdict |
|---|---|---|---|---|---|
| Contingency (project-level, 5% of BAC) | $42,000 | $9,000 | 21% | 51% (430/840) | Under-paced — fine, most risk exposure is in later integration/UAT phases |
| Management reserve (sponsor-held, 10% of BAC) | $84,000 | $0 (CR-09 pending) | 0% | — | CR-09 would draw $84K of this in full plus require a $63K supplemental ask |

**Pacing rule:** contingency drawn should roughly track % complete; front-loaded drawdown (e.g., 60% of contingency spent by 20% complete) signals an estimating error at planning time, not risk being "well managed." Under-paced contingency, as here, is only reassuring if the remaining risk register doesn't show concentrated exposure late in the schedule — check the RAID log's open items before declaring it healthy.
