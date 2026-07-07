# Playbook

Filled runbooks. Populate the bracketed fields; the sequence and thresholds are the reusable part.

## Runbook: metric discrepancy reconciliation

1. **Confirm the exact definitions on both sides** — pull the SQL/logic behind each reported number, not just the labels. "Revenue" with and without refunds, taxes, or a specific date-boundary rule are different metrics wearing the same name.
2. **Check the join grain before assuming missing/duplicate data** — for each join in the query chain, ask "what does one row represent after this join?" If a one-to-many join happens before an aggregation on a column from the "one" side, expect inflation.
3. **Quantify the affected subset** — isolate rows/records where the suspected mechanism applies (e.g. multi-shipment order lines) and confirm the dollar/count delta from just that subset explains the discrepancy, arithmetically, before declaring root cause.
4. **Fix at the query/model layer, not with a dashboard filter patch** — a filter that "corrects" a number without fixing the underlying join reintroduces the bug the next time someone builds on the same table.
5. **Add a regression test** — an automated check (e.g. dbt test) that the metric ties out to the reconciled source within a stated tolerance, run on every refresh, so the same class of bug fails at build time.

## Runbook: dashboard design checklist, by audience

| Audience | Primary need | Design implication |
|---|---|---|
| Executive | Headline number + one-line driver | Minimal filters, no drill-down required to understand the top line; a single "why it moved" annotation |
| Operational (ops/support) | Self-diagnosis of live anomalies | Drill-down to segment/record level, filters exposed, near-real-time freshness if the decision is time-sensitive |
| Analyst/data team | Full reproducibility | Underlying SQL/model reference visible or linked, grain and join logic documented inline |
| Cross-functional planning | Trend + segment decomposition together | Aggregate line shown alongside top-3-by-volume segment breakdown by default, not as an optional drill-down, to catch mix-shift before it misleads |

## Runbook: semantic-layer metric definition template

```
Metric name: [e.g. "Net Revenue"]
Definition (SQL logic, plain English): [e.g. "Sum of order_amount at order-line grain, minus refunds issued within 30 days, excluding test accounts"]
Grain: [what one row of the underlying computation represents]
Source table(s): [fact table(s) and version/model reference]
Included: [what's counted]
Excluded: [what's explicitly not counted, and why]
Freshness SLA: [refresh cadence, e.g. daily by 6am, or near-real-time with X-minute lag]
Reconciliation source of truth: [e.g. Finance's monthly close figure], tolerance: [e.g. within 0.5%]
Owner: [team/person who approves changes to this definition]
Known caveats: [seasonality, one-time adjustments, data source known gaps]
```

## Table: freshness SLA by dashboard type

| Dashboard type | Typical required freshness | Rationale |
|---|---|---|
| Executive/board reporting | Daily (T+1) | Decision cadence is weekly/monthly; real-time adds cost with no decision benefit |
| Planning/forecasting | Daily | Same — planning decisions don't change hour to hour |
| Operational/incident triage | Minutes | Decision (e.g. staffing, incident response) changes within the hour |
| Marketing campaign monitoring | Hourly | Spend/bid decisions can reasonably adjust within-day |
| Ad-hoc analyst exploration | On-demand query, not a scheduled refresh | No standing decision cadence; freshness matched to when the query runs |
