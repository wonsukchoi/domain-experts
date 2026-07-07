# Playbook

Filled procedures a service technician actually runs, with real structures, thresholds, and worked numbers. Starting points to adapt against the OEM manual and site safety program, not scripts that override either.

## 1. Pre-climb go/no-go checklist

Run in full before the first person clips onto the ladder, every shift — not once per work order.

**Rescue plan validation (all must be yes, or the climb is a no-go):**

| Check | Standard |
|---|---|
| Rescue plan on file specific to this tower's anchor/obstruction layout | Generic fleet-wide plan does not satisfy this |
| Crew present today matches (or exceeds) the plan's assumed rescue-capable headcount | A two-person plan with one person present today is a no-go |
| Self-rescue/assisted-rescue descender device inspected this shift, tag current | Expired inspection tag = equipment treated as unavailable |
| Estimated time to reach a suspended worker at the highest work point ≤ ~15 minutes | Based on orthostatic-intolerance onset window (OSHA suspension-trauma guidance, ~5–15 min) |
| Communication method to raise external emergency services confirmed working (radio/cell signal checked at tower base) | Dead zone at a remote pad site is a plan defect, not an acceptable risk |

**Weather gating:**

| Condition | Action |
|---|---|
| Sustained wind at hub height forecast ≥ OEM/site access limit (commonly 12–14 m/s for exterior tower work) | No exterior climb; interior nacelle work only if the plan and manual allow it |
| Lightning within site exclusion radius (commonly 5–10 mi, per site plan) or forecast within the work window | No climb; if already at height, execute descent per the lightning-egress procedure, not the standard descent |
| Wind gusting near the limit with high variability (not just the sustained average) | Default to no-go — gust variance is the harder hazard to plan a rescue around, not the average |

**PPE/anchor verification:** full-body harness inspected and tagged this shift; lanyard/lifeline rated and inspected; anchorage either OEM-certified for the fall-arrest system in use, or verified by a qualified person to sustain twice the maximum arrest force with a safety factor of at least 2 (OSHA 1910.140(c)(13)); rope-access or ladder-climb-assist device (if used) inspected per manufacturer interval.

## 2. Tower-flange and blade-root bolt torque/tension procedure

**Torque-tension relationship (worked calculation):**

Torque-tension formula: **T = K × D × F**, where T = applied torque, K = friction (nut-factor) coefficient, D = nominal bolt diameter, F = target preload (tension).

*Example: M36 grade 10.9 tower-flange bolt, target preload 850 kN (a stated target for this joint class, not a universal constant — confirm against the OEM spec sheet for the specific turbine).*

- Dry/as-received condition, K ≈ 0.15: T = 0.15 × 0.036 m × 850,000 N ≈ **4,590 N·m**
- Lubricated condition (OEM-specified anti-seize), K ≈ 0.12: T = 0.12 × 0.036 m × 850,000 N ≈ **3,672 N·m**

The ~20% gap between those two numbers for the *same target preload* is the reason a torque wrench reading is only trustworthy once the lubrication state is confirmed to match the K-factor the spec was calculated against (VDI 2230 method). Applying the dry-condition torque (4,590 N·m) to a lubricated joint over-tensions it by roughly the same 20%; applying the lubricated torque to a dry joint under-tensions it by the same margin — either error is a fastener that can back off or overload in service.

**Blade-root and large tower-flange bolts:** where torque-to-tension uncertainty is unacceptable at this fastener size, use tension control instead — hydraulic tensioning rigs or ultrasonic bolt-elongation measurement — which reads the actual stretch of the bolt rather than inferring tension from applied torque and an assumed friction coefficient.

**Re-torque/re-check schedule (industry-common heuristic where the OEM manual doesn't specify one — OEM interval always overrides):**

| Joint | First check | Subsequent interval |
|---|---|---|
| Tower-flange bolts | ~500 operating hours post-commissioning (bolts seat/relax fastest early in service) | Annual visual + sample torque check |
| Blade-root bolts | ~3 months post-commissioning, via ultrasonic elongation check (sample, not 100%) | Every 2 years, or per OEM manual — many OEMs specify tighter intervals for older bolt designs |
| Nacelle/main-frame structural bolts | Per OEM commissioning checklist | Per scheduled major service (commonly annual) |

## 3. Gearbox oil analysis interpretation

**Wear-metal bands (ppm) — stated as industry-common practice from oil-lab and OEM guidance, not a single universal spec; use the OEM/lab-published thresholds for the specific gearbox model when available:**

| Element | Normal | Caution | Critical |
|---|---|---|---|
| Iron (Fe) | < 75 ppm | 75–150 ppm | > 300 ppm |
| Copper (Cu) | < 30 ppm | 30–75 ppm | > 150 ppm |
| Chromium (Cr) | < 10 ppm | 10–25 ppm | > 50 ppm |

**ISO 4406 particle-count cleanliness code:** target for a healthy wind-turbine gearbox is commonly cited around **18/16/13**; an alarm-level reading around **21/19/16** (roughly a 4x jump in particle count per two-step code increase) signals filtration failure or active wear debris generation, independent of the wear-metal ppm reading.

**The trend rule (overrides the absolute band):** compare each new sample to at least the prior two. Flag for escalation if any element more than doubles between two consecutive samples, even if the new value stays inside "normal" or "caution" — a rapid rate of change is the earlier and more reliable indicator of a developing spall than waiting for an absolute-band crossing. A flat or slowly-rising trend inside "caution" can typically wait for the next scheduled sample; an accelerating trend cannot.

## 4. SCADA/vibration escalation ladder

1. **Single-sensor, single-reading alarm, no gear-mesh/shaft-order harmonic match** → log as probable sensor/mounting artifact; confirm at next scheduled SCADA pull, no dispatch.
2. **Alarm persists across 2+ consecutive load-normalized readings, still no harmonic match** → schedule a handheld vibration check at next site visit within the current maintenance window (not an emergency dispatch).
3. **Alarm amplitude sits at a gear-mesh or shaft-order harmonic, and/or corroborated by an oil-analysis trend on the same component** → schedule a borescope inspection within the week, independent of whether the absolute alarm threshold has been crossed.
4. **Alarm crosses the absolute critical threshold, or borescope confirms visible spall/pitting** → escalate to OEM engineering for a root-cause and repair-scope decision (bearing-only vs. full component exchange); begin crane-mobilization lead-time planning in parallel so the decision doesn't stall on logistics once the technical call is made.

## 5. Confined-space and nacelle-entry checklist

| Step | Requirement |
|---|---|
| Atmosphere test | Test before entry even if the site doesn't formally classify the nacelle/hub as permit-required — treat untested + restricted egress as permit-required by default |
| Electrical isolation | Lockout/tagout applied on converter and generator circuits per 1910.269 before any drivetrain or electrical work |
| Attendant/communication | Confirm a means to raise the entrant if working solo in the hub (rare, and only where the site plan explicitly allows solo hub entry) |
| Egress path | Confirm the hatch/ladder egress path is clear and the descent method is unaffected by the day's task (e.g., parts staged don't block the ladder) |
| Lightning-strike aftermath entry | Verify down-conductor resistance and receptor condition before assuming normal electrical isolation procedures are sufficient — a recent strike can leave residual charge paths the standard LOTO doesn't anticipate |
