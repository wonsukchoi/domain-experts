# Red flags

Smell tests an electrical/electronics drafter catches in the first pass over a redline, a drafted schematic, or a set headed for issuance.

### Conductor ampacity pulled from the 90°C (THHN) column when the equipment terminates at 75°C or 60°C

- **Usually means:** the drafter sized from the conductor's insulation rating instead of checking the equipment's listed termination temperature per 110.14(C).
- **First question:** what temperature rating does the starter/breaker/terminal block's UL listing actually specify, and does it match the column used?
- **Data to pull:** the equipment's nameplate or listing data, the Table 310.16 column used, the required minimum ampacity from the continuous-load calculation.

### Overload trip/heater setting exceeds 125% of motor FLC (or 115% for SF <1.15)

- **Usually means:** the overload was sized off the motor's nameplate FLA using the wrong multiplier, or the service-factor classification wasn't confirmed before calculating.
- **First question:** what service factor is stamped on the motor nameplate, and does the overload setting reflect the correct 430.32(A)(1) multiplier for that classification?
- **Data to pull:** the motor nameplate, the Table 430.250 FLC value used, the overload relay's actual heater/trip setting.

### Short-circuit/ground-fault OCPD sized above the Table 430.52 maximum percentage without a cited exception

- **Usually means:** the breaker or fuse was selected for nuisance-trip avoidance without checking whether the resulting size exceeds the code-maximum percentage of FLC.
- **First question:** does the selected OCPD size exceed 250% of FLC (inverse-time breaker) or the relevant fuse percentage, and if so, which 430.52 exception permits it?
- **Data to pull:** the calculated maximum from Table 430.52, the selected OCPD's actual rating, the cited exception if oversized.

### Equipment grounding conductor size copied from the phase-conductor ampacity table instead of Table 250.122

- **Usually means:** the drafter assumed EGC size tracks phase conductor size by rule rather than looking it up independently from the OCPD rating.
- **First question:** what OCPD rating protects this circuit, and does the EGC size match Table 250.122's entry for that rating — not the phase conductor's ampacity-derived size?
- **Data to pull:** the OCPD rating, Table 250.122, the phase conductor size (for comparison only, not derivation).

### Wire number reused for two electrically distinct nodes across sheets

- **Usually means:** a segment-based numbering habit was applied on a project using a net-based standard, or a number was reused after a design change without a full-set search.
- **First question:** does this wire number appear on more than one sheet, and if so, are both occurrences the same electrically continuous node?
- **Data to pull:** a cross-reference/wire-number report across the full sheet set, the project's numbering-convention standard.

### Control-relay logic drawn directly onto a one-line diagram

- **Usually means:** the drafter tried to make one drawing serve both the coordination-level and field-wiring purposes instead of producing both a one-line and an elementary diagram.
- **First question:** is this a system coordination sheet or a buildable field-wiring reference, and does its content match that purpose?
- **Data to pull:** the sheet index/drawing list, the project's drawing-type standard, a comparable one-line from an already-issued set.

### Raceway has 4 or more current-carrying conductors with no Table 310.15(C)(1) adjustment factor applied

- **Usually means:** the ampacity check compared load directly against the temperature-column value without derating for conductor bundling.
- **First question:** how many current-carrying conductors actually share this raceway (excluding EGC and balanced neutral), and was the corresponding adjustment factor applied before comparing to load?
- **Data to pull:** the raceway/conduit schedule, the CCC count, the adjusted ampacity value used in the sizing calc.

### PCB power trace width matches an adjacent signal trace with no IPC-2221 current calculation on record

- **Usually means:** trace width was set by visual/routing convenience rather than by copper weight and current-carrying requirement.
- **First question:** what current does this net actually carry at steady state, and what width does IPC-2221 require for the board's copper weight and allowed temperature rise at that current?
- **Data to pull:** the net's expected current, the stack-up's copper weight per layer, the IPC-2221 current-capacity curve or table used.

### Controlled-impedance net sized from a current-capacity table instead of the stack-up's impedance calculation

- **Usually means:** the trace was routed and sized using the same current-based method as a power trace, without recognizing the net requires an impedance target.
- **First question:** does this net's schematic or fab note call out a target impedance, and was the trace width derived from the stack-up's impedance model rather than a current table?
- **Data to pull:** the stack-up specification, the impedance-controlled net list, the trace width and reference-plane spacing used.

### Schematic symbol on the sheet doesn't appear in the drawing set's legend

- **Usually means:** a non-standard or vendor-specific symbol was drafted without adding it to the IEEE 315/ANSI Y32.2-based legend, or the legend wasn't updated after a late addition.
- **First question:** does every symbol used on this sheet have a corresponding legend entry, and does the legend entry match the standard (or note the deviation)?
- **Data to pull:** the drawing set's symbol legend sheet, the specific symbol in question, the IEEE 315/ANSI Y32.2 reference for comparison.

### Wiring/panel diagram terminal designation disagrees with the schematic's for the same device

- **Usually means:** one drawing was updated after a design change and the other wasn't, or the two were drafted from different revisions of the redline.
- **First question:** which drawing reflects the current, approved redline, and has the other one simply not been updated yet?
- **Data to pull:** both drawings' revision blocks and dates, the redline or engineering change note driving the discrepancy.
