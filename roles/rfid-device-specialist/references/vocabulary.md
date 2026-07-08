# RFID Device Specialist — Vocabulary

### Forward link vs. reverse link
The forward link is the reader-to-tag path that has to deliver enough power to wake a passive tag's chip; the reverse link is the tag-to-reader backscatter path the reader has to detect. They fail for different reasons and at different power budgets.
**In use:** "The reader's receive sensitivity is fine — this is a forward-link problem, the tag isn't waking up at that distance."
**Common misuse:** Diagnosing every no-read as a reader-sensitivity issue and reaching for reader firmware or receive-gain settings, when passive UHF is almost always forward-link limited — the tag failing to power up, not the reader failing to hear it.

### EIRP vs. ERP
EIRP (effective isotropic radiated power, the FCC's regulatory unit) and ERP (effective radiated power, referenced to a dipole, the unit ETSI uses) both describe transmitted power after antenna gain, but they're offset by about 2.15 dB and sit under different ceilings — 4 W EIRP in the US, 2 W ERP in Europe.
**In use:** "Don't just port the US antenna-gain spec to the EU site — 2 W ERP is a lower ceiling than it looks once you convert out of EIRP."
**Common misuse:** Treating the two units as interchangeable and comparing a vendor's EIRP-rated hardware directly against an ERP regulatory limit, which understates how close the setup actually is to the ceiling.

### Q-algorithm / Q value
The Gen2 anti-collision parameter that sets how many response slots a reader offers per query round; the reader adjusts it up when replies collide and down when slots go silent, seeking the slot count that matches the actual tag population.
**In use:** "Bump the Q value before you touch anything else — the reader's still guessing there are fewer tags in that zone than there are."
**Common misuse:** Reading a reader that keeps re-querying without the tag count settling as a broken or malfunctioning reader, when it's the algorithm correctly working through too many tags per frame for the current Q setting.

### Return loss (S11)
A vector-network-analyzer measurement of how much RF energy reflects back from an antenna instead of radiating, expressed as a negative dB value where more negative means a better match; practitioners target better than −10 dB, ideally −15 dB.
**In use:** "Bench S11 was −16 dB, but the in-situ reading near the racking is only −7 dB — that antenna needs re-matching on site."
**Common misuse:** Citing a factory bench S11 spec as proof the antenna is matched at the install site, without re-measuring in situ after the surrounding metal and inventory are actually in place.

### Multipath null
A location where reflected RF signals arrive out of phase with the direct signal and cancel it, collapsing effective read range far below the antenna's open-aisle rating — independent of whether the antenna itself is damaged or mistuned.
**In use:** "That's not a dead antenna, it's a multipath null from the new steel door — the open-aisle 3 m range is what collapsed to 30 cm."
**Common misuse:** Treating a sudden localized dead zone as evidence of a hardware fault or a bad tag batch, rather than checking for a nearby metal or reflective surface change that created a phase-cancellation pocket.

### Reference tag / witness tag
A fixed tag placed at a known position and monitored for RSSI drift from its install-day baseline, used as an environmental sentinel rather than as inventory.
**In use:** "The reference tag at that antenna dropped 18 dB from baseline — something in that zone's environment changed, go look before you touch the antenna."
**Common misuse:** Interpreting a reference tag's RSSI drop as the tag itself degrading electrically, when a passive tag's chip doesn't wear out under normal read counts — the drift almost always points at the environment around it.

### Kill password vs. access password
Two separate passwords stored in a Gen2 tag's Reserved memory bank: the kill password permanently disables the tag, the access password only locks/unlocks write access to memory — they are not interchangeable and using the wrong one has irreversible consequences.
**In use:** "Confirm which password field is populated before this ships — if the kill password got written by mistake, that tag is permanently dead the first time anyone tries to kill it."
**Common misuse:** Treating "the password" as a single field or assuming a locked-but-live tag was killed (or vice versa), when the two functions live in different parts of Reserved memory and behave completely differently.

### EPC vs. SGTIN-96
The EPC (electronic product code) is the general identifier field in a Gen2 tag; SGTIN-96 is one specific 96-bit encoding scheme for that field (header, filter value, partition, company prefix, serial) — not a synonym for "the tag's ID" in general.
**In use:** "Check the filter value in the SGTIN-96 encoding before you assume that's a pallet tag — it might be encoded at the item level."
**Common misuse:** Using "EPC" and "SGTIN-96" interchangeably in conversation with an integration team, which causes confusion when the actual tags on site use a different encoding scheme (e.g., SSCC-96 for logistics units) inside the same EPC field.

### Read rate vs. read range
Read rate is the percentage of tags in a population actually captured in a pass; read range is the physical distance at which a single tag reliably responds. A system can have excellent read range and still post a poor read rate if tags are occluded, misoriented, or moving too fast to be queried.
**In use:** "Don't sell the read-range spec as the read-rate guarantee — a 30 ft rated portal can still miss half the pallet if cartons are stacked to block line of sight."
**Common misuse:** Quoting a reader/antenna's rated read range to a client as if it were the accuracy number they'll see in production, when the two are governed by different failure modes (link budget vs. occlusion, orientation, and speed).

### Circular vs. linear polarization
Circular-polarized antennas read a tag regardless of its rotational orientation but sacrifice roughly 30% of open-aisle range compared to linear; linear antennas hold full range but only work reliably when tags pass in a fixed, known orientation.
**In use:** "These garments tumble through in random orientation — circular polarization is the right call even though it costs range."
**Common misuse:** Defaulting to linear polarization because the spec sheet range number looks better, without first checking whether the use case actually guarantees fixed tag orientation (e.g., a conveyor) or not.

### RFID vs. RTLS
RFID (as typically deployed, passive UHF) confirms identity and presence in a read zone; RTLS (real-time location systems, commonly UWB) provides continuous sub-meter positional tracking. They answer different questions and aren't substitutable by adjusting settings.
**In use:** "If the client needs to know which aisle a pallet is in, that's RFID; if they need to know it's 40 cm from the north wall in real time, that's a UWB RTLS system, not this deployment."
**Common misuse:** Quoting sub-meter positioning accuracy to a client running passive UHF RFID, when that level of continuous location precision belongs to a different technology class (UWB-based RTLS) entirely.

### Backscatter
The mechanism by which a passive tag replies: rather than transmitting its own signal, it modulates the reflection of the reader's own carrier wave back to the reader's receiver.
**In use:** "The tag's not transmitting at all in the way people picture it — it's reflecting the reader's carrier back, modulated. That's why forward-link power matters more than reader receive sensitivity."
**Common misuse:** Describing a passive tag as "transmitting" or "broadcasting" its ID, which leads to wrongly diagnosing weak reads as a tag-side power/battery problem on hardware that has no battery or active transmitter at all.

### Dead zone vs. blind spot
A dead zone is a location where no tag reads occur regardless of tag orientation (typically power/range or multipath related); a blind spot is orientation-dependent — a tag reads fine in one rotation and drops out in another, usually a cross-polarization effect a single fixed antenna angle can't cover.
**In use:** "Sweep it in a figure-8 before calling that a dead zone — if it only fails at one tag angle, that's a blind spot, and the fix is polarization or scan technique, not antenna power."
**Common misuse:** Treating any no-read location as a uniform "dead zone" needing more reader power, when an orientation-dependent blind spot needs a scanning-technique or polarization fix instead — more power won't resolve a cross-polarization miss.

### Partial power delivery (through obstruction)
A state where a tag receives enough forward-link energy to power its chip but not enough to backscatter a clean, complete reply — the tag shows up as "present" in the log with a garbled or truncated payload rather than not appearing at all.
**In use:** "That's not a damaged tag — it's reading present with a garbled payload, which is the signature of partial power through whatever's blocking it, not chip failure."
**Common misuse:** Treating a tag that reads as "present but garbled" as physically damaged and swapping it out, when the actual fix is removing or repositioning around the obstruction — a replacement tag in the same spot will show the same symptom.
