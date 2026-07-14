# Playbook

## Defect-diagnosis worksheet

Fill when a defect is found during inspection.

| Field | Value |
|---|---|
| Machine / Roll # | Loom #14, Roll #2291 |
| Defect description | Streak, lighter/looser weave |
| Position (cross-width) | 340mm from left selvedge |
| Extends along | Full 500-yard roll length |
| Pattern classification | Continuous at fixed position → single-end issue (not repeating-interval, not random) |
| Suspected system | Individual warp end tension |
| Measured value at defect position | 140g |
| Spec value | 250g |
| Deviation | 44% below spec |
| Surrounding positions measured | 245-255g (normal) |
| Root cause | Let-off tensioner slip, this end only |
| Corrective action | Re-tension/replace individual tensioner |
| Post-fix measurement | 248g (within ±10g spec) |
| Test length inspected before resuming full run? | Y (10 yd) |

## Repeating-vs-random defect classification table

| Defect pattern | Points to | First diagnostic step |
|---|---|---|
| Continuous line at one fixed cross-width position, full length | Single warp end/needle tension outlier | Measure tension at that specific position vs. surrounding positions |
| Repeats at a regular interval along the length | Specific mechanical element (needle, heddle, cam) tied to the machine's cycle | Match the interval to the machine's known mechanical cycle length |
| Random, no consistent position or interval | Yarn quality or intermittent tension source | Check yarn lot/spool records for the affected segment |
| Affects entire width uniformly | Beam-wide or whole-machine tension/setting issue | Check overall tension setting and machine calibration |

## Yarn break tracking log format

| Timestamp | Position (needle/end #) | Suspected cause | Repair action | Notes |
|---|---|---|---|---|
| record each break | record specific position | tension / yarn quality / mechanical | rejoin/repair method | flag if position repeats within shift |

**Review at end of shift:** count breaks by position — 3+ breaks at the same position in one shift is a strong signal of a developing mechanical issue at that position, warranting inspection before the next shift rather than continued isolated repairs.

## New setup verification checklist

1. Confirm pattern/gauge/draft setting against the job ticket's specification, not a visual "looks right" check.
2. Run a short test length (commonly 10 yards or the facility's standard test length).
3. Inspect the test length specifically for the new setting's expected effect (correct gauge, correct pattern repeat, no setup-specific defect).
4. Measure (don't just visually inspect) gauge/count/density against spec on the test length.
5. Only after the test length passes both visual and measured checks, commit to the full production run.
