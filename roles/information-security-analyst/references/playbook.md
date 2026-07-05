# Incident response and vulnerability-management playbook — filled templates

Working structures an agent can populate directly. Context throughout: Meridian SaaS, ~1,200 employees, the phishing → MFA-push-bombing → lateral-movement incident from the SKILL.md worked example (Incident 2026-0309), plus the quarterly program-tracking artifacts that sit around any single incident.

## 1. Incident response runbook (NIST SP 800-61 lifecycle, filled)

| Phase | Step | Target SLA (critical severity) | This incident |
|---|---|---|---|
| Detection & analysis | Triage alert to true/false positive | 15 min | 27 min (02:14–02:41) |
| Detection & analysis | Declare IR, page on-call lead | 15 min from confirmed TP | 14 min (02:41–02:55) |
| Containment | Isolate affected host(s) from network | 60 min from IR declaration | 70 min (02:55–04:05) |
| Containment | Kill active attacker session(s), disable compromised account(s) | Concurrent with isolation | 04:05–05:20 |
| Containment | Complete scoping via EDR/netflow across all endpoints | 4 hrs from IR declaration | 3h35m (02:55–06:30) |
| Eradication | Rotate every credential the compromised account/host touched | 12 hrs from IR declaration | 9h05m (02:55–12:00) |
| Eradication | Patch the exploited vulnerability | 12 hrs from IR declaration (critical) | Same window — DC patched by 12:00 |
| Recovery | Return hosts to production on fresh clean baseline, not a timer | Verification-gated, no fixed target | Pending 72-hr monitoring window |
| Post-incident | Lessons-learned review with named control-gap backlog items | 10 business days | Scheduled Mon following week |

**Rule:** a phase is not marked complete on "action taken" — containment closes on confirmed session/account kill plus scoping evidence, eradication closes on confirmed credential rotation plus vulnerability patch, recovery closes on a clean re-baseline, not elapsed time.

## 2. CVSS severity → patch SLA tier

| CVSS base score | Severity | Patch SLA (internal-only asset) | Patch SLA (internet-facing or Tier-0-adjacent) |
|---|---|---|---|
| 9.0–10.0 | Critical | 15 days | 7 days |
| 7.0–8.9 | High | 30 days | 15 days |
| 4.0–6.9 | Medium | 90 days | 45 days |
| 0.1–3.9 | Low | 180 days | 90 days |

**Rule:** internet-facing or Tier-0-adjacent assets move up one exposure tier from their base-score SLA regardless of the number — a High-severity vuln on the domain controller gets the Critical-internal timeline (15 days), not its base-score timeline (30 days). The Incident 2026-0309 DC vulnerability was CVSS 10.0 on a Tier-0 asset: SLA was 7 days from the exposure-adjusted table; it patched at day 47 — **40 days past the applicable SLA**, not the 32 days you'd get using the base internal-only table.

## 3. Detection rule tuning cadence (quarterly, false-positive-rate driven)

| Scenario | Alerts/quarter | Confirmed TPs | FP rate | Action |
|---|---|---|---|---|
| Impossible travel (geo-velocity) | 1,142 | 30 | 97.4% | Retune threshold (raise velocity floor, add device-trust signal) — do NOT set to log-only; technique maps to initial-access/credential-theft, a high-severity category |
| MFA push accepted after >5 prompts in <10 min | 62 | 41 | 33.9% | Keep as-is — FP rate acceptable for the severity of what it catches (push-bombing) |
| Anomalous LSASS access (credential dumping) | 18 | 15 | 16.7% | Keep as-is, lower detection-window threshold from 3 occurrences/6hrs to 2 occurrences/6hrs given low FP rate and high severity |
| Dormant service-account login | 210 | 2 | 99.0% | Retire scenario or narrow scope to accounts dormant >18 months (currently fires at 6 months, too broad) — this maps to a low-severity category, so retiring is the correct direction |

**Rule:** direction of the retune depends on both the FP rate and the severity of the technique the scenario detects. High FP rate + high-severity technique → retune the threshold, keep it live. High FP rate + low-severity technique → retire or narrow. Never resolve a high-FP-rate, high-severity scenario by silencing it — that's what happened to the impossible-travel rule before this incident.

## 4. MTTD / MTTR quarterly tracking (by technique category)

| Technique category (ATT&CK tactic) | Incidents this quarter | Median MTTD | Median MTTR | Program SLA target | Status |
|---|---|---|---|---|---|
| Initial access — phishing | 4 | 14h50m | 5h10m | MTTD <8h, MTTR <4h | Off target — MTTD |
| Credential access — dumping/harvesting | 3 | 6h20m | 2h45m | MTTD <8h, MTTR <4h | On target |
| Lateral movement — SMB/RDP admin shares | 2 | 9h05m | 3h30m | MTTD <8h, MTTR <4h | Off target — MTTD |
| Exploitation of remote services | 1 | 21h55m | 5h35m | MTTD <8h, MTTR <4h | Off target — both |

**Rule:** MTTD/MTTR are reported here as this quarter's median per category, trended against last quarter's, not judged against a single incident. Incident 2026-0309 (MTTD 16h27m, MTTR 4h16m) is one data point feeding the "initial access — phishing" row above, not a standalone verdict on the program.

## 5. ATT&CK coverage map (excerpt — Incident 2026-0309 kill chain)

| Tactic | Technique | Detection control mapped | Fired in this incident? |
|---|---|---|---|
| Initial Access | T1566.002 Spearphishing Link | Email gateway URL sandboxing | No — link passed sandboxing (net-new domain, no reputation history) |
| Credential Access | T1621 MFA Request Generation | Push-count anomaly rule | No — rule exists but threshold was set to >10 prompts/10min; attacker used 11/6min, just under the window boundary |
| Credential Access | T1003.001 LSASS Memory | EDR credential-dumping signature | Yes — fired after 3-occurrence/6-hr threshold, 21:45 |
| Lateral Movement | T1021.002 SMB/Windows Admin Shares | Admin-share connection monitoring | No — monitoring exists for `C$`/`ADMIN$` but wasn't alerting, only logging |
| Exploitation of Remote Services | T1210 (Zerologon-class) | Vulnerability scan + DC exploitation-attempt IDS signature | Partial — IDS signature fired but routed to a queue not actively monitored overnight |

**Rule:** "coverage exists" and "coverage fired in time to matter" are different rows in this table — this incident closed two gaps: (1) the MFA push-threshold boundary (11 prompts got through an >10 rule because it counted a 10-minute rolling window that had already partially elapsed), and (2) the overnight-monitoring gap on the exploitation-attempt IDS queue.

## 6. Variant note — ransomware precursor (encryption-stage IR, where the mechanism differs)

Same phase order (contain → eradicate → recover), but the containment SLA compresses hard: once a host shows mass file-rename/encryption activity, network isolation target drops from the 60-minute phishing-incident SLA to under 10 minutes, because encryption throughput (often >500 files/minute on modern ransomware) makes every additional minute of connectivity a directly countable additional-files-lost number, not a probabilistic risk. Eradication also adds a step absent from the credential-theft path: confirming backup integrity (immutable/offline copy, tested restore) before any recovery decision, since paying or not paying hinges on whether recovery from backup is actually viable, not just theoretically available.
