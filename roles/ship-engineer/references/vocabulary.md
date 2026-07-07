# Vocabulary

Terms generalists conflate that marine engineering officers keep sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse to avoid.

### Alarm setpoint vs. shutdown (trip) setpoint

**Alarm setpoint** is the threshold at which the monitoring system notifies the watch that a parameter is out of normal range but the equipment keeps running. **Shutdown (trip) setpoint** is the threshold at which the protective system automatically stops or isolates the equipment regardless of watch action.

*In use:* "We're at the 88° alarm, not the 95° trip — that gap is ten-plus minutes to fix the root cause before the engine protects itself."

**Common misuse:** treating the alarm setpoint as a warning to note and the shutdown setpoint as the only number that requires action — the alarm is the actual decision point; the trip is what happens when the decision was missed.

### Oil content meter (OCM) vs. oily-water separator (OWS)

**OWS** is the equipment that mechanically and chemically treats bilge water to remove oil before discharge. **OCM** is the instrument that measures the oil content of the treated effluent against the MARPOL Annex I limit, gating whether the discharge valve may open.

*In use:* "OWS is running fine mechanically, but the OCM's reading 22 ppm — that's a coalescer problem, not a pump problem."

**Common misuse:** assuming the separator running normally means the discharge is compliant; the OCM reading, not the separator's operating state, is the actual compliance gate.

### Oil Record Book, Part I vs. Part II

**Part I** logs machinery-space operations — bilge water transfer, treatment, and discharge. **Part II** logs cargo/ballast operations on oil tankers. They are separate statutory logs under MARPOL Annex I with separate entry codes.

*In use:* "That's a Part I entry — bilge transfer to the holding tank — not a Part II cargo operation."

**Common misuse:** logging a machinery-space bilge operation under the wrong part, which misroutes the entry during a port-state control or class inspection.

### "Magic pipe" / bypass hose

An unlogged, often removable piping arrangement rigged to discharge bilge water directly overboard, bypassing the oily-water separator and OCM entirely. The term comes from documented MARPOL enforcement cases, not informal ship slang for a broken system.

*In use:* "That flexible hose behind the separator isn't a spare — if it connects the bilge main straight to the overboard valve, that's a magic pipe and it comes out now."

**Common misuse:** treating a bypass arrangement as a temporary engineering workaround for a broken separator rather than what it actually is — a criminal act under APPS/MARPOL enforcement, with documented multi-million-dollar penalties and individual prosecutions.

### Jacket (fresh) cooling water vs. raw (sea) cooling water

**Jacket cooling water** is the closed fresh-water circuit that directly cools the engine block/cylinders. **Raw (sea) cooling water** is the open circuit, typically cooling the jacket water through a heat exchanger (or cooling lube oil directly), that is drawn from and returned to the sea.

*In use:* "JCW temp is climbing because the raw-water side lost pressure — check the sea strainer before you touch anything on the jacket-water side."

**Common misuse:** troubleshooting the closed jacket-water circuit for a fault that actually originates on the open sea-water side, or vice versa.

### Black-start vs. load-shedding

**Black-start** is bringing a generator online from a fully dead (de-energized) state without external power support. **Load-shedding** is the automatic or manual disconnection of non-essential loads to protect a generator from overload — used both to prevent a blackout and, in reverse as stepped loading, to recover from one.

*In use:* "We black-started DG1, then load-shed everything but the blowers and service pumps for the first two minutes to keep the frequency from dipping."

**Common misuse:** using "black-start" to describe any generator restart, including a normal start with the switchboard still energized — black-start specifically means starting with no other power source available.

### Dead ship condition

A vessel with no operating main propulsion, boiler, or auxiliary machinery due to total loss of electrical power, requiring the emergency source of power and restart procedures to recover — a defined SOLAS term, not a casual description of "engine trouble."

*In use:* "We were dead ship for six minutes between the trip and the emergency generator picking up steering and fire pump load."

**Common misuse:** applying the term to a partial casualty (one generator down, main engine still running) where the vessel retains propulsion and some electrical power.

### Purifier vs. clarifier

**Purifier** separates two liquids of different density (fuel or lube oil from water) using a dam ring or gravity disc set for that density split. **Clarifier** removes solid particulates from a single liquid and has no water-separation function.

*In use:* "Run it through the purifier first to knock out the water, then the clarifier can do its job on the remaining solids."

**Common misuse:** expecting a clarifier to remove free water from fuel or lube oil — it isn't configured to separate liquids of different density at all.

### Crankcase oil mist detector vs. crankcase explosion relief door

**Oil mist detector** continuously monitors crankcase atmosphere for the hydrocarbon mist concentration that precedes a crankcase explosion, triggering an alarm and often a slow-down before ignition conditions are reached. **Relief door** is a passive pressure-relief device that vents an explosion that has already started, limiting damage rather than preventing the event.

*In use:* "The mist detector alarmed twice this watch — that's the prevention system telling us something's wearing hot, don't just reset it and hope the relief doors never have to work."

**Common misuse:** treating the relief door as a safety margin that makes an oil mist alarm less urgent — the relief door only limits damage after ignition; it does nothing to prevent the explosion the mist alarm is warning about.

### Governor vs. overspeed trip

**Governor** continuously regulates fuel delivery to hold engine speed at the set point under varying load. **Overspeed trip** is an independent, separate protective device that shuts fuel off entirely if speed exceeds a safe limit — a backup to the governor, not a duplicate of it.

*In use:* "Governor's hunting under this load, but that's a control-loop problem — the overspeed trip is a completely separate mechanical/electronic path and it's still fine."

**Common misuse:** assuming an overspeed trip failure implies the governor is also compromised, or vice versa — they are independent systems by design, specifically so one failure doesn't defeat both.

### Class survey vs. port state control (PSC) inspection

**Class survey** is conducted by the vessel's classification society against class rules and the vessel's own certificates, maintaining class (and by extension, insurability and flag registration). **PSC inspection** is conducted by the port state's maritime authority against international convention requirements (SOLAS, MARPOL, STCW), independent of class.

*In use:* "Class flagged the separator certificate as due for renewal; PSC's separate finding was the Oil Record Book entries not matching the bell book — two different inspectors, two different findings."

**Common misuse:** treating a clean class survey as equivalent to PSC compliance, or assuming a PSC deficiency will automatically appear on the next class survey.

### Sludge vs. bilge water

**Sludge** is the oil residue separated out during fuel/lube purification, retained in a dedicated sludge tank and disposed of ashore or by incinerator per MARPOL Annex I. **Bilge water** is the accumulated water in machinery-space bilges (leakage, condensation, washdown) that must pass through the OWS/OCM before any discharge.

*In use:* "That's sludge from the purifier, it goes to the sludge tank for shoreside disposal — it never goes near the OWS at all."

**Common misuse:** conflating the two streams, or assuming sludge can be legally processed through the OWS the same way bilge water is — sludge disposal is governed separately and typically requires shoreside reception or incineration, not overboard discharge under any OCM reading.
