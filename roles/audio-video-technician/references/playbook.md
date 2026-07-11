# Playbook

Filled tables and worksheets for live-event load-in, RF coordination, lip-sync budgeting, and redundancy decisions. Populate with the specific venue's numbers; the structure and thresholds below are the reusable part.

## Load-in sequencing checklist (risk-ordered, not chronological-by-convenience)

| Order | Task | Why this order | Time-box guidance |
|---|---|---|---|
| 1 | RF spectrum scan + wireless frequency coordination | Hardest to diagnose once other gear is patched in; local TV allocation varies by venue and can shift with no warning | 30–60 min depending on channel count |
| 2 | Venue power/ground check (dedicated circuits, isolated ground where required) | A bad ground shows up as hum discovered hours later if not checked first | 15–20 min |
| 3 | Multi-hop video chain bench test (camera → switcher → scaler → display) | Most frame-accumulating latency and handshake failures live here | 45–90 min |
| 4 | Individual audio path bench tests (mic → board → output) | Faster to verify once RF is already clean | 20–30 min |
| 5 | Full end-to-end chain rehearsal at show conditions | Confirms lip sync and cutover together — never skip even under time pressure | 30–45 min |
| 6 | Redundancy cutover test (deliberately fail the primary path) | Prove backup engages within an acceptable time before doors, not during the show | 10–15 min |
| 7 | Freeze and distribute the show file | Last task before doors — nothing should change after this without re-verifying | 10 min |

**Rule of thumb:** if steps 1–3 aren't clean with at least 90 minutes of buffer before doors, escalate to the producer for a delayed start or reduced scope — do not compress step 5 (full rehearsal) to make up the time. Step 5 is the only step that catches system-level problems (lip sync, cutover) that no individual bench test will surface.

## RF frequency coordination worksheet

| Step | Action | Threshold / pass criterion |
|---|---|---|
| 1 | Scan 470–698 MHz (or locally relevant UHF band) on site | Identify occupied TV channels (6 MHz each) and any persistent RF noise floor above −85dBm |
| 2 | Exclude any channel occupied by a full-power local DTV signal | FCC 600 MHz repack (2020) removed wireless mic use above 608 MHz in most markets — verify local allocation, don't assume it's still open |
| 3 | Load remaining clear spectrum into coordination software (Wireless Workbench / WSM) | Software computes 3rd-order intermodulation products for every candidate frequency set |
| 4 | Select the frequency set with zero IM products within 100kHz of any active channel | This is the pass/fail gate — a "close enough" spacing that skips this check is the single most common cause of mid-show RF dropout |
| 5 | Reserve at least 1 unused, cleared frequency as a hot-swap spare per wireless group of 6 | Lets a tech swap a failing unit live without re-coordinating under show pressure |

## Latency-budget calculation table (lip sync)

| Chain segment | Typical added latency | Notes |
|---|---|---|
| Camera sensor/output | 1 frame | Fixed by camera design, rarely user-adjustable |
| Video switcher, frame sync engaged | 1–3 frames | Higher if reconciling a non-genlocked source |
| Scaler / format converter | 1–2 frames | One conversion per hop; chained converters add up |
| LED wall / projector processor | 1–2 frames | Varies significantly by processor model — check spec sheet, don't assume |
| **Video total (example)** | **6 frames** | At 29.97fps ≈ 200ms; at 59.94fps the same 6 frames ≈ 100ms — frame count matters more than raw ms across frame-rate choices |
| Wireless mic RF link (encode/decode) | 3–5ms | Digital wireless systems only; analog RF is near-zero |
| Digital mixer input/output stage | 1–2ms per stage | Negligible alone, additive across multiple digital devices |
| DSP processing block | 2–5ms | Depends on processing complexity (EQ, dynamics chains) |
| **Audio total (example)** | **~10ms** | |

**Procedure:** compute video total in ms at the actual show frame rate, compute audio total in ms, take the difference. If video lags audio (the common case, since video processing is frame-quantized and audio is not), set a program-audio delay equal to roughly the difference, then re-measure and adjust so the residual sits inside ITU-R BT.1359 tolerance (audio leads video by ≤15ms, or lags by ≤45ms) — center the residual near the middle of that window, not its edge, so downstream rounding or a device swap doesn't push it out of tolerance.

## Hot-backup vs. cold-backup decision table

| Path | Failure would be visible to audience? | Cutover time needed | Choice |
|---|---|---|---|
| Program audio (main PA feed) | Yes — immediate, obvious | <1 second | Hot: live redundant mixer/amp path, monitored continuously |
| Main video/IMAG feed | Yes — immediate, obvious | <1 second | Hot: pre-framed backup camera or source, live on a spare switcher input |
| Confidence monitor for presenter | No — presenter-facing only | Seconds acceptable | Cold acceptable: presenter can pause briefly without audience noticing |
| Recording/archival feed | No — not seen live | Minutes acceptable | Cold acceptable: gap can be patched in post if the live show wasn't affected |
| Secondary camera angle (b-roll) | Partial — noticed but not disruptive | Tens of seconds acceptable | Cold acceptable if primary angle unaffected |

**Rule of thumb:** anything the live audience would perceive as a failure in under 2 seconds needs a hot backup, verified with an actual cutover test during rehearsal, not inferred from "we have a spare in the case." Everything else can run cold to save setup time and gear.

## Show-file template (freeze before doors, one page)

```
<Event name / date> — Show File
RF: <mic labels> on <frequencies> — coordinated on site <date/time>, <IM-check result>. Local occupied channels: <list> (avoided).
Video chain: <source> → <switcher/config> → <scaler> → <display processor>. <N>-frame (<Xms>) accumulated latency at <fps>.
Audio: Program-audio delay set to <Xms> to compensate video latency. Residual lead/lag: <Xms> — within ITU-R BT.1359 tolerance.
Redundancy: <backup path> hot/cold-patched to <input>. Verified cutover time: <Xs> (tested <date/time>).
Frozen <time>, <X> min before <doors time>.
```
