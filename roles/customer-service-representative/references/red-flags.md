# Customer Service Representative — Red Flags

### First-call resolution below 65-70% for a specific issue category
- **Usually means:** routing sends this issue type to a team without authority to resolve it, or agents lack the documented answer and are guessing.
- **First question:** what percentage of "resolved" tickets in this category reopen within 7 days?
- **Data to pull:** FCR report segmented by issue category, reopen-rate by category and by agent.

### Customer Effort Score of 4-5 (high effort) on a ticket marked "resolved"
- **Usually means:** the resolution required multiple contacts or transfers even though the system logged it as a single clean resolution.
- **First question:** how many total touches (calls, chats, transfers) did this ticket actually have, regardless of what the status field says?
- **Data to pull:** full contact history and transfer log for the ticket.

### Same customer contacts 3+ times in 30 days for issues that look different
- **Usually means:** either an unfixed underlying root cause relabeled each time, or a genuine account-fit mismatch generating unrelated friction.
- **First question:** are these actually the same root issue described differently each time?
- **Data to pull:** account contact history with root-cause tags across all three contacts.

### An agent grants goodwill credits above their authorized threshold repeatedly
- **Usually means:** either the agent misunderstands the policy, or the product/process is generating enough genuine failures that the agent is quietly compensating for it out of the wrong budget line.
- **First question:** are the credits clustering around one product area or defect?
- **Data to pull:** credit-approval audit log by agent and by root-cause tag.

### CSAT drops sharply for one issue category within a short window
- **Usually means:** a recent product release or policy change broke something that wasn't caught before launch.
- **First question:** when exactly did the drop start, and does it correlate with a release or policy-change date?
- **Data to pull:** CSAT trend by category with release/change-log dates overlaid.

### An escalated ticket sits unassigned past its SLA
- **Usually means:** the queue is understaffed for current volume, or the ticket was auto-routed to the wrong team.
- **First question:** did the routing rule actually match the ticket's true issue type?
- **Data to pull:** queue depth and staffing level at time of escalation; routing-rule match log.

### Customer cites a competitor's offer or explicit switching threat
- **Usually means:** a genuine retention-risk moment, not a negotiating bluff to discount automatically — but not automatically worth matching either.
- **First question:** what is this account's actual value and tenure, independent of how the threat is phrased?
- **Data to pull:** account LTV estimate, tenure, and prior support/complaint history.

### Refund or credit requested for an issue with no documented root cause on file
- **Usually means:** either a genuine edge case never seen before, or an attempted policy-abuse pattern.
- **First question:** does this account have a history of similar undocumented-cause requests?
- **Data to pull:** account-level refund/credit history over the account's lifetime, not just the current ticket.

### Complaint appears on social media or a public review before the internal ticket is resolved
- **Usually means:** either an internal SLA was already breached before the customer went public, or the customer had a prior bad experience that made them skip the normal process.
- **First question:** was there an existing open ticket for this customer, and how old is it?
- **Data to pull:** open-ticket history for the account; time since last agent contact.

### A macro/canned response is sent but doesn't address the customer's actual question
- **Usually means:** the agent pattern-matched on a keyword too quickly without reading the full message.
- **First question:** does the macro's trigger keyword actually appear in a context that matches its intended use?
- **Data to pull:** original customer message compared against the macro's intended-use documentation.
