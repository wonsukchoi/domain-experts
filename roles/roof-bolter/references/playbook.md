# Playbook

Filled sizing tables and sequencing a roof bolter or foreman runs before and during a cut. Every figure below is a worked example following common regulatory floors and typical NIOSH/manufacturer references — always verify against the mine's actual approved roof control plan, the bolt/resin manufacturer's current data sheet, and the district's requirements before installing or signing off.

## 1. CMRR-to-pattern and bolt-length decision table

Method: the approved roof control plan sets pattern and bolt length off the mapped CMRR for that horizon. CMRR runs 0–100; NIOSH ground-control literature treats roughly the following bands as the practical divisions used when a plan's pattern is being reviewed or a deviation considered — treat these as reference bands for interpreting a plan, not as a substitute for the plan's own engineered numbers.

| CMRR band | General characterization | Typical pattern response (illustrative — plan governs) |
|---|---|---|
| < 45 | Weak roof — frequent partings, low beam strength | Shorter bolts insufficient to span separation alone; tighter pattern, supplemental screen/straps, or shorter extended-cut allowance more likely |
| 45–65 | Moderate roof — the CMRR-58 example used in SKILL.md's worked example falls here | Standard pattern bolts (e.g. 4-ft bolts, 5×4-ft spacing) with routine sounding and pull-test verification |
| > 65 | Strong roof — competent beam with few partings | Standard or wider pattern, more likely to carry extended-cut approval |

**Filled example — CMRR 58, 20-ft-wide entry:** 4-ft fully grouted #6 Grade 75 rebar bolts, 5-ft along-entry × 4-ft between-row pattern, 24-in resin encapsulation, 20-ft extended cut approved on this panel's roof-fall history. Coverage per bolt = 5 ft × 4 ft = 20 sq ft. A 20-ft cut at 20-ft width = 400 sq ft ÷ 20 sq ft/bolt = 20 bolts per cut.

**Tightened pattern for a flagged zone (drummy/low pull test):** 4×4-ft pattern = 16 sq ft/bolt. Same 20-ft width, 15-ft affected length = 300 sq ft ÷ 16 sq ft/bolt ≈ 18.75 → 19 bolts, vs. 15 bolts the standard pattern would have used over that same 300 sq ft — a 4-bolt increase for that stretch only.

## 2. SEPT / pull-test anchorage math

Method: pull (or torque-convert) a sample bolt to a known load, then divide by the resin encapsulation length in feet to get tons/ft (or lbf/ft) of anchorage capacity. Compare that number — not just the raw pull load — against the accepted range for the rock type.

**Reference range (NIOSH):** 12–24 tons/ft of resin encapsulation = accepted "good" anchorage; typical coal-horizon results run 10–15 tons/ft. A result below roughly 12 tons/ft (or below the low end of the mine's own historical range for that horizon) is a rock-mass flag, independent of whether the bolt cleared its regulatory minimum tension.

**Filled example:**

| Quantity | Value |
|---|---|
| Bolt rated yield (per manufacturer spec, #6 Grade 75 rebar) | 64,000 lbf |
| Minimum required tension (50% of yield, 30 CFR 75.222(b)(2)) | 32,000 lbf (16 tons) |
| Pull test result | 36,000 lbf (18 tons) |
| Resin encapsulation length | 2 ft |
| Anchorage capacity (36,000 lbf ÷ 2 ft) | 18,000 lbf/ft ≈ 9 tons/ft |
| Compare to accepted range | 9 tons/ft < 12 tons/ft floor — flag despite tension passing |

**Two-floor check, every sample:**
1. Did the bolt clear 50% of yield or anchorage capacity (whichever is less)? — regulatory hardware floor.
2. Does tons/ft of encapsulation fall in the accepted 12–24 (typically 10–15 for coal) range for this rock? — rock-mass floor implied by the plan's CMRR.

A pass on (1) and a fail on (2) is not resolved by re-torquing — it's a plan-deviation trigger.

## 3. Resin selection by gel time vs. ambient/hole temperature

Method: spin time (the time actually spent rotating the bolt to mix the resin) must stay under the cartridge's rated gel time for the temperature at hand, with a minimum mixing threshold (commonly cited as roughly 30 bolt revolutions to achieve full mix — verify against the specific product's data sheet). Gel time shortens as temperature rises and lengthens as it drops; cartridge choice (fast-set vs. slow-set) is the lever, not spin speed alone.

| Cartridge type | Typical gel time (illustrative — read the actual product data sheet) | When it's the default |
|---|---|---|
| Fast-set | ≈8–15 seconds | Warmer holes/ambient, or where quick tension setting speeds the cycle and mixing can be reliably completed well inside the shorter window |
| Slow-set | ≈30–90 seconds | Colder holes/ambient, longer bolts needing more mixing travel, or any condition where spin time can't be confidently kept under a fast-set cartridge's shorter gel window |

**Rule of thumb:** if the crew can't confirm spin time stays comfortably under the cartridge's rated gel time for that shift's conditions, switch to the slower-gel product rather than rushing the spin — a bolt that torques up on unmixed resin looks anchored on the wrench and isn't at design strength.

## 4. ATRS cycle sequencing and setback

**Setback limit:** outby edge of the ATRS crossmember/rocker pads to the last row of permanent (bolted) support ≤ 5 ft (30 CFR 75.203/75.209) — fixed, every cycle.

**Cycle, in order:**
1. Sound the roof across the full planned cut width with a bar or pick before positioning the ATRS.
2. Position and set the ATRS from a location under permanently supported roof, or from a compartment providing overhead/lateral protection — controls are never operated from unsupported roof.
3. Drill and install bolts per the plan's pattern, resin spec, and torque/tension target.
4. Pull-test or torque-check sample bolts at the plan's required sampling rate; record results.
5. Reposition the ATRS for the next row, re-confirming the ≤5-ft setback before setting it.
6. Re-sound before every new advance — not once per shift.

## 5. Methane action-level checklist (face area, 30 CFR 75.323)

| Reading | Required action |
|---|---|
| < 1.0% | Normal operation |
| ≥ 1.0% | De-energize electrical equipment in the affected area; investigate and ventilate before resuming |
| ≥ 1.5% (or per mine-specific plan trigger) | Withdraw personnel from the affected area in addition to de-energizing equipment |

**Rule:** check before positioning the ATRS and before resuming after any ventilation change on the section — not once at the start of shift.

## 6. Ground-response decision tree (drummy sound or low pull test)

1. **Sounding returns hollow/drummy over more than a few feet** → stop, mark the extent (station-to-station), and pull-test in that zone before advancing further.
2. **Pull test in that zone comes back below ~12 tons/ft (or below the mine's historical range for that horizon)** → hold advance at the last confirmed-good station; do not log the hardware-tension pass as sufficient.
3. **Call foreman/engineer** with the specific numbers: station range, sounding description, pull-test tons/ft vs. the accepted range, current pattern and CMRR assumption.
4. **Engineer authorizes deviation** — typically: tighter pattern (e.g. 5×4 → 4×4 ft) and/or screen over the flagged zone, possibly a supplemental bolt row, and confirmation of whether extended-cut depth still applies for the remainder of that heading.
5. **Re-test in the newly installed zone** to confirm anchorage is back in the accepted range before resuming the plan's standard pattern past that point.
6. **Log the deviation** — station range, data, and authorization — on the shift and roof-control records before the next crew takes over that heading.
