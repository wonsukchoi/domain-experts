# Reservoir management artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Decline curve worksheet (filled — see Worked example in SKILL.md for full narrative)

| Metric | Value |
|---|---|
| Current field output | 38 MW |
| Modeled decline rate | 3%/year |
| Actual observed decline rate (trailing 18 months) | 7%/year |
| Projected output next year (modeled) | 36.86 MW |
| Projected output next year (actual trend) | 35.34 MW |
| Corporate target | 45 MW |
| Gap between actual trend and target | 9.66 MW |

**Reading it:** the gap between modeled and actual decline (7% vs. 3%) is itself the primary finding — it signals the field may already be past sustainable yield, which should shape how (or whether) the corporate target is pursued.

## 2. Workover economics model (filled example)

| Well | Current output | Field average | Workover cost | Projected recovery (65% of gap) | Projected new output | Cost per MW gained |
|---|---|---|---|---|---|---|
| Well 8 | 1.8 MW | 3.17 MW | $2.4M | +0.89 MW | 2.69 MW | $2.70M/MW |
| Well 9 | 1.8 MW | 3.17 MW | $2.4M | +0.89 MW | 2.69 MW | $2.70M/MW |
| **Total** | 3.6 MW | | $4.8M | +1.78 MW | 5.38 MW | $2.70M/MW |

**Comparison — new well (higher model uncertainty given 4-year field history):**

| Scenario | Output | Cost | Cost/MW |
|---|---|---|---|
| Mid-case | 3.0 MW | $8.5M | $2.83M/MW |
| Downside case | 1.5 MW | $8.5M | $5.67M/MW |

**Rule applied:** workover is preferred here on both cost-efficiency ($2.70M/MW vs. $2.83M/MW mid-case) and risk grounds (narrower outcome range) given this field's limited production history.

## 3. Reservoir-wide pressure check (filled example)

| Well | Proposed change | Own-well output effect | Reservoir-wide pressure effect | Net recommendation |
|---|---|---|---|---|
| Well 3 | Increase draw 15% | +0.4 MW | Reduces wells 4 & 5 output by est. 0.5 MW combined | Net negative — do not proceed |
| Well 8, 9 | Workover | +1.78 MW combined | Minimal reservoir-wide pressure effect (restoring, not increasing draw) | Proceed |

**Rule applied:** a well-level decision is evaluated on its reservoir-wide net effect, not its own-well output alone — Well 3's proposal looks good in isolation but is net-negative once neighboring well impact is included.

## 4. Seismic monitoring traffic-light protocol (filled example)

| Level | Seismic activity threshold | Action |
|---|---|---|
| Green | Below M2.0, background rate | Normal operations |
| Yellow | M2.0-M3.0, or rate increase 2x+ background | Reduce injection rate 25%, increase monitoring frequency |
| Red | Above M3.0, or continued increase after yellow response | Suspend injection at affected well(s), full review before resuming |

**Rule applied:** each threshold has a specific, predefined action — response isn't decided in the moment under pressure, and a yellow-level event this week already triggered the defined 25% injection reduction per protocol.
