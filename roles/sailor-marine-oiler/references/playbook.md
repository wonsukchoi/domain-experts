# Sailor/Marine Oiler — Playbook

## Mooring-tension / snap-back-zone worksheet (filled example)

Line: 64 mm eight-strand polyester spring line, stated minimum breaking load (MBL) 90 tonnes. Fairlead-to-bollard span under load: 15 m.

| Check | Tension (t) | % of MBL | Action |
|---|---|---|---|
| 1 — heave-in begins | 28 | 31% | Normal, continue |
| 2 — tug takes strain | 35 | 39% | Normal, continue, personnel clear of line path |
| 3 — gust on the bow | 55 | 61% | Past 50% working-limit default: ease line, clear zone |

- **Working-limit threshold:** 50% of MBL = 45 t. Check 3 (55 t) exceeds it.
- **Snap-back zone (per OCIMF MEG4 general guidance):** treat the hazard zone as extending at least the line's own paid-out length beyond the fitting in the direction of pull — here, at least 15 m beyond the bollard along the centerline, plus a lateral arc either side of that line. A crew member standing 8 m off the bitt, directly on the centerline, is inside the zone regardless of how the line looks.
- **Correct action sequence:** call "clear the line," reposition all hands to 15 m+ off the centerline and out of the lateral arc, signal the winch operator to ease rather than continue heaving against the load spike, re-check tension after easing.
- **Confirm the fix worked:** tension eased from 55 t back to 32 t (36% of MBL) within about a minute once the gust passed and slack was taken. Only then resume normal heave-in.

## Gauge-round baseline worksheet (filled example)

Main-engine exhaust gas temperature round, six units, 0200 watch:

| Unit | Reading (°C) | Included in baseline mean? |
|---|---|---|
| 1 | 345 | Yes |
| 2 | 350 | Yes |
| 3 | 348 | Yes |
| 4 | 380 | No — flagged |
| 5 | 352 | Yes |
| 6 | 349 | Yes |

- **Baseline mean (5 units, excluding the flagged unit):** (345+350+348+352+349) / 5 = 1,744 / 5 = 348.8°C.
- **Unit 4 deviation:** 380 − 348.8 = 31.2°C.
- **Deviation as a percentage of baseline:** 31.2 / 348.8 = 8.9%.
- **Escalation threshold:** >5% deviation from baseline. 8.9% exceeds it.
- **Rating's action:** log the six raw readings, the baseline mean, and the deviation; report to the engineer of the watch by exact figures ("Unit 4 at 380, other five averaging 349, that's about 9% over"). No valve, rack, or setting is touched by the rating — diagnosis and correction are the engineer's authority.
- **What NOT to log as the finding:** "Unit 4 running hot" (an interpretation) instead of the reading, the baseline, and the percentage (the actual, escalatable finding).

## Preservation-cycle (chip/prime/paint) coverage worksheet (filled example)

Section: 40 m² of exposed weather-deck steel, corrosion holidays identified during a rounds inspection.

| Coat | DFT spec (microns) | Coverage rate (per data sheet) | Area | Gallons required | Gallons ordered |
|---|---|---|---|---|---|
| Primer | 75 | 11 m²/gal | 40 m² | 40 / 11 = 3.6 | 4 |
| Topcoat | 100 | 9 m²/gal | 40 m² | 40 / 9 = 4.4 | 5 |

- **Total system DFT:** 75 + 100 = 175 microns, matching the specified two-coat marine system.
- **Sequencing rule:** primer applied and allowed its full data-sheet recoat window (commonly 16–24 hours depending on product and ambient temperature) before topcoat goes on — never same-day for both coats on the same section, since a compressed cure shows no visible defect at inspection and fails within months.
- **Holiday-location priority:** a holiday found on this topside section is routine-priority; the same finding below the waterline or inside a ballast/void tank is treated as urgent and moved ahead of the current work order, because immersion drives corrosion rate independent of visibility.

## Drill-compliance tracker (filled example)

| Item | Value | SOLAS Ch. III, Reg. 19 requirement | Status |
|---|---|---|---|
| Crew signed off/on this port call | 5 of 18 (27.8%) | Drill within 24h of departure if >25% turnover | Triggered |
| Last abandon-ship/fire drill | Logged 0530, same rotation | Within 24h before departure | Met |
| Last lifeboat lowered/launched in water | 71 days ago | At least every 3 months (≈90 days) | Within interval, due in 19 days |
| Monthly drill cycle (no unusual turnover) | Last run 22 days ago | At least once per calendar month | Within interval |

- **27.8% crew turnover exceeds the 25% threshold**, which is why the drill was run before unmooring rather than waiting for the routine monthly cycle — the two triggers (turnover-based and calendar-based) are independent, and either one alone requires action.
- **Lifeboat-launch tracker exists specifically because the 3-month interval is a hard maximum**, not a target; a vessel that's 71 days in is not yet overdue but should have the next launch scheduled against the remaining 19-day margin, not left to be noticed only once it lapses.
