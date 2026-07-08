# Hardware-engineering working vocabulary

Terms a computer hardware engineer uses daily and precisely. Format: definition → how a practitioner says it → common misuse.

**Rise time (Tr)** — The time for a digital signal to transition (commonly 10%-90%) between its low and high states; determines the signal's knee frequency and therefore how much of the board it treats as a transmission line.
**In use:** "Driver's Tr is 150 ps, so Fknee is 2.33 GHz — that's the frequency we design the stack-up to, not the 2400 MT/s data rate itself."
**Misuse:** using the interface's nominal clock or data rate as the frequency to design SI margin around, instead of the much higher knee frequency implied by the actual edge rate.

**Knee frequency (Fknee)** — The frequency above which a digital signal's harmonic content is negligible for practical SI analysis, approximated as 0.35/Tr.
**In use:** "Fknee at 500 ps rise time is 700 MHz — that's the top of the band our PDN target impedance has to hold across."
**Misuse:** confusing knee frequency with clock frequency; a slow clock with a fast edge rate still has a high knee frequency and demands transmission-line treatment.

**Characteristic impedance (Z0)** — The impedance a transmission line presents to a signal based on trace geometry and dielectric properties, independent of trace length; a mismatch against the driver/receiver or connector impedance causes reflections.
**In use:** "Stack-up is tuned for 40 Ω single-ended, 80 Ω differential on the DQ/DQS layer — that's what the fab coupon has to measure to within ±10%."
**Misuse:** treating impedance as a stack-up constant that doesn't need per-net verification; etch variation and local geometry changes (necking near a via) shift local impedance even on a nominally-controlled layer.

**Via stub** — The unused portion of a plated via barrel beyond the layer where the signal actually transitions, left electrically connected but functionally dead.
**In use:** "60 mil stub on this via resonates around 2.75 GHz — inside our knee-frequency band, so it's getting back-drilled."
**Misuse:** assuming a stub is harmless because the routed trace itself measures clean in isolation — the stub is a separate resonant structure, not a property of the trace.

**Back-drilling** — A secondary drilling operation that removes the unused via stub after the primary plating step, eliminating the stub's resonant reflection.
**In use:** "Back-drill depth is called out per via on the fab drawing, targeting a residual stub under 10 mils."
**Misuse:** treating back-drilling as automatic or default fab behavior — it must be explicitly specified per via, with a target residual stub length, or the fab house won't apply it.

**PDN (power delivery network)** — The combined path (VRM, planes, decoupling capacitors, package, die) that delivers current to a load while holding rail voltage within its ripple budget under transient current demand.
**In use:** "PDN impedance sweep shows a resonant peak at 60 MHz, right where our cap bank's SRF gap sits — that's the droop risk."
**Misuse:** treating "PDN" as synonymous with "decoupling caps" alone; the VRM, plane geometry, and package/die parasitics are all part of the same impedance path.

**Target impedance (Ztarget)** — The maximum PDN impedance, at any frequency in the relevant band, that keeps rail ripple within budget for a given transient current step: Ztarget = ΔVallowed / ΔImax.
**In use:** "Ztarget comes out to 3.375 mΩ for this rail — every point on the impedance-vs-frequency curve up to 100 MHz has to clear that."
**Misuse:** computing Ztarget once from a steady-state current instead of the actual transient step current, which understates the real requirement.

**ESL (equivalent series inductance)** — The parasitic inductance of a capacitor and its mounting (pad, via, trace), which sets the frequency above which the cap's impedance rises again instead of continuing to fall.
**In use:** "Mounted ESL on this 0402 is 0.5 nH — that's what sets its self-resonant frequency, not the datasheet's bare-component spec."
**Misuse:** using the capacitor manufacturer's bare-component ESL figure without adding mounting (via/pad) inductance, which is often a comparable or larger contributor at board level.

**Self-resonant frequency (SRF)** — The frequency at which a capacitor's ESL and capacitance form a series resonance, below which the cap looks capacitive and above which it looks inductive.
**In use:** "SRF on this cap is 22.5 MHz — above that, adding more of the same cap value doesn't lower impedance the way it did below SRF."
**Misuse:** assuming a single capacitor value can cover a PDN's entire frequency band; every value has a bounded useful range around its SRF, which is why decoupling banks span multiple decade-spaced values.

**IR drop** — The voltage drop across a power plane's resistance between the source (VRM) and a load, proportional to current and plane resistance.
**In use:** "IR drop to the farthest corner load is 4.1% of rail voltage at max current — inside our 5% budget, but tight."
**Misuse:** assuming a wide, continuous-looking copper pour has negligible IR drop without calculating actual resistance from copper weight, width, and length at the specific current level.

**Crosstalk (NEXT/FEXT)** — Coupled noise induced onto a victim trace by an aggressor trace running parallel to it; NEXT (near-end) appears at the aggressor's driver end, FEXT (far-end) at the receiver end, and both scale with coupled length and inverse spacing.
**In use:** "FEXT sim on this 0.5 in coupled run at 4-mil spacing comes in at 6% of swing — inside our 8% crosstalk budget."
**Misuse:** applying a blanket spacing rule (3W) without checking coupled length and edge rate against the interface's actual crosstalk budget — sometimes tighter spacing is fine, sometimes 3W isn't enough on a long coupled run.

**Return path** — The path return current takes back to its source through the nearest reference plane, which sets loop inductance and radiated emissions independent of the signal trace's own routed path.
**In use:** "Return path crosses the plane split under U4 — needs a stitching via or it's an EMI and SI risk both."
**Misuse:** reasoning about a signal's path length or impedance without considering its return current's actual path, treating the trace as if current flows in isolation from its return.

**Setup time / hold time** — The minimum interval before (setup) and after (hold) a clock edge during which data must be stable for a flip-flop or memory device to sample it correctly.
**In use:** "Worst-case setup slack is 92 ps after subtracting PVT skew and jitter from the 416.7 ps UI — that's the number that governs sign-off."
**Misuse:** reporting setup/hold slack at typical corner only, without subtracting worst-case skew and jitter, which can turn a comfortable-looking typical-corner number into a failure at the actual shipped corner.

**Junction temperature (Tj)** — The actual operating temperature at a semiconductor die's junction, computed as Tj = Tambient + Pdissipated × θJA (or θJC + θCA with a heatsink), and the real constraint a thermal design has to satisfy — not TDP or ambient temperature alone.
**In use:** "Tj comes out to 98.2°C with the larger heatsink at worst-case ambient — 6.8°C under the 105°C max, but flag it as tight."
**Misuse:** checking TDP against the datasheet's rated power without computing actual Tj at the system's real ambient and airflow condition, which is the number that actually determines pass/fail.

**Thermal resistance (θJA / θJC / θSA)** — The temperature rise per watt of dissipated power across a defined path: junction-to-ambient (θJA, whole path), junction-to-case (θJC, die to package surface), sink-to-ambient (θSA, heatsink to air) — summed in series to compute total path resistance with a heatsink in the loop.
**In use:** "θJA on the datasheet is measured on a JEDEC 2s2p board with no airflow — our enclosure's real number, with the heatsink, is θJC+θCS+θSA."
**Misuse:** using the datasheet's bare-package θJA (measured under JEDEC's standard test board and airflow condition) as if it applies unchanged to a heatsinked part in a different enclosure.
