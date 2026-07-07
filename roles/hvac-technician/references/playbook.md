# Playbook

Filled walkthroughs for the three places this trade gets shortcut: charging method selection, Manual J/S/D sizing, and airflow diagnosis. Numbers are worked examples to adapt, not universal constants — always check the equipment's own charging chart, rated static, and nameplate.

## 1. Charging method decision and execution

**Step 0 — identify the metering device before picking up gauges.**

| Metering device | Charging method | Why the other method fails here |
|---|---|---|
| Fixed orifice / piston | Superheat, against manufacturer chart keyed to outdoor dry bulb + indoor wet bulb | No subcooling target exists — the piston doesn't regulate flow to hold a subcooling value |
| TXV / EEV | Subcooling, against nameplate or manufacturer target (commonly 8–12°F, verify per unit) | Valve modulates to hold superheat near its setpoint across a wide charge range — superheat stays near-target even 1–2 lb off, masking over/undercharge |

**Fixed-orifice charging chart lookup (example, R-410A 3-ton condenser):**

| Outdoor DB | Indoor WB 60°F | Indoor WB 63°F | Indoor WB 67°F |
|---|---|---|---|
| 85°F | 12 | 15 | 19 |
| 95°F | 9 | 12 | 16 |
| 105°F | 6 | 9 | 13 |

Read outdoor dry bulb down the left column, indoor wet bulb across the top, target superheat at the intersection. This table is illustrative — always pull the specific model's chart; charts vary by coil and orifice size.

**Execution sequence:**
1. Confirm indoor wet bulb with a psychrometer at the return grille — do not estimate from a thermostat's %RH display, it's frequently uncalibrated by several points.
2. Take outdoor dry bulb at the condenser, in shade, not off a phone weather app.
3. Look up target superheat (fixed orifice) or pull nameplate subcooling target (TXV).
4. Measure actual superheat/subcooling. If outside target by more than ±3°F, adjust in small increments (2 oz for residential split systems) and recheck after each — never dump a full pound and re-gauge once.
5. Log start/end recovery-cylinder or charging-cylinder weights alongside the readings — this is both the diagnostic record and the Section 608 recordkeeping requirement.

## 2. Manual J → Manual S → Manual D: load-to-equipment walkthrough

**Example house:** 2,400 sq ft single-story, 95°F outdoor design temp (1% design condition for the location), 75°F indoor setpoint, R-19 walls, double-pane low-E windows, R-38 ceiling, ducts in unconditioned attic.

**Manual J room-by-room rollup (sensible components, Btu/h at design):**

| Component | Load (Btu/h) |
|---|---|
| Walls (conduction) | 6,800 |
| Windows (conduction + solar) | 9,200 |
| Roof/ceiling | 5,400 |
| Infiltration (sensible) | 3,100 |
| Duct loss (attic-run, sensible) | 2,500 |
| Internal gains (occupants, lighting, appliances) | 3,000 |
| **Sensible subtotal** | **30,000** |

**Latent components:**

| Component | Load (Btu/h) |
|---|---|
| Infiltration (latent) | 2,200 |
| Occupant latent | 800 |
| **Latent subtotal** | **3,000** |

**Total design cooling load = 30,000 + 3,000 = 33,000 Btu/h = 33,000 ÷ 12,000 = 2.75 tons.**

**Manual S selection window:** target 100–115% of 33,000 Btu/h = **33,000–37,950 Btu/h** (up to ~140% only with a documented reason such as no smaller product-line step being available).

| Candidate equipment | Nominal capacity | % of 33,000 Btu/h load | Manual S verdict |
|---|---|---|---|
| 2.5-ton (30,000 Btu/h) | 30,000 | 91% | Under window — undersized, would run continuously on design day |
| 3-ton (36,000 Btu/h) | 36,000 | 109% | **In window — correct selection** |
| 4-ton (48,000 Btu/h) | 48,000 | 145% | Outside window — the "go up a size" install; short-cycles, poor dehumidification |

The 4-ton unit a builder or the prior contractor installed "to be safe" is 145% of the actual load — 30 points past even the generous ceiling — and is the equipment-sizing failure this role exists to catch before or after install.

**Manual D airflow requirement, once equipment is selected:** 3-ton unit at ~400 CFM/ton (residential standard-efficiency rule of thumb, verify against the air handler's blower table) = **1,200 CFM design airflow.** Duct sizing (trunk and branch) is sized off this CFM and an assumed friction rate (commonly 0.10 in. w.c. per 100 ft for residential), not off tonnage directly — undersized ducts sized for a smaller assumed CFM are a common source of the static-pressure red flags below.

## 3. Static pressure / airflow diagnostic sequence

Run whenever superheat/subcooling reads off target *before* touching refrigerant charge, and whenever the complaint is capacity- or comfort-related.

1. **Total external static pressure (TESP):** measure across the whole air handler (supply plenum minus return plenum, referenced to outdoor if needed). Compare to the unit's rated static (commonly 0.5 in. w.c. for many residential ducted air handlers — check the actual blower performance table). >0.8 in. w.c. against a 0.5 in. w.c. rating means the blower is fighting real restriction.
2. **Isolate the restriction:** measure static drop across the filter, then the coil, then supply and return trunks separately. A filter reading >0.3 in. w.c. drop on its own (vs. ~0.1 in. w.c. clean) is usually the whole problem.
3. **Cross-check with temperature split:** 16–22°F return-to-supply split on a properly dehumidifying system. A split under 14°F with high static usually means restricted airflow; a split over 22°F with normal static points at low charge or a metering-device problem, not airflow.
4. **Confirm delivered CFM** against the Manual D design CFM (see above) using the blower's rated table at the measured TESP, or a flow hood at supply registers, before concluding the system is "just old" or blaming the compressor.

## 4. EPA refrigerant-handling compliance reference (40 CFR Part 82 Subpart F)

| Full charge of equipment | Applies | Leak-rate trigger | Repair timeline |
|---|---|---|---|
| < 50 lb | Comfort cooling, most residential/light-commercial splits | No rate-based mandate | No federal timeline; shop policy should still dispatch a leak search on any non-service-related charge loss |
| ≥ 50 lb | Comfort cooling appliances (chillers, larger package units) | 10% annualized leak rate | Repair within 30 days of finding; verification test within 30 days of completing repair |
| ≥ 50 lb | Commercial refrigeration | 20% annualized leak rate | Same 30/30-day structure |
| ≥ 50 lb | Industrial process refrigeration | 30% annualized leak rate | Same 30/30-day structure, quarterly leak inspection follow-up if still above trigger |

Below the 50 lb threshold there's no federal repair-timeline clock, but every recovery/recharge is still a recordkeeping event: cylinder weight before and after, technician certification number, and date — the same log that lets the next visit tell a one-time correction from a chronic leak.
