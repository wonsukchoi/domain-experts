# Vocabulary

### ACE (Area Control Error)
The real-time measure of a balancing authority's instantaneous imbalance, combining its interchange deviation from schedule and its contribution (via frequency bias) to system frequency deviation.
**In use:** "ACE is sitting at −280 — that's the number AGC is chasing back to zero, not the raw frequency reading."
**Common misuse:** Treating ACE and frequency deviation as the same thing — a BA can be at zero ACE while system frequency is still off-nominal (other BAs are carrying the correction), or carry significant ACE while frequency reads normal.

### Frequency bias (B)
A balancing authority's programmed MW-per-0.1-Hz setting used in the ACE formula, representing its expected generation response to a frequency deviation.
**In use:** "Our bias is set at −100 MW per tenth of a Hz — that's what the ACE calculation assumes we'll contribute before penalizing us for the rest."
**Common misuse:** Assuming frequency bias is a physical property of the generators rather than a programmed setting — a poorly tuned bias setting produces an ACE calculation that doesn't reflect the BA's actual response capability.

### N-1 contingency criterion
The reliability standard requiring the system to withstand the loss of its single largest credible contingency (generator, line, or transformer) without cascading failure.
**In use:** "We're at 140 MW of spinning reserve against a 400 MW N-1 requirement — we are not N-1 secure right now."
**Common misuse:** Treating N-1 compliance as a one-time check rather than a continuously monitored condition — reserve consumed by a real event or reduced by a dispatch decision can drop a system below N-1 secure without any alarm unless it's actively tracked.

### Most Severe Single Contingency (MSSC)
The single largest generation resource or import a balancing authority relies on, which sets its minimum required contingency reserve under NERC standards.
**In use:** "Gen Unit 4 is our MSSC at 400 MW — that's why our reserve floor is 400, not some smaller number."
**Common misuse:** Assuming reserve requirements are a flat percentage of load — they're set by the single largest contingency exposure, which can be far smaller or larger than a percentage-of-load rule of thumb would suggest.

### AGC (Automatic Generation Control)
The real-time control system that automatically adjusts online generating units' output to correct ACE and maintain scheduled interchange and frequency.
**In use:** "AGC picked up the full 280 MW deviation and closed it out in eight minutes — no manual intervention needed."
**Common misuse:** Assuming AGC alone restores reserve after deploying it — AGC corrects ACE using available regulating capacity; restoring the reserve it consumed is a separate action (committing additional capacity), not something AGC does automatically.

### Spinning reserve
Generating capacity that is online, synchronized to the grid, and able to respond within minutes to a contingency — distinct from offline or slower-starting capacity.
**In use:** "We've got 420 MW of spinning reserve online right now, which covers our 400 MW N-1 requirement with 20 MW to spare."
**Common misuse:** Conflating spinning reserve with total reserve margin — non-spinning (fast-start) capacity counts toward some reserve categories but responds on a different, slower timescale and can't be substituted for spinning reserve in the first minutes of an event.

### Reactive power (VARs)
Power that oscillates between source and load without doing net work, but that's required to maintain voltage across a system — distinct from real power (MW), which does the actual work.
**In use:** "Voltage on that corridor is sagging because we're VAR-starved, not MW-starved — pushing more real power through it will make the voltage worse, not better."
**Common misuse:** Treating "power" as a single undifferentiated quantity — real and reactive power are managed with different tools (AGC/reserve for real power, capacitor banks and generator AVR settings for reactive power) and a fix aimed at one doesn't address the other.

### Voltage collapse
A cascading, nonlinear loss of system voltage driven by insufficient reactive power support relative to real power demand on a transmission path, distinct from a frequency-driven instability.
**In use:** "That corridor was on the edge of voltage collapse — every capacitor bank we had was already switched in and VAR reserve was near zero."
**Common misuse:** Treating a low-voltage reading as automatically the same type of problem as a low-frequency reading — the causes, dynamics, and corrective tools for the two are almost entirely distinct.

### UFLS (Underfrequency Load Shedding)
An automatic, staged protection scheme (per NERC PRC-006) that sheds firm load at pre-set frequency thresholds (commonly beginning near 59.5 Hz) to arrest a frequency decline before it cascades into a wider blackout.
**In use:** "We never want to see UFLS actually engage — reaching that threshold means every prior response stage already failed to hold frequency."
**Common misuse:** Treating UFLS as a planned response tool rather than a last-resort automatic protection — a dispatcher managing an event toward UFLS thresholds has already exhausted the intended response ladder, not executed a deliberate strategy.

### Disturbance Control Standard (DCS) — NERC BAL-002
The NERC standard requiring a balancing authority to return its ACE to zero (or its pre-disturbance level) within 15 minutes following a Reportable Balancing Contingency Event.
**In use:** "We closed ACE in eight minutes — well inside the fifteen-minute DCS window for that event."
**Common misuse:** Treating DCS compliance (ACE recovery) as equivalent to full event resolution — DCS governs ACE recovery time specifically, not whether contingency reserve has been restored to its required level afterward, which is a separate obligation.

### Net interchange (scheduled vs. actual)
The scheduled (NIS) versus actual (NIA) net flow of power across a balancing authority's ties with neighboring systems; the gap between them is one of the two components of ACE.
**In use:** "NIA came in 200 MW below schedule — that's the interchange component of our ACE deviation, separate from the frequency-bias component."
**Common misuse:** Reading an interchange deviation alone as the full picture of a BA's imbalance — ACE also includes the frequency-bias term, and a BA can look fine on interchange while still carrying significant ACE from the frequency component, or vice versa.
