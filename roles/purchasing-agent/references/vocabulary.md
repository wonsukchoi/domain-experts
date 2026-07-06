# Vocabulary — terms of art generalists misuse

Not a glossary of lookup-able definitions. These are terms a generalist has heard and will use confidently in the wrong situation — each entry exists because the misuse, not the definition, is the recurring failure.

**Blanket purchase agreement (BPA) / blanket release**
A standing agreement that locks price and terms with a vendor for recurring, not-yet-scheduled needs, drawn down by individual releases as the need arises — one of the three instruments distinguished in the "Blanket PO vs. one-time PO vs. contract" entry below.
- *In use:* "We have a BPA with this office-supply vendor at $4.50/case — cut a release for this month's order, not a new PO from scratch."
- *Misuse:* Citing the BPA number on an invoice with no release/line-item tied to it is the contract-as-authorization error (SKILL.md First-principles #2) applied to this specific instrument.

**Simplified acquisition threshold (SAT)**
The federal dollar ceiling below which agencies may use streamlined, less-than-full-competition procurement procedures instead of sealed bidding or full negotiated procurement.
- *In use:* "This buy is $180K — under the $350K SAT, so we can use simplified procedures instead of a formal solicitation."
- *Misuse:* Treated as a fixed number instead of a value that resets on a schedule (current figure and adjustment history in SKILL.md First-principles #1). Citing last cycle's figure from memory is applying a rule that no longer exists.

**Micro-purchase threshold**
The dollar ceiling below which a purchase can be made without soliciting competitive quotes at all — the lowest tier of procurement, typically via card.
- *In use:* "$8,400 is under the $15,000 micro-purchase threshold, so a P-card buy with no quotes is fine."
- *Misuse:* Conflated with the P-card's own single-transaction limit, which is a separate, organization-set number (often much lower, e.g. $2,500) layered underneath the federal threshold. A buy can be under the micro-purchase threshold and still be barred by the card program's own cap — checking one and not the other is a common gap.

**Sole source (noncompetitive procurement)**
A procurement made without competitive bidding, justifiable only under the four conditions enumerated in SKILL.md First-principles #4 — not a label for "we prefer this vendor."
- *In use:* "This doesn't qualify as sole source — vendor standardization isn't one of the four conditions, so it needs to go out for competitive quotes."
- *Misuse:* The single most common misuse in the role: writing "sole source" on a requisition to describe vendor familiarity, past relationship, or convenience. The justification memo doesn't become valid with better phrasing — it needs an actual condition checked and evidenced.

**Three-way match**
The reconciliation of purchase order, receiving report, and vendor invoice before payment is released — checking quantity, unit price, and line items agree across all three documents.
- *In use:* "Three-way match failed on unit price — PO says $1,150, invoice says $1,175 — hold payment and route to AP."
- *Misuse:* Generalists assume a "close enough" match (off by a few dollars, or a missing PO reference) is a rounding error to wave through under payment-cycle deadline pressure — the hold-until-resolved discipline covered in SKILL.md's Mental models.

**Maverick spend (off-contract spend)**
Purchases made outside an existing negotiated contract, even when the purchase itself is otherwise properly authorized and paid.
- *In use:* "Off-contract spend in office supplies is running 28% this quarter — that's a program-level compliance finding, not a one-off."
- *Misuse:* Assumed to mean something improper or unauthorized happened. It doesn't necessarily — a fully legitimate, correctly-approved PO can still be maverick spend if it bypasses a contract that was available and should have been used. The metric is about contract-utilization discipline, not about catching fraud.

**Split purchase**
Breaking what should be one purchase into multiple smaller transactions, same vendor and overlapping dates, specifically to keep each one under a per-transaction dollar cap.
- *In use:* "Two invoices from the same vendor, same week, summing to $4,550 against a $2,500 card limit — that's a split purchase, no exception, regardless of whether it was intentional."
- *Misuse:* Generalists look for evidence of *intent* to game the limit before flagging it. Per SKILL.md's Mental models, the rule doesn't require proving intent — same vendor, overlapping timeframe, cumulative sum over the cap gets flagged either way.

**RFQ vs. RFP**
Request for Quotation (price is the only variable, spec is fully fixed) versus Request for Proposal (quality, technical approach, or service level must be evaluated alongside price).
- *In use:* "22 identical laptops, make and model already specified — that's an RFQ, not an RFP; there's nothing to evaluate but price and lead time."
- *Misuse:* Used interchangeably as "the bid process" by generalists. Running an RFQ on a purchase with no fixed spec produces quotes that aren't actually comparable (vendors quote different things); running a full RFP on a routine, well-specified re-buy adds weeks of unnecessary evaluation to a purchase the market already prices cleanly.

**Qualified purchasing agent (QPA)**
A formal statutory designation (jurisdiction-specific, e.g. under certain state local-contracts laws) that grants an individual — not a role or seniority level — an elevated no-bid purchase authority.
- *In use:* "Is the approving agent formally designated QPA under this jurisdiction's statute, or is that being assumed from their title?"
- *Misuse:* Assumed to transfer with seniority or job title (see SKILL.md First-principles #3) — an informal "I've been doing this 15 years" does not carry the statutory weight of an actual QPA appointment in that specific jurisdiction.

**P-card single-transaction limit vs. monthly cap**
Two distinct P-card controls: a per-transaction dollar ceiling (above which the card is declined/prohibited by policy) and a separate cumulative monthly ceiling (above which the card is suspended pending review).
- *In use:* "This is $2,300 — under the $2,500 single-transaction limit — but it's her ninth card purchase this month, check the monthly cap before approving another."
- *Misuse:* Treated as one number. A transaction can individually clear the single-transaction limit while still tripping the monthly cap, and clearing both still doesn't clear split-purchase exposure if the same-vendor/same-period pattern is present.

**Cost/price analysis**
A written analysis justifying that a quoted or sole-sourced price is fair and reasonable, required once a purchase crosses an organization- or funding-source-specific dollar trigger — separate from, and required in addition to, the sole-source justification itself.
- *In use:* "At $25,300 this is well above our $9,999.99 cost-analysis trigger — the sole-source memo alone isn't sufficient, a written price analysis has to be attached too."
- *Misuse:* Assumed to be the same document as the sole-source justification, or assumed to have one universal trigger dollar amount — the trigger is institution- and funding-source-dependent (see SKILL.md's Mental models for the general range vs. this organization's instantiated figure). Using a remembered figure from a different organization or grant is applying the wrong rule to this purchase.

**Blanket PO vs. one-time PO vs. contract**
Three distinct instruments: a contract sets negotiated terms, a one-time PO obligates funds for a single fully-specified buy, and a blanket PO obligates funds against a recurring need where price is locked but exact delivery timing isn't yet fixed. (See SKILL.md First-principles #2 for why only the PO/release side of this actually commits dollars.)
- *In use:* "We don't need a new one-time PO — issue a release against the existing blanket PO, the price and vendor are already locked."
- *Misuse:* Generalists use "PO" and "contract" interchangeably, picking the wrong one of the three when scoping a new buy — e.g. drafting a fresh one-time PO for a need a blanket release already covers, or vice versa.

**Appearance-of-influence standard**
The ethics test applied to gifts, meals, or hospitality from a vendor — judged on whether a reasonable outside observer could see it as *capable* of influencing the award, not on whether it actually changed the buyer's decision.
- *In use:* "Decline the dinner invitation while their RFP is under evaluation — it doesn't matter that it wouldn't change my scoring, it fails the appearance test."
- *Misuse:* Generalists defend accepting a gift by reasoning "it didn't actually affect my decision" — the wrong-question error named in SKILL.md's Mental models (the ISM/CPSM standard is written to appearance, not actual effect).
