# Bill and Account Collector — Red Flags

### Debtor disputes the debt amount or existence, not just refusing to pay
- **Usually means:** A billing error, an identity-mix-up, or the debtor genuinely contesting the charge — distinct from simple non-payment or hardship.
- **First question:** "Is this a question about whether you owe this, or about when/how you can pay it?"
- **Data to pull:** Original account documentation, prior validation-notice send date, any written dispute already on file.

### More than 5 contact attempts logged to this debt within the trailing 7 days
- **Usually means:** The account is approaching or has hit the Reg F 7-in-7 ceiling; continuing risks a compliance violation regardless of intent.
- **First question:** "How many contacts have registered against this specific debt in the last 7 days, and when was the most recent one?"
- **Data to pull:** Call-frequency log filtered to this specific debt (not just this debtor, if they have multiple accounts).

### Debtor states "I have an attorney" or "my lawyer is handling this"
- **Usually means:** Legal representation has begun, even if formal notice hasn't been received in writing yet.
- **First question:** "Can you provide your attorney's name and contact information so I can direct future communication appropriately?"
- **Data to pull:** Any existing attorney-representation flag; confirm and flag the account immediately regardless of written confirmation status.

### Debtor mentions bankruptcy, even informally ("I might have to file")
- **Usually means:** Either bankruptcy has already been filed (automatic stay applies immediately) or is being considered — either way, continued collection pressure creates legal exposure.
- **First question:** "Have you already filed, or are you speaking with a bankruptcy attorney?"
- **Data to pull:** Court records/case number if filed; if uncertain, treat as a stop-and-verify trigger before further contact.

### Account is more than 6 years past the last activity date (varies by state statute of limitations)
- **Usually means:** The debt may be time-barred — still owed, but not legally enforceable through a lawsuit in most states.
- **First question:** "What is this state's statute of limitations for this debt type, and has it run?"
- **Data to pull:** State-specific SOL rules, last-payment or last-activity date establishing the SOL clock start.

### Debtor asks "can you sue me over this?" on a time-barred account
- **Usually means:** A high-risk moment for an FDCPA §1692e violation — any answer implying legal action is available when it is not (or without required disclosure in disclosure states) is a false representation.
- **First question:** Internally: "Is this debt past the state SOL, and does this state require a time-barred disclosure?"
- **Data to pull:** State-specific time-barred-debt disclosure requirements (several states mandate specific language).

### A payment plan has broken twice at the same structure
- **Usually means:** The plan size was never sustainable for this debtor's actual cash flow, not that the debtor is uncooperative.
- **First question:** "What changed between when we set this up and now that made the payment difficult?"
- **Data to pull:** Payment history against the plan, any hardship indicators noted in prior contacts.

### Debtor becomes agitated, raises voice, or makes a statement suggesting self-harm or crisis
- **Usually means:** This has moved outside a standard collection interaction and requires immediate escalation, not de-escalation scripting.
- **First question:** None — escalate immediately per crisis-response protocol before continuing any collection conversation.
- **Data to pull:** N/A; this is a stop-collection-activity trigger, not a data-gathering moment.

### Third party (family member, roommate, coworker) answers and collector is asked to "just tell them" the balance
- **Usually means:** A third-party-disclosure risk under FDCPA §1692c(b) — collectors generally cannot discuss debt details with anyone but the debtor (with narrow exceptions).
- **First question:** "Is [debtor's name] available? I can only discuss this matter directly with them."
- **Data to pull:** Right-party-contact verification status on the account; confirm no disclosure occurred.

### Debtor claims identity theft ("this isn't my debt, someone used my information")
- **Usually means:** Possible fraud victim — continuing to press for payment through an unverified claim is both a compliance and accuracy risk.
- **First question:** "Have you filed an identity-theft report with the FTC or local police?"
- **Data to pull:** Any fraud-alert flag on the account; route to fraud queue pending documentation.

### Debtor offers a lump-sum settlement significantly below any prior payment-plan capacity they've shown
- **Usually means:** Either a genuine liquidity event (windfall, loan, family help) worth taking seriously, or a lowball anchor expecting a counter.
- **First question:** "What's driving your ability to offer a lump sum today versus the payment plan we discussed?"
- **Data to pull:** Settlement-authorization band for this account's aging stage and balance.
