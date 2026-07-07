# Public Relations Specialist — Artifacts

## Press release (filled example)

> **FOR IMMEDIATE RELEASE**
>
> **Acme Analytics Launches Native Salesforce Integration, Cutting Setup Time from 6.2 Hours to 40 Minutes**
>
> *New integration eliminates the manual CSV-export workflow that has been the top support request for two years*
>
> SAN FRANCISCO, March 4, 2026 — Acme Analytics today announced a native Salesforce integration, replacing the manual CSV-export process that early customers cited as their top onboarding friction point. In a 30-customer beta, average integration setup time dropped from 6.2 hours to 40 minutes.
>
> "Teams were exporting data by hand every week just to keep dashboards current," said Jane Reyes, VP of Product at Acme Analytics. "This isn't a nice-to-have — it's removing the single biggest reason a pilot didn't convert to a paid plan."
>
> The integration is available today to all Business and Enterprise tier customers at no additional cost. Setup documentation is available at [link].
>
> **About Acme Analytics**
> Acme Analytics provides revenue-reporting software for mid-market B2B companies, serving over 400 customers as of March 2026. Founded in 2019, the company is headquartered in San Francisco. [boilerplate — reused verbatim across releases, updated quarterly for customer count]
>
> **Media Contact:**
> Jordan Lee, PR Specialist
> jordan@acmeanalytics.com | 415-555-0142

## Pitch-tracking table (filled example, one campaign)

| Reporter | Outlet | Beat fit | Angle sent | Sent date | Opened | Replied | Placed |
|---|---|---|---|---|---|---|---|
| M. Chen | SaaS Weekly | High — covers integrations monthly | A (benchmark) | Mar 3 | Yes | Yes | Yes (Mar 10) |
| R. Osei | TechCrunch (B2B) | Medium — broad SaaS beat | A (benchmark) | Mar 3 | Yes | No | No |
| P. Alvarez | Trade Insider | High — weekly integration roundup | B (partnership) | Mar 3 | No | No | No |
| K. Novak | Enterprise Digest | Medium | A (benchmark) | Mar 3 | Yes | Yes | Yes (Mar 11) |
| **Totals (Angle A, n=23)** | | | | | 14 (60.9%) | 5 (21.7%) | 2 (8.7%) |
| **Totals (Angle B, n=22)** | | | | | 9 (40.9%) | 2 (9.1%) | 1 (4.5%) |

## Embargo log (filled example)

| Reporter | Outlet | Embargo granted | Publish time agreed | Confirmed honored? |
|---|---|---|---|---|
| M. Chen | SaaS Weekly | Mar 5, 9:00 AM PT briefing | Mar 10, 6:00 AM PT | Yes — ran at 6:04 AM PT |
| K. Novak | Enterprise Digest | Mar 6, 2:00 PM PT briefing | Mar 11, 8:00 AM PT | Yes — ran at 7:58 AM PT |

Rule applied here: both embargoes were kept to specific reporters with confirmed publish-time commitments, not offered broadly — a broad "everyone gets this at 6 AM Monday" embargo isn't a real trade, it's just an early-access press release with extra steps and no relationship value.

## Crisis holding statement (filled example)

Scenario: a reporter emails at 2:15 PM asking about a customer-reported data-export bug that may have exposed one account's data to another account, with a 5:00 PM deadline before publishing without comment.

**Holding statement sent at 3:05 PM (50 minutes after inquiry, before full facts confirmed):**

> Thank you for flagging this — we take it seriously and are actively investigating right now. What we can confirm as of this message: we identified the issue this morning, it affects a limited, specific configuration, and we've already disabled the affected code path while we complete the investigation. We'll have a fuller statement with specifics by 4:30 PM today, well ahead of your deadline. Happy to get on a call in the meantime if useful.

**Follow-up complete statement sent at 4:20 PM, once facts were confirmed internally:**

> Following up as promised. We've confirmed the issue affected 3 customer accounts over a 6-hour window on March 2, caused by a caching bug introduced in a deploy that morning. No data was retained beyond that window — it was a display-layer issue, not persistent storage. All 3 affected customers were notified directly at 3:45 PM today, before this statement. The code path has been fully reverted and we've added an automated test to catch this class of bug before future deploys.

Note the gap discipline: the 3:05 PM message committed to a specific time (4:30 PM) and beat it by 10 minutes — a missed self-imposed deadline in a live crisis inquiry compounds the credibility problem the holding statement was trying to prevent.
