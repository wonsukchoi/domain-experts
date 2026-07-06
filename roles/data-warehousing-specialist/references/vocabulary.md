### Grain
The precise definition of what a single row in a fact table represents — the most fundamental design decision in dimensional modeling, made before any measure or dimension is added.
**In use:** "We can't add a discount measure until we settle the grain — is this one row per order, or one row per order line?"
**Common misuse:** Assumed to be obvious or already settled because a table "looks like" a familiar entity (orders, customers); two people can build against the same table with different unstated grain assumptions.

### Slowly changing dimension (SCD)
A dimension whose attribute values change over time, requiring an explicit decision about whether history is preserved (Type 2), overwritten (Type 1), or partially retained (Type 3).
**In use:** "This is a classic SCD problem — the customer's region changed, and the Q1 report needs to know what it was on the order date, not what it is today."
**Common misuse:** Treated as a single table-wide setting rather than a per-attribute decision; different attributes on the same dimension table often need different SCD types.

### Type 2 SCD
An SCD implementation that inserts a new row with a new surrogate key on every tracked change, using effective/end dates and a current-row flag to preserve full history.
**In use:** "Join on the surrogate key, not the natural key, or you'll lose the Type 2 history and always get the customer's current region."
**Common misuse:** Joined on the natural key (customer_id) instead of the surrogate key, which collapses the historical distinction Type 2 was built to preserve.

### Conformed dimension
A dimension designed so the same business entity resolves to the same key and attribute values regardless of which fact table or source system references it.
**In use:** "Before we build the bus matrix, we need dim_customer conformed — right now Sales and Support each have their own definition of 'active.'"
**Common misuse:** Assumed to be achieved just by using the same table name across fact tables, without actually reconciling differing source-system definitions behind it.

### Bus matrix
A Kimball-methodology planning tool mapping which conformed dimensions apply to which business processes/fact tables across the enterprise.
**In use:** "The bus matrix shows dim_date and dim_customer touching six of our eight fact tables — those two need to be conformed first."
**Common misuse:** Built once as a documentation exercise and never revisited, so it silently drifts out of sync with the actual current set of fact tables and dimensions.

### Surrogate key
A system-generated, meaningless key (typically an integer) used as a dimension table's primary key, distinct from the natural/business key.
**In use:** "The fact table joins on customer_key, the surrogate — that's how we get two rows for the same customer_id under Type 2 without a key collision."
**Common misuse:** Confused with or replaced by the natural key; using the natural key as the join key defeats the purpose of Type 2 history tracking.

### Change data capture (CDC)
A mechanism (log-based, trigger-based, or timestamp-based) for identifying which source records changed since the last extraction, used to drive incremental loads.
**In use:** "We're moving to log-based CDC because the modified_date approach keeps missing updates from the nightly batch job."
**Common misuse:** Assumed to mean any timestamp-filtering approach; log-based CDC and timestamp-column filtering have very different reliability guarantees, especially around updates that don't touch a tracked timestamp column.

### Watermark (in incremental loads)
The stored checkpoint value (typically a timestamp or sequence number) marking the point up to which a source has already been successfully extracted.
**In use:** "The watermark only advances after the load is validated — if we advance it before checking reconciliation, a failed load silently skips those records forever."
**Common misuse:** Advanced immediately after extraction rather than after validation, which can permanently skip records if a load fails partway through processing.

### Star schema
A dimensional model with a central fact table directly joined to denormalized dimension tables, optimized for query simplicity and BI tool performance over storage efficiency.
**In use:** "This reporting layer should be a star schema, not the normalized OLTP structure — analysts need simple joins, not five-table lookups for a product name."
**Common misuse:** Conflated with "any data warehouse structure"; a snowflake schema (normalized dimensions) or a fully normalized OLTP-style model are different design choices with different tradeoffs, not interchangeable synonyms.

### Fan-out (in joins)
The multiplication of fact table rows that occurs when joining to a dimension with a one-to-many or many-to-many relationship without a bridge table, inflating row counts and aggregate measures.
**In use:** "The promotion join is fanning out — that's why SUM(amount) is $2,595 too high even though the row count still looked right at first glance before we checked the aggregate."
**Common misuse:** Missed because row counts can still look plausible; fan-out is caught by checking whether an aggregate measure changes before and after a join, not by eyeballing row counts alone.

### Bridge table
A table resolving a many-to-many relationship between a fact table and a dimension (e.g., orders to promotions) without causing a fan-out join.
**In use:** "Route the promotion relationship through a bridge table with an allocation factor, so the discount amount splits correctly across multiple promotions instead of repeating on each row."
**Common misuse:** Skipped in favor of a direct join "since it's usually one-to-one," which works until a record with multiple relationships appears and silently fans out the aggregate.

### Late-arriving fact/dimension
A record whose business event date is earlier than when it actually arrives in the source system or load pipeline, requiring load logic that doesn't rely solely on business-date filtering.
**In use:** "That order looks like it's from three weeks ago, but it only hit the source system yesterday — the watermark logic needs to catch it on arrival, not business date."
**Common misuse:** Assumed to be rare enough to ignore; in practice, batch-processed or manually-entered source systems produce late-arriving records routinely enough that load logic must handle them explicitly.
