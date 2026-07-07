# Fishing and Hunting Worker — Playbook

## Weather go/no-go threshold table (filled, by vessel class)

| Vessel class (length) | Tested safe-operating envelope | Icing-risk adjustment | Default action past envelope |
|---|---|---|---|
| <32 ft (skiff/small gillnetter) | 15-20 kt sustained, 3-4 ft seas | Any visible ice: reduce envelope by ~1/3 | No-go; no shortened-trip exception below 10 kt |
| 32-42 ft (longliner/small crabber) | 25-30 kt sustained, 6-8 ft seas | Air temp <32°F with spray: reduce to 20 kt / 5 ft | No-go, unless trip shortened to <10 nm from a hail-out anchorage |
| 43-58 ft (mid trawler/crabber) | 30-35 kt sustained, 8-10 ft seas | Active icing: reduce to 25 kt / 7 ft, chip-ice stops mandatory hourly | No-go past envelope; partial-day option only if icing absent |
| 58-79 ft (larger crabber/trawler) | 35-40 kt sustained, 10-12 ft seas | Active icing: reduce to 30 kt / 9 ft | No-go past envelope regardless of quota deadline |

Envelope figures come from the vessel's own USCG dockside stability letter, not this table — treat these ranges as the ballpark to sanity-check a specific boat's documented numbers against, not a substitute for reading the letter.

## Trip break-even worksheet (filled example)

| Line item | Formula | Example value |
|---|---|---|
| Expected landed weight | gear × soak time × grounds CPUE estimate | 2,600 lb |
| Ex-vessel price | quoted same-day by processor/buyer | $6.10/lb |
| Gross trip value | landed weight × price | $15,860 |
| Fuel cost | gallons burned × price/gal | 220 gal × $4.15 = $913 |
| Ice cost | lb loaded × price/lb | 600 lb × $0.18 = $108 |
| Bait cost | lb loaded × price/lb | 400 lb × $1.35 = $540 |
| IFQ cost-recovery fee | ~3% of ex-vessel value (NOAA standard fee, published annually) | $476 |
| **Net trip proceeds** | gross − (fuel + ice + bait + fee) | **$13,823** |
| Fuel-cost ratio (go/no-go dial) | fuel ÷ gross | 913 ÷ 15,860 = 5.8% — well under the 15-20% shorten-trip trigger |

If fuel-cost ratio comes in above ~15-20%, don't run the trip as planned — shorten to closer grounds or a single-day set and rerun the worksheet before committing fuel and bait spend.

## Crew-share settlement template (filled, longline 40/60 split)

| Recipient | Share rate | Basis | Amount |
|---|---|---|---|
| Boat (owner, covers fuel/gear/insurance/quota amortization) | 40% | Net trip proceeds | $5,529 |
| Owner, as working crew | 20% | Net trip proceeds | $2,765 |
| Crew member A | 20% | Net trip proceeds | $2,765 |
| Crew member B | 20% | Net trip proceeds | $2,765 |
| **Total distributed** | 100% | | **$13,824** (rounding) |

Settlement is only ever run against *net* proceeds (after fuel/ice/bait/fees), never gross — a crew member who checks the math against the gross landed-weight figure will come up short by exactly the operating-cost line and conclude, wrongly, that they were shorted. Post the full worksheet, not just the final share number, at every settlement.

## IFQ quota-balance and season-closure tracker (filled example)

| Trip # | Date | Quota balance before | Landed this trip | Quota balance after | Days remaining in season |
|---|---|---|---|---|---|
| 1 | Day 6-7 | 4,200 lb | 2,600 lb | 1,600 lb | 4 |
| 2 (contingent) | Day 8-9, if fishable | 1,600 lb | up to 1,600 lb | 0 lb (if fully landed) | 2 |
| — | Day 10-11, if trip 2 didn't run | 1,600 lb | 0 lb | 1,600 lb expires unlanded | 0 |

Track this after every trip, not just at season start — the "days remaining" column is what drives the go/no-go pressure calculation in the decision framework, and it changes after every landing, not just every calendar day.

## Bycatch/PSC (prohibited species catch) monitoring log (filled example)

| Set # | Target catch | Bycatch species | Bycatch this set | Running trip total | Fishery-wide cap remaining (as reported) | Action |
|---|---|---|---|---|---|---|
| 1 | Halibut, 340 lb | Pacific cod (non-target) | 40 lb | 40 lb | 85% of trip allowance remaining | Continue, same grounds |
| 2 | Halibut, 290 lb | Pacific cod | 65 lb | 105 lb | 60% of trip allowance remaining | Continue, monitor |
| 3 | Halibut, 310 lb | Pacific cod | 130 lb | 235 lb | 48% of trip allowance remaining | Move grounds — approaching the ~50% single-set trigger |

The trigger in the decision framework fires on the *rate of approach*, not just the raw remaining percentage — set 3's 130 lb bycatch on top of an already-rising trend is the signal to move, even though technically more than half the allowance remains.
