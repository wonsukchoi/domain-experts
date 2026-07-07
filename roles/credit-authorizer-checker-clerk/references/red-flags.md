# Credit Authorizer, Checker, and Clerk — Red Flags

### Requested amount within 10% of available credit but account shows 3+ authorization attempts in under an hour
- **Usually means:** velocity-based fraud testing (a stolen card being probed with small-to-large amounts to find the limit) — second most likely is a legitimate cardholder retrying a declined transaction without realizing why it declined.
- **First question:** are the attempts from the same merchant/terminal, or scattered across different merchants in a short window?
- **Data to pull:** authorization log for the account over the last 60 minutes, merchant category codes, and geographic location if available.

### Stated income on an application doesn't reconcile with the verifying pay stub's annualized figure by more than ~15% [heuristic — issuer-specific threshold]
- **Usually means:** the applicant rounded up hopefully, or the pay stub reflects a partial-year ramp (new job, recent raise) — second most likely is misrepresentation.
- **First question:** does the pay stub's YTD figure and pay-period count support a clean annualization, or is there a raise/bonus/overtime pattern that explains the gap?
- **Data to pull:** most recent pay stub YTD line, prior year's W-2 if available, and employer start date.

### A chargeback is filed with a transaction date more than 90 days old and no clear window-close date on file
- **Usually means:** the filer (customer or merchant) didn't check the window before filing — second most likely is the dispute reason code carries a longer window than the default assumption.
- **First question:** what is this specific network's filing window for this specific dispute-reason code, not the general default?
- **Data to pull:** the network's current chargeback reason-code table and the transaction's original post date.

### An application's address, phone number, or email doesn't match any prior record for the stated identity
- **Usually means:** a legitimate move/new contact info — second most likely is identity theft using a real person's SSN with different contact details to redirect correspondence.
- **First question:** does the credit-bureau file show the new address as an update, or is it entirely absent from bureau history?
- **Data to pull:** credit-bureau address history, and whether the application channel (in-branch vs. online) matches the account's typical pattern.

### A cardholder disputes a transaction they authorized in person (chip/PIN or signature) with no fraud indicators on the account
- **Usually means:** buyer's remorse or a merchant/service dispute (didn't receive goods, dissatisfied) misfiled as a fraud dispute — second most likely is family-member/friendly fraud (someone with card access made the purchase).
- **First question:** is this a "didn't authorize" dispute or a "not as described / not received" dispute — they route to completely different resolution paths.
- **Data to pull:** the authorization method on the original transaction (chip+PIN requires physical card presence) and any prior dispute history on the account.

### An endorsement or credit-line-increase request arrives with the requested new limit exactly matching a round, high number ($10,000, $25,000) with no supporting income change on file
- **Usually means:** a legitimate ambitious request — second most likely is a fraud pattern where an account is built up with clean behavior specifically to request a large limit increase before running it up.
- **First question:** does the account's payment history and utilization pattern support organic credit growth, or does the request come with no prior gradual increase?
- **Data to pull:** account age, payment history, and utilization trend over the last 12 months.

### A document submitted for verification has metadata or formatting inconsistent with its claimed source (a "pay stub" with no employer letterhead, inconsistent fonts, or a creation date that postdates the pay period it covers)
- **Usually means:** a template-generated fake document — second most likely is a legitimate but poorly formatted document from a small employer without standardized payroll software.
- **First question:** can the employer be verified independently (phone number from a public source, not the one listed on the document)?
- **Data to pull:** the document's file metadata if available, and an independent employer contact number.

### A dispute intake shows the same merchant name appearing across multiple unrelated cardholder disputes in the same week
- **Usually means:** a legitimate merchant-side problem (an outage, a billing-system error) affecting many customers at once — second most likely is a merchant-side fraud or chargeback-fraud scheme.
- **First question:** are the disputes clustering around the same date/transaction type, suggesting a common cause?
- **Data to pull:** a list of all open disputes against that merchant in the current period, sorted by transaction date.
