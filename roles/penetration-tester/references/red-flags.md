# Red Flags

Smell tests for scoping documents, scanner output, findings, and retests. Format per flag: what it usually means, the first question to ask, the data to pull.

### Zero findings on a first external web-app pentest of a production system

- **Usually means:** the scope was too narrow (only marketing pages tested, API/auth flows excluded) or manual testing hours got cut mid-engagement — production apps essentially never come back clean on a genuine first assessment.
- **First question:** "What percentage of the in-scope URL count came from crawler discovery vs. the client-provided route list or OpenAPI spec?"
- **Data to pull:** Burp/ZAP crawl request count vs. total endpoints in the app's own route inventory.

### Every finding's CVSS score matches the scanner's raw output exactly

- **Usually means:** no manual triage occurred; base scores were never adjusted for environmental context, so a Critical on an internal dev endpoint reads at the same severity as one on the internet-facing login page.
- **First question:** "Which findings had their CVSS environmental score recalculated for this client's Confidentiality/Integrity/Availability requirements?"
- **Data to pull:** the CVSS vector strings for the top 5 findings — check whether AV, S, or CR/IR/AR components were ever touched from scanner defaults.

### Session-token entropy below 64 bits per Burp Sequencer (or equivalent)

- **Usually means:** the token is built from a timestamp, sequential counter, or weakly seeded PRNG rather than a CSPRNG; the effective keyspace is brute-forceable inside the session's idle-timeout window.
- **First question:** "At the request rate this environment can sustain, how long does exhausting the effective keyspace take, and is that shorter than the configured idle timeout?"
- **Data to pull:** Sequencer's character-level entropy output plus the app's configured session idle-timeout value.

### No account lockout after 50+ failed logins from the same source

- **Usually means:** no rate limiting or lockout policy exists on the auth endpoint; teams often assume the WAF "catches it," but WAF per-IP throttles commonly sit at 1,000+ requests/minute — far above what an account-lockout policy should allow.
- **First question:** "What's the WAF's actual per-IP throttle threshold, and does it trigger before or after the account-lockout policy should have?"
- **Data to pull:** WAF rule configuration and the server-side login-attempt log for the same test window.

### Retest confirms "fixed" but only a WAF/compensating control was added

- **Usually means:** the underlying code defect (unparameterized query, missing auth check, weak token generator) is unpatched; the compensating control is bypassable by any request that evades its signature (encoding, chunking, alternate parameter).
- **First question:** "Does the fix live in the application code or config, or only in a network control in front of it?"
- **Data to pull:** the commit/config diff tied to the remediation ticket, not just the retest's blocked response.

### A finding's sole evidence is the scanner's description text, no request/response pair

- **Usually means:** the tester never manually reproduced it — plausibly one of the 15–45% of DAST findings documented not to survive manual verification.
- **First question:** "Can you reproduce this with a raw HTTP request right now, live, on this call?"
- **Data to pull:** the original scanner alert ID cross-referenced against the manual-verification log or checklist.

### Scope document has no explicit exclusions for third-party/SaaS-embedded components

- **Usually means:** the engagement risks testing a payment iframe, SSO provider, or analytics widget the client doesn't own or control — a common way testing accidentally reaches (and potentially disrupts) a vendor's production system without that vendor's consent.
- **First question:** "For every domain the app loads a resource from, who owns it, and is it explicitly in or out of scope?"
- **Data to pull:** the full third-party domain list from a HAR capture of the app's main flows, checked against the signed RoE's scope table.

### More than 30% of a report's findings are Informational or Low severity

- **Usually means:** either the app's posture is unusually strong (rare on a first test) or low-value findings are padding the count to justify billed hours.
- **First question:** "Of the informational findings, how many would a developer act on without being explicitly told to?"
- **Data to pull:** finding count by severity tier, compared against logged hours by phase (recon vs. exploitation vs. report-writing).

### Critical/High findings with no fix-by date or retest scheduled

- **Usually means:** the report will join the pile of PDFs nobody actions. Most compliance regimes (e.g. PCI DSS 4.0 Requirement 11.4) expect a remediation timeline — commonly 30 days for Critical/High, up to 90 for Medium — with a booked retest, not just a document handoff.
- **First question:** "Who owns each Critical/High finding, and what date is the retest booked for?"
- **Data to pull:** the remediation ticket linked from each finding and the retest calendar invite.

### The engagement's PoC touches a real customer record instead of a seeded test account

- **Usually means:** the RoE's data-handling clause was unclear or ignored, creating real privacy/breach-notification exposure from the test itself, independent of the target's own vulnerabilities.
- **First question:** "Was this PoC run against a seeded test account, or did it touch a real customer record?"
- **Data to pull:** the specific account IDs referenced in the PoC evidence, checked against the client's test-account allowlist.

### Three or more individually Medium findings share a single attack surface but are reported as unrelated

- **Usually means:** the tester ran the scan and triaged each finding in isolation without asking whether they compose — the report undersells an actual high-impact chain as noise.
- **First question:** "If an attacker had all three of these simultaneously, what could they do that none of them allow alone?"
- **Data to pull:** the endpoint/parameter list for each Medium finding, checked for overlap in the same authentication or session flow.
