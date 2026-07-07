# Playbook

Filled procedures, not descriptions of procedures. Use these as the executable sequence for the three jobs that make up most service calls: balance/spring diagnosis, cycle-life spring sizing, and entrapment-protection verification.

## 1. Balance test and wind-count procedure

**Step 1 — disconnect the opener.** Pull the release cord/lever so the door is running on the spring system alone. Skipping this step is the single most common reason a spring problem gets misdiagnosed as an opener problem.

**Step 2 — lift the door by hand to roughly half-open and let go.**

| Observed behavior | Read |
|---|---|
| Stays within ~1–2 in. of release point | Balanced — proceed to whatever the actual complaint was |
| Drops toward closed | Springs weak, under-wound, or one broken — do not operate the opener until corrected |
| Rises toward open on its own | Springs over-wound — reduce turns before returning to service |

**Step 3 — identify the spring(s).** Record: wind direction (left/right-wound, by coil direction at the winding cone), wire diameter (measure 10 coils and divide, or use a wire gauge), inside diameter, and overall wound length. A replacement spring one wire gauge off delivers meaningfully different torque per turn even at the same wind count — order by these four numbers, not by "looks about the same size."

**Step 4 — set wind count from the manufacturer's chart** for that drum diameter and door weight (a 4 in. drum and a 12.5 in. drum need different turn counts to deliver the same lift on the same door — always confirm drum diameter before winding, never assume a standard size). Typical residential 7 ft door: winding in the 7–8 full-turn range is common on a standard 4 in. drum, but the chart for the specific spring/drum combination on the job governs, not this range.

**Step 5 — wind using two properly sized winding bars** seated fully in the cone's bar holes, one bar always fully seated while the other repositions, door secured with a vise-grip/C-clamp on the track so it cannot travel unexpectedly. Never substitute a screwdriver, single bar, or power tool for hand-winding.

**Step 6 — re-run the balance test** after winding and after reconnecting the opener. Confirm door holds at quarter, half, and three-quarter open before calling the job complete.

## 2. Cycle-life spring sizing worksheet

Use whenever a door's estimated or measured usage exceeds roughly 10 cycles/day (most commercial, some high-traffic residential — multi-unit shared garages, frequently-used side/service doors).

```
Step A — cycles/day:        [pull from access log, opener cycle counter, or facility interview]
Step B — operating days/yr: [ask; a 5-day warehouse ≈ 250-260, a 7-day dock ≈ 300-365]
Step C — cycles/year = A × B
Step D — rated life (years) = spring's rated cycle count ÷ C
Step E — cost/event = parts + labor + downtime estimate
Step F — annualized cost = cost/event ÷ D  (or, for run-to-failure planning: events/yr = C ÷ rated cycles; annual cost = events/yr × cost/event)
```

**Filled example — retail loading dock, single door:**

| Input | Value |
|---|---|
| Cycles/day | 22 |
| Operating days/yr | 310 |
| Cycles/year (C) | 6,820 |
| Standard spring rated cycles | 10,000 |
| Standard spring life (D) | 10,000 ÷ 6,820 ≈ 1.47 yr |
| High-cycle spring rated cycles | 50,000 |
| High-cycle spring life | 50,000 ÷ 6,820 ≈ 7.33 yr |
| Cost/event (parts + labor + downtime) | $410 |
| Standard-spring annualized cost | $410 ÷ 1.47 ≈ $279/yr |
| High-cycle upcharge (one-time) | $130 |
| High-cycle annualized cost over its 7.33-yr life | $130 ÷ 7.33 ≈ $18/yr |

**Recommendation threshold:** when the standard-duty annualized cost exceeds roughly 3–4x the high-cycle upcharge annualized over its own rated life (as above: $279/yr vs. $18/yr, a >15x gap), the high-cycle spring is the correct default quote, not an upsell. Below roughly 10 cycles/day, standard-duty hardware annualizes cheaper and the high-cycle spring is the overcorrection to avoid.

## 3. UL 325 entrapment-protection verification (automatic operators)

Run this on every automatic-operator service call, regardless of the stated complaint.

**Step 1 — confirm two independent entrapment-protection means are present and functioning:**
- **Monitored photo-eye (Type 1):** mounted no higher than about 6 in. above the floor on both jambs, aligned so the beam is unbroken with the door fully open, sending diode and receiver both lit/steady. A flickering or intermittently-tripping indicator light is a fault, not a nuisance — treat it as "protection not confirmed," not "probably fine."
- **Inherent (force/motor-current) sensing (Type 2):** built into the opener; verify by placing an approved test object (or a 2×4 laid flat) in the door's closing path and confirming the door reverses within about 2 seconds of contact, without the object being crushed.

**Step 2 — measure reversal force with a gauge**, not by feel. If the force required to trigger a reversal has been increased at any point (check adjustment screw wear/position, ask the customer if reversals were "tuned out"), reduce it back to the setting that reverses on the standard test object before returning the door to service.

**Step 3 — log the verification** (pass/fail, force reading, photo-eye alignment) on the service ticket. If either system fails and cannot be corrected same-visit, the door goes back into service on manual-only operation, opener disabled, not "monitor it and see."

## 4. Cable and track quick-check (run after any spring work)

- Cable frayed, kinked, or off the drum at either end → replace cable pair (both sides), don't spot-repair one.
- Vertical track plumb checked with a level over its full height: out by more than roughly 1/4 in. → correct alignment before returning door to service; uncorrected out-of-plumb track reloads the new spring asymmetrically and shortens its life regardless of correct sizing.
- Rollers binding or showing flat spots → replace as a set per side, since one worn roller usually means its neighbors are close behind on the same wear curve.
