# Roustabout playbook

Filled examples for the three tasks that recur most on a wellsite: confined space entry, trench sizing, and rig-up sequencing.

## 1. Confined space entry permit (filled template)

Use for any cellar, valve pit, tank, or vessel entry. Test at top, mid, and bottom before signing — a single reading at the opening does not clear the space.

| Field | Entry |
|---|---|
| Space | Valve pit, Well 14-A, 4 ft × 4 ft × 6 ft (96 ft³) |
| Task | Valve repair |
| Hazards identified | H2S accumulation (heavier than air), oxygen displacement, engulfment |
| Pre-entry test — surface | O2 20.9% / LEL 0% / H2S 0 ppm |
| Pre-entry test — mid (3 ft) | O2 20.5% / LEL 2% / H2S 8 ppm |
| Pre-entry test — bottom (6 ft) | O2 18.9% / LEL 14% / H2S 35 ppm — **FAIL** |
| Entry criteria | O2 19.5–23.5%, LEL <10%, H2S <10 ppm |
| Control applied | Forced-air ventilation, 250 cfm blower, 10-min purge (blower continuous through entry) |
| Post-purge retest — bottom | O2 20.7% / LEL 1% / H2S 3 ppm — **PASS** |
| Attendant (hole watch) | Named individual, continuous radio contact, retrieval line rigged |
| Entrant(s) | Named individual(s), SCBA staged at the opening even after a passing atmosphere test |
| Continuous monitoring | 4-gas meter worn by entrant for duration of entry |
| Time in / time out | Logged to the minute |
| Rescue plan | Non-entry retrieval first (harness + line); local fire/EMS as backup, called before entry starts, not after a problem |

Purge-time math (5-air-change stated heuristic — confirm against site-specific program, not an OSHA-fixed multiplier):

```
purge minutes = (air changes × space volume ft³) ÷ blower cfm
              = (5 × 96) ÷ 250
              = 480 ÷ 250
              = 1.92 min → round up to a conservative fixed purge (commonly 10 min) and re-test
```

## 2. Trench / excavation sizing table

OSHA 29 CFR 1926 Subpart P requires a protective system at 5 ft depth or more (except stable rock). Slope ratios below are horizontal:vertical, for a trench with vertical sides cut to the slope angle.

| Soil type | Max allowable slope (H:V) | Typical use case |
|---|---|---|
| Stable rock | Vertical (no slope required) | Rare on unconsolidated lease soil — confirm with competent person, don't assume |
| Type A (clay, hardpan) | 3/4:1 (53°) | Firm, undisturbed soil with no fissures, not previously excavated |
| Type B (silt, sandy loam) | 1:1 (45°) | Most common lease soil — cohesive but not Type A |
| Type C (gravel, sand, submerged soil) | 1 1/2:1 (34°) | Wet or granular soil, water seepage present |

**Spoil pile setback:** minimum 2 ft from the edge of the excavation — closer than that adds surcharge load on the sidewall and is itself a cited failure precursor (see [references/red-flags.md](red-flags.md)).

**Worked sizing example — 6 ft deep flowline trench, Type B soil, 1:1 slope:**

```
Depth = 6 ft
Slope ratio = 1:1 → horizontal offset at top = 1 × depth = 6 ft (each side)
Trench bottom width (pipe + working room) = 2 ft
Trench top width = bottom width + (2 × horizontal offset) = 2 + (2 × 6) = 14 ft
```

A trench box rated for 6 ft depth in Type B soil is the alternative to sloping if the 14 ft top width isn't available (tight lease-road right-of-way).

## 3. Rig-up sequence with pinch-point and line-of-fire controls

Filled sequence for rigging up a workover unit or pump-truck iron before a servicing job:

1. **Pre-job tailgate JSA** — crew signs on, hazards named for today's specific job (H2S zone status, expected pressures, live lines nearby).
2. **Spot equipment** — one spotter, hand signals per ASME B30.5, crew clear of the swing radius before the unit moves; no one rides equipment being spotted.
3. **Rig up iron/hoses low pressure first** — connect at zero pressure, confirm with a bleed-off check (not the gauge alone) before making up the final union.
4. **Pressure-test the rig-up** to the job's planned working pressure before introducing live fluid; crew stands clear of the line-of-fire radius during test, not "close enough to watch the gauge."
5. **Confirm lockout on any pumping unit or rotating equipment** in the work area that isn't part of today's job but is within reach of the crew.
6. **Call every subsequent move by name** ("bringing tension," "coming tight," "breaking connection") — hands confirmed clear before the call, not simultaneously with it.
7. **Rig down in reverse**, bleeding pressure before breaking any connection, re-verifying zero on a second point (not the same gauge) before cracking a union.
