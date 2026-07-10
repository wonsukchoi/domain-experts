# Playbook

## Open-time-vs-pot-life timeline check (filled example)

Adhesive specification: pot life 45 min, open time 20 min. Application timestamp: 9:00:00.

| Event | Timestamp | Elapsed from mix | Elapsed from application |
|---|---|---|---|
| Adhesive mixed | 8:55:00 | 0 min | — |
| Adhesive applied to substrate | 9:00:00 | 5 min | 0 min |
| Final clamping completed | 9:24:00 | 29 min | 24 min |

| Check | Limit | Actual | Status |
|---|---|---|---|
| Pot life (mix to final use) | 45 min | 29 min | Within limit |
| Open time (application to clamp) | 20 min | 24 min | **Exceeded by 4 min (20% overrun)** |

**Result:** Pot life is comfortably satisfied, but open time — the actual governing constraint for this failure mode — was exceeded. Flag for proof/destructive testing rather than releasing based on the pot-life check alone.

## Cure verification worksheet (filled example)

Cure schedule: 60 minutes at 250°F, part temperature (not chamber setpoint) must reach and hold 250°F for the full 60 minutes.

| Time | Chamber setpoint | Actual part temperature (thermocouple) | Cure clock running? |
|---|---|---|---|
| 0 min | 250°F | 180°F (still heating up) | No — part hasn't reached cure temp |
| 15 min | 250°F | 245°F | No — still 5°F below cure temp |
| 22 min | 250°F | 250°F | Yes — cure clock starts now |
| 82 min | 250°F | 250°F | Cure complete (60 min held from minute 22) |

**Naive error:** If cure time were tracked from when the chamber reached 250°F (time 0) or simply from elapsed time in the oven, this part would be pulled at the 60-minute mark (well before the part itself has actually held 250°F for 60 minutes) — releasing an under-cured assembly that measures identically to a fully-cured one on visual inspection.

## BLT and spacer selection reference (filled example)

Adhesive specification: optimal bond line thickness 0.15–0.25mm.

| Spacer/method | Resulting BLT | Within spec? |
|---|---|---|
| No spacer, clamp pressure alone | Variable, often <0.10mm (over-squeezed) | **No — commonly understated, joint starved** |
| 0.20mm calibrated glass bead spacers | 0.20mm (controlled) | Yes |
| 0.30mm fixture stop (wrong spec referenced) | 0.30mm | **No — 20% over the 0.25mm upper limit** |

**Rule applied:** Always confirm the spacer/fixture stop dimension matches the specific adhesive's specified BLT range for this joint — a stop borrowed from a different job's spec can silently put the joint outside tolerance even though a spacer is being used.
