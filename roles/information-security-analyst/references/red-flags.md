# Red flags — what an information security analyst notices instantly

Smell tests with thresholds. Any one alone can be innocent; two or three together on the same account, host, or time window is worth opening a case over.

### A detection rule's trailing-90-day false-positive rate above ~90%, tied to a high-severity technique
- **Usually means:** the threshold was set defensively wide when the rule shipped and never retuned as traffic patterns shifted — the rule is technically "coverage" but functionally invisible to the analyst triaging it, exactly the condition that let an impossible-travel alert sit unread for 15 hours in the Incident 2026-0309 case.
- **First question:** "What direction did we move this rule the last time its FP rate was reviewed — and when was that?"
- **Data to pull:** rule's confirmed-TP vs. total-alert count over the trailing quarter, current alert routing (live paging vs. log-only), date of last threshold change.
- (See `references/playbook.md` §3 for the tuning-cadence table and the severity-aware retune rule.)

### MFA push notifications sent to the same account more than ~5 times within a 10-minute window
- **Usually means:** an attacker with valid credentials attempting push-bombing/MFA fatigue, hoping the user approves out of annoyance; second most likely is a misconfigured service account looping a legitimate auth retry, which should also be fixed but isn't malicious.
- **First question:** "Was the approval that finally succeeded logged from the same device/IP as all the prior rejections, or a different one?"
- **Data to pull:** MFA prompt log with device/IP per attempt, whether any prompts were rejected before the accept, geo/IP reputation on the source of the login attempt.

### A workstation account initiating SMB admin-share (`C$`/`ADMIN$`) or RDP connections it has never made before
- **Usually means:** lateral movement using a harvested credential — this is the single highest-signal indicator that an intrusion has moved past the initial foothold, ahead of any alert about the initial compromise itself.
- **First question:** "Pull this account's admin-share/RDP connection history for the last 90 days — has it ever connected to these specific hosts before, or is this the first time?"
- **Data to pull:** EDR process lineage and network-connection logs for the source host, PAM session logs if the account is privileged, destination hosts' own logs for the same timestamp.

### Non-standard process accessing LSASS memory
- **Usually means:** credential-dumping tooling (Mimikatz-family or living-off-the-land equivalents) harvesting cached credentials from memory — rarely a false positive once the process lineage is confirmed non-standard.
- **First question:** "What process opened a handle to LSASS, and is it signed, and does it match any known admin/backup tooling that legitimately touches it?"
- **Data to pull:** EDR process-tree for the LSASS access event, hash/signature lookup against known-good and known-bad lists, timestamp correlation against any recent authentication events on the same host.

### A critical (CVSS 9.0–10.0) vulnerability more than 15 days past patch availability on an internet-facing or Tier-0-adjacent asset
- **Usually means:** either a genuine resourcing conflict (change freeze, maintenance-window contention) that needs an exception process, or the vulnerability-management backlog isn't being triaged by exposure at all — both point to the same fix, but the first needs a policy carve-out and the second needs a process audit.
- **First question:** "Why specifically did this one miss SLA — freeze conflict, missing owner, or nobody flagged the exposure tier?"
- **Data to pull:** vulnerability-scan first-seen date, patch-availability date from vendor advisory, change-management ticket history for the asset, asset criticality/exposure tag from the CMDB.
- (See `references/playbook.md` §2 for the exposure-adjusted SLA table.)

### A mailbox rule created that auto-forwards, deletes, or hides messages matching security-alert sender addresses
- **Usually means:** an attacker with mailbox access hiding evidence of their own activity (password-reset confirmations, MFA alerts, security-team notifications) from the legitimate user — this is a near-certain post-compromise indicator, not a benign productivity rule, when the filter target is security/IT-alert senders specifically.
- **First question:** "When was this rule created, and does that timestamp align with any other suspicious login or MFA event on this account?"
- **Data to pull:** mailbox rule creation audit log (creation timestamp, creating session/IP), correlated login history for the same account in the surrounding hour.

### A single local-admin credential valid across three or more hosts of different trust tiers
- **Usually means:** credential/account reuse or an overly broad admin-group membership that turns one workstation compromise into an organization-wide lateral-movement path — this is a design gap (the trust relationship), independent of whether an incident has exploited it yet.
- **First question:** "If this exact credential were compromised right now, list every host it could reach — has anyone actually enumerated that, or is this an assumption?"
- **Data to pull:** AD/IAM group membership for the account, a live enumeration of hosts trusting that credential, prior access reviews for the same account (and how long ago the last one ran).

### The same ATT&CK technique category recurring across two or more incidents within a quarter
- **Usually means:** the control gap from the first incident's remediation was never actually closed, or was closed for one host/account but not the underlying pattern.
- **First question:** "Pull the remediation item from the last incident in this category — was it closed with a verification step, or just marked done?"
- **Data to pull:** post-incident review backlog items by technique category and closure date, MTTD/MTTR trend for the category (see `references/playbook.md` §4), any verification evidence attached to the prior closure.

### An overnight or off-hours alert queue with a single on-call analyst and a backlog exceeding the alert's severity SLA
- **Usually means:** a staffing-model gap where severity-tiered SLAs exist on paper but aren't achievable with current shift coverage — this is a structural finding, not a performance issue with the analyst on shift.
- **First question:** "How long did this specific alert sit in queue before triage started, against its severity's SLA target?"
- **Data to pull:** alert-to-triage timestamp gap by severity tier and shift, on-call staffing roster for the period, queue depth at the time the alert arrived.
