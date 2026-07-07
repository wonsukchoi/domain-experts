# Playbook

Filled planning templates a commercial diver and dive supervisor actually run before, during, and after a dive. Numbers below are illustrative worked examples following standard planning methods — every dive still gets planned against the current certified dive table or dive computer in effect, never against figures memorized from a document like this one.

## 1. Bailout / reserve-gas sizing

Method: compute theoretical minimum gas needed to complete an ascent plus any owed decompression stop on bailout gas alone, at working (not resting) consumption, then double it for contingency.

**Formula per segment:** gas (cf) = SAC rate (cfm) × ATA (average for the segment) × time (min), where ATA = 1 + depth(fsw)/33.

**Filled example — bailout initiated at 100 fsw during an owed 8-minute stop at 10 fsw** (SAC rate 1.0 cfm, working diver planning figure):

| Segment | Depth range | Avg. ATA | Time | Gas used |
|---|---|---|---|---|
| Ascent to stop | 100→10 fsw | 2.7 | 3.0 min | 8.1 cf |
| Decompression stop | 10 fsw | 1.3 | 8.0 min | 10.4 cf |
| Ascent to surface | 10→0 fsw | 1.15 | 1.0 min | 1.15 cf |
| **Theoretical minimum** | | | 12.0 min | **≈20 cf** |
| **Planned reserve (×2 contingency)** | | | | **≈40 cf** |

**Bottle selection:** a 40 cf bottle meets the number with zero margin — reject it. An 80 cf bottle (nominal; ~77.4 cf usable) leaves ~37 cf of margin above the 40 cf requirement — that's the one that ships on this dive.

**Reserve-gas threshold rule during the dive itself:** call the ascent when remaining primary gas hits the planned reserve line, not when the gauge hits zero. If the task isn't done at the threshold, the task waits; the threshold doesn't move.

## 2. Repetitive-dive / surface-interval calculation

Method: a first dive leaves residual nitrogen in the diver's tissues; a surface interval reduces it but doesn't erase it. The second dive's allowable no-decompression time is the depth's normal no-decompression limit (NDL) minus the residual nitrogen time (RNT) carried over from dive one, as read off the current table for the actual repetitive-group letter and surface interval achieved.

**Filled example:**

- Dive 1: 80 fsw, 30 min bottom time → ends in a repetitive-group letter per the current table [illustrative — read the actual letter off the table in use].
- Surface interval: 1 hr 30 min → group letter reduces, carrying forward a residual nitrogen time of ~17 minutes at the planned dive-2 depth [illustrative RNT value — pull the exact figure from the current table for the actual group/interval combination].
- Dive 2 planned depth: 60 fsw. Table NDL at 60 fsw (single dive, fresh): 60 min.
- **Adjusted allowable bottom time = NDL − RNT = 60 − 17 = 43 minutes.**

If the task at 60 fsw is scoped for 50 minutes, that's 7 minutes over the adjusted limit (50 − 43 = 7). Three options, in order of preference: (1) shorten task scope to fit inside 43 minutes and finish the remainder on a later dive with a fresh interval; (2) extend the surface interval before diving to reduce the RNT further; (3) accept the dive as a decompression dive and plan the required stop rather than treating it as no-decompression — never simply dive the full 50 minutes against the un-adjusted 60-minute limit.

## 3. Wet vs. dry (habitat) underwater weld decision

| Factor | Wet weld | Dry (habitat) weld |
|---|---|---|
| Typical AWS D3.6M class achievable | B or C | A (topside-equivalent) |
| Suitable load role | Non-critical, static, temporary/interim repair | Primary or cyclic-load structural members |
| Relative cost/mobilization | Low — diver + electrodes | High — habitat rig, longer bottom time, more topside support |
| Common defect risk | Porosity, hydrogen embrittlement, reduced ductility from rapid quench | Comparable to topside welding when procedure is qualified |

**Default rule:** if the joint carries primary or cyclic structural load, specify dry/habitat welding and budget the mobilization; wet welding is the fallback only for non-critical or genuinely temporary repairs, and that fallback gets stated explicitly in the repair scope — not discovered later from an engineer asking why a load-bearing joint was wet-welded.

## 4. Underwater NDT method selection

| Task | Method | Notes |
|---|---|---|
| General condition survey | General visual inspection (GVI) | Fastest, lowest resolution; screens for gross damage/marine growth |
| Suspected crack or weld defect | Close visual inspection (CVI) + wet magnetic-particle inspection (MPI) | MPI only works on ferromagnetic material with adequate surface cleaning |
| Wall-thickness/corrosion mapping | Ultrasonic thickness (UT) gauge, grid pattern | Compare against baseline/nominal thickness, not a single spot reading |

**Repair/retirement trigger:** a heuristic used on many structural corrosion surveys is to flag for engineering review when remaining wall thickness drops below roughly 50% of nominal [stated heuristic, not a fixed code number] — the actual retirement thickness is an engineering fitness-for-service calculation specific to the structure and its loading, not a flat percentage; the diver's job is to deliver an accurate, gridded thickness map, not to make the retirement call.

## 5. Topside team and umbilical

- **Dive supervisor / person-in-charge (PIC):** holds abort authority, is not the working diver on a task complex enough to need full topside attention, controls the dive log and gas panel.
- **Tender:** manages the umbilical (paying out/taking in slack, watching for snags), relays comms, is the first line of contact if the diver goes quiet.
- **Standby diver:** fully suited and ready to deploy for the duration the working diver is in the water — not "available to suit up," actually dressed.
- **Umbilical bundle:** gas supply hose, two-way comms line, pneumofathometer (pneumo) hose for independent depth reading, and a strength member/lifeline bundled together — a kink or snag on any one line is treated as a full-umbilical problem until cleared, since they run together.

## 6. Dive-abort checklist (any one triggers a call)

- Primary gas remaining at or below the pre-set reserve threshold (see §1).
- Diver reports any symptom — cold, disorientation, unusual breathing effort, joint or limb discomfort.
- Comms silence beyond the pre-agreed check-in interval.
- Umbilical tension, kink, or entanglement reported by tender or diver.
- Task requires exceeding planned depth or bottom time without a replanned gas/decompression calculation already approved topside.
- Standby diver not fully suited and ready at any point the working diver is in the water.
