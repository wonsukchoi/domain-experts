# Spa capacity, menu, and classification playbook

Filled worksheets for the four recurring spa-manager decisions: room-hour ceiling modeling, menu-duration standardization, retail attach benchmarking, and worker classification.

## 1. Room-hour ceiling and utilization model

```
Theoretical max room-hours/week = rooms × operating hours/day × days/week
  = 6 × 11 × 7 = 462 room-hours/week

Current booked room-hours/week (from booking system) = 282
Utilization rate = 282 / 462 = 61%

Effective revenue per room-hour = average service price / average service duration (hours)
  = $135 / 1.083 = $124.60/room-hour

Weekly service revenue = booked room-hours × effective revenue per room-hour
  = 282 × $124.60 ≈ $35,137/week
```

Decision thresholds:
- **Under 70% utilization:** diagnose scheduling/menu fragmentation before assuming a demand problem.
- **70–85% utilization:** demand-generation (marketing, referral programs) has meaningful room-hour inventory left to sell into.
- **Above 85% utilization:** room-hour inventory is effectively sold out — the next lever is price increase or physical capacity expansion (more rooms/hours), not more marketing or more staff.

## 2. Menu-duration standardization matrix

| Current duration | Weekly bookings | Fragmentation impact | Standardize to |
|---|---|---|---|
| 25 min | 40 | High — leaves a 25–55 min unsellable gap depending on next booking | Fold into 50-min service, reduce scope or bundle |
| 50 min | 180 | Low — matches standard slot | Keep |
| 65 min | 90 | Moderate — mismatches with both 50 and 80-min slots | Reclassify to 50 or 80-min tier |
| 80 min | 110 | Low — matches standard slot | Keep |
| 90 min | 30 | High — mismatches 80-min slot by 10 min, creates recurring gap | Reclassify to 80-min tier or a dedicated 90-min block schedule |
| 105 min | 12 | High — infrequent, creates largest scheduling gaps | Offer only during off-peak hours where gap cost is lowest |

Rule: any duration responsible for high fragmentation impact and under ~15% of weekly bookings is a candidate to fold into an adjacent standard duration rather than preserved as a distinct menu item.

## 3. Retail attach rate benchmarking

```
Retail attach rate = retail revenue / service revenue

Current: $2,108 retail / $35,137 service = 6.0%
Benchmark (ISPA industry data): 15-20%
Target (conservative): 15%
Target retail revenue = 0.15 × $35,137 = $5,271/week
Gap = $5,271 - $2,108 = $3,162/week ≈ $164,000/year
```

Levers to close the gap, in order of typical impact per implementation cost:
1. Therapist product-recommendation training tied to treatment type (highest impact, lowest cost)
2. Point-of-sale prompt/script standardization at checkout
3. Retail display placement in high-traffic post-treatment path
4. Incentive structure (commission or spiff) tied to attach rate, not just total sales

## 4. Worker classification checklist (employee vs. independent contractor)

Score each factor; the more "Yes" answers, the stronger the case for employee classification regardless of what the contract says:

- [ ] Spa sets or approves the therapist's schedule
- [ ] Spa provides the treatment room, linens, and equipment
- [ ] Spa sets the service menu and prices the therapist charges
- [ ] Spa requires the therapist to wear a uniform or follow a specific service protocol
- [ ] Therapist works exclusively or primarily for this spa (not multiple independent client relationships)
- [ ] Spa handles client billing and pays the therapist a wage/commission rather than the therapist invoicing clients directly
- [ ] Therapist cannot subcontract the service to another therapist of their choosing

5+ "Yes" answers: classify as employee. Reclassifying a mislabeled contractor requires a documented transition — do not simply relabel without addressing back-pay/tax implications with counsel or a payroll specialist.

## 5. Cancellation/no-show policy sizing

```
Observed no-show rate (from booking system, trailing 90 days): 9%
Late-cancellation rate (under 24hr notice): 6%
Combined at-risk room-hour share: 15%

Policy: charge 50% of service price for no-shows and cancellations under 24hr notice,
        waived only for documented emergency, applied via POS at time of next booking
        or card on file — not a manual/discretionary decision by front-desk staff.
```

Track enforcement rate (fees actually charged ÷ fees triggered) monthly — a rate meaningfully below 90% signals discretionary waiving is undermining the policy's economic purpose.
