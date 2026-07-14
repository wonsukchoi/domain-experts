# Playbook

## ACE calculation worksheet

Fill with real-time telemetry whenever a deviation alarm fires; recompute every AGC cycle (commonly every 4 seconds) during an active event.

| Field | Value | Notes |
|---|---|---|
| NIS (scheduled net interchange, MW) | +50 | positive = net export |
| NIA (actual net interchange, MW) | −150 | from tie-line metering |
| Interchange deviation (NIA − NIS) | −200 | |
| FS (scheduled frequency, Hz) | 60.00 | |
| FA (actual frequency, Hz) | 59.92 | confirm against 2nd source |
| Frequency deviation (FA − FS) | −0.08 | |
| Frequency bias B (MW/0.1 Hz) | −100 | BA-specific programmed setting |
| Bias term: 10B(FA − FS) | +80 | 10 × (−100) × (−0.08) |
| IME (interchange meter error) | 0 | assume 0 unless a known meter fault |
| **ACE = (NIA−NIS) − 10B(FA−FS) − IME** | **−280** | negative = BA short of obligation |

## Escalation-ladder decision table

Apply in order; do not skip a stage unless the deviation's severity already demands it (e.g., frequency already inside a UFLS band).

| Stage | Trigger | Response | Typical response time |
|---|---|---|---|
| 1. AGC / regulation | ACE outside normal control band | AGC automatically adjusts regulating units | Seconds to ~4 sec cycle |
| 2. Spinning reserve | ACE not closing via AGC alone, or a contingency has occurred | Dispatch online synchronized reserve capacity | Minutes (typically within 10) |
| 3. Fast-start / non-spin capacity | Spinning reserve deployed and needs restoring, or event exceeds spinning reserve capacity | Commit quick-start units (CTs, hydro) | ~10 min typical CT start |
| 4. Emergency energy purchase / import | Internal capacity insufficient | Request emergency assistance from neighboring BAs / RC | 10-30 min depending on agreements |
| 5. Voluntary load curtailment | Emergency assistance insufficient or unavailable | Activate demand response / interruptible load programs | Minutes to tens of minutes |
| 6. Automatic UFLS (last resort) | Frequency reaches PRC-006 staged thresholds (commonly ~59.5, 59.3, 58.9 Hz) | Automatic protective relay action sheds firm load | Sub-second, automatic |

## Reserve-restoration timing checklist (post-contingency)

1. **T+0:** Contingency occurs (e.g., largest single generator trips). Confirm event via a second telemetry source before logging.
2. **T+0 to T+15 min:** AGC and spinning reserve work to return ACE to zero — this window is bounded by NERC BAL-002's Disturbance Control Standard for a Reportable Balancing Contingency Event.
3. **Immediately after ACE recovery:** check current spinning reserve against the N-1 (Most Severe Single Contingency) requirement. If below, treat the system as *not yet N-1 secure*, regardless of ACE status.
4. **If reserve is short:** commit fast-start capacity sized to close the gap; track its scheduled start time against actual synchronization time.
5. **Once fast-start capacity reaches full output:** recheck reserve total against the N-1 requirement. Only then log the event as fully resolved.
6. **File required reports:** any event meeting the Reportable Balancing Contingency Event threshold gets logged per the applicable NERC/regional reporting procedure, independent of whether load shed occurred.

## Voltage/VAR triage table

| Symptom | Likely cause | First response |
|---|---|---|
| Voltage <95% nominal, real power flow steady | Reactive support shortfall (capacitor bank offline, generator AVR at limit) | Switch in additional capacitor banks; raise generator VAR setpoints within limits |
| Voltage declining as real power flow rises on same path | Approaching voltage-stability limit on a reactance-dominated corridor | Reduce or reroute real power transfer on that path while adding reactive support — do not push more MW through it |
| Voltage normal, but VAR reserve near zero across multiple sources | Latent risk — system is one contingency away from a voltage problem | Treat as a reserve-margin issue: bring additional reactive sources online proactively before the next contingency |
