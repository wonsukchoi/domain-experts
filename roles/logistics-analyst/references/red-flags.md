### A carrier's quoted rate is meaningfully lower than competitors on a lane with a known accessorial or claims history
- **Usually means:** The low quote may not reflect the full total landed cost once historical accessorials or damage claims for that carrier on this lane are factored in.
- **First question:** What is this carrier's historical average accessorial add-on and damage claim rate on this specific lane?
- **Data to pull:** Freight audit history for this carrier/lane, damage claims log.

### A freight invoice's accessorial charges don't match what's documented on the bill of lading
- **Usually means:** A billing error (mischarge, duplicate accessorial, incorrect classification) — common enough to be a systematic, recoverable pattern rather than a one-off.
- **First question:** Does the BOL support the specific accessorial charge being billed (e.g., liftgate, residential delivery, reweigh)?
- **Data to pull:** Bill of lading, carrier invoice, contracted accessorial fee schedule.

### A shipment is routed via FTL (full truckload) despite weight and cube well under a full trailer's practical capacity
- **Usually means:** The mode-selection breakeven wasn't recalculated for this specific shipment, or a habitual/contractual default is being applied without checking current economics.
- **First question:** What is the actual weight/cube breakeven for this lane, and does this shipment's profile justify FTL over LTL?
- **Data to pull:** Current LTL and FTL contracted rates for this lane, shipment weight/cube.

### Carrier on-time performance is reported using the carrier's own tracking-event definition rather than appointment-level delivery
- **Usually means:** The reported OTIF may not reflect actual customer-facing service failures — a shipment can be "on-time" by carrier definition while missing the customer's required delivery window.
- **First question:** Is this OTIF figure measured against the actual delivery appointment window, or against a carrier-internal milestone (e.g., arrival at terminal)?
- **Data to pull:** Delivery appointment records, carrier's tracking-event log for the same shipments.

### A carrier or lane cost/performance trend is based on a small sample (under ~20-30 shipments or less than a month)
- **Usually means:** Normal week-to-week variation may be getting read as a meaningful trend.
- **First question:** How many shipments and what time period does this trend cover?
- **Data to pull:** Full shipment count and date range underlying the reported trend.

### A dedicated FTL contract is proposed for a lane with historically low or irregular volume
- **Usually means:** The contract's per-unit rate advantage depends on utilization assumptions this lane's actual volume pattern won't support.
- **First question:** What is this lane's actual monthly shipment volume and variability over the past 6-12 months?
- **Data to pull:** Lane volume history, proposed contract's minimum-volume or utilization terms.

### A carrier scorecard shows improving cost but no corresponding OTIF or damage-claim data for the same period
- **Usually means:** A cost improvement in isolation can mask a service-level or damage-rate tradeoff that offsets the savings once expected costs are included.
- **First question:** What is this carrier's OTIF and damage-claim rate for the same period the cost improvement covers?
- **Data to pull:** Combined carrier scorecard (cost, OTIF, damage rate) for the matching period.

### Freight audit recovery has not been performed on a carrier relationship in over a quarter
- **Usually means:** Billing errors are very likely to be accumulating unrecovered, since audit programs typically find and recover errors on a recurring basis, not as a one-time event.
- **First question:** When was the last freight audit performed on this carrier's invoices, and what was recovered?
- **Data to pull:** Freight audit log and recovery history by carrier.
