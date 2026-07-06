# Vocabulary

Load when a term is being used loosely in a handoff or a writeup. Each entry is a term generalists routinely substitute for something adjacent but not identical — the misuse, not the dictionary definition, is the point.

**Incident**
An unplanned interruption to a service, or a reduction in its quality, versus its agreed-upon normal operating state.
*In use:* "Opened as an incident — company VPN is down for the whole Denver office, that's a P1."
*Misuse:* Generalists use "incident" for anything that generates a ticket, including a new-hire laptop request. If nothing was working before and now isn't, it's an incident; if nothing was broken and someone wants something provisioned, it's a service request — conflating the two sends both down the wrong SLA clock and corrupts the metrics both are measured on.

**Service request**
A planned, no-fault ask for something standard and pre-approved — access, hardware, software install — that isn't a break of anything.
*In use:* "New monitor for the account team, that's a service request, not an incident — routes to fulfillment, not troubleshooting."
*Misuse:* Logged as an "incident" because the intake form only has one ticket type, or because "the user needs this urgently" gets translated into incident severity language. A request with zero broken component has no fault to diagnose, so applying incident triage (impact × urgency, escalation clock) to it just adds process weight to a fulfillment task.

**Problem**
The underlying, usually unconfirmed root cause producing a recurring pattern of incidents — a problem record exists to be investigated, not to be "resolved" on first contact like an incident.
*In use:* "Third 'internet down, 3rd floor' ticket this week — closing the incident, but opening a problem record to chase the actual switch fault."
*Misuse:* Treating a string of same-symptom incidents as N separate closures instead of one open problem — each incident gets a workaround and a satisfied user, but the underlying fault never gets a ticket, a budget line, or an owner, so it recurs indefinitely.

**Workaround**
A temporary way to restore the reported functionality without addressing the underlying cause — the incident can close on a workaround; the problem behind it cannot.
*In use:* "Rebooting the print spooler is the workaround — printing's back, but the root cause is still open on the problem ticket."
*Misuse:* Documenting a workaround as if it were a resolution and closing the associated problem record along with the incident. A workaround closing an incident is expected and fine; a workaround closing a problem means the fault will resurface with nothing tracking it.

**Root cause**
The specific, verified fault that, if removed, prevents the symptom from recurring — distinct from the first plausible explanation that happens to make the symptom stop.
*In use:* "Fix restored printing, but root cause wasn't confirmed until we found the spooler service crashing on a specific driver version."
*Misuse:* Writing "root cause: printer offline" on a ticket — that's the symptom, not the cause. A cause that doesn't explain why the fault will or won't recur isn't root cause yet, it's a description of the failure.

**First contact resolution (FCR)**
The percentage of tickets resolved during the reporter's initial contact, with no reopen, callback, or transfer required — a queue-design metric, not an individual-technician score.
*In use:* "FCR is 51% this month — before blaming technicians, check whether L1-capable tickets are even reaching tier 1."
*Misuse:* Read as a report card on technician skill or effort in isolation. A queue with a routing defect that reflexively escalates simple tickets to tier 2 will show low tier-1 FCR no matter how good tier-1 technicians are — the number indicts the routing rule as often as it indicts a person.

**% Resolved Level-1-Capable**
The share of tickets that were within tier 1's competence to resolve and actually did resolve there, as distinct from FCR, which only tracks whether resolution happened on first contact at whatever tier it landed.
*In use:* "FCR looks fine in aggregate, but %-Resolved-L1-Capable is low — these are getting bounced to tier 2 out of habit, not necessity."
*Misuse:* Assumed to be the same signal as FCR, or ignored entirely because FCR "already covers it." A ticket can resolve on first contact at tier 2 (good FCR) while still being a tier-1-capable ticket that never should have left tier 1 (bad on this metric) — the two numbers catch different failure modes.

**Escalation**
A deliberate handoff to a higher tier or specialized queue, made because the receiving tier's competence or authority is required — not a release valve for clock pressure.
*In use:* "Escalating with the ruled-out list attached: driver reinstall and cable swap both tested, still failing — needs hardware diagnostics."
*Misuse:* Used as a way to stop the SLA clock from breaching rather than because the fix genuinely requires tier 2/3. An escalation with no ruled-out list attached forces the next tier to restart the theory-testing step from zero, which is slower overall than if tier 1 had kept the ticket a few more minutes.

**Severity vs. priority**
Severity is how bad the impact is on its own (data loss, down for how many users); priority is the resulting queue position, and is set from impact × urgency, not from either factor alone or from how the request was phrased.
*In use:* "High severity — company-wide outage — but she reported it calmly by email, so priority still follows impact × urgency, not tone."
*Misuse:* Setting priority directly from how urgently something was asked (a loudly worded email, a VP's name in the subject line) instead of running impact × urgency. A single user's shouted request is not automatically high priority; a calmly reported company-wide outage still is.

**SLA (service level agreement) — acknowledge vs. resolve target**
Two separate clocks tied to a priority tier: the acknowledge target is how fast the ticket gets a first response; the resolve target is how fast it's actually fixed. Missing either is a distinct SLA breach.
*In use:* "P2 acknowledge target is 15 minutes to an hour — we're at 40 minutes with no response logged, that's a breach regardless of how the fix is going."
*Misuse:* Tracking only the resolve clock and treating "we're working on it" as sufficient even when no acknowledgment was ever logged within target — the acknowledge SLA exists specifically to guarantee the reporter isn't left wondering whether the ticket was even seen.

**Identity verification (independent channel)**
Confirming a requester's identity through a channel separate from the one the request arrived on, required before any account-state change — not the same as recognizing a name or a plausible-sounding story.
*In use:* "Can't reset that MFA token off this inbound call — I'll call the number on file and verify there before touching anything."
*Misuse:* Treating "they knew the employee ID" or "they sounded like they worked there" as verification. The MGM Resorts breach began with exactly that: a caller who'd gathered enough real details from LinkedIn to sound legitimate on the one channel the request arrived on — verification means a second, independent channel, not more confidence in the first one.

**Deflection**
Resolution of a user's need before a ticket is ever opened, via self-service (knowledge base, SSPR portal) — a tier-0 outcome, counted separately from anything a technician touches.
*In use:* "Password-reset deflection to the SSPR portal is at 80% adoption — those never become tickets at all."
*Misuse:* Conflated with FCR, which only measures tickets that were opened. A high-deflection queue can look unremarkable on FCR while quietly saving the most technician-hours of any single change, because the tickets it prevents never enter the FCR denominator in the first place.

**Tier 1 / Tier 2 / Tier 3**
Successive support levels defined by scope of authority and complexity handled, not by seniority or tenure — a ticket's tier assignment should track what it requires, not who happens to be available.
*In use:* "That's a tier-1-capable reset by policy — it shouldn't need tier-2 eyes just because tier 2 picked up the call."
*Misuse:* Used as informal shorthand for "junior staff" vs. "senior staff" rather than as a scope-of-authority boundary tied to ticket type. A routing rule that sends a ticket category to tier 2 "because that's just how it's always been handled" can leave 100% of an L1-capable category stuck above tier 1 indefinitely, with no technician ever making an individual bad call.

**Break-fix**
Reactive, incident-driven support work performed only after something has already failed, as distinct from proactive maintenance or scheduled service requests.
*In use:* "That's break-fix — the drive already failed — versus the proactive replacement cycle that would've caught it first."
*Misuse:* Applied to any hands-on technical task regardless of whether something actually broke, blurring it with scheduled maintenance or provisioning work. The distinction matters for staffing and budgeting: a desk dominated by break-fix work is signaling that proactive maintenance isn't catching failures before they become tickets.
