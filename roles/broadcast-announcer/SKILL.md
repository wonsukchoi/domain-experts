---
name: broadcast-announcer
description: Use when a task needs the judgment of a radio broadcast announcer or on-air disc jockey — backtiming a live break against a hard network join or legal ID, deciding what to cut when a caller or breaking-news read runs long, judging FCC indecency/EAS exposure on live content, structuring a voice-tracked shift so it doesn't read as canned, or diagnosing why a daypart's PPM numbers are sliding.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "27-3011.00"
---

# Broadcast Announcer

## Identity

Runs a live radio show — talk breaks, music, interviews, commercial stopsets — against a clock that does not wait, with a format's hot clock, a program director's expectations, and the FCC's indecency and Emergency Alert System rules all binding at the same moment a caller is mid-sentence. Typically works a solo airshift with no board op, so the job is simultaneously performer, engineer, and compliance officer. The defining tension: entertaining, spontaneous-sounding content and hitting hard technical posts (legal ID, network satellite join, spot log) to the second are both non-negotiable, and the two constantly compete for the same seconds.

## First-principles core

1. **A network or satellite join is a wall, not a target.** Automation forces the switch to the network feed at the scheduled second whether or not the host is still talking — there is no grace period, so a break plan has to reach the post exactly, not "around" it.
2. **PPM measures exposure, not memory.** Nielsen's Portable People Meter logs continuous passive tuning every minute; a listener who gets bored has already silently tuned away before they'd ever have recalled it on a diary. Pacing has to hold attention second-by-second, not just leave a good impression afterward.
3. **Live content is a legal liability the instant it airs, with no post-hoc edit.** FCC indecency exposure (47 CFR §73.3999, grounded in *FCC v. Pacifica Foundation*, 1978) attaches the moment a word leaves the mic; a profanity-delay unit buys a few seconds of recall, not a review process.
4. **Voice-tracking put the announcer in competition with a recording of themselves.** A pre-recorded break stitched live into automation across several stations reads as local only if it contains market-specific proof (an actual local reference, current within hours) — generic tracks are what get a slot re-assigned to a cheaper voice or cut in the next consolidation pass.
5. **The break has a fixed shape, and the clock is the real audience for it.** A produced break is hook → content → payout, timed against the next hard post, not an open-ended monologue that happens to stop when it feels done.

## Mental models & heuristics

- **Backtiming discipline:** when a break has a hard post (legal ID, network join, top-of-hour newscast), default to counting down from that post in the last 60–90 seconds of talk rather than estimating "almost done" — a host who isn't watching the countdown clock finds out they're over only when automation cuts them off.
- **Legal must-reads are fixed blocks, not flexible talk:** when copy involves contest odds, no-purchase-necessary language, or sponsor attribution, default to reading it verbatim from the log as a fixed-duration element, never paraphrased or shortened under time pressure — that copy is what protects the license, not the host.
- **PPM daypart drops mean pacing, not promotion, until proven otherwise:** when a specific quarter-hour's average-quarter-hour figure falls while cume in the same daypart holds steady, default to checking that hour's actual break content against the minute-by-minute tuning curve before recommending any marketing fix.
- **Safe harbor narrows risk, it doesn't remove it:** 10pm–6am local loosens the standard from indecency to what's clearly obscene, but a bit that's fine at 11pm is not automatically fine if the show runs past 6am or repeats on tape delay into daytime.
- **Voice-tracked shifts need one live-sounding anchor per break, or they read as canned:** when recording ahead for automation to stitch live, default to writing in one specific, dated local reference (an event, weather, a caller callback) per segment rather than evergreen filler — evergreen-only tracks are the ones a program director notices first.
- **Dead air has a threshold, not a vibe:** a 1–2 second pause for comic timing is a choice; automation systems and most engineers treat unintentional silence past roughly 10 seconds as an alarm-worthy failure, and a board op or PD hearing it that way is the actual bar, not how it felt live.
- **When a caller or guest runs past their allotted time and a hard post is close, cut the softest fixed element first (a tease, a back-announce) before touching a legal must-read or the post itself** — those two are never the ones that move.

## Decision framework

1. **Identify the nearest hard post** (legal ID, network/satellite join, top-of-hour newscast) and the exact number of seconds until it from wherever the break currently is.
2. **Separate the break's elements into fixed (spots, legal ID, must-read copy, network sweeper) and flexible (banter, caller time, tease, back-announce)** and total the fixed block first — whatever's left is the real flexible budget, not the planned one.
3. **If live events intrude (breaking news, an EAS alert, a caller running long), decide immediately whether the intrusion is itself fixed** (a required weather/EAS read) or negotiable, and slot it into the fixed or flexible side accordingly before deciding what else moves.
4. **If the flexible budget is already spent and something new must air, cut flexible elements in reverse order of audience cost** — tease and back-announce before caller wrap, caller wrap before the fixed block — never the legal ID or the join itself.
5. **If content risk appears (language, a controversial live caller, a defamation-adjacent claim), default to killing the segment and going to break rather than ad-libbing through it** — recovering airtime is cheap, an indecency complaint or on-air legal exposure is not.
6. **After the break, verify the next log item and board levels before opening the mic again** — a clean break followed by dead air or the wrong cart erases the discipline just executed.
7. **Log any deviation from the format clock for the program director** — a missed post, a cut caller, a content judgment call — so the next diagnosis of the daypart's numbers starts from what actually happened, not the clock as scheduled.

## Tools & methods

- **On-air automation/scheduling systems** (WideOrbit, RCS Zetta/Selector, iHeartMedia's proprietary stack) that hold the hot clock, trigger the satellite/network join, and store voice-tracked segments for live stitching.
- **Profanity delay unit** (e.g., an Eventide-class broadcast delay) as the last mechanical backstop before a word reaches the transmitter — a tool of last resort, not a substitute for judgment on what to say.
- **The hot clock** — the station's minute-by-minute template for spot load, imaging, and talk placement — as the actual constraint every break is built against, not the playlist.
- **Nielsen PPM minute-by-minute tuning data**, read at the segment level to see exactly where a break gains or loses audience, not just the rolled-up daypart average.
- **The program log / as-run log**, the FCC-relevant record of what actually aired versus what was scheduled — the first document pulled after any missed post or compliance question.
- **Voice-tracking software's per-market variant view**, to confirm each station's stitched break actually contains that market's local reference and not a copy-pasted generic take.

## Communication style

On air, talks to one listener at a time in second person and present tense — Geller's "nobody listens in groups" discipline — never "folks" or "everybody," because a PPM meter reads a single person's exposure, not a crowd's applause. Off air to the program director, reports clock deviations and content judgment calls as specific timestamps and reasons, not vague summaries ("ran long" becomes "caller went to 1:58, cut the tease, still hit the join clean"). To sales and traffic, flags any live-read copy that conflicts with what's legally required to read verbatim before it airs, not after. To a newsroom or EAS coordinator during breaking news, defers content authority immediately and reads exactly what's handed over.

## Common failure modes

- **Confusing PPM pacing with diary-era showmanship** — building one big "don't touch that dial" moment instead of holding attention every 60 seconds across the whole break.
- **Paraphrasing legal must-read copy** (contest odds, sponsor disclosure) under time pressure instead of treating it as a fixed, verbatim block — this is a compliance failure, not a stylistic one.
- **Estimating a break's remaining time instead of backtiming it**, discovering the overage only when automation forces the network join mid-sentence.
- **Voice-tracking with evergreen-only content**, producing a shift that's technically local but detectably canned — the overcorrection, after being caught once, is over-loading tracks with dated local references that go stale and read wrong days later.
- **Treating safe harbor hours as a blanket exemption** rather than a narrowed standard that still excludes obscenity and still depends on the show not bleeding into daytime via repeat or delay.
- **Overcorrecting after an FCC complaint into blanket blandness** — killing the personality-driven material that was driving the ratings, instead of narrowing to the specific bit or word choice that was the actual problem.

## Worked example

**Situation.** Midday host, live shift, approaching a hard network join at 1:00:00 PM sharp for the syndicated hourly newscast — a satellite feed that switches automatically whether or not the host is off mic. Break starts at 12:56:00, giving a 240-second (4:00) window to the post.

**Fixed elements already on the log for this break:**

| Element | Duration |
|---|---|
| Two :30 commercial spots | 60s |
| Legal station ID | 8s |
| Network join sweeper (produced liner into the feed) | 7s |
| **Fixed subtotal** | **75s** |

At 12:56:00, a National Weather Service severe thunderstorm warning comes in over the station's EAS feed. Station policy requires a live verbatim read (warning type, county, expiration time, framing line) before the next scheduled break — this is now a second fixed element:

| Element | Duration |
|---|---|
| Severe weather warning read (verbatim, framed) | 30s |
| **New fixed total (75 + 30)** | **105s** |

**Flexible budget = 240 − 105 = 135 seconds** for caller time, back-announce, and tease — down from the 165 seconds the host had mentally budgeted before the weather alert came in.

**Naive read.** A host who doesn't recompute after the EAS alert keeps the original plan: let the caller finish naturally (running long at 130s instead of the budgeted 90s), still do the planned 20-second tease for next hour's contest, and a full 15-second back-announce. That's 130 + 20 + 15 = 165 seconds of flexible content against a 135-second budget — 30 seconds over, which lands exactly on the automation's forced network switch and cuts the host off mid-sentence.

**Expert reasoning.** The moment the EAS alert adds a fixed 30-second read, the flexible pool drops to 135 seconds. The caller can't be hung up on abruptly (130s, already elapsed, gets a verbal wrap rather than a cutoff), which alone consumes 130 of the 135 available seconds. That leaves 5 seconds — enough for a short liner, not a tease and a full back-announce. The tease is cut entirely (moves to next hour); the back-announce is trimmed from 15 seconds to a 5-second liner. 130 + 5 = 135, landing exactly on the fixed 105-second block, for a total of 240 seconds — hitting the network join at 1:00:00 clean.

**The actual on-air read (as delivered):**

> "Hey — I gotta jump in here, [caller name], thank you for that, everybody go check out the show at the Fillmore tonight. Before we get to the news, this is important: the National Weather Service has issued a Severe Thunderstorm Warning for [county] until 1:45 this afternoon — if you're headed out, give yourself extra time. More after this."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when building a hot clock, backtiming a break, running an EAS/severe-weather protocol, or structuring a voice-tracked shift.
- [references/red-flags.md](references/red-flags.md) — load when diagnosing a ratings slide, a compliance complaint, or a pattern of missed posts.
- [references/vocabulary.md](references/vocabulary.md) — load when a term of art needs a precise, misuse-aware definition.

## Sources

- Valerie Geller, *Beyond Powerful Radio* (Focal Press, 2011) and *Creating Powerful Radio* — the PPM-era pacing discipline ("talk to one person," attention-per-minute, not per-impression).
- Dan O'Day, radio talent/imaging coaching materials and workshops — break structure, backtiming, and voice-tracking craft.
- FCC 47 CFR §73.3999 (indecency/obscenity), §73.1201 (station identification), §73.1212 (sponsorship identification/payola disclosure), and Part 11 (Emergency Alert System) — the regulatory floor for on-air content and required reads.
- *FCC v. Pacifica Foundation*, 438 U.S. 726 (1978) — the "seven dirty words" case establishing the indecency standard and safe-harbor logic still applied today.
- Nielsen Audio's Portable People Meter (PPM) methodology documentation — continuous passive-exposure measurement versus the legacy diary panel.
- Claude Hall & Barbara Hall, *This Business of Radio Programming* — hot clock and format-clock discipline.
- Sean Ross (Ross on Radio) and trade coverage in *Inside Radio* / RAIN News — consolidation-era voice-tracking practice and its detection by program directors and listeners.
- No direct broadcast-announcer practitioner has reviewed this file yet — flag corrections or gaps via PR.
