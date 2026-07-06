# Red Flags — HR Specialist

Signals worth an audit pass before they become a charge, a penalty, or a lawsuit. Each maps to a specific pull, not a vibe.

### I-9 Section 2 completed more than 3 business days after the employee's first day of work
- **Usually means:** a new-hire paperwork bottleneck (manager delayed sending the hire packet, or the employee's documents weren't available on day one) rather than willful noncompliance — but ICE doesn't distinguish intent on a first review.
- **First question:** "What was the actual first day of work, and is there a dated record of when Section 2 was signed?"
- **Data to pull:** I-9 audit trail/timestamp log from the HRIS or E-Verify system for the affected hire cohort, cross-referenced against payroll's recorded start date.

### More than 5% of active I-9s past their retention or reverification trigger date
- **Usually means:** no automated reverification calendar — either List B/C documents with expirations (e.g., work authorization) aren't flagged, or terminated-employee forms aren't purged on schedule, both of which are separate exposures (reverification miss vs. over-retention).
- **First question:** "Is this a reverification gap on an active employee, or a retention-date miss on a termed one?"
- **Data to pull:** I-9 management system's expiration-date report, filtered to active employees with List C documents expiring within 90 days and to termed employees past (later of 3 years post-hire / 1 year post-termination).

### An exempt employee's job description hasn't been updated in 2+ years but their actual duties have shifted toward non-exempt work
- **Usually means:** the role drifted (e.g., a shift lead promoted for "manager" duties that quietly became mostly hourly-equivalent tasks) faster than HR's job-architecture review cycle, creating a duties-test gap the salary level doesn't cover.
- **First question:** "What percentage of this person's actual weekly hours are spent on exempt-level duties (discretion, independent judgment, supervision of 2+ FTEs) versus production/clerical work?"
- **Data to pull:** current job description, most recent duties-test worksheet (if any), and a manager-completed time-allocation estimate for the role.

### A single manager accounts for more than 2 involuntary terminations of protected-class employees within 12 months
- **Usually means:** could be legitimate performance management concentrated under a tough manager, or could be a pattern an EEOC investigator would flag on the first data pull — the concentration itself, not any single termination, is the signal.
- **First question:** "Are the documented performance issues for these terminations comparable in severity and documentation quality to this manager's terminations of non-protected-class employees?"
- **Data to pull:** termination log filtered by manager and protected-class status over the trailing 12 months, plus the performance-documentation file for each termination in the cluster.

### An ADA accommodation request sits open more than 2 weeks with no documented follow-up
- **Usually means:** the request fell into a queue behind other priorities, or the manager side of the interactive process stalled waiting on a health-provider form — either way, the absence of documentation (not the delay itself) is what removes the good-faith defense.
- **First question:** "What was the last documented interaction with the employee, and what is it waiting on right now?"
- **Data to pull:** the interactive-process log/ticket for the request, including date of initial request, all follow-up dates, and any pending medical-certification deadline.

### Fewer than 95% of full-time employees are offered ACA-compliant coverage in a given month
- **Usually means:** a headcount-classification error (part-time/variable-hour employees crossing into full-time-equivalent status under the measurement-period rules without being reclassified) rather than a deliberate coverage gap.
- **First question:** "Which specific employees crossed the 30-hours/week average threshold during the measurement period, and were they offered coverage within the stability period that followed?"
- **Data to pull:** ACA measurement-period hours report from payroll/HRIS and the benefits-enrollment offer log for the same population.

### A background-check adverse action moves from pre-adverse to final notice in fewer business days than the applicable jurisdiction requires
- **Usually means:** the background-check vendor's default workflow (often a flat 5-business-day timer) wasn't configured per state, so a jurisdiction with a longer requirement (or, conversely, a shorter one like Washington's 2-day Fair Chance Act minimum for 15+ employee employers) got the wrong wait period.
- **First question:** "What state is the candidate's position based in, and does the vendor's workflow reflect that state's specific wait-period rule?"
- **Data to pull:** vendor adverse-action timeline export for the candidate, plus the jurisdiction-specific wait-period reference table used to configure the workflow.

### More than 30% of new hires in a cohort exit within the first 90 days
- **Usually means:** expectation-mismatch during recruiting or a weak first-30-days onboarding experience rather than a hiring-quality problem — the 90-day window is long enough that "bad hire" is rarely the full explanation.
- **First question:** "In exit interviews or stay conversations for this cohort, how many cite role/expectation mismatch versus a manager or culture-fit issue?"
- **Data to pull:** 90-day attrition report by hiring manager and requisition, plus exit-interview or stay-interview notes for the departed cohort.

### An EEOC charge is filed and the underlying personnel file has fewer than 3 documented performance or conduct entries in the 12 months preceding the adverse action
- **Usually means:** the adverse action (termination, demotion, denial) was undocumented in real time and is now being reconstructed after the fact — which is exactly the fact pattern that turns a defensible decision into a credibility problem in front of an investigator.
- **First question:** "What is the earliest dated document in this file that reflects the performance or conduct issue driving this action?"
- **Data to pull:** full personnel file with document creation dates (not just content), and the manager's contemporaneous notes or performance-system entries for the 12 months prior.

### A leave request is denied and the FMLA worksite headcount calculation used the company-wide total instead of the 75-mile radius count
- **Usually means:** whoever ran the eligibility check applied "we're big enough" shorthand instead of pulling the actual worksite-radius headcount, which is the single most common FMLA eligibility miss.
- **First question:** "What is the headcount of employees working within 75 miles of this employee's specific worksite, not the company total?"
- **Data to pull:** HRIS worksite/location report showing active headcount within a 75-mile radius of the employee's assigned location, as of the date leave was requested.

### A non-exempt employee's timesheet shows more than 5 hours of unpaid "off-the-clock" work in a pay period (email responses, setup/teardown, on-call check-ins)
- **Usually means:** informal expectation-creep from a manager ("just check email before you clock in") that HR didn't catch because it doesn't show up as a formal policy change — it shows up as a pattern in timesheet gaps versus badge/login data.
- **First question:** "Is there a system timestamp (email, VPN login, badge swipe) that shows work activity outside the clocked hours on the timesheet?"
- **Data to pull:** timesheet data cross-referenced against email/VPN/badge logs for the same employee over a representative pay period.

### A workers' comp claim's first report of injury is filed more than 5 business days after the employee reported the injury to a supervisor
- **Usually means:** the supervisor didn't know the reporting deadline or treated a minor-seeming injury as not requiring immediate escalation, which risks a late-filing penalty and weakens the claim's credibility if it develops into something more serious.
- **First question:** "What date did the employee first tell any supervisor about the injury, versus the date the claim was actually filed with the carrier?"
- **Data to pull:** the incident report, the claim-filing timestamp from the carrier portal, and any supervisor communication (email/text) referencing the injury before the formal filing.
