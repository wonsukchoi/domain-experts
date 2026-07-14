# Playbook

## Production-feasibility check worksheet

Fill for any design-validation prototype before it's used to sign off on a design ahead of production tooling.

| Feature | Prototype fabrication method | Achievable by prototype? | Intended production process | Achievable by production process? | Issue found? |
|---|---|---|---|---|---|
| 0.040" wall section | CNC machining | Y | Injection molding | Check vs. resin flow-length guideline | Y — below 0.060" recommended minimum for this flow length |
| Undercut snap-fit | CNC machining | Y | Injection molding | Requires side-action or redesign | Y — $15,000 side-action cost, or redesign option |

**Rule:** for every design-critical feature, separately check achievability by the prototype's method AND by the actual intended production process — success in one doesn't confirm the other.

## Material substitution scope table

| Prototype material | Production material | Validates form? | Validates fit? | Validates function? |
|---|---|---|---|---|
| Aluminum (machined) | Injection-molded plastic | Y | Y (dimensional) | NO — mechanical properties differ substantially |
| 3D-printed resin | Die-cast metal | Y | Partial (check tolerance/finish differences) | NO — strength/thermal behavior differs substantially |
| Same material, different process (e.g., machined vs. molded of same resin) | Same resin, injection molded | Y | Y | Partial — check for process-induced property differences (molding orientation effects, etc.) |

**Rule:** explicitly document which column(s) a given prototype actually validates before it's used to support a design or tooling decision — never assume function validation from a form/fit-focused prototype in a substitute material.

## Revision tracking template

| Revision | Date | Features updated | Features NOT updated (still prior revision) |
|---|---|---|---|
| Rev A | initial build | All | — |
| Rev B | date | Mounting boss redesign | Body, undercut feature (unchanged from Rev A) |
| Rev C | date | Undercut feature redesign | Body (still Rev A), mounting boss (still Rev B) |

**Rule:** for any model updated more than once, maintain this kind of feature-by-revision map — never assume the whole physical model reflects a single uniform revision after ad hoc rework.
