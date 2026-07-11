# Broadcast Announcer Playbook

Filled templates for building and running a live shift — populate with the actual station's numbers, don't rewrite from scratch each shift.

## 1. Hot clock (midday format example, 12:00:00–1:00:00)

| Time | Element | Duration |
|---|---|---|
| :00–:02 | Sweeper into music sweep | 2:00 |
| :02–:14 | Music block (3 songs) | 12:00 |
| :14–:16 | Talk break 1 (banter, back-announce) | 2:00 |
| :16–:17 | Spot break (1x :60) | 1:00 |
| :17–:29 | Music block (3 songs) | 12:00 |
| :29–:32 | Talk break 2 (feature/bit) | 3:00 |
| :32–:34 | Spot break (2x :30) | 1:00 |
| :34–:46 | Music block (3 songs) | 12:00 |
| :46–:53 | Talk break 3 (caller/interview segment) | 7:00 |
| :53–:56 | Spot break (2x :30, 1x :60) | 2:00 |
| :56–:58 | Talk break 4 (tease, back-announce) | 2:00 |
| :58 | Legal station ID | :08 |
| :58:08–:59:53 | Music bed / final sweeper | 1:45 |
| :59:53–1:00:00 | Network join sweeper | :07 |

Talk allotment per hour: ~16 minutes across four breaks. Any single break running more than 90 seconds over its slot cascades delay into every following element unless a downstream break absorbs the overage.

## 2. Backtiming worksheet (fill live, work backward from the hard post)

| Field | Example filled entry |
|---|---|
| Hard post | Network news join, 1:00:00 PM |
| Time break started | 12:56:00 |
| Total window (seconds) | 240 |
| Fixed elements (spots, legal ID, sweeper) | 75s |
| Unplanned fixed additions (EAS/weather read) | 30s |
| Revised fixed total | 105s |
| Flexible budget (window − fixed) | 135s |
| Flexible content actually run | Caller wrap 130s + short liner 5s = 135s |
| Cut to make budget | Tease (20s) moved to next hour; back-announce trimmed 15s → 5s |
| Result | Post hit at exactly 1:00:00 |

## 3. Break script template (produced or semi-scripted break)

| Beat | Purpose | Target length |
|---|---|---|
| Hook | One line that makes the listener stay through the next 30 seconds | 3–5s |
| Content | The actual bit, story, or interview payoff | Bulk of the break |
| Button/payout | The line that closes the thought — never trail off | 3–5s |
| Back-announce or tease | What just played / what's coming, tied to the next hard post | 5–15s |

Bullet-point prep, not a full script, for anything except legal must-reads — a fully scripted break reads stilted live; legal copy (contest odds, sponsor disclosure, no-purchase-necessary language) is read verbatim from the log, no exceptions.

## 4. EAS / breaking-weather protocol (fill with the station's actual policy numbers)

1. Alert received via EAS decoder or NWS feed — confirm it requires a live read (tornado/severe thunderstorm warning tier) versus a lower-tier watch that can wait for the next scheduled break.
2. Add the read as a new fixed element to the current break's time budget immediately (see backtiming worksheet, step 5) — do not try to absorb it into existing flexible time without recomputing.
3. Read verbatim: warning type, affected county/area, expiration time, one framing/safety line. Target ~30 seconds for a standard severe thunderstorm warning; longer for a tornado warning with shelter guidance.
4. Cut flexible elements in this order to protect the read: tease first, back-announce second, caller wrap-up third (verbal close, not an abrupt cutoff) — never the legal ID or the hard post itself.
5. Log the deviation (what was cut, why) for the program director before the next shift.

## 5. Voice-tracking checklist (per market, per break)

| Check | Why it matters |
|---|---|
| One dated local reference per break (event, weather, a specific street/venue) | Generic tracks are the first thing a PD or attentive listener flags as canned |
| Reference is still accurate at the scheduled air time in that market | A track recorded Tuesday for Thursday air needs weather/event language that still holds |
| No cross-market references bleed into the wrong market's track | Same host voice-tracking 4 stations must swap all market-specific lines per station, not just the station ID |
| Legal/must-read copy pulled fresh from that market's traffic log | Sponsor copy differs by market even when the host and format are identical |
| Track reviewed against that day's actual playlist, not an assumed one | Automation-side substitutions (a song swapped for rights/rotation reasons) can make a scripted back-announce reference the wrong song |

## 6. Fallback order when time runs short (any break, any cause)

1. Trim back-announce to a single liner.
2. Cut the tease — move it to the next hour or the next break.
3. Verbally wrap a caller or guest rather than cutting them off mid-sentence.
4. Shorten (never cut) a produced sweeper to its core ID element.
5. Legal ID and the hard post itself are never touched — everything above exists to protect these two.
