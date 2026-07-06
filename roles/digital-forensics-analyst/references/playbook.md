# Digital Forensics Analyst — Playbook

## Order of volatility collection sequence

| Order | Evidence type | Notes |
|---|---|---|
| 1 (most volatile) | Registers, cache | Rarely captured outside specialized live-response scenarios |
| 2 | RAM / memory contents | Capture via memory dump tool before any shutdown |
| 3 | Network state (active connections, ARP cache) | Capture while system is live |
| 4 | Running processes | Capture while system is live |
| 5 | Disk contents | Image via write-blocker after volatile evidence is secured |
| 6 | Remote logging / monitoring data | Pull from centralized log sources, SIEM, cloud service logs |
| 7 (least volatile) | Archival media, backups | Least time-sensitive to collect |

**Use:** Never skip ahead to disk imaging or shutdown before capturing everything above it on this list that's still available — each step down this list becomes permanently unrecoverable once the system state changes.

## Chain of custody log (filled example)

| Time | Action | Person | Notes |
|---|---|---|---|
| 9:03 AM | Laptop seized | IT security | Serial number logged, device photographed in place |
| 9:15 AM | Transferred to forensics analyst | Custody signature obtained | |
| 9:20 AM | Memory capture performed | Forensics analyst | 32GB RAM dump |
| 9:45 AM | Disk image created | Forensics analyst | Via write-blocker |
| 9:46 AM | Hash verification | Forensics analyst | Source and image SHA-256 match |
| 10:00 AM | Original secured in evidence locker; image moved to analysis workstation | Forensics analyst | |

**Use:** Every entry needs a timestamp, an action, and a named person — a gap in this table is exactly what an opposing party will target to challenge the evidence's integrity.

## Timeline clock-skew correction (filled example)

| Step | Value |
|---|---|
| Raw system log timestamp (upload event) | 11:47 PM (system clock configured to UTC) |
| Organization's actual timezone | Eastern (UTC−5) |
| **Corrected local time** | 11:47 PM − 5 hours = **6:47 PM** |
| Independent corroborating source (badge access log, already in local time) | Badge-out at 7:30 PM |
| **Result** | 6:47 PM upload precedes 7:30 PM badge-out → **employee was present and directly performed the action** |

**Use:** Always identify each source's actual clock configuration before comparing timestamps across systems — an uncorrected comparison here would have wrongly suggested the upload happened after the employee left.

## Anti-forensic indicator check (filled example)

| Indicator | Finding |
|---|---|
| Local system event log | Gap from 11:40 PM to 11:50 PM UTC (6:40-6:50 PM local), surrounding the upload event |
| External cloud service access log (independent, harder to alter) | Intact, no gap |
| **Interpretation** | Gap in the locally-controlled log, combined with an intact independent log covering the same window, is **consistent with deliberate local log tampering**, not a coincidental logging failure |

**Use:** Always check for an independent corroborating source when a local log shows a suspicious gap — if the independent source is also missing data for the same window, that points to a broader failure rather than deliberate tampering; if it's intact, that strengthens the anti-forensic-activity interpretation.

## Forensic findings memo — filled example

> **Digital Forensics Findings — Case [ref]**
> Evidence imaged via write-blocker; source and image SHA-256 hashes verified as matching. Chain of custody documented from 9:03 AM seizure through analysis.
> Upload event initially appeared at 11:47 PM per system clock (UTC-configured); corrected for the 5-hour UTC/Eastern offset, the actual local time was **6:47 PM**, preceding the employee's 7:30 PM badge-out — confirming direct, in-person action.
> Event log gap identified (11:40-11:50 PM UTC / 6:40-6:50 PM local) surrounding the upload, while the external cloud service's independent access log remained intact — **consistent with deliberate local log tampering.**
> **Finding: The employee directly initiated the file upload while still present in the office, and subsequently attempted to obscure local evidence of the action.**
