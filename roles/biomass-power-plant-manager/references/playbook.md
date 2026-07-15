# Fuel supply & combustion playbook

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Fuel-blend and ash-constraint worksheet (filled — see Worked example in SKILL.md for full narrative)

**Plant requirement:** 8,100 MMBtu/day (25 MW × 13,500 Btu/kWh heat rate). Ash-handling system capacity: 15 tons/day.

| Fuel | As-received HHV | Ash % | Delivered cost | Max daily volume before ash limit | Max daily energy from that volume |
|---|---|---|---|---|---|
| Primary (wood chips) | 8,000 Btu/lb | 2% | $32/ton | 750 tons (15 ÷ 0.02) | 6,000 MMBtu |
| Alternative (ag residue) | 7,200 Btu/lb | 8% | $37/ton | 187.5 tons (15 ÷ 0.08) | 2,700 MMBtu |

**Blend plan during shortfall (primary limited to 303.75 tons/day available):**
| Fuel | Volume | Energy | Cost |
|---|---|---|---|
| Primary | 303.75 tons | 4,860 MMBtu | $9,720 |
| Alternative (ash-capped) | 187.5 tons | 2,700 MMBtu | $6,937.50 |
| **Total** | **491.25 tons** | **7,560 MMBtu (93.3% of requirement)** | **$16,657.50** |

**Rule applied:** size the alternative fuel to the ash-system limit first, then check total energy against the requirement — never size to the energy gap first and discover the ash violation after committing to the volume.

## 2. Fuel source qualification checklist

| Criterion | Threshold | Status for candidate source |
|---|---|---|
| As-received HHV | State value; compare to combustion system's tested range | 7,200 Btu/lb — within tested range (6,800-8,200) |
| Ash content | Must not push daily ash above system capacity at planned volume | 8% — capped planned volume at 187.5 tons/day |
| Transport distance | Within economical radius (cost per MMBtu delivered, not price per ton at origin) | 150 mi; delivered cost $37/ton = $2.57/MMBtu vs. primary's $32/ton = $2.00/MMBtu |
| Moisture content | Within combustion parameter range without re-tuning | 22% — requires increased excess air/residence time vs. primary's normal setting |
| Seasonal availability | Confirmed volume through the shortfall window | Confirmed 187.5+ tons/day available through end of shortfall period |

## 3. Storage turnover and fire-risk monitoring log (template, filled example)

| Pile ID | Fuel type | Intake date | Days in storage | Last internal temp check | Temp reading | Action |
|---|---|---|---|---|---|---|
| P-14 | Wood chips | Day 1 | 38 | Day 38 | 142°F (rising from 128°F on Day 31) | Flagged for priority draw-down; re-check in 48 hrs |
| P-15 | Ag residue | Day 20 | 6 | Day 6 | 98°F | Normal — continue routine weekly checks |

**Rule applied:** any pile showing a rising temperature trend (not just an absolute threshold) gets prioritized for use or turnover before a pile with a stable, lower temperature but longer storage duration.

## 4. Seasonal procurement plan (filled example, agricultural-residue-heavy fuel mix)

| Month | Typical availability | Contracted volume | Inventory strategy |
|---|---|---|---|
| Sep-Nov (post-harvest peak) | High | 70% of annual need contracted | Build inventory to cover the Mar-Jun low-availability window |
| Dec-Feb | Moderate | 20% of annual need contracted | Draw down slightly, maintain buffer |
| Mar-Jun (known low) | Low | 10% of annual need contracted, supplemented by stored inventory | Draw primarily from fall-built inventory; monitor storage degradation closely given extended hold time |
| Jul-Aug | Moderate, rising into next harvest | Spot/short-term as needed | Minimal new storage commitment ahead of next peak |
