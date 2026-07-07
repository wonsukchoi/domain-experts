# Playbook

Filled procedures a chauffeur/shuttle driver actually runs, with real thresholds and worked numbers. Adapt the numbers to a specific property or account once actual history exists — these are the defaults to use before that history is built.

## 1. Multi-stop pickup schedule build

Run this before accepting or confirming any multi-passenger manifest with a hard external deadline (flight, meeting).

**Inputs:** stop list with passenger count per stop, luggage count per passenger, hard deadline, assigned vehicle's rated cargo volume.

**Steps, with a filled example (3-stop airport run, 6:00 AM curb target):**

1. **Luggage-vs-cargo check.** Budget 3.5 cubic feet per checked bag, 1.5 per carry-on/briefcase. Sum across all passengers and compare to the vehicle's cargo rating for its current seating configuration (not its nameplate class — a 3rd-row-up SUV can have less than half the cargo volume of the same model with the row folded).

   | Passenger | Checked bags | Carry-ons | Cubic ft needed |
   |---|---|---|---|
   | Hotel A – 1 pax | 1 | 1 | 5.0 |
   | Hotel B – 1 pax | 1 | 1 | 5.0 |
   | Hotel C – 2 pax | 2 | 2 | 10.0 |
   | **Total** | | | **20.0** |

   Vehicle assigned: Cadillac Escalade, 41 cu ft behind 3rd row. 20.0 ≤ 41 → clears with margin. If total exceeded ~80% of rated volume, flag for a larger vehicle or a second run rather than assume it fits.

2. **Per-stop boarding buffer.** Default 5 minutes for the first passenger at a stop with luggage, +2 minutes per additional passenger boarding at the same stop, unless the specific property's logged median differs.

   | Stop | Passengers | Buffer |
   |---|---|---|
   | Hotel A | 1 | 5 min |
   | Hotel B | 1 | 5 min |
   | Hotel C | 2 | 7 min |
   | **Stop total** | | **17 min** |

3. **Drive time.** Pull current GPS ETA for the full stop sequence (base → A → B → C → airport). Example: 38 minutes.

4. **Planned total** = stop buffers + drive time = 17 + 38 = 55 minutes.

5. **Contingency margin.** Add 10–15 minutes on top of the planned total for traffic variance and the one stop that historically runs long. Example: +15 min → **70 minutes total.**

6. **Departure time** = hard deadline − total, working backward. Example: 6:00 AM curb target − 70 min = **4:50 AM departure from base.**

**Output artifact — dispatch schedule line:**

> Run #4471 — Escalade — depart base 04:50 — Hotel A 04:58 (buffer to 05:03) — Hotel B 05:11 (buffer to 05:16) — Hotel C 05:24 (buffer to 05:31) — airport curb target 06:00 — contingency 15 min built in, 0 min spent at plan time.

## 2. Slack-burn tracking during execution

Track this live, stop by stop — not just at the final stop.

| After stop | Budgeted time to here | Actual time to here | Slack remaining (of 15-min contingency) |
|---|---|---|---|
| Hotel A | 13 min (5 buffer + drive segment) | 13 min | 15 min |
| Hotel B | 10 min stop-to-stop | 22 min (12 min late passenger) | 3 min |
| Hotel C | 7 min stop budget | 4 min (recovered via curbside handoff) | 6 min recovered back to ~6 min net |

**Rule:** the moment slack remaining drops below the time needed for all remaining stops plus remaining drive time, stop absorbing silently and act — recover time at the next stop (ask for curbside handoff instead of lobby wait), re-sequence if a later stop can tolerate more delay than an earlier one, or escalate to dispatch/client with a revised ETA before the deadline is missed.

## 3. Schedule-recovery decision when a passenger is late

1. **Get a real number, not a vibe.** Text/call: "how many minutes out are you?" Don't estimate from silence.
2. **Compare lateness to remaining slack**, not to how apologetic the passenger sounds.
   - Lateness ≤ remaining slack → absorb, continue, no escalation needed.
   - Lateness > remaining slack → move to step 3 immediately.
3. **Recover time from downstream stops before touching the deadline:** ask downstream passengers to be curbside with bags already down (typically claws back 2–4 minutes per stop), re-sequence stop order if a later passenger has more schedule flexibility than an earlier one, or split the manifest across two vehicles if one is available and the deadline is otherwise unrecoverable.
4. **Escalate to dispatch/client the moment the deadline is at risk**, with the specific number ("3 minutes of slack against 11 minutes of remaining stop-plus-drive time") — not after arrival, when nothing can be done except apologize.
5. **Apply the no-show/grace protocol only after recovery options are exhausted:** absent a specific contract term, 15 minutes grace for airport meet-and-greet pickups, 5–10 minutes for residential/office curbside. Past grace, follow the account's no-show billing terms and notify dispatch rather than holding the rest of the manifest hostage to one late passenger.

## 4. Confidentiality handling — the default posture

- **Default:** nothing seen or heard on a run is repeated to anyone — not the next client, not another driver, not casually to dispatch, not on social media, ever, regardless of how unremarkable it seemed.
- **Exception, and only this one:** a direct safety or legal-reporting obligation (e.g., a disclosed threat of harm). Even then, route it through company policy and a supervisor, not a personal decision to intervene or discuss.
- **Corporate accounts commonly carry an explicit NDA** binding the driver and the livery company; a disclosure that would otherwise be "just gossip" becomes a contract breach with financial exposure for the company, not only a service complaint.
- **Practical tell:** if repeating a detail would let anyone else identify who the passenger was, what they discussed, or where they were going beyond the manifest itself, it doesn't get repeated.

## 5. Defensive-driving following-distance table

| Condition | Following distance | Rationale |
|---|---|---|
| Daylight, dry, passenger alert/belted | 4 seconds | Wider than the generic 3-second solo rule — passenger isn't bracing for the road the way the driver is. |
| Night, or wet roads | 6 seconds | Reduced visibility/traction plus the same unbraced-passenger factor compounds. |
| VIP/protective detail, or passenger reclined/asleep/on a call | 6+ seconds | Sudden braking risks physical injury or a spilled drink/dropped device becoming the incident, not just the near-miss itself. |

Recompute after any hard-braking telematics event — a pattern of hard-braking events at normal following distances usually means the interval needs to widen for that driver's route or vehicle, not that the driver needs to be reminded once.
