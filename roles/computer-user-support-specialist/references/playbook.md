# Computer User Support Specialist — Playbook

## 1. Incident / service-request / problem classification (decision tree, filled)

| Question | Yes → | No → |
|---|---|---|
| Is something broken that worked before? | Go to **Incident** branch | Go to next question |
| Is it a planned, no-fault ask (new access, new hardware, a reset)? | Go to **Service Request** branch | Go to **Problem** branch |
| (Incident/Service Request branch) Has the same symptom recurred ≥3 times in 30 days across ≥2 users? | Also open a linked **Problem** record | Close as single incident/request when resolved |

**Worked classification examples:**

| Ticket text | Classification | Reasoning |
|---|---|---|
| "My laptop won't connect to Wi-Fi since this morning" | Incident | Something that worked yesterday doesn't work today — no planned change requested |
| "Need VPN access for our new hire starting Monday" | Service Request | Planned, no-fault, has a lead time |
| "3rd password reset this month for the same shared kiosk login" | Service Request **+ linked Problem** | Individual reset is a request; the recurrence (3rd in 30 days, 1 user) triggers the problem-record threshold |
| "Printer on 4th floor jams on every print job >10 pages, reported by 6 different people this week" | Incident **+ linked Problem** | ≥2 users, recurring pattern — closing each jam ticket without a problem record leaves root cause (worn roller, needs replacement part) untouched |

**Rule applied:** the ≥3-in-30-days / ≥2-users threshold is what converts a string of individually-resolved tickets into a mandatory linked problem record. Below that threshold, log the pattern-watch note on the ticket but don't open a problem record yet — noise ratio.

## 2. ITIL impact × urgency priority matrix (SLA bands, filled)

| Impact ↓ / Urgency → | High (business-stopping) | Medium (workaround exists) | Low (cosmetic/no workaround needed) |
|---|---|---|---|
| **High** (site/dept-wide, ≥25 users or revenue-generating system) | **P1** — ack 10–15 min, resolve 4 hrs, escalate at 30 min if unacknowledged-diagnosis | P2 — ack 15 min–1 hr, resolve 4–8 hrs | P3 — ack ≤1 hr, resolve ≤2 business days |
| **Medium** (team/segment, 5–24 users) | P2 — ack 15 min–1 hr, resolve 4–8 hrs, escalate ~5th hr | P2 — ack 15 min–1 hr, resolve 4–8 hrs | P3 — ack ≤1 hr, resolve ≤2 business days |
| **Low** (single user, 1 device) | P3 — ack ≤1 hr, resolve ≤2 business days | P3 — ack ≤1 hr, resolve ≤2 business days | P4 — ack ≤4 business hrs, resolve ≤5 business days (backlog) |

**Worked example:** "Company-wide email outage, sales team can't send quotes before EOD deadline" → Impact = High (all users), Urgency = High (revenue deadline same day) → **P1**. Ack clock starts at ticket creation, target 10–15 min; if root cause isn't diagnosed by minute 30, auto-escalate to on-call lead regardless of how close resolution feels — the escalate trigger is a clock, not a judgment call made mid-diagnosis.

**Rule applied:** tier is set by impact × urgency before diagnosis starts, not adjusted mid-ticket because the fix turned out to be easy or hard. A P1 that gets fixed in 8 minutes is still logged and closed as a P1 — the priority described the situation at intake, not the eventual difficulty.

## 3. Identity verification gate (decision table, filled)

| Request type | Verification required? | Channel |
|---|---|---|
| Password/MFA reset | Yes — always | Callback to number on file in HR system, or video call with badge visible — never the inbound channel the request arrived on |
| Remote-control session ("let me take control of your screen") | Yes — always, plus manager confirmation if request cites urgency ("I'll lose my job if this isn't fixed now") | Callback to number on file |
| Account-state change (unlock, disable, permission grant) | Yes — always | Callback to number on file, or in-person badge check |
| "What's my printer's IP" / read-only info request | No | N/A — low-risk, no account-state change |
| New-hardware service request already tied to an approved ticket/PO | No (identity already established at ticket creation via manager approval) | N/A |

**Worked example:** Caller states name and employee ID, asks for an MFA reset, says "I'm in the middle of a client call and need this in the next 2 minutes." Correct action: put the reset on hold, call the employee's number from the HR directory (not a number the caller supplies), confirm the request verbally. If the callback doesn't answer within 5 minutes, the ticket stays open and unresolved — the clock pressure from the caller does not override the gate. This is the exact shape of the MGM Resorts pretext-call failure (10-minute call, no independent-channel check, credential reset → breach).

## 4. CompTIA six-step troubleshooting sequence, with domain-specific stop conditions (filled)

**Scenario:** Ticket — "Can't print to the 3rd floor color printer, worked fine yesterday."

| Step | Action | Stop condition (move to next step only if this fails) |
|---|---|---|
| 1. Identify the problem | Ask: what changed, when, error message text, one user or many | If 1 user only + no error message + printer works for others → proceed to step 2 with hypothesis "client-side" |
| 2. Establish theory of probable cause (start with the obvious) | Theory order: (a) printer offline/out of paper/toner, (b) print queue stuck, (c) network path to printer, (d) driver corruption | Check (a) first — physically/remotely confirm printer status — before touching drivers |
| 3. Test the theory | Ping printer IP, check print queue for stuck jobs, check printer's own display panel | If printer pings and queue is empty → theory (a)/(b) ruled out, move to (c)/(d) |
| 4. Plan and implement | If driver corruption confirmed (other printers also fail from same machine): remove and reinstall driver | Implement only the fix matching the confirmed cause — do not reinstall OS or replace hardware on a first pass |
| 5. Verify full functionality | Print a real test page from the actual application the user needed (not just a Windows test page), confirm color output correct | If test page prints from Notepad but not from the user's actual app → not verified, return to step 2 with narrowed theory ("app-specific print driver setting") |
| 6. Document | Root cause: driver corruption on client machine. Action: driver removed/reinstalled. Ruled out: printer hardware, network path, queue. Outcome: verified via actual invoice template print | — |

**Ruled-out list (carried into any escalation):** printer online and reachable (ping successful, 4/4 replies); print queue empty; other users printing successfully to same device; issue isolated to one client machine — hands tier 2 a list that saves them from re-running steps 1–3 from zero.

## 5. Ticket resolution note — filled template

> **Resolution — [one-line symptom] (Ticket #[id], P[tier])**
> Classification: [Incident / Service Request / Problem-linked].
> Root cause: [confirmed cause, not the reported symptom].
> Ruled out: [specific checks performed, with results — not "checked network," but "pinged printer IP, 4/4 replies"].
> Identity verification: [channel used, or "not required — read-only request"].
> Fix applied: [exact change, exact values].
> Verified: [functional check against the original report — what was actually re-tested].
> Escalated to: [team, with ruled-out list attached] or **Resolved at tier 1**.

**Worked example (filled):**
> **Resolution — Can't print to 3rd floor color printer (Ticket #48213, P3)**
> Classification: Incident.
> Root cause: corrupted print driver on client machine (not printer hardware or network).
> Ruled out: printer online (ping 4/4), queue empty, 3 other users printing successfully to same device.
> Identity verification: not required — no account-state change.
> Fix applied: removed and reinstalled HP Universal Print Driver v7.2 on client machine.
> Verified: printed actual invoice template from Excel with correct color output, not just a Windows test page.
> Escalated to: N/A — resolved at tier 1.
