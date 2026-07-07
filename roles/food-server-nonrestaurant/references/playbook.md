# Playbook

Filled templates for the four documents this role actually runs on: the service-ratio staffing table, the guarantee/overset reconciliation sheet, the tray-line verification log, and the course-drop timing worksheet. Use these as the executable shape, not as illustrations.

## 1. Service-ratio staffing table

Ratio is covers (guests) per server, by service style. Plated needs the most staff per guest because every cover is an individual timed delivery; buffet and reception need fewer because guests self-serve the bulk of the meal.

| Service style | Covers per server | Notes |
|---|---|---|
| Plated, standard | 1:16–20 | Station of 2 rounds of 8–10 |
| Plated, head table / VIP | 1:8–10 | Tighter ratio, individual-plate timing matters more |
| Buffet | 1:30–40 | Servers replenish/bus, don't deliver individual plates |
| Reception, passed hors d'oeuvre | 1:25–30 | Per passing server, not per bartender |
| Reception, bar service | 1:75–100 | Bartender ratio, separate headcount from food servers |
| Hospital/LTC tray line, assembly | 1 assembler per ~40–60 trays/hour | Depends on tray complexity (standard vs. modified) |
| Hospital/LTC tray line, unit delivery | 1 server per ~20–30 trays per delivery round | Round trip includes bedside identity check |

**Worked staffing calc — 320-cover plated banquet:**

320 covers ÷ 20 covers/server = 16 servers, arranged as 8 stations of 2 servers each covering 4 rounds (40 covers/station), or 16 single-server stations of 2 rounds (20 covers) each — the room in the SKILL.md worked example used the latter.

## 2. Guarantee / overset reconciliation sheet (filled example)

| Field | Entry |
|---|---|
| Event | Corporate Dinner, Grand Ballroom |
| Guarantee submitted | 300 (72 hrs prior to event, per contract) |
| Overset % applied | 5% |
| Covers prepped by kitchen | 315 (300 × 1.05) |
| Actual attendance | 316 |
| Variance vs. prepped | +1 (escalated to kitchen at 6:45 p.m., 1 emergency plate fired) |
| Billing basis | 316 (greater of guarantee or actual, per contract) |
| Allergen/modified plates | 3 (shellfish-free, gluten-free, dairy-free — seats 4, 17, 29) |

**Reconciliation rule of thumb:** if actual attendance falls at or below the prepped overset, service proceeds without a kitchen escalation. If actual attendance exceeds the prepped overset by any amount, that's an immediate captain-to-kitchen flag — not something absorbed by re-portioning existing plates, because banquet portions are fixed and plated, unlike a buffet where a shortfall can sometimes be stretched.

## 3. Tray-line verification log (hospital/long-term-care, filled example)

**Checkpoints (post at every tray-line station):**

| Stage | Check | Limit/requirement |
|---|---|---|
| Tray assembly | Ticket item matches tray contents | 100% match required before tray moves to cart |
| Tray assembly | Hot component temperature | ≥ 140°F at assembly |
| Tray assembly | Cold component temperature | ≤ 41°F at assembly |
| Cart load | Tray position matches cart manifest (room/bed order) | Sequential, no gaps or duplicates |
| Unit delivery | Two-identifier check (name + room/bed, or name + DOB) | Verified against tray ticket before uncovering |
| Unit delivery | Elapsed time since assembly | Within facility's stated meal-delivery window (commonly 30–45 min) |

**Filled log — 42-tray delivery round, 3rd floor med-surg unit:**

| Tray # | Diet order | Ticket match at assembly | Temp at assembly | ID check at delivery | Result |
|---|---|---|---|---|---|
| 214 | Renal, no-added-salt | Match | Hot 148°F / Cold 38°F | Name + room# confirmed | Delivered |
| 215 | Regular, no allergen flags | Match | Hot 146°F / Cold 39°F | Name + room# confirmed | Delivered |
| 216 | Pureed (IDDSI 4), dairy allergy | Mismatch — tray carried standard-texture item | Hot 144°F / Cold 40°F | Held before cart load | Returned to line, corrected, re-verified, delivered 8 min later |
| 217 | Cardiac, low-sodium | Match | Hot 145°F / Cold 39°F | Name + room# confirmed | Delivered |

Tray 216 is the case the two-checkpoint rule exists for: the mismatch was caught at assembly (first check), before it ever reached the second, bedside check — the error never had a chance to reach the patient.

## 4. Course-drop timing worksheet (banquet, filled example)

Target: entire room served within a 12–15 minute window from the captain's "fire" call, for a room up to roughly 250–300 covers; larger rooms add stations rather than accepting a longer window.

| Room size (covers) | Stations (servers) | Covers/station | Trips/station (3 plates/trip) | Target drop window |
|---|---|---|---|---|
| 160 | 8 | 20 | 7 | 12 min |
| 240 | 12 | 20 | 7 | 13 min |
| 320 | 16 | 20 | 7 | 14–15 min |
| 400 | 20 | 20 | 7 | 14–15 min (add stations, don't slow pace) |

**Worked example — 320-cover room:**

- 16 stations × 20 covers = 320 plates.
- 3 plates per hand-carried trip → 7 trips per station (six of 3, one of 2).
- Budget ≈ 2 min per round trip (kitchen pass to table and back) → 7 × 2 = 14 min per station.
- Captain fires all 16 stations simultaneously at 7:10 p.m.; last station clears at 7:24 p.m. — 14 minutes, inside the 12–15 minute target.

If any single station is still running past minute 15, the captain's response is to pull a floater server into that station for the next event, not to accept a longer standard window going forward.
