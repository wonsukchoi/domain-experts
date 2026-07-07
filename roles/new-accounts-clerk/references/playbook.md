# New Accounts Clerk — Playbook

## CIP verification decision table

| Situation | Method | Acceptable documents/checks | Action if it fails |
|---|---|---|---|
| Customer present, has valid photo ID | Documentary | Unexpired driver's license, passport, state ID, military ID | Request second ID or non-documentary check |
| Customer present, ID expired or illegible | Non-documentary | Credit bureau match, public-database check, existing-customer confirmation | Decline to open until resolved |
| Mail-in / non-face-to-face application | Non-documentary (documentary optional as supplement) | Credit bureau match, independent source verification, existing relationship confirmation | Decline to open until resolved |
| Minor / dependent account | Documentary (parent/guardian) + minor's birth certificate or SSN card | Parent/guardian ID plus minor's ID document | Decline to open until resolved |

## Beneficial-ownership certification worksheet (filled example)

Legal entity: [LLC name]. Certification collected from: [authorized signer], title: Managing Member.

| Individual | Role | Reported ownership % | ID verification | Control person? |
|---|---|---|---|---|
| Owner A | Member | 40% | Driver's license, verified | No |
| Owner B | Member | 35% | Driver's license, verified | No |
| Owner C | Managing Member | 25% | Driver's license, verified | Yes |
| **Total** | | **100%** | | |

Sum check: 40 + 35 + 25 = 100%. If the total is under 100%, ask who holds the remainder before certifying — an unaccounted owner above 25% is a missed CDD requirement, not a rounding gap.

## OFAC screening escalation sequence

1. Screen every named individual and the entity itself at account opening — not just the primary applicant.
2. **No match:** proceed to next CIP/CDD step.
3. **Possible match** (partial name match, DOB proximity, no exact secondary-identifier match): hold activation, escalate to compliance with matched fields and customer documentation attached. Do not resolve at clerk level regardless of how confident the dismissal feels.
4. **Exact match:** block immediately, escalate to compliance and, per bank policy, to the BSA officer — this is a reportable event, not a customer-service problem.
5. Compliance clears or confirms within the bank's stated SLA (commonly 1–3 business days, policy-dependent — verify against current procedure).

## Signature-card authority setup

| Account type | Common authority default | When to deviate |
|---|---|---|
| Individual | Sole signer | N/A |
| Joint personal | Any one signer (survivorship) | Either-or-both explicitly confirmed verbally; note if "all must sign" requested instead |
| Business, single owner | Owner or designated signer | Per owner's instruction |
| Business, multiple owners | Per operating agreement (may require two-of-N or unanimous) | Always confirm against the entity's own governing document, not a bank default |

## Product-fit quick reference

| Stated need | Better-fit product if mismatched |
|---|---|
| "Won't touch this money for 12+ months" requesting checking | CD or money-market account (yield, still liquid enough) |
| Frequent small transactions requesting savings (withdrawal-limited) | Checking or money-market with debit access |
| Large idle balance in non-interest checking | Interest-bearing checking or sweep to money-market |
