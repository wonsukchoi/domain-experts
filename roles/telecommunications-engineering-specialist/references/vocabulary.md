### Insertion loss
The signal power lost as it passes through a cabling link, measured in dB, tested against a category-specific pass/fail threshold.
**In use:** "The run to 214 tested at 18.2 dB insertion loss against a 20.5 dB limit — 2.3 dB margin, comfortable."
**Common misuse:** Treated as a single pass/fail bit rather than a margin figure — a bare pass and a comfortable pass are different risk profiles, not the same result.

### NEXT (near-end crosstalk)
The signal coupling from one pair onto another pair measured at the same end of a cable, a key certification parameter for twisted-pair cabling.
**In use:** "NEXT came in at 38.1 dB against a 35.0 dB limit — that's fine, but it's the tightest margin on this run."
**Common misuse:** Confused with insertion loss; they test different failure modes (crosstalk between pairs vs. signal attenuation along a pair) and a run can pass one while marginal on the other.

### Alien crosstalk
Signal interference coupled in from adjacent, separate cables (not pairs within the same cable), which becomes the limiting factor for 10GBASE-T at longer distances on lower cable categories.
**In use:** "At 85 meters, alien crosstalk is why Category 6 can't reliably carry 10GBASE-T — Category 6A's tighter shielding/spacing is what buys the extra distance."
**Common misuse:** Assumed to be solved by the same shielding that handles ordinary (same-cable) crosstalk; it specifically requires cable design changes (spacing, shielding) rated for alien crosstalk performance.

### Demarc (demarcation point)
The physical point where the carrier's network ends and the customer's internal wiring begins — the boundary for carrier vs. customer troubleshooting responsibility.
**In use:** "Ticket's stuck because the carrier says the fault is past the demarc — we need to test right at that point to prove it either way."
**Common misuse:** Assumed to always be at the building entrance; in multi-tenant or campus buildings it can be at an intermediate distribution point, and getting this wrong misdirects troubleshooting.

### Erlang
A dimensionless unit of offered telecom traffic intensity — one Erlang represents one circuit continuously occupied for the measurement period.
**In use:** "Busy-hour traffic measured at 34 Erlangs — that's the number we size trunk groups against, not the extension count."
**Common misuse:** Confused with call volume (number of calls); Erlangs measure concurrent occupancy, not count, so two systems with the same call volume but different average call duration have different Erlang figures.

### Blocking probability (grade of service)
The target probability that a call attempt fails to get a trunk during the busy hour, used as the design input for Erlang B trunk sizing.
**In use:** "We're designing to 1% blocking, so a caller has roughly a 1-in-100 chance of a busy signal during the measured peak — tightening to 0.5% would need meaningfully more trunks for the same traffic."
**Common misuse:** Treated as a fixed universal constant (assumed 1%) rather than a business decision that trades trunk cost against call-blocking risk.

### PRI (Primary Rate Interface)
A digital circuit standard providing 23 bearer (voice/data) channels plus 1 signaling channel over a T1 (North America) — the standard unit of provisioned voice trunk capacity.
**In use:** "58 trunks required rounds up to 3 PRI spans — that's 69 channels, giving us headroom over the sizing figure."
**Common misuse:** Assumed to always mean 24 channels; the 24th channel (D-channel) carries signaling, not voice, so usable capacity per PRI is 23, not 24.

### Loss budget
The maximum allowable cumulative signal loss on a fiber link, computed from attenuation plus per-connector and per-splice loss, compared against a transceiver's specified power budget.
**In use:** "The loss budget calculates to 4.6 dB against a 6.0 dB transceiver spec — 1.4 dB of margin, which is enough to add one more patch connection later if needed."
**Common misuse:** Conflated with the cable's advertised "max distance" figure, which assumes a specific (often minimal) connector/splice count that may not match the actual installed path.

### RF site survey
A predictive and/or measured assessment of wireless signal coverage across a physical space, accounting for construction materials and interference sources.
**In use:** "The predictive survey flagged a coverage gap near the server room's reinforced concrete wall — that's where we added the extra AP, not on a grid pattern."
**Common misuse:** Skipped in favor of a fixed AP-per-square-foot ratio, which ignores that construction materials change effective coverage far more than raw floor area does.

### DAS (Distributed Antenna System)
An in-building or campus system of antenna nodes fed from a shared signal source, used to extend cellular or wireless coverage into areas standard access points/cell towers can't reach.
**In use:** "The parking structure needs a DAS node, not another Wi-Fi AP — the issue is cellular signal penetration, not Wi-Fi coverage."
**Common misuse:** Used interchangeably with a Wi-Fi access point; DAS specifically addresses distributed signal (often cellular carrier signal) distribution, a different problem and vendor relationship than enterprise Wi-Fi.

### Last-mile (in circuit provisioning)
The final physical connection segment from the carrier's nearest network point to the customer's premises — frequently the constraint that determines circuit lead time.
**In use:** "The quote jumped to 75 business days because this address needs new last-mile construction, not just an on-net cross-connect."
**Common misuse:** Assumed to be a fixed, small part of total lead time; for new-construction sites, last-mile build is often the majority of the quoted lead time, not a minor add-on.

### Cross-connect
A physical or logical connection point (patch panel, punch-down block, or carrier meet-me room connection) where two separate cabling or circuit segments are joined.
**In use:** "The fault traces to a bad cross-connect at the 110 block in IDF-2, not the horizontal run itself."
**Common misuse:** Assumed to be a single fixed point; a path can have multiple cross-connects (MDF to IDF, IDF to carrier demarc), and each is a separate potential fault point that needs its own verification.
