# Playbook

Filled worksheets for the four procedures that gate almost every job: identifying the required approach distance, applying/removing temporary protective grounds in the correct order, selecting arc-flash PPE, and sequencing crews during storm restoration. Numbers below are the published table values and worked examples, not universal constants — a specific utility's approved procedure and a specific circuit's fault-current study always control over this worksheet.

## 1. Minimum approach distance (MAD) by voltage class

OSHA 29 CFR 1910.269 Appendix B minimum approach distances, phase-to-ground exposure, alternating current, at elevations ≤3,000 ft. Distances ≤72.5kV are the published Table 5 total distances (electrical component plus the ergonomic/inadvertent-movement allowance already included); distances >72.5kV are OSHA's published Table 6 values, converted here from decimal feet to feet-inches and rounded to the nearest inch:

| Voltage class (phase-to-phase) | Minimum approach distance |
|---|---|
| 0–300V | Avoid contact; treat as energized, insulate or de-energize |
| 301V–750V | 1 ft 0 in |
| 751V–15kV | 2 ft 2 in |
| 15.1kV–36kV | 2 ft 7 in |
| 36.1kV–46kV | 2 ft 10 in |
| 46.1kV–72.5kV | 3 ft 6 in |
| 72.6kV–121kV | 3 ft 9 in |
| 121.1kV–145kV | 4 ft 3 in |
| 145.1kV–169kV | 4 ft 9 in |
| 169.1kV–242kV | 6 ft 7 in |
| 242.1kV–362kV | 11 ft 2 in |
| 362.1kV–420kV | 13 ft 11 in |
| 420.1kV–550kV | 16 ft 8 in |
| 550.1kV–800kV | 22 ft 7 in |

Reading this table: it answers "how close may a qualified employee's body or conductive tool come to this conductor," not "is this task safe" — a task that satisfies MAD can still be unsafe for other reasons (footing, fall protection, weather). Voltage class must be confirmed against system records or a second identification source before reading a row off this table; a misidentified class is a documented root cause in fatal contact incidents, and the mental-model default in SKILL.md is to round up to the next class when uncertain.

**Worked example.** A crew is assigned to trim clearance and reset a crossarm on a line marked on system maps as 46kV sub-transmission, but the crossarm hardware and insulator count visually match a 69kV construction standard more commonly seen on this utility's system. Per the "uncertain voltage class → next class up" default: treat the conductor as 46.1kV–72.5kV class (MAD 3 ft 6 in), not the mapped 36.1kV–46kV class (MAD 2 ft 10 in) — an 8-inch difference that matters directly if the crew's planned bucket position was set to the smaller number. Confirm with the system operator before proceeding either way; the discrepancy itself is reportable.

## 2. Temporary protective grounding sequence

Grounding equipment sized and rated per ASTM F855 to the circuit's available fault current (a ground set rated below available fault current can fail — melt, arc, or open — before upstream protection clears the fault, defeating its purpose). The sequence exists to create a low-impedance, bonded equipotential zone around the work location so that if the circuit is inadvertently re-energized or an adjacent circuit induces voltage, the worker is inside a zone of near-equal potential rather than the path between two different potentials.

**Application order ("make" sequence) — ground-end first, working position bracketed last:**

1. Test for absence of voltage at the work location with a rated detector, immediately before grounding — a switching order and tags establish authority to work, not proof of zero energy.
2. Attach the ground-end clamp of the first ground set to a verified system ground (grounded structure, driven ground rod, or the system neutral where approved) — this end goes on first because it establishes the reference point the equipotential zone is built from.
3. Attach the line-end clamp(s) to the conductor, working from the ground connection outward — never the reverse order, since a line-end-first connection means the worker's tool is the last thing between an unverified conductor and true ground.
4. Apply additional ground sets so the work location is *bracketed* — at least one set on each side of (or, for a single work point, immediately adjacent to) the position where work will occur, not only at one end of the de-energized section. A single ground set at the far end of a mile-long de-energized section does not protect a worker at the near end from an induced or backfed fault.
5. Confirm continuity/tightness of every clamp visually and by feel before work begins; a loose clamp is a ground set that will not perform when needed.

**Removal order ("break" sequence) — exact reverse, working position ungrounded last:**

1. Confirm all work is complete and all tools/personnel are clear of the conductor.
2. Remove line-end clamps first, working from the position farthest from the primary system ground back toward it — the opposite order from application, so the equipotential zone collapses from the outside in rather than exposing the work position first.
3. Remove ground-end clamps last.
4. Restore the switching order to service only after all grounds are confirmed removed and accounted for by count — a grounding set left on a conductor is now the fault it was protecting against.

**Worked example.** A 3-span section of 12.47kV distribution is cleared for pole replacement at the center span. Fault current study for this circuit: 4,000A available. Ground sets on hand are rated 15,000A momentary — adequate margin, proceed. Apply: ground-end clamp to a driven rod at the near structure, line-end clamps to all three phases at that structure (set 1); repeat at the far structure (set 2); this brackets the center work span between two grounded points, satisfying the bracketing rule even though the actual work is only at the center pole. Remove in reverse: line-end clamps at whichever structure is farther from the point that will be re-energized first come off first, then that structure's ground-end clamp, then the same sequence at the second structure — confirming a 2-set, 6-clamp count matches the 2-set, 6-clamp application record before authorizing re-energization.

## 3. Arc-flash PPE category selection

Utility work on exposed energized parts is governed by OSHA 1910.269 Appendix E's incident-energy exposure assessment, which uses the same cal/cm² category language as NFPA 70E's PPE category table — cite 1910.269 App E for utility generation/transmission/distribution work, not a direct 70E citation, though the two use compatible category boundaries:

| PPE category | Minimum arc rating (cal/cm²) | Typical utility task example |
|---|---|---|
| 1 | 4 | Voltage testing, routine switching on enclosed gear at lower incident-energy positions |
| 2 | 8 | Opening/closing enclosed switches, routine meter work near exposed parts |
| 3 | 25 | Work on exposed low-voltage or enclosed medium-voltage gear with elevated incident energy |
| 4 | 40 | Work at positions with high available fault current and longer clearing times |
| Above 40 | — | Task is not to be performed energized; de-energize or redesign the work method |

Selection procedure: (1) obtain or estimate the incident energy at the specific work position from the circuit's fault-current and protective-device clearing-time study — never assume a category from voltage class alone, since incident energy depends on fault current and clearing time, not voltage; (2) select the PPE category whose minimum arc rating meets or exceeds the calculated incident energy, rounding up to the next category if the calculated value falls between listed minimums; (3) treat the resulting PPE category as the floor for burn-severity mitigation, not a substitute for maintaining minimum approach distance from Table 1 above — PPE and MAD address different failure modes and both apply simultaneously.

**Worked example.** Incident-energy study for a 12.47kV distribution switch position returns 6.2 cal/cm² at the worker's expected standing position, with a 0.35-second clearing time on the upstream recloser. 6.2 cal/cm² exceeds Category 1's 4 cal/cm² minimum and falls below Category 3's 25 cal/cm² minimum — select Category 2 (8 cal/cm² minimum), the next category up that meets or exceeds the calculated value. If the recloser's clearing time were instead 1.2 seconds (slower protection, more energy through before the fault clears), the same fault current could push calculated incident energy past 25 cal/cm², moving the required category to 3 or 4 — which is why PPE category is reselected whenever protective-device settings change, not fixed to the circuit once.

## 4. Storm-restoration crew triage

See SKILL.md's worked example for the full arithmetic (transmission → distribution trunk with life-safety exception → service drops, ranked by customers restored per crew-hour). The reusable triage rule, restated as a checklist for a new event:

1. Map all reported damage to system topology (transmission segment, substation, distribution feeder, individual service) before assigning any crew — ticket volume and call order are not topology.
2. Compute customers-affected ÷ estimated crew-hours-to-repair for each damage segment; this ratio, not raw customer count or ticket age, sets the default order.
3. Apply documented life-safety exceptions (hospitals, water/wastewater treatment, 911/emergency dispatch centers) to move a specific feeder or segment ahead of its ratio-based position — document the exception and the facility, since this is a deviation from the customers-per-crew-hour rule and needs to be auditable afterward.
4. Re-run the ranking as damage assessment updates (new segments found, repairs completed) — the ranking is a living queue, not a one-time plan.
5. When mutual-aid crews arrive under an EEI mutual assistance agreement, confirm they are briefed on host-utility grounding and PPE procedures before dispatch, even under time pressure — a visiting crew defaulting to home-utility procedure on an unfamiliar system is a documented incident pattern during large storm events.
