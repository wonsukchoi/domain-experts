# Playbook

## Shrink/swell diagnosis calculation (filled example)

Load ramp 60% → 85%, drum level indicated +4" over 5 minutes, feedwater valve position unchanged.

| Metric | Value |
|---|---|
| Steam flow (current) | 620,000 lb/hr |
| Feedwater flow (current) | 590,000 lb/hr |
| Deficit | 620,000 − 590,000 = 30,000 lb/hr |
| Deficit as % of steam flow | 30,000 / 620,000 = 4.84% |
| Drum level indicated | +4" (appears to be rising) |
| Actual water inventory trend | Falling — feedwater is under-supplying relative to steam demand |

**Interpretation:** The indicated level rise is inconsistent with the flow balance. A genuine level increase would require feedwater flow to exceed or match steam flow; instead feedwater is 4.84% short. This confirms shrink/swell — increased boiling rate displacing water and inflating the indicated level — masking an actual inventory deficit.

**Correct action:** Increase feedwater flow to at least match the 620,000 lb/hr steam flow, not reduce it. Expect indicated level to settle toward true value once flows balance and the boiling rate stabilizes at 85% load.

## Startup ramp-rate verification (filled example)

Cold startup, drum wall thickness rated for a maximum 100°F/hour heating rate; turbine rotor rated for 150°F/hour.

| Component | Rated max ramp rate | Actual planned ramp rate | Governs? |
|---|---|---|---|
| Drum (thick-walled) | 100°F/hour | — | **Yes — most restrictive** |
| Turbine rotor | 150°F/hour | — | No — less restrictive than drum |
| Superheater header | 120°F/hour | — | No — less restrictive than drum |

**Applied limit:** The startup curve is set to 100°F/hour — the drum's rated limit — even though the turbine rotor and superheater header could tolerate faster heating. Using the turbine's 150°F/hour rate instead would over-stress the drum by 50% relative to its rated limit, with damage that may not surface until a later inspection cycle.

## Water chemistry excursion escalation log (filled example)

| Shift | Dissolved oxygen (ppb) | Limit | Status |
|---|---|---|---|
| Day 1 | 6 ppb | ≤ 7 ppb | Within limit |
| Day 2 | 9 ppb | ≤ 7 ppb | **Excursion — 28.6% over limit** |
| Day 3 | 11 ppb | ≤ 7 ppb | **Excursion — 57.1% over limit, escalating** |

Excursion percentage over limit: Day 2 = (9−7)/7 = 28.6%; Day 3 = (11−7)/7 = 57.1%. Even though no trip has activated on either day, the trend is worsening — escalate to chemistry/engineering staff at Day 2's first excursion rather than waiting for a trip that this parameter will never directly cause; the actual consequence (tube damage) accumulates over the following weeks and months regardless.
