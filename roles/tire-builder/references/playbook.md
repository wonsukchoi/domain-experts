# Playbook

## Splice-tolerance rejection calculation (filled example)

Belt splice specification: 15mm ± 3mm (acceptable range 12–18mm). Measured overlap: 9mm.

| Step | Value |
|---|---|
| Target overlap | 15mm |
| Tolerance | ± 3mm |
| Acceptable range | 12mm – 18mm |
| Measured overlap | 9mm |
| Deviation from target | 15 − 9 = 6mm |
| Deviation as % of target | 6 / 15 = 40% |
| Deviation below minimum threshold | 12 − 9 = 3mm |

**Result:** 9mm is 40% under the target and 3mm below even the minimum acceptable threshold — reject and rebuild the splice before proceeding.

## Stock tack-window check (filled example)

Ply stock calendered at 8:00 AM Monday. Documented tack window for this compound: 48 hours.

| Check point | Time since calendering | Within 48-hour window? |
|---|---|---|
| Used at 2:00 PM Monday | 6 hours | Yes |
| Used at 8:00 AM Wednesday | 48 hours | Yes — right at the edge |
| Used at 2:00 PM Wednesday | 54 hours | **No — 6 hours past window, flag for adhesion risk** |

**Rule applied:** Any stock use beyond the documented tack window gets flagged for inspection or rejection, even if it visually looks identical to fresh stock — tack degradation isn't visible to the eye.

## Defect-traceability worksheet (filled example)

Three green tire rejections for under-lapped belt splices over one week.

| Tire ID | Build station | Shift | Splice measurement |
|---|---|---|---|
| T-4471 | Station 4 | Day | 9mm (target 15mm) |
| T-4488 | Station 4 | Day | 10mm (target 15mm) |
| T-4502 | Station 4 | Day | 8mm (target 15mm) |

**Conclusion:** All three defects trace to Station 4's day shift — this is a station/equipment or operator-training issue, not three unrelated one-off build errors. Investigate the splice application mechanism at Station 4 specifically before treating this as normal build variance.
