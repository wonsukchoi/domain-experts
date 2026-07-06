### Normalization (1NF/2NF/3NF)
The process of structuring a relational schema to reduce data redundancy and prevent update anomalies, with successive "normal forms" imposing stricter rules.
**In use:** "This table is at 3NF, which protects write integrity but means our reporting queries need several joins."
**Common misuse:** Treating higher normalization as universally better, without weighing the query-performance cost it imposes on read-heavy workloads.

### Denormalization / star schema
A schema design that intentionally introduces redundancy (duplicating data across tables) to optimize read/query performance, commonly used in analytical/data-warehouse contexts (star schema: a central fact table surrounded by dimension tables).
**In use:** "We denormalized the reporting schema into a star schema to avoid the joins the normalized OLTP schema would require."
**Common misuse:** Applying denormalization to a write-heavy transactional system, reintroducing update anomalies that normalization was designed to prevent.

### CAP theorem
The principle that a distributed data store can't simultaneously guarantee full Consistency and full Availability during a network Partition — it must sacrifice one of the two.
**In use:** "During a partition, this database prioritizes consistency over availability for the orders table."
**Common misuse:** Assuming a single database technology's default CAP tradeoff is automatically correct for every data type in the application, without deciding per data type.

### Sharding / partitioning
Splitting a dataset across multiple database instances (shards) based on a chosen key, to distribute load and storage beyond what a single node can handle.
**In use:** "We're sharding the orders table by a hash of customer_id across 8 shards."
**Common misuse:** Choosing a shard key based on convenience rather than the dominant query pattern, resulting in expensive cross-shard queries for the most common operations.

### Shard key (partition key)
The specific field or hash used to determine which shard a given row of data belongs to.
**In use:** "The shard key is hash(customer_id), which routes 'customer order history' queries to a single shard."
**Common misuse:** Selecting a shard key without validating it against actual query logs, leading to a key that doesn't align with how the data is actually queried in production.

### Hot shard / hot key
A shard or key that receives disproportionately high load relative to others, often due to a small number of high-volume entities concentrating activity.
**In use:** "The top 50 enterprise accounts create a hot-shard risk if they're distributed under the standard sharding scheme without special handling."
**Common misuse:** Assuming a sharding scheme distributes load evenly without checking for known skew in the underlying data (e.g., a small number of accounts generating a large share of total volume).

### Index (database)
A data structure that speeds up specific query patterns (typically lookups or range scans on a column) at the cost of additional storage and write overhead, since every index must be updated on every write to the indexed column.
**In use:** "This index speeds up the customer-lookup query significantly, but it adds overhead to every insert."
**Common misuse:** Adding indexes speculatively to any column that might someday be queried, without validating against actual query plans that the index would be used and is worth its write-cost.

### Query plan (EXPLAIN)
The database engine's chosen execution strategy for a given query, revealing whether it uses available indexes, performs full table scans, or takes another path — used to validate indexing and schema decisions.
**In use:** "EXPLAIN shows this query is doing a full table scan — that's the case for adding an index here."
**Common misuse:** Adding or removing indexes without checking the actual query plan, relying on assumption rather than evidence of how the database engine actually executes the query.

### RPO (Recovery Point Objective)
The maximum acceptable amount of data loss, measured in time, that a system's backup/replication strategy is designed to tolerate.
**In use:** "RPO for this dataset is under 1 minute, using continuous replication rather than nightly backups."
**Common misuse:** Accepting a default backup schedule's implied RPO (e.g., 24 hours for nightly backups) without checking whether it actually matches the business's real tolerance for data loss on this specific dataset.

### RTO (Recovery Time Objective)
The maximum acceptable duration for restoring a system to operation after a failure, measured in time.
**In use:** "RTO for this database is 15 minutes — failover to the standby needs to happen within that window."
**Common misuse:** Setting RTO based on a generic disaster recovery template rather than the actual business cost of downtime for this specific system.

### Write-ahead logging (WAL) / continuous replication
A durability mechanism that logs changes before applying them, enabling point-in-time recovery and continuous streaming replication to a standby with minimal data loss.
**In use:** "WAL streaming replication to a standby gives us sub-minute RPO, versus the 24-hour gap a nightly backup would leave."
**Common misuse:** Relying solely on periodic full backups for a dataset whose actual RPO requirement (based on business impact) demands continuous or near-continuous replication instead.
