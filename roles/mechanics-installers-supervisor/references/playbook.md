# Playbook

Filled worksheets and procedures for the three recurring supervisor tasks: attributing a comeback pattern, job-costing a redo, and running a compliant lockout/tagout on a multi-technician job.

## 1. Comeback attribution worksheet

Run this before deciding whether a pattern is technique or parts. Populate row by row — don't skip to a conclusion.

| Step | Question | Example answer (rotor comeback case) |
|---|---|---|
| 1 | Which technician(s) and job/part combination show elevated comebacks? | Mike R., front rotor/pad replacement |
| 2 | Technician's comeback rate on this job type this period | 6/95 ROs = 6.3% (shop avg 2.3%) |
| 3 | Same-SKU comeback rate for this technician specifically | 5/14 rotor jobs = 35.7% |
| 4 | Same-SKU comeback rate for all other technicians combined | 0/26 rotor jobs = 0% |
| 5 | Conclusion rule | Elevated for one tech, flat for the rest on the identical SKU/lot → **technique**. Elevated across technicians on one SKU/lot → **parts**. Elevated across technicians on multiple SKUs from one supplier → **parts, supplier-wide**. |
| 6 | Verification before closing | Pull the specific repair procedure (torque spec, run-out tolerance, bed-in steps) and confirm the technician's install matches or deviates from it. |

**Parts-side branch:** pull the supplier lot/batch number from the parts-return log, quarantine remaining stock from that lot, and file a supplier claim citing part numbers, lot codes, and the specific failure mode (not "some rotors are bad").

**Technique-side branch:** pull the technician's ASE certification and training record for that job category before assuming a training gap exists — a certified, experienced technician with a sudden pattern often points to a rushed job (schedule pressure, a specific bay's tool calibration) rather than a skill gap, and the fix differs.

## 2. Job-costing a comeback/redo

Reconcile every no-charge redo this way before deciding on coaching versus discipline — the cost number, not the incident count, sizes the decision.

**Worksheet (rotor comeback case, 5 jobs):**

| Line | Calculation | Amount |
|---|---|---|
| Labor opportunity cost | 5 jobs × 1.2 flat-rate hrs = 6.0 hrs redo time × $165/hr door rate | $990.00 |
| Parts absorbed (salvageable) | 3 of 5 rotors re-torqued, no part cost | $0.00 |
| Parts absorbed (replaced) | 2 rotor sets × $52/set shop cost | $104.00 |
| Redo pay to technician | 6.0 hrs × $22/hr shop rework-pay rate | $132.00 |
| **Total cost of pattern** | | **$1,226.00** |

**Rework-pay policy note:** most shops pay redo/comeback labor at a reduced flat rate (commonly 30–50% of the technician's normal flat-rate equivalent) rather than zero, to avoid a wage-floor violation — verify the specific shop's written policy and the state's piece-rate minimum-wage rule before assuming $0 is compliant.

**Warranty vs. goodwill branch:** if the original repair was itself a warranty repair (OEM-covered), redo labor is billed back to the manufacturer at the warranty labor rate, not absorbed by the shop — but the manufacturer's own audit will flag a comeback-on-warranty-work pattern faster than an internal one, since it shows up in their chargeback data across shops.

## 3. Group lockout/tagout procedure for simultaneous multi-technician work

Use whenever more than one technician is working on the same vehicle, lift, or piece of equipment at the same time — regardless of job length.

1. **Identify every energy source** on the job: engine (mechanical/electrical), lift hydraulics, battery/12V or high-voltage system on hybrids/EVs, air suspension, stored spring energy (coil springs under load, driveshaft tension).
2. **Each authorized technician isolates and applies their own lock and tag** to the energy-isolating device relevant to their task — never one supervisor or lead lock standing in for the crew. A technician under the vehicle and a technician at the dash each lock independently.
3. **Verify zero energy state** before work starts: attempt a normal start/operation with all locks in place to confirm isolation, then return controls to neutral/off.
4. **No lock is removed until that technician's task is fully complete** and they personally verify the area is clear — a technician who finishes early does not remove another technician's lock.
5. **Log the lockout on the RO or a dedicated LOTO log**: date, vehicle, technicians involved, energy sources isolated, verification method used.
6. **Group lockout device (lock box) for 3+ technicians:** if the crew regularly exceeds two technicians on one job (e.g., a driveline job with a lift operator, a technician underneath, and a technician at the transmission), use a lockout box where each technician's individual lock secures the box, and the box itself holds the master key to the isolating devices — no technician can be locked out of the ability to protect themselves.
7. **Minor-servicing exception is narrow:** OSHA's minor-servicing exception (routine, repetitive, integral to production, using alternative measures that provide effective protection) rarely applies to a shop repair job outside a fixed assembly-line context — default to full lockout unless a written program specifically documents why a task qualifies for the exception.
