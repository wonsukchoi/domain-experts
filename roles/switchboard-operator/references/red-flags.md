# Red flags

Smell tests a senior switchboard/TAS operator or supervisor catches early. Format for each: what it usually means, the first question to ask, and the data to pull.

### Message-accuracy audit below ~98%, or callback-number error tickets trending up
- **Usually means:** agents skipping read-back under queue pressure — accuracy erosion tracks ASA pressure almost exactly, not agent carelessness in isolation.
- **First question:** "What's ASA the last two weeks versus the last three months, on the accounts where these errors are landing?"
- **Data to pull:** message-accuracy audit log by agent and account; ASA trend for the same window; whether read-back is even scripted as a mandatory step on the affected account.

### Abandonment rate above ~5% on an account
- **Usually means:** understaffing against real volume, not a one-off spike — a single bad day rarely moves a rolling abandonment rate this much.
- **First question:** "Is this a volume spike against flat staffing, or has staffing dropped against flat volume?"
- **Data to pull:** call arrival volume by hour for the last 4 weeks; scheduled agent-hours for the same account and window; whether a surge/overflow protocol exists and whether it triggered.

### On-call rotation unreachable on more than one attempt in a shift
- **Usually means:** the escalation chain is stale — a cell number changed, a physician left the rotation, and nobody re-tested the chain since the last update.
- **First question:** "When was this on-call list last confirmed live with the client, not just updated on paper?"
- **Data to pull:** escalation-chain change history; live-callback test log from the last onboarding or update; count of escalation-failure log entries in the trailing 90 days.

### Agent gave advice or guidance beyond the script's branch points
- **Usually means:** a script gap forced an off-script judgment call, or an under-trained agent improvised rather than escalating an unmatched call.
- **First question:** "What did the script say to do at the exact point this call diverged?"
- **Data to pull:** call recording or transcript, script version in effect at call time, and whether this keyword/situation has come up before without a script update following it.

### Overhead code or mass-notification activation delayed beyond the facility's target window
- **Usually means:** unclear ownership of who pages first, a console/system fault, or the operator wasn't drilled on this facility's specific code sheet.
- **First question:** "Walk me through, second by second, from the trigger call to the page going out."
- **Data to pull:** activation timestamp vs. acknowledgment timestamp from the incident log; operator's last code-sheet drill date; system uptime/fault log for the paging console that shift.

### Sustained occupancy above ~90–92%
- **Usually means:** the queue looks efficient on a dashboard while accuracy and agent burnout are quietly rising — high occupancy is a leading indicator of read-back skipping, not a productivity win.
- **First question:** "What's average handle time and agent turnover done over the same period occupancy climbed?"
- **Data to pull:** occupancy trend, AHT trend, message-accuracy trend, agent attrition/absence rate — all on the same timeline.

### VIP or do-not-disturb list mismatch (a screened call gets through, or a cleared caller gets blocked)
- **Usually means:** the list wasn't synced to the console after the client's last update — these lists change more often than anyone remembers to push them.
- **First question:** "When was this list last updated on the client side, and when was it last pushed to the console?"
- **Data to pull:** list version/timestamp on both the client's source document and the live console configuration.

### Client billing dispute over call count or minutes
- **Usually means:** CDR is logging transfers or holds as separate billable events, inflating the count against what the client's own phone log shows.
- **First question:** "Pull raw CDR against the client's own call log for the disputed period — where's the delta?"
- **Data to pull:** raw CDR export, billed-call reconciliation report, transfer/hold-handling configuration for that account.

### Spike in misrouted or "wrong extension" transfers
- **Usually means:** the extension/directory map is out of date after a reorg, new hire, or department move that never reached the console configuration.
- **First question:** "When did this org last change its extension structure, and when was the console's directory last refreshed against it?"
- **Data to pull:** misroute log by extension, directory-map last-updated date, comparison against the client's current org chart.

### Medical-account message log contains full diagnosis, SSN, or other detail beyond callback-brief format
- **Usually means:** the agent is transcribing what the caller says verbatim instead of applying the minimum-necessary standard — a training or script-discipline gap, and a compliance exposure for the account.
- **First question:** "What does the script say to capture at this branch point, and does the logged message match that or the caller's raw statement?"
- **Data to pull:** message content sample audit against script requirements; whether the account is under a signed HIPAA business-associate agreement; prior compliance training records for the agent.

### Emergency-keyword escalation count declining while total call volume is flat
- **Usually means:** the keyword list has gone stale relative to how callers actually phrase things now, or agents have grown desensitized and are under-flagging borderline calls — not that emergencies have genuinely dropped.
- **First question:** "When was the emergency keyword list last reviewed against actual call transcripts, not just written once at onboarding?"
- **Data to pull:** escalation count trend vs. total volume trend; sample of routine-classified calls for keyword-adjacent language that should have escalated.

### New client went live with no pre-launch test-call audit
- **Usually means:** launch-date pressure skipped the onboarding checklist step that catches script and escalation-chain errors before a real caller does.
- **First question:** "Show me the 10-call test-audit results from before go-live."
- **Data to pull:** onboarding checklist completion record; first-week live-call error rate compared against accounts that did complete the pre-launch audit.
