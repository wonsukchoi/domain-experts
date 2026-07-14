# Playbook

## Turn-count cross-check worksheet

Fill periodically during winding, especially for high-turn-count coils.

| Checkpoint | Counter reading | Independent layer-count calculation | Discrepancy | Action |
|---|---|---|---|---|
| 250 turns (mid-winding) | 250 | 248 | 2 turns (0.8%) | Flag counter for calibration; switch to verified independent method for remainder |
| 500 turns (final) | N/A (using verified method) | 500 | 0 | Confirmed |

**Rule:** cross-check at minimum once mid-winding and once at completion for any coil where turn count matters electrically — never rely solely on the mechanical/electronic counter's display without periodic independent verification.

## Electrical test reference table (illustrative — always use the specific coil's actual specification)

| Test | What it verifies | Typical acceptance criteria |
|---|---|---|
| DC Resistance | Wire continuity, approximate turn count/gauge consistency | Within specified tolerance of calculated target resistance |
| Inductance (LCR meter) | Turn count accuracy, core/winding characteristics | Within specified % of target inductance |
| Hi-pot / dielectric test | Insulation integrity, absence of shorts | Withstands specified voltage for specified duration without breakdown |
| Insulation resistance | Insulation quality (distinct from hi-pot breakdown test) | Above specified minimum resistance value |

**Rule:** perform all applicable tests per the coil's specification — passing one test (e.g., resistance) does not confirm the others (e.g., insulation integrity via hi-pot).

## Wire tension/insulation handling checklist

1. Confirm wire gauge and insulation type before setting tension.
2. Set tension to the specified range for this specific wire/insulation combination — not by feel.
3. Inspect wire guides and tensioning equipment for any sharp edges or wear that could nick insulation during winding.
4. Maintain consistent tension throughout the winding — monitor for any drift during a long winding run.
5. Follow the specified winding pattern/layering sequence exactly.
6. After winding, perform all specified electrical tests before accepting the coil — do not rely on visual/mechanical inspection alone.
7. Document tension settings, turn count verification method, and electrical test results together in the coil's quality record.
