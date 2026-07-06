# Wind project development stage-gate playbook

Filled worksheets for the four recurring development decisions: gate sequencing, interconnection cost-allocation stress test, land option term matrix, and safe-harbor deadline tracking.

## 1. Stage-gate sequencing checklist

Advance to the next capital-intensive gate only after the prior gate's kill-risk is cleared or explicitly accepted:

| Gate | Approximate cost | Kill-risk if failed | Sequence rule |
|---|---|---|---|
| Land control (options) | $50K-200K | Site unavailable | First — cheapest, fastest de-risking step |
| Preliminary wind resource assessment | $150K-400K | Resource inadequate for bankability | Second — before interconnection application in most queues |
| Interconnection queue application + preliminary study | $50K-150K deposit | Queue position denied or excessive cost allocation | Third — do NOT commit to full permitting spend before results |
| Environmental/species desktop screening | $30K-80K | Major habitat conflict requiring redesign | Run in parallel with interconnection study, not after |
| Full system impact/facilities study | $200K-500K | Confirmed cost allocation makes project uneconomic | Fourth — economics must be re-validated against this result |
| Detailed engineering + formal permitting | $3M-10M+ | Permit denial, appeal delay | Fifth — only after interconnection economics confirmed viable |
| PPA/offtake execution | Negotiation cost only | No viable revenue contract | Can run parallel to permitting once economics are confirmed |
| Financial close (tax equity, debt) | Transaction costs | Financing terms don't clear hurdle | Last — requires all above resolved |

Rule: never authorize spend on gate N+1 while gate N's outcome could still kill the project's economics — a confirmed interconnection cost allocation is the single most common gate where "keep moving forward" wastes the most money if skipped.

## 2. Interconnection cost-allocation stress test

```
Base capex (excl. interconnection upgrade): $280,000,000 / 200MW = $1.40/W
Interconnection upgrade allocation (from SIS): $52,000,000
Total capex: $332,000,000 / 200MW = $1.66/W

Base-case LCOE (at $280M capex): $24.00/MWh
Scaled LCOE (at $332M capex, proportional approximation):
  $24.00 × (332/280) = $28.46/MWh

Anchor PPA price: $27.50/MWh (fixed, 20-year)
Result: LCOE ($28.46) > PPA price ($27.50) → uneconomic at full allocation
```

Run this stress test at three scenarios before authorizing next-stage spend:
1. **Full allocation as studied** (worst case, above)
2. **Cluster cost-share** (if a queue restudy splits the upgrade cost across multiple projects — estimate each project's proportional share)
3. **Post-withdrawal restudy** (if a competing queue project withdraws, reducing the shared upgrade need)

Only proceed to the next capital-intensive gate if at least the base or a clearly probable scenario clears the bankability threshold.

## 3. Land option term matrix

| Development phase | Typical duration | Cumulative time from land control |
|---|---|---|
| Wind resource assessment | 1-3 years (multi-year data often required for bankability) | Year 1-3 |
| Interconnection queue study process | 1-3 years, longer with restudy | Year 2-5 |
| Environmental/permitting | 1-3 years, longer with appeal | Year 3-6 |
| Financial close to notice-to-proceed | 6-12 months | Year 4-7 |
| **Recommended option term + extensions** | **7-9 years minimum** | Covers realistic worst-case above |

Rule: negotiate the option term against the worst-case cumulative timeline above, not the optimistic case — a shorter term forces a rushed permitting or interconnection decision under expiration pressure, which is a worse outcome than paying a modest premium for extension rights up front.

## 4. Tax-credit safe-harbor deadline tracker

```
Credit type: <PTC / ITC>
Safe-harbor method: <5% cost-incurred test / physical-work test>
Applicable deadline (per current IRS guidance for the relevant construction-start year): <date>
Documentation required:
  - 5% cost test: binding equipment purchase contracts, invoices, proof of payment totaling ≥5% of total project cost
  - Physical work test: contracts and evidence of physical work of a significant nature (on-site or off-site manufacturing) begun before deadline
Continuity requirement: <continuous construction/efforts through commercial operation — track annually>
Current status: <met / at risk / missed>
Action if at risk: <accelerate procurement of qualifying equipment, document physical work evidence immediately>
```

Treat this deadline as a hard input to the procurement schedule — a missed safe-harbor date can change project economics by the full value of the credit, independent of any other development delay.

## 5. Environmental/species-habitat desktop screening checklist

- [ ] Federal/state-listed threatened or endangered species range overlap checked against site boundary
- [ ] Known migratory bird/bat corridor data reviewed (USFWS voluntary guidelines or equivalent regional data)
- [ ] Wetlands/waters delineation desktop review (National Wetlands Inventory or equivalent)
- [ ] Cultural/historic resource desktop screening (state historic preservation office database)
- [ ] Local zoning/setback ordinance review against preliminary site layout
- [ ] Noise/shadow-flicker preliminary modeling against nearest residence setback requirements

Run this before or parallel to the interconnection system impact study — not after, since a significant conflict found here can change the site layout in ways that also affect the interconnection point and cost allocation.
