# Vocabulary

Terms generalists conflate that a relay/substation technician keeps sharply separate, because the difference changes what's actually being verified or protected.

## Dependability vs. security (protection-system attributes)

**Dependability** is a protection scheme's certainty of operating correctly when it should. **Security** is its certainty of *not* operating when it shouldn't. The two trade against each other — a scheme tuned purely for dependability (fast, sensitive) risks nuisance trips; one tuned purely for security (slower, more supervisory checks) risks a slow or missed trip on a real fault.

**In use:** "Adding that supervisory logic buys us security against nuisance trips on load swings, but it costs us dependability if the actual fault current sits right at that supervisory threshold — that's the tradeoff we're signing off on, not a free improvement."

**Common misuse:** treating a scheme change as strictly "better protection" without naming which attribute it improves and which it costs.

## Coordination time interval (CTI) vs. pickup tolerance

**Pickup tolerance** is how close an individual relay's trip threshold must land to its own setpoint (e.g., ±5%). **Coordination time interval** is the time margin between two adjacent relays' operating times at a given fault current, covering breaker interrupting time and relay overtravel, so the closer device trips first. A relay can pass its own pickup tolerance and still violate CTI with its neighbor.

**In use:** "Pickup's fine at 2% off — the problem is CTI to the upstream relay is down to 0.15 seconds after that setting change, and that's below where we're comfortable."

**Common misuse:** signing off a relay test as "coordinated" because the individual relay passed its own tolerance, without re-checking the margin against its neighbors.

## Total dissolved combustible gas (TDCG) vs. key gas

**TDCG** is the summed concentration of combustible gases (H2, CH4, C2H2, C2H4, C2H6, CO) dissolved in transformer oil, banded into IEEE C57.104 condition levels. **Key gas** is which specific gas is elevated or rising, which points to a fault type (acetylene → arcing, ethylene/ethane → thermal, hydrogen → partial discharge). A transformer can be in a "normal" TDCG band while its key-gas pattern already signals a specific developing fault.

**In use:** "TDCG's still Condition 1, but acetylene's the gas that moved — that's an arcing signature, not just aging, regardless of what band the total sits in."

**Common misuse:** reporting only the TDCG condition level and treating it as the complete diagnosis, without naming which gas actually drove the number.

## Duval/IEC ratio method vs. absolute gas level

The **ratio method** (Duval triangle or IEC 60599 ratios) classifies fault type from the *relative proportions* of specific gases to each other, independent of the absolute concentration. **Absolute gas level** (TDCG, individual ppm) drives urgency and condition banding. A high ratio-method confidence in "arcing fault" can coexist with a still-moderate absolute TDCG — the ratio says what's happening, the absolute level says how far along it is.

**In use:** "The ratio method says this is a high-energy arcing fault pattern — TDCG's only Condition 2 today, but that's a statement about progress, not about fault type."

**Common misuse:** using an elevated absolute TDCG alone to conclude "arcing," when the ratio/key-gas pattern actually points to a thermal fault, or vice versa.

## Primary injection vs. secondary injection (relay testing)

**Secondary injection** applies test current/voltage directly to the relay's input terminals, testing the relay in isolation from the current transformer (CT) and wiring. **Primary injection** passes current through the actual primary circuit and CT, testing the relay, the CT ratio and polarity, and the wiring between them together. A relay can pass every secondary-injection test while a CT wiring or polarity error still causes a misoperation on an actual fault.

**In use:** "Secondary injection's clean, but we haven't primary-injected since the CT was replaced last outage — that's still an open question on this scheme."

**Common misuse:** treating a passed secondary-injection test as full verification of the protection scheme, when it doesn't touch the CT circuit at all.

## Differential protection vs. sudden-pressure protection

**Differential protection** is an electrical scheme comparing current in and current out of a protected zone (a transformer, a bus) — a mismatch beyond a set threshold indicates an internal fault. **Sudden-pressure protection** is a mechanical device detecting a rapid pressure change inside the transformer tank, typically from arcing or a fault generating gas rapidly. The two detect the same category of event through different physics, and a transformer's protection is not complete with only one.

**In use:** "Differential's been quiet, but the sudden-pressure relay alarmed — that's the mechanical detection catching something the electrical comparison hasn't crossed threshold on yet."

**Common misuse:** treating differential protection alone as sufficient transformer protection, or dismissing a sudden-pressure alarm because differential hasn't also operated.

## Stored energy (breaker mechanism) vs. electrical lockout/tagout

**Electrical lockout/tagout** isolates and verifies the absence of voltage in the circuit a breaker switches. **Stored mechanical/pneumatic energy** — a charged closing spring, pressurized SF6, a hydraulic accumulator — exists independently in the breaker's operating mechanism and can move contacts or components even after the electrical circuit is dead and grounded. Substation breaker work requires both, verified separately.

**In use:** "Electrical LOTO's done and it's grounded, but the spring's still charged — block it or discharge it before anyone's hands go near that mechanism."

**Common misuse:** treating "electrically locked out" as equivalent to "mechanically safe to work," skipping the stored-energy check as if it were covered by the electrical step.

## Misoperation vs. correct operation for the wrong reason

A **misoperation** is any protection-system operation (or failure to operate) that deviates from the intended design response to an event — including a relay that trips correctly but for a different fault than the one that actually occurred, or one that should have tripped and didn't. **Correct operation for the wrong reason** — a relay that trips and clears the fault, but via a scheme or path that wasn't the intended primary protection — still counts as a misoperation for investigation purposes (per NERC PRC-004) even though the outcome looked fine.

**In use:** "The breaker did open and the fault cleared, but it was backup protection that operated, not the primary zone — that's still a misoperation we have to report and root-cause, not a save."

**Common misuse:** closing out an event as "no misoperation" because the fault cleared and no customer noticed, without checking whether the intended primary scheme was actually the one that acted.

## Switching order vs. clearance/hold tag (substation scale)

**Switching order** is the sequence of breaker/switch operations to reach a target bus configuration. **Clearance (or hold) tag** authorizes a specific crew to work a specific isolated section once that configuration is reached — same distinction as outdoor line work, but at substation scale the switching order routinely involves multiple sources and bus ties, making independent verification of the order itself, not just the tag, a separate required step.

**In use:** "The switching order gets independently checked against today's bus configuration before anyone throws a switch — the tag only matters once we're actually at the configuration the order was written for."

**Common misuse:** independently verifying only the clearance tag (who's authorized to work) while assuming the switching order itself (which devices, in what sequence) was correct as written.
