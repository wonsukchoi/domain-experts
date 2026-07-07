# Playbook

Filled sequences a technician actually runs on a service call, with real thresholds and example numbers. Starting points to adapt per appliance model and region, not scripts to follow blind.

## 1. Pre-visit check: recall and warranty, before any diagnosis

Run this before leaving the truck for the door, every call:

1. **Pull model and serial number** from the customer over the phone at booking, or from the unit's data plate on arrival.
2. **Check CPSC.gov and SaferProducts.gov** by model/serial or product category. If a match exists, stop the billable-repair path — read the remedy (free part, free repair, refund, or replacement) and route the customer to it instead.
3. **Check the manufacturer's warranty lookup by serial number.** Two separate windows commonly apply: the whole-unit warranty (usually 1 year) and a sealed-system/compressor parts warranty (commonly 5-10 years on refrigerators, parts only — labor is billable even inside that window unless the shop holds a manufacturer service contract).
4. **Only after both come back clear does the visit become a normal billable diagnostic call.**

**Example outcome table:**

| Check | Result | Action |
|---|---|---|
| CPSC/SaferProducts | No match | Proceed |
| Manufacturer recall page | No match | Proceed |
| Whole-unit warranty | Expired (unit is 4 years old, 1-year window) | Billable |
| Sealed-system parts warranty | Active (8 of 10 years used) | If sealed-system fault confirmed, part is free — bill labor only |

## 2. Fault-frequency-by-symptom tables

Sequencing shortcuts for where to point the multimeter first. These are trade-consensus rankings (Master Samurai Tech curriculum, PartSelect/RepairClinic diagnostic guides), not a single controlled study — treat the ordering as a starting sequence, always confirmed by a measured test before any part is ordered.

**Refrigerator — "not cooling" / "warm":**

| Rank | Cause | Approx. share of calls | Confirm with |
|---|---|---|---|
| 1 | Dirty/blocked condenser coils | ~30% | Visual + airflow check |
| 2 | Evaporator fan motor failure | ~20% | Amp draw vs. rated spec |
| 3 | Defrost system failure (heater/thermostat/timer) | ~20% | Continuity/resistance check |
| 4 | Start relay / compressor overload | ~15% | Relay continuity, capacitor test |
| 5 | Compressor / sealed-system failure | ~10% | Locked-rotor amp draw, static pressure read |
| 6 | Refrigerant leak | ~5% | UV dye or electronic leak detector |

**Clothes washer — "won't spin" / "leaking":**

| Rank | Cause | Confirm with |
|---|---|---|
| 1 | Unbalanced load / door lock fault | Cycle re-run, lock switch continuity |
| 2 | Drive belt worn or off pulley | Visual + tension check |
| 3 | Door/lid switch failure | Continuity check |
| 4 | Drain pump clogged or failed | Amp draw, visual for debris |
| 5 | Motor coupling/clutch worn (top-load) | Visual + torque test |
| 6 | Motor control board failure | Voltage output test |

**Clothes dryer — "no heat" / "overheating":**

| Rank | Cause | Confirm with |
|---|---|---|
| 1 | Lint-clogged exhaust vent (restricted airflow) | Airflow/static pressure check at exhaust |
| 2 | Heating element open (electric) or igniter failed (gas) | Continuity/resistance check |
| 3 | Thermal fuse blown (often a downstream symptom of #1) | Continuity check |
| 4 | Cycling thermostat failure | Continuity check at rated temp |
| 5 | Timer or control board failure | Voltage output test |

**Dishwasher — "not draining" / "not cleaning":**

| Rank | Cause | Confirm with |
|---|---|---|
| 1 | Clogged filter/drain path | Visual inspection |
| 2 | Drain pump/motor failure | Amp draw, visual |
| 3 | Spray arm clogged or cracked | Visual |
| 4 | Water inlet valve failure | Continuity + flow test |
| 5 | Control board failure | Voltage/relay test |

## 2b. Sequential diagnosis rule when two causes remain plausible

After the first test, if two candidate causes are still both plausible (e.g., defrost thermostat and compressor both look consistent with the symptom), fix the cheaper confirmed one first and retest before condemning the expensive part. Example: a $18 defrost thermostat that tests marginal alongside a compressor with an inconclusive amp reading — replace the thermostat, run a full defrost cycle, and only escalate to compressor diagnosis if the fault persists. This keeps a false-positive expensive quote from ever reaching the customer, at the cost of a slightly longer visit.

## 3. Repair-vs-replace worksheet

```
APPLIANCE: [type, brand, model]           AGE: [years] / EXPECTED LIFE: [years]
CONFIRMED FAULT(S): [component(s), from measured test — not guess]

PARTS:                                     $______
LABOR: [hours] x $[rate]/hr                $______
                              TOTAL REPAIR: $______

COMPARABLE REPLACEMENT (installed, same tier): $______

REPAIR / REPLACEMENT RATIO: [total repair ÷ replacement] = ____%

THRESHOLD CHECK:
  - Unit in first third of expected life?  -> replace threshold ~35-40%
  - Unit in middle/last third?             -> replace threshold ~50%
  - Ratio within 10 points of threshold?   -> present both numbers, customer decides

RECOMMENDATION: [repair / replace / customer's call]
```

**Worked fill (matches SKILL.md example, non-compressor branch):**

```
APPLIANCE: GE top-freezer refrigerator     AGE: 9 / EXPECTED LIFE: 13
CONFIRMED FAULT(S): defrost heater (open), evaporator fan motor (over-amp)

PARTS: defrost heater $45 + fan motor $65  $110
LABOR: 1.5 hr x $110/hr                    $165
                              TOTAL REPAIR: $275

COMPARABLE REPLACEMENT (installed):        $950

REPAIR / REPLACEMENT RATIO: 275 / 950 = 29%

THRESHOLD CHECK:
  - Unit is in last third of expected life (9 of 13 yrs) -> threshold ~50%
  - 29% is well under 50%, not in the ambiguous 10-point band

RECOMMENDATION: repair
```

## 4. Truck-stock loadout

Sized to the top of the fault-frequency curve across appliance types, reviewed monthly against the return-trip log (section 5). Not a full parts catalog — carrying everything makes the van an inventory problem instead of a diagnostic tool.

**Standing stock (fits most single-day routes):**

| Category | Parts carried |
|---|---|
| Universal | Multimeter, clamp meter, assorted wire nuts/terminals, universal door gaskets (top 3 sizes by brand) |
| Refrigerator | Defrost heaters (2 common types), defrost thermostats, start relays/overload protectors, evaporator fan motors (2 voltage classes) |
| Washer | Door/lid switches, drive belts (2 common sizes), universal drain pumps |
| Dryer | Heating elements (electric, 2 wattage classes), igniters (gas), thermal fuses, cycling thermostats |
| Dishwasher | Water inlet valves, universal drain pumps, spray arm kits |
| Sealed-system (certified techs only) | Refrigerant recovery tank, manifold gauge set — no refrigerant carried pre-charged; recovered/recharged per job under EPA 608 scope |

**Not stocked as standard** (special-order): control boards (too many SKUs per model to stock economically), compressors (heavy, model-specific, ordered once diagnosis confirms), and any part with a same-day special-order option in the local market.

## 5. Return-trip log (the truck-stock correction loop)

Every call that ends without a same-visit fix gets one line:

```
DATE | APPLIANCE | SYMPTOM | CONFIRMED FAULT | PART MISSING | WHY NOT STOCKED
```

Reviewed monthly. A part appearing 3+ times in a rolling 90-day window moves into standing stock even if it wasn't previously in the top fault-frequency ranking for that appliance — regional model mix can shift the real distribution away from the general trade tables in section 2.

## 6. Sealed-system work gate

Before opening any sealed refrigeration system (compressor swap, evaporator/condenser coil replacement involving refrigerant lines):

1. Confirm the technician holds the EPA Section 608 certification level required — Type I covers small appliances (charge of 5 lbs or less: most household refrigerators, freezers, window/portable AC units, dehumidifiers); Universal is required if the technician also services larger charge equipment.
2. Confirm recovery equipment (recovery machine, storage tank) is on the truck and within certification/inspection date.
3. Recover refrigerant into a labeled tank — never vent to atmosphere; venting is a federal violation regardless of appliance size.
4. Weigh in the correct refrigerant charge per the nameplate specification after the repair, not "until it feels cold" — overcharging and undercharging both cause repeat no-cool calls.
5. If certification level or equipment is missing, reschedule the sealed-system portion to a certified colleague rather than proceeding.
