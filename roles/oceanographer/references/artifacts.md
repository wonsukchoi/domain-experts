# Oceanographer artifacts — templates with real structure

Working templates an agent can fill in. Example numbers throughout are for a 14-day, US-flagged, intermediate-class UNOLS research vessel (day rate ~$35,000, consistent with mid-size global-class ships in recent NSF-funded proposals) running a full-depth repeat hydrographic section.

## 1. Ship-time / cruise-budget proposal (NSF Ocean Sciences style)

**Section: justification of ship-days.**

| Activity | Days | Rationale |
|---|---|---|
| Transit to first station | 1.5 | 220 nm at ~9 kt average |
| Full-depth CTD/rosette stations (36 total, ~4,500 m avg) | 9.0 | ~6 hr/station incl. wire time + bottle sampling, 24 hr ops |
| Mooring turnaround (2 moorings: recover + redeploy) | 1.5 | 8 hr per mooring incl. transit between sites |
| Weather/contingency buffer | 1.5 | 12% of on-station days — regional Nov–Mar weather-day loss rate from prior cruise reports on this vessel class |
| Transit to port | 0.5 | 75 nm |
| **Total requested** | **14.0** | |

**Budget line (at $35,000/day ship rate, $000s):**

| Line | Amount | Note |
|---|---|---|
| Ship time (14 days × $35K) | $490.0 | UNOLS scheduled rate for vessel class |
| Personnel (2 PI-days/day × 14, plus 3 techs) | $95.0 | Salary + fringe, cruise duration only |
| Consumables (Niskin O-rings, reagents, filters) | $12.5 | Winkler reagents, salinometer standards, GF/F filters |
| Sensor calibration (pre-cruise CTD send-out) | $8.0 | Sea-Bird factory calibration, 2 units |
| Shipping/mobilization | $6.5 | Gear to/from port of embarkation |
| **Total direct cruise cost** | **$612.0** | |

**Rule:** the weather/contingency buffer is sized from the vessel's own historical weather-day loss rate for the season and region, not a flat percentage picked without evidence — a 12% buffer on a fair-weather summer coastal cruise is generous; the same 12% on a Southern Ocean winter transit is likely to be exceeded.

## 2. CTD cast QC / calibration-flag log

Per-cast QC record, filled at the end of each station and reconciled against crossover bottle samples at designated calibration stations (typically every 3rd–4th station).

| Cast # | Date | Max depth (m) | Bottle crossover? | CTD sal. (PSU) | Bottle sal. (PSU) | Offset | QC flag |
|---|---|---|---|---|---|---|---|
| 01 | Day 1 | 4,510 | Y | 34.702 | 34.701 | +0.001 | 2 (good) |
| 06 | Day 3 | 3,880 | Y | 34.699 | 34.700 | −0.001 | 2 (good) |
| 12 | Day 5 | 4,220 | Y | 34.691 | 34.696 | −0.005 | 3 (probably good) |
| 18 | Day 7 | 4,610 | Y | 34.688 | 34.696 | −0.008 | 5 (adjusted) |
| 24 | Day 9 | 4,340 | Y | 34.687 | 34.698 | −0.011 | 5 (adjusted) |
| 30 | Day 12 | 4,780 | Y | 34.684 | 34.697 | −0.013 | 5 (adjusted) |
| 36 | Day 14 | 4,505 | Y | 34.685 | 34.700 | −0.015 | 5 (adjusted) |

**Flag convention** (aligned to WOCE/GO-SHIP practice — verify against the specific data center's scheme before submission): 1 = not evaluated, 2 = good, 3 = probably good, 4 = bad, 5 = changed/adjusted (correction applied and documented), 9 = missing.

**Correction procedure when offset trends with cast number (not scattered):** fit a linear regression of offset against elapsed day across all crossover stations; apply the fitted per-day offset to every cast's salinity, not the cruise-mean offset. Archive both raw and adjusted salinity; flag adjusted casts 5, never overwrite the raw value.

## 3. Mooring turnaround checklist

Run in this order at every recovery/redeployment; each step gates the next — do not redeploy on a failed check.

1. **Pre-recovery:** confirm acoustic release response (send interrogation, confirm range and correct release code) before committing ship time to the site.
2. **On deck:** download raw data from all instruments before opening any housing — a bad download attempt after opening risks moisture ingress on a unit that otherwise has good data.
3. **Battery check:** log remaining voltage on every instrument against its rated deployment life; replace any unit below ~20% of expected remaining capacity even if it "still reads," since failure mid-deployment is unrecoverable until next turnaround (often 6–12 months out).
4. **Biofouling inspection:** photograph and log fouling on optical/conductivity sensors; note fouling severity (light/moderate/heavy) against days deployed — this becomes the first input when a later drift-correction decision needs a physical cause, not just a statistical one.
5. **Pre-deployment calibration check:** compare each sensor's reading in a known reference (calibration bath or a co-located, just-serviced sensor) against its factory calibration before it goes back in the water.
6. **Redeploy:** confirm anchor weight and release codes logged in the cruise report match the physical unit going over the side — a swapped release code is a mooring that can't be recovered next visit.
7. **Post-deployment fix:** log GPS position of the surface expression (or acoustic-ranged anchor position) immediately after deployment, before the ship leaves station — this is the only accurate position record if the mooring drags.
