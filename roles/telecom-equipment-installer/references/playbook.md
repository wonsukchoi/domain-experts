# Playbook

Filled worksheets for the four checks that gate almost every premise telecom job: certifying structured cabling against TIA-568, budgeting PoE power delivery over a real cable length, capturing VoIP QoS and mapping symptoms to metrics, and triaging a trouble call at the demarc/NID before touching anything on either side. Figures below are published standard values and worked examples, not universal constants — the specific cable/PSE/PD datasheet and the carrier's own test equipment always control over this worksheet for a given job.

## 1. TIA-568 structured cabling certification worksheet

**Two separate limits, not one:** permanent link (fixed in-wall cabling, connector to connector) ≤ 90m. Channel (permanent link + patch cords/equipment cords at both ends) ≤ 100m. A run can be under 100m total and still fail cert if the permanent-link portion alone exceeds 90m.

| Category | Max frequency | Permanent link | Channel max | Typical use |
|---|---|---|---|---|
| Cat5e | 100 MHz | 90m | 100m | 1000BASE-T, VoIP, PoE (802.3af/at) |
| Cat6 | 250 MHz | 90m | 100m | 1000BASE-T; 10GBASE-T limited to ~37–55m due to alien crosstalk |
| Cat6A | 500 MHz | 90m | 100m | 10GBASE-T at full 100m; preferred for high-density PoE++ |

**Certification pass criteria at the channel/permanent-link length above (checked by a cert tester, not a tone probe):**

| Test | What it catches | Fails on |
|---|---|---|
| Wire map | Correct pin-to-pin continuity, split pairs, shorts | Miswire, split pair, transposed pair |
| Length (NVP-corrected) | Permanent link/channel over the category's cap | >90m link or >100m channel |
| Insertion loss (attenuation) | Signal power lost over the run's length | Excess length, poor-quality cable |
| NEXT (near-end crosstalk) | Pair-to-pair interference, usually from termination | Untwisted pair length at the jack/patch panel exceeding ~13mm (0.5in) |
| Return loss | Impedance mismatch reflecting signal back | Poor connector seating, cable damage, bend violations |

**Worked example — see SKILL.md** for the 92.3m permanent-link failure (channel 97.3m, under the 100m cap, but the 92.3m link exceeds the 90m submaximum) that produced intermittent PoE brownouts on two 3rd-floor drops.

**Second worked example — new-build horizontal run.** IDF-to-desk permanent link measures 78m. IDF patch cord 3m, desk patch cord 2m. Total channel = 78 + 3 + 2 = 83m — 17m of headroom under the 100m channel cap and 12m under the 90m permanent-link cap. NEXT and return loss both pass with margin on a Cat6A cert tester at 500MHz. This run has room to absorb a future re-termination or a slightly longer patch cord without requiring recertification.

## 2. PoE power budget and voltage-drop worksheet

**PoE power classes (IEEE 802.3af/at/bt):**

| Type | Class | PSE output (per port) | PD guaranteed minimum | Typical device |
|---|---|---|---|---|
| 802.3af (Type 1) | 0–3 | 15.4W | 12.95W | IP phone, basic AP |
| 802.3at (Type 2, "PoE+") | 4 | 30W | 25.5W | PTZ camera, higher-power AP |
| 802.3bt Type 3 ("PoE++") | 5–6 | 60W | 51W | Video conferencing endpoint |
| 802.3bt Type 4 ("PoE++") | 7–8 | 90–99.9W | 71.3W | Laptop charging, high-power radio |

**Voltage-drop formula:** delivered power (W) = [PSE minimum output voltage − (current draw × loop resistance for the run length)] × current draw. Use the worst-case assumption underlying 802.3af (20Ω loop resistance per 100m of Cat5e/6, scaled linearly to actual run length) unless the cable datasheet specifies otherwise, and check both **steady-state** current draw and the device's documented **inrush** current (commonly 1.5–2× steady-state for a few tens of milliseconds at power-up).

**Worked example — 92.3m run, Class 3 device (steady state and inrush):**
- Loop resistance at 92.3m = 20Ω × 0.923 = 18.46Ω (textbook), 21.3Ω (field-measured, marginal termination).
- Steady state (350mA, field resistance): drop = 0.35A × 21.3Ω = 7.46V; delivered = 44V − 7.46V = 36.54V; power = 36.54V × 0.35A = 12.79W — just under the 12.95W Class 3 ceiling, already tight even before inrush is considered.
- Inrush (700mA, field resistance): drop = 0.7A × 21.3Ω = 14.91V; delivered = 44V − 14.91V = 29.09V — below the ~30V PD undervoltage-lockout threshold, causing a reboot on power-up or after a momentary load spike (display backlight, relay click).
- **Remediation options in preference order:** (1) re-terminate to remove the marginal connection and recheck resistance; (2) if permanent-link length can't drop under 90m, relocate a PoE midspan/injector closer to the device to shorten the powered run; (3) downgrade to a lower-draw device variant only if (1) and (2) aren't feasible — last resort, since it doesn't fix the underlying marginal cabling.

**Bundled-cable thermal derating (TIA TSB-184-A):** running many PoE-powered cables together in a conduit or tightly bundled tray raises the bundle's internal temperature under sustained current draw. A bundle of 24+ cables all delivering Type 2/3 power in an unventilated conduit can require derating each cable's effective usable class by one tier versus the same cable run in free air — check the switch vendor's bundling guidance before assuming every port in a dense PoE deployment can run at full rated class simultaneously.

## 3. VoIP QoS capture and symptom-to-metric mapping

**Thresholds (ITU-T G.114, common carrier/vendor practice):**

| Metric | Acceptable | Degraded | Symptom when this metric fails |
|---|---|---|---|
| One-way latency | <150ms | 150–400ms tolerable, >400ms unacceptable | Delay, talk-over, "cutting each other off" |
| Jitter | <30ms | >30ms causes buffer discards | Robotic, garbled, chopped audio |
| Packet loss | <1% | >1% audibly degrades calls | Gaps, silence, dropped syllables |

**MOS (Mean Opinion Score) reference scale:**

| MOS | Quality |
|---|---|
| 4.3–5.0 | Excellent (uncompressed/toll quality) |
| 4.0–4.3 | Good |
| 3.5–4.0 | Acceptable — typical G.729 codec ceiling |
| <3.5 | Degraded — user complaints expected |

**Worked example — see SKILL.md** for the 42ms average / 65ms peak jitter case (latency 45ms and loss 0.2% both within threshold) that produced "robotic" audio specifically, remediated via DSCP EF tagging rather than a bandwidth upgrade.

**Codec bandwidth reference** (for trunk/LAN capacity planning, not quality diagnosis): G.711 ≈ 64kbps payload, ≈87kbps with RTP/UDP/IP/Ethernet overhead per call; G.729 ≈ 8kbps payload, ≈24–31kbps with overhead. A 40-desk office provisioning for 12 simultaneous G.711 calls needs ≈1.04Mbps of dedicated/prioritized bandwidth (12 × 87kbps) before any data traffic — undersizing this budget produces loss and jitter under peak call volume even when average utilization looks fine.

## 4. Demarc/NID responsibility-boundary triage

| Step | Test | Result | Conclusion |
|---|---|---|---|
| 1 | Loopback or dial-tone/sync test at the NID/smart jack | Clean (0% loss, low RTT, sync present) | Fault is inside the building — proceed to premise cabling/PoE/QoS checks |
| 1 | Loopback or dial-tone/sync test at the NID/smart jack | Dirty (loss, no sync, no dial tone) | Fault is upstream of the demarc — carrier's responsibility, escalate with the measurement |
| 2 | Cabling from NID to first premise jack/punch-down | Certifies clean | Fault is further inside — device, PoE, or QoS layer |
| 2 | Cabling from NID to first premise jack/punch-down | Fails cert | Premise cabling is the fault — remediate before escalating anything |

**Worked example.** A retail location reports a POS terminal offline. Tech runs a loopback at the smart jack: clean, 0% loss. Tech then checks the punch-down block immediately downstream of the NID: wire map fails on pair 2 (split pair). The fault is a premise-side termination error made during a recent remodel, not a carrier circuit issue — no carrier ticket needed, re-terminate the punch-down and retest.
