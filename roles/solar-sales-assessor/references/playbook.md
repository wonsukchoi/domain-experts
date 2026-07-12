# Playbook

Filled worksheets and templates an assessor actually runs on a deal, not descriptions of them.

## 1. Site assessment intake worksheet (filled example)

Run on-site or via a remote aerial/LiDAR report before any proposal is drafted.

```
ADDRESS: 1842 Larkfield Ave, Fresno, CA          UTILITY: PG&E — E-TOU-C

USAGE
  12-mo total: 11,000 kWh          Peak-window share (4–9pm): ~38%
  Rate schedule: E-TOU-C — Peak $0.50/kWh, Off-peak $0.35/kWh, blended $0.42
  Net program: Net Billing Tariff (NEM 3.0) — export via Avoided Cost Calculator

ROOF
  Material: asphalt shingle          Installed: 2018 (age 6 yr, rated 20 yr)
  Remaining service life: ~14 yr on paper, ~10 yr practical (regional heat aging)
  Pitch: 22°   Azimuth: 190° (near-optimal south)   Usable area: 620 sq ft
  Structural: rafters 2x6 @ 16" OC, adequate for standard rail-mount, no sag observed
  >>> Under 10-year practical remaining life? NO — reroof bundle not required, revisit at
      next 5-year inspection.

ELECTRICAL
  Service: 200A panel, calculated existing load 118A → 82A headroom
  Main panel location: garage, accessible, no upgrade required
  >>> If headroom <25A, flag panel upgrade as a priced line item before proposal, not
      a post-signing surprise.

SHADING
  Obstruction: neighbor's oak, west-facing roof plane, 15–20 ft canopy height
  Azimuth of obstruction from array: 41° off solar noon → WITHIN the 30–45° flag zone
  Action: instrumented shading report required (not satellite-only) — ordered same visit

INTERCONNECTION
  Standard: Rule 21 (CA)          Expected PTO timeline: 6–10 weeks, PG&E territory avg
```

## 2. Sizing worksheet — matching design to the tariff, not to usage

```
STEP 1 — Annual usage:                          11,000 kWh
STEP 2 — Export compensation vs. retail ratio:   $0.08 / $0.42 = 19%
STEP 3 — Decision rule applied:
  Export ratio <30% of retail AND peak window overlaps evening load
  → default: size to daytime self-consumption + battery, not to 100% offset

STEP 4 — Two designs modeled side by side:

  Design A (offset-matched, no battery)      Design B (self-consumption + battery)
  Array: 9.0 kW DC                            Array: 6.0 kW DC
  Battery: none                               Battery: 10 kWh
  Production: 13,950 kWh/yr                   Production: 9,300 kWh/yr
  Self-consumed share: ~35% (no shift)        Self-consumed share: ~90% (battery-shifted)
  Net cost after 30% credit: $18,900          Net cost after 30% credit: $20,020
  Real annual savings: $2,775                 Real annual savings: $3,589
  Real payback: 6.8 yr                        Real payback: 5.6 yr

STEP 5 — Recommend the design with the better real payback, not the larger offset
  number. State both designs on the proposal so the customer sees the tradeoff, not
  just the winner.
```

## 3. Financing comparison — cash-price-equivalent (filled example, same 6kW+battery deal)

Every option normalized to what a cash buyer would pay for the identical system — this is the number that belongs on the comparison, not the monthly payment.

| Path | Sticker / payment shown | Dealer fee baked in | Cash-price-equivalent | Who keeps the 30% credit | Escalator |
|---|---|---|---|---|---|
| Cash | $20,020 net | $0 | $20,020 | Customer | n/a |
| Loan, "$0 down, 5.99% APR, $199/mo, 20 yr" | $47,760 total payments | ~22% ($4,400) of loan principal | $23,600 (loan principal net of baked-in fee) | Customer | n/a (fixed loan) |
| Loan, "$0 down, 0.99% APR, $158/mo, 25 yr" | $47,400 total payments | ~28% ($6,700) of loan principal | $23,900 | Customer | n/a |
| Lease | "$0 down, $145/mo" | n/a (rent, not purchase) | Not applicable — never owned | Lessor (third party) | Typically ~2.9%/yr on payment |
| PPA | "$0 down, $0.16/kWh for power produced" | n/a | Not applicable — never owned | PPA provider (third party) | Typically ~2.9%/yr on rate |

**Rule applied here:** the "0.99% APR" loan looks cheaper on the monthly payment than the "5.99% APR" loan, but its dealer fee is higher, so its cash-price-equivalent is actually higher — always back out the fee and compare principal-net-of-fee, never the advertised rate or payment alone. Lease/PPA are quoted for comparison but flagged: the customer never owns the system, never receives the 30% credit, and payment/rate escalates annually — appropriate for a customer without tax appetite for the credit, not a default recommendation.

## 4. Proposal template (structure, filled with the worked-example deal)

```
PROPOSAL: 1842 Larkfield Ave — 6.0 kW PV + 10 kWh Battery
PREPARED BY: [Rep name, NABCEP cert #]        DATE: [date]

CURRENT STATE
  Annual usage: 11,000 kWh   Annual cost: $4,620   Rate schedule: PG&E E-TOU-C

RECOMMENDED SYSTEM
  6.0 kW DC array (18 × 333W panels) + 10 kWh battery
  Modeled production: 9,300 kWh/yr (PVWatts, derate stack: inverter 96%, wiring 2%,
    soiling 2%, shading per instrumented report)
  Degradation assumption: 0.5%/yr

PRICE
  Gross system price: $28,600 ($3.10/W equivalent, array + battery)
  Federal Residential Clean Energy Credit (30%): −$8,580
  Net price: $20,020

PROJECTED SAVINGS (assumptions stated, not buried)
  Utility rate escalation assumed: 3.0%/yr (EIA historical range 2.5–3.5%)
  Export value: PG&E Avoided Cost Calculator, current published rate
  Year 1 savings: $3,589   Simple payback: 5.6 years
  25-year cumulative savings (at stated escalation): [table, not headline-only]

ALTERNATIVE CONSIDERED AND REJECTED
  9.0 kW array, no battery: lower sticker ($18,900 net) but real payback 6.8 years —
  oversized relative to export compensation, rejected in favor of the design above.

INTERCONNECTION
  Rule 21 application → Permission to Operate: 6–10 weeks (PG&E territory average)

WHAT THIS PROPOSAL DOES NOT ASSUME
  No roof replacement needed (assessed at ~10yr practical remaining life)
  No panel upgrade needed (82A headroom on 200A service)
  Savings do not assume any future rate-design change beyond the 3%/yr baseline
```
