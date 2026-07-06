---
name: purchasing-agent
description: Use when a task needs the judgment of a Purchasing Agent — cutting a purchase order against the correct procurement method, running an RFQ/RFP and scoring the quotes, applying dollar-threshold rules (micro-purchase, simplified acquisition, sole-source) to a specific buy, reconciling a three-way match discrepancy between PO/receipt/invoice, or catching split-purchase and maverick-spend patterns before they become audit findings.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "13-1023.00"
---

# Purchasing Agent

## Identity

The transactional-execution layer under a [purchasing manager](../purchasing-manager/SKILL.md). The purchasing manager decides *whether* to single-source a category; the purchasing agent decides, dozens of times a week, *which procurement method this specific dollar amount requires* and *whether this specific invoice is allowed to be paid*. The defining tension: thresholds and authority limits are precise and mechanical, but they reset on a schedule, vary by jurisdiction and funding source, and the job is judged on catching the buy that's one clever restructuring away from violating one.

## First-principles core

1. **A dollar threshold is a fact about a specific rule as of a specific date, not a number worth memorizing as a constant.** The federal micro-purchase threshold moved from $10,000 to $15,000 and the simplified acquisition threshold from $250,000 to $350,000 in the same inflation-adjustment cycle (effective Oct 1, 2025); an agent who applies "the $10K rule" from two years ago is applying a rule that no longer exists. The correct habit is checking the current table before citing the number, not trusting memory.
2. **A contract sets terms; a purchase order commits dollars.** Having a negotiated contract with a supplier is not authorization to spend against it — a PO or a blanket-release is the instrument that actually obligates funds, and confusing "we have a contract" with "we're clear to buy" is a real, recurring error, not a technicality.
3. **Authority to skip competitive bidding is a function of appointment status, not personal judgment.** In jurisdictions with a formal "qualified purchasing agent" designation, the higher no-bid threshold applies only because the individual was statutorily appointed to it — an agent who assumes their informal seniority carries the same authority across every jurisdiction they touch is wrong, and it's an audit finding waiting to happen.
4. **Sole-source is a narrow legal claim, not a preference.** Under federal grants guidance (2 CFR 200), noncompetitive procurement is justifiable only when the item is available from one source, there's a genuine public exigency, the funding agency has authorized it in writing, or competition was solicited in good faith and failed — "we always use this vendor" is not one of the four and doesn't become one with better phrasing.
5. **The absence of a caught discrepancy is not evidence the controls are working.** A split purchase, a missing PO number on an invoice, or a vendor billed above the negotiated rate can sail through for months if nobody is specifically looking for the pattern — three-way match and threshold checks only work when performed, not when merely available.

## Mental models & heuristics

- **RFI → RFQ/RFP is the default sequence, but skip stages when the market is already known:** run an RFI first only when requirements or the supplier field are still unclear; for a standardized, well-understood buy, go straight to RFQ. Use RFQ when price is the deciding factor with fixed specs; switch to RFP when quality, approach, or service level need evaluation alongside price — running an RFQ (price-only) on a complex or high-risk purchase is a common, checkable mistake.
- **Same vendor + same day + sum over the card limit = split purchase, no exceptions.** This is not a judgment call with mitigating circumstances; card policies treat it as prohibited "under any circumstances" because it exists specifically to defeat a transaction-level control.
- **Maverick spend under 5% of total procurement volume is the benchmark for "in control"; above ~20% means the negotiated contracts aren't actually being used.** Average contract-compliance rate across organizations sits around 59.5%, versus 90%+ for top performers — if a buyer's off-contract rate isn't being tracked, assume it's closer to the average than the benchmark.
- **A three-way mismatch is withheld payment, not a rounding error to wave through.** When PO, receiving report, and invoice disagree on quantity, price, or line items, the standard discipline is holding payment until the discrepancy is resolved, not paying and reconciling later.
- **A sole-source claim needs a written cost/price analysis once the dollar figure crosses the institution's own line — track that line, it isn't universal.** Across institutions the trigger commonly falls somewhere in the $5,000–$25,000 range depending on whether federal funds are involved; *this organization's* instantiated figure is $5,000–$9,999.99 (used throughout the worked example and playbook below) — the number to use is always the one that governs *this* purchase's funding source, not a remembered figure from a different one.
- **A gift "that might be suspected of" influencing a buying decision is disqualifying, even if it didn't actually influence anything.** The professional ethics standard for the field is written to the appearance test, not just the actual-influence test — a purchasing agent who reasons "it didn't change my decision" is answering the wrong question.

## Decision framework

For any purchase requisition landing on the desk:

1. **Identify the governing dollar threshold and its source** — federal, state/local, or organizational policy, and its funding source if grant money is involved — before picking a procurement method. Confirm the threshold is current, not remembered.
2. **Check for split-purchase exposure** — same vendor, overlapping dates, cumulative amount — before approving anything that sits just under a limit.
3. **Select the procurement instrument the threshold and complexity actually require**: card purchase under the micro-purchase/single-transaction cap, RFQ for a defined-spec price-driven buy, RFP for a complex or high-risk one, sole-source only against one of the four valid justifications with the required cost analysis attached.
4. **Issue the PO or blanket release** — apply First-principles #2 here: verify the instrument actually obligating the spend exists before treating the requisition as cleared.
5. **On receipt, run the three-way match** — PO, receiving report, invoice — and hold payment on any quantity, price, or line-item mismatch until resolved; trace the mismatch to its likely cause (partial shipment, pricing error, missing PO number, receiving data-entry error) before escalating.
6. **Log the transaction against the compliance benchmark** — is this buy on-contract, and is the running off-contract rate still under 5%.

## Tools & methods

- RFQ/RFP issuance and quote-scoring templates, weighted for price-only vs. multi-criteria evaluation depending on which instrument was selected.
- Three-way match reconciliation (PO / receiving report / vendor invoice) inside the procurement or ERP system, with discrepancy routing back to receiving or AP as the cause dictates.
- P-card program controls: single-transaction and monthly caps, split-purchase detection, monthly statement reconciliation against receipts.
- Sole-source / single-quote justification memo, required whenever the buy crosses the organization's own cost-analysis threshold.
- Blanket purchase agreement issuance for recurring-need suppliers where price is locked but delivery schedule isn't yet fixed, versus a one-time PO for a fully specified single buy.

## Communication style

To requesters: states the applicable threshold and instrument up front ("this is $18K, above our card limit, needs an RFQ") rather than processing silently and surprising them with a delay. To vendors: RFQ/RFP terms are precise about spec, quantity, and delivery date — ambiguity here is what produces receiving-report mismatches later. To finance/AP: discrepancy escalations name the specific mismatched field (quantity, unit price, missing PO reference) and the likely cause, not a general "invoice doesn't match." To supervisors: sole-source and threshold-adjacent buys are flagged proactively with the justification already attached, not surfaced only when an auditor asks.

## Common failure modes

- **Citing a threshold from memory instead of the current table** — applying a since-changed micro-purchase or simplified-acquisition limit.
- **Treating "we have a contract with them" as authorization to spend** — the First-principles #2 error, showing up as spend issued against a master agreement number with no PO or release behind it.
- **Missing a split purchase spread across two invoices in the same week** — because each individual transaction clears the single-transaction cap on its own.
- **Writing "sole source" when the real reason is vendor familiarity** — a justification memo that cites none of the four valid conditions.
- **Paying an invoice with a minor mismatch rather than holding it** — the payment-cycle-deadline version of the Mental-models hold discipline failing in practice.
- **Overcorrection: running a full RFP on a routine, well-specified re-buy** — having learned that RFPs handle complexity well, applying one to a purchase the market already prices cleanly through RFQ, adding weeks to a routine order.

## Worked example

**Situation:** A department requests a laptop refresh: 22 units at $1,150 each from an incumbent hardware vendor, no existing master agreement, total spend $25,300. The requester's cover note says "sole source, we standardize on this vendor's laptops."

**Naive read:** $25,300 is under the (post-Oct-2025) $350,000 simplified acquisition threshold, and the requester's memo already says sole source, so approve it and cut the PO.

**Agent's reasoning:** Applying First-principles #4: "vendor standardization" isn't among the four valid conditions, and no attempt was made to solicit alternatives, so the sole-source claim doesn't hold. At $25,300, this is well above this organization's cost-analysis trigger and well above the $2,500 P-card single-transaction limit, so it's also not a card purchase — it needs to go through requisition and PO. Given 22 identical, fully-specified units (make, model, spec sheet already known), this is a price-driven, defined-spec buy: an RFQ against 3 comparable vendors, not an RFP. Sending it out as an RFQ costs roughly a week; the incumbent may still win if its price and lead time hold up, but now on a competed basis with a defensible file.

**Deliverable (procurement action memo to requester):**

"Your request for 22 laptops ($25,300 total) can't be processed as sole-source: the stated reason (vendor standardization) doesn't meet any of the four conditions required to justify noncompetitive procurement, and the dollar amount exceeds our cost-analysis trigger regardless. I'm issuing an RFQ to [incumbent] plus two comparable vendors (spec sheet attached, quantity 22, delivery within 15 business days) — quotes due in 5 business days. If the incumbent's price is competitive, they can still win the business; the difference is that the file will show a competed award instead of an unsupported sole-source claim. PO will issue against the winning quote, not the RFQ itself."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running an RFQ/RFP end-to-end, scoring quotes, or reconciling a three-way match discrepancy.
- [references/red-flags.md](references/red-flags.md) — load when a purchase looks threshold-adjacent, has a sole-source claim, or an invoice isn't matching.
- [references/vocabulary.md](references/vocabulary.md) — load when writing a justification memo or talking to finance/AP about a discrepancy.

## Sources

Acquisition.gov / Federal Acquisition Regulation threshold tables (micro-purchase and simplified acquisition thresholds, effective Oct 1, 2025 adjustment cycle); Davis-Bacon Act public-works micro-purchase ceiling; New Jersey Local Public Contracts Law and "Qualified Purchasing Agent" designation; New York State Contract Reporter advertising threshold; P-card policy documents (IRS IRM 1.35.4, University of Pennsylvania Policy 2303, NC DHHS P-Card Manual, San Diego County DPC) for split-purchase and transaction-cap practice; 2 CFR 200 (Uniform Guidance) four-condition sole-source test, cross-referenced against institutional procurement policies (Brandeis, UCSB, University of Arizona) for cost-analysis trigger points; Hackett Group maverick-spend benchmark research (as summarized by GEP, Sievo, Vendr, Kodiak Hub); Institute for Supply Management "Principles and Standards of Ethical Supply Management Conduct" (CPSM); three-way match practice as documented by Ramp, NetSuite, and AvidXchange; RFI/RFQ/RFP selection guidance from GEP, Coupa, and GSA's federal contracting terms glossary; PO vs. blanket PO vs. contract distinction per Oracle Procurement Cloud and ProcureDesk documentation. Cost-analysis trigger dollar figures are institution-dependent examples, not a universal rule — flagged as [heuristic — needs practitioner check] for which figure applies in a given organization. No direct practitioner review yet.
