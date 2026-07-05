# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual rent analysis, reserve schedule, or vendor checklist — not for general reasoning (that's `SKILL.md`).

## Rent / vacancy-cost worksheet

```
Unit: [ID]                    Current asking rent: $1,850/mo         Weeks vacant so far: 6

Comparable market data:
  Comparable units' avg rent: $1,750/mo
  Comparable units' avg time-to-lease: 2-3 weeks

Cost of current strategy (staying at $1,850):
  Vacancy cost so far: $1,850 × 1.5 months = $2,775
  Projected additional vacancy if no leasing activity continues: [estimate based on trend]

Cost of alternative (reduce to $1,750):
  Expected additional vacancy: 2-3 weeks = ~$875-1,310
  Annual rent differential vs. $1,850: $100/mo × 12 = $1,200/yr

Break-even check: does the avoided vacancy cost from faster lease-up exceed the annual rent
differential? If yes (as in this example, ~$1,700 avoided vs. $1,200/yr differential), recommend
the reduction.
```

## Reserve funding schedule tracker

```
Association: [name]                    Reserve study date: [date]         Study horizon: 30 years

Major components (from reserve study):
Component        | Useful life | Remaining life | Replacement cost | Annual funding needed
------------------|-------------|-----------------|--------------------|-----------------------
Roof              | 25 yrs      | 8 yrs           | $180,000           | $22,500/yr
Paving            | 20 yrs      | 4 yrs           | $95,000            | $23,750/yr
Elevators (2)     | 30 yrs      | 12 yrs          | $220,000           | $18,333/yr
------------------|-------------|-----------------|--------------------|-----------------------
Total recommended annual funding: $64,583/yr

Current actual funding: $48,000/yr (74% of recommended)
Gap: $16,583/yr — this is a fiduciary decision to disclose explicitly to the board/owners, not a
default outcome of avoiding an assessment increase.

Current reserve balance: $310,000
Percent funded (balance vs. ideal funding position per study): 58%
```

## Vendor qualification checklist (elevated tier — life-safety/structural systems)

```
Vendor: [name]                    System type: [fire suppression / elevator / structural]

Standard checks:
  [ ] License verified and current
  [ ] Insurance certificate current and coverage adequate for scope
  [ ] References checked (minimum 2, ideally including a comparable-scope project)

Elevated diligence (required for this system category, not just standard vendor selection):
  [ ] Track record specifically in this system category, not general contracting experience
  [ ] Any prior incidents/citations checked (state licensing board, if applicable)
  [ ] Total cost of ownership compared (not just bid price) including expected maintenance/
      failure-response cost differential vs. other bidders

Do not select on lowest bid alone for this system category.
```
