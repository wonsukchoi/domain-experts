# Vocabulary

Terms generalists conflate that route servicers keep sharply separate.

## Par level vs. slot capacity

**Par level** is the computed restock target for a slot — average daily velocity times the days until the next visit, times a safety factor. **Slot capacity** is the physical maximum the tray or coil can hold. Par is usually below capacity; when it isn't, that's a signal, not a rounding error.

*In use:* "Par on that chips slot came out to 16.9, but capacity's only 10 — we're not under-restocking, the slot's undersized for this route's cycle."

*Common misuse:* restocking every slot to capacity by default and calling it "topping off," which ties up cash in slow SKUs and, on perishable slots, raises discard risk with no sales benefit.

## DEX (Data Exchange) vs. MDB (Multi-Drop Bus)

**DEX** is the data file format a vending machine exports summarizing vend counts, cash totals, and error events over a period — what telemetry platforms ingest for reporting. **MDB** is the live communication protocol between the machine's controller and its peripherals (bill validator, coin mechanism, card reader) in real time. DEX tells you what happened; MDB is how the machine and its peripherals talk while it's happening.

*In use:* "DEX shows the vend count, but if I want to know why the validator's rejecting bills right now, I'm pulling MDB-level diagnostics, not the DEX summary."

*Common misuse:* treating a DEX report as if it contains live peripheral-health data — it's a periodic summary, not a real-time diagnostic feed.

## TCS (time/temperature control for safety) product vs. shelf-stable product

**TCS product** requires specific temperature holding and has a defined maximum time above the safe threshold before mandatory discard (fresh sandwiches, dairy, salads). **Shelf-stable product** (chips, candy, canned drinks) has no such holding-time exposure. Only TCS slots carry the discard-on-excursion rule.

*In use:* "The chips slot doesn't care that the case ran warm for an hour — the sandwich slot next to it does, and those units are getting pulled."

*Common misuse:* applying visual/smell judgment to a TCS excursion, which substitutes an inspection for a documented time/temperature threshold that doesn't care how the product looks.

## First-insert acceptance rate vs. false-reject rate

**First-insert acceptance rate** is the percentage of bills or coins accepted on the first attempt. **False-reject rate** is the percentage of genuinely valid currency rejected by the mechanism. A validator can have a high acceptance rate and still have a creeping false-reject problem if customers are re-inserting the same bill multiple times before it's accepted.

*In use:* "Acceptance looks okay in the daily total, but the false-reject rate on first insert is climbing — customers are just trying twice, that's not the same as the validator being fine."

*Common misuse:* reading overall acceptance percentage as the whole health picture without checking first-insert performance specifically, which hides an emerging sensor or belt-wear problem.

## Cash variance vs. shrinkage

**Cash variance** is the dollar or percentage gap on a single visit between telemetry-expected cash and physical count. **Shrinkage** is the accumulated pattern of variances over time that indicates a persistent loss, whether from miscounting, mechanism fault, or custody breach. One variance is a data point; shrinkage is a trend across visits.

*In use:* "One visit's $25 variance is a ticket. Three visits running $20-plus on the same machine is shrinkage, and that's a different conversation."

*Common misuse:* dismissing each individual variance as "within normal counting error" without ever totaling them across a quarter, which is exactly how real shrinkage stays invisible.

## Route cycle vs. restock cycle

**Route cycle** is the fixed schedule on which a technician visits a given stop (e.g., Monday/Thursday, averaging 3.5 days). **Restock cycle** is how long a given slot's inventory is expected to last based on velocity — it can be shorter than the route cycle if the slot is undersized, which is the condition that triggers a par-vs-capacity review.

*In use:* "The route cycle here is 3.5 days, but this SKU's restock cycle is only 2.4 days at full capacity — that gap is where the lost sales are coming from."

*Common misuse:* assuming the route cycle and restock cycle are the same thing by design, when a mismatch between them is often the actual cause of a chronic stockout complaint.

## Coin mechanism jam vs. bill validator jam

A **coin mechanism jam** is typically a bent, foreign, or out-of-tolerance coin lodged in the coin path, mechanically distinct from a **bill validator jam**, which is usually a transport-belt or sensor issue with a bill (torn, folded, or a dirty optical path misreading a valid note). The two mechanisms, diagnostics, and OEM service procedures don't overlap.

*In use:* "Same machine, two different alarms today — coin jam was a foreign token, validator jam was belt debris. Neither fix applies to the other."

*Common misuse:* treating "jam" as one generic fault category and applying the same clear-and-test procedure to both, which misses mechanism-specific wear indicators each one actually has.

## Defrost cycle vs. compressor duty cycle

The **defrost cycle** periodically warms the evaporator coil to clear ice buildup, briefly raising internal case temperature by design. The **compressor duty cycle** is the normal on/off cooling pattern maintaining set temperature. A temperature excursion clustering right after defrost cycles points to the defrost interval or duration being miscalibrated, not a general refrigeration failure.

*In use:* "Three of the last four excursions logged right after a defrost — that's an interval problem, not the compressor failing."

*Common misuse:* diagnosing a general refrigeration fault (compressor, refrigerant) when the excursion pattern actually points specifically to defrost-cycle timing.

## Advance-exchange swap vs. bench repair (mechanism-level)

**Advance-exchange swap** replaces a whole failed mechanism (validator, coin mech, dispenser assembly) with a working unit on the spot, sending the faulty one out for depot repair later. **Bench repair** fixes the specific failed component in place or on a service bench without swapping the assembly. Route work skews toward swap because route time is expensive relative to component cost on most vending mechanisms — but a mechanism still under warranty or with a cheap, confirmed fix can make bench repair the better call.

*In use:* "Validator's swapped, faulty unit's going back on advance exchange — bench-repairing it here would burn the rest of today's route."

*Common misuse:* assuming swap is always cheaper because it's faster; on higher-cost assemblies with a simple confirmed fault, the swap can cost meaningfully more than the ten minutes a bench fix would take.

## Stop viability vs. machine uptime

**Machine uptime** measures whether a given unit is functioning. **Stop viability** measures whether that stop's revenue, net of route service cost, still justifies the visit frequency. A stop can show perfect uptime and still be economically marginal or negative.

*In use:* "Every machine at Stop C is running fine — the problem isn't uptime, it's that the stop's net contribution has been under threshold for two cycles running."

*Common misuse:* using uptime reports as a proxy for route health, which hides stops that are mechanically fine but no longer worth the visit cost.
