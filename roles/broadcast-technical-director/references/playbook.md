# Playbook

Filled templates a technical director/ops manager actually runs. Adapt the specifics; keep the structure and thresholds.

## 1. Pre-air technical rehearsal (line-up) checklist

Run 60–90 minutes before any live broadcast with the full crew present, not a subset. A line-up that skips the failover exercise isn't a line-up, it's a hope.

```
SHOW: RSN — NBA regional telecast + post-game syndicated join
LINE-UP START: 6:00 pm   AIR: 7:30 pm

[ ] Genlock/PTP reference verified against network house clock — 0-frame offset
[ ] Timecode mode confirmed drop-frame, matched to network reference
[ ] All camera ISOs confirmed locked to house reference (not local free-run)
[ ] Router protect-path exercised LIVE — pull primary, confirm auto/manual
    failover completes within stated SLA (state the number; if none exists,
    that's a defect, not a pass)
[ ] PTP grandmaster failover exercised LIVE — force primary offline,
    confirm boundary clocks reacquire on backup grandmaster
[ ] Loudness spot-check on every pre-produced insert scheduled in the first
    hour (promos, sponsor reads) — not just the live mix
[ ] Closed-caption encoder confirmed passing through on both primary and
    protect paths
[ ] EAS encoder/decoder confirmed NOT scheduled to fire a Required Monthly
    Test during the broadcast window (see EAS calendar below)
[ ] Comms (intercom/IFB) checked to every position: TD, director, A1, A2,
    EVS, graphics, truck engineer, master control
[ ] Ad-avail cue points (SCTE-35) confirmed against network cue sheet,
    frame-accurate join tolerance stated (contract-specific — typically
    ≤2 frames before make-good liability applies)

DEFECT LOG (fill during line-up, do not wait until after):
  # | Found by | System | Description | Fix applied | Re-verified | Time
  1 | Eng #2   | Clock  | Free-run non-drop | Re-genlocked to PTP | Y | 7:02p
  2 | A1       | Audio  | Promo -16 LKFS  | Re-normalized       | Y | 7:20p

GO/NO-GO: recorded 45 min before air, signed by TD + Director of Engineering.
Showstopper defects (any one blocks air): no genlock, no redundant path
verified, EAS collision unresolved, caption encoder down on both paths.
Accepted-risk defects: logged, owner named, remediation date set.
```

## 2. Redundancy / failover runbook

State the posture explicitly per path — "we have a backup" is not a spec.

| Path | Redundancy posture | What it does NOT cover | Failover trigger | Failover action | Rehearsed? |
|---|---|---|---|---|---|
| Truck→facility video (ST 2110) | N+1 protect path, separate switch fabric | Shared fiber entrance into the building | Packet loss >1e-6 sustained 5s, or PTP offset outside spec sustained 5s | Router auto-switches; TD confirms on multiviewer | Y — 6:40p |
| PTP grandmaster | 2N — primary + independent backup grandmaster, different GPS antenna run | Shared building power (both on house UPS) | Loss of lock announcement from boundary clocks | Boundary clocks auto-reacquire backup GM; engineer confirms offset <spec | Y — 6:40p |
| Facility power | Utility + generator, UPS bridges the gap | Both feeds enter building through same conduit run | Utility loss detected | Generator auto-start; UPS bridges; confirm generator online before UPS depletes | Per NAB Engineering Handbook guidance — confirm bridge time covers generator start margin |
| Playout server (ad insertion) | N+1 hot standby, synced content | Shared SAN/storage backend | Health-check failure on primary | Auto-promote standby; verify content parity before promoting | Y — quarterly |

**Rule:** any path listed without a stated exclusion column gets one before it's signed off — the exclusion is usually where the next incident comes from.

## 3. EAS test-scheduling calendar

Required Monthly Test (RMT) and Required Weekly Test (RWT) obligations under 47 CFR Part 11 do not pause for live programming — the schedule has to move around the broadcast, not the reverse.

```
MONTH: scheduling window for RMT (odd months: 8:30am–local sunset;
        even months: local sunset–8:30am, per state EAS plan)

Live event calendar (from programming):
  Fri 7:30p–10:30p  NBA telecast + post-game (HIGH profile — no test)
  Sat 12:00p–3:00p  Regional college game (MED profile)
  Sun open           — RMT scheduled here, 2:00p, low-risk window

CHECK BEFORE FINALIZING:
[ ] RMT window does not overlap any live sports/news broadcast
[ ] RMT window confirmed against state EAS plan required time-of-day band
[ ] Test logged in EAS log per §11.61/§11.55 retention requirement
[ ] Master control watch-standers briefed on exact test time (a real alert
    arriving during a scheduled test must not be dismissed as the test)
```

## 4. Master-control shift-handoff log

Every shift change is a chance for tribal knowledge to evaporate. Handoff is written, not verbal-only.

```
SHIFT HANDOFF — Master Control, 11:00p–7:00a → 7:00a–3:00p

OPEN DEFECTS CARRIED FORWARD:
- Router protect-path #2: showed 1 transient packet-loss event at 2:14a,
  cleared in <1s, no on-air impact. Vendor ticket #4471 opened, monitoring.

SCHEDULED EVENTS THIS SHIFT:
- 9:00a RWT (Required Weekly Test) — routine, no live conflict
- 1:00p Satellite uplink window for affiliate feed swap — engineer on site

EQUIPMENT STATE:
- PTP grandmaster A primary, B standby — both nominal, offset <5µs
- Generator fuel: 85%, last load-test 14 days ago (30-day cycle)

WATCH FOR:
- Vendor ticket #4471 — if packet loss recurs, treat as pattern not
  isolated event; consider proactive failover to path #1 before next
  live show at 7:30p.
```

## 5. Incident report template (filled example)

Written before the next show airs, not "when there's time."

```
INCIDENT REPORT — RSN Master Control

DATE/TIME: [date], 8:47p (2nd quarter, live NBA telecast)
DURATION ON AIR: 4 frames visible glitch (~133ms at 29.97fps)
DETECTED BY: TD, confirmed by multiviewer alarm 1s later

WHAT HAPPENED: Primary ST 2110 video path packet loss exceeded the 5s
sustained threshold at 8:47:02p. Auto-failover to protect path completed
in 6 frames (~200ms) — 4 of those frames were visible on air as a
freeze before the protect path locked in.

ROOT CAUSE: Failover trigger threshold (packet loss >1e-6 sustained 5s)
correctly fired, but router protect-path re-acquisition time (200ms)
exceeds what's visually undetectable (<2 frames, ~67ms) at this codec/
GOP structure. The rehearsal on [date] tested the trigger logic but not
the acquisition-time-under-load — a gap in the rehearsal script, not a
new equipment fault.

FIX (not "be more careful"):
1. Reduce protect-path acquisition time via pre-warmed decoder buffer
   (vendor config change, ticket #4502) — target <2 frames.
2. Add acquisition-time measurement to the standard rehearsal checklist
   (Section 1 above) — verified, not just triggered.
3. Until #1 is confirmed, treat any packet-loss event as a candidate for
   manual pre-emptive failover at the 2-3s mark rather than waiting the
   full 5s threshold.

SIGNED: TD + Director of Engineering, reviewed within 48 hours.
```
