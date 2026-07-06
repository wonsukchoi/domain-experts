# Playbook

Filled sequences with real thresholds, not descriptions of what to consider. Deviate consciously and say why.

## 1. Live-table schema migration sequencing

Never a single blocking transaction against a table taking production traffic. The additive-then-backfill-then-constrain sequence, with the lock each step takes:

1. **Add the column nullable, no default.** `ALTER TABLE orders ADD COLUMN fulfillment_zone text;` — metadata-only on Postgres 11+, sub-millisecond `ACCESS EXCLUSIVE` lock. (Pre-11, or any version if a non-null `DEFAULT` is specified on a non-constant, this rewrites the table — check version and clause before running.)
2. **Backfill in batches, not one UPDATE.** `UPDATE orders SET fulfillment_zone = ... WHERE id BETWEEN :lo AND :hi AND fulfillment_zone IS NULL;` in batches of 5,000–20,000 rows with a short sleep (50–200ms) between batches. A single-statement backfill on a 40M-row table holds row locks and generates WAL/binlog volume that can itself cause replica lag; batching keeps each transaction short and replays cheaply downstream.
3. **Add the constraint as `NOT VALID` first.** `ALTER TABLE orders ADD CONSTRAINT fulfillment_zone_not_null CHECK (fulfillment_zone IS NOT NULL) NOT VALID;` takes `ACCESS EXCLUSIVE` but only for the instant of adding the constraint row to the catalog — no scan.
4. **Validate separately.** `ALTER TABLE orders VALIDATE CONSTRAINT fulfillment_zone_not_null;` takes only a `SHARE UPDATE EXCLUSIVE` lock (blocks other DDL, not reads/writes) while it scans to confirm no violations — this is where the actual table scan cost lands, off the write-blocking critical path.
5. **Build any new index `CONCURRENTLY`.** `CREATE INDEX CONCURRENTLY idx_orders_zone ON orders (fulfillment_zone);` takes roughly 2x as long as a blocking build (two table passes) but never blocks writes. If it fails partway (deadlock, unique violation), it leaves an invalid index — drop it (`DROP INDEX CONCURRENTLY`) and retry; don't leave it silently unused.
6. **Only after backfill is 100% and constraint validated, flip application code to rely on the column, then drop any temporary dual-write path.** Sequencing constraint-then-app-cutover the other way around risks the app writing rows the constraint would reject during the deploy window.

**Rollback posture:** each step above is independently reversible (`DROP CONSTRAINT`, `DROP INDEX CONCURRENTLY`, `DROP COLUMN`) except the backfill, which needs a companion down-migration only if the column is read by anything before validation completes.

## 2. Incident triage order (query slow / errors spiking)

Cheapest, most common causes first — most incidents resolve at step 1–3 without touching schema or scaling:

1. **Lock contention.** Query `pg_locks` joined to `pg_stat_activity` for blocked/blocking pairs; MySQL: `SHOW ENGINE INNODB STATUS` for the deadlock/lock-wait section. A single long-running transaction (often an ORM leaving a transaction open, or a forgotten `BEGIN` in a psql session) holding a row lock for minutes explains most "sudden slowness" incidents.
2. **Connection saturation.** Compare active connections to `max_connections` (Postgres default 100) or pool size. If the app-side pool is maxed and requests are queueing for a connection, the database itself may be idle — check pool wait time, not just DB CPU.
3. **Plan regression from stale statistics or bloat.** `EXPLAIN (ANALYZE, BUFFERS)` the slow query; compare estimated vs actual row counts. A gap over ~5x means `ANALYZE` first, investigate bloat (`pgstattuple`) second.
4. **Replication lag feeding stale reads.** If reads are routed to replicas, check lag (`pg_stat_replication.replay_lag` or `SHOW SLAVE STATUS` seconds_behind_master) before assuming the data itself is wrong.
5. **Resource exhaustion (I/O, CPU, disk space).** Only after 1–4 are ruled out: check `iostat`/cloud provider I/O metrics, disk free space (WAL/binlog fill-up can silently halt writes), and whether a competing job (backup, ETL, batch) is consuming I/O bandwidth autovacuum or replication needs.
6. **Write the timeline to the minute** (deploy time, first alert, first mitigation, resolution) — it's the single most useful artifact for both the postmortem and catching recurrence.

## 3. Backup/restore drill and RPO/RTO worksheet

Run quarterly at minimum, and after any storage/version upgrade. A backup strategy is unverified until this has been run against a production-scale snapshot, not a small staging copy.

| Step | Target | Example measured result |
|---|---|---|
| Continuous WAL archiving interval | archive_timeout ≤ 60s | 60s configured, confirmed via `pg_stat_archiver.last_archived_time` |
| RPO (max acceptable data loss) | stated by the business, e.g. 5 min | Measured: last successful WAL push was 42s before simulated failure — within target |
| Base backup cadence | full snapshot daily + continuous WAL | Daily 02:00 UTC via pgBackRest |
| Restore time (RTO) — full restore from base backup + WAL replay | stated target, e.g. ≤60 min | Measured: 38 min to restore 340GB base backup + replay 6h of WAL on equivalent instance class |
| Failover time (if using standby, not restore) | stated target, e.g. ≤2 min | Measured: 47s for RDS Multi-AZ synchronous standby promotion; 2–4 min typical for a manually promoted async replica (DNS/connection-string cutover adds most of the delta) |
| Post-restore verification | row counts + checksums on 3 known tables vs pre-failure snapshot | orders: 41,987,203 rows both sides; checksums matched |

If measured RTO exceeds the stated target, the fix is one of: faster storage for restore, a warm standby instead of restore-from-backup, or renegotiating the target with whoever owns the SLA — not a note in a runbook that "restores may take longer than expected."

## 4. Connection pool and index-count capacity math

**Pool sizing.** Starting formula (HikariCP wiki): `connections = (core_count * 2) + effective_spindle_count`. For an 8-vCPU instance on SSD-backed cloud storage (effective_spindle_count = 1): `(8 * 2) + 1 = 17`, round to 20 real backend connections behind PgBouncer in transaction-pooling mode. Confirm with `pgbench` under realistic concurrency (200+ simulated app connections against the 20 pooled backend connections) before committing — the formula is a starting point, the load test is the answer.

**Index cost on the write path.** Each index adds roughly one extra page write (plus WAL) per row-affecting statement. A table doing 5,000 writes/sec with 6 indexes is generating on the order of 30,000 index-page writes/sec before counting the heap write itself — if p99 write latency is the complaint, count indexes before adding another one to "fix" a read query. Rule of thumb: justify each index against a specific query pattern it serves above a stated frequency (e.g., "runs 200+ times/hour"); drop indexes `pg_stat_user_indexes.idx_scan = 0` after 30 days of representative traffic.
