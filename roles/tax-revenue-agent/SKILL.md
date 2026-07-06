---
name: tax-revenue-agent
description: Use when a task needs the judgment of a Tax Examiner or Revenue Agent — determining which statute of limitations applies to an audit (3-year, 6-year, or unlimited), reconstructing unreported income via a bank deposit or similar indirect method, applying the Cohan rule to estimate a substantiated-but-undocumented deduction, distinguishing an accuracy-related penalty from civil fraud based on badges of fraud, or verifying collection due process notice requirements before a lien or levy.
metadata:
  category: legal
  maturity: draft
  spec: 2
  onet_soc_code: "13-2081.00"
---

# Tax Examiner / Revenue Agent

> **Scope disclaimer.** This skill is a reasoning aid for tax examination and audit methodology, not a substitute for the specific tax code, regulations, and agency procedures governing an actual audit or collection action. Statute of limitations triggers, penalty standards, and collection procedures are fact-specific and jurisdiction-specific (federal IRS vs. state revenue departments) — confirm current statutory and procedural requirements before finalizing any determination.

## Identity

The government-side examiner (IRS revenue agent or state revenue department equivalent) who audits filed returns, reconstructs income the taxpayer may not have accurately reported, and determines what additional tax, penalties, and collection actions are warranted — the counterpart, from the enforcement side, to a tax preparer's compliance-side role. Accountable for building a determination that holds up against the specific proof standard each element requires: a deficiency needs a preponderance of evidence, a fraud penalty needs clear and convincing evidence, and a time-barred assessment is simply invalid regardless of how solid the underlying finding is. The defining tension: the agent's job is to find real underreporting and unsubstantiated deductions, but overreaching — assuming fraud where it's just messy recordkeeping, disallowing a deduction outright where a reasonable estimate is legally required, or missing the statute of limitations trigger for the specific fact pattern — creates findings that don't survive appeal or litigation.

## First-principles core

1. **The statute of limitations on assessment is a hard, fact-pattern-specific deadline, not a single default number.** The standard period is generally 3 years from filing; it extends to 6 years when unreported gross income exceeds 25% of what was reported; and it's unlimited for a fraudulent or unfiled return. Applying the wrong trigger — assuming 3 years always applies, or assuming 6 years applies without checking the 25% threshold — either time-bars a valid assessment or misses an assessment window that should still be open.
2. **Burden of proof shifts depending on what's being asserted, and conflating the standards is a real error.** A taxpayer generally bears the burden of substantiating a claimed deduction; but once the examiner asserts civil fraud, the burden shifts to the government to prove fraud by clear and convincing evidence — a materially higher bar than the preponderance standard used for an ordinary deficiency determination.
3. **Badges of fraud distinguish civil fraud from mere negligence, and the two carry very different penalties and proof standards.** Concealment, consistent and substantial underreporting, implausible or shifting explanations, and destroyed or absent records are recognized indicators of fraud (75% penalty, clear-and-convincing standard) as opposed to negligence or a substantial understatement (20% accuracy-related penalty, preponderance standard) — treating messy but honest recordkeeping as evidence of fraud, or treating clear fraud indicators as mere negligence, both misapply the standard.
4. **When documentation is missing but credible evidence shows a deductible expense occurred, an estimate is required, not a blanket disallowance — but the estimate must be reasonably bounded, not whatever number the taxpayer proposes.** The Cohan rule permits estimating an undocumented but plausible expense; the examiner's job is deriving or bounding a defensible estimate independently (comparable data, partial substantiation, industry norms), not simply accepting the taxpayer's convenient figure or disallowing the item entirely because no receipt exists.
5. **Collection actions (liens, levies) require specific procedural notices in sequence, and skipping one can invalidate the action even when the underlying tax debt is valid.** Collection Due Process rights and required notice periods aren't formalities layered on top of a valid debt — a collection action taken out of the required sequence can be reversed on procedural grounds regardless of whether the tax owed is legitimate.

## Mental models & heuristics

- **When an income discrepancy is identified, default to checking whether the unreported amount exceeds 25% of the gross income stated on the return before assuming the standard 3-year statute of limitations applies** — this threshold determines whether a 6-year window is available.
- **When badges of fraud are present (concealment, implausible explanations, destroyed records, pattern of substantial underreporting), default to elevating scrutiny and considering a fraud referral — but recognize the clear-and-convincing evidentiary bar is meaningfully higher than what supports an ordinary deficiency, and don't assert fraud on evidence that only clears the lower preponderance standard.**
- **When a taxpayer lacks full documentation for a plausible expense, default to deriving a reasonable, independently bounded estimate (via partial records, comparable industry data, or verifiable proxies) rather than disallowing the expense entirely or accepting the taxpayer's proposed figure uncritically.**
- **When proposing any penalty, default to first confirming which specific penalty applies and its required proof standard — accuracy-related (preponderance) versus civil fraud (clear and convincing) — before selecting one, rather than defaulting to the more severe penalty because the underreporting is large.**
- **When a taxpayer proposes a collection resolution (installment agreement, offer in compromise), default to independently calculating reasonable collection potential (assets plus future income capacity) rather than accepting the taxpayer's proposed payment amount at face value.**
- **When taking a collection action (lien or levy), default to verifying every required notice was sent and its waiting period elapsed, in the correct sequence, before proceeding** — a procedurally defective collection action can be invalidated independent of the debt's validity.

## Decision framework

1. **Determine which statute of limitations applies** to the specific tax year and fact pattern — check whether unreported income exceeds the 25%-of-gross-income threshold for the extended 6-year period, or whether fraud/non-filing removes the limitation entirely.
2. **Review the return against supporting documentation**, identifying specific discrepancies (unreported income, unsubstantiated deductions) rather than a general impression of noncompliance.
3. **Where records are incomplete, determine whether a Cohan estimate is warranted** and, if so, independently derive a reasonably bounded estimate rather than accepting the taxpayer's proposed figure or disallowing outright.
4. **Assess whether badges of fraud are present** to determine whether this is an accuracy-related matter or warrants pursuing a civil fraud determination, applying the correct proof standard to each.
5. **Calculate the proposed deficiency**: additional unreported income plus disallowed deductions, applied against the correct marginal rate.
6. **Determine and apply the correct penalty** (accuracy-related vs. civil fraud) based on the evidence and its applicable proof standard.
7. **If pursuing collection, verify all required procedural notices (including Collection Due Process rights) were issued in the correct sequence** before a lien or levy proceeds.

## Tools & methods

Statute of limitations analysis (3-year/6-year/unlimited triggers), indirect income reconstruction methods (bank deposit analysis, net worth method, source and application of funds), Cohan rule estimation methodology, badges-of-fraud checklist, accuracy-related penalty (IRC §6662) and civil fraud penalty (IRC §6663) determination, reasonable collection potential (RCP) analysis for installment agreements/offers in compromise, Collection Due Process (CDP) notice and hearing procedures.

## Communication style

With taxpayers/representatives: specific, documented findings ("bank deposits show $30,000 more than reported gross receipts, after excluding identified non-taxable transfers") rather than general assertions of noncompliance. With legal/fraud referral units: findings framed against the correct proof standard (preponderance vs. clear and convincing), with badges of fraud specifically enumerated, not asserted generally. With taxpayers proposing collection resolutions: independently calculated reasonable collection potential shown component by component (assets, income capacity), not just an accepted or rejected proposal.

## Common failure modes

- Applying the standard 3-year statute of limitations without checking whether the 25%-of-gross-income threshold extends it to 6 years.
- Asserting civil fraud on evidence that only meets the preponderance standard appropriate for an ordinary deficiency, not the clear-and-convincing standard fraud requires.
- Disallowing an entire deduction for lack of full documentation instead of deriving a reasonable Cohan estimate when credible evidence shows the expense plausibly occurred.
- Accepting a taxpayer's proposed installment agreement or offer amount without independently calculating reasonable collection potential.
- Proceeding with a lien or levy without verifying every required Collection Due Process notice was issued in the correct sequence.

## Worked example

A taxpayer's Schedule C reports gross receipts of $180,000 and deductions of $140,000. Total gross income reported on the return (including other income) is $185,000.

**Indirect income reconstruction (bank deposit analysis):** Total bank deposits for the year: $230,000. Of this, $20,000 is identified and documented as non-taxable (loan proceeds and a gift). Remaining identified business-related deposits: $210,000.

**Unreported income:** $210,000 (actual business deposits) − $180,000 (reported gross receipts) = **$30,000 unreported income**.

**Statute of limitations check:** Is $30,000 greater than 25% of the $185,000 reported gross income ($46,250)? $30,000 < $46,250 — **does not meet the 25% threshold**, so the extended 6-year statute of limitations does not apply; the standard 3-year period applies (assuming no fraud), and the return must still be within that window to assess.

**Documentation review:** Taxpayer substantiates $125,000 of the $140,000 claimed deductions with receipts. The remaining $15,000, claimed as vehicle/mileage expense, has no mileage log, but the taxpayer has fuel receipts and a plausible business-use pattern consistent with their occupation (contractor).

**Cohan estimate:** Rather than disallowing the full $15,000 or accepting it outright, the examiner independently derives a reasonable estimate using fuel receipt totals and comparable industry mileage patterns for similar contractors, allowing **$9,000** of the claimed $15,000 and disallowing **$6,000**.

**Deficiency calculation:**
- Additional unreported income: $30,000
- Disallowed deductions: $6,000
- **Total additional taxable income: $36,000**
- At a 24% marginal rate: $36,000 × 24% = **$8,640 additional tax**

**Penalty determination:** No badges of fraud identified — taxpayer was cooperative, records were imperfect but not concealed or destroyed, explanations were consistent. This is an **accuracy-related penalty** matter (substantial understatement, since $36,000 exceeds the greater of $5,000 or 10% of correct tax), not civil fraud: $8,640 × 20% = **$1,728 penalty**.

**Total proposed assessment:** $8,640 + $1,728 = **$10,368**.

Examination report:

> **Examination Report — Taxpayer [ref], Tax Year [ref]**
> Unreported income (bank deposit analysis): $30,000. Statute of limitations: standard 3-year period applies (unreported income of $30,000 is below the $46,250 / 25%-of-gross-income threshold for the extended 6-year period).
> Disallowed deductions: $6,000 of $15,000 claimed vehicle expense (Cohan estimate applied; $9,000 allowed based on fuel receipts and comparable mileage data).
> **Additional taxable income: $36,000 | Additional tax: $8,640 | Accuracy-related penalty (20%, no fraud indicators present): $1,728**
> **Total proposed assessment: $10,368.**

## Going deeper

- [references/playbook.md](references/playbook.md) — load when checking a statute of limitations trigger, running an indirect income reconstruction, or calculating a Cohan estimate.
- [references/red-flags.md](references/red-flags.md) — load when a specific return, discrepancy, or collection situation looks off and you need to know what it usually means.
- [references/vocabulary.md](references/vocabulary.md) — load when a term in an examination or collection record needs a precise definition.

## Sources

Internal Revenue Code statute of limitations provisions (IRC §6501, including the 25%-of-gross-income 6-year extension and the unlimited period for fraud/non-filing); Cohan v. Commissioner (2d Cir. 1930) establishing the estimation doctrine; IRC §6662 (accuracy-related penalty) and §6663 (civil fraud penalty) with their respective proof standards; IRC §6330 (Collection Due Process) procedural requirements. Specific figures in this file (thresholds, rates, penalty percentages) reflect current commonly cited federal provisions — always confirm against the current tax code and the specific jurisdiction's (federal or state) applicable rules before finalizing a determination.
