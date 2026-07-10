# Red Flags

Bench smell tests. Format per flag: what it usually means, the first question, the data to pull.

## qPCR standard curve efficiency outside 90–110% (or R² < 0.98)

- **Usually means:** serial-dilution pipetting error — frequently an out-of-calibration pipette used for the template transfer step — less often master-mix inhibition or degraded primers.
- **First question:** "When was the pipette used for the dilution series last gravimetrically checked, and is it still in tolerance?"
- **Data to pull:** pipette calibration log for the run date, and the raw Cq table by dilution point to see whether one point (not the whole line) is driving the deviation.

## Cell viability by trypan blue <90% pre-plating (outside an expected post-thaw dip)

- **Usually means:** extended time at room temperature during passaging, mistimed trypsin exposure, or a stressed/high-passage line.
- **First question:** "Is this a fresh thaw, where a dip is expected, or a routine passage, where it isn't?"
- **Data to pull:** passage log and time-out-of-incubator log for that specific passage.

## Negative/no-template control shows signal

- **Usually means:** reagent contamination — commonly a shared master mix or a contaminated water/buffer stock — cross-well carryover, or primer-dimer misread as amplification.
- **First question:** "Is the contamination in the master mix lot itself, or introduced during plating?"
- **Data to pull:** melt curve or gel for the NTC well, and the master mix lot number cross-referenced against every other plate using that lot.

## A260/A280 outside roughly 1.8–2.0 for a nucleic-acid prep

- **Usually means:** protein carryover (below 1.8, often incomplete deproteinization), contaminating RNA in a DNA prep, or phenol/guanidine carryover.
- **First question:** "Was this a column- or phenol-chloroform-based prep, and was the wash-step timing followed?"
- **Data to pull:** the A260/A230 ratio as well — phenol contamination often shows there before A260/A280 moves — and the extraction kit lot number.

## Pipette or balance found >30 days past its calibration due date

- **Usually means:** the calibration schedule isn't tracked against active instruments, or a "backup" unit was pressed into routine use without being added to the program.
- **First question:** "What's the last known-good calibration date, and what results were generated on this instrument since then?"
- **Data to pull:** calibration log, and the experiment log cross-referenced to the instrument's serial number for the gap window.

## Biosafety cabinet certification lapsed (>12 months, or a filter change/relocation with no recertification)

- **Usually means:** certification renewal wasn't triggered by the maintenance event — not necessarily that the cabinet is unsafe today — but any BSL-2+ work performed on it since the triggering event is technically out of compliance.
- **First question:** "What was the last certifying event — a routine annual, or was there a filter change or move since?"
- **Data to pull:** the BSC certification sticker/log and the facilities maintenance record for that cabinet.

## Autoclave biological-indicator (spore test) fails or hasn't been run in the required interval

- **Usually means:** a load didn't reach sterilizing conditions — commonly an overpacked load, wrong cycle selected, or a door-seal issue — rather than a bad indicator.
- **First question:** "Did the cycle's own printout show target temperature and time were reached, independent of the spore result?"
- **Data to pull:** the cycle printout/chart-recorder trace and the spore-test log for the preceding weeks.

## Reagent lot changed mid-study with no bridging comparison run

- **Usually means:** budget or scheduling pressure skipped the bridge, or nobody noticed the lot number changed — common with vendor auto-substitution on reorder.
- **First question:** "Do we have any samples run on both lots, even incidentally, to check for a shift?"
- **Data to pull:** the reagent receiving log and results grouped by lot number and date.

## Same result reproduced only by the technician who first got it

- **Usually means:** an undocumented technique variable — grip, timing, an unwritten "trick" step — or a shared reagent/equipment idiosyncrasy specific to that person's station.
- **First question:** "What does this technician do differently, step by step, from the SOP as written?"
- **Data to pull:** a side-by-side protocol walkthrough, not just the data — the deviation is procedural, not numeric.

## Lab notebook entries for a run made after the day of the run

- **Usually means:** a lab that documents at end-of-day or later, which is exactly where deviations (a slightly-off timing, a substituted reagent) get silently smoothed over or forgotten.
- **First question:** "Right now, without checking notes — what lot was the master mix?" If the technician can't answer, the notebook couldn't either by the time it was written.
- **Data to pull:** ELN entry timestamp metadata against the actual run time logged on the instrument.

## Positive control drifting toward the edge of its acceptable range across consecutive plates, but still "passing"

- **Usually means:** an early degradation signal — aging control stock, a slow calibration drift, or a reagent nearing end-of-shelf-life — that a single pass/fail check won't catch until it's already an OOS result.
- **First question:** "Plotted over the last 10 plates, is the control trending, or just noisy?"
- **Data to pull:** the control value time series across recent runs (a Levey-Jennings-style chart), not just the most recent plate's pass/fail flag.
