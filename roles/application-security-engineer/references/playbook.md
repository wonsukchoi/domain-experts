# Application Security Engineer — Playbook

## Object-level authorization test (filled example)

| Step | Value |
|---|---|
| Endpoint | `GET /api/invoices/{invoice_id}` |
| Authentication check present? | Yes — valid session required |
| Object-level authorization check present? | **No** — invoice.owner_id never compared to session's user_id |
| Test account | user_id 500, legitimately owns 3 invoices |
| Test method | Request invoice_id 1 through 1000 sequentially |
| **Result** | **1,000 different customers' invoice records retrieved** — full IDOR confirmed |
| Estimated total exposure | ~45,000 invoices (based on production ID range) |
| **Fix** | Add explicit check: `invoice.owner_id == session.user_id`, return 403/404 on mismatch |

**Use:** Always test object-level authorization directly with a cross-account request — confirming authentication alone doesn't tell you whether the specific resource-level check exists.

## Dependency vulnerability reachability triage (filled example)

| Finding | CVSS score | Reachable in this codebase? | Real risk | Priority |
|---|---|---|---|---|
| JSON library deserialization vulnerability | 9.8 (Critical) | **No** — only basic parse function used, not the vulnerable method | Near-zero | Lower |
| Regex library ReDoS vulnerability | 5.3 (Medium) | **Yes** — called directly on user-submitted search queries | Real, exploitable | **Higher — fix first** |

**Use:** Always check reachability before setting remediation priority — a high CVSS score on unreachable code should not outrank a lower-scored but directly exploitable finding.

## Threat modeling checklist (STRIDE, at design time)

1. **Spoofing:** Can an attacker impersonate a legitimate user or system component in this design?
2. **Tampering:** Can data be modified in transit or at rest without detection?
3. **Repudiation:** Can a user deny performing an action with no way to prove otherwise?
4. **Information disclosure:** Could this design expose data to users not authorized to see it?
5. **Denial of service:** Can this design be overwhelmed or made unavailable by an attacker?
6. **Elevation of privilege:** Can a lower-privileged user gain higher privileges through this design?

**Use:** Run this checklist during design review, before implementation begins — each category caught here is far cheaper to address than the same flaw found in code review or production.

## SAST/DAST/SCA coverage matrix

| Vulnerability class | SAST | DAST | SCA |
|---|---|---|---|
| Code-pattern issues (e.g., SQL injection pattern) | Strong | Partial | No |
| Runtime/business-logic flaws | Weak | Strong | No |
| Known dependency vulnerabilities | No | No | Strong |
| Access control logic errors | Partial | Partial | No |

**Use:** No single tool covers every row — combine all three, and recognize that access control logic errors (like the IDOR example above) often require manual review since no automated tool reliably catches them alone.

## Context-specific output encoding checklist (per output sink)

1. Identify every context where this untrusted input is output: HTML body, HTML attribute, JavaScript, SQL query, URL parameter, etc.
2. Confirm encoding specific to each context is applied at that sink, not a single generic sanitization applied once upstream.
3. Test each context specifically for injection (e.g., does this value break out of a JavaScript string context even though it's HTML-escaped?).

## Security findings memo — filled example

> **Application Security Review — Invoice API and Dependency Triage**
> **Finding 1 (Critical — confirmed exploitable):** IDOR on `GET /api/invoices/{invoice_id}` — missing object-level authorization allows any authenticated user to retrieve any customer's invoice. Confirmed exposure: ~45,000 invoice records. **Fix: added explicit owner_id verification before returning invoice data.**
> **Finding 2 (dependency triage):** SCA flagged a CVSS 9.8 vulnerability in an unreachable code path (zero real exploitability) and a CVSS 5.3 vulnerability in a directly reachable, user-input-driven code path (real ReDoS risk).
> **Recommendation: Remediate the reachable CVSS 5.3 finding first — CVSS score alone does not determine remediation priority; reachability and exploitability in this specific codebase do.**
