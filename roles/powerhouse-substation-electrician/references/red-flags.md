# Red flags

Smell tests a relay/substation technician catches before a switching order is executed, a relay is signed off, or a transformer's DGA report is filed without further action. Each entry: what it usually means, the first question a veteran asks, and the data to pull before proceeding.

### TDCG rate of rise exceeds roughly 30 ppm/day between successive samples, even though the absolute level is still Condition 1 or 2

**Usually means:** a developing fault is gassing faster than the condition-band snapshot reflects — the band alone won't flag this until it crosses the next threshold, which may be well after the fault has worsened.
**First question:** "What's the ppm/day rate since the last sample, not just today's condition band?"
**Data to pull:** the last two DGA lab reports with sample dates, TDCG and individual gas values for both, and the transformer's prior 12–24 month trend.

### Acetylene (C2H2) present or increasing between samples

**Usually means:** an active arcing fault, distinct from the ethylene/ethane-dominant pattern of a purely thermal fault — a different urgency and root cause than "the transformer is aging."
**First question:** "Is acetylene actually rising, or is this within normal lab measurement variation for this transformer's baseline?"
**Data to pull:** the specific C2H2 values and dates for at least the last two samples, any coincident protection-scheme alarms (sudden-pressure, differential), and load/loading history over the same window.

### Protective relay approaching or past its NERC PRC-005 maintenance interval with no functional test on record

**Usually means:** the relay hasn't had a verified-correct pickup/timing test in close to its full compliance window — not yet non-compliant, but the margin for a fault occurring on unverified protection is shrinking.
**First question:** "How many months into this relay's interval are we, and has anything changed (misoperation elsewhere, a DGA concern on the protected equipment) that should move this test up?"
**Data to pull:** the relay's last test date and applicable PRC-005 table interval for its type/monitoring level, and any recent condition changes on the equipment it protects.

### Relay pickup test passes tolerance but timing test result is reported as an average or "close enough" pass

**Usually means:** someone is treating pickup and timing as one combined score instead of two independent pass/fail criteria — a relay that trips at the right threshold but at the wrong time still breaks coordination with its neighbors.
**First question:** "What was the timing result specifically, against what tolerance, independent of the pickup result?"
**Data to pull:** the test report's separate pickup and timing values against the setting sheet's specified tolerances for each.

### Coordination time interval between two adjacent relay curves comes out below roughly 0.2–0.3 seconds at maximum fault current

**Usually means:** the margin meant to cover breaker interrupting time and relay overtravel has been eroded, likely by an independent setting change on one of the two relays without re-checking the pair.
**First question:** "Was this pair's coordination re-verified after the last setting change on either relay, or just the individual relay's own test?"
**Data to pull:** current TCC plots for both relays at the fault current in question, and the change log for settings on either device.

### Switching order for a substation bus reconfiguration has not been independently verified by a second qualified person

**Usually means:** the order is being executed on the originator's read of the one-line alone — the most common precursor to operating the wrong device on a multi-source bus.
**First question:** "Who independently checked this switching order against today's actual bus configuration, not just the standard one-line?"
**Data to pull:** the switching order document, the as-built one-line with today's bus-tie and source status, and the second reviewer's sign-off.

### Breaker mechanism work begins after electrical lockout/tagout with no confirmation of stored mechanical/pneumatic energy status

**Usually means:** the crew is treating "electrically dead and grounded" as equivalent to "mechanically safe," skipping the separate spring/SF6/hydraulic energy check this equipment requires.
**First question:** "Is the closing spring discharged or blocked, and has SF6/hydraulic pressure been isolated per the manufacturer procedure — separately from the electrical lockout?"
**Data to pull:** the breaker manufacturer's stored-energy release procedure and the job briefing's specific sign-off line for it, not just the electrical LOTO log.

### A relay misoperation is closed out after correcting the single flagged relay, with no scheme-level review

**Usually means:** the investigation stopped at the symptom (one relay's incorrect operation) without checking whether a shared cause — CT wiring, a coordination gap, a setting applied scheme-wide — will reproduce the same misoperation on the next fault.
**First question:** "Was this misoperation's root cause traced to this relay specifically, or could it recur on a device that wasn't touched?"
**Data to pull:** the PRC-004 misoperation report, fault records for the event, and the coordination study covering every device that saw the fault current.

### Arc-flash PPE category is selected from voltage class alone for switchgear or a breaker compartment

**Usually means:** someone is applying the outdoor-line PPE-selection habit (voltage class → category) to enclosed equipment, where incident energy depends on gap distance, enclosure geometry, and clearing time — not voltage alone.
**First question:** "What does the equipment-specific IEEE 1584 study say for this compartment, and is it current against present relay settings?"
**Data to pull:** the arc-flash study document and its date, cross-checked against the last date any upstream protective device's clearing time was changed.

### DGA resample interval is extended to the standard annual cycle despite a condition trending upward

**Usually means:** the condition band, not the trend, is driving the sampling decision — a common error when a report is read for its current category label rather than its trajectory.
**First question:** "Is this trend flat, or has it moved bands (or moved fast within a band) since the prior sample?"
**Data to pull:** at least three prior DGA reports in sequence to establish trend direction, not just the most recent one.

### Station battery float voltage or internal ohmic reading is out of the manufacturer's specified range

**Usually means:** the DC control power that trips the breaker may not be reliable at the moment it's needed, independent of how well the protective relay itself is set and tested.
**First question:** "When was this battery's float voltage and internal ohmic value last checked against spec, and is a capacity test overdue?"
**Data to pull:** the battery maintenance log (float voltage checks, ohmic/impedance test dates) and the applicable PRC-005 interval for battery testing at this monitoring level.
