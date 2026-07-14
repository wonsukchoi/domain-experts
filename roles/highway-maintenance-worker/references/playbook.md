# Highway Maintenance Playbook

Filled tables and step sequences for the three recurring maintenance calls: work-zone setup, pothole patching, and snow/ice control.

## 1. Lane-closure taper length by posted speed (MUTCD Part 6C)

Formula: speeds ≥45 mph use L = W × S; speeds ≤40 mph use L = W × S² / 60. W = lane/offset width in feet, S = posted speed in mph, L in feet. Example uses W = 12 ft.

| Posted speed (mph) | Formula used | Taper length L (ft) | Device spacing (~1 ft/mph) | Devices in taper |
|---|---|---|---|---|
| 25 | WS²/60 | 12 × 625 / 60 ≈ 125 | 25 ft | 125/25 + 1 = 6 |
| 35 | WS²/60 | 12 × 1225 / 60 ≈ 245 | 35 ft | 245/35 + 1 = 8 |
| 40 | WS²/60 | 12 × 1600 / 60 = 320 | 40 ft | 320/40 + 1 = 9 |
| 45 | WS | 12 × 45 = 540 | 45 ft | 540/45 + 1 = 13 |
| 55 | WS | 12 × 55 = 660 | 55 ft | 660/55 + 1 = 13 |
| 65 | WS | 12 × 65 = 780 | 65 ft | 780/65 + 1 = 13 |

Note the discontinuity at the 40→45 mph boundary is expected — MUTCD deliberately switches formulas there rather than interpolating; don't average the two results for an intermediate posted speed, use the formula matching the actual posted (not observed) speed.

Buffer space (between the end of the taper and the start of the actual work space) is a separate MUTCD Table 6C-2 lookup by speed, not part of this formula — pull the current buffer table for the posted speed rather than estimating it as a multiple of the taper.

## 2. Pothole material selection by pavement/ambient temperature

| Condition | Material | Why | Follow-up required |
|---|---|---|---|
| ≥40°F, dry, forecast holding | Hot-mix asphalt (HMA), tack coat on vertical faces | Compacts and bonds properly at this range | No — treat as permanent if properly compacted |
| <40°F, or wet pavement | Cold-mix bagged premix | HMA won't stay workable long enough to compact; cold mix is designed for this range | Yes — flag hot-mix follow-up for first dry day forecast ≥40–50°F |
| <40°F, high-ADT road where any closure is high-risk | Cold-mix premix, minimal-time patch | Same material logic; closure duration is the variable being minimized | Yes, same as above, higher priority |
| Same location patched ≥2 times in one season | Do not re-patch surface only | Recurring failure indicates subsurface/drainage defect, not a surface one | Route to drainage/subgrade inspection before next patch |

**Coverage arithmetic (cold-mix bagged premix):** a standard 50 lb bag covers approximately 0.5 ft³ of compacted fill. To size bags needed: volume (ft³) = π × r² × depth (r, depth in ft), then bags = ceil(volume ÷ 0.5). Round the material order up, never down — running out mid-patch means reopening a closed lane to restock.

Example: 18-in diameter, 4-in deep pothole → r = 0.75 ft, area = π × 0.75² ≈ 1.77 ft², volume = 1.77 × 0.333 ≈ 0.59 ft³ → 0.59 ÷ 0.5 ≈ 1.18 → order 2 bags.

## 3. Snow/ice chemical selection and application rate by pavement temperature

| Pavement temp | Chemical | Typical rate | Notes |
|---|---|---|---|
| ≥25°F | Straight rock salt (NaCl), dry or pre-wet | 150–200 lb/lane-mile (anti-icing, ahead of black ice) | Most cost-effective range |
| 15–25°F | NaCl, pre-wet with brine, or blended with CaCl₂/MgCl₂ | 200–300 lb/lane-mile | Straight dry salt slows noticeably; pre-wetting improves adhesion and melt speed |
| <15°F | Chloride blend (CaCl₂/MgCl₂) or abrasives (sand) | Per manufacturer chart, not the NaCl rate | Plain rock salt's melt rate collapses below this range — spreading more NaCl does not compensate |
| Any temp, black-ice-prone bridge deck or shaded curve | Pre-treat with brine before precipitation (anti-icing) | 30–50 gal/lane-mile brine, ahead of storm | Anti-icing before bonding beats deicing after — a bonded layer takes far more material and time to break |

Read pavement temperature from a pavement sensor or infrared gun, not the truck cab thermometer — pavement can run 5–15°F colder than air on a clear, calm night due to radiational cooling.

## 4. Post-crash guardrail repair checklist

1. Confirm the damaged section's system type (standard W-beam, thrie-beam, cable) and its rated dynamic deflection from the as-built record or manufacturer spec — don't assume it matches a similar-looking run elsewhere on the route.
2. Measure the current offset from the back of the rail location to the nearest fixed object behind it (bridge pier, culvert headwall, sign post foundation, rock cut).
3. If the measured offset is less than the system's rated deflection, do not reinstall the standard section — specify a stiffened repair (nested rail, reduced post spacing) or escalate to the district engineer for a redesigned section.
4. Confirm the end terminal (if within the repaired run) is a MASH-rated unit matching the current rail height and system — a mismatched terminal from parts stock is a common source of a repair that looks complete but isn't rated as a system.
5. Log the repair with system type, terminal part number, and measured offset on the work order — this is what a future crew checks before assuming "matches what's there."
