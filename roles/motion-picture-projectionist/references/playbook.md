# Playbook

Filled checklists and worksheets a booth actually runs, with real target numbers. Adapt the specifics; keep the structure and thresholds.

## 1. Pre-show KDM and ingest checklist

Run 48–72 hours before any new title's first show, then re-verified the morning of. One row per title per auditorium.

| Title | Aud. | KDM valid from | KDM valid until | Server ID matches? | Ingest validated? | Notes |
|---|---|---|---|---|---|---|
| Feature A | 3 | Thu 00:01 | Sun 23:59 | Yes | Yes | Clean |
| Feature B | 5 | Fri 06:00 | Fri 23:00 | Yes | Yes | **Window closes before Sat 12:40 matinee — request extension today** |
| Feature C | 7 | — (not received) | — | — | No | **Missing KDM — escalate to distributor, do not schedule Sat AM show until confirmed** |

**Rule:** any KDM whose validity window closes within 48 hours of a scheduled showtime, or any title with no KDM on file 48 hours out, gets escalated to the distributor the same day — not the morning of the show. A replacement or extended KDM typically takes several hours to generate and deliver once requested; there is no same-minute fix once a window has actually closed.

**Server-ID mismatches** (KDM issued against a different server or IMB serial than what's installed, usually after hardware service) are the single most common reason a validated, ingested DCP still won't play — check this explicitly, don't assume "ingested" means "keyed correctly."

## 2. Pre-open calibration spot-check

Per auditorium, per format change (2D/3D, scope/flat, standard/HFR). Not a once-a-week task.

| Check | Target | Tool | Action if out of spec |
|---|---|---|---|
| Screen-center luminance, 2D | 14 fL ±3 fL (11–17 fL) | Photometer, feature test pattern | Below range: check lens/aperture cleanliness, lamp/laser hours, dimmer setting before assuming lamp failure |
| Screen-center luminance, 3D | ~4.5–7 fL | Photometer, 3D test pattern, glasses on | If 2D is in spec but 3D is low: suspect the 3D optical path (filter wheel, polarizer alignment, glasses batch), not the lamp |
| Sound level | Reference fader position (commonly "7.0" on cinema processors), calibrated to the room's X-curve target via C-weighted pink noise | SPL meter | Re-run calibration tone per channel; don't trust memory of "how loud it usually is" |
| Focus | Sharp at screen center and corners | Visual, test pattern with resolution wedge | Refocus; check for heat-related lens drift on long-throw setups |
| Framing/masking | Matches title's stated aspect ratio (commonly 1.85:1 flat or 2.39:1 scope) | Visual against masking edges | Reset masking preset — a leftover preset from the prior title in that slot is the most common cause |
| Frame rate | 24fps standard; 48fps/HFR only if the release is mastered for it | TMS/server playback settings | Verify against the distributor's technical notes, not assumption |

## 3. Physical print inspection worksheet (archival/festival/roadshow bookings)

Before threading any physical print, not after a jam mid-reel.

```
TITLE: ____________________   FORMAT: 35mm / 70mm   REELS RECEIVED: ___ of ___
Can label footage (per reel): ____________________________________
Actual measured footage:       ____________________________________
  → discrepancy over ~2% of stated footage = flag before threading, don't assume a counting error
SPLICE COUNT (per reel): _____   Condition: clean / lifting / brittle
PERFORATION DAMAGE: none / minor (isolated) / significant (recurring every reel)
  → significant damage = platter run NOT recommended; use interlocked changeover, lower tension
LEADER PRESENT: Academy leader / house leader / none — reattach before first run if missing
ASPECT RATIO STATED: ________   MASKING SET TO MATCH: yes / no
PRESENTATION METHOD: platter (continuous) / dual-projector changeover
  → default to changeover for fragile, nitrate-era, or heavily-spliced prints regardless of
    whether the booth normally runs platters
```

**Changeover cue reference** (Academy Leader standard, 1930): motor cue appears ~8 seconds before reel end (upper-right corner), changeover cue ~1 second before reel end — the second projector's motor should already be up to speed and threaded before the motor cue appears, not started at it.

## 4. Lamp and consumables threshold table

| Item | Typical rated life | Swap trigger | Notes |
|---|---|---|---|
| Xenon lamp (2–4kW, standard screen) | ~1,000–1,500 hrs | ~80% of rated hours, or before a known high-traffic block (opening weekend, holiday) | Degrading brightness and unreliable strike both increase past this point; don't wait for failure mid-show |
| Xenon lamp (6–7kW, large-format screen) | ~1,000–1,200 hrs | Same 80% rule, tighter margin given cost (~$1,200–2,000/lamp) | Log hours weekly, not only at swap time |
| Laser-phosphor illuminator | Rated in the tens of thousands of hours | Manufacturer service interval, not hour-triggered swap | Brightness drift is slower and more linear than xenon; still verify with photometer, don't assume "laser never dims" |
| Server storage (DCP library) | — | Plan ingest/purge cycle before storage drops under ~15% free | Ingesting a large title (HFR/HDR, multiple audio versions) with low headroom is a common cause of ingest failures |

## 5. Incident escalation note (filled template)

```
BOOTH INCIDENT — [Auditorium] — [Date/time]
SYMPTOM: ________________________________________________
SHOWTIME AT RISK: yes/no — minutes of buffer remaining: ____
DIAGNOSTIC STEPS TAKEN: _________________________________
ROOT CAUSE (if known) / LEADING HYPOTHESIS: ______________
IMMEDIATE ACTION: _______________________________________
FALLBACK PLAN IF NOT RESOLVED BY [time]: _________________
ESCALATION: vendor ticket # ____ / distributor contacted: y/n
```

The two fields most often skipped under pressure: **minutes of buffer remaining** (forces a real deadline instead of open-ended troubleshooting) and **fallback plan** (a pre-committed decision — reschedule, refund, format downgrade — instead of deciding it live in front of an impatient house manager).
