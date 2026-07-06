# Red flags — computer-user-support-specialist

### Caller asks for a password/MFA reset or remote-control session and cites urgency ("I'm about to miss a call with the CEO") within the first 60 seconds
- **Usually means:** A legitimate employee genuinely locked out and stressed, or — indistinguishable at this point — a pretext call running the FTC-tracked tech-support-scam / help-desk-social-engineering pattern (the MGM Resorts breach opened exactly this way).
- **First question:** "What's a way to reach you back on a number or address already on file, separate from this call?"
- **Data to pull:** HR directory entry (phone, manager, start date) and the account's last-known verified contact channel.

### Same account requests 2+ password/MFA resets within a 30-day window
- **Usually means:** An expiring-password policy colliding with a shared device or bad habit (a service request masquerading as a recurring incident), or credential-stuffing pressure making the account a live target.
- **First question:** "Is this the same underlying cause each time, or a new one?"
- **Data to pull:** Ticket history for the account, filtered to category = password/account, last 90 days.

### Request to change the on-file recovery email or phone number arrives in the same contact as a credential-reset request
- **Usually means:** A legitimate device change bundled for convenience, or an attacker locking out the real owner's recovery path before pivoting further into the account.
- **First question:** "Can you confirm the current recovery contact on file before we change it?"
- **Data to pull:** Account audit log for recovery-contact field changes in the last 30 days.

### Caller fails the standard identity challenge but offers to answer a substitute question instead
- **Usually means:** A legitimate employee who forgot the answer (rare, but happens after a life event like a name change), or someone working from partial OSINT (LinkedIn, a data-breach dump) who can't clear the real bar.
- **First question:** "Can I call you back on the number already in the directory instead?"
- **Data to pull:** Directory record for the callback number and a check of whether that number matches the ticket's stated contact.

### A ticket tagged L1-capable sits in the tier-2 queue for >24 hours before anyone touches it
- **Usually means:** A stale routing rule sending an entire category to tier 2 regardless of complexity, not a tier-2 workload spike.
- **First question:** "Is this ticket type auto-routed by category, or was it escalated by a person?"
- **Data to pull:** % Resolved Level-1-Capable report and the routing rule config for the ticket's category.

### The same symptom (same error, same device class, or same app) generates 5+ incidents in a rolling 7-day window
- **Usually means:** A shared root cause that's never been opened as its own problem ticket — every occurrence gets resolved individually and the underlying cause recurs.
- **First question:** "Has anyone opened a problem record linking these, or is each one closed as a one-off incident?"
- **Data to pull:** Incident list filtered by symptom keyword and date range, sorted by affected device/user.

### A ticket is marked resolved and reopens within 48 hours
- **Usually means:** The fix addressed the loudest symptom, not the original report, or verification against the full original complaint was skipped.
- **First question:** "What was verified as fixed before this was closed — the original report or just the symptom mentioned last?"
- **Data to pull:** The closed ticket's resolution notes plus the reopened ticket's new description.

### Queue-wide first-contact resolution sits below ~60% for 2+ consecutive months in a desk with documented tiers
- **Usually means:** A routing or definition problem (misclassified tickets, stale auto-escalation rules) rather than a technician skill gap — HDI's own benchmark gap between tiered (72%) and undefined (45%) desks is structural.
- **First question:** "Are we measuring FCR against tickets that never reach tier 1 in the first place?"
- **Data to pull:** % Resolved Level-1-Capable broken out by category, next to the routing-rule config per category.

### A ticket requesting new software/system access has no linked HR onboarding record or manager approval
- **Usually means:** A normal request that simply skipped the paperwork step, or an attempt to provision access outside the approval chain.
- **First question:** "Who's the approving manager, and can I see the request in the access-management system?"
- **Data to pull:** HRIS onboarding/role record and the access-request ticket in the identity-management system.

### Average speed to answer on a queue drops below ~10 seconds while ticket volume is flat or rising
- **Usually means:** Tickets are being auto-accepted and closed without the standard identify → verify → diagnose sequence being run, inflating a metric that looks good on a dashboard.
- **First question:** "Pull three of this week's sub-10-second tickets — was identity verification actually logged on each?"
- **Data to pull:** Call/chat timestamps against the ticket's logged verification step, for a sample of recent closures.

### An escalated ticket arrives at tier 2/3 with no ruled-out list or troubleshooting notes attached
- **Usually means:** Clock pressure produced an escalation before the six-step theory-testing sequence was actually run, forcing tier 2 to restart from zero.
- **First question:** "What's already been ruled out, and what's the theory that led to escalating instead of continuing?"
- **Data to pull:** The ticket's activity log/notes field for the time between assignment and escalation.

### A single department or building generates a P1-severity spike (10+ tickets) within a 2-hour window
- **Usually means:** A real infrastructure outage (network, auth provider, shared server) rather than 10 unrelated individual incidents — each one classified alone under-prices the true impact.
- **First question:** "Do these share a location, subnet, or upstream system, or are they genuinely unrelated?"
- **Data to pull:** Ticket list for the window filtered by location/device, cross-referenced against infrastructure monitoring/status-page alerts.
