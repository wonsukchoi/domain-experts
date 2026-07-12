# Rental Counter Clerk — Red Flags

### Damage waiver declined on a liability-heavy item (over the store's COI threshold) with no certificate of insurance on file
- **Usually means:** The clerk accepted a verbal insurance assurance without pulling documentation, often under counter time pressure.
- **First question:** Is there a current COI on file naming the store as additional insured for this reservation, or just a note that the customer said they're covered?
- **Data to pull:** Reservation file's insurance-document field, item's replacement value against the COI-required threshold.

### A unit "due back today" is promised to a new reservation before it's checked in
- **Usually means:** The reservation system's "available" status was trusted over physical verification, or scheduling assumed an on-time return that hasn't happened yet.
- **First question:** Has this unit actually been checked in and inspected, or is the promise based on the scheduled return time?
- **Data to pull:** Live check-in status, outgoing renter's confirmed return time (if any).

### Damage found at return doesn't appear anywhere on the pre-rental diagram
- **Usually means:** Either genuine new damage from this rental, or the pre-rental inspection was rushed/skipped and never established a baseline.
- **First question:** Was the pickup inspection completed and signed, and does the diagram show this area as clear?
- **Data to pull:** Pickup diagram/photos, return diagram/photos, timestamps on both.

### Deposit or authorization hold collected is below the posted amount for this item class
- **Usually means:** A clerk manually overrode the system default, often to close a hesitant sale faster.
- **First question:** Was the lower amount approved by a manager, or entered without an override reason logged?
- **Data to pull:** Transaction log showing the hold amount entered vs. the item class's posted minimum.

### Customer's age, ID, or payment type doesn't meet the item's policy minimum but the rental proceeded
- **Usually means:** A counter-level override to close the transaction, sometimes without recognizing the policy applied to this specific item class.
- **First question:** What policy minimum applies to this item, and was an exception approved or just skipped?
- **Data to pull:** Item-class policy minimums, ID/payment type actually captured on the contract.

### Same account has 3+ late returns or damage disputes within a rolling 90-day window
- **Usually means:** A pattern worth flagging for account-level review (higher deposit tier, waiver mandatory, or declined future service) rather than treating each incident as isolated.
- **First question:** Has anyone looked at this account's history as a pattern, or is each return being handled independently?
- **Data to pull:** Account-level rental and dispute history for the trailing 90 days.

### A cleaning or fuel fee is charged as a round, eyeballed number instead of the posted flat fee
- **Usually means:** The clerk estimated the fee informally rather than applying the store's schedule, which is much harder to defend if disputed.
- **First question:** What's the posted flat fee for this condition, and does the charged amount match it?
- **Data to pull:** Store fee schedule, actual line-item charged on the invoice.

### A self-storage account is 30+ days delinquent with no default notice yet sent
- **Usually means:** The lien-sale clock hasn't started, extending the store's unrecovered-rent exposure and delaying eventual sale eligibility.
- **First question:** What delinquency-threshold date triggers the first notice at this store, and has that date passed?
- **Data to pull:** Account payment history, delinquency-threshold policy, notice-sent log.

### A high-value item is rented to a first-time walk-in on a debit card with no additional verification
- **Usually means:** Policy calls for a higher hold, additional ID, or a credit-only requirement on this item class that wasn't applied.
- **First question:** Does this item class require credit (not debit) or extra verification for a first-time customer, and was that requirement followed?
- **Data to pull:** Item-class payment-type policy, customer's rental history (first-time vs. repeat).

### A return inspection was completed without the customer present and no timestamped photos exist
- **Usually means:** The inspection can't establish when any damage found actually occurred, weakening the store's position in any dispute.
- **First question:** Was the customer offered the chance to be present for the return walk-around, and were photos taken at the time of return?
- **Data to pull:** Return-inspection log's timestamp and customer-presence field, photo metadata.

### A customer disputes a lien-sale notice claiming it was never received
- **Usually means:** Either a legitimate delivery failure (bad address on file) or a customer contesting a valid notice to delay the sale.
- **First question:** What delivery method and confirmation does the store have for this notice (certified mail receipt, email read receipt)?
- **Data to pull:** Notice-delivery record, address/contact on file at time of sending.
