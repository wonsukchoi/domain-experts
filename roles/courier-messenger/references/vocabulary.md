# Courier and Messenger — Vocabulary

### Chain of custody
A documented, unbroken record of who held an item and when, from pickup to final delivery, used to prove the item wasn't tampered with or misdelivered.
**In use:** "This is a specimen run — I need a signed hand-off log at every transfer point, not just pickup and delivery."
**Common misuse:** Treating it as only relevant to law-enforcement evidence; it applies to any item where proof of unbroken possession matters (medical specimens, financial instruments, notarized documents).

### Proof of delivery (POD)
The evidence captured at the point of delivery — signature, photo, barcode scan, or witnessed-refusal note — that confirms what happened and when.
**In use:** "The manifest calls for a named-recipient signature on this one, not just a doorstep photo."
**Common misuse:** Assuming any delivery confirmation is equivalent; a photo-at-door and a named signature carry different evidentiary weight and aren't interchangeable substitutes.

### Substituted service
A legally defined alternative method of delivering process (like a subpoena) when the named recipient can't be personally served, following specific statutory rules (e.g., leaving with a co-resident of suitable age, then mailing a copy).
**In use:** "Personal service failed twice — check whether this jurisdiction allows substituted service before a third attempt."
**Common misuse:** Treating "leaving it with whoever answered the door" as automatically valid; substituted service has specific statutory requirements that vary by jurisdiction and must be followed exactly.

### Earliest-deadline-first (EDD) sequencing
A route-ordering method that sequences stops by which deadline is soonest, rather than by shortest total distance.
**In use:** "Nearest-neighbor put B before A, but A's window closes first — resequence to EDD."
**Common misuse:** Assuming the shortest-distance route is always the best route; it only holds when no stop has a binding time window.

### Delivery window
The time range within which an item must arrive to satisfy the sender's or recipient's requirement.
**In use:** "Stop C's window is 9:40 to 10:10 — arriving at 9:35 means we wait, not that we're ahead."
**Common misuse:** Treating a window's opening time as optional and the closing time as the only thing that matters; early arrival outside the window can be a problem too (recipient not ready, facility not open).

### Cold chain
An unbroken sequence of temperature-controlled handling and storage required for temperature-sensitive items (many medical specimens, some pharmaceuticals).
**In use:** "This transport box is only rated for 4 hours at spec temperature — that's the real deadline, not the recipient's stated window."
**Common misuse:** Focusing only on the delivery-window deadline and missing that the item's own stability window can be the binding constraint.

### Manifest
The document (paper or digital) listing every item on a route, its destination, proof-of-delivery requirement, and any special handling or fallback instructions.
**In use:** "The manifest doesn't authorize leaving this with a neighbor — hold it and flag dispatch."
**Common misuse:** Treating the manifest as just an address list; it's the authoritative source for what proof and what fallback each item requires.

### Delivery exception
A delivery attempt that didn't result in standard completion — refused, no-answer, wrong-address, damaged, or access-denied.
**In use:** "Log this as a no-answer exception, not a failed delivery — there's a difference in how dispatch routes the reattempt."
**Common misuse:** Lumping all non-standard outcomes into one vague "couldn't deliver" note instead of the specific exception type, which determines the correct fallback.

### Signature-required
A delivery classification requiring a named or authorized recipient's physical or electronic signature as proof of delivery.
**In use:** "This is signature-required — a photo at the door doesn't satisfy it even if someone's clearly home."
**Common misuse:** Treating "someone was home and accepted it" as equivalent to a captured signature; the requirement is the specific proof artifact, not just physical possession changing hands.

### Time-window-constrained routing
A route-optimization problem where stops must be visited within specified time windows, not just in the shortest total distance.
**In use:** "This isn't a traveling-salesman distance problem — it's time-window-constrained, so deadline order matters more than mileage."
**Common misuse:** Applying pure distance-minimization logic (like generic GPS routing) to a problem where hard deadlines, not total distance, are the binding constraint.

### Access-denied exception
A delivery attempt blocked by a physical barrier (locked gate, secured building, gated community) rather than recipient unavailability.
**In use:** "Log this as access-denied with a photo of the locked gate — it's a different fallback path than no-answer."
**Common misuse:** Conflating access-denied with no-answer; the former often requires a different resolution (buzzer code, building management contact) than simply reattempting later.

### Custody gap
An undocumented period where an item's location or handler isn't recorded in the chain-of-custody log.
**In use:** "There's a 40-minute custody gap between pickup and the first log entry — that undermines the whole chain."
**Common misuse:** Assuming a short, well-intentioned gap ("just grabbed lunch, item was in the locked trunk") doesn't matter; for chain-of-custody purposes, an undocumented gap is a gap regardless of actual risk.
