# Playbook

## Leak-investigation decision worksheet

Fill when a pressure or flow anomaly is detected.

| Field | Value |
|---|---|
| Section | Section 7, Distribution Line B |
| Baseline flow (weather-adjusted) | 1,000 Mcf/day |
| Current flow | 1,180 Mcf/day |
| Flow deviation | +18% |
| Baseline pressure | 50 psig |
| Current pressure | 42 psig |
| Weather explanation? (temp comparison) | No — 68°F today vs. 65°F yesterday, no cold-snap driver |
| Scheduled demand change? | No known industrial ramp-up |
| Conclusion | Anomaly NOT explained by demand/weather → treat as probable leak |
| Action | Dispatch leak survey crew (NOT a compression/setpoint adjustment) |
| Survey result | record actual findings |
| Estimated leak rate (if found) | record actual, reconcile against flow deviation |
| Section isolated? | Y/N and timestamp |

## MAOP pressure-margin table

| Parameter | Value | Notes |
|---|---|---|
| MAOP | 60 psig | Regulatory ceiling |
| Normal operating pressure | 55 psig | ~8% margin below MAOP |
| Action threshold (reduce throughput) | Set well below MAOP, per facility control philosophy | Do not rely on automatic shutdown as sole control |
| Automatic high-pressure shutdown | Per facility design, typically very close to MAOP | Last-resort control, not primary response |

**Rule:** if operating pressure trends toward the action threshold without a deliberate, documented reason (a planned throughput increase), treat it as an anomaly requiring investigation, not a routine condition.

## Odorant multi-point verification checklist

1. Confirm odorant injection rate at the plant/injection skid against the required rate (per 49 CFR 192.625 or applicable state regulation).
2. Verify odorant concentration at intermediate points along the distribution system per the monitoring schedule (not just at injection).
3. Verify odorant concentration at the farthest/most distant monitored points in the system, where odor fade risk is highest.
4. If any point reads below the detectable/required threshold, investigate cause (pipe material/age, distance, temperature effects) and adjust injection rate or monitoring frequency as needed.
5. Document all readings with location, timestamp, and result in the odorization monitoring log.

## Public odor complaint response checklist

1. Log complaint with exact location, time received, and caller-reported details.
2. Dispatch a field crew immediately with combustible gas detection equipment — treat as a potential real leak regardless of initial plausibility.
3. On arrival, take CGI (combustible gas indicator) readings at the reported location and surrounding area, including any confined spaces (basements, meter pits).
4. If gas is detected: follow the facility's emergency response procedure (isolate, evacuate as needed, notify emergency services if warranted by reading magnitude).
5. If no gas detected: document the negative finding, but do not treat the complaint as closed without this field verification step having occurred.
6. Log the complaint's resolution and field findings, regardless of outcome.
