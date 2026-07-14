# Playbook

## Cumulative-reduction tracking worksheet

Fill for any multi-pass cold rolling job.

| Pass | Start thickness | End thickness | Reduction this pass | Cumulative reduction since last anneal | Anneal trigger (35-40%) approaching? |
|---|---|---|---|---|---|
| 1 | 0.100" | 0.085" | 15% | 15% | No |
| 2 | 0.085" | 0.071" | 16.5% | 29% | Yes — schedule anneal before Pass 3 |
| [Anneal] | — | — | — | Reset to 0% | — |
| 3 (post-anneal) | 0.071" | 0.058" | 18.3% | 18.3% | No |
| 4 | 0.058" | 0.050" | 13.8% | 32.1% | Monitor if further passes needed |

**Rule:** track cumulative reduction since the LAST anneal (not since original stock) — this is what determines actual material capacity at any given pass, and it resets each time an anneal is performed.

## Crown/gap verification table

| Job parameter change from prior validated setup | Action required |
|---|---|
| Same material, same width, same reduction | Crown/gap setting likely transfers — verify with a quick multi-point check |
| Different width | Re-verify crown compensation — deflection profile changes with width |
| Different reduction/rolling force | Re-verify crown compensation — deflection scales with load |
| Different material (hardness/composition) | Re-verify both crown and gap — different material behaves differently under the same nominal force |

**Rule:** always measure actual output thickness at multiple points across width during setup for any changed parameter — never assume a prior setting transfers without verification.

## Inter-stand speed coordination guide

1. Before adjusting any single stand's speed, identify which adjacent stands (upstream and downstream) will be affected.
2. Calculate the resulting tension/compression effect on material between the adjusted stand and each neighbor.
3. Adjust neighboring stand speeds as needed to maintain appropriate inter-stand tension — don't leave them at prior settings if the change creates a new mismatch.
4. Monitor for necking (excess tension) or buckling (insufficient tension) symptoms immediately after any stand speed change.
5. Document the full stand speed profile (not just the changed stand) whenever an adjustment is made.
