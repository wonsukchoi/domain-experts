# Vocabulary

Terms generalists flatten together that a transportation engineer keeps sharply separate — the value is in the misuse, not the definition.

## Level of service (LOS) vs. volume-to-capacity (v/c) ratio

**LOS** is a lettered grade (A–F) derived from a delay (signalized/unsignalized) or density (freeway) calculation. **v/c** is the ratio of demand flow to capacity. A movement can have v/c well under 1.0 and still carry a poor LOS grade, because LOS is a delay-based measure, not a simple capacity-headroom number.

**In use:** "v/c is only 0.14, but the delay calc still puts this at LOS C — capacity headroom and LOS aren't the same finding."

**Common misuse:** treating a low v/c ratio as proof the LOS grade must also be favorable, skipping the actual delay computation.

## Design speed vs. posted speed vs. operating (85th-percentile) speed

Three distinct values. **Design speed** governs geometric design elements (sight distance, curve radius, superelevation). **Posted speed** is the legal/regulatory limit. **Operating speed** (85th percentile) is what drivers actually do, measured in the field.

**In use:** "Posted speed is 45, but the 85th-percentile study came back at 51 — geometric checks run against 51, not the sign."

**Common misuse:** using posted speed for a geometric design check when no operating-speed study has been run, silently removing the design's safety margin.

## Design hour volume (DHV) vs. K-factor

**DHV** is the traffic volume used for design, typically the 30th-highest hourly volume of the year (30HV) — high enough to represent recurring peak conditions without designing for a rare extreme. **K-factor** expresses that DHV as a fraction of annual average daily traffic (AADT).

**In use:** "AADT is 18,000 and K is 0.10, so DHV = 1,800 — that's the volume the geometric design has to handle, not the daily average."

**Common misuse:** designing capacity around AADT directly instead of converting through the K-factor to an actual design hour volume.

## Trip generation vs. trip distribution vs. trip assignment

Three sequential steps. **Generation** answers how many trips a land use produces. **Distribution** answers where those trips go. **Assignment** answers which specific route or turning movement each trip uses. Skipping steps means using an earlier step's output as if it already answered a later step's question.

**In use:** "Generation gives us 110 new trips — we still have to distribute and assign before that number means anything at a specific driveway movement."

**Common misuse:** applying a gross generation number directly as a driveway turning-movement volume without distributing or assigning it first.

## Pass-by trip vs. diverted-linked trip vs. primary trip

**Pass-by trips** are already on the adjacent street and simply stop in en route. **Diverted-linked trips** detour off a nearby route to access the site. **Primary trips** are made specifically for that destination. Each gets a different treatment in a capacity analysis.

**In use:** "That shopping-center rate has a 34% pass-by component — those trips reduce the corridor's new-trip total but still show up as driveway turning movements."

**Common misuse:** treating all reduced (non-primary) trips the same way, or applying the pass-by reduction to driveway volumes where it doesn't belong.

## Critical gap vs. follow-up time (unsignalized capacity)

**Critical gap** is the minimum gap in major-street traffic a minor-street driver will accept to complete a maneuver. **Follow-up time** is the headway between successive minor-street vehicles using that same accepted gap. Both feed the HCM unsignalized capacity formula but represent different driver behaviors.

**In use:** "Critical gap of 7.5 seconds and follow-up of 3.5 — two different numbers in the capacity formula, not interchangeable."

**Common misuse:** using one value for both terms, or citing a single "gap acceptance" number as if the formula only needs one input.

## Warranted vs. justified vs. mandated

A **warrant** being met means a numeric or engineering threshold is satisfied, authorizing the agency to *consider* the improvement. It is not by itself **justification** (weighing secondary effects) and does not **mandate** construction.

**In use:** "The left-turn lane volume warrant is met — that gets it on the table for consideration, it doesn't obligate the agency to build it tomorrow."

**Common misuse:** treating a met warrant as an automatic requirement to build, skipping the engineering-judgment step entirely.

## Functional classification

The categorization of a roadway (arterial, collector, local) by its role in the network — mobility versus land access — that determines the applicable design standards, access-spacing policy, and typical design speed range for that facility.

**In use:** "It's classified as a minor arterial, so the agency's access-spacing standard applies at 660 ft, not the local-street 150 ft spacing."

**Common misuse:** assuming a road's design standards follow from its physical appearance or number of lanes rather than its adopted functional classification.

## Stopping sight distance (SSD) vs. intersection sight distance (ISD)

**SSD** is the distance a driver needs to perceive and stop for an object in the roadway ahead. **ISD** is the distance needed to safely complete a turning or crossing maneuver at an intersection. Different formulas, different governing exhibit in the Green Book, and passing one says nothing about the other.

**In use:** "SSD checks out along the mainline, but ISD at the side-street approach still needs its own calculation."

**Common misuse:** running only the SSD table check at an intersection and assuming it also covers the intersection sight-distance requirement.

## Peak hour factor (PHF)

The ratio of the full hourly volume to four times the peak 15-minute volume within that hour — a measure of how sharply demand peaks within the hour. A PHF near 1.0 means flat demand; a low PHF (roughly 0.80–0.85) means a sharp 15-minute surge.

**In use:** "PHF came in at 0.82 — there's a real 15-minute surge inside that hour, and the capacity check needs to reflect that peaking, not the hourly average."

**Common misuse:** running a capacity analysis on the raw hourly volume without applying PHF, understating the actual peak-15-minute demand the intersection has to handle.

## Highway Capacity Manual (HCM) LOS vs. Highway Safety Manual (HSM) crash prediction

Two separate AASHTO/TRB-published methodologies measuring different things — HCM measures operational delay/density, HSM predicts crash frequency. A location can be LOS-acceptable and safety-deficient at the same time.

**In use:** "HCM says LOS C, but HSM's predicted crash frequency for this configuration is above the state average for the facility type — those are two different findings that both need reporting."

**Common misuse:** treating a favorable HCM LOS result as evidence the location is also safe, when no HSM analysis was run.

## Crash modification factor (CMF)

A multiplier, sourced from the FHWA CMF Clearinghouse, applied to a baseline predicted crash frequency to estimate a specific countermeasure's effect. A CMF of 0.75 means the countermeasure is associated with an estimated 25% crash reduction on average — not a guaranteed outcome at any single location.

**In use:** "Adding the left-turn lane carries a CMF around 0.65 for left-turn crashes at this configuration — that's the expected reduction, not a certainty."

**Common misuse:** stating a CMF-based reduction as a deterministic outcome rather than an average estimated effect from the underlying research studies.

## Access management

The practice of controlling the location, spacing, and design of driveways and intersections along a roadway to preserve through-traffic capacity and safety. Distinct from site access design, which is one project's input into the broader access-management policy for that corridor.

**In use:** "The agency's access-management plan caps driveway spacing at 440 ft on this corridor — the site plan has to fit inside that, not the other way around."

**Common misuse:** treating access management as a synonym for a single site's driveway design rather than the corridor-wide spacing and consolidation policy it actually is.

## Storage length vs. taper length (turn lane)

**Storage length** is the queue-holding portion of a turn lane, sized to the 95th-percentile queue from the capacity analysis. **Taper length** is the transition geometry moving a vehicle from the through lane into the storage lane, sized to design speed. Undersizing each produces a different failure.

**In use:** "Storage is sized to the 95th-percentile queue, but the taper still needs its own check against design speed — they fail in different ways if undersized."

**Common misuse:** sizing only the storage length and treating the taper as a fixed, minor detail that doesn't need its own calculation.
