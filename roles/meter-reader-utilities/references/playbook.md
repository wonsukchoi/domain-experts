# Meter Reader, Utilities — Playbook

## Anomaly-investigation worksheet (filled example)

| Field | Value |
|---|---|
| Account | #4471-002 |
| Meter type | Residential electric, single-phase |
| Vacancy flag on file? | No |
| Last actual read (date, register) | Aug 24, 84,320 kWh |
| This read (date, register) | Sep 23, 84,410 kWh |
| Consumption this cycle | 84,410 − 84,320 = 90 kWh / 30 days = 3.0 kWh/day |
| Same-month-last-year consumption | 900 kWh / 30 days = 30.0 kWh/day |
| Deviation | (30.0 − 3.0) / 30.0 = 90.0% below baseline |
| Investigation threshold | >70% deviation on occupied account → mandatory physical inspection |
| Threshold crossed? | Yes — proceed to physical inspection before posting |

## Physical inspection checklist (run only when threshold is crossed)

1. **Tamper seal** — present, and does the serial number match the account's on-file seal install record? If broken or mismatched, photograph before touching anything else.
2. **Visible wiring at the meter** — any jumper/bypass wire bridging line and load lugs? Photograph in place; do not remove it.
3. **Meter register** — glass intact, dial/digital display legible, no signs of physical damage or reversed installation.
4. **CT/multiplier meters only (commercial accounts)** — does the current transformer ratio on the nameplate match what's on file for the account? A mismatch alone can produce a large false anomaly with no tampering involved.
5. **Occupancy signals** — visible activity, mail accumulation, seasonal-vacancy indicators (e.g., pool cover on in winter, holiday lighting absent) — corroborating evidence, not conclusive on its own.

## Classification and routing

| Finding | Classification | Route to |
|---|---|---|
| No physical evidence found; deviation explainable by known account change (e.g., logged move-out, solar install) | Normal variation | Post read as-is |
| Register damaged, stuck, or reading physically implausible for meter class | Equipment malfunction | Technician dispatch for meter exchange |
| Broken seal and/or bypass wire found | Tamper indicator | Revenue protection ticket, read logged estimated-pending-investigation, photos attached |
| Deviation crosses threshold but no physical access to meter (locked area, hazard) | Needs follow-up | Log access issue, schedule return visit or escalate for utility-side resolution |

## Estimated-read reconciliation (filled example)

| Cycle | Read type | Register | Consumption |
|---|---|---|---|
| June | Actual | 83,940 kWh | 720 kWh |
| July | Estimated (access denied) | 84,700 kWh (est.) | 760 kWh (est., based on prior-year July) |
| August | Estimated (access denied) | 85,540 kWh (est.) | 840 kWh (est., based on prior-year August) |
| September | Actual | 85,650 kWh | True total since June actual = 85,650 − 83,940 = **1,710 kWh over 3 cycles** vs. **1,600 kWh already billed via the July + August estimates** |

The two estimates *understated* consumption by 110 kWh against what the property actually used (1,710 true vs. 1,600 already billed). On the September actual read, this is trued up as an additional line on that bill rather than posted silently — the customer's statement carries a documented reconciliation line ("+110 kWh true-up for July–August estimate variance"), not an unexplained jump from a normal-looking September number.

## Route-log discrepancy check (filled example)

Route GPS/timestamp log shows the technician's device pinged at the property address at 10:42 AM. The read submitted matches the prior cycle's exact register value to the digit — a static, unchanged number. Correct handling: flag for supervisor review before the read is accepted; a genuinely flat baseload on a confirmed-vacant property is plausible, but an *unflagged, occupied* account with an identical register value two cycles running is far more likely a stuck register or an office-entered placeholder than true zero consumption.
