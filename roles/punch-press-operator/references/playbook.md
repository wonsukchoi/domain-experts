# Playbook

## Feed-pitch diagnostic worksheet

Fill when a progressive die shows a downstream alignment issue.

| Field | Value |
|---|---|
| Die | 4-Station Progressive, PP-3384 |
| Spec feed pitch | 1.500" ± 0.002" |
| Measured actual pitch | 1.494" |
| Deviation | -0.006" (exceeds tolerance by 0.004") |
| Defect location observed | Station 4 (profile-to-pilot-hole misalignment) |
| Station where defect actually originates | Feed system (upstream of Station 1), NOT Station 4 tooling |
| Station 4 tooling condition (verify separately) | Confirm sharp/correct before ruling out — in this case, confirmed OK |
| Root cause | Feed roller wear, reduced effective diameter |
| Corrective action | Replace feed rollers, re-verify pitch |
| Post-repair pitch | 1.500" ± 0.001" — within spec |
| Post-repair alignment offset | <0.001" (vs. 0.006" on affected parts) |
| Affected parts identified | Via production sequence log for suspected drift period |
| Disposition of affected parts | Inspection/rework/scrap per quality review |

## Die clearance reference table (illustrative — always use the die's specific clearance chart)

| Material | Thickness | Typical clearance (% of thickness, per side) |
|---|---|---|
| Mild steel | 0.030"-0.060" | 5-8% |
| Mild steel | 0.060"-0.125" | 6-10% |
| Stainless steel | 0.030"-0.125" | 8-12% (higher due to work-hardening) |
| Aluminum | 0.030"-0.125" | 4-6% |

**Rule:** always confirm against the specific die's clearance chart and current material spec — this table is illustrative, not a substitute for the actual specification.

## Point-of-operation safe-access procedure checklist

1. Identify the specific task requiring access (jam clear, die check, adjustment, changeover step).
2. Determine the correct safeguard level required for this specific task (single-stroke with guard intact vs. full lockout) — not the minimum that seems sufficient.
3. Apply the required safeguard level fully before any hand access near the point of operation.
4. Never substitute a lesser safeguard (e.g., single-stroke without lockout) for a task that requires full lockout.
5. Never bypass, block, or defeat a light curtain, guard, or two-hand control for any reason, including "just this once."
6. After completing the task, verify all safeguards are restored to active status before resuming normal cycling.
7. If a safeguard bypass is observed (by self or others), report immediately per the facility's safety reporting procedure, regardless of whether an incident occurred.
