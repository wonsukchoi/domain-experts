# Playbook

## Chip load calculation worksheet

Fill whenever feed rate, RPM, or cutter is changed.

| Field | Value |
|---|---|
| Feed rate | 20 ft/min (240 in/min) |
| Cutter RPM | 18,000 |
| Number of cutting edges | 2 |
| Chip load = feed rate ÷ (RPM × edges) | 240 / 36,000 = 0.00667 in/edge |
| Target chip load range (hardwood, general) | 0.005-0.015 in/edge (verify against species/cutter data) |
| Within range? | Y |

**If burning/finish issue occurs:**

| Diagnostic step | Check |
|---|---|
| 1. Cutter hours since last sharpen | Compare to service interval |
| 2. Chip load at current settings | Recalculate, don't assume |
| 3. If cutter overdue for service | Resharpen/replace FIRST, before adjusting feed rate |
| 4. If cutter recently serviced and chip load is low | Consider increasing feed rate or reducing RPM to raise chip load |

**Rule:** never reduce feed rate as a first response to burning without first checking cutter condition — a lower chip load on a dulling cutter makes burning worse.

## Burn/tearout diagnostic table

| Symptom | Check first |
|---|---|
| Burning appearing partway through a run | Cutter hours/service interval |
| Burning present from the very start of a run | Chip load calculation (feed/RPM/edges) |
| Tearout at a specific location on the workpiece | Grain direction at that location |
| Tearout uniformly across multiple parts | Cutter sharpness or chip load, not grain (unless material batch shares the same figure) |

## Moisture content reference guide by end-use environment (illustrative — always verify with local/regional standards)

| End-use environment | Target moisture content |
|---|---|
| Indoor, climate-controlled (typical US interior) | 6-8% |
| Indoor, less controlled (garage, unheated space) | 9-12% |
| Outdoor/exterior use | 12-15%+ (species and region dependent) |

**Rule:** always verify target moisture content against the specific region's typical equilibrium moisture content (EMC) tables and the part's actual intended environment — this table is illustrative, not a substitute for local reference data.
