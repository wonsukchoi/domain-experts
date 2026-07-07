# Artifacts

Filled templates for the technical baseline. Populate the bracketed fields with program-specific values; the structure and thresholds are the reusable part.

## Interface control document (ICD) skeleton

```
ICD-<subsystem-A>-<subsystem-B>-<sequence>
Revision: <rev letter>          Baseline date: <YYYY-MM-DD>
Owners: <team A lead> / <team B lead>

Interface type: [data | power | mechanical | timing]
Physical layer: <connector, protocol, voltage/current, or bus spec>
Logical layer: <message format, field-by-field, byte order, units>
Timing: <update rate, max latency, jitter tolerance>
Fault behavior: <what each side does on loss-of-signal, malformed message, out-of-range value>

Change control: any edit requires sign-off from both subsystem owners
  and a re-run of affected VCRM lines (see below).
```

Example filled row (comms subsystem to mission data recorder):

| Field | Value |
|---|---|
| Physical layer | RS-422, differential, 5V, 4-wire |
| Logical layer | 64-byte packet, header (4B sync + 2B length) + payload + 2B CRC-16 |
| Timing | 40 Mbps sustained, max 12ms latency at 95th percentile, jitter < 2ms |
| Fault behavior | Recorder holds last-known-good frame for 3 missed packets, then flags CRITICAL-COMMS-LOSS |

## N² interface matrix (4-subsystem example)

Rows = source, columns = destination. Cell = interface type, or blank if none.

| | Antenna Ctrl | SDR Front End | Mission Data Rec | Power Dist |
|---|---|---|---|---|
| **Antenna Ctrl** | — | timing (10Hz sync) | — | power (28V) |
| **SDR Front End** | pointing cmd (data) | — | data (40Mbps) | power (28V) |
| **Mission Data Rec** | — | ack/nak (data) | — | power (28V) |
| **Power Dist** | telemetry (data) | telemetry (data) | telemetry (data) | — |

9 populated cells out of 12 possible (N=4, N×(N-1)=12) — each populated cell needs its own ICD or an ICD section.

## Verification cross-reference matrix (VCRM)

| Req ID | Requirement (abbreviated) | Verification method | Evidence artifact | Status |
|---|---|---|---|---|
| SYS-014 | Comms link sustains 40Mbps at ≤12ms latency (p95) | Test | Bench test report TR-0091 | Pass |
| SYS-015 | Comms link recovers from 3-packet loss within 500ms | Test | Bench test report TR-0092 | Pass |
| SYS-022 | SDR front end operates -20°C to +55°C | Analysis (thermal model) | Thermal analysis TA-0034 | Pass |
| SYS-031 | System MTBF ≥ 8,000 hours | Analysis (reliability prediction) | Reliability report RR-0012 | Open — awaiting vendor FIT data |
| SYS-044 | ICD-SDR-014 fault behavior matches spec | Demonstration | Integration test log IT-0201 | Pass |

Every row needs a method (test/analysis/demonstration/inspection) before the requirement is baselined — a blank method column is the signal a requirement isn't ready.

## Technical performance measure (TPM) tracking table

| TPM | Allocated budget | Current estimate | Margin | Trend (last 3 reviews) |
|---|---|---|---|---|
| SDR module mass | 1.8 kg | 1.65 kg | 8.3% | Stable |
| End-to-end latency | 15 ms | 13.8 ms | 8.0% | Improving |
| Power draw (SDR + antenna ctrl) | 45 W | 42.1 W | 6.4% | **Below 10% floor — escalate** |
| Recorder storage margin | 20% | 24% | +4pp above target | Stable |

Power draw crossing below the 10% margin floor with 7 months of design work remaining triggers a design review per the decision framework, not a wait for the next scheduled milestone.

## Build-vs-buy total-cost worksheet

```
Option: <COTS component name>
  Unit cost:                          $______
  Adapter/wrapper engineering:        $______  (engineer-weeks × loaded rate)
  Adapter verification (new VCRM lines): $______
  Vendor EOL redesign risk (probability-weighted): $______
  TOTAL INTEGRATION COST:             $______

Option: <in-house build>
  Engineering cost:                   $______
  Adapter needed?                     [Y/N — if Y, add cost]
  EOL/support risk:                   $______ (usually $0 if team retains ownership)
  TOTAL INTEGRATION COST:             $______

Delta: $______
Overriding non-cost factors (schedule risk, single point of failure, program risk plan thresholds): ______
Decision: ______
```

Fill the worksheet before the trade study memo is written — the memo quotes this worksheet's bottom line, not the other way around.
