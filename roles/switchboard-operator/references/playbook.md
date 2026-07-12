# Playbook

Filled operational templates a switchboard/TAS operator actually runs — adapt the numbers to the account, keep the structure.

## 1. Call-answering script skeleton (filled — medical after-hours account)

```
ACCOUNT: Lakeside Family Medicine (after-hours line)
GREETING (verbatim): "Lakeside Family Medicine after-hours service,
  this is [agent], how can I help you?"

BRANCH 1 — Emergency keyword match
  Triggers: "chest pain," "can't breathe," "severe bleeding,"
    "unresponsive," "overdose," "suicidal"
  Action: "I'm connecting you to the doctor on call right now — if
    you feel this is life-threatening, please hang up and dial 911."
    Transfer immediately to on-call rotation. Do NOT queue this call.
    Log as EMERGENCY, notify on-call contact by page + text simultaneously.

BRANCH 2 — Urgent, non-emergency
  Triggers: "high fever," "medication reaction," "post-surgical
    concern," caller explicitly asks for the doctor tonight
  Action: Take name, DOB, callback number, one-line reason. Read back
    callback number. Page on-call physician within 10 minutes per
    contract. Log as URGENT.

BRANCH 3 — Routine
  Triggers: refill requests, appointment questions, billing questions
  Action: Take name, callback number, one-line reason. Read back
    callback number. Log as ROUTINE — delivered to office at 8 AM open.
    Do NOT page on-call for routine items.

BRANCH 4 — Caller volunteers full medical detail unprompted
  Action: Log only name, callback number, and the one-line reason
    category (e.g., "medication question") — HIPAA minimum-necessary
    standard. Do not transcribe symptom detail, diagnosis, or SSN into
    the message even if the caller states it.

CLOSE (verbatim): "I have you down as [read back]. The doctor's office
  will follow up. Is there anything else?"
```

**Rule:** any keyword not on the current escalation list that sounds like it should be gets flagged to the account supervisor same-shift, not silently treated as routine — the list is reviewed monthly, not written once.

## 2. On-call escalation chain (filled example, timed)

```
PRIMARY:   Dr. Alvarez (cell) — page + call, wait 4 min for callback
SECONDARY: Dr. Chen (cell) — if no response from primary by minute 4
TERTIARY:  Answering-service supervisor — if no response from
           secondary by minute 8; supervisor calls practice manager's
           emergency line directly
FALLBACK:  If no contact reached by minute 12 on an URGENT or higher
           call, instruct caller: "I haven't been able to reach the
           on-call physician — if this is worsening, please go to
           the nearest emergency room or dial 911." Log as ESCALATION
           FAILURE, notify account manager same-shift, not next
           business day.
```

Escalation chain order and timing come from the client contract, not agent judgment — a chain that seems slow gets raised with the account, never skipped live.

## 3. Surge / overflow protocol (filled thresholds)

| Signal | Threshold | Action |
|---|---|---|
| Queue depth, single account | >5 calls waiting | Pull 1 floater agent from lowest-priority active account |
| Queue depth, single account | >10 calls waiting | Pull 2nd floater; page shift supervisor |
| ASA trailing 15 min | >2x contracted target | Trigger surge review regardless of raw queue depth |
| Abandonment rate, trailing hour | >5% | Trigger surge review; check for outage/spike vs. normal pattern |

Floater reassignment always follows account priority tier (contracted SLA tightness), never "whichever queue looks worst" — pulling a floater off a Tier-1 (15-sec SLA) account to rescue a Tier-3 (60-sec SLA) account breaches the tighter contract to fix the looser one.

## 4. Hospital overhead-paging script (filled — Code Blue)

```
TRIGGER: Nursing station reports patient in cardiac/respiratory arrest.
ACTION:
  1. Confirm exact location (building, floor, room/bed) verbally with
     caller before paging — a page with the wrong location wastes the
     response team's minute one.
  2. Page overhead, exact wording, three times at ~10-second intervals:
     "Code Blue, [building] [floor], room [number]. Code Blue,
     [building] [floor], room [number]."
  3. Simultaneously trigger mass-notification system (pager/text) to
     the code team roster — overhead paging alone does not satisfy
     the hospital's emergency-notification requirement.
  4. Log activation time to the second. Log first acknowledgment
     receipt time to the second.
  5. Do not clear the page or reuse the console for routine calls
     until "Code Blue clear" is called by the responding team.
```

Different facilities assign different code words to different emergencies (Code Red = fire at one hospital, security threat at another) — an operator moving between facilities re-drills the local code sheet before taking a live console, never assumes the prior facility's codes carry over.

## 5. New-client onboarding audit (filled checklist)

```
CLIENT: [name]                    GO-LIVE DATE: [date]
[ ] Script built and reviewed with client for all 4 standard branches
    (emergency / urgent / routine / off-script)
[ ] Emergency keyword list confirmed by client, not assumed generic
[ ] On-call escalation chain confirmed with named contacts + numbers,
    tested with a live callback before go-live
[ ] VIP/DND list (if any) loaded and confirmed
[ ] 10 test calls placed against the script by a second agent,
    covering all 4 branches — go-live blocked until 10/10 pass
[ ] Billing/CDR field mapping confirmed against client's expected
    invoice format
[ ] Client sign-off on SLA tier and reporting cadence
```

The two steps most often skipped under launch-date pressure: the live callback test on the escalation chain (a chain that "looks right" on paper with a disconnected cell number fails on the first real emergency call), and the 10-call script audit before go-live rather than after the first client complaint.
