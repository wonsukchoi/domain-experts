# Playbook

## Axis-tolerance check by cylinder power (filled example)

Commonly cited ANSI Z80.1-based axis tolerance guidance, tightening as cylinder power increases:

| Cylinder power | Typical axis tolerance |
|---|---|
| 0.12–0.37 D | ±14° |
| 0.38–0.62 D | ±8° |
| 0.63–1.00 D | ±5° |
| 1.01–2.00 D | ±3° |
| Over 2.00 D | ±2° |

**Applied to the worked example:** Job at -1.50 D cylinder falls in the 1.01–2.00 D bracket, tolerance ±3°. Measured axis 085° vs. ticket 090° is a 5° error — exceeds the ±3° tolerance for this power. Reject and regrind.

**Comparison — same 5° error at a different cylinder power:**

| Cylinder power | Tolerance | 5° error status |
|---|---|---|
| 0.25 D | ±14° | Within tolerance — acceptable |
| 0.75 D | ±5° | Within tolerance — acceptable |
| 1.50 D | ±3° | **Exceeds tolerance — reject** |
| 2.50 D | ±2° | **Exceeds tolerance — reject** |

The same 5° axis deviation is acceptable at low cylinder power and rejection-worthy at moderate-to-high cylinder power — axis checks always have to reference the specific job's cylinder power, not a single flat threshold.

## Prism/decentration verification worksheet (filled example)

Job ticket: OD -4.00 -1.50 × 090, 0.5△ base-in prism, optical center at wearer's monocular PD (32mm).

| Check | Ticket specification | Lensometer/measurement result | Status |
|---|---|---|---|
| Sphere | -4.00 D | -4.00 D | Match |
| Cylinder | -1.50 D | -1.50 D | Match |
| Axis | 090° | 085° | **Mismatch — 5° error, exceeds ±3° tolerance at this power** |
| Prism | 0.5△ base-in | No prism detected at check point | **Mismatch — missing or optical center mispositioned** |
| Decentration point | Wearer's PD (32mm) | Verify against tracing/blocking record | Confirm before final release |

**Result:** Two independent discrepancies (axis, prism) — both must be resolved via regrind and re-check before this lens proceeds to edging.
