# Playbook

Filled sequences and reference tables for table resets, side-work checklists, and bar-back par sheets — the artifacts this role actually executes against, not descriptions of them.

## Table reset sequence, by party size

| Step | 2-top quick reset | 4-top full reset | 8-top banquet-style reset |
|---|---|---|---|
| 1. Clear to tub | Plates, glasses, flatware | Same, plus condiment caddy | Same, plus linens if soiled |
| 2. Crumb/wipe | Crumber pass, sanitizer wipe | Crumber pass, sanitizer wipe | Crumber pass, sanitizer wipe ×2 (long surface) |
| 3. Linen | Skip unless stained | Change only if stained | Change (standard for this size) |
| 4. Place setting | 2 settings, no bread plate | 4 settings + bread plates | 8 settings + bread plates |
| 5. Condiments/candle | Reposition existing | Reposition existing | Restock if low |
| 6. Signal ready | POS flag / host light | POS flag / host light | Verbal tag to host (large parties usually pre-flagged) |
| **Target time** | **90 sec** | **3 min** | **5–6 min** |

Rule of thumb: reset to the *next known party size* from the wait list or reservation book, not to the table's default template. Resetting a 4-top for an incoming 2-top costs an extra ~60–90 seconds of unnecessary setup and wastes place settings that need re-laundering.

## Table-turn math (worksheet form)

```
Target turn time  = average dine time + target dead time
Target dead time   = bus/reset time (by party size, table above) + host reseat lag (~2 min)
Actual dead time    = [POS: check-closed timestamp] → [POS: next-seated timestamp]

Turns available in a shift window = floor(shift minutes / turn time)
Lost turns  = (target turns − actual turns) × number of tables in that section
Lost covers = lost turns × average party size
Lost revenue = lost covers × average check
```

Worked instance (casual dining, 300-min peak window, 40 tables, avg party 2.7, avg check $32):

- Target dead time: 3 min reset + 2 min reseat lag = 5 min → target turn 42 + 5 = 47 min → 6 turns/table.
- Actual dead time (from logs): 11 min → actual turn 42 + 11 = 53 min → 5 turns/table.
- Lost: 1 turn × 40 tables = 40 turns → ×2.7 covers ≈ 108 covers → ×$32 ≈ $3,456 for the shift.

## Side-work checklist (full-service casual dining, ~40-table floor)

**Opening (target: complete before doors, ~20 min for 2 attendants)**

1. Test sanitizer buckets at every station (target: within label ppm range — see vocabulary.md)
2. Wipe down and stage bus tubs at each station point
3. Stock server-side condiment caddies to par
4. Fill ice bins to 75% capacity (bar and server stations)
5. Cut and stock garnish for opening par (bar)
6. Set backup linens/napkins at each station (par: 1.5× expected covers/hour)
7. Check date labels on any pre-portioned items in server-side reach-ins
8. Sweep/mop entry mats and high-traffic aisles

**Running (ongoing through service, triage order under pressure)**

1. Bus and reset tables per the sequence above (highest priority, never cut)
2. Re-test sanitizer bucket concentration every 2 hours or on visible soiling (never cut — safety)
3. Restock bar garnish/ice/mixers at the half-par trigger (never cut — prevents stockout mid-rush)
4. Restock server-side condiments and linens as depleted (cut only if genuinely backlogged on #1–3)
5. Run food/drinks to tables when servers are buried (cut only if genuinely backlogged on #1–3)
6. Wipe down server stations, straighten menus (cosmetic — first to cut under time pressure)

**Closing (target: 25–30 min for 2 attendants)**

1. Empty and sanitize all bus tubs
2. Break down and sanitize sanitizer buckets — remake fresh for tomorrow's open, never leave overnight
3. Restock and cover garnish trays for next-day prep; discard anything past its date label
4. Ice bins drained and wiped (not left to melt overnight)
5. Backup liquor/keg inventory counted against par sheet, shortage flagged to manager
6. Linens bagged for laundry, counted against par
7. Condiment caddies consolidated, near-empty bottles combined
8. Floors swept/mopped at all stations
9. Trash and recycling from server stations to dumpster
10. Final walk-through: no table left unset for tomorrow's open
11. Checklist board signed off by closing attendant, initialed by shift lead
12. Report any 86'd items or shortages to the opening shift via the pass-down log

## Bar-back par sheet (single-bar, ~150-cover Friday night)

| Item | Par (start of shift) | Restock trigger | Restock source |
|---|---|---|---|
| Lime wedges | 6 dozen | ~half par (~3 dozen) | Cut fresh, walk-in stock |
| Lemon wedges | 4 dozen | ~half par (~2 dozen) | Cut fresh, walk-in stock |
| Olives/cherries | 1 quart each | ~half par (~2 cups) | Pre-jarred, walk-in |
| Bar ice | 75% of well capacity | 40% remaining | Ice machine |
| Backup well spirits | 1 bottle per well brand | Current bottle below ~1/4 | Liquor storeroom |
| Backup call/premium spirits | 2 bottles per high-velocity call brand | Current bottle below ~1/4 | Liquor storeroom |
| Draft beer backup keg | 1 full keg per active tap | Current keg reading low pour pressure / near empty | Keg cooler |
| Backup glassware (rocks/pint/coupe) | 1.5× expected covers/hour | Below 1 rack per type | Dish return / dry storage |

Rule: restock is queued at the *second-to-last visible unit*, not at zero. A bar-back who waits for a bartender to call "86 on limes" mid-ticket has already created a stockout — cutting garnish takes 2–4 minutes the bartender doesn't have during a 90-second cocktail window.
