# Playbook

Filled operational templates a shift supervisor executes directly — not descriptions of what they'd contain.

## Opening checklist (filled example, 6:00am open for 6:30am doors)

| Time | Task | Threshold / spec | Sign-off |
|---|---|---|---|
| 6:00am | Walk-in cooler temp check | ≤41°F; log actual reading, not "OK" | initials + reading |
| 6:05am | Reach-in cold-line temp check | ≤41°F | initials + reading |
| 6:10am | Hot-holding units powered on, verify to temp | ≥135°F before first item loaded | initials + reading |
| 6:15am | Register drawer count-in | matches prior close's drop amount exactly, or logged variance | initials + count |
| 6:20am | Line setup: portioning cups, backup product pulled from walk-in per par sheet | par sheet quantities, not "enough for the rush" | initials |
| 6:25am | Safety walk: floor mats down, wet-floor signage available, fire suppression pull-pin visible | pass/fail | initials |
| 6:30am | Doors open | — | supervisor sign |

## Closing checklist (filled example, last order 9:00pm, close by 9:45pm)

| Time | Task | Threshold / spec | Sign-off |
|---|---|---|---|
| 9:00pm | Last order taken, doors locked or drive-thru closed per posted hours | — | initials |
| 9:05pm | Cooling log started on any bulk-cooked item held over | 135°F→70°F within 2 hrs, then 70°F→41°F within an additional 4 hrs (6 hrs total) | initials + start temp/time |
| 9:15pm | Register drawer close, count against POS z-report | variance >$2 → recount; >$10 → incident report | initials + variance |
| 9:20pm | Comp/void log reconciled against POS override report | every override has a reason code | initials |
| 9:30pm | Equipment shutdown per manufacturer sequence (fryers off/cooled before cleaning) | — | initials |
| 9:40pm | Trash/grease disposal, floor mopped, walk-in door sealed | — | initials |
| 9:45pm | Final walk with next-shift note left for opener (any 86'd items, equipment issues, variance flagged) | written, not verbal-only | supervisor sign |

## Shift-coverage fallback ladder (in preference order)

When a scheduled body doesn't show or calls out mid-shift, work down this list — stop at the first option that closes the gap without creating a new problem:

1. **Already-clocked-in cross-trained floater** — zero incremental cost, zero onboarding lag. Check who's cross-trained on the missing station before anything else.
2. **Early call-in from the next scheduled shift** — costs a few extra hours of straight time; check the incoming person isn't a minor whose hours would then breach a daily cap once you add the extra time.
3. **Overtime for someone already on the clock** — only after 1 and 2 are exhausted; confirm this doesn't push them over 40 hrs/week, which changes the wage math and needs sign-off above shift-lead level in most operations.
4. **Supervisor self-covers the station temporarily** — buys time while the above are arranged; acceptable for 30–60 minutes, not a whole shift, since it pulls the supervisor off floor oversight.
5. **Run short and simplify** — 86 slow-moving or labor-intensive menu items, consolidate stations (e.g., combine two registers into one with a longer queue) — last resort, and only communicated to the guest-facing team with a script, not silently.

## Comp/void approval matrix (filled example)

| Comp/void amount | Who can approve | Required field |
|---|---|---|
| Under $10 | Shift lead (any certified crew lead) | Reason code only |
| $10–$25 | Shift supervisor / MOD | Reason code + free-text note |
| $25–$75 | Store manager or GM | Reason code, note, and guest name/order # if available |
| Over $75 | GM + district/franchise ops notification | Full incident-style write-up |
| Any illness or foreign-object claim, regardless of dollar amount | GM, immediately | Incident report, product sample held if applicable |

## Cash-drawer variance procedure

1. Drawer counted against POS z-report at close of every register, every shift — no exceptions for "it's always fine."
2. Variance ≤$2: logged, no further action.
3. Variance $2–$10: same-shift recount by a second person; if it still doesn't reconcile, logged with a note (till error, misring, etc.) — no incident report yet.
4. Variance >$10, or the same cashier short/over >$2 on 3+ shifts in a rolling 2-week window: incident report, loss-prevention notified, drawer reassigned to individual login if it wasn't already.
5. Drop-safe counts reconciled against register drops at least once per shift change, independent of the register-close count.

## SPLH staffing matrix (filled example, one weekday)

| Daypart | Forecast sales | Target SPLH | Crew labor-hours (forecast ÷ target) | Positions to fill |
|---|---|---|---|---|
| Open–11am (prep) | $400 | $40/hr | 10.0 | 2 grill (5 hrs each) |
| 11am–2pm (lunch) | $2,600 | $60/hr | 43.3 | 2 grill, 2 register, 1 drive-thru (~8.7 hrs total ÷ 5 stations ≈ ~1.7 hrs headroom above minimum staffing) |
| 2pm–5pm (trough) | $600 | $45/hr | 13.3 | 1 grill, 1 register (skeleton crew) |
| 5pm–9pm (dinner rush) | $3,200 | $50/hr | 64.0 | 2 grill, 2 register, 1 drive-thru, supervisor floats |
| 9pm–close | $500 | $45/hr | 11.1 | 1 grill, 1 register |

Read the table right-to-left when building the actual schedule: forecast sales and target SPLH are fixed inputs from historical data and chain policy; crew labor-hours is the number the schedule has to hit, and positions are how those hours get distributed across stations — not the other way around.

## De-escalation script fallback ladder (customer complaint)

1. **Acknowledge without conceding fault** — "I'm sorry your order wasn't right, let's fix it" — before any dollar figure is discussed.
2. **Offer the standard remedy** (remake the item, or comp the specific item) — this is within any shift lead's authority per the comp/void matrix above.
3. **If declined, escalate to the supervisor/MOD on shift** — who can authorize up to the next matrix tier without pulling in the GM.
4. **If the complaint involves illness, injury, or a foreign object**, skip straight to GM notification and an incident report regardless of the guest's requested remedy — this tier is about legal exposure, not guest satisfaction.
5. **Close the loop in the shift log** either way, so a pattern across multiple complaints on the same shift or item is visible to whoever reviews the week.
