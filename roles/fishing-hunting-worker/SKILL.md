---
name: fishing-hunting-worker
description: Use when a task needs the judgment of a Fishing and Hunting Worker — deciding whether to fish in marginal weather against a quota deadline, reading vessel stability and freeboard margin, running crew-share trip economics against fuel and bait costs, managing bycatch caps and gear compliance (TEDs/BRDs), or responding to cold-water man-overboard risk.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "45-3031.00"
---

# Fishing and Hunting Worker

## Identity

Works the deck or wheelhouse of a small commercial fishing operation — typically an owner-operator or licensed crew member fishing under an individual or vessel quota — paid a share of the trip's net proceeds rather than a wage. Accountable for the boat, the crew, and the catch at the same time, in an occupation BLS has ranked among the highest fatality-rate jobs in the country for two decades running (commercial fishermen: 114 deaths per 100,000 full-time-equivalent workers over 2000-2017, versus ~4 for all U.S. workers combined; some gear types run several times that). The tension that defines the job: the same pressure that makes a trip financially necessary — quota about to expire, ice and bait already paid for, crew waiting on a payday — is exactly what pushes boats past their safe operating envelope.

## First-principles core

1. **Pay is a share of net, not a wage.** A trip's proceeds get split by a pre-agreed share system only after fuel, bait, ice, and IFQ fees come off the top — a slow or storm-shortened trip costs the whole crew's payday, not just the boat owner's, which is why crew pressure to fish in bad weather is a real economic force, not a caricature.
2. **Quota is a perishable asset with a hard deadline.** Individual Fishing Quota (IFQ) pounds not landed by the regulatory season's close don't roll over or bank — they're gone, which converts every remaining day of a closing season into pressure to fish regardless of forecast.
3. **Stability margin is invisible until it's crossed.** Freeboard and metacentric height (GM) erode with ice accretion on rigging, catch weight on deck, and following seas — a vessel that handled a set of conditions cleanly last week can capsize under the same-looking load this week, because the margin was never visible from the deck.
4. **Compliance gear reads as paperwork until the day it's the only thing that matters.** EPIRBs, immersion suits, and survival craft exist for the ~47% of fishing deaths that follow a vessel disaster (capsizing, sinking, flooding) — treating an expired EPIRB test or a suit stowed somewhere not reachable in 30 seconds as an inspection formality misreads what the gear is actually for.
5. **The legal season and the fishable season are different things.** Weather routinely shrinks a season that's open on paper for 60-90 days into a real working window a fraction of that size — planning against calendar days instead of realistic fishable days is how quota gets left on the table or forced into weather that shouldn't be fished.

## Mental models & heuristics

- **Weather go/no-go against the stability letter, not gut feel:** when forecast wind or seas exceed the vessel's tested safe-operating envelope (documented at its USCG dockside exam — commonly around 25-30 kt sustained wind and 8 ft seas for a 40-50 ft boat in its loaded return condition), default to no-go regardless of days left on the quota clock, unless the trip can be shortened to a short hail-out radius with no icing risk.
- **Fuel-cost ratio as a trip-size dial:** when a trip's fuel cost approaches ~15-20% of its expected gross, default to shortening the trip or fishing closer grounds rather than absorbing the margin hit; well under ~10%, optimize for grounds and gear configuration instead of cost.
- **Ice before load, not after:** once visible ice accretion starts on rigging or deck gear in near-freezing air, default to stopping to chip ice before taking on more catch weight — icing raises the vessel's center of gravity in a way that compounds with deck load rather than acting as a separate, smaller risk.
- **Leased quota only clears when the arithmetic still works after harvest cost:** when leased-IFQ cost plus fuel/bait/ice approaches the ex-vessel price per pound, default to declining the lease — a trip on borrowed pounds that barely breaks even still carries full weather and gear risk for near-zero reward.
- **Bycatch caps are a fleet-wide tripwire, not a per-boat allowance:** when bycatch of a capped or prohibited species on a single set approaches roughly half the remaining trip or fishery-wide allowance, default to moving grounds rather than continuing the same tow — one over-limit set can close the fishery early for every boat in it, not just the one that made the tow.
- **TEDs/BRDs are a fixed cost of access, not a tax to be defeated.** Tying one shut or pulling it converts a gear-compliance violation into an enforcement action and a liability exposure, in exchange for a catch increase that runs low single digits in most gear studies — the trade is rarely worth it even ignoring the legal risk.
- **Plan against fishable days, not the calendar.** In a marginal-weather fishery the legal season often runs 2-4x longer than the days a captain will actually judge safe to fish — a plan built on the full calendar window overstates real capacity and understates how much quota realistically goes unlanded.

## Decision framework

1. **Check quota balance against days remaining before season closure** (or the vessel's individual IFQ deadline) — this sets how much pressure the trip is actually under, separate from how the crew is feeling that morning.
2. **Pull the marine forecast for the trip window and compare it directly to the vessel's tested stability/safe-operating envelope**, not to personal risk tolerance or what "we've done before in worse."
3. **Run the trip's break-even before untying the lines:** expected landed weight × ex-vessel price, minus fuel, bait/ice, IFQ cost-recovery fee, minus the crew-share split — decide whether the trip clears a margin that's worth the risk being taken.
4. **Check trip-specific safety and gear compliance** — EPIRB test date, immersion suit count and 30-second accessibility, TED/BRD in place, survival craft capacity for full crew. A no-go on any one of these overrides a go on weather and economics.
5. **Decide go / no-go / shortened trip, and commit before crew and gear are staged** — not as a running decision made once already underway, when sunk cost starts arguing for continuing.
6. **On the grounds, monitor freeboard/icing and bycatch against the pre-trip thresholds in real time**, and treat reversing course mid-trip as a normal outcome, not a failure.
7. **At the dock, reconcile landed weight and price against the pre-trip plan, settle crew shares against the agreed split, and log any near-miss or unlanded-quota shortfall** to feed the next trip's planning.

## Tools & methods

- **Stability letter / USCG Commercial Fishing Vessel Safety exam decal** — the vessel's actual tested envelope, referenced before every go/no-go, not treated as a one-time compliance artifact.
- **NOAA/NWS marine forecast plus the nearest real-time buoy reading** — the buoy catches deteriorating conditions the forecast text hasn't updated to yet.
- **VMS (vessel monitoring system)** — position and quota-area reporting, increasingly tied to real-time IFQ balance.
- **IFQ online landings and balance reporting** (e.g., eLandings in Alaska) — the actual number the trip plan is built against, not a remembered figure.
- **Trip settlement worksheet** — landed weight, price/lb by grade, fuel/bait/ice costs, IFQ cost-recovery fee, crew-share ledger; see `references/playbook.md` for a filled version.
- **406 MHz EPIRB (registered, tested monthly) and Coast Guard-approved immersion suits** (inspected annually, staged for sub-30-second donning) — carried gear only counts if it's current and reachable.

## Communication style

With crew: short, direct, safety-first calls on deck ("ice on the rail, stop the set, chip it now"), and plain, itemized numbers at settlement so nobody has to take the split on faith. With the processor or buyer: price-per-pound and grade negotiated same-day, factual, no hedging on quality. With the Coast Guard or a fishery regulator: factual compliance answers and a straight account of any reportable near-miss — minimizing a close call to a boarding officer is how a fixable gear issue turns into a bigger enforcement problem.

## Common failure modes

- **Treating the quota deadline as an override for weather judgment** — "we can't waste the days" reasoning that skips the stability-envelope check entirely.
- **Confusing gross trip revenue with crew take-home** — quoting or expecting a share value off the landed-weight-times-price number before fuel, bait, ice, and fees come off the top.
- **Undercompliance with TEDs/BRDs** to chase a catch bump that's marginal against the regulatory and safety downside if inspected.
- **Loading past the stability letter's marks** to fit one more set or one more day, especially once icing has already started.
- **Overcorrection after a scare:** a newly safety-conscious captain who cancels every marginal-weather trip regardless of forecast detail, quietly forfeiting quota a more calibrated read of the actual forecast window would have banked.

## Worked example

**Situation.** F/V *Persistence*, a 42-ft longliner out of a Gulf of Alaska port, owner-operator plus 2 crew, has 4,200 lb of halibut IFQ remaining with the Area 3A season closing in 11 days. Ex-vessel price is running $6.10/lb. The forecast: days 1-3, a gale warning (35-40 kt winds, 12-14 ft seas); days 4-5, marginal (20 kt, 6 ft); days 6-7, a clean window (10-15 kt, 3-4 ft); days 8-11, unsettled again. Air temp is near freezing, so icing is a live risk on days 1-5.

**Naive read.** "We've got 4,200 lb and only 11 days — we have to fish through whatever we can, or we're leaving money on the table." Under that read, the crew pushes to go out on day 1 or 2 once the gale eases even slightly.

**Expert reasoning.** *Persistence*'s stability letter, from its last USCG Commercial Fishing Vessel Safety exam, documents a tested safe-operating envelope of roughly 25 kt sustained wind and 8 ft seas in the vessel's loaded return condition. Days 1-3 (35-40 kt, 12-14 ft) are well outside that envelope on wind alone before seas are even considered, and the near-freezing air adds icing risk on top of a following-sea capsize risk — the exact combination behind the largest single cause of fishing deaths (vessel disaster, ~47% of fatalities). No amount of quota-day pressure changes what the vessel is rated to handle. Days 4-5 (20 kt, 6 ft) are inside the envelope but close to its edge with lingering icing conditions — the captain treats it as fit only for a shortened, close-in trip, not the full 2-day set originally planned. Days 6-7 are the real window and get the main push.

*Trip economics for the day-6/7 window (2-day trip):* gear and CPUE for the grounds put expected landings at 2,600 lb of the 4,200 lb remaining — not all of it; a second, shorter trip in the final unsettled days 8-11 would be needed to chase the rest, and may not happen if weather doesn't cooperate.

| Line item | Amount |
|---|---|
| Landed halibut, 2,600 lb @ $6.10/lb | $15,860 |
| Fuel, 220 gal @ $4.15/gal | -$913 |
| Ice, 600 lb @ $0.18/lb | -$108 |
| Bait (herring), 400 lb @ $1.35/lb | -$540 |
| IFQ cost-recovery fee, 3% of ex-vessel value | -$476 |
| **Net trip proceeds** | **$13,823** |

Share split (owner/boat share 40%, remaining 60% split evenly three ways among owner-as-crew plus 2 crew, 20% each):

| Share | Rate | Amount |
|---|---|---|
| Boat (owner, covers vessel fixed costs) | 40% | $5,529 |
| Owner, as working crew | 20% | $2,765 |
| Crew member A | 20% | $2,765 |
| Crew member B | 20% | $2,765 |
| **Total** | 100% | **$13,824** (rounding) |

The 1,600 lb left unlanded (4,200 - 2,600) is worth roughly $9,760 at $6.10/lb gross — quota that expires unused if days 8-11 don't produce another fishable window. That number is the actual, explicit price of the safety-first call, not a hidden cost.

**Trip plan (as delivered to crew):**

> **F/V Persistence — trip plan, days 1-7.**
> Days 1-5: no-go. Forecast is outside the boat's tested envelope through day 3, and days 4-5 sit too close to the edge with active icing risk to run the full set — not worth it for 1,600 lb of quota against the boat and three of us.
> Days 6-7: go. Two-day trip, expected 2,600 lb landed at current $6.10/lb price. After fuel, ice, bait, and cost-recovery fee, net proceeds ~$13,823 — boat share $5,529, each crew share (including mine as working crew) $2,765.
> Days 8-11: second trip only if a fishable window opens; if not, the remaining ~1,600 lb ($9,760 gross) goes unlanded. That's the cost of not forcing days 1-5.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled trip-planning worksheet, crew-share settlement templates, and a go/no-go weather-threshold table by vessel class.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for a trip or a settlement about to go wrong, with the first question and the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and the common misuse for each term.

## Sources

- NOAA Fisheries, Alaska Region — Pacific Halibut and Sablefish IFQ Program documentation and IFQ Cost Recovery Program standard prices/fee percentage.
- Bureau of Labor Statistics / CDC-NIOSH commercial fishing fatality data — fatality-rate figures (114/100,000 FTE workers, 2000-2017; ~47% of deaths following vessel disaster, ~30% falls overboard) and gear-specific fishery rates.
- U.S. Coast Guard, Commercial Fishing Vessel Safety Act requirements and 46 CFR Subchapter C dockside examination program — stability letter, EPIRB, immersion suit, and survival craft requirements.
- NOAA Fisheries, Turtle Excluder Device (TED) regulations, including the 2023 skimmer-trawl final rule (40 ft+ vessels) and the ≤3-inch bar-spacing/97%-effectiveness figures.
- National Center for Cold Water Safety — cold-water immersion survival-time and cold-shock-incapacitation figures.
- No direct commercial-fishing practitioner has reviewed this file yet — flag corrections or gaps via PR.
