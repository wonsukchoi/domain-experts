# Red flags

Smell tests for a completed install, a comeback complaint, or a work order under review.

### Final wired speaker impedance below the amplifier's rated stable minimum (e.g., 1-ohm final load on an amp rated stable no lower than 2-ohm)
- **Usually means:** the install was wired for maximum theoretical power/volume without checking the achievable configurations against the amp's spec sheet, or the sub pairing genuinely has no wiring option that lands on the amp's rated sweet spot and the lowest option was chosen anyway.
- **First question:** "What's the amp's rated stable-impedance floor, and what final load does this exact wiring configuration compute to?"
- **Data to pull:** amp spec sheet stable-impedance rating (stereo and bridged separately), sub voice-coil configuration (SVC/DVC, ohm rating per coil), the wiring diagram as installed.

### Gain set at or near maximum with no distortion measurement recorded on the work order
- **Usually means:** gain was set "by ear" under time pressure, which reliably overdrives the preamp stage into clipping well before the amp's rated power is used, regardless of how loud it sounds.
- **First question:** "What reference (DD-1/oscilloscope reading, or calculated target voltage) was used to set gain, and is that value on the work order?"
- **Data to pull:** the target voltage calculation (√(P×R)) for the amp's rated power at the wired impedance, the measured gain-setting value, distortion-detector result if used.

### Parasitic draw increases more than the low teens of mA over the pre-install baseline after full module sleep
- **Usually means:** an installed module's trigger wire is landed on a constant-hot circuit instead of a switched one, or the module isn't fully entering standby — either way it will measurably shorten how long the vehicle can sit before the battery drains.
- **First question:** "What was the parasitic draw before this install, what is it now with everything asleep, and what's the delta?"
- **Data to pull:** pre-install baseline draw reading, post-install draw reading (after 20–40 min sleep), fuse-pull isolation results if the delta wasn't immediately explained.

### A "Lost Communication" DTC (e.g., a U0100-series code) or intermittent warning lights appearing weeks after an aftermarket install with no note connecting it to that work
- **Usually means:** a factory data-bus wire (commonly CAN-H/CAN-L) was spliced into directly rather than integrated through a bypass/T-harness module, and the added splice is degrading bus signal integrity intermittently.
- **First question:** "Was any factory data-bus wire spliced directly, or was every add-on integrated through a harness-specific bypass module?"
- **Data to pull:** the installation photos/notes showing tap points, the specific bypass module (if any) used and its part number match to the vehicle's trim/year.

### A splice connector or crimp found directly on a CAN-H or CAN-L wire
- **Usually means:** the installer used a universal splice-in method instead of a trim-specific bypass harness, either because none was available or to save labor time.
- **First question:** "Why wasn't a bypass module used for this signal, and was that decision documented?"
- **Data to pull:** harness/bypass-module availability for this exact make/model/year/trim, the installer's documented reason if a splice was used anyway.

### An accessory's trigger or power wire lands on a wire that reads 12V+ with the ignition off
- **Usually means:** the wrong circuit was tapped for a device meant to be switched, which keeps the device (and often its radio/CAN transceiver) awake continuously instead of sleeping with the vehicle.
- **First question:** "Is this wire supposed to be switched or constant per the harness diagram, and does it match what's actually landed?"
- **Data to pull:** the harness pinout/wiring diagram for the specific circuit, a voltage reading at that wire with ignition off vs. on.

### Amplifier or bypass module noticeably warm to the touch at idle/standby with no signal playing
- **Usually means:** the amp is being asked to drive a load below its rated floor and is running its current-limiting/thermal protection continuously, or a module isn't entering low-power standby as designed.
- **First question:** "What's the wired impedance the amp is seeing, and is the module's standby state confirmed against its documented sleep current?"
- **Data to pull:** wired impedance calculation, ambient case temperature reading, module manufacturer's rated standby current.

### Windshield, front bumper cover, or grille removed/reinstalled as part of or incidental to the job with no ADAS calibration note
- **Usually means:** the install disturbed a camera's or radar's mounting or optical path without triggering the calibration check that OEM guidance requires whenever that path is disturbed.
- **First question:** "What forward camera or radar sensors are mounted at or near the panel that was removed, and was calibration performed, referred out, or ruled not applicable — and is that documented?"
- **Data to pull:** the vehicle's ADAS sensor locations for this trim, the calibration status note on the work order, a post-install scan for related DTCs.

### Line output converter (LOC) output clips at a low factory head-unit volume setting
- **Usually means:** the LOC's input sensitivity doesn't match the factory deck's actual output voltage swing, so the signal is already distorted before it reaches the aftermarket amp's gain stage.
- **First question:** "What's the factory deck's actual peak output voltage, and does the LOC's input range cover it without attenuating or clipping?"
- **Data to pull:** factory head-unit output voltage spec (or a measured value), LOC model's rated input voltage range, an oscilloscope trace of the LOC's output at the volume level the customer actually uses.

### No pre-install baseline (parasitic draw, DTC scan, ADAS sensor inventory) recorded before work began
- **Usually means:** there's no way to later prove whether a battery-drain complaint or a data-bus fault was caused by this install or was pre-existing, which leaves the shop unable to defend a comeback dispute.
- **First question:** "What was measured and recorded before any wire was cut on this job?"
- **Data to pull:** the work order's pre-install section, timestamped draw/DTC readings if a shop-standard checklist exists.

### Customer reports intermittent electrical gremlins (random warning lights, door locks cycling, radio resetting) starting shortly after an aftermarket install
- **Usually means:** a data-bus integration issue (splice-induced bus noise, a bypass module mis-wired to the wrong signal) rather than an unrelated factory fault, especially if the timing lines up with the install date.
- **First question:** "What changed in the vehicle's electrical system on the install date, and does the symptom pattern match a bus-integrity issue versus a coincidental factory fault?"
- **Data to pull:** install date vs. symptom onset date, the specific bypass/splice method used, a bus-health scan if the shop has the equipment.
