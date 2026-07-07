# Vocabulary

Terms generalists conflate that field-service practitioners keep sharply separate.

## Response time vs. resolution time

**Response time** is the interval from ticket open to technician on-site and acknowledged. **Resolution time** (also "restore time") is the interval from ticket open to fault verified cleared and ticket closed. A contract can define separate SLA windows for each, and they are scored independently.

*In use:* "We hit response at 78 minutes, well inside the 2-hour window — but resolution ran to 4 hours 40 on a 4-hour tier. That's still a breach."

*Common misuse:* treating "on-site on time" as if the SLA obligation is satisfied. Dispatch reports that only track response time hide resolution breaches until the invoice's service-credit line shows up.

## MTBF vs. MTTR vs. availability

**MTBF** (mean time between failures) measures reliability — total operating time divided by number of failures. **MTTR** (mean time to repair/resolve) measures serviceability — total downtime divided by number of incidents. **Availability** combines both: MTBF ÷ (MTBF + MTTR).

*In use:* "MTTR's fine at 2.5 hours, but MTBF dropped from 30,000 to 19,000 notes this quarter — availability is falling even though the repair number looks good."

*Common misuse:* reporting MTTR alone as "reliability." MTTR measures how fast you fix things, not how often they break — a fleet can hit every MTTR target while getting less reliable.

## FRU (field-replaceable unit) vs. component-level repair

An **FRU** is a whole assembly or module designed to be swapped as a unit in the field (dispenser module, control board, power supply). **Component-level repair** replaces or repairs the specific failed part within that assembly (a gear, a capacitor, a belt) without swapping the whole unit — typically bench work, not always field-executable.

*In use:* "The board's bad, but it's one blown capacitor — bench repair is $40 in parts against a $310 FRU. If the SLA window allows it, repair it."

*Common misuse:* assuming FRU swap is always faster and therefore always right — it's faster and more certain, not automatically cheaper or the correct call when the remaining SLA window has room for the diagnosis.

## Break-fix vs. preventive maintenance (PM)

**Break-fix** is reactive service performed after a fault occurs. **PM** is scheduled service performed on an interval (cycle count, page count, or calendar) intended to prevent the failure before it happens. PM intervals are set from OEM wear data, not from a technician's convenience.

*In use:* "This unit's been on pure break-fix for six months because the PM got skipped twice — that's why it's failing in bursts now instead of gracefully."

*Common misuse:* treating PM as a discretionary visit that can slip when the schedule is tight. Deferred PM doesn't show up as a cost until the deferred failures arrive in a cluster, at which point it looks like an unrelated reliability crisis.

## Two-person integrity (TPI) vs. dual custody

**Two-person integrity** requires two authorized people physically present for the entire duration a control (like a cash compartment) is open. **Dual custody** is the broader principle that no single person has unilateral control over a cash asset end-to-end (e.g., one person holds the combination, another holds the key). TPI is the specific field-service execution of the dual-custody principle.

*In use:* "TPI was broken for four minutes when the second custodian stepped out to take a call — that's a variance investigation regardless of whether the count came back clean."

*Common misuse:* treating "a second person was in the building" as satisfying TPI. TPI requires continuous presence for the compartment-open window, not general on-site coverage.

## Cash cassette vs. reject bin vs. cash cartridge

The **cash cassette** is the removable, lockable container loaded with notes for dispensing. The **reject bin** captures notes the dispenser mechanism rejects during a transaction (miscounted, damaged, doubled notes) — it is not a dispensing source and fills over time as a normal part of operation. **Cash cartridge** is vendor-specific terminology some OEMs use interchangeably with cassette; it is not a third physical component.

*In use:* "The E-052 wasn't a cassette problem — the reject bin was at capacity from a missed collection cycle, which is a completely different fix."

*Common misuse:* assuming any dispenser-adjacent alarm means the cassette itself is faulty, which sends the diagnosis toward a swap when the actual cause is a bin that just needs emptying.

## Jam rate vs. MCBF (mean cycles between failure)

**Jam rate** is a short-window operational metric — jams per some count of transactions, useful for spotting an emerging problem on one asset. **MCBF** is the OEM's rated reliability spec for a mechanism across its expected service life, used for fleet planning and PM-interval setting, not for judging a single unit's current health.

*In use:* "Its jam rate this month is triple the OEM's MCBF-implied rate — that's not bad luck, that's a wear signature."

*Common misuse:* comparing a single unit's short-term jam count directly against the fleet-wide MCBF spec without normalizing for that unit's actual transaction volume, which makes a high-volume branch look artificially unreliable.

## Root cause vs. proximate cause

**Proximate cause** is the immediate mechanical event that produced the fault (the reject bin was full). **Root cause** is why that event occurred (the branch's collection cycle was set for a lower transaction volume than the branch now runs). Closing a ticket on the proximate cause fixes today's call; only the root cause prevents the next one.

*In use:* "Proximate cause: bin full. Root cause: this branch's transaction volume grew 40% since the collection schedule was set, and nobody updated it."

*Common misuse:* logging only the proximate cause as "resolved" — it clears the ticket but leaves the underlying condition to generate the next call, and erases the data a PM review would need to catch the pattern.

## NBD (next business day) vs. 8×5 vs. 24×7 coverage

**NBD** specifies the resolution deadline as the following business day, not a fixed hour count. **8×5** and **24×7** describe when a technician is dispatchable at all — business hours only versus around the clock. A Tier-2 NBD/8×5 contract has no obligation to respond at 11pm Friday for a Saturday failure; a Tier-1 24×7 contract does.

*In use:* "This is an off-premise ATM, Tier-2, NBD under 8×5 coverage — it went down Friday night, so the clock doesn't start until Monday morning."

*Common misuse:* assuming every SLA implies round-the-clock coverage. Coverage window and resolution deadline are two separate contract terms that have to be read together.

## Advance exchange vs. depot repair

**Advance exchange** ships a working replacement unit before the faulty one is returned, minimizing field downtime. **Depot repair** sends the faulty unit to a repair center and returns it once fixed, which is cheaper per unit but adds shipping and queue time the field SLA usually can't absorb.

*In use:* "We're on advance exchange for dispenser modules — the depot-repair turnaround is nine days, way outside any resolution window we carry."

*Common misuse:* assuming depot repair is simply "the slow version of the same thing" rather than a different logistics model with its own cost and stocking implications for the depot's spare-unit pool.
