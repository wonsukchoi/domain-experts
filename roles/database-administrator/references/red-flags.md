# Red Flags

Smell tests for replication, query performance, migrations, and backups. Format per flag: what it usually means, the first question to ask, the data to pull.

### Replica lag over 30 seconds and climbing

- **Usually means:** apply throughput on the replica can't keep up with the primary's current write rate — a bulk load, a burst of updates, or the replica itself I/O-starved by a competing job (backup, report query). Second most likely: a single large transaction on the primary that hasn't committed yet, so the replica is waiting on WAL it hasn't received.
- **First question:** "What changed on the write side in the last 15 minutes — deploy, batch job, migration — and is lag growing linearly or did it jump?"
- **Data to pull:** `pg_stat_replication.replay_lag` (or `SHOW SLAVE STATUS` seconds_behind_master) trended over the last hour, plus primary write throughput (`pg_stat_database.tup_inserted/updated/deleted` delta) over the same window.

### `n_dead_tup` over 20% of `n_live_tup` on a table over 10M rows

- **Usually means:** autovacuum is falling behind — commonly a long-running transaction holding back the xmin horizon, or `autovacuum_vacuum_cost_limit`/`cost_delay` throttling it during a period of competing I/O demand.
- **First question:** "Is there an open transaction older than an hour anywhere in `pg_stat_activity`, and is autovacuum currently running on this table or was it recently canceled?"
- **Data to pull:** `pg_stat_activity` sorted by `xact_start` ascending; `pg_stat_user_tables.last_autovacuum` and `autovacuum_count` for the table; `age(relfrozenxid)` to check wraparound distance.

### Query planner chooses a sequential scan over an index you expect it to use

- **Usually means:** stale table statistics (row-count or selectivity estimate off by 5x+) most often; index or table bloat second; a misconfigured `random_page_cost` left at the spinning-disk default (4.0) on SSD-backed storage third.
- **First question:** "When did `ANALYZE` last run on this table, and does the estimated row count in `EXPLAIN` match reality?"
- **Data to pull:** `EXPLAIN (ANALYZE, BUFFERS)` output compared estimated vs. actual rows; `pg_stat_user_tables.last_analyze`/`last_autoanalyze`; current `random_page_cost` setting.

### Index or table bloat over 30% (via `pgstattuple` or `pg_stattuple` leaf/page density)

- **Usually means:** a large delete or update batch without a corresponding vacuum/reindex cycle, or an update-heavy table whose fill factor is too high for the churn rate.
- **First question:** "Was there a bulk delete or update in the window before this bloat appeared, and did autovacuum run to completion afterward?"
- **Data to pull:** `pgstattuple('table_or_index_name')` for actual vs. minimal size; `pg_stat_user_tables` dead-tuple history around the suspected event.

### Connection count pinned at `max_connections` with the app reporting pool-wait timeouts

- **Usually means:** the pool is undersized for current concurrency, or a leak — connections checked out and never returned, often from an unhandled exception path that skips the `finally`/`close`.
- **First question:** "Are the connections actually executing queries, or sitting idle-in-transaction?"
- **Data to pull:** `pg_stat_activity` grouped by `state` (`active` vs `idle in transaction` vs `idle`); application-side pool metrics (checked-out count vs. pool max).

### `idle in transaction` sessions older than a few minutes

- **Usually means:** application code opened a transaction and is now waiting on something else (an external API call, a lock, a slow downstream step) before committing — holding row locks and blocking vacuum's xmin horizon the whole time.
- **First question:** "What query or code path opened this transaction, and what is it waiting on right now?"
- **Data to pull:** `pg_stat_activity` filtered to `state = 'idle in transaction'`, sorted by `xact_start`; application logs/traces correlated to the session's backend PID.

### Transaction ID age (`age(datfrozenxid)`) approaching 1.5–2 billion

- **Usually means:** autovacuum has been unable to freeze old transaction IDs across the database fast enough, most often due to `autovacuum_freeze_max_age` never being reached because vacuum keeps getting canceled or starved — heading toward forced read-only mode at wraparound.
- **First question:** "Is there a table where autovacuum has never completed a full vacuum, and is a long-held replication slot or prepared transaction holding the horizon back?"
- **Data to pull:** `SELECT datname, age(datfrozenxid) FROM pg_database ORDER BY 2 DESC;`; check for orphaned replication slots (`pg_replication_slots`) or abandoned prepared transactions (`pg_prepared_xacts`).

### A backup job reporting green for months with no restore ever tested

- **Usually means:** the archive process is "succeeding" at the step that's easy to check (job exit code) while silently failing at the step that matters (a restorable, complete, consistent archive) — a missing WAL segment, a corrupted base backup, or a retention policy that already deleted the segment a stated RPO would need.
- **First question:** "When was the last time anyone actually restored from this backup to a fresh instance and verified row counts?"
- **Data to pull:** backup tool's own verification log (e.g., `pgbackrest info`) plus the date of the last completed restore drill.

### A migration PR contains a single `ALTER TABLE ... ADD COLUMN ... DEFAULT <non-constant>` or unindexed `NOT NULL` add on a table over a few million rows

- **Usually means:** the author tested against a small dev database where the rewrite/scan is instant, and doesn't know the same statement takes an `ACCESS EXCLUSIVE` lock for the full table-rewrite duration in production.
- **First question:** "What's the row count on this table in production, and has this exact migration been run against a copy of that size?"
- **Data to pull:** production row count for the target table; the migration tool's generated SQL (not just the ORM migration file) to confirm it isn't silently doing a blocking rewrite.
