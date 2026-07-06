# Data Engineer — Playbook

## Event-time vs. processing-time correction (filled example)

| Metric | Processing-time based (incorrect) | Event-time based (corrected) |
|---|---|---|
| March 14 revenue | $780,000 | $825,000 (+$45,000 reattributed) |
| March 15 revenue | $810,000 | $765,000 (−$45,000 removed) |
| **Day-over-day trend** | **+$30,000 (+3.8%)** | **−$60,000 (−7.3%)** |

**Use:** Always check whether a reported trend holds up under event-time reattribution before trusting it — a processing-time artifact can produce not just a slightly different number, but the opposite conclusion about business direction.

## Idempotency bug and fix (filled example)

| Step | Value |
|---|---|
| Initial fix (incorrect): appended $45,000 correction as a new row | March 14 total: $780,000 + $45,000 = $825,000 (correct, this time) |
| Pipeline retried automatically the next night | Appended the same $45,000 again |
| **Resulting double-counted total** | $825,000 + $45,000 = **$870,000 (incorrect)** |
| **Fix: switched to idempotent upsert-by-date-key** | Retries now recompute and overwrite the same correct total every time |

**Use:** Any correction or backfill operation needs to be idempotent from the start — an append-based fix that happens to produce the right number once will corrupt data on the very next retry.

## Idempotency test checklist

1. Run the pipeline once against a test dataset and record the output.
2. Run the exact same pipeline again against the same input, without clearing prior output.
3. Confirm the output after the second run is identical to the output after the first run.
4. If the output changed (grew, duplicated, or shifted), the operation is not idempotent — switch to upsert-by-key or full partition overwrite.

## Data quality check matrix (illustrative structure)

| Check type | What it catches | Example threshold |
|---|---|---|
| Completeness | Missing/dropped records | Row count within ±5% of expected daily volume |
| Uniqueness | Duplicate records | Zero duplicate primary keys per partition |
| Freshness | Stale/delayed pipeline runs | Data updated within 2 hours of expected SLA |
| Distribution | Anomalous value patterns | Key metric within historical ±3 standard deviations |

**Use:** Implement checks like these at each pipeline stage, not just at final output — catching a completeness or freshness failure at the source stage is far cheaper than discovering it after it's propagated through several downstream transformations.

## Schema compatibility validation checklist

1. Identify the proposed schema change (field addition, removal, rename, type change).
2. Check whether the change is additive-only (generally safe) or removes/renames/retypes an existing field (generally breaking).
3. Validate the change against the schema registry's compatibility mode before allowing it to publish.
4. If the change is breaking, coordinate a migration plan with downstream consumers before deploying.

## Findings and remediation memo — filled example

> **Revenue Pipeline Data Quality Finding — March 14-15**
> Issue 1 (event-time vs. processing-time): $45,000 in orders placed late on March 14 were misattributed to March 15 due to processing-time partitioning. Corrected: March 14 = $825,000 (was $780,000), March 15 = $765,000 (was $810,000) — **actual trend is a 7.3% decline, not the originally reported 3.8% growth.**
> Issue 2 (idempotency): The initial fix's re-aggregation appended the corrected $45,000 rather than upserting it, causing a double-count to $870,000 on the next automatic retry.
> **Remediation: Repartitioned pipeline by event time with a 6-hour lateness watermark; corrected the aggregation to use idempotent upsert-by-date-key instead of append, so retries and backfills no longer risk double-counting.**
