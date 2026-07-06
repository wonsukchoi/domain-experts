# Telecommunications Engineering Playbook

## Fiber link loss-budget calculation

Compute before committing to a fiber run, not after installation:

```
Loss budget (dB) = (fiber attenuation per km × distance in km)
                  + (connector loss × number of connectors)
                  + (splice loss × number of splices)
```

Typical component values (verify against actual cable/hardware spec sheets):

| Component | Single-mode | Multimode (OM4) |
|---|---|---|
| Attenuation | 0.35 dB/km (1310nm) | 3.0 dB/km (850nm) |
| Connector (per mated pair) | 0.3-0.5 dB | 0.3-0.5 dB |
| Fusion splice | 0.1 dB | 0.1-0.3 dB |
| Mechanical splice | 0.3 dB | 0.3-0.5 dB |

Worked calculation — single-mode run, 8km, 4 connector pairs, 2 fusion splices:

```
Attenuation:  0.35 dB/km × 8 km        = 2.8 dB
Connectors:   0.4 dB × 4 pairs         = 1.6 dB
Splices:      0.1 dB × 2               = 0.2 dB
------------------------------------------------
Total loss budget                      = 4.6 dB
```

Compare against the transceiver's specified power budget (e.g., a 10km single-mode SFP+ typically specifies ~6.0 dB link budget). **4.6 dB < 6.0 dB → link passes with 1.4 dB margin.** If the total exceeds the transceiver budget, reduce connector/splice count, use a higher-power optic, or shorten the path — don't rely on the cable's "max distance" spec sheet figure alone, since that figure assumes a specific, often lower, connector/splice count than the actual installed path.

## PBX/VoIP trunk sizing (Erlang B)

1. Pull busy-hour concurrent-call data from an existing comparable system's call detail records. If none exists, use a documented traffic study or an industry-typical call-per-extension assumption, and flag it as an assumption in the design doc.
2. Convert to offered traffic in Erlangs (busy-hour concurrent calls = the traffic intensity figure directly, if measured at true peak).
3. Apply Erlang B (via lookup table or the square-root safety-staffing approximation `n ≈ A + z√A`, z ≈ 2.33 for 1% blocking, z ≈ 1.65 for 5% blocking) to find required trunk count at the target blocking probability.
4. Add a growth headroom multiplier (commonly 15-25%, document the figure chosen and why).
5. Round up to the nearest whole-span increment (23 B-channels per PRI/T1, 30 per E1) and specify circuit count accordingly.

| Busy-hour concurrent calls (A) | Target blocking | Approx. trunks needed (z=2.33) | Spans (23ch PRI) |
|---|---|---|---|
| 10 | 1% | 10 + 2.33×3.16 ≈ 17 | 1 |
| 20 | 1% | 20 + 2.33×4.47 ≈ 30 | 2 |
| 34 | 1% | 34 + 2.33×5.83 ≈ 48 | 3 (with headroom) |
| 60 | 1% | 60 + 2.33×7.75 ≈ 78 | 4 |

## Carrier circuit provisioning checklist

Order sequencing — place in this order, on day 1 of the project:

1. **Confirm site serviceability** with the carrier (address-level check) before assuming any lead time figure.
2. **Place the order the same day** the site/service is confirmed — this is almost always the longest-lead item in the project.
3. **Get a written quoted turn-up date** and firm order/ticket number; track against every other project milestone from day one.
4. **Escalation fallback order** (use in this sequence if turn-up slips):
   - First: escalate via the account team using the order/ticket number with the specific missed date.
   - Second: request an interim/temporary circuit (e.g., a wireless failover link) if the slip threatens a hard go-live date.
   - Third: replan go-live date and communicate the new date with the carrier's revised commitment attached as evidence.

Typical lead times by circuit type (verify against the specific carrier's current quote — these vary by region and last-mile construction need):

| Circuit type | Typical lead time |
|---|---|
| Existing on-net building, no new construction | 10-15 business days |
| New construction, standard build | 30-45 business days |
| New construction, requiring permits/trenching | 60-90+ business days |

## Wireless/DAS coverage design

1. **Predictive RF survey**: model expected coverage using floor plan, wall material/attenuation (e.g., drywall ~3-4 dB, reinforced concrete ~12 dB, per-wall), and target signal strength (commonly -65 to -67 dBm for voice-grade Wi-Fi).
2. **AP placement** driven by the predictive model's coverage gaps, not a fixed grid or per-square-foot ratio.
3. **Post-install walk test**: physically measure signal strength and channel utilization at multiple points per area; compare against the predictive model.
4. **Remediation fallback order** if walk test reveals gaps: (a) adjust existing AP power/channel first, (b) add an AP at the specific measured gap location, (c) only as a last resort, relocate existing APs (highest labor cost).
