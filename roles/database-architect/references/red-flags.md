### A schema is normalized to 3NF (or higher) for a read-heavy analytical workload
- **Usually means:** Query performance may be suffering from expensive joins that a denormalized or star-schema design would avoid, since analytical queries typically favor read speed over write-anomaly protection.
- **First question:** What is the actual read/write ratio for this workload, and does the current normalization level match it, or was it applied by default?
- **Data to pull:** Query logs showing join complexity and frequency, read/write ratio for this dataset.

### A distributed database is deployed without an explicit decision on consistency vs. availability during a partition
- **Usually means:** The system's actual behavior during a network partition is undefined or defaulted, which could produce either unacceptable staleness or unacceptable unavailability depending on the data type.
- **First question:** For this specific data type, has a deliberate choice been made and documented — consistency-favoring or availability-favoring — for partition scenarios?
- **Data to pull:** Database configuration for consistency level/replication mode, documented rationale (or its absence).

### A new index is added without checking query plans or expected write volume impact
- **Usually means:** The index may add write overhead and storage cost without actually speeding up a query pattern that occurs often enough to justify it.
- **First question:** Does an EXPLAIN/query plan analysis show this index would actually be used by a common query pattern, and what's the estimated write overhead?
- **Data to pull:** Query plan analysis for the target query pattern, current write volume on the affected table.

### A shard/partition key was chosen without validating it against the dominant query access pattern
- **Usually means:** The most common query type may require an expensive cross-shard scatter-gather instead of routing to a single shard, and correcting this later requires a costly re-sharding migration.
- **First question:** What percentage of actual production queries would route to a single shard under this key, versus requiring a scatter-gather across all shards?
- **Data to pull:** Query logs showing filter patterns, proposed shard key's alignment with those patterns.

### A small number of keys are known to concentrate a disproportionate share of write volume, with no explicit handling in the sharding scheme
- **Usually means:** These keys likely create hot shards that exceed average per-shard capacity, risking a bottleneck concentrated on a subset of the infrastructure.
- **First question:** What percentage of total write volume do the top N highest-volume keys represent, and is there dedicated capacity or routing to handle that concentration?
- **Data to pull:** Write volume distribution by key, current shard capacity and load per shard.

### A backup strategy relies on nightly (or less frequent) full backups with no discussion of the implied RPO
- **Usually means:** The actual potential data loss window (up to 24 hours or more) may not match what the business can actually tolerate for this dataset.
- **First question:** What is the quantified business impact (cost, customer effect) of losing up to a full day of data for this dataset, and does that match the nightly-backup-implied RPO?
- **Data to pull:** Current backup frequency, any documented business impact analysis for data loss on this dataset.

### A database design decision isn't documented with its underlying tradeoff rationale
- **Usually means:** Future maintainers may not understand why a specific normalization level, shard key, or consistency choice was made, risking an uninformed later change that reintroduces a problem the original design solved.
- **First question:** Is there design documentation explaining what this decision optimized for and what it deliberately sacrificed?
- **Data to pull:** Existing design documentation (or its absence) for the decision in question.

### A single global consistency/availability configuration is applied across all tables or data types in a distributed system
- **Usually means:** Different data types within the same system likely have different actual requirements (a financial transaction vs. a recommendation cache), and a one-size-fits-all configuration may be wrong for at least some of them.
- **First question:** Does every table/data type in this system genuinely have the same consistency-vs-availability requirement, or were some assigned the default without specific consideration?
- **Data to pull:** List of data types/tables and their actual business requirement for consistency vs. availability.
