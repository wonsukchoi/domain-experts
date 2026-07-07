# Travel Agent — Red Flags

### Connection under 90 minutes at an international arrival airport with a re-clear step
- **Usually means:** the booking system sold at or near the airport's published MCT, which assumes no immigration line and no upstream delay.
- **First question:** "Is this a same-terminal transfer with pre-clearance, or does the passenger have to exit security and re-enter?"
- **Data to pull:** the specific airport's MCT table and terminal map for that connection, not a generic rule of thumb.

### Client accepts a non-refundable fare on a trip tied to a non-movable date
- **Usually means:** the client focused on price and didn't weigh the cost of a missed event against the fare-class savings.
- **First question:** "What happens to this trip's purpose if the date has to move — is there any flexibility on your end?"
- **Data to pull:** the fare difference between the non-refundable fare and the next refundable/flexible tier.

### Mixed-nationality booking treated as one entry-requirement check
- **Usually means:** the agent checked the destination's requirements once and applied the result to the whole PNR.
- **First question:** "What passport is each traveler on this booking holding?"
- **Data to pull:** per-passport entry-requirement lookup for the specific destination and travel dates.

### GDS fare rule pulled more than a few minutes before quoting
- **Usually means:** fare and availability data may have changed; GDS caches are not guaranteed live at the moment of quote.
- **First question:** "When was this fare rule last pulled — same session, or from an earlier search?"
- **Data to pull:** a fresh fare-rule pull immediately before quoting or booking.

### Insurance recommended without matching the rider to the client's actual risk
- **Usually means:** insurance was offered as a reflexive upsell rather than matched to trip cost, refundability, and health history.
- **First question:** "What's the largest non-refundable deposit on this trip, and does the client have any health condition that could affect a claim?"
- **Data to pull:** the policy's covered-reasons list and pre-existing-condition waiver deadline, compared against the client's actual situation.

### Commission on the recommended option is noticeably higher than a comparable alternative
- **Usually means:** the recommendation may be economically influenced rather than purely client-optimal — not necessarily wrong, but undisclosed is the problem.
- **First question:** "Have I shown the client the lower-commission comparable option, or only the one I'm recommending?"
- **Data to pull:** side-by-side commission rates across the comparable options considered.

### Client requests a same-day or near-minimum-connection change to an already-ticketed itinerary
- **Usually means:** the original booking's buffer assumptions no longer hold, or the client didn't understand the original connection risk.
- **First question:** "Is this change still inside the fare's change-penalty window, and does the new connection still clear the working buffer?"
- **Data to pull:** the fare's change-penalty terms and a fresh connection-buffer check on the proposed new routing.

### Cruise or tour-operator deposit exceeds 20% of total trip cost
- **Usually means:** cancellation exposure is concentrated in a non-refundable or partially-refundable deposit.
- **First question:** "What is the deposit's refund schedule, and does it match the client's confidence in these dates?"
- **Data to pull:** the supplier's deposit refund-schedule table (percentage recoverable by days-before-departure).

### Visa processing lead time is close to or exceeds the time remaining before departure
- **Usually means:** the itinerary was built before entry requirements were checked, or dates shifted after the visa timeline was already tight.
- **First question:** "Given today's date, does the consulate's stated processing time still leave margin before departure?"
- **Data to pull:** the specific consulate's current stated processing time (not a general country-level estimate, which can be stale).

### Client declines all insurance on a trip with a total cost above roughly $5,000
- **Usually means:** the client may be underestimating cancellation or medical-evacuation exposure, or the offer wasn't framed against their specific risk.
- **First question:** "What would happen financially if this trip had to be cancelled the week before departure?"
- **Data to pull:** the specific dollar exposure (non-refundable deposits + any pre-purchased components) if the trip cancelled at various points before departure.
