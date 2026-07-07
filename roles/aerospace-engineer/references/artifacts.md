# Artifacts

Filled examples an agent can populate or execute directly — not descriptions of what these documents contain.

## Weight & balance budget tracker

| Subsystem | Budget (lb) | Predicted (lb) | Actual/weighed (lb) | Delta vs budget | Contingency remaining |
|---|---|---|---|---|---|
| Structures | 24,500 | 24,700 | 24,850 | +350 | 0 lb (exhausted) |
| Propulsion | 9,200 | 9,100 | 9,100 | −100 | 100 lb (banked) |
| Systems | 6,600 | 6,750 | 6,830 | +230 | 0 lb (exhausted, escalate) |
| Furnishings & interior | 4,700 | 4,760 | 4,800 | +100 | 0 lb (exhausted) |
| **Program pool contingency** | 500 | — | — | −580 net draw | −80 lb (overdrawn) |

Rule of thumb: a subsystem with 0 lb contingency remaining and a design phase earlier than Critical Design Review (CDR) is a program-level flag, not a subsystem-level one — the pool is what absorbs it, and the pool is now overdrawn before flight test, where growth historically continues.

## Margin-of-safety calculation sheet

```
Component: Wing spar cap, root station (WS 0.0)
Load case: V-n diagram positive maneuver corner point, n = 2.5g @ MTOW (82,000 lb)
Applied ultimate bending stress (from FEM):      54,200 psi
Base material allowable (7075-T6 extrusion, B-basis):  78,000 psi
Knockdown — fastener hole (open-hole compression): x 0.90
Knockdown — fatigue/environment (hot/wet):         x 0.93
Effective allowable = 78,000 x 0.90 x 0.93 =       65,286 psi

MS = (Effective allowable / Applied ultimate stress) - 1
MS = (65,286 / 54,200) - 1 = +0.20

Disposition: MS within target band (0.10-0.30) for primary structure. No redesign.
Disposition if MS < 0: structural redesign required before proceeding to static test article build.
```

Fallback order when MS comes back negative or under target band, in preference order:
1. Re-verify the governing load case and knockdown stack — confirm no double-counted knockdown or wrong corner point selected before touching the design.
2. Local reinforcement (doubler, thicker cap) if the shortfall is isolated to one station.
3. Material substitution to a higher-allowable alloy if the shortfall is structural-wide and schedule allows requalification.
4. Load relief (aerodynamic or operational limitation) only if 1–3 are infeasible on schedule — this is a program-level decision, not an engineering one, since it constrains the customer's operating envelope.

## Means of compliance matrix (excerpt)

| Requirement (14 CFR §) | Description | Verification method | Status |
|---|---|---|---|
| 25.305(b) | Structure must withstand ultimate load without failure | Test (static test article) | Test article built, test scheduled Q3 |
| 25.629 | Aeroelastic stability (flutter) | Analysis + flight test | Analysis complete, MS=+0.15; flight test pending |
| 25.1309(b) | Failure condition probability vs severity | Analysis (fault tree / FMEA) | Complete, no catastrophic condition >1e-9/hr |
| 25.981 | Fuel tank flammability (special condition, novel propulsion) | Analysis + test (per special condition SC-XX) | Means of compliance not yet negotiated with FAA — **open risk** |

The last row is the pattern to flag: a special condition applied to a novel system with no negotiated means of compliance yet is a certification-schedule risk before it's an engineering risk — surface it to the program office, don't wait for the analysis to be "ready" to raise it.

## Design review memo template (filled)

```
TO: Program Chief Engineer
FROM: Structures Lead, Wing Section
RE: DDR Weight & Margin Status — Wing Box

Status: Empty-weight budget +580 lb against total (+680 lb excluding locked propulsion delta).
Fuel-burn impact: ~0.68% block fuel vs +/-1.0% guarantee band.
Structural: Wing-root spar cap MS=+0.20 at governing V-n corner point (n=2.5g); no action.
Recommendation: Furnishings redesign targeting 60 lb recovery (ROM $180/lb) before flight test,
rather than accepting further margin erosion into a phase where historical growth continues.
Certification: No open means-of-compliance items on this station; SC-XX fuel tank flammability
finding remains open at program level, tracked separately.
```
