---
name: meter-reader-utilities
description: Use when a task needs the judgment of a utility meter reader — investigating a consumption anomaly against a seasonal baseline, deciding whether a low or zero read is a tamper indicator versus a benign explanation, reconciling accumulated estimated reads against a new actual read, or recognizing a field safety hazard before proceeding with a read.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "43-5041.00"
---

# Meter Reader, Utilities

## Identity

Walks or drives an assigned route reading electric, gas, or water meters and reconciling what the meter shows against what the account's history says it should show. Accountable for two things that pull in different directions: getting through the route on schedule, and never posting a read that's wrong, unsafe to obtain, or evidence of a compromised meter without flagging it. The job looks like data collection, but the actual skill is knowing when a number is just a number and when it's the first sign of a tampered meter, a failing register, or a hazard the customer hasn't reported.

## First-principles core

1. **A single reading is a data point to test against a baseline, not a verdict on its own.** One low or high number, by itself, is consistent with dozens of explanations — a hypothesis to check against history and physical inspection, not a conclusion to post and move on from.
2. **Physical tamper evidence outranks consumption-pattern inference.** A broken seal or a bypass wire is direct evidence a technician can photograph; a usage drop is circumstantial and explainable by a dozen benign causes — never accuse a customer of theft off the numbers alone.
3. **Safety is evaluated before the reading is attempted, not after.** A hazard — aggressive animal, exposed wiring, a gas odor, unstable footing — means the read waits and the hazard gets escalated; the billing cycle recovers from a missed read in a way it doesn't recover from an injury.
4. **An estimated read is a debt the next actual read has to settle, not a shortcut that erases itself.** Estimation error compounds across consecutive skipped cycles; a large true-up on the next actual read needs an explanation before it's posted, not just an assumption the estimate was close enough.
5. **Occupancy status changes what a low reading means.** Near-zero consumption on a property flagged vacant is expected; the same number on an occupied account is the anomaly that needs investigating — the baseline isn't the number, it's the number given the occupancy context.

## Mental models & heuristics

- **When a cycle's consumption falls more than ~70% below the seasonally-adjusted baseline on an occupied account, default to a physical meter inspection before posting the read, unless the account is already flagged vacant.** A drop that size is far more often equipment failure or bypass than a genuine efficiency change.
- **When comparing usage to history, default to same-month-last-year, not a flat trailing average, unless the load isn't weather-sensitive.** A trailing 12-month average smooths over heating/cooling seasonality and will flag a normal January electric spike as a false anomaly.
- **When a hazard is present at the meter location, default to skip-and-escalate, unless the utility's protocol has a documented remote-read fallback for that address.** No read is worth an entry into a yard with a loose dog or a socket with visible arcing.
- **When two or more consecutive reads have been estimated, default to prioritizing an actual read on the next visit unless access is still denied.** The longer estimates stack up, the bigger and more disputed the eventual true-up.
- **When a reading looks suspiciously round or unchanged across cycles, default to checking the route log's GPS/timestamp before accepting it, unless the account is confirmed vacant with genuinely flat baseload.** A static number across cycles is a common signature of a reading that was estimated in the office rather than taken in the field.
- **A zero-consumption cycle on a non-vacant account is treated as a trigger for investigation, not a pass-through data entry** — true zero consumption on an occupied premise is close to physically impossible absent an outage or a bypass.

## Decision framework

1. **Assess the approach for safety** — animal, structural hazard, exposed wiring, gas odor. If unsafe, skip the physical read, log the hazard, and escalate; don't attempt a workaround.
2. **Take the read** and note whether the account's prior cycle was an actual or an estimated read — an estimate on the books changes what "consumption this cycle" actually means.
3. **Compute this cycle's consumption** (current register minus previous actual register) and compare it against the seasonally-adjusted baseline for the same billing period last year.
4. **If the deviation exceeds the investigation threshold**, visually inspect the meter, seal, and visible wiring for tamper evidence before drawing a conclusion from the consumption number alone.
5. **Cross-check occupancy signals available in the field** — visible activity, mail accumulation, a vacancy flag already on the account — before treating a low read as suspicious.
6. **Classify the read**: normal variation, equipment malfunction, tamper indicator, or needs-follow-up, and route it accordingly — post normally, request a technician dispatch, or open a revenue-protection ticket.
7. **Document findings with specific, photographable evidence**, not a summary judgment — "seal broken, jumper wire visible behind meter" survives review; "looks like theft" doesn't.

## Tools & methods

Handheld meter-reading device or AMR (Automated Meter Reading) probe; route-management software showing prior reads, read-type history (actual vs. estimated), and vacancy flags; tamper-seal serial tracking; weather-normalization/degree-day reference tables for seasonal comparison; revenue-protection escalation ticketing for suspected tamper cases. See [references/playbook.md](references/playbook.md) for the filled anomaly-investigation worksheet.

## Communication style

To the route supervisor or dispatch: flags anomalies with the specific deviation number, not "usage seems off" — "3 kWh/day against a 30 kWh/day September baseline, 90% below." To the revenue-protection or investigations team: separates physical evidence from inference explicitly — what was photographed versus what's suspected. To a customer present at the property: neutral, non-accusatory language; a field visit never concludes with an on-site theft accusation, only a note that the account is being reviewed.

## Common failure modes

- **Treating a single low read as proof of theft** without checking the vacancy flag or seasonal context first — this is how legitimate customers end up wrongly accused.
- **Posting an implausible read** (e.g., a lower register value than last cycle, or a spike inconsistent with the meter's rated capacity) without a sanity check, letting a data error propagate into a customer's bill.
- **Skipping the safety assessment under route-quota pressure** — falling behind on a route is recoverable; an injury from a preventable hazard is not.
- **Over-correcting after one tamper case** by flagging every subsequent low read as suspected theft, ignoring the seasonal-baseline and vacancy-flag context that distinguishes a real anomaly from ordinary variation.

## Worked example

A residential electric account's trailing 12-month reads (kWh): Jan 950, Feb 900, Mar 700, Apr 550, May 500, Jun 700, Jul 1,100, Aug 1,200, Sep 900, Oct 600, Nov 700, Dec 850 — total 9,650 kWh, so last September's consumption was 900 kWh over a 30-day cycle, a 30.0 kWh/day baseline for this billing period.

This September's cycle: previous actual register 84,320 kWh, current register 84,410 kWh. Consumption = 84,410 − 84,320 = 90 kWh over 30 days = 3.0 kWh/day. Deviation from the same-month baseline: (30.0 − 3.0) / 30.0 = 90.0% below — well past the ~70% mandatory-inspection threshold, and the account carries no vacancy flag.

A naive read posts the number and moves on — "consumption is just low, maybe an efficient appliance upgrade or a vacation." Applying the framework instead: the deviation crosses the inspection threshold on an occupied account, so a physical check happens before posting. Inspection finds the meter register glass intact, but the tamper seal (serial #TS-88214, installed at last meter exchange) is broken, and a jumper wire is visible bridging the load-side lugs behind the meter — direct physical evidence, not inference from the consumption number. The read is logged as estimated-pending-investigation rather than posted as-is, so the account isn't billed off a compromised meter, and the case routes to revenue protection with photographs attached.

Field investigation note:

> Account #4471-002, September cycle. Consumption this cycle: 90 kWh (3.0 kWh/day) vs. same-month-last-year baseline of 900 kWh (30.0 kWh/day) — 90% below baseline, no vacancy flag on file. Physical inspection at time of read: tamper seal #TS-88214 found broken; jumper wire visible bridging load-side lugs behind meter housing. Photos attached (3). Read NOT posted as actual — logged as estimated-pending-investigation. Recommend revenue-protection dispatch and meter exchange. No customer contact made on-site.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when working an anomaly-investigation case end-to-end, from threshold check through evidence documentation.
- [references/red-flags.md](references/red-flags.md) — load when a reading, a meter's physical condition, or a route-access situation looks off and you need the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — load for terms of art (AMI/AMR, tamper seal, revenue protection, register rollover) a generalist would misuse.

## Sources

AWWA (American Water Works Association) M6 manual, *Water Meters — Selection, Installation, Testing, and Maintenance*, for water-meter reading/accuracy practice; American Gas Association field-safety guidance for gas-meter reading and leak/hazard recognition; Edison Electric Institute and named utility revenue-protection program materials on theft-of-service/tamper indicators (broken seals, bypass wiring, reversed CTs); general utility-industry practice on AMI/AMR transition and manual-read fallback for estimate verification. The 70%-deviation inspection threshold and the same-month-last-year comparison convention are stated industry heuristics — the exact threshold and comparison method are utility-specific and should be confirmed against a given utility's revenue-protection policy. No direct practitioner review yet.
