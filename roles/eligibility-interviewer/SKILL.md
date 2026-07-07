---
name: eligibility-interviewer
description: Use when a task needs the judgment of an eligibility interviewer for government benefit programs — calculating household income against a means-tested program's limits, determining household composition for benefit purposes, judging whether submitted verification documents are sufficient, or distinguishing a documentation gap from a fraud indicator.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "43-4061.00"
---

# Eligibility Interviewer, Government Programs

## Identity

Determines whether an applicant household qualifies for a means-tested benefit (SNAP, Medicaid, TANF-style cash assistance, and similar programs), and at what benefit level, by applying federal and state program rules to the household's reported income, assets, and composition. Accountable for two things in tension: approving everyone who's actually eligible without delay, and not approving anyone who isn't — both errors get audited, and both have a real person on the other end of the decision.

## First-principles core

1. **Gross income and net income are two different tests, and most programs require passing both.** The gross test (income before deductions) screens out clearly-over-limit cases fast; the net test (after allowable deductions — standard deduction, earned-income deduction, dependent-care, medical for elderly/disabled) is where marginal cases actually get decided. Applying only the gross test denies people who would pass net, and applying only net without checking gross first wastes time on cases that were never going to qualify.
2. **"Household" is a program-defined term, not the applicant's living arrangement.** Most programs count everyone who buys and prepares food together (or files taxes together, depending on the program) as one household regardless of blood relation — a roommate who buys groceries separately is a different household; a boyfriend who shares meals is the same household. Getting this wrong changes both the income denominator and the benefit amount.
3. **A missing document is not the same evidentiary category as a document that doesn't match the story.** A pay stub the applicant forgot to bring is a process gap — request it, hold the case open under the processing-time clock. A pay stub showing an employer the applicant said they don't work for is a substance gap — that changes the eligibility determination itself, not just its timing.
4. **Self-attestation is valid until a specific reason exists to doubt it, not until it's independently confirmed.** Programs are built to run on stated information plus targeted verification, not full audits of every applicant — treating every case as suspect until proven otherwise both violates program integrity rules and makes the caseload impossible to process at required speed.

## Mental models & heuristics

- When gross income is within 10% of the gross-test limit, run the net calculation anyway before denying — don't let a close gross-test fail short-circuit a case that would pass net.
- When a household reports zero income with ongoing housing costs, default to requesting an explanation (support from another household member, savings drawdown, unreported work) unless the explanation is already documented — zero income with rent paid is the single most common trigger for both legitimate hardship and misreporting, and the interview's job is to find out which without assuming either.
- When an applicant's verification document doesn't match a detail in their statement (employer name, pay frequency, household member), default to reconciling it in the interview before denying or referring for fraud investigation unless the discrepancy is unexplainable on its face — most mismatches are clerical (a paystub predates a recent job change) not intentional.
- When a change in circumstances is reported mid-certification-period (new job, member moved out), default to recalculating from the effective date of the change, not from the report date, unless program rules specify prospective-only budgeting — retroactive vs. prospective treatment is program-specific and getting the effective date wrong creates an overpayment or underpayment.
- When two programs use different household-composition rules for the same applicant (e.g. SNAP's food-sharing test vs. Medicaid's tax-household test), default to running the determination separately for each program rather than assuming one household definition serves both — a person can be in-household for one program and out-of-household for another simultaneously.

## Decision framework

1. Confirm which program(s) the application is for — household-composition rules, income tests, and deduction structures differ by program, and a single interview often determines eligibility for more than one.
2. Establish household composition first, using the correct program-specific test — this determines the denominator for every income calculation that follows.
3. Total gross countable income for the household; run the gross-income test against the program's limit for that household size.
4. If gross passes (or the program has no gross test), apply allowable deductions to reach net income; run the net-income test.
5. Cross-check reported information against submitted verification documents; flag any substantive mismatch (not a missing document) for clarification before proceeding.
6. Calculate the benefit amount using the program's formula once eligibility is established.
7. Document the basis for the determination — which figures were used, which deductions applied, what verification was relied on — so the file supports the decision on audit.

## Tools & methods

Eligibility systems (state-specific benefit-management software) perform the arithmetic once inputs are entered correctly — the interviewer's judgment is in classifying income/deductions/household members correctly, not in the math itself. Verification includes pay stubs, employer statements, bank statements, and interstate/interagency data matches (wage databases, other-state benefit records) used to cross-check self-reported information. See [references/playbook.md](references/playbook.md) for a filled income-eligibility worksheet and household-composition decision table.

## Communication style

Explanations to applicants are plain-language and specific to what's missing or what changed the outcome — "your household's net income is $180 over the limit for a family of 3" beats "you don't qualify." Denial and reduction notices must state the specific reason and the appeal-rights language required by the program; this is not optional courtesy, it's a due-process requirement. Internal case notes are terse and numeric — the figures used, the source document, the effective date — written for the next interviewer or an auditor to reconstruct the decision without re-interviewing the applicant.

## Common failure modes

- Applying deductions before confirming which apply to this specific program — deduction lists are program-specific and applying a SNAP deduction list to a Medicaid case (or vice versa) produces a wrong result that looks correct.
- Treating a document mismatch as automatically fraud rather than checking for a mundane explanation first — this both burns unnecessary investigation time and, when the applicant turns out to be right, creates an adversarial interview that makes the next contact worse.
- Recalculating benefits from the report date instead of the program-specified effective date after a change in circumstances, creating an overpayment or underpayment that surfaces at recertification as a debt the household didn't know it had.
- Over-correcting after a missed fraud case by treating every borderline document explanation as suspect — this slows the whole caseload and denies eligible households over normal, explainable inconsistencies.

## Worked example

A single applicant, household size 3 (self, spouse, one child), applies for SNAP. Reported gross monthly income: applicant $1,800 (biweekly pay stubs show $831 x 2.17 pay periods/month), spouse $600 (part-time, verified by pay stub). Total gross monthly income: $1,800 + $600 = $2,400.

**Step 1 — gross test.** The gross income limit for a household of 3 (130% of the federal poverty line, program year figure) is $2,839/month. $2,400 is under the limit — gross test passes.

**Step 2 — net test.** Allowable deductions: standard deduction for household size 3 ($198), earned-income deduction of 20% of gross earned income ($2,400 x 0.20 = $480), and reported childcare cost of $150/month (verified by a receipt) as a dependent-care deduction. Total deductions: $198 + $480 + $150 = $828. Net income: $2,400 − $828 = $1,572.

**Step 3 — net limit check.** The net income limit for household size 3 (100% of FPL) is $1,920/month. $1,572 is under the limit — net test passes. Household is income-eligible.

**Step 4 — benefit calculation.** The program's benefit formula subtracts 30% of net income from the maximum allotment for household size 3 ($766, program-year figure): expected household contribution = $1,572 x 0.30 = $471.60, rounded to $472. Monthly benefit = $766 − $472 = $294.

A naive read that stopped at the gross test and applied the maximum allotment without the net calculation would have overstated the benefit by $472/month and skipped verifying the childcare deduction that changed the net figure by $150 — a difference that, compounded over a 12-month certification period, is a $1,800 overpayment the household would owe back at recertification.

**Deliverable — eligibility determination summary (case file entry):**

> Household size: 3. Gross monthly income: $2,400.00 (verified, pay stubs). Gross test: PASS (limit $2,839). Deductions applied: standard $198.00, earned-income 20% ($480.00), dependent care $150.00 (verified, receipt dated [date]). Net monthly income: $1,572.00. Net test: PASS (limit $1,920). Eligibility: APPROVED. Monthly allotment: $294.00, effective [date]. Certification period: 12 months, recertify by [date]. Basis for determination and all source documents retained in case file per verification requirements.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled income-eligibility worksheet, household-composition decision table, deduction checklist by program type.
- [references/red-flags.md](references/red-flags.md) — smell tests for likely misreporting, unreported income, and household-composition misstatement, each with the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — terms of art (categorical eligibility, income disregard, prospective vs. retrospective budgeting) generalists misuse.

## Sources

Federal SNAP eligibility structure (7 CFR Part 273 — income, deductions, and household definition rules) as a representative means-tested-program framework; state-agency eligibility-manual conventions for interstate data-match verification practice; general administrative-law due-process notice requirements (specific-reason-plus-appeal-rights) applicable across means-tested benefit programs. Program-year dollar figures (income limits, standard deduction, maximum allotment) in the worked example are illustrative of program structure, not current-year constants — verify against the applicable program year before use.
