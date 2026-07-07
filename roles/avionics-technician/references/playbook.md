# Playbook

Filled procedures for the four recurring tasks: intermittent-fault wiggle testing, bonding/wire-separation verification, STC-vs-field-approval decisions, and DO-160 environmental cross-checks.

## 1. Intermittent-fault wiggle-test sequence

Ground checks reproduce a fault less than half the time it's real — the wiggle test recreates the mechanical/thermal domain a static check skips.

Procedure:

1. Pull the LRU's internal fault-history log (most nav receivers, FMS, and autopilots retain timestamped fault codes) and the squawk history for the same ATA/system over the last 60–90 days.
2. Correlate event timestamps against flight-phase data (gear cycles, flap transitions, engine start, known bus-load transients) from the maintenance data downloader or dispatch log — a real pattern beats a coincidence of dates.
3. With the aircraft on ground power and the system monitored (breakout box or the LRU's own BITE readout), start the wiggle test at the LRU connector itself, then move backward: LRU connector → first junction/splice → mid-bundle → aircraft-structure ground point → antenna/sensor connector.
4. At each point, flex the connector and 6 inches of bundle on either side while watching for a dropout, not just a full fault — a momentary flicker on the monitor counts as a reproduction.
5. If two full passes (LRU-to-sensor and back) produce no reproduction, stop repeating the same test. Widen scope: check adjacent system grounds and bonding straps for cross-coupling, and re-examine the fault log for a pattern the first pass missed (e.g., correlation with a specific system on the same bus, not a specific connector).
6. Log every point tested and its result, whether or not it reproduced — a documented "did not reproduce at this connector" narrows the field for the next technician; an undocumented pass is lost information.

Worked correlation example (matching SKILL.md):

```
Event 1: 2026-01-14, log timestamp 09:07:22
Event 2: 2026-01-19, log timestamp 14:32:05
Event 3: 2026-01-27, log timestamp 21:48:11

Gear-retraction timestamps (from maintenance data downloader), same flights:
09:07:18 | 14:32:00 | 21:48:06

Delta (event − gear cycle): 4 sec | 5 sec | 5 sec
```

A 4–6 second delta across three unrelated flights is a pattern, not noise — the next step is testing the gear-motor circuit's proximity to the affected wire bundle, not swapping the LRU.

## 2. Bonding resistance and wire-separation verification

Representative figures — **verify against the aircraft-specific wiring diagram manual and the current AC 43.13-1B edition before applying; these illustrate the shape of the limits, not a substitute for the current-revision source** [heuristic — needs practitioner check against current AC 43.13-1B edition].

| Check | Typical limit | Instrument |
|---|---|---|
| Equipment-rack/antenna bonding strap resistance | ≤ 3.0 mΩ (0.003 Ω) | Calibrated milliohmmeter, four-wire (Kelvin) lead |
| Static-discharge bonding jumper | ≤ 10 mΩ (0.010 Ω) | Milliohmmeter |
| Data/signal pair to power/high-current lead, unshielded | ≥ 2 in separation | Direct measurement along the run |
| Data/signal pair to power lead, twisted-shielded pair per mfr. install manual | Manufacturer-specified (often less than 2 in, credited to the shield) | Manufacturer install drawing |
| Wire-bundle support/clamp interval | Not to exceed 24 in, no more than 1 in unsupported sag | Direct measurement |

Verification sequence:

1. Confirm the milliohmmeter's calibration is current before measuring — an expired-calibration reading is not a valid bond measurement regardless of the number displayed.
2. Measure at the actual bonding point (strap-to-structure interface), not mid-strap — surface preparation and torque at the interface, not the strap material itself, is the usual failure point.
3. If the reading exceeds spec, remove the strap, inspect and clean both mating surfaces for anodize/paint/corrosion, reinstall to the specified torque, and remeasure. Do not accept a marginal-but-passing reading without cleaning if the surface shows visible oxidation.
4. Measure wire-bundle separation from adjacent power/high-current runs at the closest point along the run, not just at the endpoints — bundles often sag closer together mid-span than at their clamped ends.
5. Where separation can't be met (tight bay, shared conduit), consult the manufacturer's install manual for a twisted-shielded-pair or conduit exception before accepting a routing shortcut — the exception has to be specifically credited, not assumed.
6. Record both the before and after figures in the discrepancy log — a "corrected" bonding entry with no measured numbers is not a verified repair.

## 3. STC vs. field approval vs. DER-approved data — decision procedure

| Path | When it fits | Turnaround (typical) | Fleet-repeat suitability |
|---|---|---|---|
| AML (Approved Model List) STC | Airframe and equipment combination already covered by an existing approved-model list | Same-day paperwork once licensed in; equipment vendor supplies install drawings | Best — designed for repeat installs across covered models |
| Single-aircraft STC | Equipment/airframe combo covered by an STC not on an AML, or purchasing a new STC | Weeks to months if a new STC must be obtained | Fits if the same tail-specific STC is purchased once and applies fleet-wide; otherwise weak |
| Field approval (FAA Form 337 + FSDO data approval) | Genuine one-off alteration, no covering STC exists, and the shop isn't planning to repeat it | Historically 2–6 weeks per FSDO, increasingly discouraged for repeat use | Weak — FAA Order 8900.1 Vol. 4 guidance discourages FSDOs from approving the same alteration repeatedly |
| DER-approved data (FAA Form 8110-3) | Engineering disposition needed for a configuration no manual or STC covers | Depends on DER availability | Fits a specific engineering question, not a repeat-install program by itself |

Decision steps:

1. Search the AML STC list for the exact airframe model and equipment part number/TSO letter combination first — this is the fastest and most durable path when it exists.
2. If no AML STC fits, search for a single-aircraft STC covering the combination; if one exists, buy into it.
3. If neither exists, ask: will this exact alteration repeat on more than one or two aircraft? If yes, price and pursue an STC rather than a field approval, even though the field-approval paperwork might already exist from a prior one-off job — reusing it for a repeat installs converts a legitimate one-off documentation into a workaround for what is now a production alteration.
4. If the alteration is genuinely one-off and no STC exists, pursue field approval: submit Form 337 with substantiating data to the FSDO.
5. If the configuration doesn't fit any manual, STC, or field-approval precedent, escalate to a DER for approved data before installing anything.

Worked turnaround arithmetic (matching SKILL.md fleet example):

```
Prior field-approval turnaround (this shop, this alteration): 35 days
Aircraft remaining after the first: 5
Sequential field-approval turnaround for remaining fleet: 5 × 35 = 175 days
Compliance deadline: 90 days

175 days > 90-day deadline → field approval path cannot meet the deadline
for the fleet, independent of the FSDO policy question.

AML STC install time per aircraft: ~2 days
Parallel bays available: 2
Fleet of 6 aircraft, 2 in parallel: 6 ÷ 2 × 2 days = 6 days total install time,
well inside the 90-day window once the STC is licensed in.
```

## 4. DO-160 environmental qualification cross-check

Every TSO'd LRU carries a DO-160 qualification basis expressed as a category letter/number per section (not one grade). Sections most relevant to an install-location decision:

| DO-160 section | Covers | Install-location question to ask |
|---|---|---|
| Section 4 | Temperature and altitude | Does the qualified temperature range cover this bay's actual extremes (pressurized/heated vs. unpressurized/unheated)? |
| Section 8 | Vibration | Is this a high-vibration mount location (engine-adjacent, gear bay) versus the category the equipment was qualified for? |
| Section 16 | Voltage spike | Is this bus shared with high-inrush equipment (starter-generator, gear motors)? |
| Section 21 | Emission of RF energy | Could this LRU's emissions interfere with adjacent nav/comm antennas at this mounting distance? |
| Section 22 | Lightning-induced transient susceptibility | Is this LRU's wiring run in a zone with direct or induced lightning exposure per the aircraft's zoning analysis? |

Procedure:

1. Pull the equipment's environmental qualification form (EQF) or DO-160 compliance matrix from its TSO authorization paperwork — read every relevant section's category, not just the headline category letter.
2. Compare each category against the actual installation zone's known environment (temperature/altitude range at the aircraft's operating ceiling, vibration source proximity, EMI-emitting neighbors).
3. Where a mismatch exists (equipment qualified for pressurized-cabin temperatures being installed in an unpressurized tail cone, for example), stop and either relocate the equipment to a qualifying bay or select equipment with a matching qualification — do not install and "monitor for problems."
4. Record the qualification basis and the install-location match in the installation paperwork alongside the STC/field-approval reference — an approved-data chain without an environmental cross-check is incomplete.
