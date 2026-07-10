# Playbook

## Meter-reconciliation investigation (filled example)

Legal department, weekly meter usage under cost code `LGL-4400`.

| Metric | Value |
|---|---|
| Weekly baseline (trailing 8 weeks average) | 40 lbs |
| Actual usage this week | 209 lbs |
| Overage vs. baseline | 209 − 40 = 169 lbs |
| Documented large mailing (case filing, [date]) | 15 lbs |
| Overage remaining after documented mailing | 169 − 15 = 154 lbs |
| Single-day batch (same date) | 22 pieces, avg 7 lbs each = 154 lbs |
| Destination pattern | 6 distinct residential addresses |
| Share of overage explained by the batch | 154 / 169 = 91.1% |

**Investigation steps:**
1. Pull the piece-level meter log by department, date, weight, and destination as soon as usage exceeds baseline by a wide margin.
2. Cross-check against any documented large mailing (litigation filing, mass mailer) for that period.
3. If a gap remains after subtracting documented mailings, group the remainder by date to find concentration.
4. If the remainder concentrates on a single day and routes to residential rather than business addresses, treat it as a personal-mail-abuse pattern, not routine variance.
5. Route findings to the facilities/finance manager with the numbers; do not confront an individual before the department lead is looped in.

## Chain-of-custody log (filled example)

Certified letter, tracking #C-778241, addressed to VP Finance.

| Timestamp | Handoff point | Signature | Notes |
|---|---|---|---|
| 9:14 AM | Received at mailroom dock from carrier | J. Ruiz (clerk) | External carrier scan confirms building delivery |
| 9:20 AM | Logged into internal certified-mail register | J. Ruiz (clerk) | Assigned to Finance floor route |
| 10:05 AM | Handed to floor mail runner | J. Ruiz → M. Patel | Runner signs register on pickup |
| 10:40 AM | Delivered to VP Finance's assistant | M. Patel → R. Chen | Assistant signs register on receipt |

Every row has a named signature, not just a timestamp — a gap at any row is the point where "it never arrived" becomes unresolvable.

## Carrier rate-tier comparison (filled example)

Outgoing package, 4.2 lbs, shipping zone 5.

| Service tier | Rate | Notes |
|---|---|---|
| Priority overnight | $38.50 | Current department default |
| 2-day expedited | $19.75 | Meets the stated delivery need (arrival by Thursday) |
| Ground (5-7 day) | $11.20 | Too slow for this shipment's need-by date |

Since the recipient's need-by date is Thursday and today is Monday, 2-day expedited meets the requirement at $19.75 — $18.75 cheaper than the department's habitual overnight default, with no service-level shortfall. Recommend 2-day expedited unless the sender specifically requires overnight confirmation.
