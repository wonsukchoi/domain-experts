# Insurance Claims and Policy Processing Clerk — Red Flags

### Photos submitted show inconsistent lighting/weather conditions across the claimed loss date
- **Usually means:** Photos taken on different dates than claimed, or photos not actually from the loss location.
- **First question:** "Can you confirm all photos were taken on [date of loss]?"
- **Data to pull:** Photo metadata (timestamp, geolocation if available) against claimed date of loss.

### Contact information on the claim submission doesn't match the policy's on-file contact information
- **Usually means:** Legitimate update never processed, or the submission isn't from the actual policyholder.
- **First question:** "Has your contact information changed recently? If so, when did you last update it with us?"
- **Data to pull:** Policy's on-file contact history and last-updated date.

### Prior-claims history shows 3+ claims on the same address within 12 months
- **Usually means:** Legitimate high-risk property (older home, prior unaddressed damage), or a pattern worth an adjuster's attention.
- **First question:** Not this role's call to make — route to adjuster with the prior-claims count and dates, no editorializing.
- **Data to pull:** Full claims history on the address, not just the policyholder's name (a property can have multiple named insureds over time).

### Cause-of-loss code and narrative describe inconsistent event types
- **Usually means:** Miscoded at intake (most common), policyholder unclear on cause, or a genuine mismatch worth flagging.
- **First question:** "Can you describe what caused the damage in your own words?"
- **Data to pull:** Original narrative text, submitted code, and any photos for cross-reference.

### Contractor/repair estimate submitted before an adjuster has scoped the loss
- **Usually means:** Policyholder proactively getting ahead of the process (common, not suspicious on its own), or a public-adjuster/contractor relationship steering the claim.
- **First question:** Route to adjuster with a note — this role doesn't evaluate estimate reasonableness, only logs it as received.
- **Data to pull:** Estimate source (independent contractor vs. a company frequently appearing across multiple claims).

### Endorsement request effective date falls before an already-open claim's date of loss
- **Usually means:** Processing error if unintentional, or a request to retroactively expand coverage onto an existing loss — the latter needs underwriter review, not routine processing.
- **First question:** "Can you confirm the requested effective date for this change?"
- **Data to pull:** Open-claims query on the policy number before processing any endorsement.

### Proof-of-loss statement received with a signature date after the claim's stated filing deadline
- **Usually means:** Filing-window tracking wasn't flagged at intake (process gap on this role's end), or the policyholder genuinely missed the deadline.
- **First question:** Route to adjuster/coverage desk immediately — a late proof-of-loss can affect the claim's validity depending on state law.
- **Data to pull:** Date of loss, applicable state's filing-window length, and the actual signature/receipt date.

### File has been in "pending information" status past the cycle-time benchmark with no status update sent
- **Usually means:** Held file fell off the clerk's active tracking (most common), request never actually went out despite being logged as sent.
- **First question:** "When was the last outbound communication on this file, and is there a delivery/read confirmation?"
- **Data to pull:** File's communication log against the benchmark date.

### Multiple claims across different policyholders list the same contractor/mitigation company with similar estimate amounts
- **Usually means:** Legitimate high-volume local contractor, or a pattern worth an SIU look.
- **First question:** Not this role's call — route the pattern (company name, claim numbers, estimate amounts) to the adjuster or SIU liaison without characterizing it as fraud.
- **Data to pull:** Cross-claim search by contractor/company name field, not just by policyholder.
