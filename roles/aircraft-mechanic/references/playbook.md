# Playbook

Filled procedures and templates for the four recurring tasks: MEL dispatch decisions, AD compliance-time tracking, torque/safety-wire verification, and log/return-to-service entries.

## 1. MEL deferral decision procedure

MEL categories set the maximum deferral window (consecutive calendar days, counted from the day *after* discovery, per the operator's approved MEL preamble):

| Category | Max deferral | Typical items |
|---|---|---|
| A | As stated in the MEL remarks column (no standard default — can be "0," i.e. before next flight) | Items with a condition-specific limit written directly into the entry |
| B | 3 days | Redundant avionics, some cabin systems |
| C | 10 days | Secondary electrical/hydraulic sources, one of two APU functions |
| D | 120 days | Low-utilization items with negligible operational impact (e.g., decorative cabin lighting) |

Procedure:

1. Confirm the item is actually listed in the MEL by ATA chapter/item number — an unlisted item is not deferrable by analogy to a listed one.
2. Read the (M) and (O) columns in full, not just the category letter. (M) = a maintenance procedure required before dispatch (e.g., deactivate and placard); (O) = an operational procedure the crew must follow (e.g., avoid a specific airport type, reduce payload, avoid RVSM airspace).
3. Cross-check against every other currently-open MEL item on the same aircraft for interaction (e.g., two independently-legal single-system deferrals that together remove all redundancy in one flight regime).
4. Compute the expiration date: discovery date + category days. Example — discovered March 3, Category C (10 days): deferral expires March 13 (March 4 is day 1).
5. Enter the deferral on the placard/logbook with expiration date, referenced MEL item number, and (M)/(O) procedures in force.
6. Open a parts/repair tracking entry with a target completion date at least 1–2 days before expiration — never plan the permanent repair for the expiration day itself.

## 2. Airworthiness Directive compliance-time tracking

AD compliance times fall into four structural types:

| Type | Example wording | Action |
|---|---|---|
| Immediate | "Before further flight" | Aircraft grounded until AD action complete — no dispatch, no deferral |
| Flight-hour/cycle window | "Within 500 flight hours or 300 cycles, whichever occurs first, from the effective date" | Track both counters; whichever hits its limit first sets the deadline |
| Calendar window | "Within 90 days of the effective date" | Track calendar date only, independent of utilization |
| Next-inspection, capped | "At next scheduled inspection, not to exceed 100 hours since last compliance" | Compute margin = cap − hours since last compliance; convert to days using average daily utilization |

Worked calculation (next-inspection, capped, matching the SKILL.md example):

```
Cap:                     100 flight hours since last compliance
Engine time at last AD compliance:   14,820 hrs
Current engine time:                 14,895 hrs
Hours since compliance:  14,895 − 14,820 = 75 hrs
Remaining margin:        100 − 75 = 25 hrs
Daily utilization:       ~6 flight hrs/day (typical 3–4 leg regional day)
Days of margin:          25 ÷ 6 ≈ 4.2 days
```

Always recompute margin against the *current* flight schedule, not a rounded estimate — a schedule change (charter add-on, weather diversion adding cycles) can consume margin faster than the daily average assumes. If margin drops below 1 day's worth of scheduled flying, ground for compliance rather than gambling the last leg.

## 3. Torque and safety-wire verification

Representative torque values by fastener class — **verify against the aircraft-specific manual or AC 43.13-1B Table 7-1 before applying; these illustrate the *shape* of the table, not a substitute for the current-revision source** [heuristic — needs practitioner check against current AC 43.13-1B edition]:

| Bolt/fastener class | Thread size | Typical torque range (in-lbs) |
|---|---|---|
| AN3 (10-32) | 3/16" | 20–25 |
| AN4 (1/4-28) | 1/4" | 50–70 |
| AN5 (5/16-24) | 5/16" | 100–140 |
| AN6 (3/8-24) | 3/8" | 160–190 |

Verification sequence:

1. Confirm the calibration sticker on the torque wrench is current (not expired) before use — an expired-calibration reading is not a valid torque value regardless of what the dial shows.
2. Torque to the value specified by the type-specific manual for that exact fastener and application (never a "close enough" class); apply in the sequence specified (often a star or cross pattern for multi-bolt patterns) to avoid uneven clamping.
3. Apply torque seal (torque paint) across the fastener head and adjacent structure immediately after final torque — this is the visual proof for the *next* inspection, not a formality.
4. Where safety wire is specified instead of or in addition to torque seal: standard wire diameter is 0.032" for most small AN fasteners (0.041" or 0.051" for larger/higher-load fasteners per the manual), twisted 6–8 twists per inch, direction such that any fastener loosening tightens the wire's grip rather than loosening it.
5. On reinspection, absence of an intact torque-seal stripe or a wire with fewer than the specified twists per inch (or twisted the wrong direction) is logged as a new discrepancy — treat it as "unknown torque state," not "probably fine."

## 4. Discrepancy write-up and return-to-service log entry template

Minimum fields per 14 CFR 43.9/43.11 — filled example:

```
Aircraft: N482QX (CRJ-700)             Date: 2026-03-03
Total airframe time: 24,110.4 hrs      Total cycles: 18,204

DISCREPANCY (as reported):
APU generator fails to come online; load meter fluctuates during
APU start. Ref. Sq. #4471.

CORRECTIVE ACTION (as performed, with data reference):
MEL 24-31-01 applied per [Operator] MEL Rev. 14, Category C.
Deferred effective 2026-03-03, expires 2026-03-13. (O) procedure:
external ground power or air-start cart required at all outstations
for duration of deferral. Routing revised — legs 3–4 rerouted away
from KABQ/KTUS (no ground power available). Repair scheduled at
MX base, target completion 2026-03-06, ahead of MEL expiration.

PARTS/REF: N/A (deferral only — no part replaced this entry)

RETURN TO SERVICE STATEMENT:
"I certify that this aircraft has been inspected/repaired in
accordance with current regulations and is approved for return to
service, subject to the MEL 24-31-01 deferral and (O) procedure
stated above, which remain in force until 2026-03-13 or repair,
whichever occurs first."

Signature: ______________________   Certificate #: A&P 1234567
```

Fallback positions in preference order when data is ambiguous or missing:

1. OEM type-specific maintenance/structural repair manual for the exact configuration (by serial number/effectivity).
2. AC 43.13-1B/2A, only if the repair qualifies as minor and no OEM data exists for it.
3. Manufacturer or DER engineering disposition (written), for anything outside 1–2 — never an improvised bridge between two procedures that don't quite match the configuration.
4. If none of the above resolve within the time available before dispatch, ground the aircraft — "escalate later, dispatch now" is not an available option once data runs out.
