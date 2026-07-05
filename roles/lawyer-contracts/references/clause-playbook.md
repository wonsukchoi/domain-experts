# Clause Playbook — High-Stakes Terms in Commercial Agreements

US commercial context. "Buyer" = customer/licensee side; "Vendor" = supplier/licensor side. Positions assume a mid-market B2B deal (roughly $50k–$2M/yr); scale ambition up or down with deal size. Every fallback ladder is ordered by preference — take the highest rung the counterparty will give you.

---

## 1. Limitation of Liability (LoL)

**Controls:** the maximum check either party ever writes, and which damage types are recoverable at all. The single most negotiated clause in commercial contracts, and the one that decides what a lawsuit is worth before it's filed.

**Market positions:**
- *Vendor-side:* cap at 6–12 months' fees, mutual, all consequential damages waived, no carve-outs (or carve-outs only for customer payment obligations).
- *Buyer-side:* 12 months' fees as the general cap; carve-outs (uncapped) for indemnification obligations, breach of confidentiality, gross negligence/willful misconduct; super-cap of 2–3x fees for data-protection breaches; breach-response costs deemed direct damages.

**Typical range:** general cap 6–24 months of fees (12 is the overwhelming landing zone). Data-breach super-cap 2–5x fees or a fixed dollar amount ($2M–$10M common where the vendor holds significant PII); often tied to the vendor's cyber-insurance limits. Fraud and willful misconduct escape caps as a matter of law in most states — but draft it anyway.

**Fallbacks (buyer-side):**
1. 12-month cap + uncapped indemnity/confidentiality carve-outs + 3x data-breach super-cap.
2. Same but 2x super-cap, or super-cap covers confidentiality only.
3. 12-month cap, carve-outs limited to indemnification and willful misconduct, breach-response-costs-are-direct-damages sentence.
4. Accept vendor cap but require cyber insurance at a limit that covers the realistic exposure, with certificate of insurance and additional-insured status.

**Never:** a cap that also caps the indemnification obligation for third-party IP claims (you're buying their product; their IP problem shouldn't become your bill), or a unilateral cap (vendor capped, customer uncapped).

---

## 2. Indemnification

**Controls:** who defends and pays when a third party sues. Distinct from direct liability between the parties — this is about outsiders (patent trolls, injured plaintiffs, data-breach class actions, regulators via fines).

**Market positions:**
- *Vendor gives:* IP infringement indemnity (defend + pay) for the product as delivered — this is table stakes; a vendor refusing it is telling you something.
- *Buyer gives:* indemnity for its own content/data and its use of the product outside the license scope.
- Both: bodily injury/property damage from negligence where relevant.

**Typical range:** the fight is over (a) whether the IP indemnity has exclusions that swallow it (combinations, modifications, failure to update — narrow these to combinations *required* by vendor documentation), (b) whether data-breach indemnity exists at all (buyer-side push where vendor processes PII; vendors resist hard), (c) control of defense and settlement (indemnitor controls defense, but no settlement admitting fault or imposing obligations on indemnitee without consent).

**Fallbacks (buyer-side, IP indemnity):**
1. Full defend/indemnify/hold harmless, no cap, remedies include procure-right-to-use, replace, or refund.
2. Indemnity subject to the super-cap rather than uncapped.
3. Indemnity capped but with a refund-plus-transition remedy if the product is enjoined.

**Never:** an indemnity you *give* that covers the counterparty's own negligence, or one triggered by mere allegation with no defense-control or mitigation duties. Watch for "hold harmless" without "defend" — you may end up reimbursed years later instead of defended now.

---

## 3. IP Ownership / License

**Controls:** who owns what's created, and what each side can actually do with it after the relationship ends.

**Market positions:**
- *SaaS:* vendor owns the platform; customer owns its data (say so expressly); customer gets a subscription license. Vendor gets a limited license to process customer data to provide the service — resist "improve our services" language broad enough to cover training models on your data without limits.
- *Services/development:* customer default is work-for-hire plus present-tense assignment ("Vendor hereby assigns") of deliverables; vendor default is vendor-owns-with-broad-license-to-customer. Landing zone: customer owns bespoke deliverables; vendor retains pre-existing IP and generic tools with a perpetual license to customer for anything embedded in deliverables.

**Typical range:** the real negotiation is the residuals/background-IP boundary and feedback clauses (vendor takes a perpetual license to your feedback — fine if narrow, dangerous if "feedback" is defined to include your data or requirements).

**Fallbacks (customer-side, development work):**
1. Assignment of all deliverables + license to embedded background IP.
2. Joint ownership of deliverables (usually a trap — either party can license to your competitor; avoid unless you understand this).
3. Broad perpetual, irrevocable, sublicensable license instead of ownership.

**Never:** "work made for hire" language alone with no backup assignment (most software isn't a statutory work-for-hire category, so the label can silently fail — always pair with "and hereby assigns"), or a vendor license to customer data that survives termination without deletion obligations.

---

## 4. Termination

**Controls:** the real leverage during the relationship — who can leave, how fast, and what it costs.

**Market positions:**
- Termination for material breach with 30-day cure period: universal, mutual.
- Termination for convenience: buyers want it (30–90 days' notice); vendors resist or price it (early-termination fee, forfeit prepaid fees).
- Insolvency/bankruptcy triggers: standard but weakly enforceable against a US debtor in bankruptcy (ipso facto clauses are largely unenforceable under §365(e) — include anyway for out-of-court workouts).

**Typical range:** cure periods 15–60 days (immediate for confidentiality/IP breach and non-payment beyond a grace period). Convenience-termination fees range from nothing to the remaining contract value; midpoint is prepaid-fees-forfeited or a sliding scale.

**Post-termination tail — negotiate these up front, they're unnegotiable later:** data return/export in a usable format within 30–60 days then certified deletion; transition assistance (rate-carded, 30–90 days); wind-down license for any embedded vendor IP; survival clause listing exactly which sections survive.

**Fallbacks (buyer-side):**
1. Convenience termination on 60 days' notice, pro-rated refund of prepaid fees.
2. Convenience termination, no refund but no penalty.
3. No convenience right, but shorter initial term / no auto-renewal, and termination right on change of control of vendor to a competitor.

**Never:** a contract with no exit for persistent SLA failure, or auto-renewal with a renewal-notice window shorter than 30 days (calendar it regardless).

---

## 5. Warranties

**Controls:** what the vendor promises the product/service actually is, and what the remedy is when it isn't.

**Market positions:**
- *Vendor-side:* material conformance to documentation, professional/workmanlike services, plus a full disclaimer of implied warranties (merchantability, fitness for particular purpose) in ALL CAPS — the UCC §2-316 conspicuousness requirement is why.
- *Buyer-side:* add non-infringement, compliance with law, no malware/open-source-contamination (for delivered code), and don't let the exclusive remedy for warranty breach be "re-perform the services" alone.

**Typical range:** warranty period 30–90 days for deliverables (services), continuous for SaaS conformance. The trap is the *exclusive remedy* clause: repair/replace/refund as sole remedy is fine until the remedy "fails of its essential purpose" (UCC §2-719(2)) — buyer-side, make sure a refund path exists.

**Never (buyer-side):** accepting "AS IS" on paid commercial software, or a warranty whose only remedy is re-performance by the same team that failed.

---

## 6. Confidentiality

**Controls:** what each side can do with the other's information, and for how long.

**Market positions:** mutual, definition covering information reasonably understood as confidential (not only marked documents — marking requirements are where confidentiality obligations go to die in practice), standard exclusions (public, independently developed, rightfully received, already known), compelled-disclosure procedure with notice.

**Typical range:** term 2–5 years post-disclosure or post-termination; trade secrets protected as long as they remain trade secrets (say so expressly — a fixed term can arguably *waive* trade-secret status after expiry). Residuals clauses (counterparty can use what its people remember) are a vendor ask; resist or narrow to general know-how excluding your data and roadmap.

**Never:** one-way confidentiality in a two-way exchange, or a residuals clause broad enough to be a license to your trade secrets.

---

## 7. Data Protection

**Controls:** what the vendor may do with personal data, security obligations, breach notification, and who pays when it goes wrong.

**Market positions:** where personal data is processed, attach a DPA. US state laws (CPRA, Colorado, Virginia, et al.) require processor-contract terms; GDPR Article 28 requires more if EU data is in scope — jurisdiction matters enormously here. Baseline asks: processing only on documented instructions, no sale/sharing, subprocessor flow-down and list with objection right, security program referencing a standard (SOC 2 Type II, ISO 27001), breach notification without undue delay and in any case within 48–72 hours of confirmation, audit rights (accept SOC 2 report + questionnaire in lieu of on-site for smaller deals), deletion/return on termination.

**Typical range:** the money fight lives in the LoL clause (super-cap, §1 above) and in who pays breach-response costs. Landing zone: vendor pays notification and remediation costs for breaches caused by vendor's failure to meet its security obligations.

**Never:** "vendor may use customer data to improve its products" without an aggregation/de-identification limit, or breach notification measured from vendor's *completion of investigation* rather than discovery/confirmation.

---

## 8. Assignment

**Controls:** whether you can end up in a contract with someone you never chose.

**Market positions:** no assignment without consent, carve-out for assignment to an affiliate or in connection with a merger/sale of substantially all assets. Buyer-side refinement: the M&A carve-out should *exclude* assignment to your direct competitor, or give you a termination right on such a change of control.

**Remember the default:** absent this clause, contracts are freely assignable (UCC §2-210 and common law), with narrow exceptions for personal-services contracts and material changes to the obligor's duty. Silence here is a real position — usually the wrong one.

**Never:** an anti-assignment clause that binds you but exempts them entirely, without at least the affiliate/M&A carve-out being mutual.

---

## 9. Governing Law / Dispute Resolution

**Controls:** which state's defaults fill every gap, and the forum where enforcement actually happens.

**Market positions:** each side proposes home state; the classic neutrals are Delaware and New York (both enforce choice-of-law in commercial deals and have deep commercial case law; NY General Obligations Law §5-1401 allows choosing NY law for deals ≥$250k even without other NY contacts). Arbitration (AAA/JAMS) vs. courts is a genuine trade: arbitration is private and final but has no meaningful appeal and costs more up front; carve out injunctive relief for IP/confidentiality breaches either way.

**Typical range:** if you can't win governing law, prioritize (in order): venue you can live with > jury waiver > prevailing-party fees (double-edged — shifts settlement dynamics; skip it if you're more likely to be plaintiff-shy) > shortened contractual limitations period (watch: some states cap how short).

**Never:** counterparty's home law *and* mandatory arbitration seated in their headquarters city *and* a one-sided fee-shifting clause, on a deal big enough to ever litigate. That combination is a designed-in enforcement barrier — see "every right is worth what it costs to enforce."

---

## 10. Force Majeure

**Controls:** who eats the loss when performance is blocked by events outside anyone's control.

**Market positions:** defined event list (acts of God, war, terrorism, epidemics, government action) plus a catch-all "beyond reasonable control"; excused performance during the event; notice and mitigation duties. Post-2020, epidemics/pandemics are explicitly listed or explicitly excluded — silence is now a drafting choice courts notice.

**Buyer-side essentials:** payment obligations are *not* excused by force majeure; vendor FM doesn't suspend SLA credits indefinitely; termination right if the FM event persists 30–90 days.

**Never:** an FM clause covering "labor shortages" or "supplier failure" for a vendor whose entire job is managing labor and suppliers — that's a performance excuse dressed as boilerplate. FM is construed narrowly in US courts (unlike some civil-law systems with statutory hardship doctrines); don't rely on it as a substitute for a real termination right.

---

## 11. Non-Solicitation (of Employees)

**Controls:** whether the counterparty can hire away the team that serviced your account.

**Market positions:** mutual non-solicit of employees *directly involved in the engagement*, 12 months post-termination, with the standard carve-out for general advertisements not targeted at the individual and responses thereto.

**Typical range:** 6–24 months; scope from "any employee" (overbroad — resist) down to "personnel who worked on the engagement" (right-sized). Note jurisdiction: California will not enforce employee no-hire terms in most B2B contexts and treats broad restraints as void under Bus. & Prof. Code §16600 — a nationwide company should assume the clause is worth little against a California counterparty.

**Fallbacks:** 1. Engagement-team-only, 12 months, general-ads carve-out. 2. Add a buy-out fee (e.g., 50% of first-year comp) as the exclusive remedy instead of an injunction fight. 3. Drop it — it's rarely worth deal friction.

**Never:** a no-*hire* clause (vs. no-solicit) without a general-ads carve-out — it turns an employee's own job search into your breach.
