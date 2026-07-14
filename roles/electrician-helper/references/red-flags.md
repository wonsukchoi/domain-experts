# Electrician Helper — Red Flags

### Box-fill calculation exceeds the mounted box's rated capacity by any margin
- **Usually means:** a standard box size was reused from elsewhere on the job without re-running the calc for this specific box's cable/device count; second most likely is an added device or splice that wasn't in the original take-off.
- **First question:** "How many cables and devices actually land in this box, and does that match what the box was picked for?"
- **Data to pull:** the box-fill worksheet for that specific box against NEC Table 314.16(A)/(B), re-run before mounting or before the cover goes on.

### Conduit fill calculated or estimated above 40% for three or more conductors
- **Usually means:** the conduit trade size was picked to match adjacent runs rather than calculated for this run's actual conductor count; second most likely is added conductors (a later circuit tap) that weren't in the original fill calc.
- **First question:** "What's the actual conductor count and trade size, and does that clear NEC Chapter 9 Table 1 at 40%?"
- **Data to pull:** the conduit-fill table for the trade size on hand against the actual conductor count and gauge.

### Wire pull stalls or shows rising resistance mid-pull with no lubricant applied
- **Usually means:** fill percentage is higher than assumed, or a bend exceeds practical friction limits; second most likely is a kink or snag at a coupling or box entry.
- **First question:** "Has lubricant been applied along this pull, and what's the fill percentage on this run?"
- **Data to pull:** none in the moment — stop, back off tension, apply lubricant, and re-check the fill calc before continuing.

### Total conduit bends between pull points approaching or exceeding 360° equivalent
- **Usually means:** bends were placed run-by-run without tracking the cumulative total; second most likely is a field routing change that added a bend without revisiting the plan.
- **First question:** "What's the running bend-degree total on this segment, and is a pull box needed before the next bend?"
- **Data to pull:** the bend-degree tracking log for the run against NEC 344.26.

### Reversed polarity or open ground on a plug-in tester at trim-out
- **Usually means:** a hot/neutral swap at a push-in or backstab connection during device landing; second most likely is a miswired splice upstream in a feed-through box.
- **First question:** "Does the GFCI trip-test still pass, and if so, does that mean the wiring is right — or just that GFCI protection works independently of polarity?"
- **Data to pull:** trace the circuit box-by-box from the panel, checking each termination, rather than re-testing the same device repeatedly.

### Non-contact voltage tester (NCVT) gives an inconsistent or ambiguous reading
- **Usually means:** induced voltage from an adjacent energized conductor, or proximity to grounded metal conduit suppressing the reading; second most likely is a low battery in the tester itself.
- **First question:** "Has this circuit been verified dead with a rated meter and lockout, or are we relying on the NCVT alone?"
- **Data to pull:** none from the NCVT itself — escalate to the electrician's rated-meter verified-dead check before any tool touches the conductor.

### Wire gauge staged or found on site doesn't match the breaker size on the panel schedule
- **Usually means:** a supply substitution or mislabeled reel; second most likely is a panel schedule that wasn't updated after a field change.
- **First question:** "Does this gauge match what's called out for this breaker size, and if not, which one is wrong — the wire or the schedule?"
- **Data to pull:** the panel schedule/circuit directory against NEC Table 310.16 ampacity for the gauge in hand.

### GFCI- or AFCI-required location staged with a standard (non-protected) device or breaker
- **Usually means:** the rough-in sheet's location wasn't cross-checked against NEC 210.8/210.12 before staging; second most likely is a substitution made when the correct device wasn't in stock.
- **First question:** "Is this location on the GFCI/AFCI-required list, and does the staged device or breaker match?"
- **Data to pull:** the rough-in sheet against the GFCI/AFCI required-location table before the box closes.

### Undocumented or abandoned wiring found in a wall, ceiling, or panel cavity
- **Usually means:** a prior renovation or trade left wiring in place without updating drawings; second most likely is active wiring that was never captured on the as-built.
- **First question:** "Is this energized, and does it change the load path or scope before anyone builds over it?"
- **Data to pull:** the as-built or permit drawing set for that area, and a verified-dead check before assuming it's inactive.

### Measured run length within about 5% of the wire reel's remaining footage before a pull starts
- **Usually means:** the take-off didn't account for actual routing length (bends, vertical drops) versus straight-line distance; second most likely is a reel that was already partially used on an earlier run.
- **First question:** "Is there a full reel or a splice kit staged as backup before this pull starts?"
- **Data to pull:** the reel's remaining footage against the measured run length, checked before the pull begins, not mid-pull.

### A termination or lug found "snug" but not torqued to a stated spec
- **Usually means:** a prior connection was hand-tightened without a torque driver/wrench; second most likely is a helper being asked to finish a termination that should have gone to the electrician.
- **First question:** "Is this a licensed termination task, and if so, why is it being asked of the helper?"
- **Data to pull:** none — this is a stop-and-escalate, not a task to complete solo regardless of how routine it looks.
