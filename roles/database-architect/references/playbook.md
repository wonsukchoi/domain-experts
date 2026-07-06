# Database Architect — Playbook

## Sharding key evaluation (filled example)

| Option | Alignment with dominant query (customer order history, 70% of queries) | Write load distribution | Result |
|---|---|---|---|
| A: hash(customer_id) | Strong — single-shard routing for most queries | Uneven — top 50 accounts = 18% of volume, creating hot shards | Fast queries, hot-shard risk |
| B: order_date (time-based) | Weak — requires cross-shard scatter-gather for customer history | Even — writes naturally distributed over time | Even load, slow dominant query |
| **Hybrid (chosen)** | hash(customer_id) for 99%+ of accounts, dedicated shards for top 50 | Balanced via dedicated capacity for hot accounts | **Preserves fast queries AND manages hot-shard risk** |

## Write load calculation (filled example)

| Component | Value |
|---|---|
| Total peak write volume | 8,000 writes/sec |
| Top 50 accounts' share of volume | 18% = 1,440 writes/sec |
| Remaining volume across 6 standard shards | (8,000 − 1,440) ÷ 6 ≈ **1,093 writes/sec per shard** |
| Dedicated shards for top 50 accounts | 2 shards sized for the 1,440 writes/sec load |

**Use:** Always calculate per-shard load after accounting for known skew — an even split assumption (8,000 ÷ 8 = 1,000/shard) would understate the actual load on shards holding high-volume accounts.

## CAP tradeoff assignment table (illustrative structure)

| Data type | Priority during partition | Rationale |
|---|---|---|
| Orders / financial transactions | Consistency | A lost or inconsistent order has real financial/legal consequences |
| Recently viewed products / recommendation cache | Availability | Slightly stale recommendations are acceptable; blocking checkout-adjacent flows is not |
| User session data | Availability | Losing a session briefly is recoverable; blocking login is worse |
| Inventory count (checkout-blocking) | Consistency | Overselling inventory has direct financial and customer-trust cost |

**Use:** Assign this per data type explicitly — don't apply one global consistency/availability setting to every table in a distributed system.

## RPO/RTO derivation worksheet (filled example)

| Component | Value |
|---|---|
| Historical incident: data loss window | Over 5 minutes |
| Resulting cost (support labor + goodwill impact) | ~$50,000/incident |
| **Derived RPO requirement** | Under 1 minute |
| Chosen mechanism | Continuous WAL streaming replication to standby |
| Nightly-backup-only implied RPO (rejected as inadequate) | Up to 24 hours |

**Use:** Always tie the RPO/RTO target back to a quantified business impact figure — a target set without this basis is either arbitrarily strict (over-engineering cost) or arbitrarily loose (real risk exposure).

## Indexing decision checklist

1. Pull the query plan (EXPLAIN) for the target query pattern — does it currently perform a full table scan or an inefficient lookup?
2. Estimate the query pattern's actual frequency in production — is it common enough to justify the index?
3. Estimate the write volume on the affected table/column — how much write overhead would this index add?
4. Add the index only if the read benefit (validated via query plan) outweighs the write and storage cost for this specific table's actual workload.

## Database architecture decision memo — filled example

> **Sharding and Replication Strategy — Orders Database**
> Shard key: hash(customer_id) across 8 shards, with the top 50 high-volume accounts (18% of order volume) pinned to 2 dedicated shards to avoid hot-shard bottlenecks. Remaining shards average ~1,093 writes/sec, within capacity.
> CAP tradeoff: Orders table prioritizes consistency (synchronous replication) over availability during a partition; recommendation cache prioritizes availability (eventual consistency).
> RPO: Under 1 minute via continuous WAL streaming replication, based on a $50,000/incident cost basis for data loss beyond 5 minutes — nightly backup alone is insufficient for this requirement.
> **Rationale documented for future maintainers: dominant query pattern (customer order history) drove shard key choice; known B2B volume concentration required explicit hot-key handling rather than being absorbed into the primary sharding scheme.**
