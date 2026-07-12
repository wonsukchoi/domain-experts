# Security Supervisor Playbook

Filled examples for the three recurring artifacts: shift briefing, staffing-gap decision, and incident/use-of-force report. Populate with the site's real numbers; the structure and thresholds below are the parts that don't change.

## Shift briefing (start-of-shift, 5–8 minutes, standing)

```
SHIFT BRIEFING — Site: Meridian Tower           Date: 2026-07-12   Shift: 2300–0700

1. LAST SHIFT (what happened)
   - 1 access-control override (tenant lockout, Suite 410) — logged, no incident.
   - Pass-down note: elevator 3 intermittent door-sensor fault, facilities ticket #4471 open.

2. TODAY (what's different)
   - Freight elevator out of service 0600–1400 for maintenance — reroute deliveries to loading dock B.
   - Post 2 (garage) covered by roaming officer only tonight (Post 2 primary on approved leave) —
     checkpoint interval tightened to 20 min, 2300–0300.

3. KNOWN RISK (what to watch)
   - Garage: 2 prior attempted break-ins, both 0015–0140, trailing 14 months — extra checkpoint
     pass through Level 2 required, log timestamp each pass.
   - Lobby: tenant reported suspicious loitering near south entrance 3 nights ago — no incident,
     flag if repeated.

4. ASSIGNMENTS
   - Officer A: Post 1 (lobby/access control), fixed.
   - Officer B: Post 2 (garage), roaming, 20-min checkpoints via GPS tour system.
   - Supervisor: mobile, callout coverage active 2300–0700, phone [xxx-xxx-xxxx].

Briefed by: _________  Acknowledged (signature, each officer): _________  _________
```

Rule: a briefing with nothing in section 3 is a missed handoff, not a quiet night — pull the trailing incident log before writing "none."

## Staffing-gap decision (callout / no-show)

Decision order, in priority:

| Option | Response time | Cost multiplier vs. base rate | Use when |
|---|---|---|---|
| 1. Cross-trained officer from nearest site (within contract's response window, typically ≤45 min) | Fast | 1.0x (no premium) | Default first move — check the cross-site roster before anything else |
| 2. On-call/flex-pool officer | Moderate (30–90 min) | 1.0–1.25x depending on contract flex-pool terms | Cross-site pool unavailable or contract bars pooling |
| 3. Overtime — current-shift officer holds over | Immediate | 1.5x | Gap is under 4 hours and no pool/flex option exists |
| 4. Overtime — off-shift officer called in | 30–60 min | 1.5x + response delay | Gap exceeds 4 hours, no pool option |
| 5. Temporary post reduction with documented substitute control | Immediate | Cost saved, not spent | Only after site risk window and prior-incident count are checked (see red-flags.md) — never the first move |

Log every gap-fill decision with: gap start/end time, option chosen, cost, and who approved it. Two or more overtime fills (options 3–4) in a rolling 2-week window at the same post triggers escalation to recruiting/headcount, not another overtime approval.

## Incident / use-of-force report structure

```
INCIDENT REPORT #____        Site: __________   Date/Time: __________
Reporting officer: __________   Post: __________

1. NARRATIVE (chronological, first person, no conclusions)
   - What was observed/reported, in order, with timestamps to the minute.

2. SUBJECT(S) INVOLVED
   - Description, statements made, injuries (subject and officer).

3. FORCE USED (if any)
   - Level of resistance offered by subject (none / passive / active / assaultive / deadly).
   - Level of force applied by officer, using the 5-step continuum
     (presence / verbal / soft empty-hand / intermediate weapon / deadly force).
   - Reconciliation: force level must be within one step of resistance level, or this
     report is flagged for supervisor use-of-force review before filing, regardless of outcome.

4. WITNESSES
   - Name, contact, independent statement attached (not paraphrased by reporting officer).

5. EVIDENCE
   - Camera footage timestamp range pulled, physical evidence collected, chain-of-custody log
     started if evidence retained.

6. NOTIFICATIONS
   - Law enforcement (yes/no, time, case #), EMS (yes/no), client contact (yes/no, time), supervisor
     (time notified — must be within the shift, not next business day).

7. SUPERVISOR REVIEW
   - Force-level reconciliation confirmed: Y/N
   - Post order compliance confirmed: Y/N
   - Prior similar incident count (trailing 12–24 mo) at this location: ___
   - Follow-up action (retraining / policy update / client notification / none): __________

Reviewed by: __________   Date: __________
```

## Client cost-reduction request — decision checklist

Before agreeing to any post cut or downgrade:

1. Pull prior-similar-incident count for the site, trailing 12–24 months.
2. Cross-reference incident timestamps against the proposed coverage gap — does the gap include the risk window?
3. If two or more similar incidents fall inside the proposed gap window, do not agree to a straight cut — propose a substitute control (roaming coverage, camera/LPR, access hardening) sized to the actual window, and quote both options with hours and dollar figures.
4. Put the recommendation and the incident count in writing to the client before implementing any change — verbal agreement to a coverage reduction is not a defensible record.
5. If the client proceeds against the recommendation, document that in writing and retain a copy — this is the branch's own liability record, not just the client's decision.
