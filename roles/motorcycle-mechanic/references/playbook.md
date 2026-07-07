# Playbook

Filled reference material: the T-CLOCS checklist in full, chain-slack and tire-spec tables, the valve-clearance architecture comparison, and the seasonal storage-prep cost worksheet.

## 1. T-CLOCS pre-ride/intake inspection, in full

| Category | Check | Ride/no-ride trigger |
|---|---|---|
| **T**ires & wheels | Tread depth (3 points: crown + both shoulders), pressure cold, sidewall cracking, DOT date code, spoke tension/rim runout | Tread at wear bar; sidewall cracking at bead; DOT code older than ~5–6 years |
| **C**ontrols | Lever/pedal free play, cable routing and fray, throttle snap-back, clutch engagement point | Throttle doesn't snap back to idle; brake lever reaches the grip before engaging |
| **L**ights & electrics | Headlight (high/low), brake light (both switches), turn signals, horn, battery terminal corrosion | Brake light inoperative on either switch |
| **O**il & fluids | Engine oil level/condition, coolant level (liquid-cooled), brake fluid level/color/age, chain lube | Brake fluid contaminated or below minimum line |
| **C**hassis & suspension | Chain slack at tightest point, sprocket tooth profile, fork seal weep, shock linkage play, steering-head bearing drag | Chain slack past spec range with hooked sprocket teeth; steering-head notchiness under load |
| **S**tands | Sidestand spring tension and return, centerstand ground clearance, kickstand cutoff switch function | Sidestand doesn't return under spring tension alone (falls-over risk) |

## 2. Chain-slack and tire-spec quick reference

**Chain slack** — measured at the tightest point of the chain's travel (found by rotating the rear wheel through a full revolution and marking the point of least sag), bike in the manufacturer-specified stand position (commonly on the sidestand, weight on the wheel — verify per platform, some specify on the centerstand):

| Condition | Vertical deflection at tightest point |
|---|---|
| Typical manufacturer spec range | 20–30 mm (many Japanese standard/sport platforms) to 35–50 mm (some cruiser/shaft-adjacent chain designs) — confirm against the specific platform's manual before adjusting |
| Flag for inspection | Slack measured at more than ~1.5× the platform's spec upper bound |
| Replace chain + sprockets together | Slack can't be brought into spec within the adjuster's remaining travel, or sprocket teeth show a visible hooked/shark-fin profile |

**Tire tread and age:**

| Measure | Legal / spec minimum | Shop practitioner threshold (wet/lean riding) |
|---|---|---|
| Tread depth remaining | 1/32 in (0.8 mm) at the wear-bar indicator — common across US states | Flag for replacement nearer 2/32–3/32 in remaining, measured at the shoulder, not just the crown |
| Tire age (DOT date code, week/year) | No universal legal limit | Manufacturer guidance (Michelin, Dunlop) commonly suggests replacement around 5–6 years regardless of tread, due to sidewall hardening/cracking |
| Load index vs. bike GVWR | Tire sidewall load index must meet or exceed the bike's GVWR-derived per-tire load requirement | Check load index against actual GVW (bike + rider + cargo), not rim-size fit alone |

## 3. Valve-clearance architecture comparison

| Architecture | Adjustment method | Typical service interval | Failure mode if neglected |
|---|---|---|---|
| Screw-and-locknut (solid lifter, common on cruisers/singles) | Feeler gauge + locknut adjustment at the rocker | Commonly 4,000–8,000 mi / platform-specific | Loose clearance is noisy (tapping) well before it's damaging; tight clearance burns a valve with less warning |
| Shim-under-bucket (common on multi-cylinder sportbikes) | Feeler gauge measures clearance; cams removed and shims swapped to correct | Commonly 12,000–16,000 mi (~20,000–24,000 km), platform-specific | Same asymmetry as above, but the correction requires cam removal, making a skipped interval more consequential to catch late |
| Hydraulic lifter (many modern Harley-Davidson Evolution/Twin Cam/Milwaukee-Eight engines) | Self-adjusting, no manual clearance check | Not a scheduled interval item | N/A — applying a clearance-check interval to this architecture wastes a service call; the failure mode instead shows up as lifter noise/collapse, a different diagnostic path entirely |

**Always confirm architecture before quoting a valve service** — a shop that defaults to "valve clearance check every 16,000 mi" across its whole fleet either wastes the call on hydraulic-lifter bikes or under-services solid-lifter cruisers on a shorter interval.

## 4. Seasonal storage-prep cost worksheet

Reconciling example (fuel-stabilization/battery-tender prep vs. the spring repair it prevents), figures consistent with the SKILL.md worked example:

| | Prep done before layup | Prep skipped |
|---|---|---|
| Fuel stabilizer treatment | $8 product + 0.25 hr labor to circulate before storage = $8 + (0.25 × $95) = $31.75 | $0 upfront |
| Battery tender | One-time device, ~$35 (amortized across seasons, not charged per visit if customer owns one) or a shop drop-off/pickup service line | $0 upfront, but battery sulfation risk if resting at low charge for months |
| Spring result | Bike starts and idles normally; no carb service needed | Carb ultrasonic clean + pilot jet clear + float reset: 1.5 hr × $95 + $28 parts = $170.50 |
| **Net cost comparison** | **$31.75 spent** | **$170.50 spent, plus the inconvenience of a multi-day repair wait the customer didn't plan for** |

**Reconciling arithmetic:** $170.50 avoided repair − $31.75 prep cost = **$138.75 net savings** to the customer for doing prep, which is the number worth stating explicitly when pitching fall storage service — not "recommended maintenance," a specific avoided cost.

## 5. Ride/no-ride documentation checklist (every intake, before any repair is quoted)

- [ ] Tread depth measured at crown and both shoulders, DOT date code recorded.
- [ ] Chain slack measured at the tightest point of travel, in the manufacturer-specified stand position; sprocket tooth profile checked.
- [ ] Brake fluid age/color checked in both reservoirs (front and rear, if separate).
- [ ] Battery resting voltage checked if the bike has been stored or sat unused more than 30 days.
- [ ] Engine architecture (carbureted/EFI, air/liquid-cooled, lifter type) confirmed before diagnostic work begins.
- [ ] Any ride/no-ride finding communicated to the service writer and customer before the bike leaves the shop, independent of whether the customer authorizes the repair.
