# Playbook

Filled templates for scoping, scoring, and reporting a pentest engagement. Populate the placeholders per engagement; the structure and thresholds are the reusable part.

## Engagement time-allocation table (10/20/50/20 heuristic)

For a 5-day (40-hour) external web-application test:

| Phase | % of budget | Hours | What happens |
|---|---|---|---|
| Scoping & kickoff | 10% | 4h | RoE sign-off, scope confirmation call, test-account provisioning |
| Recon & enumeration | 20% | 8h | OSINT, DNS, port/service scan, authenticated + unauthenticated crawl |
| Vulnerability analysis & exploitation | 50% | 20h | Automated scan, manual triage of every candidate finding, PoC building, chaining |
| Reporting | 20% | 8h | Executive summary, per-finding write-ups, evidence packaging, QA pass |

Internal network test with Active Directory (5–10 days depending on host count): shift 5 points from recon to exploitation once initial domain foothold is achieved — AD attack-path discovery (BloodHound) and lateral movement consume more of the exploitation block than web recon does.

## RoE checklist (filled example)

| Field | Example value |
|---|---|
| Client | Acme Fintech Inc. |
| Testing window | 2026-03-10 09:00 UTC – 2026-03-14 18:00 UTC |
| In-scope targets | `app.example.com`, `api.example.com`, IP range 203.0.113.0/28 |
| Explicit exclusions | `payments.thirdpartyprocessor.com` (embedded iframe, not client-owned) |
| Test types authorized | Web app testing, authenticated + unauthenticated, session/token brute-force against **staging replica only** |
| Data-handling clause | No PoC may use real customer records; use seeded test accounts `pentest_user_01`–`pentest_user_10` |
| Emergency contact | Client IR lead, phone + Slack channel, response SLA 30 min |
| Denial-of-service authorization | Not authorized — no load/stress testing, no account-lockout mass-trigger against production |
| Get-out-of-jail letter | Signed by Acme CISO, references this RoE by version + date |

## CVSS v3.1 severity bands (reference)

| Base score range | Severity |
|---|---|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | Critical |

Base score formula (Scope: Unchanged): `ISS = 1 - [(1-C)(1-I)(1-A)]`; `Impact = 6.42 × ISS`; `Exploitability = 8.22 × AV × AC × PR × UI`; `Base = roundup(min(Impact + Exploitability, 10))`. Metric weights: AV — N 0.85 / A 0.62 / L 0.55 / P 0.20; AC — L 0.77 / H 0.44; PR (Unchanged) — N 0.85 / L 0.62 / H 0.27; UI — N 0.85 / R 0.62; C/I/A — H 0.56 / L 0.22 / N 0. Environmental score reweights the same formula with client-declared CR/IR/AR multipliers (0.5 Low / 1.0 Medium / 1.5 High) applied to the corresponding C/I/A component before recomputing Impact.

## Filled finding template

```markdown
### Finding EX-07 — SQL Injection in Login Form (`username` parameter)
**CVSS v3.1:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H — Base 9.8 (Critical)
**Location:** POST https://app.example.com/api/v1/login, parameter `username`
**Confirmed:** Yes — manually reproduced 2026-03-11 14:22 UTC, independent of scanner alert

**Evidence:**
Request:
    POST /api/v1/login HTTP/1.1
    Host: app.example.com
    Content-Type: application/json

    {"username": "admin' OR '1'='1' -- ", "password": "x"}

Response: HTTP 200, returns valid session for the first row in the `users` table
(`pentest_user_01`, not a real customer — table order confirmed via `ORDER BY`
boolean-blind follow-up test, not by touching row content).

**Impact:** Full authentication bypass; any user account is accessible without
credentials by row-position manipulation. Confirmed against the seeded test
table only per RoE data-handling clause — did not enumerate real user rows.

**Remediation:** Parameterized queries / prepared statements on this endpoint.
Do not remediate with input-sanitization regex alone — verify with a second
tester using a different bypass payload before closing.

**Retest date requested:** within 30 days (Critical, per client's PCI DSS 4.0
Requirement 11.4 remediation SLA)
```

## Retest tracker (filled example)

| Finding ID | Severity | Fix committed? | Retest method | Result |
|---|---|---|---|---|
| EX-07 (SQLi) | Critical | Yes — parameterized query, commit `a1b2c3d` | Re-run original PoC payload + 2 alternate bypass payloads | Closed — no longer reproducible |
| EX-03 (session prediction chain) | High (env. 8.1) | Partial — WAF rule added, token generator unchanged | Checked token generation source, not just WAF response | **Reopened** — underlying CSPRNG fix not shipped; WAF rule bypassed via alternate encoding |
| EX-11 (verbose error header) | Medium | Yes — header stripped in reverse proxy config | Confirmed header absent across 10 sampled error responses | Closed |

## Recon command reference (filled example)

```sh
# Service/version enumeration, scope-limited to the signed RoE range
nmap -sV -p- -T4 203.0.113.0/28 -oA acme_ext_recon

# Authenticated crawl seeded from client-provided route list, reconciled
# against Burp's passive crawl (47 discovered vs. 51 in client's OpenAPI spec
# — the 4-endpoint gap gets a written follow-up question, not an assumption)
```
