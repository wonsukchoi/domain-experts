# Playbook — shift triage, scoring, and escalation

Filled processes, not descriptions. Use the NEWS2 table to score, the triage sequence to order the round, and the SBAR templates to escalate.

## 1. Shift-start triage (first 15–20 minutes)

For each of the 5–6 patients on the assignment, pull three data points before touching a med cart: last documented vitals, time since last full assessment, and stated acuity driver (post-op day, new admission, telemetry alarm history, confusion risk). Rank into three tiers:

| Tier | Criteria | Round order |
|---|---|---|
| See first | Unstable trend on handoff, telemetry alert overnight, <24h post-op with an active drain/PCA, any NEWS2 ≥3 at last check | Within first 20 min |
| See second | Stable but due for a time-critical medication (insulin, IV antibiotic, anticoagulant) in the next hour | Before the drug is due, not after |
| See last | Stable, routine schedule, no overnight events | Anytime before their next scheduled med |

Reassess this ranking after every unscheduled event — a "see last" patient who trends abnormal moves to "see first" immediately, and the rest of the round waits.

## 2. NEWS2 quick-reference scoring table

| Parameter | 3 | 2 | 1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| Resp. rate (/min) | ≤8 | | 9–11 | 12–20 | | 21–24 | ≥25 |
| SpO2 % (room air) | ≤91 | 92–93 | 94–95 | ≥96 | | | |
| Air or oxygen | | | | air | O2 (+2) | | |
| Systolic BP | ≤90 | 91–100 | 101–110 | 111–219 | | | ≥220 |
| Pulse (/min) | ≤40 | | 41–50 | 51–90 | 91–110 | 111–130 | ≥131 |
| Consciousness | | | | alert | | | new confusion/CVPU |
| Temp °C | ≤35.0 | | 35.1–36.0 | 36.1–38.0 | 38.1–39.0 | ≥39.1 | |

**Aggregate interpretation:**
- 0–4: routine monitoring, standard frequency.
- 5–6, OR any single parameter = 3: urgent review — reassess within the hour and notify the covering physician/RRT criteria owner.
- ≥7: emergent — continuous monitoring, immediate physician/critical-care review, consider RRT.

**Rule that gets missed:** the single-parameter override fires independent of the total. A patient with RR 26 (3) and every other parameter at 0 has an aggregate of 3 — "low risk" by total — but still meets urgent-review criteria on the RR alone.

## 3. Reassessment cadence by trigger

| Trigger | New cadence |
|---|---|
| Baseline / no concerns | Per unit standard (commonly q4h med-surg, continuous telemetry) |
| NEWS2 rose ≥2 points since last check, still <5 | Recheck in 30 min, not next scheduled interval |
| NEWS2 5–6 or single parameter = 3 | Recheck in 15 min, notify physician |
| NEWS2 ≥7 | Continuous vitals (q5min) until stabilized, RRT/physician at bedside |
| Post-intervention (O2 started, fluid bolus given, RRT left) | Recheck at the specific interval the intervention protocol specifies before returning to standard cadence |

## 4. SBAR templates by urgency

**Non-urgent update (FYI, no action needed right now):**
> "Dr. [Name], this is [RN] on [unit] with an update on [patient], room [#]. Background: [one line]. She's [assessment finding], which I wanted to flag — no action needed right now, just wanted you aware before rounds."

**Urgent (needs a decision this call):**
> "Dr. [Name], this is [RN] on [unit], calling about [patient], room [#]. I need [specific ask — order, medication change, bedside visit within X minutes]. Background: [one line]. She's now [assessment: vitals, NEWS2 score, new findings]. My concern is [named differential/risk]. What would you like me to do?"

**Emergent (rapid response / immediate bedside):**
> "Dr. [Name], this is [RN] on [unit], [patient] in room [#] — she's acutely worse in the last [X] minutes and I need you at bedside now, or I'm calling a rapid response. Background: [one line]. Assessment: [vitals, NEWS2 score]. I'm concerned about [named risk]. I've already [interventions started]. Which do you want — you at bedside, or RRT?"

Always end with a specific ask, and always state the time of the call in the chart entry immediately after.

## 5. Delegation checklist (NCSBN five rights)

Before handing a task to a CNA/tech, confirm all five, out loud if needed:

1. **Right task** — is this within the delegate's role (routine vitals, ADLs, blood glucose) and not an assessment/interpretation task?
2. **Right circumstance** — is this specific patient stable enough that the task doesn't require clinical judgment mid-task? (An early post-op telemetry patient trending abnormal is the wrong circumstance for delegated vitals alone.)
3. **Right person** — does this delegate have the competency and current training for this specific task (e.g., glucometer certification)?
4. **Right direction/communication** — did you state the specific abnormal-value threshold that requires an immediate callback, not "let me know if anything changes"?
5. **Right supervision/evaluation** — will you personally review the delegated result and decide on action, rather than treating "reported normal" as closing the loop?

If any of the five is uncertain, keep the task yourself or pair it with a shorter personal recheck interval.

## 6. Post-event documentation sequence

After any escalation or rapid response: (1) timestamped vital-sign trend from baseline through the event, (2) the SBAR call time and who was called, (3) interventions given with times, (4) response to intervention, (5) reassignment note for the rest of the shift (who covered the other patients and for how long). This sequence — not a narrative paragraph — is what a chart review or root-cause analysis reads first.
