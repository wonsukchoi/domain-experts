---
country: KR
regulator: Korea Financial Intelligence Unit (KoFIU), under the Financial Services Commission
as_of: 2026-07-07
---

# New Accounts Clerk — Korea Overlay

Delta only. Everything in the US-baseline SKILL.md not contradicted here still applies (signature card scope, product-fit judgment, escalation discipline).

## Legal basis differs from CIP/OFAC

- **Real-Name Financial Transaction Act** (금융실명거래 및 비밀보장에 관한 법률, 1993) is the foundational statute, not a CIP-equivalent bolt-on: every account, at any amount, must be opened under the customer's real name verified against a government-issued ID (resident registration card, alien registration card for foreign nationals, or passport for non-residents). There is no de minimis exception — a KRW 1 account opening triggers the same identity-verification bar as a KRW 100M one.
- **Customer due diligence (CDD)** is mandated under Article 5-2 of the Act on Reporting and Use of Certain Financial Transaction Information (특정 금융거래정보의 보고 및 이용 등에 관한 법률, the "FTRA") — the FATF-aligned AML statute, functionally Korea's CIP/BSA equivalent. Enhanced due diligence (EDD) is required, not discretionary, when the customer's purpose for opening the account cannot be clearly established.

## Thresholds that differ from US baseline

- **Currency Transaction Report (CTR) trigger: KRW 10,000,000** (roughly USD 7,500 at time of writing) in cash transactions within a single business day, aggregated across same-customer transactions at the branch — lower than the US BSA's USD 10,000 CTR threshold, and reported to KoFIU, not FinCEN.
- **Beneficial ownership disclosure for legal-entity accounts: 25% threshold**, same cascading logic as the US CDD Rule's beneficial ownership test (largest individual owner ≥25% direct or indirect equity/voting control, or the individual with actual control if no one crosses 25%) — but codified under FTRA Article 5-2 rather than 31 CFR 1010.230, and the beneficial-owner declaration form is KoFIU's standard 실제소유자 확인서, not a FinCEN certification form.
- **Suspicious Transaction Report (STR)** has no minimum dollar threshold — filed on suspicion regardless of amount, same principle as a US SAR, filed to KoFIU rather than FinCEN.

## What doesn't carry over

- There is no OFAC-equivalent single sanctions list to screen against by default — Korea maintains its own sanctions list under the Foreign Trade Act, administered jointly by the Ministry of Foreign Affairs and the Bank of Korea, and a clerk opening accounts for a bank with US-nexus exposure (US correspondent banking relationship, USD-denominated accounts) screens against both lists, not one.
- Non-resident foreign nationals opening accounts face additional restrictions under the Foreign Exchange Transactions Act (외국환거래법) that have no US CIP analogue — certain account types (e.g., high-value time deposits) require Bank of Korea reporting above statutory thresholds.

Laws cited current as of 2026-07-07 — verify against Korea Financial Intelligence Unit (KoFIU), under the Financial Services Commission before acting; not legal advice.
