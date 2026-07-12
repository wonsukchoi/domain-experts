# Freight Forwarder — Red Flags

### Shipment ≥15 CBM quoted as LCL without an FCL comparison run
- **Usually means:** the forwarder is pricing off the shipper's request ("give me an LCL rate") rather than checking the breakeven, or hasn't recalculated revenue tons for this specific shipment.
- **First question:** "Have we compared this against a full-container rate at this volume?"
- **Data to pull:** the lane's current 20'/40' FCL all-in rate, and the shipment's computed revenue-ton LCL cost side by side.

### Incoterm on the PO doesn't match who's actually arranging each leg
- **Usually means:** the sales contract and the shipping instructions were written by different people who assumed different responsibility splits, or the term was copy-pasted from a prior deal without checking this routing.
- **First question:** "Who's named as shipper of record on the export declaration, and does that match who this Incoterm assigns to export clearance?"
- **Data to pull:** the sales contract's Incoterm clause, the shipping instructions, and the intended export filer.

### No confirmed cargo-ready date against the carrier's CY/doc/VGM cutoffs
- **Usually means:** the shipper hasn't been told the actual cutoff sequence, or is tracking production readiness against a different (later) date than the booking assumes.
- **First question:** "Is cargo gated in and VGM submitted by cutoff, or are we tracking toward a production date that's later than that?"
- **Data to pull:** the vessel schedule's CY, documentation, and VGM cutoff times for this specific sailing.

### Shipper unaware that demurrage/detention free time is running
- **Usually means:** nobody pushed the destination free-time deadline to the shipper at vessel arrival, so the first they hear of it is a per diem invoice.
- **First question:** "Who's clearing customs and picking up this container, and by what date does that need to happen?"
- **Data to pull:** carrier's published free-time tariff for the destination port, current customs entry status.

### High-value or regulated cargo (hazmat, temperature-controlled, high-value electronics) booked under a standard cargo quote
- **Usually means:** the commodity wasn't flagged during quoting, so the standard liability cap and standard equipment/handling don't actually match what's being shipped.
- **First question:** "Does the standard tariff cover this commodity class, or does it need a rider, special equipment, or separate cargo insurance?"
- **Data to pull:** the forwarder's cargo liability policy exclusions list, the commodity's HS classification and any hazmat/IMDG class.

### Declared value on the House Bill of Lading is materially lower than the commercial invoice value
- **Usually means:** the shipper is minimizing cargo insurance premium or duty exposure without realizing declared value also caps what the forwarder's liability will pay out on a claim.
- **First question:** "This declared value caps any claim payout at that figure even if the goods are worth more on the invoice — is that the number you want on record?"
- **Data to pull:** the commercial invoice value, the HBL's declared value field, the applicable liability-cap-per-kg for this trade lane.

### LCL consolidation shipper still shows "in transit to CFS" within 48 hours of vessel cutoff
- **Usually means:** the consolidation is at real risk of rolling to the next sailing, damaging every other shipper booked into the same container, not just the late one.
- **First question:** "What's this shipper's confirmed CFS receipt date, and does it clear the container's stuffing schedule?"
- **Data to pull:** CFS receiving log, the container's stuffing/cutoff schedule, alternative sailing availability if a roll is unavoidable.

### General Rate Increase (GRI) or Peak Season Surcharge (PSS) announced for the lane after a quote was issued but before booking
- **Usually means:** the quote is now stale — the base FAK rate the client was quoted no longer reflects what will actually be invoiced at sailing.
- **First question:** "Has a GRI or PSS been announced for this sailing week since we quoted?"
- **Data to pull:** carrier/alliance surcharge announcements for the relevant departure week, the quote's validity date.

### Cargo description on the booking is generic ("general cargo," "consumer goods") for a shipment that needs HS-code-specific handling
- **Usually means:** the commodity hasn't actually been classified, risking a customs hold or misdeclaration flag at destination that a domestic-only shipment wouldn't face.
- **First question:** "Do we have an HS code for this, or does the destination customs broker need to determine it before the shipment lands?"
- **Data to pull:** HS classification, destination-country import restrictions or licensing requirements for that code.

### Forwarder issuing its own House Bill of Lading without a current NVOCC tariff/bond on file for the trade lane
- **Usually means:** the forwarder is contracting as principal (assuming carrier-like liability) without the regulatory standing that makes that HBL enforceable, exposing both the forwarder and the shipper.
- **First question:** "Is our NVOCC registration and bond current for this trade lane, or are we issuing this HBL on stale registration?"
- **Data to pull:** current FMC OTI license/bond status (or equivalent regulator for the trade lane), the forwarder's published NVOCC tariff.
