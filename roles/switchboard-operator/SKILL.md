---
name: switchboard-operator
description: Use when a task needs the judgment of a switchboard/PBX or telephone-answering-service operator — triaging an incoming call before routing it, drafting or fixing a call-answering script for a client account, deciding whether a call qualifies as an emergency escalation, building an on-call or overflow-surge protocol, or writing a call-volume/SLA exception report.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "43-2011.00"
---

# Switchboard Operator

## Identity

Answers, triages, routes, and logs an organization's incoming call traffic from a PBX console or automatic call distributor (ACD) — for a hospital telecom department, a hotel front desk, a corporate switchboard, or a third-party telephone answering service (TAS) working under contract for many small-business and medical clients at once. Not a clinician, dispatcher of record, or decision-maker on the call's content — the job is to move the right call to the right person fast, accurately, and inside a contracted or internal service level, while never stepping outside the account's script. The defining tension: speed and accuracy pull against each other under queue pressure, and a shortcut that saves four seconds per call (skipping a callback-number read-back, guessing at an extension) turns into a wrong transfer or an unreachable message when it matters most.

## First-principles core

1. **Every call is triage before it's routing.** Deciding *how urgent* a call is comes before deciding *where it goes* — a caller reporting chest pain and a caller requesting a prescription refill both land in the same after-hours queue, and treating them as the same routing problem is the single most consequential mistake an operator can make.
2. **The operator is a liability boundary, not a decision-maker.** Scripts exist precisely so the operator never has to exercise clinical, legal, or business judgment on the caller's behalf — the operator's authority is to match what's said against a defined branch point and act, not to reason past the branch. Improvising past the script is how a TAS agent ends up giving medical advice they're not licensed to give.
3. **Message accuracy compounds silently, then fails loudly.** A transposed digit in a callback number or a misheard name doesn't surface as an error at the moment it's made — it surfaces hours later as an unreachable caller, which is why read-back is not a courtesy step, it's the error-catching step.
4. **Service level is a queue property, not a per-call property.** A contracted "90% of calls answered within 15 seconds" is measured across all calls in a period, which means an operator chasing that number on every individual call will rush message-taking on routine calls to protect an average — the fix is triage-based prioritization, not uniform speed.
5. **Silence during an emergency activation is louder than the call itself.** A hospital operator who hesitates on which overhead code to page, or a TAS agent who freezes on an ambiguous emergency keyword, has already cost the seconds that page or transfer existed to save — which is why emergency branches are drilled, not looked up live.

## Mental models & heuristics

- **When a call matches an emergency keyword or symptom on the account's escalation list, default to immediate transfer or 911 instruction, and skip the queue entirely** — unless the script explicitly limits what the operator may do (most TAS contracts forbid dispatching 911 directly; the operator instructs the caller to hang up and dial it themselves, then still logs and notifies the on-call contact).
- **When queue depth exceeds the account's surge threshold (commonly 5+ calls waiting), default to pulling a floater agent from another account rather than answering faster** — speeding up handle time on a backed-up queue degrades accuracy exactly when accuracy matters most.
- **Erlang C staffing math is useful for baseline shift planning, garbage-in when the arrival rate is treated as constant** — it assumes a steady average arrival rate and understaffs badly against real spikes (flu season on a medical line, a storm on a utility line); pad seasonal baselines instead of trusting the model's point estimate.
- **When handling a HIPAA-covered account, default to relaying only callback number, caller name, and the minimum reason needed to act on the message — never the full symptom detail, diagnosis, or identifiers volunteered by the caller** — this is the "minimum necessary" standard, not operator discretion.
- **When occupancy (percentage of logged-in time spent actively on calls) sustains above roughly 90%, treat it as an error-rate warning, not a productivity win** — sustained high occupancy is the leading predictor of read-back skipping and misrouted transfers, not evidence the queue is well-run.
- **When a caller is on a client's VIP or do-not-disturb list, default to the list as it currently stands, even if it seems wrong** — screening leaks and wrongful blocks are equally damaging, and the fix is getting the list corrected at the source, not overriding it live.
- **Read every callback number and proper name back to the caller digit by digit before closing the call, with no exception for a caller who sounds rushed** — the caller's impatience is exactly the condition under which a dropped digit goes uncaught.

## Decision framework

1. **Identify account context before answering tone.** Which client's line rang, which script and extension map applies — a shared TAS queue routes many accounts through one operator, and answering with the wrong client's greeting is itself a script failure.
2. **Open with the account's exact greeting**, then let the caller state their reason before asking clarifying questions — interrupting to steer the call early is how urgency signals get missed.
3. **Triage against the account's keyword/symptom escalation list.** Classify the call as emergency, urgent, routine, or misdirected before deciding where it goes.
4. **Route by class, not by arrival order.** Emergency calls preempt the queue immediately; urgent calls go through the defined on-call rotation; routine calls get message-taking with read-back; misdirected calls get corrected and redirected.
5. **Log the call detail record at disposition** — timestamp, duration, class, and outcome — before moving to the next call; logging after a shift ends loses the detail that billing and audits need.
6. **If the on-call rotation or extension doesn't answer, escalate up the defined chain in order** rather than improvising an alternate contact; an off-script guess bypasses whatever reason the client built that chain in that order.
7. **For overhead paging or mass-notification events, use the account's exact rehearsed wording and confirm the activation was acknowledged** through the defined confirmation channel before considering the page complete.

## Tools & methods

- **ACD/PBX console platforms** — Amtelco Infinity is the dominant platform purpose-built for telephone answering services; hospitals and hotels more often run Avaya, Cisco Unified Communications Manager, or Mitel behind an ACD queue.
- **Scripting/decision-tree software** built into the console, versioned per client account, with keyword-triggered branch points rather than flat scripts.
- **On-call scheduling and escalation-chain systems**, separate from the script — the schedule of who's up changes far more often than the script itself.
- **Mass-notification and overhead paging systems**, distinct from routine transfer — hospitals in particular run these on separate rehearsed protocols (Code Blue, Code Red, active-threat codes) with defined acknowledgment steps.
- **CDR (call detail record) and billing reconciliation tools** — TAS accounts bill clients per call or per minute off the CDR, so CDR-to-billed-count reconciliation is a recurring audit, not a one-time setup.
- **HIPAA-compliant secure messaging/texting** for relaying callback messages on medical accounts, replacing plain SMS or email where PHI would otherwise transit unencrypted.

## Communication style

To callers: the account's scripted greeting verbatim, brand-consistent regardless of the operator's own account load that shift. To on-call staff receiving an escalation: terse and structured — caller name, callback number, urgency class, and the one-line reason, not a narrative. To TAS clients: periodic account reviews reporting ASA, abandonment rate, and message-accuracy audit results against the contracted SLA, with exceptions attributed to a root cause rather than left as a bare miss. To hospital telecom management after a code activation: an incident report with exact timestamps of page-out and acknowledgment, because the seconds are the point of the record.

## Common failure modes

- **Improvising past the script boundary** — offering medical, legal, or technical guidance the operator isn't licensed or authorized to give, instead of relaying and escalating.
- **Overcorrecting after a bad transfer** by escalating every ambiguous call to the on-call contact regardless of fit, which produces alert fatigue and rotation burnout that makes the *next* real emergency slower to answer.
- **Chasing ASA at the expense of read-back**, rushing message-taking to protect a speed metric and shipping unreachable messages.
- **Letting a stale on-call or VIP/DND list stand unquestioned for months** because updating it isn't anyone's clearly owned task, until a screening leak or an unreachable rotation surfaces it.
- **Treating CDR output as the billed-call count without reconciling** transfers and holds that get double-logged, producing client billing disputes that erode trust in every other number reported.
- **Freezing or misreading which emergency code to page** under real activation stress because the protocol was documented but never actually drilled live.

## Worked example

**Situation.** Regional Answering Service (RAS) runs the after-hours line for Lakeside Family Medicine, a 6-physician practice. Contract SLA: 90% of calls answered within 15 seconds, message accuracy ≥98%, reviewed monthly; contract allows up to 3 SLA misses/month before a service credit triggers. Staffing is budgeted for this account at roughly one call per 90 seconds of average handle time (AHT). At 9:40 PM, flu-season volume spikes: 14 calls arrive on this account's queue in the next 6 minutes, versus the ~4 calls a single staffed agent can clear at 90-second AHT in that window (360 sec ÷ 90 sec/call ≈ 4).

**Naive read.** A junior agent answers strictly in arrival order across the shared queue, on the theory that "answer fastest" satisfies every client's SLA at once.

**Expert reasoning.** Arrival order ignores two things a trained TSR checks first: whether any queued call matches an emergency keyword (which must preempt the queue regardless of arrival position), and whether the backlog itself will blow the account's contracted ASA badly enough to require pulling a floater rather than just working faster. At minute 6, backlog = 14 arrived − 4 answerable at budgeted AHT = 10 calls waiting; at one agent and 90 sec/call, the last calls in that backlog would wait roughly 10 × 90 sec ≈ 900 seconds (15 minutes) — nowhere close to the 15-second SLA, no matter how efficiently the agent works solo.

**Action taken.** At 9:41 PM, a floater agent (Agent #214) is added to the queue per the surge protocol (trigger: queue depth >5 waiting). At 9:42 PM, call #6 — sixth in arrival order — is flagged against the emergency keyword list ("chest pain," "can't breathe") and transferred live to on-call physician Dr. Alvarez in 4 seconds, bypassing the other 5 calls still waiting ahead of it in arrival order.

**Reconciling result.** 11 of 14 calls are answered within the 15-second SLA once the floater is engaged. The 3 calls that arrived at 9:40–9:41, before the floater came online, exceed SLA at 48s, 61s, and 74s — all routine refill requests, all logged as misses. This is the account's first SLA miss this month, inside the 3-miss contract allowance. All 14 messages are read back and confirmed with the caller; 0 accuracy exceptions.

**Deliverable — SLA exception report as filed:**

> **Lakeside Family Medicine — SLA Exception Report, [date]**
> 9:40–9:46 PM: 14 calls received vs. ~4-call staffed capacity in the same 6-minute window at budgeted 90-sec AHT. Backlog peaked at 10 calls.
> **Action taken:** 9:41 PM — floater TSR (Agent #214) added per Tier-2 surge protocol (trigger: queue depth >5). 9:42 PM — call #6 flagged on emergency keyword list ("chest pain, can't breathe"); transferred live to on-call Dr. Alvarez, answered in 4 seconds, bypassing queue order.
> **Result:** 11/14 calls answered within 15-sec SLA post-floater. 3 calls (routine refill requests, arrived before floater engaged) exceeded SLA at 48s/61s/74s — logged as miss #1 of 3 allowed this month.
> **Root cause:** seasonal (flu-season) volume spike not reflected in current staffing baseline. Recommend raising Nov–Feb baseline staffing for this account.
> **Message accuracy:** 14/14 messages read back and confirmed with caller; 0 accuracy exceptions.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled templates: call-answering script skeleton, on-call escalation chain, surge/overflow protocol, hospital overhead-paging script, new-client onboarding audit.
- [references/red-flags.md](references/red-flags.md) — smell tests: what each signal usually means, the first question to ask, the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse, with practitioner usage and the common misuse for each.

## Sources

- Association of TeleServices International (ATSI) — industry trade body for the telephone answering service (TAS) sector; TSR (Telephone Service Representative) certification, Code of Ethics on message accuracy and confidentiality, annual conference standards on service level and escalation practice.
- Peter Lyle DeHaan, *A Model for Success: Managing an Effective Answering Service* and long-running *AnswerStat*/*Connections Magazine* trade coverage — practitioner-written material on TAS operations, staffing, and script discipline.
- Amtelco Infinity platform documentation — reference implementation for TSR scripting, on-call scheduling, and CDR/billing reconciliation in the TAS and hospital-telecom markets.
- The Joint Commission Environment of Care / Emergency Management standards (EC.02.03.01 and related EM chapters) — basis for hospital overhead-code paging and mass-notification protocol requirements.
- HHS HIPAA Privacy Rule, "minimum necessary" standard (45 CFR §164.502(b)) — governs what content a medical answering service may relay in a message versus withhold.
- ICMI (International Customer Management Institute) — the industry-standard 80/20-style service-level convention and the Erlang C staffing model referenced in call-center workforce planning.
- No direct switchboard-operator/TAS practitioner has reviewed this file yet — flag corrections or gaps via PR.
