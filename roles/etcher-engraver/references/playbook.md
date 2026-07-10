# Playbook

## Undercut-compensation calculation (filled example)

Target final line width 0.30mm, etch depth 0.10mm, isotropic undercut ratio ~1:1.

| Step | Value |
|---|---|
| Target final line width | 0.30mm |
| Etch depth | 0.10mm |
| Undercut per side (1:1 ratio) | 0.10mm |
| Total undercut (both sides) | 0.10 × 2 = 0.20mm |
| Compensated resist opening | 0.30 − 0.20 = 0.10mm |
| Result if resist opening built at naive 0.30mm | 0.30 + 0.20 = 0.50mm final width — 66.7% over target |

## Etch time worksheet (filled example)

Etch rate 0.025mm/minute, target depth 0.10mm.

| Target depth | Etch rate | Calculated time |
|---|---|---|
| 0.05mm | 0.025mm/min | 0.05 / 0.025 = 2.0 min |
| 0.10mm | 0.025mm/min | 0.10 / 0.025 = 4.0 min |
| 0.15mm | 0.025mm/min | 0.15 / 0.025 = 6.0 min |

**Verification step:** Run a test coupon at the calculated time and measure actual depth with a profilometer before committing the full production batch — especially on a new material lot, where the true etch rate may differ from the nominal 0.025mm/min value used in this calculation.

## Adjacent-line bridging check (filled example)

Two resist openings spaced 0.40mm apart (center to center), each 0.10mm wide, at a depth producing 0.10mm undercut per side.

| Element | Value |
|---|---|
| Opening 1 width | 0.10mm |
| Opening 2 width | 0.10mm |
| Center-to-center spacing | 0.40mm |
| Gap between opening edges (before undercut) | 0.40 − (0.10/2 + 0.10/2) = 0.30mm |
| Undercut eating into the gap from each side | 0.10mm + 0.10mm = 0.20mm total |
| Remaining gap after undercut | 0.30 − 0.20 = 0.10mm |

**Result:** 0.10mm of material remains between the two etched features after undercut — they don't bridge, but the margin is thin. If spacing were 0.30mm center-to-center instead of 0.40mm, the gap before undercut would only be 0.20mm, and the same 0.20mm combined undercut would fully consume it — a bridging defect that isolated per-line undercut calculations wouldn't catch without this combined check.
