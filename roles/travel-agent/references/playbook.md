# Travel Agent — Playbook

## Itinerary-build sequence

1. **Constraint capture** — fixed dates, passport(s), budget ceiling, refundability requirement, accommodation needs. Write these down before touching the GDS; they're the filter for every routing option that follows.
2. **Routing skeleton** — build the connection chain first, unpriced. Discard any routing that fails the connection-buffer check or a visa/entry check before pricing it.
3. **Connection-buffer check** — compare booked connection time against a working buffer, not the airport's published MCT:

| Connection type | Published MCT (typical) | Working buffer (recommend) |
|---|---|---|
| Domestic → domestic, same terminal | 30–45 min | 60 min |
| Domestic → domestic, terminal change | 45–60 min | 75 min |
| International → domestic (with immigration/customs) | 60–90 min | 120 min |
| International → international, no re-clear | 45–75 min | 90 min |
| International → international, with re-clear/visa check | 90 min | 150 min |

If the booked connection is below the working buffer, either re-route or flag explicitly to the client as accepted risk in writing.

4. **Per-traveler visa/entry check** — one row per passport, not one row per booking:

| Traveler | Passport | Destination | Requirement | Lead time |
|---|---|---|---|---|
| Traveler A | US | France (Schengen) | Visa-free, 90-day tourist | None |
| Traveler B | US | France (Schengen) | Visa-free, 90-day tourist | None |
| Traveler A | US | Japan | Visa-free, 90-day tourist | None |

(For a mixed-nationality booking, this table would show different requirement/lead-time values per row — that's the case it's designed to catch.)

5. **Pricing reconciliation** — every component priced at supplier cost, then commission/fee applied, summed to client price:

| Component | Supplier cost | Rate | Commission/fee | Client price |
|---|---|---|---|---|
| Air | $X | ~0% + flat service fee | $ | $ |
| Lodging | $X | 8–12% typical | $ | $ |
| Cruise | $X | 10–16% typical | $ | $ |
| Packaged tour | $X | 10–20% typical | $ | $ |
| **Total** | **$** | | **$** | **$** |

Subtotal (supplier cost) + commission/fee column must sum exactly to the client-price column total. Any margin between client price and budget ceiling is stated to the client, not absorbed silently.

6. **Insurance-tier comparison** — present at least two tiers side by side when trip cost or non-refundable deposit exceeds the CFAR-discussion threshold:

| Tier | Premium (typical %) | Covered reasons | Reimbursement if CFAR-triggered |
|---|---|---|---|
| Standard | 4–7% of trip cost | Named list (illness, death in family, weather closure, etc.) | N/A |
| Cancel For Any Reason (CFAR) | 6–10% of trip cost (often standard + 40–60%) | Any reason, must be purchased within 14–21 days of initial trip deposit | Typically 50–75% of trip cost, not 100% |

7. **Deliverable** — itinerary proposal stating routing changes and why, per-traveler entry requirements, fare rules/change penalties in plain language, and insurance recommendation with the tradeoff named, not just offered.

## Fare-rule quick-read checklist

- Fare basis code and booking class match what's actually being sold (re-pull if the GDS session is more than a few minutes old).
- Change penalty amount and whether it's a flat fee or fare-difference-plus-fee.
- Refund eligibility: fully refundable, refundable-with-penalty, or non-refundable.
- Advance-purchase and minimum/maximum-stay restrictions that could conflict with the client's actual dates.
- Whether the fare qualifies for the 24-hour DOT free-cancellation window (only applies to bookings made 7+ days before departure, US-originating).

## Commission-disclosure trigger

Disclose both options and the commission gap to the client when:
- Commission on the recommended option exceeds a comparable alternative by more than ~5 percentage points, OR
- The recommended option is the highest-commission option among 3+ comparable choices presented.
