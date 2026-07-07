# Short-order playbook

Filled reference tables and worked drills for a solo flattop-and-fryer station. Numbers are plausible operational figures, not universal constants — recalibrate against your own equipment and ticket volume.

## Griddle zone reference

A 36-inch flattop split into three working zones rather than run at one temperature:

| Zone | Target surface temp | Used for | Failure mode if merged with another zone |
|---|---|---|---|
| A — sear | 400–425°F | Bacon, sausage patties, burgers, hash brown final crisp | Eggs scorch on the edges before the center sets |
| B — eggs/pancakes | 350–375°F | All egg styles, pancakes, French toast | Bacon renders too slowly, sausage stays gray |
| C — hold/toast | 300–325°F | Butter for toast, holding a finished item 30–60 seconds for a slow ticket-mate, quesadilla-style items | Eggs overcook waiting for a same-ticket item to finish elsewhere |

Recheck all three with a probe or laser thermometer every 20–30 minutes during a rush — a single 14-item burst across Zone A can drop it 20–30°F below the dial setting, which is exactly when bacon starts coming off gray instead of crisp.

## Egg doneness-to-zone cheat sheet

| Order | Zone | Flip? | Visual done cue | Typical active time |
|---|---|---|---|---|
| Sunny side up | B | No | White fully set, yolk glossy and unbroken, edges just browning | 2.5–3 min |
| Over easy | B | Yes, once, brief | Flip, 15–20 sec on second side, yolk still liquid | 2–2.5 min total |
| Over medium | B | Yes, once | Flip, 30–40 sec second side, yolk thickened but not set | 2.5–3 min total |
| Over hard | B | Yes, once | Flip, 60+ sec second side, yolk fully set | 3–3.5 min total |
| Scrambled, soft | B | Continuous fold | Curds form but stay glossy, no browning | 90 sec |
| Scrambled, dry | B | Continuous fold | No visible liquid egg, light browning on curd edges acceptable | 2 min |

Advisory doneness orders (over easy, over medium, sunny side up served to a customer who declined the well-done substitution) require the menu's consumer-advisory disclosure per FDA Food Code 3-603.11 — the cook's obligation is only to keep these off the standard batch grouping, since a batch is fired as one unit and a scrambled-dry order accidentally grouped with an over-easy batch comes out wrong for both.

## Par-hold reference table

Only items that hold safely above 135°F and don't lose the texture that makes them the ordered product belong on a par-hold plan. Eggs are excluded on both counts.

| Item | Par-cook method | Safe hold temp | Quality hold window | Finish-to-order time |
|---|---|---|---|---|
| Bacon | Cook to ~70% doneness (limp, rendered, not yet crisp) | ≥135°F | Up to ~4 hours | 60–90 sec on Zone A |
| Breakfast sausage patty | Cook through to 155°F internal, hold | ≥135°F | Up to ~4 hours | 45–60 sec on Zone A |
| Hash browns ("scattered") | Par-steam or par-fry shredded potato until just tender, no color | ≥135°F or room-temp staged for immediate use | ~2 hours before quality drops | 90 sec–2 min browning on Zone A |
| Home fries | Par-boil diced potato until fork-tender | ≥135°F | Up to ~3 hours | 2–3 min crisping on Zone A |

## Ticket-batching drill (worked example)

Rail shows five tickets at once:

| Ticket | Items |
|---|---|
| 1 | 2 eggs over easy, bacon, wheat toast |
| 2 | 3 eggs scrambled dry, sausage, hash browns "smothered and covered" |
| 3 | 1 egg over medium, bacon, hash browns "scattered" |
| 4 | Western omelet (no batching — cooked to order, single item, ~4 min) |
| 5 | 2 eggs over easy, sausage, hash browns "covered"

**FIFO approach (naive):** cook ticket 1 start-to-finish (≈5 min with toast), then ticket 2 (≈5 min), then 3, 4, 5 — total ≈24 minutes before ticket 5 even starts, let alone finishes. First ticket out at 5 min, last ticket out at ~24+4=28 min.

**Zone-batched approach:**
- Eggs over easy (tickets 1, 3-medium is separate doneness so held out, 5) — tickets 1 and 5 share an over-easy batch on Zone B: 4 eggs, one flip motion, ~2.5 min.
- Ticket 3's over medium is a different doneness — fired as its own single-egg batch on Zone B in parallel, ~3 min.
- Scrambled dry (ticket 2) fired as its own batch since no other ticket shares that doneness this round, ~2 min, timed to land with ticket 2's sausage.
- Bacon (tickets 1, 3) batched together off the par-hold: 60–90 sec.
- Sausage (tickets 2, 5) batched together off the par-hold: 45–60 sec.
- Hash browns: three different modifiers ("smothered and covered," "scattered," "covered") still share Zone A browning time even though toppings differ — one pass, ~2 min, toppings added per-ticket at plate-up.
- Western omelet (ticket 4) is the one item that can't batch — cooked alone on Zone B once the egg-batches clear it, ~4 min.

Result: all five tickets land within an 8–9 minute window instead of the FIFO approach's 28 minutes, because five tickets' worth of items reduce to roughly four concurrent batches across two zones instead of five sequential single-ticket cooks.

## 86 threshold calculation

Formula: 86 the item when `remaining stock < (remaining rush minutes ÷ average minutes between orders for that item)`.

**Example.** Hash browns: 18 portions left at 8:40am. Rush ends at 9:30 (50 minutes left). Over the last 30 minutes, hash browns have been ordered on average once every 4 minutes → expected remaining demand = 50 ÷ 4 = 12.5 portions.

18 > 12.5, so hash browns are not yet at the 86 threshold — but the gap (18 − 12.5 = 5.5 portions of buffer) is thin enough to start a fresh par-boil batch now rather than wait. If the same check at 9:05 shows 6 portions left with 25 minutes remaining and the same 4-minute order interval (expected demand 25 ÷ 4 = 6.25), the item crosses the threshold and gets called as 86'd immediately — before the next ticket that would have needed it fires.

## Shift handoff par-usage log (filled example)

```
Date: Sat, rush 8:00–9:30
Tickets: 30 | Items: 72
Bacon:      par 60 (40 opening + 20 mid-rush) | used 46 | held over 14 (discarded, hold-limit)
Sausage:    par 45 | used 38 | held over 7
Hash browns: par 70 portions | used 61 | 86'd at 9:05, restocked for lunch
Griddle notes: Zone A drifted to 370°F under the 8:15 burst — recheck with probe before next rush
Next-shift adjustment: start hash brown second batch at +20 min, not +30
```
