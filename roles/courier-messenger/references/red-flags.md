# Courier and Messenger — Red Flags

### Route sequenced by nearest-distance when any stop has a hard deadline
- **Usually means:** dispatch or route software defaulted to distance-minimization without factoring in deadlines, or the courier resequenced manually without checking window feasibility.
- **First question:** "Does any stop on this route have a hard delivery window, and does the current sequence hit all of them?"
- **Data to pull:** the route manifest's deadline column against the sequenced stop order and drive-time estimates.

### Chain-of-custody item left unattended for any duration, even briefly
- **Usually means:** time pressure led to a "quick stop" (fuel, restroom, second errand) with the item left in an unlocked or unmonitored vehicle.
- **First question:** "Was the item in continuous, documented custody the entire time?"
- **Data to pull:** the custody log's timestamp gaps against the courier's actual route timeline (GPS/telematics if available).

### Proof-of-delivery logged after the shift ends rather than at time of delivery
- **Usually means:** volume pressure pushed logging to a batch task at day's end, degrading accuracy of timestamps and circumstance details.
- **First question:** "Was this logged at the door, or reconstructed later?"
- **Data to pull:** system timestamp on the log entry vs. the GPS timestamp at that stop's location.

### Signature-required item delivered without a signature ("left with neighbor," "left at door")
- **Usually means:** the manifest's proof-of-delivery requirement was overridden in the field because the named recipient wasn't available and the courier substituted a lower-evidentiary option.
- **First question:** "Did the manifest authorize this fallback, or did the courier choose it unprompted?"
- **Data to pull:** the manifest's specified proof-of-delivery type against what was actually captured.

### Delay notification sent after a missed window instead of before
- **Usually means:** the courier didn't recognize slippage until arrival, or recognized it but didn't flag it up the chain in time for the recipient to adjust.
- **First question:** "At what point did the delay become knowable, and when was it actually communicated?"
- **Data to pull:** route telematics timestamp when cumulative delay crossed a flag-worthy threshold vs. the timestamp of the notification sent.

### Refused or no-answer delivery resolved without checking the manifest's fallback instruction
- **Usually means:** the courier improvised a resolution (left with a different person, returned without attempting the specified reattempt) rather than following the sender's pre-written plan.
- **First question:** "What does the manifest say to do in this exact exception scenario?"
- **Data to pull:** the manifest's fallback-instruction field for that item against the exception-resolution log.

### An item on the manifest closes the route with no final status
- **Usually means:** the item was overlooked in the reconciliation step, or its status was assumed rather than confirmed.
- **First question:** "Is this item delivered, an exception, or still in the vehicle — and how do we know?"
- **Data to pull:** end-of-route manifest reconciliation against the vehicle's physical contents.

### Cold-chain or temperature-sensitive item's transport time exceeds its stated stability window
- **Usually means:** a route delay pushed total transit time past the specimen or product's viability window without anyone flagging it.
- **First question:** "What's the item's maximum stable transit time, and how does actual elapsed time compare?"
- **Data to pull:** pickup timestamp, delivery timestamp, and the item's documented stability-window specification.

### Same courier repeatedly reports "running behind" on the same route structure
- **Usually means:** either the route's time-window assumptions are unrealistic (traffic patterns, stop-service-time underestimated) or a specific stop consistently causes friction (access issues, recipient unavailability pattern).
- **First question:** "Is this a one-off delay pattern, or does this specific route/stop fail its estimate repeatedly?"
- **Data to pull:** delay logs for this route over the last 2-4 weeks, isolated by stop.
