# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual operating-limits checklist, staffing forecast, or contingency plan — not for general reasoning (that's `SKILL.md`).

## Ride/attraction operating-limits checklist

```
Attraction: [name]                    Inspection current through: [date]

Certified operating parameters (from manufacturer manual + current inspection):
  Wind speed (sustained): max [X] mph
  Wind speed (gust): max [X] mph
  Temperature range: [min]-[max] °F
  Rider restrictions: height [min-max], weight [max], health restrictions [list]
  Water/precipitation restriction: [e.g., no operation during active lightning within N miles]

Monitoring plan for today:
  Forecast conditions: [today's forecast vs. limits]
  Monitoring interval: every [15] min once conditions reach [80%] of limit
  Shutdown trigger: sustained reading at or above [X mph / condition]
  Resume criteria: [N consecutive readings] back within limit

Decision log (fill during operation):
  Time | Reading | Action | Staff initials
  ---- | ------- | ------ | --------------
```

## Rolling staffing forecast (weekly, refreshed 3-5 days out)

```
Day: Saturday [date]
Baseline (same-day-of-week trailing avg attendance): 5,100
Adjustments:
  + Holiday/event factor: +2,400 (holiday weekend, historical +45-50% factor)
  + Advance ticket sales signal: 8,200 sold vs. typical 4,800 at this lead time (+71%)
  Weather adjustment: forecast wind event afternoon — may suppress late-day walk-up, -300 (partial offset)

Forecast attendance: ~8,200 (using advance sales as primary signal, weather as secondary adjustment)

Staffing plan (vs. standard Saturday baseline):
  Ride operations: +3 FTE (queue management, coaster area supervision)
  Food/retail: +5 FTE (based on secondary spend per capita × forecast attendance)
  Guest services/first aid: +2 FTE
  Supervisory: +2 (specifically flagged for high-demand attraction crowd management)
```

## Peak-window contingency activation plan

```
Trigger: advance sales >X% above typical for the day-of-week, OR forecast weather event during a
top-decile revenue day

Activation checklist:
  [ ] Indoor/covered attraction capacity confirmed open and staffed
  [ ] Extended hours confirmed on weather-unaffected attractions
  [ ] Virtual queue rebooking policy communicated to guests holding reservations for
      weather-sensitive attractions
  [ ] Additional supervisory staff assigned to highest-demand attraction queue areas
  [ ] Guest communication (app push, signage) prepared in advance for possible hold/resume messaging

Revenue-at-risk estimate: [forecast attendance] × [avg per-cap spend] × [% of day potentially
affected by weather window] = $[estimate] — this sizes how much contingency investment is
justified for this specific day vs. a typical day.
```
