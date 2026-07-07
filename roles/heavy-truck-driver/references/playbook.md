# Heavy Truck Driver — Playbook

Filled reference sequences: HOS clock check, cargo-securement WLL calculation, pre-trip defect classification, and ELD malfunction handling.

## 1. Hours of Service clock check

Run all three before accepting or continuing toward a delivery commitment — don't stop at whichever clock looks most permissive.

| Clock | Rule | How to check |
|---|---|---|
| 11-hour driving | Max 11 hours of driving after 10 consecutive hours off duty | ELD cumulative driving-time total since last qualifying off-duty/sleeper period |
| 14-hour window | Max 14 hours on duty (driving or not) from first duty status change after the 10-hour break; driving not allowed past hour 14 even if driving hours remain | ELD on-duty start timestamp + 14 hours |
| 30-minute break | Required after 8 cumulative hours of driving since the last off-duty/sleeper/non-driving break of 30+ consecutive minutes | ELD driving-time-since-last-break counter |
| 60-hour/7-day or 70-hour/8-day | Cumulative on-duty (driving + non-driving) hours over a rolling 7 or 8 days, carrier-dependent | ELD cumulative on-duty total; plan a 34-hour restart before hitting the ceiling, not after |

**Worked check (matches SKILL.md example):** On-duty since 05:00, cumulative driving 7.75 hr by 12:30, no qualifying break taken yet.

```
11-hour clock remaining   = 11.00 − 7.75 = 3.25 hr
14-hour window remaining  = 14.00 − 7.50 = 6.50 hr   (on-duty time, not driving time)
Binding clock             = min(3.25 hr driving, 6.50 hr window) = 3.25 hr
Max further distance      = 3.25 hr × 52 mph = 169 mi
```

Always take the driving-clock distance as the ceiling, not the window — the window is longer because it includes non-driving on-duty time already spent (loading, fueling, inspection), which doesn't consume the 11-hour clock but also doesn't buy back driving hours.

**Adverse driving conditions exception:** extends the 11-hour driving limit and 14-hour window by up to 2 hours if conditions (snow, fog, unusual traffic from an accident) were unknown at dispatch time. Must be noted in the log at the time, not added retroactively after running long.

**Short-haul exception (150 air-mile radius):** CDL drivers returning to the work-reporting location within 150 air miles get a 14-hour (not extended) duty-period exception from full ELD/logging detail, but the 11-hour driving and 30-minute break rules still apply in full.

## 2. Cargo securement — working load limit calculation

Two independent checks; use whichever produces the higher tiedown count.

**Check A — aggregate WLL vs. cargo weight (49 CFR §393.106):**

```
Required aggregate WLL = cargo weight × 0.50
```

Example: 42,000 lb steel coil load.

```
Required aggregate WLL = 42,000 × 0.50 = 21,000 lb
Chain rated WLL         = 5,400 lb per chain (4-inch grade 70)
Chains needed           = 21,000 ÷ 5,400 = 3.9 → round up to 4 chains
Aggregate WLL provided  = 4 × 5,400 = 21,600 lb  (≥ 21,000 required — passes)
```

**Check B — minimum tiedown count by article length (49 CFR §393.106 Table 1, general-freight rule):**

| Article length | Minimum tiedowns |
|---|---|
| ≤ 5 ft, ≤ 1,100 lb | 1 |
| ≤ 5 ft, > 1,100 lb, or 5–10 ft | 2 |
| > 10 ft | 2 for first 10 ft, plus 1 per additional 10 ft or fraction |

Example: same load on a 48-ft flatbed article.

```
Base                = 2 (first 10 ft)
Additional segments = (48 − 10) ÷ 10 = 3.8 → round up to 4
Minimum tiedowns    = 2 + 4 = 6
```

**Reconcile:** Check A says 4 chains suffice by weight; Check B requires 6 by length. Use 6 — the higher of the two — and confirm the 6-chain aggregate WLL (6 × 5,400 = 32,400 lb) still clears the 21,000 lb weight requirement with margin.

## 3. Pre-trip inspection sequence and defect classification

Fixed order, every time — not read off a laminated card mid-walk:

1. Engine compartment (fluid levels, belts, hoses, leaks, mounts)
2. Cab/controls (gauges, mirrors, horn, wipers, seatbelt, steering play)
3. Lights and reflectors (all required lamps functional, reflective tape condition)
4. Walk-around (tires, wheels/rims, suspension, frame, fuel tank, mud flaps)
5. Brakes (pushrod stroke where accessible, air system build-time and leak-down, low-air warning)
6. Coupling (fifth wheel lock, kingpin, glad-hands, safety chains/cables, landing gear)

| Defect example | Classification | Action |
|---|---|---|
| Steer tire tread below 4/32 in | Out-of-service | Do not depart — replace or swap unit |
| Any required lamp inoperative (brake, turn, tail) | Out-of-service | Do not depart — repair before moving |
| Cracked but non-structural mud flap | Minor | Note on DVIR, depart, repair at next scheduled stop |
| Pushrod stroke past CVSA chamber-type limit | Out-of-service | Do not depart — same threshold table used on the repair side |
| Low washer fluid | Minor | Note on DVIR, top off when convenient |
| Air system fails to build from 85 to 100 psi within ~3 minutes | Out-of-service (functional brake system defect) | Do not depart — diagnose compressor/dryer/governor before moving |

Rule: an out-of-service item stops the truck from legally leaving the yard regardless of appointment time — there is no "write it up and go anyway" option.

## 4. ELD malfunction / diagnostic event handling

| Code type | Meaning | Required action |
|---|---|---|
| Data diagnostic event (e.g., missing required data, power data diagnostic) | ELD flags a data-quality issue, not necessarily a malfunction | Note the event; continue electronic logging if the device is otherwise functional |
| Malfunction (e.g., power compliance, engine synchronization compliance, timing compliance, positioning compliance, data recording compliance, data transfer compliance) | Device can no longer reliably certify compliant records | Switch to paper logs (or ELD-provided backup) immediately; notify carrier within 24 hours |
| Uncorrected malfunction past 8 days | Device not repaired, replaced, or serviced within the mandatory window | Continued reliance on it is itself a violation — carrier must provide a compliant device or driver reconstructs logs manually until resolved |

Reconstruct paper logs for the current 24-hour period plus the previous 7 days on request from an inspector during an active malfunction — that reconstruction, not the malfunctioning device, is what an inspector checks against.
