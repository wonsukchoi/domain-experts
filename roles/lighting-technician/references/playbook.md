# Playbook

Worksheets a lighting technician actually fills out, with plausible numbers, before and during a gig. Starting points to adapt, not scripts.

## 1. Power load-calc and phase-balance worksheet

Run before hang day, once the plot and fixture inventory are final.

**Step 1 — connected load, by fixture type:**

| Fixture type | Qty | Watts ea. | Subtotal |
|---|---|---|---|
| Conventional (e.g., ETC Source Four, 750W) | 48 | 750W | 36,000W |
| LED moving fixture | 14 | 700W | 9,800W |
| **Total connected load** | | | **45,800W (45.8kW)** |

**Step 2 — service capacity check (informational only, not the real constraint):**

```
Service: 400A, 208Y/120V, 3-phase company switch
Capacity = √3 × V × I = 1.732 × 208 × 400 ≈ 144,107 VA (144.1kVA)
Connected load ÷ capacity = 45,800 / 144,107 ≈ 31.8%
```

A comfortable-looking percentage here proves nothing about any individual leg. Do not stop here.

**Step 3 — per-phase amperage, balanced:**

Target ≈ total load ÷ 3 per leg, then convert to amps at 120V phase-to-neutral, and check against 80% of the feeding breaker's rating (the continuous-load ceiling for a run over ~3 hours).

| Phase | Dimmers | Movers | Load | Amps (W÷120V) | % of 200A breaker | Under 160A (80%) ceiling? |
|---|---|---|---|---|---|---|
| A | 16 × 750W | 5 × 700W | 15,500W | 129.2A | 64.6% | Yes |
| B | 16 × 750W | 5 × 700W | 15,500W | 129.2A | 64.6% | Yes |
| C | 16 × 750W | 4 × 700W | 14,800W | 123.3A | 61.7% | Yes |

Reconciliation check: dimmers 16+16+16=48 ✓; movers 5+5+4=14 ✓; load 15,500+15,500+14,800=45,800W ✓ (matches Step 1 total).

**Rule of thumb:** if any single leg lands above 80% of its breaker rating, move whole fixture groups (not individual units) between legs until all three land within roughly 5% of each other — don't shave load off the worst leg by trimming the flattest fixture in the room, move a matched group so the design intent stays intact.

## 2. DMX universe-planning worksheet

**Step 1 — channel need per fixture class:**

| Fixture | Mode | Channels each | Qty | Total channels |
|---|---|---|---|---|
| Conventional dimmer | Single-channel dim | 1 | 48 | 48 |
| LED moving fixture | Extended (pan/tilt/color/gobo/etc.) | 36 | 14 | 504 |
| **Total** | | | | **552** |

552 exceeds one universe's 512-channel ceiling — split before patch day, not at the console on load-in morning.

**Step 2 — universe split (each fixture assigned to exactly one universe):**

| Universe | Dimmers | Movers | Channels used |
|---|---|---|---|
| 1 | 1–24 | 1–7 | 24 + (7×36=252) = 276 |
| 2 | 25–48 | 8–14 | 24 + (7×36=252) = 276 |

Reconciliation: 276 + 276 = 552 ✓ (matches Step 1 total); 24+24=48 dimmers ✓; 7+7=14 movers ✓.

**Rule of thumb:** default to splitting by *physical position* (e.g., all of one truss on Universe 1) rather than splitting a matched fixture group across universes — a group split across universes fails independently if one universe's Art-Net node drops, producing a half-dead effect instead of a clean fallback.

## 3. Rigging load worksheet

For every load-bearing point, before anything goes in the air:

| Point ID | Rated WLL (from venue grid plot) | Planned hung weight | Safety factor achieved | Sign-off |
|---|---|---|---|---|
| US truss, pt. 3 | 1,000 lb | 240 lb (6 movers × 40 lb) | 4.2:1 | Venue TD initialed |
| DS truss, pt. 7 | Not listed in grid plot | — | Unknown — treat as unrated | Escalate to venue TD/engineer before hanging |

**Rule of thumb:** entertainment rigging generally targets a safety factor of at least 5:1 (often higher, per ANSI E1.2 and house-specific engineering) between rated working load limit and actual applied load — never infer a point's rating from a visually similar point elsewhere on the same grid.

## 4. Focus session run sheet (filled example)

Run top-down, position by position, in the order the LD actually works — never fixture-to-fixture at random, which forces re-climbing.

```
FOCUS SESSION — [Show], [Date]
ORDER: (1) US truss general wash → (2) DS truss specials →
       (3) box booms → (4) movers/programmed positions
Per position, LD calls: channel #, intensity ref, focus note, color/gobo note.

Example log entries:
  Ch. 112 (US truss, SL wash) — full, tighten to actor's mark
    at DSC, hard edge upstage side, soft edge downstage.
  Ch. 214 (DS special) — 60%, narrow the iris two points,
    center on the table, no spill onto the backdrop.
  Ch. 301 (mover, US truss) — palette "Verse 1 wash," check
    gobo rotation direction matches the beat, not reversed.
```

**Rule of thumb:** log every note as it's given, in the fixture's own line — reconstructing focus notes from memory after the session is how a technician ends up patching against notes that don't match what's actually hung.

## 5. Strike checklist (reverse of load-in, not a fresh list)

```
1. Confirm show is fully closed (no hold for encore/re-light) before first cable pull.
2. Strike in reverse hang order: movers/specials down first (highest-value,
   most fragile), general wash last.
3. Coil and label cable by run (not just by type) — mislabeled multicable
   is next gig's power-balance problem.
4. Case fixtures against the packing manifest; flag any damage or lamp
   failure on the manifest itself, not verbally to the next crew.
5. De-rig points only after load confirms zero remaining weight — never
   drop a bridle with another point still loaded on the same batten.
6. Return distro boxes with breakers open, not just unplugged.
```

**Rule of thumb:** the fastest strike is the one that mirrors the load-in plan exactly — crews that strike "whatever's easiest to reach first" reliably lose track of which cable belongs to which circuit for the next load-in.
