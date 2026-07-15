# Production diagnostic artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Bottleneck analysis (filled — see Worked example in SKILL.md for full narrative)

| Station | Capacity (units/day) | WIP queued upstream | WIP trend |
|---|---|---|---|
| 1 — Prep | 1,400 | 20 | Stable |
| 2 — Subassembly | 1,280 | 35 | Stable |
| 3 — Core assembly | **976** | **340** | **Growing +15/day** |
| 4 — QC/test | 1,240 | 25 | Stable |
| 5 — Final assembly | 1,120 | 18 | Stable |
| **Actual line output** | **980/day** | | Matches Station 3 capacity almost exactly |

## 2. Capital investment comparison (filled example)

| Option | Target station | Cost | Capacity effect | Output effect | Payback |
|---|---|---|---|---|---|
| Overtime at Station 5 | Non-bottleneck | $340/day | 1,120 → 1,400/day | **0 units/day** (bottleneck elsewhere caps output) | Never — no output gain |
| Second fixture at Station 3 | Bottleneck | $28,000 one-time | 976 → 1,200/day | +220 units/day | 7.1 days at $18/unit margin |

**Rule applied:** capital is directed at the confirmed bottleneck, not the most visible or most recently problematic station — the overtime option would have been pure waste despite "feeling" productive.

## 3. OEE model (filled example)

| Component | Value | Note |
|---|---|---|
| Availability | 92% | Planned downtime (changeover, maintenance) accounted for |
| Performance | 88% | Actual speed vs. ideal cycle time |
| Quality | 96% | Good units / total units produced |
| **OEE** | **92% × 88% × 96% = 77.7%** | |

**Comparison — proposed speed increase at a non-bottleneck station:**

| Scenario | Performance | Quality | OEE |
|---|---|---|---|
| Before | 88% | 96% | 77.7% |
| After (25% faster, but defect rate rises) | 96% | 89% | 78.6% |

**Rule applied:** the speed increase looks good on the performance dimension alone, but the resulting quality drop means OEE barely moves — a single-metric read (speed) would have overstated the actual benefit.

## 4. Cost-of-quality-by-detection-point worksheet (filled example)

| Detection point | Cost per defect | Multiplier vs. source |
|---|---|---|
| At point of creation (in-process) | $12 (immediate rework) | 1x |
| At final inspection | $85 (disassembly, rework, retest) | ~7x |
| After shipment (customer discovery) | $2,400 (return, replacement, support cost, no brand-damage estimate included) | ~200x |

**Rule applied:** quality control investment (poka-yoke, in-process checks) is weighted toward the earliest feasible detection point given this cost multiplier, rather than concentrated at final inspection alone.
