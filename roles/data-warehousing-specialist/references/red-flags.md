### A fact table's grain wasn't declared in writing before modeling began
- **Usually means:** the table was designed measure-first (someone needed a specific number, built a table to hold it) rather than grain-first; second likeliest is two people modeled different parts of the same table against different assumed grains.
- **First question:** what does one row in this table actually represent, in one sentence with no "and"?
- **Data to pull:** the fact table's DDL alongside a sample of 10-20 actual rows, checked against the stated grain.

### A dimension attribute known to change over time is implemented as Type 1 (overwrite) with no documented reason
- **Usually means:** the SCD type was applied as a table-wide default rather than decided per attribute; second likeliest is nobody asked whether any downstream report needs historical "as it was then" values for that attribute.
- **First question:** does any existing or planned report need this attribute's value as of a past transaction date, not just its current value?
- **Data to pull:** list of reports/dashboards joining to this dimension, and which attributes each one filters or groups by.

### An incremental load uses a `modified_date > last_run` filter with no confirmation the column updates on every relevant change
- **Usually means:** the load logic was copied from another source's pattern without verifying this specific source's update behavior; second likeliest is a batch/bulk update process in the source that bypasses the tracked column.
- **First question:** has this specific source's owner confirmed that column updates on every write path, including batch jobs?
- **Data to pull:** source system's update/write documentation, or a test insert/update tracing whether the column changes.

### A completed load passed row-count reconciliation but no aggregate-measure check was run
- **Usually means:** validation stopped at the easiest check; second likeliest is the load process doesn't have an automated aggregate reconciliation step at all.
- **First question:** does `SUM()`/`COUNT(DISTINCT)` on the key measures match between source and warehouse for this load period?
- **Data to pull:** source and warehouse aggregate query results for the same measures and period.

### Two BI dashboards report different numbers for what should be the same conformed dimension
- **Usually means:** two source systems have different definitions of the same business entity (e.g., "active customer") that were never explicitly reconciled; second likeliest is one dashboard queries a stale or unconformed copy of the dimension.
- **First question:** do the two source systems' definitions of this entity actually match, with a concrete example checked?
- **Data to pull:** both dashboards' underlying query definitions and both source systems' documented entity definitions.

### A join between a fact table and a dimension produces more rows than the fact table alone
- **Usually means:** a many-to-many relationship (e.g., multiple promotions per order line) is being joined directly instead of through a bridge table, fanning out rows and inflating aggregate measures.
- **First question:** is there a genuine one-to-many (or many-to-many) relationship here, and if so, is a bridge table being used?
- **Data to pull:** row count of the fact table alone versus the joined result set for the same filter.

### A Type 2 dimension has multiple rows marked `is_current = 'Y'` for the same natural key
- **Usually means:** the load process that closes out the previous current row failed or ran out of order relative to the insert of the new row; second likeliest is a race condition in a concurrent load process.
- **First question:** when did this duplicate current-row state first appear, and does it correlate with a specific load run?
- **Data to pull:** load run history/logs for the affected dimension table around the time the duplicate appeared.

### Backdated source corrections to historical data have no defined handling in the load process
- **Usually means:** the load was designed only for the on-time, forward-moving happy path; second likeliest is the team assumed corrections "don't really happen" without checking source system behavior.
- **First question:** has the source system ever issued a correction to data older than the current load window, and what happened to it in the warehouse?
- **Data to pull:** source system's change log or audit trail for any backdated correction events.

### A surrogate key collision or gap appears in a dimension table
- **Usually means:** two separate load processes are generating surrogate keys independently without coordination (e.g., two ETL jobs both inserting new customer rows); second likeliest is a key-generation sequence was reset or reused.
- **First question:** is there more than one process capable of inserting new rows into this dimension table?
- **Data to pull:** surrogate key generation logic and a list of all processes that write to this dimension table.
