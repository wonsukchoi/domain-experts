# IT decision artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Total cost of ownership comparison (filled — see Worked example in SKILL.md for full narrative)

| | Tool A (current) | Tool B (proposed switch) | Plugin on Tool A |
|---|---|---|---|
| Annual licensing (800 users) | $364,800 | $326,400 | $364,800 + $2,000 |
| One-time migration cost | — | $85,000 | $8,000 |
| One-time retraining cost | — | $96,000 | ~$0 (no platform change) |
| Total one-time cost | — | $181,000 | $8,000 |
| Annual savings vs. Tool A | — | $38,400/year | −$2,000/year (net cost) |
| Payback period | — | 4.7 years | N/A (feature-only cost) |
| 5-year total cost | $1,824,000 | $1,824,000 − $192,000 + $181,000 = $1,813,000 | $1,824,000 + $8,000 + $10,000 = $1,842,000 |

**Reading it:** Tool B's 5-year total is marginally lower than staying on Tool A, but the plugin route delivers the actually-requested feature for a fraction of the disruption and migration risk — the recommendation in SKILL.md's worked example is the plugin, prioritizing low disruption over a thin, long-payback licensing saving.

## 2. Technical debt register (filled example)

| Item | Age | Estimated remediation cost | Risk if deferred another year | Capacity allocated this quarter |
|---|---|---|---|---|
| Legacy billing system on unsupported framework | 3 years | $180,000 | Vendor support ends in 8 months; unpatched security exposure after that | 1 engineer, 1 quarter (in progress) |
| No automated test coverage on payment reconciliation module | 2 years | $60,000 | Each manual release carries ~15% chance of a reconciliation error requiring manual correction | Not yet allocated — queued for next quarter |
| Deprecated authentication library (EOL in 6 months) | 1 year | $40,000 | Post-EOL, no security patches; forced emergency migration likely | 0.5 engineer, this quarter |

**Rule applied:** each item carries an estimated cost and a specific deferred-risk statement, not just a description — this is what lets debt paydown compete fairly against new feature work for capacity.

## 3. Security risk register entry (filled example)

| Field | Value |
|---|---|
| Finding | Unpatched CVE in internal API gateway, CVSS 7.4 (high) |
| Likelihood | Medium — requires authenticated access, no known public exploit yet |
| Business impact if exploited | High — API gateway sits in front of customer data; estimated cost of a breach in this system: $1.2M (incident response, notification, regulatory exposure) |
| Risk score (likelihood × impact framing) | Medium-high — prioritized above lower-impact criticals in the queue |
| Remediation plan | Patch scheduled in next maintenance window (12 days) |
| Interim mitigation | WAF rule added to block the known exploit pattern in the meantime |
| Accountable owner | CISO — reviewed and logged as accepted-with-mitigation for the 12-day window |

**Rule applied:** the risk-acceptance decision (accept-with-mitigation for 12 days) is explicit, dated, and owned — not silent deferral.

## 4. Disaster recovery investment sizing (filled example)

| System | Downtime cost/hour | RTO | RPO | DR investment level |
|---|---|---|---|---|
| Payment processing | $45,000/hour | 15 minutes | Near-zero (synchronous replication) | High — active-active multi-region |
| Customer-facing web app | $8,000/hour | 2 hours | 15 minutes | Medium — warm standby, automated failover |
| Internal HR portal | $400/hour | 24 hours | 24 hours | Low — nightly backup, manual restore acceptable |

**Rule applied:** DR investment tier follows the actual quantified downtime cost per system — the HR portal doesn't get the payment system's investment level, and vice versa.
