# Broadcast Technician Playbook

## Alarm/complaint triage table

Run every incoming signal through this before dispatching anyone. Compliance-clock items always outrank engineering-risk items of equal or lower severity.

| Signal | Class | First action | Escalate to truck roll if |
|---|---|---|---|
| VSWR > 1.5:1, forward power steady | Engineering-risk | Cross-check weather (icing/precip) and a second meter; switch to aux if trending up | Cross-check shows no environmental cause, or VSWR keeps climbing after switch |
| Forward power drop >10% with no VSWR change | Engineering-risk | Check PA stage telemetry (plate V/I) before assuming antenna fault | Telemetry confirms PA-side fault, not a metering glitch |
| EAS decoder misses a Required Weekly Test (RWT) | Compliance-clock | Log the miss with timestamp immediately; do not wait for repair | Always — decoder swap/repair is separate from the log-and-report step, which happens now |
| Tower light outage detected | Compliance-clock | Confirm with a second observation point (webcam, site visit call) then notify per station's FAA-notification procedure | Confirmed outage, regardless of cause |
| Loudness complaint naming a specific spot/segment | Content/quality, becomes compliance-clock once confirmed | Measure the named item's integrated LKFS directly; do not trust its metadata tag | Measured loudness is >2 LU over program average — pull from rotation now, root-cause after |
| Closed-caption dropout reported | Content/quality → compliance-clock (CVAA) | Confirm live on a second monitor/decoder; check if pass-through or encoder-side | Confirmed dropout on more than one downstream monitor |
| Automation "silence detect" alarm (dead air) | Compliance-clock (audience-facing) | Verify on-air monitor immediately; check upstream source before local automation | Confirmed silence — switch to backup source/slate immediately, diagnose after |

## Redundancy-audit checklist (quarterly, or after any real failover event)

1. **List every single-threaded dependency** in the signal chain: primary power feed, STL path, EAS decoder, master-control server, transmitter PA.
2. **For each, confirm a second path exists** (generator + automatic transfer switch, alternate STL frequency/IP path, backup EAS unit, redundant automation server, auxiliary transmitter).
3. **Force a live-traffic failover test on each path**, not a bench test — e.g., actually switch on-air audio/video to the backup STL for a scheduled maintenance window, not just verify it powers up.
4. **Record the failover time** (seconds from trigger to confirmed clean signal on the backup) and compare against the station's own target (commonly under 10 seconds for STL, under limits set by RWT/RMT test cadence for EAS decoders).
5. **Confirm alarms re-arm on the primary** after testing — a backup left "hot" and unmonitored, or a primary returned to service with alarms still silenced from the test, both count as an open finding.
6. **Flag any dependency with no second path** as a finding with a remediation owner and target date — do not close the audit with an unmitigated single point of failure logged as "acceptable risk" without a named sign-off.

Example filled finding:

> **Finding: STL path — single Ku-band link, no terrestrial backup.** Last failover test: never (no backup exists). Remediation: install microwave STL as secondary path, target Q3. Interim mitigation: fiber-based IP contribution as manual fallback, verified working 2026-01-08, failover time ~90 seconds (manual switch, not automatic — flagged as insufficient for live news, acceptable for satellite/syndicated programming only).

## EAS test-log template

Every RWT and RMT gets a log line the moment it runs — not reconstructed after the fact. FCC Part 11 requires the station's own log, independent of the decoder's internal memory.

| Date | Test type | Originator | Received (Y/N) | Retransmitted (Y/N) | Time to retransmit | Notes |
|---|---|---|---|---|---|---|
| 2026-01-07 | RWT | State EAS Primary | Y | Y | 4 min | Normal |
| 2026-01-14 | RWT | State EAS Primary | N | N/A | N/A | Decoder heartbeat lost 13:58–14:22; logged as compliance incident, decoder rebooted, missed test reported to state EAS committee same day |
| 2026-01-19 | RMT | FEMA/National | Y | Y | 3 min | Normal |

A missed test gets reported the day it's discovered — the log entry is the compliance artifact; the decoder repair is a separate, non-urgent maintenance ticket.
