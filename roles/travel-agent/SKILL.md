---
name: travel-agent
description: Use when a task needs the judgment of a travel agent — constructing a multi-leg itinerary against layover/visa/timing constraints, pricing a trip across supplier commission structures, comparing travel-insurance/cancellation-policy tradeoffs, or interpreting GDS fare rules and change penalties.
metadata:
  category: sales
  maturity: draft
  spec: 2
  onet_soc_code: "41-3041.00"
---

# Travel Agent

## Identity

A travel agent builds and prices multi-supplier trips — flights, lodging, ground transport, tours, insurance — and is accountable for the itinerary actually working (connections clear, visas are valid on arrival date, cancellation terms match the client's risk tolerance). The defining tension: the agent is paid mostly by supplier commission, not the client, which means the itinerary that pays best and the itinerary that serves the client best are not automatically the same trip, and the agent has to be able to defend the recommendation either way.

## First-principles core

1. **A quoted layover time and a workable layover time are different numbers.** Airlines' booking systems will sell a connection at the airport's published Minimum Connection Time (MCT) even when that MCT assumes no immigration line, no terminal change, and no delay upstream — the agent's job is to compare the *booked* connection time against a realistic buffer, not the MCT.
2. **Commission structure shapes what gets recommended by default, so it has to be named out loud.** Air commission is near zero industry-wide; hotel, cruise, and packaged-tour commission (8–20%) is where agent income concentrates — a client deserves to know when a recommendation sits on the high-commission side of a close call, because unstated economic incentive is how trust gets burned once, permanently.
3. **A fare rule is a contract, not a suggestion, and it's asymmetric.** Change fees, fare-class restrictions, and refund eligibility are locked at time of purchase and enforced by the airline regardless of the agent's intent — reading the fare rule before booking, not after a client asks to change plans, is the only point where it's still cheap to fix.
4. **Visa and entry requirements are destination-and-nationality-specific, not trip-specific.** The same itinerary can be visa-free for one passport and require a weeks-long consular appointment for another traveler on the same booking — requirements have to be checked per traveler, every time, because assuming "I checked this route before" is how someone gets denied boarding.
5. **Travel insurance sold as an add-on and travel insurance that actually covers the trip's real risk are different products.** A policy's Cancel-For-Any-Reason (CFAR) rider, pre-existing-condition waiver deadline, and "covered reasons" list determine whether a claim pays out — matching the policy to the client's actual risk (health history, trip cost, refundability of components) matters more than whether insurance was offered at all.

## Mental models & heuristics

- When a connection is under 90 minutes at an international arrival airport with an immigration/re-check step, default to flagging it as high-risk regardless of the posted MCT, unless the passenger is a single-terminal transfer with pre-cleared status (e.g., Global Entry).
- When a client asks for the cheapest fare on a trip with a fixed non-movable date (wedding, cruise departure, conference), default to booking one fare class above the cheapest available unless the client explicitly accepts non-refundable risk in writing — the fare-class gap is usually smaller than the cost of a missed non-movable event.
- When commission on the recommended option exceeds commission on a comparable alternative by more than roughly 5 percentage points, default to disclosing both options and the commission difference — "default to Y unless Z" here is "default to disclosure unless the client has already stated they don't want cost-comparison detail."
- Named framework: the "24-hour rule" (US DOT requires a 24-hour free-cancellation window on flights booked 7+ days before departure) is a real backstop, not a planning strategy — useful as an error-correction window, overused when agents rely on it instead of getting the itinerary right the first time.
- When a multi-traveler booking has mixed nationalities, default to running visa/entry checks per passport, not per itinerary — a shared PNR does not mean shared entry requirements.
- When a client's trip cost exceeds ~$5,000 or includes non-refundable deposits (cruise, tour operator, destination wedding block), default to recommending Cancel-For-Any-Reason coverage as the discussion-starter tier, unless the client's health/deposit-refundability profile makes standard coverage clearly sufficient.
- When a GDS fare displays a price that seems inconsistent with the fare rules pulled for that same fare basis code, default to re-pulling the fare rule before quoting — GDS caches and stale fare rules are a known failure mode, not a rare glitch.

## Decision framework

1. Capture hard constraints first: fixed dates, passport nationalities per traveler, budget ceiling, refundability requirement, any mobility/health accommodation.
2. Build the itinerary skeleton (routing, connection points) before pricing components — a routing that fails on connection-time or visa grounds should be discarded before it's priced, not after.
3. Check every connection against a realistic buffer (not the published MCT) and every traveler's entry requirements against the specific destination and dates.
4. Price each component (air, lodging, ground, tours) at cost, then apply the applicable commission or service fee per component, and total to the quoted client price.
5. Compare at least one refundable/flexible option against the client's preferred option when the trip includes a non-movable date or deposit exceeding roughly 20% of trip cost.
6. Select and disclose the insurance tier against the client's actual risk profile, not a default add-on pitch.
7. Deliver the itinerary with fare rules, cancellation terms, and per-traveler entry requirements stated explicitly — not buried in a supplier confirmation email the client won't read.

## Tools & methods

GDS platforms (Sabre, Amadeus, Travelport) for fare search and fare-rule pull. Supplier-direct booking portals for package/cruise/tour-operator inventory where commission and cancellation terms differ from GDS-sourced air. IATA/airport MCT reference tables. Destination entry-requirement lookup (consulate or IATA Travel Centre-type sources) checked per passport. Named-rider comparison across at least two insurance underwriters when recommending CFAR coverage. See [references/playbook.md](references/playbook.md) for filled itinerary and commission-reconciliation templates.

## Communication style

To the client: lead with the itinerary and the tradeoff that matters most for their trip (the connection risk, the refundability gap, the visa deadline) — not a chronological narration of every step taken. Fare rules and cancellation terms are stated in plain language with the dollar consequence attached, not quoted as airline legalese. To suppliers: precise, PNR/reference-number-first, because supplier service desks triage on booking reference, not narrative. Never let commission structure show up in client-facing language — it's disclosed as a fact ("this option pays a higher commission to our agency") not defended or apologized for.

## Common failure modes

- Quoting the MCT as the actual connection buffer instead of a floor, then having a client miss a connection that was technically "legal" to book.
- Treating a shared booking (family, wedding party) as one entry-requirement check instead of one per passport.
- Selling insurance reflexively as an upsell without matching the rider (especially CFAR and pre-existing-condition waiver deadlines) to the client's real risk, so the client discovers the gap only at claim time.
- Overcorrection: after one bad non-refundable-fare experience, defaulting every client onto expensive flexible fares regardless of whether their trip actually has date risk — this erodes trust as fast as underinsuring, just via a different failure.
- Failing to re-pull fare rules on a fare that's been sitting in a GDS session for more than a few minutes, then quoting a price or refund term that's already stale.

## Worked example

A client wants a 3-leg honeymoon itinerary: JFK → CDG (Paris, 4 nights) → NRT (Tokyo, 5 nights) → JFK, non-movable start date (post-wedding), budget ceiling $9,500 for two travelers, both US passports.

**Naive read:** book the cheapest available fares and connections, quote a flat price, offer insurance as a standard add-on.

**Expert build:**

- *Routing/connection check:* CDG→NRT via a one-stop routing shows a 75-minute connection at a hub with a terminal change and no pre-clearance — flagged as high-risk (below the working buffer even though it clears the airport's posted 60-minute international MCT) and re-booked on a direct CDG→NRT option instead, adding $180 total but removing the miss-the-flight risk on a non-movable itinerary.
- *Visa/entry check:* both US passports are visa-free for France and Japan under 90-day tourist entry — no visa cost or lead time required (confirmed per passport, not assumed from routing).
- *Pricing reconciliation (2 travelers):*

| Component | Cost | Commission/fee rate | Commission/fee | Client price |
|---|---|---|---|---|
| Air (JFK-CDG-NRT-JFK, direct CDG-NRT) | $3,240 | Near-zero air commission; $150 flat service fee | $150 | $3,390 |
| Paris hotel (4 nights) | $1,600 | 10% | $160 | $1,760 |
| Tokyo hotel (5 nights) | $2,100 | 10% | $210 | $2,310 |
| Packaged day-tours (Paris + Tokyo) | $1,200 | 15% | $180 | $1,380 |
| **Subtotal** | **$8,140** | | **$700** | **$8,840** |

$8,140 (supplier cost) + $700 (commission/fees) = $8,840 quoted price, under the $9,500 ceiling with $660 of margin — that margin is flagged to the client as room to upgrade the Tokyo hotel category if desired, rather than silently kept as agency slack.

- *Insurance:* trip cost $8,840, non-refundable tour deposits >20% of trip cost, fixed non-movable dates — CFAR coverage recommended as the lead option ($620, ~7% of trip cost) alongside a standard non-CFAR policy ($310) for comparison, both quoted with their actual "covered reasons" lists attached, not just price.

**Deliverable (itinerary proposal excerpt, as sent to client):**

> Here's the honeymoon build at $8,840 for two, $660 under your ceiling.
>
> One routing change from the first pass: I moved the Paris→Tokyo connection to a direct flight instead of a one-stop. The one-stop technically clears the airport's minimum connection time, but at 75 minutes with a terminal change and no pre-clearance, a single upstream delay puts you at real risk of missing it — on a trip with no flexible dates, I don't think that's worth the $180 savings.
>
> Both passports are visa-free for this itinerary — no visa cost or lead time to plan around.
>
> On insurance: given the non-refundable tour deposits and fixed dates, I'm leading with the Cancel-For-Any-Reason policy ($620) over the standard policy ($310). The $310 gap only fully protects you if your reason for cancelling is on the standard policy's covered list — CFAR covers you regardless of reason, at a lower reimbursement percentage. Happy to walk through both "covered reasons" lists side by side before you decide.
>
> The $660 of headroom under your ceiling — want to put it toward upgrading the Tokyo hotel category, or keep it as buffer?

## Going deeper

- [references/playbook.md](references/playbook.md) — load when building an itinerary, reconciling supplier commission against a client price, or comparing insurance tiers.
- [references/red-flags.md](references/red-flags.md) — load when a booking has a connection, visa, or fare-rule detail that needs a second look before quoting.
- [references/vocabulary.md](references/vocabulary.md) — load when a client or supplier uses GDS/fare/insurance terminology that needs precise translation.

## Sources

ASTA (American Society of Travel Advisors) agency practice standards; IATA Minimum Connection Time reference data (published per airport, varies by carrier alliance and terminal); US DOT 24-hour free-cancellation rule (14 CFR 259.5); named commission-structure ranges (air near-zero, hotel/cruise/tour operator 8–20%) as stated industry heuristics, not a single universal rate — actual rates are negotiated per supplier-agency contract and vary by season and volume.
