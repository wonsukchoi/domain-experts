# Playbook

Filled tables and worksheets for triaging PLC, VFD, and control-panel faults under arc-flash-aware, downtime-cost-driven field service.

## 1. Downtime-cost triage worksheet (simultaneous down-calls)

Fill for every open call before dispatching to any one of them.

| Line/asset | Downtime cost ($/hr) | Est. repair time (min) | Priority weight ($/hr ÷ min) | Rank |
|---|---|---|---|---|
| Line A — conveyor VFD, F5 OV trip | $9,500 | 25 | 380.0 | 1 |
| Line B — pusher photoeye, rung false | $2,200 | 15 | 146.7 | 2 |

Rule: dispatch to the highest priority-weight first, not the highest raw $/hr and not call order — a fast fix on a high-cost line clears more total dollar exposure than a slow fix on the same line would, and can outrank a lower-cost line even if that line's raw $/hr looks smaller. Recompute the ranking any time a new call comes in or an estimate changes materially (>25% swing).

Exception: a call involving an active safety hazard (smoke, arc, exposed conductor, guard defeated) outranks any cost calculation — go there first regardless of $/hr.

## 2. VFD fault-code category table (generic, cross-manufacturer pattern)

| Category | Example fault names | Likely physical location | First check |
|---|---|---|---|
| Input/line-side | Undervoltage (UV), input phase loss, line transient at power-up | Incoming line, transformer taps, upstream breaker/contactor | Line voltage per phase, transformer tap setting, breaker trip history |
| Output/motor-load side | Overcurrent (OC), ground fault (GF), output phase loss, motor overload | Motor windings, output cable, mechanical binding on the driven load | Megger test on motor leads, clamp-meter current balance across phases, manual jog check for binding |
| Drive-internal | Heatsink overtemperature (OH/OT), IGBT desaturation, control-board watchdog/comm fault | Cooling fan, heatsink, power module, control board | Fan operation, heatsink temperature, fault-log timestamp vs. ambient/load conditions |
| Regenerative/braking | DC bus overvoltage (OV) during deceleration | Dynamic-braking (DB) resistor, chopper transistor, decel ramp setting | Confirm trip is decel-only (not at power-up/steady speed); ohm-check the DB resistor against nameplate rating |

Sequencing rule: match the fault category to a physical location *before* opening the drive, and confirm the category-implied location with a live test before swapping any part. A fault that could be either output-side or drive-internal (e.g., a ground-fault code with no obvious cable damage) gets the cheaper, faster test first — megger the motor leads before pulling the drive's power module.

## 3. PLC signal-trace worksheet (field device → wiring → I/O module → logic)

| Step | Check | Result pattern | Points to |
|---|---|---|---|
| 1 | Field device's own indicator (sensor LED, limit-switch flag) | Device shows "actuated"/"sees target" | Device believes it's working — move to step 2 |
| 2 | I/O module's physical status LED for that point | LED **off** while device shows actuated | Wiring/terminal path between device and card |
| 2 | I/O module's physical status LED for that point | LED **on** | Signal reached the card — move to step 3 |
| 3 | Software online-monitor tag/bit value vs. forced-value flag | Bit shows false/0 despite LED on, no force active | PLC-side: address mapping, card channel fault, or module failure |
| 3 | Software online-monitor tag/bit value vs. forced-value flag | Bit is forced to a fixed value | Program was left in a forced state — not a physical fault at all; clear the force and re-test |
| 4 | Ladder rung logic upstream of the bit (interlocks, other conditions ANDed in) | Bit is genuinely true but the rung output still doesn't fire | Program logic itself — an unmet interlock or an incorrect rung condition, not the I/O point |

Rule: never open the field device or replace a card before completing the step where the pattern first diverges from expected — most calls are resolved by step 2 or 3, and opening the device housing first is guessing with tools already in hand.

## 4. Board/drive swap-vs-component-repair worksheet

| Line item | Bench repair | Board/drive swap |
|---|---|---|
| Labor time (minutes) | diagnosis (already done via steps above) + repair + test | swap + parameter/auto-tune reload + test |
| Loaded labor rate | shop rate, typically $85–125/hr fully loaded | same rate |
| Part cost | component-level part(s) — resistor, fan, gate-driver chip, connector | full drive/module/board assembly |
| Downtime exposure while working | repair time × line's $/hr | swap time × line's $/hr |
| **Total** | labor$ + part$ + downtime-during-repair$ | labor$ + part$ + downtime-during-swap$ |

Decision gate, in order:
1. Confirmed component-level failure (fan, resistor, discrete part) with the part on the truck and bench-repair time comfortably inside the schedule → **repair**, take the lower total.
2. Root cause ambiguous between two internal components, or no bench part on hand, and remaining schedule is tight → **swap**, accept the higher cost for certainty and speed.
3. Same fault code and category has recurred 2+ times on the same asset within 30 days → neither yet; pull 90-day fault-log history and escalate to a root-cause review before repeating either fix a third time.

## 5. Arc-flash PPE category quick-reference (verify against site's current arc-flash study before use)

| PPE Category | Approx. incident-energy band | Minimum arc-rated clothing system | Typical additional PPE |
|---|---|---|---|
| 1 | ≈1.2–4 cal/cm² | AR-rated shirt/pants or coverall, ≥4 cal/cm² | Arc-rated face shield or hood, safety glasses, hearing protection, insulated gloves rated for system voltage |
| 2 | ≈>4–8 cal/cm² | AR-rated coverall system, ≥8 cal/cm² | Arc-rated face shield/hood, balaclava, hearing protection, insulated gloves |
| 3 | ≈>8–25 cal/cm² | AR-rated multi-layer flash suit, ≥25 cal/cm² | Arc-rated flash hood, insulated gloves, leather protectors |
| 4 | ≈>25–40 cal/cm² | AR-rated multi-layer flash suit, ≥40 cal/cm² | Arc-rated flash hood, insulated gloves, leather protectors |
| >40 | above 40 cal/cm² | No PPE system rated adequate | De-energize — live work not performed at this level |

The panel's arc-flash label states the calculated incident energy and working distance for that specific piece of equipment — use the label's number, not this table's midpoint, to select PPE. This table is a sanity check for whether a label looks plausible, not a substitute for it.
