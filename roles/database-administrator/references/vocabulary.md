# Vocabulary

Terms generalists misuse. Format per term: definition, a sentence a practitioner would actually say, the common misuse.

### RPO vs RTO

- **Definition:** Recovery Point Objective is how much data you can afford to lose, measured as a time window before the failure. Recovery Time Objective is how long you can afford to be down while recovering.
- **In use:** "We're quoting a 5-minute RPO and a 30-minute RTO to the customer — that means WAL archiving on a sub-60-second cadence, and a restore path we've timed at under 20 minutes to leave margin."
- **Common misuse:** using "we have backups" as if it answers either question. A nightly-only backup with no continuous WAL archiving has an RPO of up to 24 hours regardless of how fast the restore runs; conflating "backups exist" with "RPO is low" is the single most common gap this role catches.

### Replication lag

- **Definition:** the delay between a write committing on the primary and that write becoming visible on a replica, usually measured in bytes-behind or seconds-behind.
- **In use:** "Lag is climbing linearly with the batch job's write rate, not spiking — that's apply throughput being outpaced, not a network blip."
- **Common misuse:** treating any nonzero lag as a bug to eliminate. Async replication has structural lag by design; the actual question is whether current lag is within the staleness the application (and the humans reading the data) can tolerate, not whether it's zero.

### Isolation level (read committed / repeatable read / serializable)

- **Definition:** the guarantee a database gives about what concurrent transactions can see of each other's uncommitted or concurrently-committing changes.
- **In use:** "Read committed lets this report see a different snapshot per query within the same transaction — if we need one consistent view across all three queries, we need repeatable read, not a client-side workaround."
- **Common misuse:** assuming "transaction" alone implies full isolation from all other activity. Postgres and MySQL both default to read committed, which permits non-repeatable reads within a single transaction — a common source of "the numbers didn't add up" bugs in reports that run multiple queries.

### Index bloat

- **Definition:** wasted space in a B-tree index from deleted or updated rows whose slots haven't been reclaimed and repacked, measured as the gap between actual on-disk size and the minimal size the live data would need.
- **In use:** "Leaf density is 44% — the index is roughly 56% bloat, which is why it's 2.87GB when the data needs about 1.26GB."
- **Common misuse:** assuming `VACUUM` (non-full) reclaims index space back to the OS. Standard vacuum marks space reusable within the table/index but doesn't shrink the file; only `VACUUM FULL`, `REINDEX`, or `pg_repack` return space, and the first of those locks the table.

### Sharding vs. partitioning

- **Definition:** partitioning splits one table into pieces on a single database instance, transparent to most queries. Sharding splits data across separate database instances, requiring the application (or a routing layer) to know which shard holds which row.
- **In use:** "Partitioning by month solves the vacuum and index-bloat problem on this table; we don't need sharding until we're write-bound on a single instance's I/O, which we're not."
- **Common misuse:** reaching for sharding to solve a query-performance or maintenance problem that partitioning (much simpler operationally, no cross-shard query logic) already solves. Sharding is a scaling tool for write throughput and dataset size beyond one instance, not a first-line fix for a slow table.

### Connection pooling (and pool exhaustion)

- **Definition:** reusing a small, bounded set of real database connections across a larger number of application requests, because each Postgres/MySQL connection is a full backend process/thread with real memory and context-switch cost.
- **In use:** "We're not CPU-bound, we're pool-bound — 200 app instances each opening their own pool of 20 means 4,000 attempted connections against a database sized for 100."
- **Common misuse:** sizing each application instance's pool independently without accounting for the total across all instances hitting one database — the database-side `max_connections` limit is shared, not per-app.

### Query plan cost (planner cost units)

- **Definition:** an internal, unitless estimate the query planner computes to compare candidate execution plans — not a measurement of actual time, though `seq_page_cost`/`random_page_cost`/`cpu_tuple_cost` are meant to approximate relative real costs.
- **In use:** "The planner's cost estimate favors the seq scan because `random_page_cost` is still at the spinning-disk default of 4.0 on storage where random and sequential reads cost about the same."
- **Common misuse:** reading a lower total cost number as "guaranteed faster" without checking whether the underlying cost constants match the actual storage — a stale or wrong constant makes the comparison, not just the estimate, wrong.

### Autovacuum (and the freeze horizon)

- **Definition:** the background process that reclaims dead tuples and prevents transaction ID wraparound by "freezing" old row versions so their transaction ID no longer needs comparison against the current counter.
- **In use:** "Age on this database is 1.4 billion — we're past the point of tuning thresholds and into forcing a manual `VACUUM FREEZE` on the oldest tables before we hit the wraparound shutoff."
- **Common misuse:** thinking of autovacuum purely as disk-space hygiene. Missing the freeze deadline doesn't just waste space — Postgres will force the database into read-only mode to protect data integrity once transaction ID age approaches the 2^31 wraparound limit.

### Failover vs. restore

- **Definition:** failover promotes an already-running, already-replicating standby to primary (fast, seconds to low minutes). Restore rebuilds a database from a backup plus WAL/binlog replay (slower, minutes to hours, depending on data volume).
- **In use:** "Our RTO target assumes failover to the standby, not restore-from-backup — if we ever lose both, we're looking at the restore-time number instead, which is an order of magnitude longer."
- **Common misuse:** quoting a failover-time SLA (e.g., under a minute) as the organization's RTO when there's no tested standby for the actual failure scenario in question — a region-wide outage or logical corruption replicated to the standby needs a restore, not a failover.

### Statement timeout vs. lock timeout

- **Definition:** `statement_timeout` bounds how long any single query is allowed to run before being canceled. `lock_timeout` bounds how long a statement will wait to acquire a lock before giving up — a much shorter, distinct setting.
- **In use:** "We set `lock_timeout` to 5 seconds on the app role so a blocked migration or long transaction fails fast and visibly, instead of queuing behind it silently for the full `statement_timeout`."
- **Common misuse:** setting only `statement_timeout` and assuming it also caps how long a query waits for a lock before it even starts executing — a query stuck waiting to acquire a lock hasn't started running yet, so `statement_timeout`'s clock may not be the one that matters.
