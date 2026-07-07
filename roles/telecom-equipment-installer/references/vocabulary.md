# Vocabulary

Terms generalists conflate that a premise telecom technician keeps sharply separate, because the difference changes what's actually being measured or whose responsibility it is.

## Demarcation point vs. NID

The **demarcation point (demarc)** is the contractual/legal boundary where the carrier's network ownership ends and the customer's premise wiring begins. The **NID (network interface device)**, or smart jack, is the physical hardware installed at (or near) that point that the tech actually tests against. The demarc is a concept defined by tariff/regulation; the NID is the box you put a test set on.

**In use:** "The demarc is legally at the building entrance, but the NID's actually mounted in the IDF closet — that's where I'm running the loopback."

**Common misuse:** treating "the demarc" as if it were always a labeled physical point on the wall, when its exact location is a contractual fact that has to be confirmed, not assumed from where cabling happens to enter the building.

## Permanent link vs. channel

The **permanent link** is the fixed, in-wall cabling from one connector to another — no patch cords — capped at 90m under TIA-568. The **channel** is the permanent link plus the patch cords/equipment cords at both ends, capped at 100m total. A run can pass the 100m channel limit and still fail cert on the 90m permanent-link submaximum.

**In use:** "Channel's only 97m, but the permanent link alone is 92 — that's the number that's actually failing cert, not the total."

**Common misuse:** quoting "100 meters" as the single limit and never checking whether the permanent-link portion alone exceeds its own 90m cap.

## PSE vs. PD (in PoE)

The **PSE (power-sourcing equipment)** is the switch or midspan injector supplying power — rated by output wattage per port. The **PD (powered device)** is the phone, camera, or AP consuming it — rated by guaranteed minimum received power, which is always lower than the PSE's rated output because cable loss is built into the standard's math.

**In use:** "PSE's rated for 15.4W on this port, but the PD's only guaranteed 12.95W — the gap is the cabling loss the standard assumes."

**Common misuse:** treating the PSE's output wattage as what the device actually receives, ignoring voltage drop over the cable run.

## PoE class vs. PoE type

**Type** (802.3af/at/bt, or "Type 1–4") is the IEEE standard generation. **Class** (0–8) is the specific power tier negotiated within a type via LLDP or physical classification signaling. Two devices can be the same Type but different Class, with materially different power budgets.

**In use:** "Both are Type 2 ports, but this camera negotiates Class 4 at 25.5W while the AP next to it only pulls Class 3."

**Common misuse:** using "Type" and "Class" interchangeably, leading to a power budget calculated against the wrong tier.

## Jitter vs. latency

**Latency** is the one-way time a packet takes to arrive. **Jitter** is the variation in that arrival time between consecutive packets. A network can have low average latency and still have high jitter, and the two produce different call symptoms — latency causes delay, jitter causes garbled/robotic audio from jitter-buffer discards.

**In use:** "Latency's fine at 45ms — it's the 42ms of jitter that's causing the garbled audio, not the delay."

**Common misuse:** running a simple ping test, seeing a low average round-trip time, and concluding the network is fine for VoIP without separately checking jitter.

## MOS vs. R-factor (E-model)

**MOS (Mean Opinion Score)** is a 1–5 subjective quality rating, historically from human listening panels, now commonly estimated algorithmically from network metrics. **R-factor** (from the ITU-T E-model) is the underlying 0–100 computed score that MOS estimates are derived from, incorporating latency, jitter, loss, and codec choice together rather than as a single listening impression.

**In use:** "The phone's reporting an R-factor of 78, which maps to a MOS around 4.0 — acceptable, but check whether that was captured during the actual complaint window."

**Common misuse:** citing a MOS number without knowing whether it reflects the specific time window the customer is complaining about, or whether it's an estimate versus a listener-scored value.

## NEXT vs. attenuation (insertion loss)

**NEXT (near-end crosstalk)** measures interference one pair induces into another at the same end of the cable — usually a termination-quality issue. **Attenuation (insertion loss)** measures signal power lost traveling the length of the cable — a function of distance and cable quality. A run can fail one and pass the other, and the failure signature points at a different root cause each time.

**In use:** "It's failing NEXT, not attenuation — that's a termination problem at the jack, not a length problem."

**Common misuse:** treating any certification failure as "the cable is bad," when a NEXT-specific failure points at the termination, not the cable itself.

## SIP trunk vs. PRI

A **SIP trunk** delivers voice as packetized data over an IP/Ethernet handoff, typically from a hosted or cloud PBX. A **PRI (Primary Rate Interface)** delivers voice as 23 or 24 digital time-division-multiplexed channels over a T1, from a traditional on-premise PBX. They fail differently: SIP trunk problems show up as QoS metrics (jitter, loss); PRI problems show up as channel/D-channel sync or framing errors.

**In use:** "This building's still on a PRI, so a garbled-call complaint isn't a jitter problem — check D-channel sync and framing errors instead."

**Common misuse:** applying VoIP QoS troubleshooting (jitter, DSCP tagging) to a PRI circuit, which uses an entirely different fault model.

## Punch-down (110 block) vs. patch panel cross-connect

A **110-block punch-down** terminates individual conductors permanently into an insulation-displacement connector — part of the permanent link. A **patch-panel cross-connect** uses a modular jack-to-jack patch cord to make a temporary, re-arrangeable connection — part of the channel's patch-cord allowance, not the permanent link.

**In use:** "The punch-down at the 110 block is part of the permanent-link measurement — the patch cord from the panel to the switch is separate and comes out of the channel's cord budget."

**Common misuse:** counting a patch-panel cross-connect as if it were part of the permanent link, miscalculating how much length budget is actually left.

## Key system vs. PBX vs. hosted (cloud) PBX

A **key system** is a small, self-contained phone system with direct line appearances, minimal call routing intelligence, suited to a handful of lines. A **PBX (private branch exchange)** is on-premise call-routing hardware/software for larger deployments with extension dialing, trunking, and voicemail. A **hosted (cloud) PBX** moves that call-routing logic off-premise entirely, leaving only endpoints and network connectivity on site.

**In use:** "There's no PBX hardware to troubleshoot here — it's hosted, so the call-routing logic lives with the provider and our scope stops at the LAN handoff."

**Common misuse:** assuming there's an on-premise PBX to diagnose when the system is actually hosted, wasting time looking for hardware that doesn't exist on site.

## Smart jack (NIU) vs. dumb demarc

A **smart jack (network interface unit, NIU)** is an active, remotely testable device at the demarc that supports carrier-initiated loopback testing without a truck roll. A **dumb demarc** is a passive punch-down block or connector with no built-in test capability — verifying the carrier side requires a physical visit or a butt set at the block.

**In use:** "We've got a smart jack here, so the carrier can loop it remotely — no need to schedule a joint visit just to isolate the fault."

**Common misuse:** assuming every demarc supports a remote loopback test, when a dumb demarc requires physical access from both parties to isolate a fault.

## QoS tagging (DSCP/802.1p) vs. raw bandwidth

**QoS tagging** (DSCP in the IP header, 802.1p in the Ethernet frame) marks packets for priority handling so voice traffic is forwarded ahead of best-effort data during congestion. **Raw bandwidth** is simply the pipe's total capacity. A link can have abundant raw bandwidth and still degrade voice quality if tagging isn't applied or isn't honored by every switch in the path.

**In use:** "We've got plenty of bandwidth headroom — the problem is DSCP EF tags aren't being honored past the 3rd-floor switch, so voice is queuing behind data during the afternoon traffic peak."

**Common misuse:** treating a bandwidth upgrade as the fix for voice quality problems that are actually caused by missing or unhonored QoS tagging.
