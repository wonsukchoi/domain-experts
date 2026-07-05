# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual variance worksheet, menu matrix, or par tracker — not for general reasoning (that's `SKILL.md`).

## Food cost variance worksheet (weekly)

```
Week ending: [date]                    Food sales: $18,500        Target food cost %: 30%

Beginning inventory:        $22,400
+ Purchases this week:      $ 6,100
- Ending inventory:         $22,190
= Theoretical usage (COGS): $ 6,310    -> Theoretical food cost % = 6,310/18,500 = 34.1%

Actual food cost booked:    $ 6,327    -> Actual food cost % = 34.2%
Variance vs. 30% target:    +4.2 pts = $777 over plan

DRIVER ISOLATION (cheapest check first):
1. Price variance: top-10 item invoice prices vs. last period — [flat / +X%]
2. Portion check: spot-check 5 plates of top-3 sellers against recipe spec (oz) — [result]
3. Waste log: this week's disposed inventory ($) vs. 8-week trailing average — [result]
4. Comp/void report: this week's $ vs. trailing average — [result]

Unexplained residual after driver checks: $[amount] — escalate to full recipe cost audit if >$150 or >1 point
```

## Menu engineering matrix

```
Item              | Sales mix % | Food cost % | Contribution margin/plate | Quadrant        | Action
------------------|-------------|-------------|----------------------------|-----------------|------------------
Steak frites      | 18%         | 38%         | $14.20                     | High pop/Low mgn| Reprice +$2 or reduce portion 1oz
Roast chicken     | 22%         | 26%         | $11.80                     | High pop/High mgn | Feature, protect price
Duck confit       | 4%          | 24%         | $16.50                     | Low pop/High mgn | Reposition on menu, staff upsell training
Veggie plate      | 6%          | 41%         | $6.10                      | Low pop/Low mgn | Cut or reprice; check if it's a loss leader by design
```

## Par level tracker (per SKU)

```
Item: Chicken breast, 8oz portion
8-week trailing avg weekly usage: 210 lbs
Delivery frequency: 2x/week (Mon, Thu)
Lead time: 1 day
Safety stock: 15% of avg usage between deliveries = ~16 lbs

Par (max) = (avg usage between deliveries) + safety stock = 105 lbs + 16 lbs = 121 lbs
Par (min, reorder point) = lead-time usage + safety stock = 30 lbs + 16 lbs = 46 lbs

Review cadence: monthly, or immediately after a >15% shift in that item's sales mix
```
