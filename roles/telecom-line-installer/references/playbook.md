# Playbook

Filled worksheets for the four things that gate almost every outside-plant fiber job: calculating the loss budget before construction, checking joint-use pole clearance, tracking the make-ready timeline, and respecting bend-radius/splice-closure specs during install. Numbers below are industry-standard figures and worked examples, not universal constants — the pole owner's engineering table and the fiber manufacturer's datasheet always control over this worksheet for a specific job.

## 1. Loss budget worksheet

**Formula:** Total link loss (dB) = (fiber length in km × attenuation in dB/km) + (splice count × per-splice loss) + (connector mated-pair count × per-connector loss) + (splitter insertion loss, if present) + (any inline device loss, e.g. WDM filters). Compare the result against the transceiver class's rated optical budget and require at least 3dB of remaining margin, reserved for future splices, connector aging, and temperature-driven attenuation drift — not designed to the ceiling.

**Reference figures:**

| Component | Typical value | Notes |
|---|---|---|
| Singlemode fiber attenuation, 1310nm | 0.35 dB/km | ITU-T G.652 |
| Singlemode fiber attenuation, 1550nm | 0.21–0.25 dB/km | ITU-T G.652; lower loss than 1310nm, standard for longer PON feeder runs |
| Fusion splice loss, average | 0.02–0.05 dB | Modern fusion splicer with good cleave; re-splice above ~0.3dB (stated field heuristic, not a single universal standard) |
| Mechanical splice loss | ~0.3 dB | Higher and less consistent than fusion; used for emergency/temporary repairs, not new builds |
| Connector mated-pair loss, typical | 0.3 dB | Per Telcordia GR-326 typical performance |
| Connector mated-pair loss, ceiling | 0.5 dB | GR-326 acceptance ceiling for a single mated pair before rework |

**Splitter insertion loss by split ratio (industry-standard figures):**

| Split ratio | Insertion loss |
|---|---|
| 1:2 | 3.7 dB |
| 1:4 | 7.3 dB |
| 1:8 | 10.5 dB |
| 1:16 | 14.1 dB |
| 1:32 | 17.5 dB |
| 1:64 | 21.0 dB |

**GPON optical budget classes (ITU-T G.984.2):**

| Class | Usable range |
|---|---|
| B | 10–25 dB |
| B+ | 13–28 dB |
| C+ | 15–32 dB |

**Worked example — see SKILL.md** for the full 12km/1:32 GPON build (22.375dB calculated loss, 5.6dB margin against Class B+, 2.6dB margin against standard Class B — the reason to specify B+ optics on this build).

**Second worked example — point-to-point business fiber, no splitter.** 6km run, singlemode at 1310nm (0.35dB/km) = 2.1dB, 3 splices at 0.04dB average = 0.12dB, 2 connector pairs at 0.3dB = 0.6dB. Total = 2.82dB. Against a typical 1000BASE-LX optical budget of 7.5dB (transmit −9.5dBm minimum, receive sensitivity −20dBm, minus a 3dB safety allowance already built into the transceiver spec), margin = 7.5 − 2.82 = 4.68dB — well above the 3dB reserve, so this link tolerates a future re-splice or a moderately dirty connector without falling out of spec.

## 2. Joint-use pole clearance (communication worker safety zone)

Per NESC Rule 235, jointly-used poles reserve separate vertical zones for power space, an unoccupied safety buffer, and communication space. Commonly cited construction figures (confirm against the specific pole owner's engineering table, since exact values shift with voltage class, grounding scheme, and NESC edition):

| Supply voltage class | Minimum vertical separation, power space to communication space |
|---|---|
| 0–750V (secondary/service drop) | 30 in |
| 751V–8.7kV (primary distribution, grounded-neutral construction) | 40 in — the figure commonly called the "communication worker safety zone" |
| >8.7kV or non-grounded-neutral construction | Per pole owner's engineering table — often 60 in or more |

**Worked example.** A make-ready survey on a 12.47kV primary distribution line (751V–8.7kV class) finds an existing telecom attachment 38 inches below the lowest primary conductor — 2 inches inside the 40-inch minimum. The existing attacher must relocate down before any new attachment is authorized on that pole; the new attacher does not get to attach above the existing one and call the zone satisfied, since the violation is between the *lowest power conductor* and the *highest point of the communication space*, not between individual telecom attachments.

## 3. Make-ready timeline (FCC one-touch make-ready, orders under 300 poles)

1. **Application filed** with the pole owner, identifying the poles, requested attachment height, and whether the applicant intends to self-perform simple make-ready (one-touch) or have existing attachers perform their own.
2. **Survey window: 45 days** from a complete application for the pole owner (or its contractor) to complete a survey identifying required make-ready work and existing attacher relocations.
3. **Make-ready completion window: 60 days** from survey completion for existing attachers (or the new attacher, under one-touch make-ready, for simple/non-complex work) to complete required relocations.
4. **Total planning baseline: ~105 days** from application to attachment-ready, for an order under 300 poles in a state — larger orders are pro-rated by pole count under the FCC's rules.
5. **New attachment only after make-ready is confirmed complete** on every affected pole — attaching on a subset of poles while others are still pending relocation creates a mixed-compliance route that fails inspection pole-by-pole.

## 4. Bend radius and splice-closure procedure

**Bend radius convention** (confirm against the specific cable's datasheet — bend-insensitive fiber per ITU-T G.657 tolerates materially tighter radii than standard G.652 fiber):

| Condition | Typical minimum bend radius |
|---|---|
| At rest / storage (coiled slack, no tension) | ~10× cable outer diameter |
| Under installation tension (pulling, lashing) | ~20× cable outer diameter |

**Worked example.** A 12mm outer-diameter loose-tube outdoor cable is being coiled into a handhole for slack storage. At-rest minimum bend radius = 10 × 12mm = 120mm (~4.7 in). If the same cable is still under pulling tension when routed around a conduit sweep, the applicable minimum is 20 × 12mm = 240mm (~9.4 in) — using the at-rest figure while the cable is still under tension is a common shortcut that under-radii the bend by half.

**Splice closure sealing.** Closures rated per Telcordia GR-771-CORE must maintain their environmental seal (equivalent to an IP68-class submersion rating for buried/handhole closures) through repeated re-entry — not just at first close. Each re-entry: replace or re-activate the gel/gasket seal per the manufacturer's re-entry procedure, verify cable strain relief is intact, and confirm no bend-radius violation was introduced while routing slack back into the closure before final close-out.
