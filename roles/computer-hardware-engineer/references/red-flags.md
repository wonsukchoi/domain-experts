# Red flags — what a computer hardware engineer notices instantly

Smell tests with thresholds. Any one can be innocent; two or three together in the same layout or sim result is a pattern worth stopping the review for.

### Timing closure report shows setup/hold slack at typical corner only, no PVT sweep
- **Usually means:** the STA run used default (nominal) library corners instead of the slow-slow/min-voltage/max-temperature corner the shipped part will actually see — a design can show 165 ps of typical-corner slack and still fail at worst-case corner once skew and jitter are subtracted.
- **First question:** "What's the setup and hold slack at the slow-slow, minimum-voltage, maximum-temperature corner, with vendor skew and jitter numbers included?"
- **Data to pull:** the multi-corner STA report and the vendor's published skew/jitter numbers used (or not used) in the margin calculation.

### Decoupling cap bank copied from a prior board's reference design with no Ztarget recalculation
- **Usually means:** the new load's transient current step or rise time differs from the reference board's, and the copied cap count no longer holds the actual Ztarget across the actual Fknee band — a slower reference design's "working" cap count can be 4x under-provisioned for a faster load.
- **First question:** "What's this rail's ΔI, ripple budget, and current-edge rise time, and does the cap bank's impedance curve clear Ztarget at Fknee?"
- **Data to pull:** the vendor power-delivery guideline for the actual part, and a PDN impedance-vs-frequency sim (SIwave or equivalent) for the specific cap bank as placed.

### High-speed via with no back-drill callout on the fab drawing
- **Usually means:** the stub-length-vs-resonant-frequency check was never run, or was run pre-layout and never re-checked against final via/plane assignment — an unaddressed stub produces a resonant notch in the eye diagram independent of how clean the routed trace itself measures.
- **First question:** "What's the unused stub length on this via, and does its quarter-wave resonant frequency fall inside the signal's knee-frequency band?"
- **Data to pull:** the stack-up drawing showing via length vs. signal-layer position, and the stub-resonance calculation for the longest unaddressed stub.

### θJA used for heatsink sizing sourced from the datasheet's open-air JEDEC test condition
- **Usually means:** the actual enclosure's airflow and ambient differ from the JEDEC 2s2p open-air test board condition the datasheet θJA was measured under — a fanless or low-airflow enclosure can run 15-20°C hotter than the test condition assumed, silently eating the thermal margin a spec-sheet comparison implied existed.
- **First question:** "What airflow and ambient temperature was this θJA measured at, and does it match the actual enclosure's worst-case condition?"
- **Data to pull:** the datasheet's stated test condition (LFM airflow, ambient) and the enclosure's actual worst-case thermal/airflow spec.

### DDR byte-lane DQ-to-DQS length matching exceeds the interface spec's stated tolerance (commonly ±10 mils for DDR4)
- **Usually means:** autorouter length-matching wasn't constrained per-byte-lane, or was constrained to a generic board-wide tolerance instead of the specific interface spec's per-lane requirement.
- **First question:** "What's the actual DQ-to-DQS mismatch on the worst lane, against the interface spec's stated tolerance?"
- **Data to pull:** the length-matching report from the layout tool, broken out by byte lane, against the JEDEC spec's stated tolerance for this data rate.

### Trace-to-trace spacing on a high-speed bus is below 3x trace width with no interface-specific crosstalk sim to justify it
- **Usually means:** the 3W spacing rule was skipped for routing density without checking whether the actual coupled length and edge rate make crosstalk a real risk at that spacing — sometimes justified, but only with a sim showing NEXT/FEXT within budget.
- **First question:** "What's the simulated near-end and far-end crosstalk at this spacing and coupled length, against the interface's crosstalk budget?"
- **Data to pull:** the SI crosstalk sim result and the interface spec's stated crosstalk tolerance (often expressed as a % of signal swing).

### A signal's return path crosses a split or gap in the adjacent reference plane
- **Usually means:** a plane was split for power-domain isolation without checking which high-speed signals route directly above the split — the return current has to detour around the gap, increasing loop inductance and radiated EMI regardless of how the signal trace itself was routed.
- **First question:** "Does this trace's return-current path stay on a single continuous plane for its full length, and if not, is a stitching via placed at the crossing?"
- **Data to pull:** the plane-layer artwork overlaid with the signal-layer routing for the specific net in question.

### IR drop on a power plane exceeds roughly 3-5% of rail voltage at max current with no plane-copper sizing calculation shown
- **Usually means:** plane copper weight and pour width were set by routing convenience rather than a current-capacity and IR-drop calculation — a plane that looks continuous in the layout viewer can still starve a far corner of the board under max load.
- **First question:** "What's the calculated IR drop from the VRM to the farthest load point at max current, and does it clear the rail's noise budget?"
- **Data to pull:** the plane current-density/IR-drop sim (or hand calc from copper weight, width, and length) at worst-case load current.

### BGA via-in-pad fab note is missing or doesn't specify fill-and-cap
- **Usually means:** the fab drawing was generated from a generic layer stack template without a design-specific fab-note review — an unfilled via-in-pad on a fine-pitch BGA risks solder voiding during reflow, a defect that doesn't show up until assembly yield drops.
- **First question:** "Does the fab drawing explicitly call out fill-and-cap (or equivalent) for every via-in-pad under this BGA?"
- **Data to pull:** the fab drawing's via-in-pad note and the BGA's pitch (fill-and-cap is close to mandatory below ~0.8 mm pitch).

### Clock jitter budget on a report cites only RMS jitter, not the interface's actual peak-to-peak requirement
- **Usually means:** RMS jitter was reported because it's the easier number to pull from the clock vendor's datasheet, but the timing budget requires peak-to-peak (or RMS × a stated sigma multiplier) — reporting RMS alone understates the actual timing impact.
- **First question:** "What sigma multiplier does the interface spec require for jitter, and was that multiplier applied before subtracting it from setup/hold margin?"
- **Data to pull:** the clock vendor's jitter datasheet (RMS figure) and the interface spec's required sigma multiplier for peak-to-peak conversion.

### Post-fab TDR impedance measurement is more than ~10% off the simulated target with no stack-up recheck
- **Usually means:** actual dielectric constant, copper thickness, or etch factor from the fab run diverged from the stack-up model used in pre-fab simulation — a common gap between "what the simulator assumed" and "what the fab house actually built."
- **First question:** "Does the fab house's actual impedance-coupon measurement match what was specified, and if not, was the stack-up model updated for the next spin?"
- **Data to pull:** the fab house's impedance-coupon test report against the specified target and tolerance.
