# Community Health Worker — Playbook

## SDOH screening sequence (filled example)

| Domain | Screening question (PRAPARE-style) | Client response | Flagged? |
|---|---|---|---|
| Housing | "What is your housing situation today?" | "Staying with my sister temporarily" | Yes — instability |
| Food | "In the past 12 months, did you worry your food would run out?" | "Often true" | Yes |
| Transportation | "Has lack of transportation kept you from appointments?" | "Yes, no car, bus route changed" | Yes |
| Utilities | "In the past 12 months, has the gas/electric company threatened to shut off services?" | "No" | No |
| Safety | "Do you feel safe where you currently live?" | "Yes" | No |
| Employment | "Are you currently employed?" | "Yes, part-time, no set schedule" | Context flag — affects outreach timing |

**Ranking pass (ask the client, don't assume):** client names transportation as most urgent ("I keep missing my baby's checkups because of the bus"), housing second, food third. Address in that order even though housing instability is the clinically higher-severity flag.

## Closed-loop referral tracking log (filled example)

| Client ID | Domain | Referral made (date) | Contact confirmed scheduled? | Appointment date | Attendance confirmed? | Notes |
|---|---|---|---|---|---|---|
| 1042 | Transportation | 3/3 | Yes (3/5) | 3/12 | Yes (3/13 call) | Used voucher, attended |
| 1042 | Housing | 3/3 | Yes (3/6) | 3/20 | No — pending | Follow-up call scheduled 3/21 |
| 1058 | Food | 3/4 | No — 3 attempts, no answer | — | — | Switching to evening outreach attempt |
| 1071 | Transportation | 3/5 | Yes (3/5) | 3/15 | No — no-show | Called; bus route changed again, escalating to case conference |

**Rule:** a row only moves to "complete" once attendance is confirmed, not once the referral is made. A referral with no attendance-confirmation column filled in after 14 days triggers the warm-handoff-recheck heuristic.

## Home-visit sequence (filled example)

1. **Pre-visit:** confirm address and safety context with referring source; bring screening tool, resource list, and interpreter line info if needed.
2. **Opening (2-3 min):** state purpose in plain language — "I'm here to see how things are going and if there's anything getting in the way of your appointments."
3. **Screening (10-15 min):** run full SDOH tool even if client leads with one issue.
4. **Ranking (2 min):** confirm out loud which flagged domain the client wants addressed first.
5. **Teach-back check (5-10 min, if a clinical instruction is in play):** ask client to demonstrate or restate the instruction in their own words; if the restatement misses a key step, re-explain using a different anchor (their routine, not the clinical rationale) and re-check.
6. **Close (2-3 min):** confirm next contact date, tied to the referral's first appointment date, not a generic "check in next week."
7. **Post-visit (same day):** log all screening results, referrals made, and the confirmed next-contact date in the tracking system — same-day documentation catches gaps a next-week write-up misses.

## Teach-back verification — before/after example

**Clinical instruction as given:** "Take your metformin twice daily with meals and check for signs of low blood sugar."

**Naive restatement check:** "Does that make sense?" — client says yes. No information gained.

**Teach-back check:** "Can you walk me through what your morning will look like tomorrow with this medicine?" Client responds: "I take one in the morning before I eat, since I don't usually eat till lunch." Gap identified: client is taking the dose before food, not with it, and has only one meal window, meaning the "twice daily with meals" instruction doesn't fit their actual eating pattern.

**Reconciled plan communicated back to the referring provider:** "Client's daily eating pattern is one meal (lunch) plus snacks — recommend provider re-evaluate twice-daily-with-meals dosing against actual intake pattern rather than assuming two meals."
