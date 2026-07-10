# Playbook

## Batch mass balance reconciliation (filled example)

Batch reactor, reactant A + B charge, expected 1–2% evaporation loss.

| Step | Value |
|---|---|
| Reactant A charged | 500 kg |
| Reactant B charged | 300 kg |
| Total charged | 800 kg |
| Expected evaporation loss (1–2%) | 8–16 kg |
| Expected in-vessel weight range | 784–792 kg |
| Actual measured in-vessel weight | 770 kg |
| Total shortfall vs. total charged | 800 − 770 = 30 kg |
| Unaccounted shortfall (high end of expected loss) | 30 − 16 = 14 kg |
| Unaccounted shortfall (low end of expected loss) | 30 − 8 = 22 kg |

**Result:** 14–22 kg unaccounted for beyond expected evaporation — escalate for leak check, instrument calibration, and byproduct sampling rather than accepting as normal variance.

## Alarm priority classification worksheet (filled example)

| Alarm | Consequence severity | Time-to-effect | Priority | Response order |
|---|---|---|---|---|
| High reactor pressure | Severe (relief valve activation risk) | Minutes | **Priority 1** | Respond first, regardless of trigger order |
| Cooling water flow low | Moderate (feeds into exotherm risk) | Tens of minutes | Priority 2 | Respond second |
| Level transmitter noise | Low (nuisance, known instrument quirk) | Hours+ | Priority 3 | Acknowledge, investigate when capacity allows |

**Scenario:** All three alarms trigger within 2 minutes of each other, with the level transmitter noise alarm firing first chronologically. Correct response order is High reactor pressure → Cooling water flow low → Level transmitter noise, based on priority classification — not the order they actually fired.

## Combined-variable safe-envelope check (filled example)

| Variable | Individual limit | Current value | Individually within limit? |
|---|---|---|---|
| Temperature | ≤ 180°C | 175°C | Yes (5°C margin) |
| Pressure | ≤ 8.0 bar | 7.6 bar | Yes (0.4 bar margin) |
| Concentration | ≤ 40% | 37% | Yes (3-point margin) |

**Combined assessment:** All three variables individually pass, but each sits within a narrow margin of its own limit simultaneously — a combination that historically precedes an excursion in this process, even though no single variable has crossed its threshold. Flag as a caution condition for supervisor awareness rather than confirming "all clear" from the individual checks alone.
