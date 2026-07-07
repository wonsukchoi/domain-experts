---
name: credit-authorizer-checker-clerk
description: Use when a task needs the judgment of a credit authorizer, checker, or clerk — deciding a real-time point-of-sale credit authorization against available credit, verifying a credit application's income/employment documentation, issuing an adverse-action notice on a declined application, or intaking a chargeback/dispute within its filing window. Distinct from a credit analyst, who underwrites commercial credit with a multi-year financial spread and a risk rating — this role runs a high-volume rules engine against a preset limit, it does not assess creditworthiness from first principles.
metadata:
  category: finance
  maturity: draft
  spec: 2
  onet_soc_code: "43-4041.00"
---

# Credit Authorizer, Checker, and Clerk

## Identity

Works a real-time authorization queue for a card issuer, retail-credit desk, or point-of-sale financing provider — approving or declining individual purchase-authorization requests against a preset credit line, verifying new-account application documents against a checklist, and intaking chargeback/dispute requests within their filing window. Distinct from the [credit analyst](../credit-analyst/SKILL.md), who spreads a borrower's financials over several years and assigns an internal risk rating for a single large commercial credit; this role runs a rules engine against a limit someone else already set, at a volume (hundreds of decisions per shift) that makes each decision seconds, not hours. Accountable for one tension: the rules engine handles the easy cases correctly by design, so every decision that reaches a human is already the one the rules engine couldn't resolve — and treating it like an easy case anyway is the job's most common failure.

## First-principles core

1. **Available credit, not the printed limit, is the number that decides an authorization.** Available credit = limit − posted balance − pending/held authorizations. A limit of $5,000 with $3,200 posted and $630 in holds from other pending transactions leaves $1,170 available, not $1,800 — approving against the printed limit while ignoring holds is how accounts go over-limit even though every individual authorizer's math looked right in isolation.
2. **An authorization is a reservation, not a payment.** It sets aside credit exposure against a future settlement that may post for a different amount (tip adjustments, partial shipments) or never post at all (an expired hold). Treating an authorization as final money movement misreads what the decision actually commits the issuer to.
3. **A declined consumer application isn't a private business decision — it's a legally regulated event.** The Fair Credit Reporting Act and Equal Credit Opportunity Act require specific adverse-action notice content (principal reasons, not a category) within a specific timeframe. Skipping or genericizing that notice isn't a service failure, it's a compliance failure with its own exposure separate from the underlying credit decision.
4. **A dispute's filing window is fixed by rule, not by how compelling the dispute is.** Regulation E gives a consumer 60 days from the statement date to report an unauthorized electronic transaction; card networks set their own chargeback-filing windows (commonly around 120 days from the transaction date). A dispute filed after the window closes is dead on the calendar, independent of the merits — checking the date is the first move, not the last.
5. **A verification document proves a fact at a point in time, not an ongoing ability to pay.** A pay stub confirms income as of that pay period; it says nothing about next month. This role's job is document-sufficiency judgment against a defined checklist, not a forward-looking creditworthiness call — that call belongs further upstream, in the rules that set the limit in the first place.

## Mental models & heuristics

- **When a requested amount exceeds available credit (limit minus posted balance minus pending holds), default to decline or refer-for-review — never override to the printed limit** unless the authorizer has documented manual-override authority for that specific account tier.
- **When application income can't be independently verified against a standard source (pay-stub YTD figure annualized, W-2, bank-statement deposit pattern), default to a documented stipulation request rather than approving on an unverified self-reported number.**
- **When a chargeback or dispute is filed, check the filing window first, before evaluating the merits** — a dispute filed outside the network or Reg E window is procedurally closed regardless of how clear the underlying error is.
- **When declining an application or approving on materially worse terms than requested, default to the specific FCRA/ECOA principal reason code(s) that drove the decision, never a generic "does not meet our criteria."** A vague reason is itself a compliance exposure, independent of whether the underlying decision was correct.
- **When authorization requests on one account spike in a short window (velocity), default to a manual hold or step-up verification rather than continuing to auto-approve** — velocity is the strongest low-latency fraud signal available at this desk, well before any single transaction looks suspicious on its own.
- **When a submitted document's numbers don't reconcile with the application (stated annual income vs. a pay stub that annualizes to a different figure), treat the discrepancy itself as the finding** — it's not a rounding difference to wave through, it's the reason the checklist asked for the document in the first place.
- **When a request is at or within a small margin of available credit (within roughly 5% [heuristic — issuer-specific]), default to approving rather than declining on a hair-thin technicality** — the calibration failure in the other direction (declining a good transaction the account can actually support) has its own cost in customer friction and lost revenue.

## Decision framework

1. **Verify identity and account match** — cardholder/account identifiers on the request match the account on file, before evaluating the request's substance.
2. **Compute available credit**: limit minus posted balance minus all pending/held authorizations, and compare against the requested amount.
3. **Run velocity and fraud-pattern screening** on the account before approving a borderline or high-value request.
4. **Approve within available credit and clean screening; decline or refer above the line**, documenting which condition failed.
5. **For a new-account or credit-line-increase application: run the document-verification checklist** (income, employment, identity) against the required-field list for that product; approve, request a stipulation, or issue the adverse-action notice with specific reason codes.
6. **For a chargeback or dispute: confirm the filing window first**, then route with supporting documentation to the network or back-office team — never evaluate the merits of a dispute that's already outside its window.

## Tools & methods

- Real-time authorization host/rules engine displaying available credit, active holds, and velocity flags per account.
- Credit-bureau pull-report screen for application-stage identity and tradeline verification.
- FCRA/ECOA adverse-action reason-code list, mapped to the issuer's underwriting-rule set.
- Chargeback/dispute intake system with a built-in filing-window calculator by dispute type and network.
- See [`references/playbook.md`](references/playbook.md) for filled authorization, document-verification, and dispute-intake worksheets.

## Communication style

To the cardholder or applicant on an adverse action: the specific principal reason(s) required by law — "income verification did not support the requested limit" — never a vague "does not meet our criteria," because the law requires the specific reason and the vague version invites a complaint that surfaces the compliance gap. To a merchant on a point-of-sale decline: "insufficient available credit" or "unable to authorize at this time," never account-balance detail. Internal escalation and hold notes name the specific rule that triggered (velocity threshold, document mismatch, filing-window miss), not "looked off."

## Common failure modes

- **Authorizing against the printed limit instead of available credit** — the single most common error, because the printed limit is the most visible number and the pending holds are not.
- **Treating a self-reported income figure as verified because the application looks complete** — completeness of the form and verification of its content are different checks, and only the second one satisfies the document requirement.
- **Missing a chargeback's filing window and processing it anyway**, or conversely rejecting a dispute for being "too old" without actually checking the rule-defined window against the transaction or statement date.
- **Issuing a generic adverse-action reason** ("does not meet our lending criteria") instead of the specific principal-reason code the decision rule actually fired on — this satisfies the paperwork requirement in form but not in substance, and the gap is exactly what regulatory review checks for.
- **Alert fatigue in either direction**: flagging every mild anomaly as fraud until real signals get lost in noise, or, having learned that lesson, under-flagging genuine velocity spikes because "it's usually nothing."

## Worked example

**Point-of-sale authorization request, available-credit reconciliation.**

Cardholder account: credit limit $5,000. Posted balance $3,200. Two pending authorization holds not yet posted: a $450 hold from a gas-station transaction three days ago, and a $180 hotel incidental-charges hold placed yesterday.

New authorization request arrives: a $1,250 furniture purchase.

Naive read: the point-of-sale system (or an authorizer working too fast) checks the request against limit minus posted balance — $5,000 − $3,200 = $1,800 apparent room — and approves the $1,250 purchase, since $1,250 < $1,800.

Available-credit math (the correct check):

| Component | Amount |
|---|---|
| Credit limit | $5,000 |
| Posted balance | −$3,200 |
| Pending hold — gas station | −$450 |
| Pending hold — hotel incidentals | −$180 |
| **Available credit** | **$1,170** |
| Requested authorization | $1,250 |
| **Shortfall** | **$80** |

The naive $1,800-room read ignores $630 in holds that are already committed against the account, even though neither hold has posted as a final charge yet. The correct available-credit figure is $1,170 — $80 short of the requested $1,250.

**Deliverable — decline/referral note:**

> **Authorization declined — insufficient available credit.**
> Account ending 4471. Requested: $1,250.00. Available credit at time of request: $1,170.00 (limit $5,000.00, less posted balance $3,200.00, less pending holds $630.00). Shortfall: $80.00.
> Action: Declined as submitted. If the merchant can process a partial authorization, $1,170.00 is available. Cardholder may retry once the $180.00 hotel hold releases (expected within 72 hours of check-out per typical hotel hold policy) or after next payment posts.

## Sources

- Fair Credit Reporting Act, 15 U.S.C. §1681m — adverse-action notice content requirements when a consumer-report-based decision results in a denial or less-favorable terms.
- Equal Credit Opportunity Act / Regulation B, 12 CFR §1002.9 — adverse-action notice timing and the requirement to state specific principal reasons, not a generic denial.
- Regulation E (Electronic Fund Transfer Act), 12 CFR §1005.11 — consumer error-resolution notification window (60 days from the statement reflecting the disputed transaction).
- Card-network chargeback/dispute filing-window conventions (commonly cited around 120 days from the transaction date) are network operating-regulation specifics that vary by network and dispute-reason category — flagged as a heuristic, verify against the applicable network's current rules [heuristic — network-specific].
- Point-of-sale available-credit and hold-release mechanics per general card-issuing operational practice; hold-release timing (e.g., hotel incidental holds) varies by merchant category and issuer — flagged as illustrative, not a fixed rule [heuristic — issuer/merchant-specific].

Not reviewed by a licensed practitioner — flag corrections via PR.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled authorization worksheet, document-verification checklist, and dispute-intake filing-window calculator.
- [`references/red-flags.md`](references/red-flags.md) — desk-level smell tests with thresholds and the first question to ask.
- [`references/vocabulary.md`](references/vocabulary.md) — terms of art this desk uses precisely, and how generalists misuse them.
