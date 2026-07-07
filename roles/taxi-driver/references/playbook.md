# Playbook

Filled procedures a taxi driver actually runs, with real thresholds and worked numbers. Adapt the numbers to a specific city's tariff and local demand pattern once actual history exists — these are the defaults to use before that history is built.

## 1. Utilization / deadhead calculation

Run this at least once mid-shift and again at shift end — not just as a final gut check.

**Inputs:** odometer reading at shift start and end (or checkpoint), revenue miles per trip (meter-on to meter-off), fuel cost, shift lease/gate fee.

**Worked example (18:00–04:00 shift):**

| Segment | Miles |
|---|---|
| 13 street-hail/app trips, ~4 mi avg | 52 revenue mi |
| 1 airport flat-rate trip (JFK–Midtown) | 15 revenue mi |
| **Total revenue miles** | **67** |
| Total odometer miles, full shift | 195 |
| **Deadhead miles (195 − 67)** | **128** |
| **Utilization = 67 ÷ 195** | **≈ 34%** |

**Benchmark:** traditional street-hail taxis have historically run 30–40% utilization; app-matched rides in the same markets run closer to 55%. Below ~35%, treat it as a signal to change positioning strategy for the rest of the shift, not as a normal night.

**Cost reconciliation:**

Gas: 195 mi ÷ 30 mpg (hybrid sedan) × $3.50/gal ≈ $23.
Lease/gate fee (10-hr shift): $130.
Gross fares + tips: $290.
**Net = $290 − $130 − $23 = $137 → $13.70/hour** — the number that matters, not the $290 gross.

## 2. Flat-rate vs. metered fare check

Run this before starting the meter or quoting a price, every trip that could plausibly match a filed flat-rate zone (airport-to-core-city trips are the most common).

1. **Identify origin, destination, and direction.** Filed flat rates are direction-specific — a flat rate from the airport to a defined zone does not automatically apply in reverse.
2. **Check the filed tariff for an exact match** (e.g., a specific airport code and a specific named zone or borough, both directions listed separately in the tariff).
3. **If it matches exactly:** charge the flat rate, full stop — even if the meter would clearly run higher in traffic. Overcharging a filed flat-rate trip by running the meter instead is a fineable violation regardless of which number is bigger that day.
4. **If it doesn't match exactly** (wrong direction, destination just outside the filed zone, different airport terminal not covered): default to metered.
5. **Tolls and passthrough surcharges are separate from the fare rule** — they're owed on top of either the metered or flat fare and aren't a reason to second-guess which fare rule applies.

**Worked comparison:**

| | Flat rate (filed) | Metered equivalent that trip |
|---|---|---|
| JFK → Midtown Manhattan | $70 | ≈ $95 (heavy traffic) |

The flat rate governs. Charging $95 here isn't "getting a better rate" — it's an overcharge complaint waiting to be filed, and TLC-style flat-rate violations commonly carry a fine plus a point against the license, which costs far more than the apparent $25 difference.

## 3. Hail-acceptance safety screen

Run silently, in seconds, on every hail — not just the ones that already feel off.

| Factor | Lower risk | Higher risk |
|---|---|---|
| Hour | Daytime / early evening | Late night (roughly midnight–5 AM) |
| Location | Well-lit, populated block | Isolated, unlit, or unfamiliar block |
| Destination stated | Before doors lock | Refused or vague until underway |
| Passenger presentation | Calm, sober | Visibly agitated, intoxicated, or aggressive at the window |

**Rule of thumb:** one higher-risk factor alone is routine and usually fine. Two or more stacking together is where a veteran driver verifies the destination out loud before pulling away, waits for a second passenger to join, or declines the hail outright — the screen runs the same way regardless of how uneventful the last fifty hails were.

## 4. De-escalation ladder (fare dispute or aggressive passenger)

1. **Verbal redirect** — calmly restate the fare rule ("this route is the filed flat rate, it's on the receipt") without arguing the amount itself.
2. **Cite the printed record** — meter printout or flat-rate receipt — as the neutral third party in the dispute, not the driver's word against the passenger's.
3. **Move toward the nearest safe, public, well-lit stop** (not the current isolated spot) while the conversation continues — don't stop to argue mid-route in a dead zone.
4. **If it doesn't de-escalate, involve dispatch or authorities** from the safe stop, not from wherever the dispute started.

Skipping straight to confrontation, or negotiating the fare amount curbside in an isolated location, is the failure mode this ladder exists to prevent.

## 5. Positioning strategy by utilization trend

| Shift utilization so far | Default positioning move |
|---|---|
| At or above ~45% | Continue current mix of cruising and app-matching; whatever's working |
| 35–45% | Start favoring app/e-hail matches for the next block of the shift over speculative cruising |
| Below ~35% | Switch fully to app-matched positioning, or stage at a known feeder point (transit hub, hotel line, airport holding lot) rather than cruising residential or low-demand streets |

**Feeder-point staging:** when heading to a known high-demand point, factor in the deadhead cost of getting there — staging at an airport holding lot only pays off if the queue wait plus trip-pass rules produce a net utilization gain over cruising, not just a longer single fare.

## 6. Licensing and inspection renewal calendar (illustrative cadence)

| Requirement | Typical cadence |
|---|---|
| Vehicle safety/meter inspection | Every 4 months to annually, by jurisdiction |
| Driver license/permit renewal | Every 1–3 years, by jurisdiction |
| In-vehicle GPS/camera/payment system certification | At vehicle registration and after any hardware swap |

Confirm exact cadence and forms against the local licensing authority — cadences vary by city/state and this table is a planning skeleton, not a substitute for the filed local rule.
