# Vocabulary

Terms generalists conflate or use loosely that a switchboard/TAS operator keeps sharply separate.

### ASA vs. abandonment rate
**ASA** (average speed of answer) is how long a caller waits before an agent picks up, averaged across all answered calls. **Abandonment rate** is the percentage of callers who hang up *before* being answered — a call that abandons never enters the ASA calculation at all, which means ASA can look fine while abandonment is quietly climbing on the calls that gave up.

**In use:** "ASA looks stable at 12 seconds, but abandonment jumped to 8% — we're not answering slower, we're losing the calls that would've pulled the average up."

**Common misuse:** reporting ASA alone as "queue health," which hides exactly the calls that never got answered.

### Occupancy vs. utilization
**Occupancy** is the percentage of an agent's logged-in time spent actively on a call or in after-call work (wrap-up, logging). **Utilization** is the broader figure including scheduled but non-call activities like training or breaks. A dashboard showing high occupancy looks like efficiency; it's often understaffing wearing a productivity costume.

**In use:** "Occupancy's been over 90% for two weeks — that's not a well-run queue, that's not enough agents."

**Common misuse:** treating occupancy near 100% as the goal, rather than a warning threshold past which accuracy and burnout both degrade.

### TSR (Telephone Service Representative)
The industry-specific job title and ATSI certification for a trained telephone-answering-service agent, distinct from a generic "receptionist" or "operator" — it implies script discipline, triage training, and account-specific certification, not just call-answering.

**In use:** "She's a certified TSR — she's trained on emergency-keyword triage, not just message-taking."

**Common misuse:** using "operator" and "TSR" interchangeably when describing hiring or training requirements; TSR certification is a specific, verifiable credential.

### CDR (call detail record)
The system-generated log of every call event — timestamp, duration, disposition, transfers — that billing and audits are built from. It is a raw event log, not the same thing as a "billed call count" until it's reconciled against the account's billing rules (a transfer might log as two events but bill as one call).

**In use:** "The billing dispute is real — raw CDR shows 340 events this month, but half are holds that shouldn't count as separate calls."

**Common misuse:** quoting CDR event counts directly as the invoice number without reconciling transfer/hold logic first.

### On-call rotation vs. escalation chain
**On-call rotation** is the schedule of who is designated as primary responder for a given period. **Escalation chain** is the ordered fallback sequence — who gets contacted next, and after how long, if the primary doesn't respond. Confusing the two leads to "escalating" by just re-trying the same primary contact instead of moving to the next name in the chain.

**In use:** "Primary didn't respond in 4 minutes — that's the chain's trigger, not a reason to try her again, move to secondary."

**Common misuse:** treating "escalate" as synonymous with "call again," rather than "move to the next contact in the defined sequence."

### Script branch vs. flat script
A **script branch point** is a decision node where the operator's next action depends on what the caller says (an "if this, then that" moment). A **flat script** is verbatim text with no decision logic. Most real scripts are mostly flat with a handful of branch points that carry nearly all the judgment risk.

**In use:** "The greeting's flat, read it verbatim — but branch 1, the emergency-keyword check, is where the actual training happens."

**Common misuse:** assuming "follow the script" means reciting text, when the real skill is correctly identifying which branch a live caller's words have triggered.

### PBX vs. ACD
A **PBX** (private branch exchange) is the system that routes and switches calls within an organization — internal extensions, external trunk lines. An **ACD** (automatic call distributor) sits on top, queuing inbound calls and distributing them to available agents by a defined rule (round-robin, skills-based, priority). A TAS or hospital switchboard typically runs an ACD layered over PBX/carrier trunks, not one or the other alone.

**In use:** "The PBX routes the trunk lines fine — the queuing problem is in the ACD rule set, not the phone system itself."

**Common misuse:** calling any phone-routing problem a "PBX issue" when the actual fault is in queue/distribution logic, which is a different system with different fixes.

### Overhead paging vs. mass notification
**Overhead paging** is a live audio broadcast within a physical building. **Mass notification** is a simultaneous, multi-channel alert (pager, text, app push, email) to a defined roster, independent of whether anyone is near a speaker. Hospitals require both for code activations — overhead paging alone reaches only people currently in the building and in earshot.

**In use:** "The page went out fine, but mass notification didn't fire — that's why the off-site cardiologist didn't get paged."

**Common misuse:** assuming an overhead page satisfies an emergency-notification requirement on its own.

### Minimum necessary (HIPAA)
The HIPAA Privacy Rule standard requiring that only the minimum protected health information needed for the stated purpose be used, disclosed, or — for an answering service — relayed in a message. It is not a discretionary judgment call; it's a compliance floor.

**In use:** "Log the callback reason as 'medication question,' not the specific drug and dosage she volunteered — that's more than the message needs."

**Common misuse:** transcribing everything a caller says verbatim on the theory that more detail is more helpful, when it's actually a compliance exposure on a covered account.

### Erlang C
A queuing-theory formula used to estimate the number of agents needed to hit a target service level given an average call arrival rate and average handle time. It assumes a steady-state Poisson arrival process.

**In use:** "Erlang C says 6 agents clears our normal Tuesday volume at target ASA — but that's the baseline, not the flu-season number."

**Common misuse:** trusting the model's point estimate as a staffing plan on its own, without padding for known seasonal or event-driven spikes the model's constant-arrival-rate assumption doesn't capture.

### SLA tier
The contracted service-level commitment (typically ASA target and accuracy floor) attached to a specific client account, distinct from the operator's general effort level. Different accounts in the same shared queue routinely carry different tiers.

**In use:** "This account's Tier 1 at a 15-second ASA — the floater goes here before the Tier 3 account down the hall."

**Common misuse:** treating a shared queue as one undifferentiated pool and answering strictly in arrival order, which silently breaches the tighter-SLA account's contract to protect the looser one's average.
