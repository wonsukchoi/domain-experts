# Playbook

Filled worksheets an operator actually runs against a specific line, not descriptions of them — substitute the numbers for the conveyor in front of you.

## 1. Throughput/capacity worksheet (bottleneck identification)

Formula: **Q (tph) ≈ 60 × v (fpm) × A (ft²) × ρ (lb/ft³) ÷ 2000**, where v is measured belt speed (not nameplate), A is the loaded cross-sectional area at the current troughing/loading condition, and ρ is material bulk density. Compute this for every conveyor in the series — the line's actual throughput ceiling is the **minimum** of the computed values, not the conveyor with the highest amp draw or the one nearest the end process.

| Conveyor | Design speed (fpm) | Measured speed (fpm) | Rated tph (design speed) | Actual tph (measured speed) |
|---|---|---|---|---|
| C1 | 425 | 425 | 520 | 520 |
| C2 | 350 | 280 | 460 | 368 |
| C3 | 400 | 400 | 500 | 500 |

**Reading the table:** the line's actual ceiling is 368 tph (C2), not 520 or 500 — even though C1 shows the highest motor amperage. Amperage tells you about friction and drag; it does not tell you about rated capacity. Always cross-check measured speed against nameplate design speed before trusting a rated-tph figure — a conveyor silently running below its design speed (workaround, belt slip, VFD derated after a fault) is the single most common way a "known" rated capacity turns out to be wrong in the field.

**Escalation trigger:** any conveyor measuring speed more than 10% below its nameplate design speed with no open work order explaining why — that's an unticketed capacity reduction, and it's usually the bottleneck.

## 2. LOTO energy-source checklist by conveyor configuration

A single "main disconnect locked" note is not verification — enumerate every energy source physically present on that specific unit before signing off isolation.

| Conveyor feature present | Energy source | Isolation action required |
|---|---|---|
| Electric drive motor (all conveyors) | Electrical | Lock/tag main disconnect; verify zero energy with tester, not by assumption |
| Gravity (counterweighted) take-up | Stored/potential (mechanical) | Block or chain the counterweight carriage in addition to electrical lockout — the carriage can drop and re-tension/move the belt on its own |
| Inclined or declined belt, loaded | Gravity (material load) | Block the belt against roll-back (mechanical belt clamp/dog) before opening any point on the loaded run — electrical lockout does not stop a loaded incline belt from rolling back |
| Pneumatic clutch or brake | Stored pneumatic | Bleed and lock out the air supply; verify zero pressure at gauge |
| Screw (mechanical) take-up | None beyond electrical | Electrical lockout only — do not spend time blocking a screw take-up, it holds no stored gravity energy |
| Flywheel or high-inertia drive | Kinetic (residual) | Allow full stop and verify zero motion before working the isolation point, not just power-off |

**Verification order:** lock, tag, then physically attempt to operate the local control (try-out) — for gravity take-ups and inclines, physically confirm the block/chain is engaged and load-bearing, not just present. A block set loosely enough to allow the carriage or belt to shift under its own weight is not isolation.

## 3. Mistracking diagnostic table

| Symptom pattern | Likely cause | Action |
|---|---|---|
| Walks the same direction empty and loaded | Structural/idler misalignment | Framing-square check at training idler; escalate if out-of-square exceeds ~1° |
| Walks only under load, tracks fine empty | Load placement / loading chute off-center | Check chute alignment and material drop point relative to belt centerline before touching idlers |
| Walks only when empty, tracks fine loaded | Belt carcass camber or splice skew | Inspect splice squareness; escalate to maintenance if splice is the cause — not an idler adjustment |
| Tracks correctly for <1 shift after a training-idler correction, then walks again | Recurring structural cause, not idler wear | Escalate — three retracking attempts on the same idler without holding is a diagnostic lead, not a maintenance chore |
| Edge fraying or spillage concentrated at one point along the belt | Local mistracking at that section, not a whole-belt issue | Inspect the specific idler/structure at that station first, don't retrack the full length |

**Reconciling example:** a belt shows edge wear only near the tail pulley, walks the same direction whether loaded or empty, and the training-idler correction there held for 6 hours before recurring twice. Pattern matches "walks under all conditions + doesn't hold" → structural misalignment at the tail section, escalate with the framing-square reading (e.g., 2.5° out of square) rather than adjusting the idler a fourth time.

## 4. Splice selection and rated-capacity comparison

| Splice type | Typical rated capacity (% of belt's full rated tensile strength) | Install time | When to use |
|---|---|---|---|
| Vulcanized (hot) | ~90–100% | Longest (hours, requires press/heat) | Continuous high-tension or high-cycle service; long-belt-life installations |
| Vulcanized (cold) | ~80–90% | Moderate | Similar service to hot vulcanized where a press isn't available |
| Mechanical fastener — solid plate | ~55–65% | Fast (under an hour) | Lower-tension runs, frequent-splice-access applications, temporary repair pending a vulcanized redo |
| Mechanical fastener — hinged/wire hook | ~35–50% | Fastest | Light-duty or low-tension belts only; not a substitute for vulcanized at rated operating tension near the fastener's ceiling |

**Worked check:** a belt's operating tension runs at 42% of its full rated tensile strength. A hinged mechanical fastener rated to ~40% is running with almost no margin — the fastener, not the belt, becomes the limiting component, and any tension spike (a jam, a load surge) risks splice failure before the belt itself would fail. The correct call is stepping up to a solid-plate fastener (55–65% rating) or a vulcanized splice, not accepting the thin margin because the current fastener "hasn't failed yet."

## 5. Guard verification (standard + field practice)

| Check | Standard reference | Pass condition |
|---|---|---|
| Nip point guarded if within 7 ft of a walking/working surface | ANSI/ASME B20.1, OSHA 1910.212 convention | Guard present and fixed (not hinged-open) at every pulley, take-up, and snub point meeting this criterion |
| Guard opening sized so fingers/hand cannot reach the nip point at the guard's standoff distance | OSHA 1910.212 point-of-operation guarding convention | Opening small enough at the guard's actual distance from the hazard — verify with the distance/opening table on the guard's installation record, not by eye |
| Field practice: is the guard ever propped open for routine access? | — | No — if jam-clearing routinely happens through a propped panel or opening, the guard is defeated regardless of its physical compliance; escalate as a practice issue, not just a hardware fix |
