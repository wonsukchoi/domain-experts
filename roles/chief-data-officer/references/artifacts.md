# Artifacts

Filled templates for the three documents a CDO produces most: the metrics catalog entry, the data classification tiering, and the retention/minimization risk assessment.

## Metrics catalog entry (filled example)

```markdown
## Metric: monthly_recurring_revenue (MRR)

**Owner:** Finance Data (data steward: J. Ramos)
**Definition:** Sum of normalized monthly subscription value for all accounts with
an active, non-past-due subscription as of the last day of the calendar month.
Annual plans are normalized by dividing by 12; multi-year plans by total months.
**Source system:** Billing (Stripe subscriptions table, `status = active`)
**Explicitly excludes:** trial accounts, past-due accounts in dunning, one-time
purchases, usage-based overage charges.
**Approved consumers:** board deck, investor reporting, Finance dashboards.
**Not approved for:** Sales pipeline forecasting (use `pipeline_weighted_value`
instead — different metric, different owner).
**Change log:** 2025-11-03 — excluded past-due accounts (previously counted through
day 30 of dunning); prior historical values restated, see ADR-DATA-009.
**Review cadence:** quarterly, or on any billing system schema change.
```

## Data classification tiering (filled example)

| Tier | Criteria | Example datasets | Governance requirements |
|---|---|---|---|
| Tier 1 — Regulated/critical | Feeds board/regulatory reporting, or is PII/financial subject to breach-notification law | Customer PII, payment card data, board-facing revenue metrics | Named owner, documented lineage, access review every 90 days, DPIA on any new collection, encryption at rest + in transit |
| Tier 2 — Business-sensitive | Internal decision-making data, not externally reported, moderate reidentification risk | Product usage analytics, internal salary bands, vendor contract terms | Named owner, access review every 180 days, lineage documented for top 20 tables only |
| Tier 3 — Low-risk internal | No PII, no external reporting dependency, low reconstruction cost if lost | Internal wiki analytics, non-customer-facing A/B test logs | Light governance — owner named at team level, no fixed review cadence |

Rule applied: a dataset's tier is set by its *highest* qualifying criterion, not
an average — a mostly-internal dataset that happens to include one PII column
is Tier 1 for that column, not Tier 2 for the whole table.

## Retention / minimization risk assessment (filled example)

```markdown
# Retention review: marketing_email_click_history

**Current state:** 4.2M rows, retained indefinitely since 2019, includes email
address + click timestamp + device fingerprint.
**Named use case on file:** none documented — originally collected "for future
personalization work" that never shipped.
**Liability exposure:** 4.2M records × estimated $150/record breach-notification +
remediation cost (2023-2024 IBM Cost of a Data Breach Report per-record average,
adjusted for PII+behavioral combination) ≈ $630K plausible exposure, before any
regulatory fine.
**Documented value:** zero — no active consumer of this table in the last 2 quarters
per query-log audit.
**Decision:** purge records older than 13 months (aligned to marketing's own
attribution-window need, the only identified live use case); implement rolling
13-month deletion going forward; require a named use case + retention period
before any future field of this type is collected.
**Owner:** Marketing Data, enforced by automated deletion job, reviewed annually.
```
