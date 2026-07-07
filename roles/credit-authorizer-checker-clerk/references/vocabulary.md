# Credit Authorizer, Checker, and Clerk — Vocabulary

### Available credit
The amount an account can still authorize against right now: credit limit minus posted balance minus all pending/held authorizations.
**In use:** "The printed limit says $5,000, but available credit is only $1,170 once you subtract the two open holds."
**Common misuse:** treating "available credit" and "credit limit minus posted balance" as the same number — they're only the same when there are zero pending holds, which is rarely the case on an active account.

### Authorization hold
A temporary reservation of credit against a pending transaction that hasn't posted as a final charge yet.
**In use:** "That $180 hotel hold will release automatically in 72 hours if the final folio never posts."
**Common misuse:** assuming a hold is the same as a charge and that it will definitely post for that exact amount — holds can post for a different amount (tips, incidentals) or expire unposted.

### Adverse action
A legally defined event under FCRA/ECOA — denying an application, approving on worse terms than requested, or reducing an existing credit line — that triggers a mandatory notice with specific content.
**In use:** "A credit-limit reduction on an existing account is adverse action too, not just a new-application denial — it needs the same notice."
**Common misuse:** thinking "adverse action" only applies to outright denials; it also covers less-favorable terms and involuntary limit decreases.

### Principal reason (adverse-action notice)
The specific, individualized factor(s) that drove a decline decision, required by ECOA/Regulation B — not a category or boilerplate phrase.
**In use:** "The principal reason has to be 'income insufficient for amount requested,' not 'does not meet our lending criteria.'"
**Common misuse:** citing a generic denial category instead of the actual rule that fired, which satisfies the letter of sending a notice but not the requirement that it state the real reason.

### Velocity
The rate of transaction attempts on an account within a short time window — a key low-latency fraud signal independent of any single transaction's size.
**In use:** "Three declined attempts at three different merchants in twelve minutes is a velocity flag, even though none of the individual amounts looks unusual."
**Common misuse:** treating velocity as only about large-dollar transactions; a burst of small "card-testing" transactions is a classic velocity pattern precisely because each one looks unremarkable alone.

### Chargeback
A card-network-mediated reversal of a transaction, initiated by the cardholder's issuing bank on the cardholder's behalf, distinct from a merchant-initiated refund.
**In use:** "The cardholder didn't get a refund from the merchant, so we filed a chargeback with the network instead."
**Common misuse:** using "chargeback" and "refund" interchangeably — a refund is the merchant voluntarily reversing a charge; a chargeback is a formal dispute process the merchant can contest.

### Filing window
The rule-defined period (set by regulation or card-network operating rules) within which a dispute must be filed to be eligible for processing.
**In use:** "The transaction is from four months ago — check the specific reason code's filing window before doing anything else with this dispute."
**Common misuse:** assuming a single universal window (like "90 days") applies to all disputes; the window varies by dispute type, reason code, and network.

### Stipulation
A specific additional document or clarification requested from an applicant to resolve a verification gap, short of an outright decline.
**In use:** "Rather than decline on the income mismatch, we're requesting a stipulation — the applicant's most recent W-2."
**Common misuse:** treating a stipulation request as equivalent to a decline; it's a middle path that keeps the application open pending a specific, named piece of evidence.

### Posted balance
The account balance reflecting transactions that have fully settled, as distinct from pending authorizations that haven't posted yet.
**In use:** "Posted balance is $3,200, but total exposure including pending holds is closer to $3,830."
**Common misuse:** using "posted balance" and "current balance" as if they capture the same exposure — posted balance excludes pending holds, which is exactly why available-credit math has to add them back separately.

### Step-up verification
An additional, higher-friction identity or transaction check triggered by a specific risk signal (velocity, geographic anomaly, high-value request), applied selectively rather than to every transaction.
**In use:** "The velocity flag triggered step-up verification — we texted a one-time code to the phone on file before approving."
**Common misuse:** applying step-up verification uniformly regardless of risk signal, which defeats its purpose (targeted friction on elevated-risk events) and just adds friction to routine transactions.

### Partial authorization
Approving a transaction for less than the requested amount, up to the available credit, when the merchant's system supports splitting payment across a remaining balance and another payment method.
**In use:** "We can't authorize the full $1,250, but a partial authorization for the $1,170 available is possible if the merchant terminal supports split tender."
**Common misuse:** assuming partial authorization is always an option — it depends on merchant-terminal capability, not issuer policy alone.

### Card-not-present (CNP) transaction
A transaction where the physical card isn't presented to the merchant (online, phone) — carries materially different fraud-risk and dispute-resolution rules than a card-present transaction.
**In use:** "That's a CNP transaction, so chip/PIN authentication doesn't apply — the dispute path and evidentiary standard are different."
**Common misuse:** applying card-present fraud-liability and evidence standards to a CNP dispute; the two have different network rules and different liability-shift conventions.
