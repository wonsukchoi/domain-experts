# Artifacts

Filled templates for the three documents a correctional services manager produces most: the staffing risk-acceptance memo, the use-of-force after-action review, and the classification review trigger log.

## Staffing risk-acceptance memo (filled example)

```markdown
# Staffing Risk Memo — Third Shift Reduction Proposal

Facility: [Name] | Rated capacity: 800 | Current population: 850 (106%)
Proposed change: reduce third-shift ratio from 1:12 to 1:18

Historical incident rate by staffing ratio (this facility, trailing data):
  1:12 -> 2.1 incidents / 1,000 inmate-days
  1:15 -> 2.4 incidents / 1,000 inmate-days
  1:18 -> 5.8 incidents / 1,000 inmate-days (measured 2024, prior staffing cut)

Projected quarterly incidents at proposed ratio: ~443
Current quarterly trajectory (already +40% QoQ): ~225

Risk determination: NOT ACCEPTED AT MANAGER LEVEL. Escalated to oversight
board per policy — any staffing level below documented critical minimum
(1:15 for this facility) requires board-level risk acceptance, not
administrative implementation.

Mitigation options presented to board:
  1. Restore funding to maintain 1:15 minimum — estimated cost: $340,000/year
  2. Expedited population reduction to bring under rated capacity — target
     -50 inmates via transfer/parole coordination, estimated 6-8 weeks
  3. Reallocate 2 non-custody administrative staff to critical third-shift
     posts as an interim measure while option 1 or 2 is pursued

Board decision required by: [date] — third-shift schedule for next pay
period is otherwise locked at current (1:12) staffing.
```

## Use-of-force after-action review (filled example)

```markdown
# After-Action Review — UOF Incident #2026-0847

Date/time: [date], 14:20
Location: Housing Unit C, Pod 3
Staff involved: 2 officers
Summary: Physical restraint applied following inmate non-compliance with
housing move order; minor injury to inmate (bruising), no staff injury.

System-factor review (completed BEFORE individual conduct review):
  Staffing at time of incident: 1 officer covering pod (short 1 from
  posted minimum of 2) due to unfilled call-out.
  Classification status: inmate had an unreviewed mental health flag
  from 11 days prior — review was due at 7 days per policy, was overdue.
  De-escalation attempted: verbal de-escalation attempted per report,
  duration approximately 90 seconds before physical intervention.
  Physical plant: no camera coverage of the specific cell front where
  the incident began (documented blind spot, flagged in 2 prior reviews).

Findings:
  1. Overdue mental health review is a contributing factor — inmate's
     recent crisis flag may have affected compliance response. POLICY
     GAP: no automated alert exists for overdue reviews past 48 hours.
  2. Understaffing at time of incident reduced available de-escalation
     options (single officer vs. two-officer standard response).
  3. Camera blind spot has now contributed to 3 incidents in 8 months —
     capital request for coverage in this location is now a priority
     item, not a routine backlog item.

Individual conduct review: separate track, per policy — use-of-force
technique itself found within policy given the circumstances above.

Action items: (1) automated overdue-review alert, owner IT/Records,
due 30 days. (2) camera coverage capital request, owner Facilities,
escalated to priority. (3) staffing call-out backfill policy review,
owner Operations, due 14 days.
```

## Classification review trigger log (filled example)

```markdown
# Classification Review Trigger Log — [Month/Year]

Trigger event                  | Inmate ID | Review due (per policy) | Completed | Status
--------------------------------|-----------|---------------------------|-----------|--------
Assault involvement (victim)    | #4471     | Within 24 hours           | On time   | Closed - housing unchanged
Gang affiliation change (flag)  | #3982     | Within 48 hours            | On time   | Closed - reclassified, moved
Mental health crisis flag        | #5104     | Within 7 days               | 11 days   | OVERDUE - contributed to UOF #2026-0847
Disciplinary infraction (Class A)| #4890     | Within 72 hours            | On time   | Closed - housing unchanged
Mental health crisis flag        | #5233     | Within 7 days               | 5 days    | On time

Monthly summary: 5 triggers, 1 overdue (20%). Overdue case directly
linked to a subsequent use-of-force incident — reinforces the case for
an automated alert system rather than manual tracking, per after-action
review action item #1 above.
```
