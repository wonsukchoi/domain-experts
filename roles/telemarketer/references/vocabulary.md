# Vocabulary

Terms generalists conflate that a telemarketing practitioner keeps sharply separate — the value is in the misuse column.

## Prior express consent vs. prior express written consent

**Prior express consent** is sufficient under the TCPA for a live-agent call to a cell phone with no autodialer or prerecorded voice. **Prior express written consent** — a signed or e-signed disclosure, not just an opt-in checkbox — is required for any autodialed or prerecorded-voice call to a cell phone, including most predictive-dialer campaigns.

*In use:* "This list has consent for a live-agent dial, but not written consent — we can call it manually, we can't put it on the predictive dialer."

*Common misuse:* treating a general "yes, contact me" checkbox as sufficient for an autodialed campaign. It's sufficient for a live-agent call; it is not the written consent standard the predictive dialer requires.

## Predictive dialer vs. power dialer

A **predictive dialer** dials multiple lines ahead of agent availability based on a statistical model of expected answer rates, which creates abandoned-call risk when the model overshoots. A **power dialer** advances to the next number only once an agent is free, and carries no abandonment risk by design.

*In use:* "We're over our abandonment margin on the predictive dialer — move this list to power-dial mode until we retune the pacing."

*Common misuse:* using the terms interchangeably in a compliance conversation. The distinction is the entire reason one carries TSR abandonment-rate exposure and the other doesn't.

## Abandonment rate

The share of calls where a consumer answers but no live agent connects within 2 seconds of the greeting, measured across a rolling 30-day campaign — capped at 3% under the TSR.

*In use:* "Today's abandonment looked fine at 1.8%, but the 30-day rolling average is at 2.9% — we're one bad afternoon from a violation."

*Common misuse:* checking only a single day's number and calling the campaign compliant. The legal measure is the rolling 30-day average, not any single shift.

## National Do-Not-Call Registry vs. internal/company-specific Do-Not-Call list

The **National Registry** is the FTC-maintained list consumers join once, with no expiration, that any telemarketer must scrub against every 31 days. The **internal (entity-specific) Do-Not-Call list** is a company's own record of anyone who has told that specific company to stop calling, honored within 30 days of the request and kept regardless of National Registry status.

*In use:* "She's not on the National Registry, but she told us to stop calling in March — she goes on our internal list either way."

*Common misuse:* assuming a National Registry scrub covers a specific "remove me" request made directly to the company. The two lists are separate obligations, and a National scrub does not substitute for honoring a direct request.

## Right-party contact (RPC) vs. connect rate

**Connect rate** is the share of dials where any live person answers. **Right-party contact** is the narrower share where the person reached is actually the intended decision-maker — not a wrong number, not a household member who isn't the target, not a business's general line.

*In use:* "Connect rate looks fine at 32%, but RPC is only 60% of that — a third of our answers are wrong numbers, and that's a list problem, not an agent problem."

*Common misuse:* reporting connect rate as if it measures pitch opportunity. A high connect rate with a low RPC rate means most of those answers were never a viable pitch to begin with.

## Automatic Telephone Dialing System (ATDS)

The TCPA's statutory term for equipment that triggers written-consent requirements when calling cell phones. *Facebook, Inc. v. Duguid* (2021) narrowed the definition to systems that use a random or sequential number generator to store or produce numbers — meaningfully excluding some dialers that call from a curated list even if the dialing itself is automated.

*In use:* "Our dialer pulls from a fixed customer list, not a generator — legal's read is it may fall outside ATDS post-Duguid, but we're still treating cell numbers as written-consent-required until state law is checked."

*Common misuse:* assuming any automated dialing equipment is automatically an ATDS. The post-2021 legal definition is narrower than "the dialing is automated," and state mini-TCPA statutes often define it more broadly again — the federal narrowing doesn't travel to every state.

## Occupancy rate vs. utilization

**Occupancy rate** is the share of logged-in time an agent spends on a call or in after-call work, versus idle/available. **Utilization** is a broader efficiency measure that can include scheduling adherence and shrinkage, not just active-call time.

*In use:* "Occupancy is at 85% — that's fine, but if utilization is only 60%, the gap is scheduling, not call handling."

*Common misuse:* using the two as synonyms when diagnosing a productivity problem. A high-occupancy, low-utilization team has a different fix (scheduling) than a low-occupancy, high-utilization one (call flow or hold time).

## Talk time vs. after-call work (ACW) vs. handle time

**Talk time** is time actively on the call. **After-call work** is disposition-coding and notes done immediately after hanging up. **Handle time** is the sum of both, the number used for staffing math.

*In use:* "Handle time crept up, but talk time is flat — it's ACW that's grown, probably from the new disposition codes taking longer to select."

*Common misuse:* coaching agents on "handle time" as if it's a single skill. A handle-time problem rooted in slow disposition coding needs a UI or code-simplification fix, not a talking-faster fix.

## Established business relationship (EBR)

A prior transaction or inquiry within a defined lookback period (commonly 18 months for a purchase, 3 months for an inquiry, under FTC/FCC frameworks) that can support a call without a fresh Do-Not-Call check for that specific company, though it does not override autodialer written-consent requirements for cell calls.

*In use:* "She bought from us fourteen months ago — that's inside the 18-month EBR window for a live-agent call, but we still need written consent if this goes on the predictive dialer."

*Common misuse:* treating EBR as a blanket exemption from all telemarketing rules. It addresses the entity-specific Do-Not-Call obligation, not the separate autodialer/prerecorded-voice consent requirement.

## Safe harbor (Telemarketing Sales Rule)

A defined set of operating conditions — abandonment rate at or below 3% over 30 days, a recorded identification message on any abandoned call, records retained on pacing and abandonment — that, if met, protect a seller from liability for an occasional inadvertent DNC or abandonment miss. It is not blanket immunity; it requires the underlying practices to already be compliant.

*In use:* "We're inside safe-harbor pacing, but that only protects the occasional miss — it doesn't cover a list we never scrubbed at all."

*Common misuse:* treating "safe harbor" as meaning no violation can occur as long as the number is close to compliant. It's a defense for good-faith operational error, not a substitute for the underlying compliance work.
