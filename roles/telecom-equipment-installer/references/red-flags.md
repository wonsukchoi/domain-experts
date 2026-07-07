# Red flags

Smell tests a premise telecom technician catches before a cert report is signed off, a PoE deployment is turned up, or a truck roll is requested from the carrier.

### Cert tester reports permanent-link length over 90m, even if total channel is under 100m

**Usually means:** the horizontal run was pulled longer than planned (routing detour, IDF relocated after design) and nobody checked the permanent-link submaximum separately from the overall channel figure.
**First question:** "What's the NVP-corrected permanent-link length specifically, not just the total channel length?"
**Data to pull:** the cert tester's length report broken out by permanent link vs. total channel, and the as-built cable route.

### PoE-powered device reboots intermittently, correlated with power-up or display/backlight activity rather than random timing

**Usually means:** marginal voltage delivery at the device — a long run, elevated termination resistance, or both — that passes steady-state draw but browns out on inrush current.
**First question:** "What's the field-measured loop resistance on this run, and what's the device's documented inrush current versus steady-state draw?"
**Data to pull:** the cert tester's resistance/length reading and the device manufacturer's inrush-current spec.

### VoIP calls described as "robotic" or "garbled" specifically, with latency and packet loss both testing clean

**Usually means:** jitter above the ~30ms threshold a typical jitter buffer is sized to absorb — a bandwidth increase won't fix this symptom.
**First question:** "What's the measured jitter during the actual complaint window, not just latency and loss?"
**Data to pull:** a concurrent QoS capture (latency, jitter, loss) during a reproduced call, and the DSCP/802.1p tagging configuration end to end.

### Packet loss over 1% sustained during a call quality complaint

**Usually means:** LAN congestion, a failing switch port, or a QoS policy not actually prioritizing RTP traffic despite being configured to.
**First question:** "Is the loss happening on the LAN segment or upstream of the demarc?"
**Data to pull:** loss measurements taken at both the demarc and the LAN switch nearest the affected device, to localize which segment is dropping packets.

### Wire-map test passes but the run fails NEXT or return loss on certification

**Usually means:** a termination-quality problem — untwisted pair length at the jack or patch panel exceeding spec, a poorly seated connector — not a cable defect.
**First question:** "How much pair untwist is there at the termination, measured against the category's untwist limit?"
**Data to pull:** the cert tester's NEXT/return-loss trace and a physical inspection of the termination.

### Demarc/NID loopback test comes back clean, but the ticket is escalated to the carrier anyway

**Usually means:** the escalation was made on the customer's description of symptoms rather than a measurement, wasting a carrier truck roll on a fault that's actually inside the building.
**First question:** "What specific measurement was taken at the demarc, and what did it show?"
**Data to pull:** the loopback/sync test result and timestamp, before any carrier ticket is opened.

### New PoE deployment where the switch's per-port rated class assumes free-air cabling, but the cable run is bundled with 20+ other powered cables in conduit

**Usually means:** the deployment plan didn't account for thermal derating in a dense bundle, and ports that pass individually may not sustain rated class simultaneously under load.
**First question:** "What does the cable and switch vendor's bundling/derating guidance say for this bundle size and conduit fill?"
**Data to pull:** TIA TSB-184-A-referenced vendor derating tables and the actual bundle count/fill on this run.

### As-built patch panel or cross-connect label doesn't match the physical jack being tested

**Usually means:** a labeling gap from TIA-606 administration not being maintained after a move/add/change, leading to troubleshooting the wrong physical run.
**First question:** "Does the label on this patch panel port match a physical trace to the jack in question, or just the documentation?"
**Data to pull:** the as-built cross-connect map and a physical toner trace from jack to panel.

### SIP trunk registration flapping while the physical layer (cabling, PoE) tests clean

**Usually means:** a router-side NAT or SIP ALG (application-layer gateway) interference issue, not a cabling or power problem — mid-call or registration issues after dial tone/link established point to the signaling layer.
**First question:** "Is the router's SIP ALG enabled, and does disabling it change the registration behavior?"
**Data to pull:** router SIP ALG/NAT configuration and the PBX/trunk registration logs during the flapping window.

### A structured-cabling job is certified to full Cat6A/10GBASE-T spec for a drop that will only ever carry an analog phone or a POS terminal

**Usually means:** over-speccing driven by habit or upsell rather than the actual load, adding material and labor cost with no functional benefit.
**First question:** "What's the actual maximum bandwidth this drop needs to carry, now and in a realistic multi-year horizon?"
**Data to pull:** the device/application list for this jack and the building's cabling standard (if one exists) for device-type-to-category mapping.
