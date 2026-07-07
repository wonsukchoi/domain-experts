# Vocabulary

Terms generalists conflate that a pumper keeps sharply separate. Each: definition, a sentence a practitioner would actually say, and the common misuse.

### PPM vs. %LEL

**PPM** (parts per million) measures toxic concentration — how much of a gas is present relative to air, used for H2S exposure limits. **%LEL** (percent of the lower explosive limit) measures how close a gas concentration is to being able to ignite, a completely different hazard axis. A reading can be low on one scale and high on the other.

**In use:** "Monitor's alarming on H2S ppm, not LEL — this is a toxicity exposure, not yet a fire/explosion risk, though a bigger release could trip both."

**Common misuse:** treating a "clear" LEL reading as proof the air is safe to breathe, or a low H2S ppm reading as proof there's no flammable-gas hazard. They're independent alarms measuring independent hazards.

### IDLH vs. PEL vs. TLV/STEL

**IDLH** (Immediately Dangerous to Life or Health, NIOSH) is the concentration above which unprotected exposure causes irreversible harm or death within a short window — for H2S, 100 ppm. **PEL** (Permissible Exposure Limit, OSHA, enforceable) is the general-industry ceiling — 20 ppm for H2S under 29 CFR 1910.1000 Table Z-2. **TLV/STEL** (Threshold Limit Value / Short-Term Exposure Limit, ACGIH, a guideline body, not an enforcement agency) are lower, health-based recommendations reflecting more conservative long-term-exposure science.

**In use:** "We're well under IDLH but over the OSHA ceiling — this still isn't a 'safe to keep working unprotected' number."

**Common misuse:** using IDLH as if it were the trigger for concern, when it's the threshold for irreversible harm — by the time a reading approaches IDLH, protective response should already be well underway, not just starting.

### Fluid pound vs. gas lock vs. gas interference

Three distinct dynamometer-card diagnoses, often confused because all three involve gas and all three reduce pump efficiency. **Fluid pound**: pump outrunning well inflow, plunger free-falls and impacts fluid (sharp vertical drop on the card). **Gas lock**: gas trapped in the barrel prevents either valve from opening at all (flat card, minimal load swing). **Gas interference**: free gas in the barrel delays valve action without stopping it entirely (rounded bottom corner, reduced card area).

**In use:** "That's fluid pound, not gas lock — the card's still swinging full range, it's just dropping hard on the down side. Slow the SPM before we touch anything downhole."

**Common misuse:** calling any gas-related card irregularity "gas lock" and prescribing a full pump pull, when fluid pound and gas interference are usually fixed by an SPM or gas-separator change, not a workover.

### SPM vs. fillage

**SPM** (strokes per minute) is how fast the pump is cycling — a setting the pumper controls. **Fillage** is the percentage of the barrel's stroke volume actually filled with liquid at bottom-of-stroke — a property of well inflow the pumper reads off the card, not sets directly.

**In use:** "We're at 8 SPM but fillage is running around 65% — the pump's asking for more fluid than the well can deliver."

**Common misuse:** raising SPM to "get more production" without checking fillage first, which increases fluid-pound severity rather than production.

### Casing pressure vs. tubing pressure

**Tubing pressure** is measured at the production tubing, carrying fluid up from the pump or perforations to surface. **Casing pressure** is measured in the annulus between casing and tubing, and on a properly functioning well is often near zero or a small stable value — a rising casing pressure with no operational cause is a leak or migration signal, not an alternate production-pressure reading.

**In use:** "Casing pressure's up 15 psi over two weeks with nothing changed uphole — that's not noise, that's worth a leak check before the next report."

**Common misuse:** treating casing pressure as just a secondary or redundant number to tubing pressure rather than a distinct integrity indicator with its own baseline.

### BS&W

Basic sediment and water — the non-oil fraction (water plus solids) in a produced-fluid sample, expressed as a percentage, measured from a thief sample via centrifuge or settling.

**In use:** "BS&W's crept from 0.6% to 1.2% over three months with no workover — worth flagging before it's called normal."

**Common misuse:** treating a BS&W trend as noise because the absolute percentage is still small; the trend direction over several readings, not any single value, is the signal for water breakthrough or emulsion issues.

### Pump-off controller (POC)

A surface control device that senses pump load or motor current and stops the pumping unit when the well's fluid level drops below what the pump can efficiently lift, then restarts once fluid has recovered — an automated substitute for a pumper manually tuning SPM to match fillage.

**In use:** "This well's been pounding fluid every visit — put a POC on it instead of me guessing at SPM every round."

**Common misuse:** installing a POC and assuming it eliminates the need to check dynamometer cards; a POC prevents pounding from over-pumping but doesn't diagnose valve leaks or gas lock, which still need a card read.

### Wellhead vs. Christmas tree

The **wellhead** is the structural/pressure-containing assembly at the surface where casing strings are hung and sealed. The **Christmas tree** is the stack of valves, fittings, and chokes mounted above the wellhead that controls flow. On a pumping well, the tree is comparatively simple; the term still gets misapplied to the whole surface assembly.

**In use:** "Leak's at the tree, not the wellhead itself — it's a valve packing issue, not a casing seal problem."

**Common misuse:** using "wellhead" to describe the entire surface equipment stack, which obscures whether a problem is structural (wellhead) or a controllable fitting (tree).

### MASP vs. formation fracture pressure

**MASP** (max authorized surface pressure) is the regulator-permitted injection pressure limit for a disposal well, set with a margin below the **formation fracture pressure** — the pressure at which the injection zone's rock would physically fracture, established by a step-rate test. MASP is a permit number; fracture pressure is a physical property of the rock.

**In use:** "We're at 87% of MASP — that's not 87% of what the rock can take, MASP already has margin built in below the frac gradient."

**Common misuse:** treating MASP as if it were the physical failure point itself, when it's a regulatory limit set below that point specifically so operators never have to operate near the actual fracture pressure.

### Type curve vs. actual production

The **type curve** is the mathematical decline projection (Arps exponential/hyperbolic/harmonic) fit to a well's early production history. **Actual production** is the measured rate at each visit. The gap between them, tracked over consecutive readings, is the diagnostic signal — not either number alone.

**In use:** "Two months running below the type curve, not just one — that's past the noise band, time to pull a card before we call the engineer."

**Common misuse:** reacting to a single below-curve reading as if it were confirmed underperformance, when gauge error or a one-off upset is the more common explanation for an isolated deviation.
