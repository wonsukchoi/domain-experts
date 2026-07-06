# Data Warehousing Playbook

## Grain declaration worksheet

Fill this out before modeling any fact table:

```
Fact table: fact_orders
Grain (one sentence): "One row per [order line item], for [each distinct promotion applied]."
Test: does this sentence use "and" to describe two different things a row could be? If yes, split into two fact tables or redeclare grain.

Measures at this grain:
  - line_amount (additive)
  - discount_amount (additive)
  - quantity (additive)

Dimensions this grain can join to:
  - dim_date (order_date)
  - dim_customer
  - dim_product
  - dim_promotion (via bridge table if many-to-many)
```

## SCD type decision table

| SCD Type | Behavior | Use when | Don't use when |
|---|---|---|---|
| Type 1 | Overwrite in place, no history | Correcting errors (typo fixes, data entry corrections); attribute has no historical reporting need (email, phone) | A report needs to reflect the attribute's value as of a past transaction date |
| Type 2 | New row per change, with `effective_date`/`end_date`/`is_current` | Attribute changes and historical reporting needs "as it was then" (region, sales rep assignment, price tier) | Change volume is very high (creates row explosion) or history genuinely doesn't matter |
| Type 3 | Add a "previous value" column, limited history (usually 1 prior value) | Only the immediately prior value is ever needed, not full history | More than one historical value might be needed later — Type 3 can't retroactively add more history |

Type 2 implementation template:

```sql
-- Close out the current row when an attribute change is detected
UPDATE dim_customer
SET end_date = @change_date - INTERVAL '1 day', is_current = 'N'
WHERE customer_id = @customer_id AND is_current = 'Y';

-- Insert the new current row
INSERT INTO dim_customer (customer_key, customer_id, region, effective_date, end_date, is_current)
VALUES (@new_surrogate_key, @customer_id, @new_region, @change_date, '9999-12-31', 'Y');
```

## Incremental load design checklist

1. **Identify the source's actual change-capture mechanism** for this specific feed:
   - CDC log / transaction log shipping (most reliable — captures every change including deletes)
   - `modified_date` column (reliable only if confirmed to update on every relevant change, including batch jobs)
   - Batch flag / status column (reliable only for that specific batch process's changes)
2. **Confirm the mechanism against the source system owner**, not by assumption — ask specifically whether batch/bulk updates touch the tracked column.
3. **Design for late-arriving records**: a record with an old business date but a recent change-capture timestamp must still be captured by the watermark logic (filter on change-capture timestamp, not business date).
4. **Design for backdated corrections**: a source correction to historical data needs a defined behavior (reprocess the affected historical partition, or Type 2 the affected dimension row) — decide this explicitly, don't let it silently fall through.
5. **Set the watermark only after confirming the load succeeded** — advancing the watermark before validating the load risks silently skipping records on a retry.

## Source-to-target reconciliation template

Run both checks — row count is necessary but not sufficient:

```
Reconciliation Report — fact_orders, period 2026-02-01 to 2026-02-28

Row count:
  Source extract:     48,213 rows
  Warehouse load:      48,213 rows
  Match: YES

Aggregate measures (the actual correctness test):
  SUM(order_line_amount):
    Source:     $1,839,411.00
    Warehouse:  $1,842,006.50
    Discrepancy: $2,595.50  <-- FAIL, investigate before sign-off

  COUNT(DISTINCT order_id):
    Source:     12,847
    Warehouse:  12,847
    Match: YES

Investigation: discrepancy traced to fan-out join against dim_promotion
  (many-to-many relationship joined directly instead of via bridge table).
Fix: rebuilt join through promotion_bridge table.
Re-reconciliation: $0.00 discrepancy. Load approved.
```

## Conformed dimension conflict resolution

When two source systems disagree on a dimension's definition:

1. Document both definitions side by side with a concrete example showing where they diverge (e.g., "System A counts a customer active with any order in trailing 12 months; System B uses trailing 6 months — customer C-4471's last order was 8 months ago, active under A's definition, inactive under B's").
2. Escalate to the business owner(s) of both systems — this is a business-rule decision, not a data-modeling one.
3. Once a decision is made, document the chosen definition in the conformed dimension's metadata/documentation, and note which source system's reports will now disagree with the warehouse (so that discrepancy is expected, not a bug report).
4. Never silently pick one source's definition without documenting the decision and notifying both systems' stakeholders — this is exactly the kind of quiet decision that produces "the warehouse and Report X disagree" tickets months later.
