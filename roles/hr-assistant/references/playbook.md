# Playbook

Filled templates and step sequences for the recurring HR-assistant transactions. Adapt the numbers to the actual case; keep the sequence, the deadlines, and the escalation points.

## 1. New-hire paperwork / I-9 timeline

```
EMPLOYEE: D. Osei                              HIRE DATE (first day of work): 2026-03-09

DAY 0 (2026-03-09):
  [ ] I-9 Section 1 completed by employee (deadline: first day of work — no grace period)
  [ ] Offer letter countersigned copy filed
  [ ] W-4 / state withholding form collected
  [ ] Equipment/accounts provisioned request submitted

DAY 0–3 business days (deadline: 2026-03-12, i.e. Mon–Wed if hire is Monday):
  [ ] I-9 Section 2 completed — employer reviews original List A, or List B+C, documents
      in person or via authorized representative
  [ ] E-Verify case created (if employer participates) — same 3-business-day clock,
      run in parallel with Section 2, not sequentially after it

IF DOCUMENTS UNAVAILABLE ON DAY 1:
  Do NOT delay Section 1 — it is independent of the document-review step.
  Employee may present a receipt for a replacement document (not the document
  itself) for List A/B/C in limited cases; document review must still complete
  within the original 3-business-day window using the receipt rule, not an
  extended deadline.

REVERIFICATION TRACKING (if List C document has an expiration date):
  Document: Employment Authorization Document, expires 2027-01-15
  Calendar reminder set: 2026-12-15 (30 days prior) to request updated document
```

## 2. Personnel-file segregation audit

Run quarterly on a rolling sample (minimum 10% of active files or 20 files, whichever is larger), plus any file touched by a recent leave/accommodation/background-check case.

```
FILE: M. Torres                                AUDIT DATE: 2026-02-10

GENERAL FOLDER — should contain: offer letter, signed acknowledgments,
  performance reviews, disciplinary records, job description, general correspondence.
  FOUND: accommodation-related medical note (physician letter, dated 2026-01-20)
         — MISPLACED, does not belong here.

MEDICAL FOLDER (segregated, separate access) — should contain: FMLA
  certifications, ADA accommodation medical documentation, workers' comp
  medical records.
  ACTION: relocate the 2026-01-20 letter here same day. Confirm category only
  (accommodation-related medical documentation) — do not read for content
  beyond what's needed to classify it correctly.

I-9 FOLDER (segregated, separate from both above) — Section 1, Section 2,
  supporting documents, reverification records. Never store I-9s in the
  general personnel file (a common finding in DOL/ICE audits).
  FOUND: correctly filed.

RESULT: 1 misfile found, corrected same day, logged in the audit tracker
  with before/after location and correction timestamp.
```

## 3. Background-check coordination and adverse-action sequence

```
CANDIDATE: K. Ferreira                    ROLE: Warehouse supervisor
CONSENT SIGNED: 2026-04-01

STEP 1 (Day 0): Order report from vendor (Sterling) after signed consent on file.
STEP 2 (Day 3, 2026-04-04): Report returned. Flag: misdemeanor conviction,
  2021, unrelated to job duties on its face.
STEP 3: THIS ROLE DOES NOT DECIDE. Route the report and the individualized-
  assessment worksheet (nature of offense, time elapsed, job relatedness) to
  the hiring manager and HR specialist same day — coordination role ends at
  routing, not at recommending an outcome.
STEP 4 (if leaning adverse, per specialist/manager decision): Send PRE-ADVERSE
  ACTION notice — includes a copy of the report and "A Summary of Your Rights
  Under the FCRA." Sent: 2026-04-05.
STEP 5: WAIT — jurisdiction-specific minimum from date of confirmed receipt:
  California / NYC: 5 business days       Washington (FCA, employers 15+): 2 days
  No applicable state/local rule: 5 business days (federal practitioner norm)
  Track: receipt confirmed 2026-04-06 → earliest final notice date 2026-04-13.
STEP 6: If candidate disputes or submits information during the wait, log it
  and route back to the specialist for re-evaluation before proceeding —
  do not independently judge whether the new information changes the outcome.
STEP 7: Send FINAL ADVERSE ACTION notice only after the wait period clears
  and the specialist/manager confirms the decision stands.
STEP 8: Log every date in this sequence (consent, report received, flag
  routed, pre-adverse sent, receipt confirmed, wait-period end, final notice
  sent) — this timeline is the record if the sequence is ever challenged.
```

## 4. Benefits effective-date lookup (plan-document driven, not memory-driven)

```
PLAN DOCUMENT RULE (§4.2): coverage effective 1st of month following 30
  days of continuous employment.

LOOKUP TABLE — hire date → 30-day mark → correct effective date:
  Hire 1/6   → 30 days = 2/5   → effective 3/1
  Hire 1/20  → 30 days = 2/19  → effective 3/1
  Hire 2/3   → 30 days = 3/5   → effective 4/1
  Hire 2/18  → 30 days = 3/20  → effective 4/1

RULE OF THUMB: any hire date in the first half of a month typically lands
  its 30-day mark still within the following month, pushing effective date
  to the month AFTER that — do not assume "next month" without running the
  actual 30-day add. A hire on the last few days of a month often pushes
  the 30-day mark two calendar months out; always compute, never eyeball.

CROSS-CHECK BEFORE SUBMITTING TO PAYROLL: does the HRIS "coverage effective
  date" field match this table's output, or does it default to the hire
  date? If it defaults to hire date and isn't manually overridden, payroll
  will start deducting early — this is the error pattern in SKILL.md's
  worked example.
```

## 5. Employment-verification response script

```
INCOMING REQUEST TYPE: Verification of employment (former employer reference
  call, mortgage lender, background-check company for another employer)

STANDARD RESPONSE — confirm ONLY:
  - Job title(s) held and dates of employment
  - Whether full-time or part-time
  - Eligibility for rehire (yes/no/per policy, from the personnel file flag)

DO NOT PROVIDE without separate written employee authorization on file:
  - Salary or compensation details
  - Performance ratings or disciplinary history
  - Reason for separation, beyond "voluntary" or "involuntary" if policy allows
  - Any medical, accommodation, or leave information — ever, regardless of
    authorization, unless the request is a specific legal subpoena routed
    through HR specialist/legal first

IF REQUESTER PUSHES FOR MORE: "I can confirm dates and title. For anything
  beyond that, we'd need [written authorization from the employee / to route
  this through our HR specialist]." Log the call: requester, date, what was
  confirmed, whether pushed for more.
```
