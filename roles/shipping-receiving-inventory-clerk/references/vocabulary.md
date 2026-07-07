# Shipping, Receiving, and Inventory Clerk — Vocabulary

### Cycle count
A recurring partial physical count of inventory (a subset of SKUs or locations counted on a rotating schedule) used to verify system accuracy without a full facility shutdown.
**In use:** "BRK-1180 is due for its cycle count this week per the A-item schedule."
**Common misuse:** treating "cycle count" as a synonym for "spot check" — a real cycle count follows a defined schedule and classification (ABC), not an ad hoc "let's check this one."

### ABC classification
A method of grouping SKUs by value/velocity (A = high, C = low) to set differentiated cycle-count frequency and control intensity.
**In use:** "It's an A-item, so it gets counted monthly, not the C-item quarterly cadence."
**Common misuse:** assuming ABC classification changes how carefully a SKU is counted rather than how often — the counting procedure itself doesn't change by class.

### Put-away
The transaction and physical act of moving received goods from the receiving dock to their storage bin location, recorded in the system.
**In use:** "The put-away task for that receipt is still open — nothing's been shelved yet."
**Common misuse:** using "put-away" to mean any inventory movement — it specifically refers to the receiving-to-storage step, not a bin-to-bin transfer or a pick.

### Quarantine
A physical and system status holding discrepant, damaged, or unverified stock separate from sellable/usable inventory until the discrepancy is resolved.
**In use:** "Those six units are quarantined pending the vendor's damage-claim response."
**Common misuse:** treating quarantine as optional paperwork rather than a physical separation — quarantined stock that stays in the normal put-away flow defeats the purpose.

### Discrepancy tagging
The documentation step that records the specific nature of a receiving or count mismatch (short, over, damaged, wrong item) at the point it's found.
**In use:** "Tag it as a short-ship, not a damage issue — the carton was intact, the quantity was just wrong."
**Common misuse:** using a generic "discrepancy" tag instead of the specific category, which loses the information purchasing needs to resolve it correctly (a short-ship and a damage claim go to different resolution paths).

### Pick list
The system-generated list of items, quantities, and locations an outbound order requires a picker to pull from inventory.
**In use:** "The pick list says two units of Adapter C — don't pack three just because three were pulled."
**Common misuse:** conflating the pick list with the packing slip — the pick list is the internal instruction for what to pull; the packing slip (for outbound) is the customer-facing document of what's in the box, and they should match but are generated at different steps.

### Bill of lading (BOL)
The carrier's shipping document accompanying a freight shipment, listing carton count and often condition at time of carrier pickup/delivery — distinct from the vendor's packing slip.
**In use:** "Sign the BOL for carton count only — note any visible damage before signing, since a clean signature closes the carrier damage-claim window."
**Common misuse:** treating the BOL and the packing slip as the same document — the BOL is the carrier's record of what they transported; the packing slip is the vendor's record of what's inside the cartons.

### Short-ship / over-ship
A receipt where the physical quantity received is less than (short) or more than (over) what the packing slip or PO specifies.
**In use:** "That's a short-ship of 12 units — accept what arrived and flag the remainder for backorder."
**Common misuse:** using "short-ship" to describe any quantity discrepancy, including counting errors on the receiving end — the term specifically means the vendor sent less than documented, not that the receiving count was wrong.

### Case-pack tolerance
A vendor- or facility-stated allowable variance in a shipment's unit count, usually expressed per case or per line, that doesn't trigger a formal discrepancy.
**In use:** "One unit off on a 500-unit case is inside the case-pack tolerance — accept it, no need to flag."
**Common misuse:** applying a blanket tolerance across all vendors/SKUs rather than checking the specific stated tolerance, which varies.

### Location transfer
A system transaction moving inventory from one bin/location to another without a change in total on-hand quantity.
**In use:** "That variance wasn't shrinkage — it was an unrecorded location transfer to the overflow shelf."
**Common misuse:** treating any bin-to-bin movement as automatically documented — a location transfer only shows up in the transaction history if someone actually recorded it, which is exactly the gap that causes many cycle-count "mysteries."

### Lot/batch tracking
A system capability to trace a specific unit of inventory back to its receiving date/shipment, used to isolate discrepant stock after it's been put away.
**In use:** "If lot tracking is enabled, we can still pull just the units from the disputed receipt instead of recounting the whole bin."
**Common misuse:** assuming lot tracking exists by default — many facilities don't track at that granularity, which is exactly why catching a discrepancy before put-away matters so much more when it's absent.

### Physical inventory
A full, facility-wide count of all on-hand inventory, typically done annually, as distinct from the rolling partial coverage of cycle counting.
**In use:** "Cycle counts catch most drift during the year, but physical inventory is the backstop that catches what cycle counts miss."
**Common misuse:** treating physical inventory results as more "true" than cycle counts by default — a rushed annual count with less careful procedure can introduce its own errors, and a clean cycle-count history on a SKU that shows a big physical-inventory variance is itself worth investigating, not just accepting.

### Discrepancy investigation vs. adjustment
The distinction between diagnosing why a system-vs-physical variance occurred (investigation) and simply changing the system number to match the physical count (adjustment).
**In use:** "Don't just adjust it — investigate first, or the same variance shows up again next cycle."
**Common misuse:** using "resolved" to mean the numbers now match, when an unexplained adjustment with no root cause found isn't resolved, it's just reset to recur.
