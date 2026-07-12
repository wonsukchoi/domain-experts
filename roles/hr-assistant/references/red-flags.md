# Red Flags — HR Assistant

Signals worth a process check before they become an audit finding, a payroll error, or a liability the role wasn't authorized to create. Each maps to a specific pull, not a vibe.

### More than 5% of a new-hire cohort has I-9 Section 2 completed outside the 3-business-day window
- **Usually means:** hiring-manager delay getting the new hire in for document review, or documents unavailable on Day 1 — rarely willful noncompliance on a first occurrence.
- **First question:** "What was the actual verified first day of work, and is there a timestamped record of when Section 2 was signed?"
- **Data to pull:** I-9 case log timestamps cross-referenced against payroll's recorded start date for every hire in the cohort.

### Benefits effective date entered as hire date instead of the plan document's waiting-period date, on more than one record per onboarding cohort
- **Usually means:** the HRIS onboarding template has a free-text effective-date field with no computed lookup, so entry defaults to habit rather than the plan document.
- **First question:** "Does the onboarding template compute the effective date from the plan's waiting-period rule, or is it typed in manually?"
- **Data to pull:** plan document's waiting-period clause, HRIS benefits-effective-date field for the cohort, payroll deduction start dates.

### A medical, immigration, or background-check document found in the general personnel file rather than its segregated file
- **Usually means:** a manager or new hire handed the document directly to whoever was nearest, bypassing the intake checklist rather than a deliberate misfile.
- **First question:** "Who filed this, and was the standard intake checklist followed for this hire?"
- **Data to pull:** file-access log (if digital) or physical audit note, plus the onboarding intake checklist completion record for that hire.

### The same interpretive question type gets escalated more than 3 times in a month with no documented answer template
- **Usually means:** a genuine policy gap or an outdated FAQ resource, not several employees independently confused about unrelated things.
- **First question:** "Is there a standing answer for this question, and where does it live for the next person who asks?"
- **Data to pull:** inquiry/ticket log tagged by question type, current FAQ or knowledge-base article for that topic.

### Background-check vendor turnaround exceeds the standard SLA on more than 10% of checks in a month
- **Usually means:** a vendor-capacity issue or candidate delay providing consent or supplemental information — rarely a coordination failure once the pattern is checked case by case.
- **First question:** "Is each delayed case vendor-side or candidate-side?"
- **Data to pull:** vendor portal status timestamps and candidate consent/submission dates for the affected checks.

### A personnel-file audit finds a missing signed offer letter, I-9, or W-4 for an active employee
- **Usually means:** the item was verbally confirmed at hire but never actually collected and filed, a gap that widens the longer the employee stays without anyone re-checking.
- **First question:** "When was this file last audited, and is the employee reachable to re-collect the missing item now?"
- **Data to pull:** new-hire document checklist completion log dated to that employee's start date.

### More than one field mismatch between the HRIS census and the payroll register for the same pay period
- **Usually means:** a manual re-entry step exists between the two systems instead of a direct feed, and something was dropped or mistyped in transit.
- **First question:** "Is there a direct integration between HRIS and payroll for this field, or a manual step?"
- **Data to pull:** HRIS census export and payroll register for the same pay date, diffed field by field.

### The same hiring manager flags "urgent" scheduling more than twice in a quarter without the requisition itself carrying an urgent priority
- **Usually means:** the manager has learned that declaring urgency gets faster service, not that the requisition is genuinely time-sensitive.
- **First question:** "Is this requisition flagged urgent by the recruiter or HR manager, or only by the hiring manager?"
- **Data to pull:** requisition priority field in the ATS and the req-aging report.

### An employment-verification response includes anything beyond title, dates, and rehire eligibility without a written authorization on file
- **Usually means:** the requester pushed for more (salary, performance, reason for separation) and it was given without routing through the standard verification script.
- **First question:** "What script or policy governs this response, and does a signed authorization exist for the additional detail given?"
- **Data to pull:** the verification request log and the standard reference-response policy.

### An I-9 for a terminated employee remains in the active file past its retention date (later of 3 years post-hire or 1 year post-termination)
- **Usually means:** no calendared annual purge, so termed-employee forms accumulate past their retention window unnoticed.
- **First question:** "When was the last annual I-9 purge run, and does it cover this termination date?"
- **Data to pull:** I-9 management system's retention-date report filtered to terminated employees past the later of the two dates.
