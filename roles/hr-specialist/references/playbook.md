# Playbook

Filled templates and step sequences for the recurring HR-specialist processes. Adapt the numbers to the actual case; keep the sequence and the thresholds.

## 1. FMLA eligibility determination worksheet

Run this against every leave request before quoting an entitlement — never from memory.

```
EMPLOYEE: J. Alvarez                          REQUEST DATE: 2026-03-10
LEAVE REASON: Own serious health condition (knee surgery, ~6 wks recovery)

TEST 1 — Tenure
  Hire date: 2024-11-04    →  16 months employed as of request date   PASS (≥12 mo)

TEST 2 — Hours worked, trailing 12 months
  Payroll hours 2025-03-10 to 2026-03-10: 1,410 hrs                   PASS (≥1,250)

TEST 3 — Worksite headcount (NOT company-wide)
  Employee's worksite: Denver distribution center
  Headcount at that worksite: 38
  Headcount at worksites within 75 mi (incl. Denver): 38 + 19 (Aurora) = 57
                                                                        PASS (≥50)

DETERMINATION: Eligible. Entitlement: up to 12 workweeks unpaid,
  job-protected, within a rolling 12-month look-back window anchored
  to first use.

12-MONTH LOOK-BACK CALC (rolling method):
  Look back from each day leave is taken; count FMLA weeks already
  used in the trailing 365 days from that day. Prior use this rolling
  year: 0 wks. Remaining entitlement: 12 wks (480 hrs at 40 hr/wk).

NEXT ACTIONS:
  [ ] WH-381 (rights & responsibilities notice) sent within 5 business days
  [ ] Certification (WH-380-E) requested, 15-calendar-day return window
  [ ] Designation notice (WH-382) sent within 5 business days of receiving
      certification, or of the 15-day window lapsing
  [ ] Calendar entitlement-exhaustion date: start date + 12 wks
  [ ] Manager notified of schedule impact (not diagnosis) same day
```

**If Test 3 fails:** check state family/medical leave law (many states use a lower or no worksite-size floor — e.g., some state laws cover employers with 15–25 employees, no 75-mile test). Don't stop at "FMLA doesn't apply" — restate as "federal FMLA doesn't apply; check [state] leave law."

## 2. ADA interactive-process log

Open this the same day an accommodation request or an obvious-need signal (visible impairment, doctor's note limiting duties) arrives — before assessing feasibility.

```
EMPLOYEE: R. Chen                     ROLE: Warehouse associate
REQUEST: "I need to avoid repetitive overhead lifting" (verbal, 2026-04-02)

STEP 1 (Day 0): Acknowledge request in writing; request medical
  documentation of the functional limitation (not the diagnosis).
  Sent: 2026-04-02.

STEP 2 (Day 0–10): Identify essential functions of the role from the
  job description, cross-checked against what's actually performed.
  Essential functions here: pallet staging (yes), overhead restocking
  (occasional, ~10% of shift), inventory scanning (yes).

STEP 3 (Day 7, doc received 2026-04-09): Medical documentation confirms
  15-lb overhead lift restriction, 90 days, post-surgical.

STEP 4: Brainstorm accommodation options with employee present, ranked:
  a) Reassign overhead restocking to team lead during restriction window
     (no essential-function change, no cost) — SELECTED
  b) Lift-assist device for overhead tasks ($1,200) — held in reserve
     if (a) creates coverage gaps
  c) Temporary reassignment to a non-lifting role — not needed given (a)

STEP 5: Document the selected accommodation, start date, review date,
  and confirm with employee in writing same day as decision.
  Accommodation: overhead tasks reassigned 2026-04-10 through 2026-07-09.
  Review date calendared: 2026-07-02 (before expiration, to reassess).

STEP 6 (review date): Confirm restriction lifted, extended, or made
  permanent; close the log or reopen Step 4 if circumstances changed.
```

**Undue-hardship test (only if no viable accommodation found):** document specific cost/disruption against the employer's actual size and budget, not a general "too expensive" — an unsupported hardship claim is functionally the same exposure as skipping the process.

## 3. I-9 retention-date calculator

Run per employee, at hire and again at termination — never estimate.

```
Rule: retain until the LATER of (hire date + 3 years) OR (termination date + 1 year)

Case A — short tenure (worked 2024-01-15 to 2024-09-30, 8.5 months):
  Hire + 3 yrs  = 2027-01-15
  Term + 1 yr   = 2025-09-30
  Retain until: 2027-01-15  (hire-date rule controls — tenure < ~2 yrs)

Case B — long tenure (worked 2018-06-01 to 2026-02-28, ~7.75 years):
  Hire + 3 yrs  = 2021-06-01
  Term + 1 yr   = 2027-02-28
  Retain until: 2027-02-28  (termination-date rule controls — tenure > ~2 yrs)

Crossover point: roughly 2 years of tenure is where the controlling rule
flips from hire-date to termination-date — flag any employee near that
line for manual double-check rather than a shortcut formula.
```

**Annual audit cadence (minimum):** pull all I-9s past their retention date each January; purge those past date, flag any active employee missing a current I-9 or missing reverification for an expiring work-authorization document (check List A/C expiration dates against today + 90 days).

## 4. ACA employer shared-responsibility penalty calculator

```
INPUTS
  Full-time equivalent headcount (FT, monthly avg): 45
  Coverage offered to ≥95% of FT employees?: No
  # FT employees receiving marketplace premium tax credit: 4
  Penalty A rate (annual, per FT employee, 2026 indexed): $3,340
  Penalty B rate (annual, per affected employee, 2026 indexed): $5,010

PENALTY A (no coverage offered to ≥95% of FT, §4980H(a)):
  (FT headcount − 30) × $3,340
  = (45 − 30) × $3,340
  = $50,100 / yr  →  $4,175 / month while condition holds

PENALTY B (coverage offered but unaffordable/inadequate for some, §4980H(b)):
  applies only if the 95% offer threshold IS met; scoped to affected employees
  # affected employees × $5,010
  = 4 × $5,010 = $20,040 / yr (illustrative, if offer threshold were met)

DECISION RULE: if offer rate < 95% of FT headcount, penalty A applies to
  the ENTIRE FT headcount minus 30 — not to the count of employees who
  received a credit (see SKILL.md's worked example for the reasoning and
  the CFO-facing writeup this calculator feeds). Penalty B only becomes
  the relevant calculation once the 95% offer threshold is satisfied.

AFFORDABILITY CHECK (per employee, for penalty B applicability):
  employee's lowest-cost self-only premium contribution ≤ 9.96% of
  household income (2026 indexed figure; use W-2 safe harbor if household
  income unknown: box 1 wages × 9.96% ÷ 12 = max monthly contribution).
```

## 5. FCRA background-check adverse-action sequence

```
STEP 1: Obtain consumer report; make preliminary decision.
STEP 2 (if leaning adverse): Send PRE-ADVERSE ACTION notice — includes
  copy of the report, "A Summary of Your Rights Under the FCRA," and a
  statement that a final decision hasn't been made.
STEP 3: WAIT — jurisdiction-specific minimum, from date of confirmed
  receipt (not send date):
    California:            5 business days
    New York City:         5 business days (position must remain open)
    Washington (FCA, eff. Jul 2026, employers 15+ employees): 2 days
    No applicable state/local rule:                            5 business
                                                                 days (federal practitioner norm; FCRA sets no fixed
                                                                 number — "reasonable period")
STEP 4: If candidate disputes or submits information during the wait,
  re-evaluate before proceeding — the wait exists so this can happen.
STEP 5: Send FINAL ADVERSE ACTION notice — includes name/contact of
  reporting agency, statement that the agency didn't make the decision,
  and the right to dispute accuracy/completeness with the agency.
STEP 6: Log the sequence dates (report received, pre-adverse sent,
  wait-period end, final notice sent) in the candidate file — the dates
  are the defense if the timeline is ever challenged.
```

## 6. 90-day onboarding sequence (retention-framed, not checklist-framed)

```
BEFORE DAY 1 (logistics — necessary, not sufficient):
  Equipment shipped/provisioned, accounts created, I-9 Section 1 sent
  for completion by end of Day 1, Section 2 scheduled within 3 business
  days of start.

WEEK 1 — target: reduce first-week flight risk (see SKILL.md first-principles
  #5 for the underlying stats this sequence is built to counter)
  Day 1: manager 1:1 (role expectations, first 30/60/90 goals drafted
    together, not handed down); team intro; buddy assigned.
  Day 3: check-in — "does the job match what you expected?" (targets the
    expectation-mismatch attrition driver directly).
  Day 5: HR check-in independent of manager — surfaces issues employees
    won't raise with their new boss yet.

WEEK 2–4 — target: culture connection, run deliberately rather than left ambient
  Structured intros to 3–5 cross-functional partners, not just the team.
  First deliverable assigned, scoped to be completable and reviewed by
  day 30 — a visible early win, not a first-quarter-sized project.

DAY 30: Manager + HR joint check-in. Explicit go/no-go read on the three
  attrition drivers: expectation match, team connection, onboarding
  experience. Any "no" on two or more → escalate to a structured
  30-60-90 reset, not a wait-and-see.

DAY 60: Goals review against the Day-1 30/60/90 plan; adjust scope if
  mis-set initially.

DAY 90: Formal review. This is the retention-risk checkpoint — treat a
  lukewarm 90-day review as an actionable signal, not a formality to file.
```
