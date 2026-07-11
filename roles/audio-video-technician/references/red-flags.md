# Red Flags

On-site smells during load-in, rehearsal, or a live show. Format per flag: what it usually means, the first question a veteran asks, and the specific data to pull.

### Wireless mic drops out or gets intermittent static in one specific zone of the room

- **Usually means:** a multipath RF null at that location, or a third-order intermodulation product landing on that frequency — more likely once 8+ wireless channels are active in the same room.
- **First question:** "Does it happen at the same physical spot every time, or only at certain moments?"
- **Data to pull:** an RF spectrum scan taken at that exact location during a repeat of the dropout, compared against the coordinated frequency list.

### "No signal" on a display after a source or switcher was power-cycled or hot-swapped

- **Usually means:** an EDID or HDCP handshake failure, not a cable fault — displays and sources renegotiate on reconnect, and a mismatch there produces the identical symptom as a dead cable.
- **First question:** "Did anything just get plugged in, unplugged, or power-cycled downstream of this display?"
- **Data to pull:** the switcher/scaler's handshake or EDID log if available; failing that, swap in an EDID emulator before swapping the cable.

### Lip sync perceptibly off — audio noticeably ahead of the picture

- **Usually means:** accumulated video-processing latency (switcher, scaler, wall processor) was never compensated with a program-audio delay.
- **First question:** "What's the total frame count from source to display right now, at today's frame rate?"
- **Data to pull:** each device's manufacturer-stated latency in frames, summed and converted to milliseconds at the show's actual frame rate.

### Hum audible through the PA only when a specific device (laptop, DI'd instrument) is connected

- **Usually means:** a ground loop — the device is grounded through both its own power connection and the shared signal ground, creating a loop that induces 60Hz/120Hz hum.
- **First question:** "Does the hum disappear if that device runs on battery, or through a different circuit?"
- **Data to pull:** none needed to diagnose; fix with an isolation transformer or DI box on the signal path. Never lift the AC safety ground to test this — that's a shock hazard, not a diagnostic step.

### Frequencies that were "cleared" weeks ago show interference at the actual venue on show day

- **Usually means:** the coordination was done off-site or reused from a prior show, and a full-power local TV signal now occupies that channel — post-2020 spectrum repack, allocations shift more than clients assume.
- **First question:** "When and where was this frequency set actually scanned — this room, today, or somewhere else, some other day?"
- **Data to pull:** a fresh on-site spectrum scan taken the day of the event, not the coordination file from the last venue.

### Backup path takes visibly long (multiple seconds of black or silence) to engage during a failure

- **Usually means:** the backup was cold — powered and routed only at the moment of failure — rather than hot: live, framed, and monitored continuously.
- **First question:** "Was this backup live and being watched/listened to before the cut, or did it power up when the primary failed?"
- **Data to pull:** the cutover time measured during rehearsal, if it was tested at all; if it wasn't tested, that absence is itself the finding.

### Audio and video sync drift over the course of a long show (fine at the start, off by the end)

- **Usually means:** two digital devices without a shared clock reference (no genlock on video, no shared word clock on audio) are each running their own internal clock, and the tiny difference compounds over hours.
- **First question:** "Are the video devices genlocked to a common reference, and are the digital audio devices on a shared word clock?"
- **Data to pull:** the clock-source setting on each device; check whether more than one device is configured as clock master.

### Multiple digital audio devices intermittently click or pop with no obvious cable or interference cause

- **Usually means:** a clock-master conflict — two devices on the same digital audio network (Dante, AES) both trying to act as the sample-rate reference.
- **First question:** "Which device is set as clock master, and is anything else on the network also configured that way?"
- **Data to pull:** the network's clock-status page/utility, which will flag a master conflict directly.

### An HDMI run that benched clean at full length drops or sparkles once installed through the venue's in-wall or under-carpet cabling

- **Usually means:** the real-world run exceeds passive HDMI's practical distance/connector-count limit even though the cable's spec claims otherwise — connector count and cable quality matter as much as raw length.
- **First question:** "What's the total run length including every coupler or wall-plate connector in the path, not just the cable's own length?"
- **Data to pull:** a physical trace of the run with every connection point counted; if it exceeds roughly 7–8m or has more than one coupler, plan to convert to HDBaseT or fiber rather than debugging the passive run further.

### The venue's house network or PA "should work fine" with your gear but hasn't been tested with it

- **Usually means:** compatibility was asserted, not verified — house infrastructure often lacks the specific configuration (network QoS, PA headroom, isolated circuits) a touring rig assumes.
- **First question:** "Has this exact combination — our gear, their network/PA — been run under actual show load, or is this an assumption from a spec sheet?"
- **Data to pull:** a load test with the real rig before committing the show's signal path to house infrastructure.
