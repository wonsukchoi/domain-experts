# Red flags

Smells a veteran avionics technician catches reviewing a squawk history, an install job, or a logbook before signing anything.

### Nav/comm or autopilot fault logged "operational check good" three or more times

- **Usually means:** an intermittent fault living in the dynamic domain (vibration, thermal cycling, bus transient) that a static ground check never reproduces — the underlying condition is still present.
- **First question:** "What flight phase or electrical event was actually happening at each logged occurrence, per the fault-history timestamps?"
- **Data to pull:** LRU internal fault-history log with timestamps; maintenance data downloader or dispatch log for the same flights; any other system on the same bus with recent squawks.

### Bonding strap reading above roughly 3 mΩ on a milliohmmeter

- **Usually means:** surface contamination (anodize, paint, corrosion) at the strap-to-structure interface, not a failed strap itself — cleaning and reseating the interface usually restores spec, replacing the strap alone often doesn't.
- **First question:** "Was this measured at the actual interface, or mid-strap?"
- **Data to pull:** the specific measurement point and reading; last time this strap was disturbed (panel removal, prior work in the zone); whether any recent intermittent squawk shares a system on the same ground point.

### Data/signal wire bundle routed within roughly 1 inch of a power or high-current lead over an unshielded run

- **Usually means:** either an install shortcut taken under a tight-bay constraint without a manufacturer-credited exception, or bundle sag that closed the gap after the original install passed inspection.
- **First question:** "Is there a twisted-shielded-pair or conduit exception on file for this run, or is this just uncorrected sag?"
- **Data to pull:** the original install drawing's specified separation; current measured separation at the closest point (not just the clamped ends); the manufacturer's install manual for any shielding-based exception.

### Field approval requested for an alteration the shop plans to repeat across more than one or two aircraft

- **Usually means:** the shop is treating a genuine one-off approval path as a shortcut around STC cost for what is now a production alteration — FSDOs are guided away from approving repeat field approvals for the same change.
- **First question:** "How many aircraft is this alteration actually going on, total?"
- **Data to pull:** the fleet program plan; whether an AML or single-aircraft STC already exists for this equipment/airframe combination; the shop's historical FSDO turnaround time for this type of submission.

### Replacement avionics box installed because it's "compatible," not because it's on the covering STC's parts list

- **Usually means:** a bolt-in, powers-up substitution that hasn't been checked against the STC's approved parts list or TSO letter — an unapproved alteration even though it functions.
- **First question:** "Is this exact part number and TSO letter listed on the STC's installation drawing, or just functionally similar to what's listed?"
- **Data to pull:** the STC's approved parts list; the new unit's TSO authorization letter; whether the wiring interface (pinout, connector type) matches the STC drawing exactly.

### New LRU installed in an unpressurized or unheated bay with no DO-160 temperature/altitude category check

- **Usually means:** the equipment's environmental qualification basis was never cross-checked against the actual install zone — the box may be qualified only for pressurized-cabin conditions.
- **First question:** "What's this equipment's DO-160 Section 4 qualification range, and what's the actual temperature/altitude extreme in this bay?"
- **Data to pull:** the equipment's environmental qualification form (EQF); the aircraft's zone temperature data at operating ceiling; the STC or install manual's stated mounting-location restrictions.

### Avionics work log entry with no repairman certificate number or repair-station reference

- **Usually means:** either the signer's authority for this specific scope was never verified, or the entry was rushed and the paperwork was an afterthought.
- **First question:** "Whose certificate, issued by which repair station, actually covers this scope of work?"
- **Data to pull:** the entry against the 14 CFR 43.9 required-content checklist; the repair station's roster of repairman certificates and their scope limitations; shift/duty roster for who performed the work.

### Circuit breaker for the same avionics system resets more than once in a single flight

- **Usually means:** a real overcurrent or short condition, not a nuisance trip — resetting and continuing without investigation risks a wiring fault propagating to an arc or fire condition.
- **First question:** "Was this breaker reset in flight, and by whom, and is that documented as a discrepancy or just a verbal mention?"
- **Data to pull:** the discrepancy log for this breaker/system; wiring diagram for what else shares this circuit; any recent work in the zone that could have introduced a short.

### GPS/WAAS or comm antenna coax connector shows corrosion or discoloration at the interface

- **Usually means:** moisture intrusion at the connector, which degrades signal before it causes an outright fault — often the real cause behind a "weak signal" or "occasional RAIM" squawk that reads fine on a bench-tested cable.
- **First question:** "Has this connector been opened and inspected, or only continuity-tested through the connector?"
- **Data to pull:** connector inspection photos/notes; antenna coax routing for low points where water could pool; squawk history correlated with weather conditions (rain, high humidity).

### Navigation database or software cycle not current before releasing an IFR-capable system to service

- **Usually means:** a scheduling gap in the update process, not a technical fault — the system will function but isn't legal for the procedures it's being relied on for.
- **First question:** "What cycle is loaded, and what's the current effective cycle?"
- **Data to pull:** the system's currently loaded database cycle date; the update log for this tail number; whether the operator's ops specs require a specific update interval.
