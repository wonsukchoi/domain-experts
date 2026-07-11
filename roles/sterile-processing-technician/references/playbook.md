# Playbook

Filled workflow templates a sterile processing tech actually runs, with real thresholds and sequence. Adapt to facility policy and each device's IFU — these are structured starting points, not a substitute for either.

## 1. Decontamination sequencing

Order matters; skipping or reordering a step is the single most common source of a downstream sterilization failure.

1. **Point-of-use pretreatment** (in the OR, before transport): gross soil wiped, lumens flushed, instruments kept moist (foam spray or damp towel) so soil doesn't dry and bake on during transport. Dry-transport delay beyond roughly 1 hour raises the odds soil hardens past what enzymatic soak alone will lift.
2. **Sorting and disassembly** at the decon sink: box locks opened, multi-part instruments broken down to manufacturer spec — a closed box lock is the most common cause of an instrument coming out "clean" on the outside and soiled inside the joint.
3. **Enzymatic pre-soak**: soak time per the instrument's own IFU — commonly 1–3 minutes for general stainless, longer (5–15 min) for lumened or powered equipment per that device's IFU. A department-wide "2 minutes for everything" default is only a fallback when the tray tag doesn't specify, never an override of a stated device IFU.
4. **Manual brushing under water** (not air, to avoid aerosolizing bioburden), lumens brushed with a brush sized to the lumen diameter per IFU — an undersized brush leaves an inner channel of soil that no downstream step recovers.
5. **Ultrasonic cleaning**: tank degassed 2–5 minutes before the first load of the day (a non-degassed tank cavitates against dissolved air instead of soil); cycle time and detergent per manufacturer spec, instruments fully submerged and hinges open.
6. **Automated washer-disinfector**: thermal disinfection validated to an A0 value of 600 or higher (per ISO 15883 — roughly equivalent to 90°C for 1 minute, or a longer time at a lower temperature on the same A0 curve).
7. **Drying and inspection**: function-tested (box locks, cutting edges, insulation integrity on electrosurgical instruments checked for pinholes), borescope-inspected for lumened devices. Any instrument that fails function test is pulled, tagged, and routed to repair — it does not go back in the tray "for this case."

## 2. Tray assembly and count protocol

**Count sheet reconciliation, filled example (general laparotomy tray, 62-piece count):**

| Step | Action | Discrepancy trigger |
|---|---|---|
| 1 | Assembler counts against count sheet, item by item | Any miss on first pass |
| 2 | Second technician independently re-counts the full tray (not just the missing item) | Second count disagrees with first |
| 3 | Search decon area, washer racks, and ultrasonic basket for the missing item | Not found after one search cycle |
| 4 | Escalate to SPD lead; tray held, does not go to sterilization | Item still missing |
| 5 | Document count discrepancy, corrective tray substitution if OR needs the set urgently | — |

**Rule:** a discrepancy is never resolved by a single re-counter, and a tray with an unresolved discrepancy does not get sterilized "to not fall behind" — an instrument found later in a drain or a patient is a retained-surgical-item event, not a paperwork correction.

## 3. Sterilizer load and release rules by device class

| Load type | Monitoring required before release | Typical cycle (steam, gravity) | Typical cycle (steam, pre-vac) |
|---|---|---|---|
| Routine non-implant instrument set | Physical monitor (printout) + Class 5/6 chemical indicator in the load; BI run concurrently but load may release on CI while BI incubates | 250°F (121°C), 30 min wrapped | 270°F (132°C), 4 min wrapped |
| Implant-containing tray (e.g., ortho screws, plates) | **BI result required before release** — rapid-readout (1–4 hr) or standard culture; load does not release on CI alone regardless of urgency | Same parameters, BI mandatory | Same parameters, BI mandatory |
| Immediate-use steam sterilization (IUSS/"flash") | Documented clinical justification (no reasonable substitute set exists); CI + physical monitor; used as exception, not routine coverage for shortages | 132–135°C, 3–4 min, unwrapped, minimal or no drying | Same |
| Low-temperature (H2O2 gas plasma / EtO) | Chemical + biological indicator per that sterilizer's validated cycle; EtO requires aeration time before handling | Per manufacturer validated cycle | Per manufacturer validated cycle |

**Rule of thumb:** any load carrying an implant holds for BI confirmation, full stop, regardless of how fast a rapid-readout system reports — the requirement is the hold, not the readout speed.

## 4. Biological indicator failure — recall protocol

1. **Confirm it's a real failure, not a contaminated control**: check the paired negative-control ampoule/strip. Control growth invalidates the test lot rather than confirming a sterilizer fault — retest with a fresh lot before declaring a recall.
2. **Define the exposure window**: every load on that specific sterilizer since its last confirmed-negative BI, not just the load carrying the positive result.
3. **Cross-reference tray tracking** to split the window into "still in storage — quarantine now" versus "already used — escalate to Infection Prevention for patient-level follow-up."
4. **Pull the sterilizer from service** pending an empty-chamber test cycle and a full-load repeat BI.
5. **Pull physical/chemical monitor logs for the whole window** — in-range logs throughout point toward a load-specific cause (overpacking, a cold spot); any out-of-range reading anywhere in the window points toward an equipment fault and changes the corrective-action conversation with biomedical engineering.
6. **Document and notify** per facility policy — Infection Prevention, OR leadership, Risk Management get the scope (load count, tray count, used vs. quarantined split) at detection, not after root cause is known.

## 5. Wet-pack investigation

Triggered when a sterilizer's wet-pack rate on a load type exceeds roughly 2% over a week (a single wet pack is a handling event; a recurring rate is a process signature).

1. **Check loading pattern first** — trays too close together or stacked block steam penetration and drying airflow; this is the single most common cause and the cheapest to fix.
2. **Check water quality/feed** — mineral content or condensate quality issues show up as a wet-pack pattern concentrated on one sterilizer, not fleet-wide.
3. **Check the drying-phase cycle time/vacuum setting** on that specific unit against its validated parameters — a drying phase silently shortened by a firmware update or a service reset will produce exactly this pattern.
4. **Only after equipment and process are cleared, review technique** (wrap tension, tray density, instrument arrangement) — retraining staff before ruling out the machine wastes the fix on the wrong target.
