# Light Truck Driver — Playbook

Filled reference sequences: GVWR/GCWR threshold check, stop-count/time-budget check, proof-of-delivery classification, and telematics safety-score bands.

## 1. GVWR/GCWR threshold check (CDL vs. non-CDL CMV)

Two federal thresholds, not one — check both every time a vehicle or route reassignment changes the truck.

| Threshold | Rule | Trigger |
|---|---|---|
| 10,001 lb GVWR | Non-CDL commercial motor vehicle (49 CFR §390.5) | DOT medical certification, driver-qualification file, and (if interstate) HOS recordkeeping apply even without a CDL |
| 26,001 lb GVWR or GCWR (with a towed unit over 10,000 lb) | CDL required (49 CFR §383.5) | Vehicle cannot legally be operated by a non-CDL driver at this rating, regardless of how the load is distributed |

**Worked check A — route vehicle upgrade, stays non-CDL:**

```
Old vehicle: Ford Transit 250 cargo van, GVWR 9,070 lb        -> below 10,001 lb, no DOT medical/DQ file required
New vehicle: Freightliner MT45 box truck, GVWR 19,500 lb      -> crosses 10,001 lb, stays below 26,001 lb
Result: still non-CDL, but DOT medical certificate and driver-qualification file are now required before driving it
```

**Worked check B — route vehicle upgrade that crosses into CDL territory:**

```
Box truck GVWR                = 19,500 lb
Add pup trailer, GVWR         = 8,500 lb  (over the 10,000 lb towed-unit threshold that counts toward GCWR)
Combined GCWR                 = 19,500 + 8,500 = 28,000 lb
28,000 lb > 26,001 lb          -> CDL required; a non-CDL driver cannot legally take this combination
```

Rule: check the rating on the vehicle's certification/data plate, not the loaded weight on a given day — GVWR/GCWR is a fixed rating, not a live scale reading. A truck rated at 24,000 lb GVWR loaded to only 15,000 lb today is still a non-CDL vehicle that happens to be lightly loaded; a truck rated at 27,000 lb GVWR loaded to only 15,000 lb today still requires a CDL because the rating, not the current load, sets the requirement.

## 2. Stop-count / on-duty time-budget check

Match pace to route density, then recompute the budget every time stops are added or removed — don't treat the shift-start plan as fixed.

| Route density | Typical stops/hour | Typical min/stop (incl. drive-between) |
|---|---|---|
| Dense urban / multi-unit | 20–28 | 2.1–3.0 |
| Suburban residential | 15–20 | 3.0–4.0 |
| Rural / low-density | 6–10 | 6.0–10.0 |

**Worked check (matches SKILL.md example):** Suburban route, 172 stops at 3.2 min/stop, 10.0-hour (600-minute) on-duty budget.

```
Baseline route time     = 172 × 3.2 = 550.4 min
Buffer remaining        = 600.0 − 550.4 = 49.6 min
Added stops requested   = 40 × 3.2 = 128.0 min
Shortfall before shortcut = 128.0 − 49.6 = 78.4 min over budget
```

**If a shortcut is proposed** (e.g., skipping full GOAL checks on backing stops), compute its actual savings before accepting it as a fix, not just as a general sense that it will "help":

```
Backing stops on this route     = 52 (about 30% of 172)
Proposed time saved per stop    = 0.75 min (45 sec)
Total shortcut savings          = 52 × 0.75 = 39.0 min
Net shortfall after shortcut    = 78.4 − 39.0 = 39.4 min still over
```

A shortcut that closes less than the full gap is not a fix — it is unpaid risk taken for a schedule that still fails. The correct output of this check is a specific number handed back to dispatch, not a qualitative "I'll try."

## 3. Proof-of-delivery / signature-exception classification

| Package type | Delivery method required | Action if recipient unavailable |
|---|---|---|
| Standard, no signature flag | Release with geotagged delivery photo | Place at documented safe location, photo shows exact placement, log and continue |
| Signature required (no age restriction) | Any adult or resident signs | Attempt redelivery or hold at facility if no one signs; do not release-and-photo instead |
| Adult signature required (age-restricted, high-value) | Signer must show ID confirming 21+ (or 18+ per product) | Do not release without ID-verified signature under any circumstance; return to facility if unmet |
| Collect-on-delivery (COD) | Payment collected and signature captured together | Do not mark delivered without both; a photo alone does not satisfy a COD requirement |

Rule: scan-as-delivered happens only after the package is physically placed and (if required) the signature or ID check is complete — scanning first "to save time" converts an ordinary non-delivery dispute into a driver-attributable loss the moment a customer disputes receipt, because the scan record becomes evidence the package was placed when it may not have been.

## 4. Telematics safety-score bands and backing protocol

**GOAL (Get Out And Look)** sequence, every stop requiring a reverse maneuver:

1. Stop the vehicle before starting the reverse.
2. Exit and walk the intended path, checking for children, pets, low obstacles, and soft ground.
3. Re-enter and reverse slowly, covering the path just walked.
4. If the path is not fully visible from the mirrors at any point, stop and re-check rather than continuing on memory of the walk-through.

**Typical AI-dashcam / driving-score bands** (Netradyne/Mentor-style scoring, scale and thresholds vary by carrier program — confirm the exact bands with the specific fleet's scorecard):

| Band | Typical score range | Meaning |
|---|---|---|
| Fantastic/Great | 800–1000 (or top decile) | Few or no flagged events (hard brake, following distance, sign/signal, distraction) over the scoring window |
| Fair | 650–799 | Recurring minor events, usually tied to a specific pattern (late braking at one intersection type, following distance on highway segments) |
| Poor | Below 650 | Frequent events across multiple categories, typically correlated with schedule-pressure days or a specific route segment |

When a score decline coincides with a specific schedule-pressure period (an added-stop day, a compressed cutoff), pull the day-by-day event log rather than treating the average score as the diagnosis — the average hides which specific days or stops are driving it.
