# Playbook

Operational sequences a service unit operator actually runs, with structure, thresholds, and example numbers. Starting points to adapt to the job order and local regulation, not scripts.

## 1. Rig-up and pre-job well check

Run in this order every time, regardless of how routine the lease feels.

1. **Pull the well file and the last kill/completion record** — fluid weight last used, TVD, known pressures, perforation or plug depths on record. Treat it as a prediction to verify, not a fact.
2. **Match wellhead/BOP rating to anticipated pressure.** Example: wellhead rated 3,000 psi working pressure, well's historical SICP has run up to 600 psi with one build-back event recorded at 900 psi → rig up the 3,000# stack, not a lighter one "because this well's always low."
3. **Spot and level the unit; verify anchor points and guy-line tension before raising the mast.** A mast raised out of level loads the drawworks and derrick legs unevenly under pull.
4. **Nipple up the BOP stack; function-test blind rams, pipe rams, and annular (if fitted) before breaking the first connection** — cycle each ram closed and open against test pressure per the job's rating, log the test.
5. **Bleed down the well at the master valve; hold a 10–15 minute observation period; re-check.** Zero-then-hold = confirmed dead. Zero-then-build-back = trapped pressure, kill required before proceeding (see §3).
6. **Only after the well reads dead and holds, begin breaking down the tree/wellhead connections for tubing/rod work.**

## 2. Tubing/rod tally — filled example

The tally, not the well file, is the record of truth for depth. Build it live as pipe comes out; reconcile at the end.

**Baker 4 tubing pull, 2⅜" tubing, nominal joint length ~31 ft (actual varies per joint):**

| Stand # | Joints | Measured length (ft) | Running total (ft) | Note |
|---|---|---|---|---|
| 1–10 | 10 | 309.4 | 309.4 | |
| 11–20 | 10 | 310.1 | 619.5 | |
| 21–30 | 10 | 308.8 | 928.3 | |
| ... | ... | ... | ... | |
| 196–198 | 3 | 92.6 | 6,141.2 | last full stand |
| — | 1 pup joint | 8.9 | 6,150.1 | landing pup + seating nipple |

**Reconciliation:** well file lists tubing landed at 6,148 ft (last completion record, 2019). Fresh tally comes in at 6,150.1 ft — a 2.1 ft difference, within normal tally tolerance (typically ±3–5 ft over 6,000+ ft from joint-length variance and prior thread makeup). Difference beyond that band (say, >15–20 ft) is a flag to stop and reconcile against a gamma-ray/collar log tie-in before setting a plug or perforating off the tally alone, not to average the two numbers and proceed.

**Plug-setting depth call:** target zone top at 6,020 ft (from the completion log). Set bridge plug at 5,980 ft — 40 ft above the zone top, using the fresh tally as the reference depth, not the 2019 file number.

## 3. Kill-fluid decision sequence (trapped-pressure or kick response)

1. **Confirm the well is not dead** (bleed-and-hold shows build-back, or a swab/pull job shows unplanned flow).
2. **Record SICP (shut-in casing pressure) or SITP (shut-in tubing pressure), whichever is relevant to the job), and TVD.**
3. **Calculate required kill weight:**
   `KWM (ppg) = current fluid weight (ppg) + SICP (psi) / (0.052 × TVD (ft))`
4. **Add a standing trip/safety margin** (commonly 0.2–0.5 ppg per company procedure) to the calculated KWM before mixing/ordering fluid.
5. **Choose kill method based on known or estimated injectivity:**
   - **Lubricate-and-bleed** — default when injectivity into the perforated zone is unknown or low; alternately pump kill fluid in at the top and bleed gas/fluid off at the choke in small increments until surface pressure reaches zero. Slower, safer for an unknown formation.
   - **Bullhead** — default only when the zone is known to take fluid readily (established injectivity from a prior job) and getting weighted fluid to bottom quickly matters more than precision; pumping into a zone that won't take fluid risks breaking down the formation at surface pressure instead of controlling downhole pressure.
   - **Volumetric method** — default when there's no fluid supply to bullhead or lubricate with (e.g., gas well with no liquid kill fluid readily available) and the well must be controlled by bleeding gas in metered increments while tracking wellbore volume.
6. **Call out a pump/kill truck** — a standard pulling unit has no circulating capability of its own; this is a scheduling and cost item to flag to the company representative immediately, not something to work around.
7. **Kill, then re-run the bleed-and-hold check from §1 step 5 before resuming the job** — a completed kill operation gets the same verification a routine dead-well check gets, not an assumption it worked.

## 4. Stuck-pipe response sequence

1. **Stop pulling the instant hookload spikes or drag pattern changes** — don't continue applying force while "figuring out what happened."
2. **Work the string in measured increments** (jar up/down, rotate if rod string) **up to the pre-set overpull limit** — commonly ~80% of the string's rated body yield strength, calculated from pipe grade and wall thickness, not a round number picked on the day.
3. **If the string frees within that margin, resume the pull at normal rate**, logging the depth and cause (fill, scale, differential sticking) for the job record.
4. **If the string does not free within the overpull margin, stop and call for a free-point tool** to locate the stuck point before any further pulling — pulling blind past the limit is how a string that could have been fished intact gets parted instead.
5. **Once free-pointed, decide fish vs. back-off vs. abandon-in-place** based on: value of the string and zone below the stuck point, estimated fishing cost and time, and whether a second stuck point is likely (repeat fill/scale conditions). Escalate the cost comparison to the company representative in dollar terms, not "we should keep trying."
6. **Track cumulative fishing cost against the interval's value explicitly** — the point to stop is an economic threshold, not a morale call, and it should be named out loud before the crew is three days into a job that started as a one-day pull.

## 5. Swab job — controlled unload

1. **Confirm well is dead per §1 before rigging swab equipment**, same as any other pulling job.
2. **Run swab at a controlled speed** matched to expected fluid-level recovery rate — too fast increases drawdown past what the crew is prepared to control if it triggers unplanned inflow.
3. **Track fluid level and recovered volume per run**; compare against the well's known productivity — a run that recovers far more or far less than expected is diagnostic before it's a completion decision.
4. **If gas or unexpected fluid shows at surface during a swab run, stop swabbing and shut in** — treat as a well-control event and re-enter the bleed-and-hold sequence, not as "the well's finally kicking off, that's good."
