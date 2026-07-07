# Forensic Science Technician — Playbook

## Scene collection sequencing (by fragility/contamination risk)

| Order | Evidence class | Example | Why this order |
|---|---|---|---|
| 1 | Volatile/fragile trace | Loose hair, fiber, gunshot residue | Lost to airflow, foot traffic, weather within minutes |
| 2 | Biological (wet) | Blood pooling, not yet dried | Degrades, dilutes, or gets tracked if walked through |
| 3 | Impression evidence | Shoe/tire impressions, tool marks | Casting must happen before ground disturbance or weather changes |
| 4 | Biological (dry) | Dried bloodstains, touch-DNA swabs | Stable but still contamination-prone from handling |
| 5 | Latent prints | Doorframes, glass, weapons | Needs dedicated processing (fuming/powder), can wait for photography to finish first |
| 6 | Bulk items | Clothing, weapons, furniture | Least time-sensitive; collect and package last |

Elimination/reference samples (victim, first responders, residents) are collected **alongside** step 2/4, not deferred — a mixture profile with no elimination sample on file can't be resolved into known-vs-unknown later.

## Presumptive-to-confirmatory test routing

| Presumptive test | Positive indicates | Known false-positive triggers | Confirmatory test required before report |
|---|---|---|---|
| Kastle-Meyer (blood) | Peroxidase activity | Plant peroxidases (horseradish, potatoes), some metals, certain cleaners | ABAcard HemaTrace (human hemoglobin) or Takayama crystal test |
| Marquis reagent (opiates/amphetamines) | Color change class reaction | Many over-the-counter/legal compounds | GC-MS confirmatory analysis at lab |
| Acid phosphatase (semen) | Enzyme presence | Vaginal secretions, some plant material | Microscopic sperm identification or P30/PSA confirmatory |

**Rule:** a presumptive positive is a collection/prioritization signal, never a report-ready finding. If a report or testimony states a presumptive result without noting the confirmatory step, treat it as incomplete regardless of how confident the field note sounds.

## Bloodstain angle-of-impact calculation

Formula: **sin θ = stain width ÷ stain length** (stain assumed circular at 90° impact, elliptical at oblique angles).

| Stain | Width (mm) | Length (mm) | sin θ = W/L | Angle of impact (θ) |
|---|---|---|---|---|
| A | 3.0 | 6.0 | 0.50 | 30.0° |
| B | 4.2 | 6.0 | 0.70 | 44.4° |
| C | 5.8 | 6.1 | 0.95 | 71.8° |

**Area of convergence:** back-project the long axis of each stain from its point of origin at the calculated angle; where **3 or more independent stain trajectories intersect** within a small tolerance region is a defensible area of convergence. A single stain's angle, reported alone as "the area of origin," is not — it only constrains a line, not a point, and any conclusion built on one stain should be labeled provisional pending additional stains.

## Backlog triage (when queue exceeds capacity)

| Priority tier | Trigger | Example |
|---|---|---|
| 1 — Expedite | Biological degradation clock or statutory deadline | Sexual assault kits, in-custody suspect with an approaching hearing |
| 2 — Standard priority | Violent felony, active investigation | Homicide, aggravated assault trace/print evidence |
| 3 — Routine queue | Property crime, cold case with no imminent deadline | Burglary tool marks, older unsolved case re-submission |

Triage overrides FIFO — a tier-3 item submitted first does not jump ahead of a tier-1 item submitted later.
