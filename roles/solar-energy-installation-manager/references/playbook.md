# Installation Playbook

Load this when running the site-survey-to-permit sequence, estimating a change order, reconciling a derate/attachment stack, or setting a PTO timeline. Templates below are meant to be filled and run, not read as description.

## 1. Site-survey-to-mobilization checklist

Run in this order. Do not mobilize the crew until every row is closed or explicitly deferred with a signed change order.

| # | Check | Pass threshold | If fail |
|---|---|---|---|
| 1 | Roof plane obstructions (vents, HVAC curbs, skylights) mapped against sold layout | 0 unresolved obstructions inside array boundary | Redraw at row level, price change order |
| 2 | Rafter spacing measured on 3 points per plane | Matches design spec ±1" | Re-run structural calc for actual spacing |
| 3 | Service panel busbar rating vs. interconnection method | 120% rule: `busbar rating × 1.20 ≥ main breaker + backfeed breaker` | Flag for panel upgrade or supply-side tap, price separately |
| 4 | Roof condition / remaining life | ≥ 10 years remaining, or written customer waiver | Recommend re-roof before install, hold job |
| 5 | Attic/rafter access for verification | Confirmed visually, not from plan set alone | Schedule attic inspection before ordering racking |
| 6 | Shading obstructions (trees, adjacent structures) | Solar access ≥ 85% per string, per Solmetric/Aurora report | Re-layout string or flag for module-level power electronics |
| 7 | Setback compliance (ridge, eave, edge) | Per adopted fire code (typically 18–36" per plane depending on jurisdiction) | Drop row/column, do not shrink individual module footprint |

**Deferred item log format** (one line per item, kept with the job folder):
`[date] — [item] — [dollar impact] — [change-order # or "pending signature"] — [crew-proceed: yes/no]`

## 2. Change-order estimating worksheet

Fill top to bottom; each row's output feeds the next.

```
Sold system:              ____ modules × ____ W = ____ kW DC
Contract rate:             $____/W installed
Sold contract value:        $____

Site-survey finding:        [describe obstruction / access issue]
Modules affected:           ____ (row-level, not module-level — see SKILL.md heuristic)
Revised system:             ____ modules × ____ W = ____ kW DC
Nameplate change:           ____ % (revised − sold) / sold

Labor delta:
  Additional crew-hours:    ____ hrs × $____/hr blended rate = $____
  Additional material:      [item] × [qty] × $____/unit = $____
  Equipment upgrade (if any, e.g. panel upgrade): $____

Change-order total:         $____ (contract value delta + labor delta + material delta)
Signature required before:  [crew mobilization date]
```

**Worked instance** (companion to SKILL.md's vent-stack example, different job):
```
Sold system:               32 modules × 415W = 13.28 kW DC
Contract rate:              $2.75/W installed
Sold contract value:        $36,520

Site-survey finding:        Skylight sits inside 2nd row from eave; code setback forces dropping full row
Modules affected:            5 (full row)
Revised system:              27 modules × 415W = 11.205 kW DC
Nameplate change:            −15.6%

Labor delta:
  Additional crew-hours:     6 hrs × $85/hr = $510 (re-layout, re-flash 5 fewer penetrations, net time saved partly offset by redesign)
  Additional material:       none (fewer standoffs needed, credited back)
  Standoff credit:            −4 × $38 = −$152

Change-order total:          −$5,706.25 (2,075W dropped × $2.75/W) + $510 (labor) − $152 (standoff credit) = −$5,348.25
Signature required before:   crew mobilization, 3 business days out
```

## 3. Structural attachment reconciliation procedure

1. Pull the PE's stamped uplift number for the affected row (lbs, total across all points, not per-point — per-point is a derived number, not the source number).
2. Count actual usable attachment points after survey. If a point is lost, redistribute *that point's* load onto its nearest remaining neighbors on the same support run (typically the two immediate adjacent points) — never assume the lost point's share is simply gone. Only spread it across every remaining point in the row if the PE's stamped calc explicitly models the row as one continuous load path; otherwise an even-across-the-row split understates the load actually landing on the two closest points and can miss where the real failure is.
3. Pull the fastener's rated withdrawal capacity per inch of thread penetration from the manufacturer table (example: #14 lag, ~194 lbs/inch).
4. Multiply by actual embedment depth confirmed on site (not the spec sheet minimum) to get nominal capacity per fastener.
5. Apply the test-protocol margin (ICC-ES AC428: nominal capacity ÷ 1.5 = allowable design load per fastener).
6. Compare: `redistributed per-point load ≤ allowable design load per fastener`.
   - **Pass, ≥15% margin remaining:** proceed as redistributed.
   - **Pass, <15% margin:** flag for PE review before crew proceeds on that row.
   - **Fail:** apply a fallback in this order — (a) double-lag the points adjacent to the lost one, (b) add a supplemental point elsewhere on the same rafter if spacing allows, (c) reduce the row's module count further to cut the load, (d) full re-layout with PE re-stamp. Do not proceed on (a) or (b) without PE as-built sign-off.
7. Torque-check every point at install: under the manufacturer's floor voids the warranty and the AC428 test basis; over the ceiling (typically stated in the install manual, e.g. 20 ft-lb max on a given lag) ruptures the flashing seal — both directions are a fail, log the actual torque applied per point.

## 4. Electrical derate stack template

Run all four lines in order; stopping after the first is the most common miss.

```
Module Isc:                       ____ A
1. NEC 690.8(A) continuous current: Isc × 1.25 =                ____ A
2. NEC 690.8(B) safety factor:      (line 1) × 1.25 =            ____ A   [combined 156% of Isc]
3. Ambient temperature correction:  (line 2) × [table factor for record-high ambient] = ____ A
4. Conduit fill / bundling derate:  (line 3) × [NEC Table 310.15(B)(3)(a) factor] = ____ A
Final ampacity requirement:         ____ A → select conductor/OCPD ≥ this number
```

**Worked instance:** Module Isc = 14.0A. 690.8(A): 14.0 × 1.25 = 17.5A. 690.8(B): 17.5 × 1.25 = 21.875A. Ambient correction at a 40°C record-high design temp on 90°C-rated THWN-2 (0.91 factor per NEC Table 310.15(B)(1)): 21.875 ÷ 0.91 = 24.04A. Four current-carrying conductors bundled (0.8 factor): 24.04 ÷ 0.8 = 30.05A required ampacity — a 10 AWG THWN-2 conductor (40A at 90°C per NEC Table 310.16) clears it; a 12 AWG (30A at 90°C) does not, missing by less than 1A, once both derates stack.

## 5. Rapid-shutdown compliance check

| Zone | Requirement | Verify by |
|---|---|---|
| Inside array boundary (1 ft) | ≤ 80V within 30 seconds of shutdown initiation | Manufacturer's UL 3741 or 690.12 listing sheet + as-built label matches actual equipment model |
| Outside array boundary | ≤ 30V within 30 seconds, OR listed PV Hazard Control System in place of module-level shutdown | Confirm AHJ has previously accepted this exact method — check local permit history first, don't assume |
| Label | Placarding matches 2023-cycle wording exactly, placed at PV disconnect and initiation point | Physical inspection before permit submittal, not from the drawing set |

## 6. Permit package audit (run before every submittal)

- [ ] Structural calculations present and stamped — not just referenced
- [ ] Equipment model numbers identical across site plan, structural calc, and single-line diagram (pull all three side by side, character-match model numbers)
- [ ] Title block complete: address, parcel/APN, contractor license #, revision date, sheet count
- [ ] Rapid-shutdown labeling matches installed equipment, not a prior-revision template
- [ ] Fastener schedule on structural calc matches the racking BOM being ordered

Any single miss above is a recurring rejection cause in permit-reviewer accounts [heuristic — no published rejection-rate breakdown by field] — audit the full set even if only one item seems in question.

## 7. Fall-protection decision gate

```
Exposure ≥ 6 ft?
  No  → standard housekeeping controls, log pitch/height on file
  Yes → Guardrail, net, or PFAS in place?
          Yes → proceed, log competent-person name
          No  → "Infrequent and temporary" exemption claimed?
                  Both true required:
                    (a) written 15-ft no-approach rule exists
                    (b) rule is actively enforced (name the enforcement method: spotter, cordon, verbal callout log)
                  Both true → exemption valid, log justification
                  Either false → non-compliant, stop work on that plane until protection is in place
```

## 8. PTO timeline tracker (per-utility, not company average)

| Utility | Solar-only PTO | Solar + storage PTO | Notes |
|---|---|---|---|
| Southern California Edison | 4–6 weeks | 8–12 weeks (occasionally 16) | Simplified track only below system-size threshold |
| National Grid (MA) | 15–20 business days post-inspection | Not on simplified track | Simplified SLA applies to standard residential only |
| [utility C — fill from local tracker] | ____ | ____ | ____ |

Update this table from actual closed jobs each quarter — do not quote a customer from a stale row.
