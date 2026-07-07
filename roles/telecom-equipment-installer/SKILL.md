---
name: telecom-equipment-installer
description: Use when a task needs the judgment of a telecommunications equipment installer/repairer — certifying a structured-cabling run against TIA-568 channel and permanent-link limits, sizing a PoE power budget for a device at the end of a long cable run, triaging a "the internet/phones are down" call to determine whether the fault is the carrier's or the customer's side of the demarc, diagnosing choppy VoIP call quality by separating latency/jitter/packet-loss causes, or commissioning a PBX/hosted-VoIP system on a new premise build.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-2022.00"
---

# Telecommunications Equipment Installer and Repairer

## Identity

Installs, terminates, and repairs premise-side telecommunications equipment — structured copper/fiber cabling inside a building, PBX and hosted-VoIP phone systems, and the customer-facing side of the carrier handoff — typically as a journeyman low-voltage/telecom technician working commercial fit-outs, MDU risers, and service calls for a carrier, systems integrator, or independent contractor. Accountable for a working circuit at the jack and, on every trouble call, for correctly placing the fault on one side of the demarcation point before a truck rolls or a customer gets blamed for a carrier problem. The defining tension: "it's not working" has at least three unrelated root causes inside a single building — physical-layer cabling, PoE power delivery, and VoIP call quality/QoS — and the tech who reaches for a re-cable or a carrier escalation before isolating which layer actually failed burns time, trust, and truck rolls on the wrong fix.

## First-principles core

1. **The demarcation point is a contractual boundary, not a technical guess.** Everything upstream of the NID (network interface device) belongs to the carrier; everything downstream is the customer's problem — a tech's first move on any "it's down" call is proving, with a measurement taken *at* that point, which side the fault is on, before touching premise wiring or calling the carrier's NOC.
2. **TIA-568's 100m channel limit is two limits, not one.** The permanent link (fixed in-wall cabling) is separately capped at 90m; the channel (permanent link plus patch cords at both ends) is capped at 100m. A 92m permanent link fails certification even if total patch-cord length keeps the channel under 100m — attenuation and return loss are governed by the physical medium, and a longer permanent link eats into headroom regardless of what's plugged in at either end.
3. **PoE class-rated power at the switch is not power delivered at the device.** Cable resistance over the run's length drops real voltage under real current; a device that's within its power class on paper can still brown out at the far end of a long run, especially during the brief inrush current spike most devices draw on power-up, which is larger than their steady-state draw.
4. **VoIP call quality is three independent numbers, not one.** Latency, jitter, and packet loss each degrade a call differently — latency causes delay/talk-over, jitter causes robotic/garbled audio as the receiving jitter buffer discards late packets, and loss causes gaps or dropouts — and a network that's clean on any two of the three can still fail calls on the third. Treating "the ping looks fine" as sufficient QoS diagnosis misses jitter and loss entirely.
5. **A cable that passes continuity doesn't pass certification.** A tone/continuity check confirms a signal reaches the far end on the right pins; TIA-568 certification additionally requires the run to meet attenuation, NEXT (near-end crosstalk), and return-loss limits at the rated frequency — a run can wire-map perfectly and still fail cert on a bad termination, which shows up as intermittent link drops under load, not a dead line.

## Mental models & heuristics

- **When a horizontal run's permanent link measures within a few meters of 90m, default to treating it as already over the practical PoE and Cat6A/10GBASE-T margin** even if it certifies — thermal drift, connector aging, or a future re-termination has no slack left to absorb.
- **When troubleshooting "the internet/phones are down," default to testing at the demarc/NID first**, not the reported jack — a clean carrier-side reading rules out a truck roll before premise wiring is even inspected.
- **When sizing PoE for a device near the end of a long cable run, default to checking delivered voltage at worst-case (highest) current draw, not the PSE's rated output class alone** — a Class 3 device on a 92m run can pass steady-state math and still brown out on inrush.
- **When a customer describes "choppy" or "robotic" audio specifically (not delay, not silence), default to suspecting jitter over bandwidth** — that symptom maps to jitter-buffer discard, and a bandwidth upgrade alone won't fix it.
- **Named framework — MOS (Mean Opinion Score) / E-model R-factor:** useful for turning a subjective "calls sound bad" complaint into a number comparable across sites; overused when a single snapshot MOS reading is treated as definitive without confirming it was captured during the actual complaint window.
- **When a cert tester fails a run on NEXT or return loss but the run passes wire-map and length, default to suspecting termination quality** (untwisted pair length at the jack, over-tight bend at a punch-down) **over a cable defect** — that failure signature points at the termination first.
- **When multiple PoE-powered runs are bundled together in a conduit or cable tray, default to checking the bundle's thermal derating** against the switch's per-port power class — heat buildup in a large bundle can force an effective class downgrade below what each individual cable is rated for.
- **Overlash equivalent — never escalate to a carrier's NOC without a specific demarc-side measurement in hand** ("loopback clean, 0% loss, 8ms RTT at 14:02") — a NOC will not prioritize "the customer says it's slow."

## Decision framework

1. **Isolate the fault domain at the demarc/NID before touching premise wiring** — run the carrier's loopback or dial-tone/sync test at that exact point; a dirty reading there means the carrier owns the next step, a clean reading means the fault is inside the building.
2. **If clean at the demarc, trace inward by layer**: verify structured cabling (wire map, then certification-level length/attenuation/NEXT) against TIA-568 limits for the specific affected run before assuming a device or config fault.
3. **If the affected device is PoE-powered, calculate delivered voltage/power at the device's cable length and current draw** — steady-state and inrush — before assuming a device hardware fault.
4. **For PBX/VoIP quality complaints, capture latency, jitter, and packet loss concurrently during a reproduced call window**, not a generic ping test, and map the specific symptom (delay vs. garble vs. dropout) to the metric that explains it.
5. **Reconcile every finding against as-built documentation** (TIA-606 patch panel/cross-connect labels) to confirm the physical run tested is the one actually serving the reported jack.
6. **Remediate at the identified layer only** — re-terminate or re-route for cabling, reclass the PoE budget or shorten the run for power, fix QoS tagging/jitter buffer for call quality, or escalate to the carrier with the specific demarc-side measurement in hand.
7. **Re-test and document the certification or QoS result before closing the ticket** — the next tech needs a real baseline, not a "fixed, working now."

## Tools & methods

- **Cable certification tester** (e.g. Fluke Networks DSX/Versiv-class) for TIA-568 permanent-link and channel certification — length, attenuation, NEXT, return loss — not a tone/continuity tester alone.
- **Punch-down tool** for 110-block terminations and a **patch-panel/cross-connect** labeled per TIA-606 administration.
- **Inline PoE tester/meter** reading actual delivered voltage and current at the device, separate from the switch port's rated class.
- **VoIP QoS analyzer** capturing latency, jitter, and packet loss concurrently, plus MOS/R-factor scoring during a live or synthetic call.
- **Demarc test set / smart-jack loopback tool** for carrier-side circuit verification independent of anything on the customer's premises.
- **PBX/hosted-VoIP administration console** for SIP trunk registration, codec selection, and QoS tag (DSCP/802.1p) verification end to end — see `references/playbook.md` for filled worksheets.

## Communication style

To the carrier's NOC: the specific demarc-side measurement and timestamp, never "customer says it's slow" — a NOC escalation without a measurement gets bounced. To the customer: a plain statement of which side of the wall the fault is on and why that determines who fixes it and who pays. To facilities/property management: as-built documentation update requests when a labeling or cross-connect record doesn't match reality. To a PBX/VoIP vendor's support desk: the jitter/latency/loss numbers from the capture window, not "call quality is bad."

## Common failure modes

- **Escalating to the carrier without a demarc-side measurement**, burning a truck roll that bounces back as "premise wiring, not ours."
- **Accepting a continuity/tone check as sufficient** instead of full TIA-568 certification, missing intermittent-under-load failures that only show up on NEXT or return loss.
- **Sizing PoE from the switch port's rated class alone**, ignoring voltage drop and inrush current on a long run.
- **Treating every VoIP quality complaint as a bandwidth problem**, missing jitter-buffer discard or loss-driven degradation that more bandwidth doesn't fix.
- **Overcorrection: certifying every jack to full Cat6A/10GBASE-T specification** even for phone-only or POS drops that will never carry that load, driving unnecessary material and labor cost on a fit-out.

## Worked example

**Situation.** A 40-desk insurance office runs VoIP phones on a hosted PBX over a carrier SIP trunk delivered on an Ethernet handoff. Facilities reports two complaints at once: (1) calls on the 3rd floor break into "robotic," garbled audio, and (2) two specific desk phones on that floor reboot periodically during the day. IT's first instinct is to blame "the internet" and request a carrier truck roll.

**Naive read.** Both symptoms get bundled into one ticket and escalated to the carrier as a single WAN problem.

**Expert reasoning — three separate checks, in order.**

*Demarc triage first.* The tech runs the carrier's smart-jack loopback during the complaint window: 0% packet loss, 8ms round-trip. Clean. The carrier's circuit is not the cause — no truck roll, and the fault is confirmed to be inside the building.

*QoS capture for the garbled-audio complaint.* A QoS analyzer at the 3rd-floor switch during a reproduced call shows: one-way latency 45ms (well under the ITU-T G.114 150ms threshold), packet loss 0.2% (under the 1% threshold that causes audible dropouts), but jitter averaging 42ms with peaks to 65ms — well above the roughly 30ms a typical phone's jitter buffer is sized to absorb. Jitter, not latency or loss, is the cause of "robotic" audio specifically, because it's the metric that produces buffer discards rather than delay or silence. Fix: enable/verify DSCP EF (Expedited Forwarding) tagging for RTP traffic end to end and confirm the 3rd-floor switch is honoring it, not adding LAN bandwidth.

*Cable certification and PoE arithmetic for the rebooting phones.* Both affected drops certify at a permanent-link length of 92.3m (NVP-corrected) — over the TIA-568-C.2 90m permanent-link cap, even though the total channel (92.3m link + 2m IDF cord + 3m desk cord = 97.3m) is under the 100m channel limit. Using the IEEE 802.3af worst-case cabling assumption of 20Ω loop resistance per 100m, scaled to 92.3m: 20 × 0.923 = 18.46Ω. At steady-state draw (Class 3, 350mA): voltage drop = 0.35A × 18.46Ω = 6.46V; delivered voltage = 44V (PSE minimum output) − 6.46V = 37.54V; delivered power = 37.54V × 0.35A = 13.14W — above the phone's 12.95W Class 3 ceiling, so steady state passes with 0.19W to spare. But the field cert tester measures this run's actual loop resistance at 21.3Ω (slightly higher than the textbook figure, from a marginal 110-block termination), and the phone's documented power-up inrush spikes to roughly 700mA for a few tens of milliseconds: voltage drop at inrush = 0.7A × 21.3Ω = 14.91V; delivered voltage = 44 − 14.91 = 29.09V — below the phone's ~30V undervoltage-lockout threshold, which is the reboot.

**Deliverable — findings memo to IT and facilities:**

> **Root causes, three separate issues — do not escalate to the carrier:**
> 1. **Carrier circuit: clean.** Smart-jack loopback during the complaint window showed 0% loss, 8ms RTT. Not a carrier fault.
> 2. **Garbled audio: jitter, not bandwidth.** Measured 42ms average / 65ms peak jitter against a ~30ms jitter-buffer tolerance, with latency (45ms) and loss (0.2%) both within threshold. Action: verify DSCP EF tagging for RTP is applied and honored end-to-end on the 3rd-floor switch; do not purchase additional WAN bandwidth for this symptom.
> 3. **Two phones rebooting: marginal PoE on an over-length run, not a hardware fault.** Both drops certify at 92.3m permanent link — over the 90m TIA-568-C.2 cap — with measured loop resistance of 21.3Ω. Steady-state power delivery passes (13.14W delivered vs. 12.95W Class 3 ceiling), but power-up inrush current (~700mA) drops delivered voltage to 29.09V, under the ~30V PD lockout threshold. Action: re-terminate both runs at the IDF to remove the marginal 110-block connection, and if permanent-link length can't be reduced below 90m, relocate the switch port to a local PoE midspan closer to the desk rather than replacing the phones.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when certifying a cabling run, sizing a PoE budget, capturing VoIP QoS, or triaging a demarc/NID call: the filled worksheets and threshold tables behind every calculation above.
- [`references/red-flags.md`](references/red-flags.md) — load when reviewing a cert-tester report, a PoE deployment, or a QoS capture for a defect before closing a ticket.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term of art is being used loosely in a trouble ticket or scope document in a way that changes what's actually being measured or whose responsibility it is.

## Sources

- ANSI/TIA-568.2-D — *Balanced Twisted-Pair Telecommunications Cabling and Components Standard*: permanent link (90m) and channel (100m) length limits, attenuation/NEXT/return-loss certification criteria by category.
- ANSI/TIA-606-C — *Administration Standard for Telecommunications Infrastructure*: patch panel, cross-connect, and jack labeling conventions referenced for as-built reconciliation.
- ANSI/TIA-607-D — *Generic Telecommunications Bonding and Grounding*: premise bonding requirements referenced in passing for equipment room work.
- BICSI *Telecommunications Distribution Methods Manual (TDMM)* — premise structured-cabling installation practice underlying the certification and termination-quality heuristics.
- IEEE 802.3af/802.3at/802.3bt — PoE power-class definitions, PSE/PD voltage and current specifications, and the worst-case cable-loss assumptions used in the voltage-drop worked example.
- TIA TSB-184-A — *Guidelines for Supporting Power Delivery Over Balanced Twisted-Pair Cabling*: bundled-cable thermal derating for PoE referenced in the mental models section.
- ITU-T G.114 — one-way transmission-time recommendation for acceptable voice quality (150ms threshold used in the worked example).
- ITU-T P.800 / the E-model (ITU-T G.107) — MOS and R-factor voice-quality scoring referenced in the mental models section.
- FCC demarcation point rules (47 CFR §68.3, historical Part 68 registration framework) and standard carrier tariff/NEC practice establishing the carrier/customer responsibility boundary at the NID.
- No direct premise-telecom practitioner has reviewed this file yet — flag corrections or gaps via PR.
