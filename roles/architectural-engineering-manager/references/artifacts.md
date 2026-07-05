# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual fee proposal, change order, or staffing tracker — not for general reasoning (that's `SKILL.md`).

## Fee proposal skeleton (lump-sum + hourly hybrid)

```
PROJECT: [Name] — [Building type, size]
BASIS OF FEE:

Phase                        | Fee Type       | Amount     | Basis
------------------------------|----------------|------------|----------------------------------
Schematic Design (SD)         | Lump sum       | $62,000    | 400 hrs equiv @ $95/hr blended, 3.0x multiplier ÷ scope %
Design Development (DD)       | Lump sum       | $124,000   | 800 hrs equiv, program assumed frozen at DD sign-off
Construction Documents (CD)   | Hourly, NTE    | $156,000   | Based on current program; NTE cap, billed monthly against actual hours
Bidding/Negotiation           | Hourly, NTE    | $18,000    | ~140 hrs estimate
Construction Admin (CA)       | Hourly, NTE    | $46,000    | ~350 hrs estimate, RFI/submittal review
------------------------------|----------------|------------|----------------------------------
TOTAL ESTIMATED FEE            |                | $406,000   |

ADDITIONAL SERVICES (not included above):
- Program/scope changes requested after DD sign-off: $130/hr, authorized in writing before work begins
- Redesign due to client-directed changes: $130/hr
- Site visits beyond the 12 included in CA phase: $850/visit flat
- Regulatory resubmittals beyond 1 round per phase: $130/hr

PEER REVIEW (fixed, included regardless of overall budget tracking):
- Independent lateral system review by [Name, license #], 40 hrs @ $130/hr = $5,200, billed as fixed line item
```

## Additional-services change order (short form)

```
CHANGE ORDER #[N] — [Project Name]

Original scope reference: [Section X of original proposal, dated Y]
Requested change: [1-2 sentence description of what client is asking for]
Why this is outside original scope: [reference specific scope boundary from original contract]
Estimated additional hours: [N] hrs @ $130/hr = $[amount]
Schedule impact: [none / +N business days]

Client authorization required before work proceeds: [ ] Yes  [ ] No (de minimis, <2 hrs, proceeding under existing scope)

Approved by (client): ______________  Date: ______
Approved by (firm PM): ______________  Date: ______
```

## Staffing / utilization tracker (monthly snapshot)

```
Discipline: Structural          Month: [Month/Year]
Staff        | Billable Target | Actual Billable Hrs | Utilization | Assigned Projects
-------------|-----------------|----------------------|-------------|-------------------
J. Alvarez   | 130 hrs (75%)   | 142 hrs              | 82%         | Project A (60%), Project B (22%)
R. Chen      | 130 hrs (75%)   | 98 hrs               | 57%         | Project C (57%) — under target, has capacity
M. Osei      | 130 hrs (75%)   | 137 hrs              | 79%         | Project A (40%), Project D (39%)
-------------|-----------------|----------------------|-------------|-------------------
Discipline avg utilization: 73% (target: 75%, break-even floor: 62%)

New project staffing rule: do not assign a new project to a discipline average above 78% without an identified specific staff member with confirmed open capacity below target — R. Chen (57%) is the confirmed-available staff for new structural work this month.
```

## Break-even / target multiplier quick calc

```
Direct labor cost (est. hours × blended loaded rate) = A
Overhead rate (as % of direct labor, from firm financials) = B%
Break-even fee = A × (1 + B)
Break-even multiplier = Break-even fee ÷ A = (1 + B)

Target fee = A × target multiplier (typically 2.9–3.1 for a healthy AE firm)
Margin built into target fee = Target fee − Break-even fee

Example: A = $114,000, B = 155% → Break-even fee = $114,000 × 2.55 = $290,700 (break-even multiplier 2.55)
Target fee at 3.0x = $342,000 → margin over break-even = $51,300 (before profit-sharing/bonus allocation)
```
