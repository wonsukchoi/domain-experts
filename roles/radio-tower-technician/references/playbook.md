# Playbook

## Pre-climb checklist (run in this order, every climb)

1. **Rescue plan validity** — specific to this tower, this crew, today's weather; anchor and obstruction layout confirmed, not assumed from a prior visit.
2. **RF survey and power-down/reduction status** — for every carrier with an antenna in range of the work location, not just the requesting carrier. Written confirmation required, with either (a) a specific dB reduction value, or (b) confirmed off-air/shutdown status. A ticket that only says "reduced" or "cleared" without a number is not sufficient — request the value before proceeding.
3. **Fall-protection equipment inspection** — harness, lanyards, connectors inspected and tagged current for this user, this trip; a shared or borrowed kit gets inspected again, not assumed good because someone else used it that morning.
4. **Weather check against the site's access-limit threshold** — sustained wind and lightning-exclusion radius, same discipline as any tower trade.
5. **Confirm which anchor points and structural transitions are on today's route**, and brief the crew on where 100% tie-off changeovers happen — ladder-to-platform, platform-to-antenna-mount, and any point requiring a temporary anchor.

## MPE (maximum permissible exposure) reference table

Power density limits under 47 CFR 1.1310 / FCC OET Bulletin 65 and 65B. `f` = frequency in MHz. Occupational/controlled tier applies to trained personnel aware of and able to control their exposure (i.e., tower crew); general population/uncontrolled applies where the public could be present.

| Band | Occupational (mW/cm²) | General population (mW/cm²) | Averaging time |
|---|---|---|---|
| 0.3–1.34 MHz | 100 | 100 | 6 min / 30 min |
| 1.34–30 MHz | 180/f² | 180/f² | 6 min / 30 min |
| 30–300 MHz | 1.0 | 0.2 | 6 min / 30 min |
| 300–1500 MHz | f/300 | f/1500 | 6 min / 30 min |
| 1500 MHz–100 GHz | 5.0 | 1.0 | 6 min / 30 min |

**Worked examples at common cellular/PCS frequencies:**

- 850 MHz (cellular): occupational = 850/300 = **2.83 mW/cm²**
- 1900 MHz (PCS): falls in the 1500 MHz–100 GHz band → occupational = **5.0 mW/cm²** flat (not f/300 — that formula only applies below 1500 MHz)
- 2100 MHz (AWS): same band as above → occupational = **5.0 mW/cm²** flat

**Reading an RF survey against MPE:**

1. Get the surveyed or calculated power density at the *actual planned work position*, not a ground-level or entry-point reading — distance from the radiating face matters more than any other variable.
2. Compare against the occupational limit for that band (table above).
3. If above MPE at current power, calculate required attenuation in dB:

`dB reduction needed = 10 × log10(measured power density ÷ target power density)`

Target power density should sit below MPE with margin (a common working target is ~50% of MPE), not skimmed at 100% of the limit, since survey readings and actual field conditions carry measurement uncertainty.

**Example:** measured 8.2 mW/cm² at full power, target 1.42 mW/cm² (50% of 2.83 mW/cm² occupational MPE at 850 MHz):

10 × log10(8.2 ÷ 1.42) = 10 × log10(5.77) = 10 × 0.761 = **7.6 dB** → request 8 dB reduction, rounding up for margin.

**Sanity-check any NOC-reported reduction against this math** — a reported "3 dB reduction" only halves power (10 × log10(2) ≈ 3.01 dB), so 8.2 mW/cm² at 3 dB down is still 4.1 mW/cm², which stays above the 2.83 mW/cm² MPE at 850 MHz. Do not treat "some reduction was applied" as equivalent to "enough reduction was applied."

## VSWR / PIM troubleshooting sequence

| VSWR | Return loss | Read as |
|---|---|---|
| ≤1.5:1 | ≥14 dB | Good — no action |
| 1.5:1–2.0:1 | 10–14 dB | Marginal — investigate before sign-off |
| >2.0:1 | <10 dB | Fail — do not commission |

*(The ≤2.0:1 ceiling is the commonly cited acceptable maximum for cellular systems; the finer 1.5:1/2.0:1 banding above is a field heuristic layered on top of it — always check the site's RFDS for the carrier's actual acceptance tolerance.)*

Troubleshooting order on a marginal or failing VSWR reading, working from the antenna backward toward the radio (cheapest/fastest checks first):

1. **Weatherproofing boots and connector torque** at every accessible connection point — water ingress and under-torqued connectors are the most common and cheapest-to-fix cause.
2. **Jumper cable condition** — visual inspection for kinks, crush damage, or corrosion at connector interfaces.
3. **Antenna port itself** — swap to a known-good jumper and re-test before concluding the antenna is defective.
4. **Feed line / hybrid cable run** — only after ruling out the accessible connection points above.

**PIM (passive intermodulation):** test to the carrier's site-specific RFDS spec — commonly in the −150 dBc range or tighter (some carrier specs call for −153 to −155 dBc); there is no single universal regulatory PIM threshold, so the site's RFDS is the actual acceptance criterion. A PIM fail with a passing VSWR points at a connection that's mechanically fine for standing-wave purposes but has a micro-arcing or dissimilar-metal contact issue — check for loose-but-not-loose-enough connectors, corroded threads, or a rusted structural member in contact with the RF path (common at grounding kits and hanger hardware).

## Tower-light outage response timeline

| Time from discovery | Action |
|---|---|
| 0 min | Outage discovered (via monitoring system or field observation) |
| 0–30 min | Notify FAA if the light is not back in service — 47 CFR 17.48 sets a 30-minute clock, not 24 hours |
| At notification | FAA issues a NOTAM (Notice to Airmen) covering the outage |
| If repair extends past the NOTAM's stated window | Contact FAA again with an updated return-to-service estimate — repeat until the light is restored and the NOTAM is closed |

A site with an outage-monitoring system alerting the owner at the moment of failure is the only realistic way to consistently hit the 30-minute window — a routine drive-by inspection cadence will miss it on most outages, since the outage could have started hours before it's noticed.
