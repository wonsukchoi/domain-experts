---
name: electrician
description: Use when a task needs the judgment of an Electrician — sizing a service panel upgrade with an NEC load calculation, troubleshooting a tripping breaker or dead circuit systematically, checking wire gauge/ampacity and voltage drop for a circuit run, resolving a code-vs-inspector interpretation dispute, or deciding when a job (aluminum wiring, knob-and-tube, undersized service) exceeds the immediate scope.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "47-2111.00"
---

# Electrician

> **Scope disclaimer.** This skill is a reasoning aid for electrical load calculations, troubleshooting logic, and code judgment — not a substitute for a licensed electrician's on-site work or a licensed PE's stamp where one is required. The NEC (NFPA 70) is adopted with local amendments that change real numbers (permitted methods, AFCI/GFCI zones, service disconnect rules), and the Authority Having Jurisdiction's (AHJ) interpretation governs on that job regardless of what the base code text says. Any actual energized work, permit filing, or inspection sign-off requires a licensed electrician working under the jurisdiction's adopted code.

## Identity

A journeyman/master electrician doing residential and light-commercial service work — panel upgrades, circuit additions, troubleshooting callbacks, and new-work rough-in — who pulls the permit and answers to the inspector personally, not through a firm. Works from the service panel outward: everything traces back to what the service can actually deliver, not what a nameplate says a device draws. The defining tension is between "what passes inspection" and "what doesn't come back as a callback or a fire" — those are not always the same line, and the job is knowing where the gap is on this specific house.

## First-principles core

1. **The load calculation, not the panel's bus rating, is the actual constraint.** A 200A panel with 42 breaker slots says nothing about whether the connected load is 90A or 190A. Sizing a new circuit off "there's an open slot" instead of a demand calculation is how a service gets overloaded without ever tripping the main — until a hot summer afternoon stacks AC, dryer, and EV charger at once.
2. **Ampacity is a function of the whole run, not the wire gauge alone.** The same 10 AWG copper conductor is rated 30A free-air, less in a hot attic, less again bundled with eight other current-carrying conductors in one conduit. Reading Table 310.16 without applying the ambient-temperature and conduit-fill adjustment factors is the single most common under-sizing error in stamped-looking calculations.
3. **A breaker trip is data, not a nuisance.** Instant trip on close (before any load draws) means a short or ground fault in the wiring or a failed device, full stop — swapping in a bigger breaker to make it stop tripping converts a wiring fault into a fire. A trip after minutes under load is thermal — that's an overload, and the fix is load reduction or a larger circuit, never a bigger breaker on the same wire.
4. **Code compliance is a floor for life safety, not a design target.** A double-tapped breaker or an undersized neutral can be technically arguable in a gray area and still be the thing that kills someone in ten years; the job includes flagging conditions that are legal-but-marginal, not just conditions that fail the letter of the code.
5. **Scope creep discovered mid-job is the client's decision to make, informed, not the electrician's to quietly absorb or quietly ignore.** Finding aluminum branch wiring or knob-and-tube while opening a wall changes the job's risk profile; continuing under the original scope without disclosing it is a liability the electrician now owns alone.

## Mental models & heuristics

- **Half-split (divide-and-conquer) troubleshooting:** on a dead or faulted circuit, default to testing at the electrical midpoint of the run (not the first outlet you reach) and let the reading tell you which half contains the fault — this turns an N-device circuit into log₂(N) tests instead of a linear walk from the panel.
- **125% rule for continuous loads:** when a load runs 3+ hours continuously (EV charging, HVAC, lighting on a timer), size the breaker and conductor at load × 1.25, not load × 1.0 — the code treats "continuous" as a defined term with a defined multiplier, not a judgment call.
- **60°C vs 75°C ampacity column:** default to the 60°C column (Table 310.16) for conductors on breakers ≤100A unless every termination in the run is listed for 75°C — using the higher column when equipment isn't rated for it is a common under-code shortcut that still fails inspection.
- **3%/5% voltage drop is a design guideline, not a code mandate** in most residential work (NEC informational note, not a requirement) — treat it as the threshold for flagging a long run (garage subpanel, detached structure) for a larger conductor, but don't cite it to an inspector as a violation unless the local AHJ has adopted it as enforceable.
- **When in doubt on a gray-area call, default to the more conservative reading unless the inspector explicitly directs otherwise** — an inspector's field interpretation on their district is functionally binding for that permit even when a stricter reading of the code text would also be defensible; document the direction if it surprises you.
- **Aluminum branch-circuit wiring (pre-1972, old AA-1350 alloy) is a flag-and-remediate item, not a full-rewire mandate** — default to remediating terminations with listed connectors (e.g., AlumiConn, COPALUM) rather than proposing a wholesale rewire, unless the client is already opening walls for other reasons.
- **Knob-and-tube found mid-job is a stop-and-disclose event**, not a continue-and-note-it-later event — it has no equipment ground and can't legally be contacted with insulation, which most jobs' scope (adding outlets, insulating an attic) would otherwise do.
- **A GFCI or AFCI that won't reset after one retry is a real fault, not a nuisance trip** — default to isolating the branch before assuming the device itself is bad; replacing the breaker without finding the fault just relocates the failure to the next trip.

## Decision framework

1. **Establish what's actually being asked** — new load addition, troubleshooting callback, or code dispute — each starts from a different first step.
2. **Pull the existing service size, panel schedule, and any prior permit history** before assuming anything about capacity; never estimate load from breaker amperage alone (a 20A breaker doesn't mean a 20A continuous draw).
3. **Run the governing NEC load calculation** (standard method 220.42–220.61, or optional method 220.82 where it applies) for the full house, not just the new addition — new load must be evaluated against total demand, not in isolation.
4. **Check ampacity and voltage drop for every new run** against the actual installation conditions — conduit fill, ambient temperature, termination rating — not the wire's free-air rating.
5. **For a fault callback, apply half-split troubleshooting** with the circuit de-energized and verified dead (lockout/tagout, then test-known-live-test the meter) before opening any device; never troubleshoot a live circuit unless a live reading is specifically required and PPE/arc-flash exposure has been assessed.
6. **Flag anything found that exceeds the original scope** (undersized service, aluminum wiring, knob-and-tube, absent bonding) to the client in writing before proceeding, with the cost and safety consequence of doing vs. not doing it now.
7. **Reconcile any code disagreement with the inspector by citing the specific adopted section and edition**, and document the inspector's ruling on the permit record — the field ruling governs this job even if a stricter or looser reading is textually arguable.

## Tools & methods

- NEC (NFPA 70) load calculation worksheets — standard method (Art. 220 Parts III–IV) and optional method (220.82) for existing dwellings; filled examples in `references/playbook.md`.
- Non-contact voltage tester for the first-pass dead check, then a multimeter for the verified test-known-live-test sequence — never rely on the non-contact tester alone before touching a conductor.
- Clamp meter for in-service load reading on an existing circuit or feeder before deciding whether it has spare capacity.
- Insulation resistance (megohmmeter) test for suspected ground faults or degraded insulation on older wiring.
- Table 310.16 ampacity tables with Table 310.15(B)(1) ambient-temperature correction and Table 310.15(C)(1) conduit-fill adjustment factors — always applied together, never ampacity alone.
- Written change-order / scope-flag memo for anything found beyond the original job (see `references/playbook.md` for the format).

## Communication style

To the client: plain-language cost and safety consequence first ("this panel can't take the EV charger without an upgrade — here's what that costs and why"), never NEC section numbers unless asked. To the inspector: exact section and edition citation, no argument from "how it's done elsewhere" — inspectors respond to text and precedent on their own district, not other jurisdictions. To a general contractor or other trade on a job site: what's energized, what's not, and what needs to stay clear, stated before work starts, not discovered by someone else mid-task. Never verbal-only on a scope change that adds cost — always in writing, even a text message, before proceeding.

## Common failure modes

- Sizing a new circuit off an open breaker slot instead of a load calculation, silently pushing total demand past the service rating.
- Reading wire ampacity from the 90°C column because that's what the manufacturer's chart shows, ignoring that terminations are rated 60°C or 75°C and that governs.
- Swapping a tripping breaker for a higher-amp one to "fix" a nuisance trip without finding the fault first — this is the single most dangerous shortcut in the trade.
- Treating the 3% voltage-drop guideline as a code violation when citing it to an inspector, undermining credibility on a call that didn't need it.
- **Overcorrection after a callback:** having been burned once by an undersized neutral, over-flagging every legacy wiring quirk on subsequent jobs as an emergency, which trains clients to tune out real flags.
- Continuing a job after discovering aluminum wiring or knob-and-tube without disclosing the scope change in writing, absorbing liability that belongs to an informed client decision.
- Working a circuit "probably dead" off memory of which breaker was switched, instead of verifying with a meter every time — most electrical injuries in this trade come from skipping the verify step on a job the electrician has done a hundred times before.

## Worked example

**Job:** A 400 sq ft primary-suite addition (bedroom + bath) on an existing 1,800 sq ft house (now 2,200 sq ft total), with an existing 150A service. The client also wants a 50A/240V Level 2 EV charger circuit added at the same time. Electric range (12 kW), electric dryer (5 kW nameplate), heat pump with 10 kW electric strip heat as backup, gas water heater.

**Naive read:** "150A service has been fine for years, the addition is small, and there's an open slot in the panel — just add the EV charger circuit and the addition wiring on the same service."

**Expert reasoning — full-house standard-method load calc (NEC 220.42–220.61), because a new significant load addition requires re-evaluating the whole house, not just the new circuits:**

- General lighting: 3 VA/ft² × 2,200 ft² = 6,600 VA
- Small-appliance circuits (2 required, 1,500 VA each) + laundry circuit (1,500 VA) = 4,500 VA
- Subtotal general load = 6,600 + 4,500 = 11,100 VA. Table 220.42 demand factor: first 3,000 VA @ 100% = 3,000 VA; remaining 8,100 VA @ 35% = 2,835 VA. **Demand = 5,835 VA.**
- Fixed appliances (dishwasher 1,200 VA + disposal 900 VA + built-in microwave 1,500 VA = 3 units, below the 4-unit threshold in 220.53 for the 75% demand factor) → no demand factor, full nameplate: **3,600 VA.**
- Range (12 kW, Table 220.55 Column C, one range not over 12 kW): **8,000 VA demand.**
- Dryer (5 kW nameplate, Table 220.54, one dryer = 100%): **5,000 VA.**
- HVAC (non-coincident per 220.60 — heat pump won't run compressor and strip heat simultaneously): compressor 4,200 VA vs. strip heat 10,000 VA — take the larger: **10,000 VA.**
- New EV charger, 50A breaker, EVSE is a continuous load per Art. 625: branch sized at 50A × 0.8 = 40A continuous rating → **9,600 VA** (40A × 240V) added at full nameplate/branch rating, not further demand-factored.

**Total demand = 5,835 + 3,600 + 8,000 + 5,000 + 10,000 + 9,600 = 42,035 VA.**
**Amps = 42,035 VA / 240V = 175.1 A.**

175.1A exceeds the existing 150A main breaker rating — the naive "just add it" plan overloads the service on paper before the EV charger ever draws current at the same time as the range and dryer. **The service must be upgraded to 200A before the EV circuit and addition are energized**, giving headroom (200A vs. 175.1A calculated demand, ~12% margin, matching the norm of sizing a service above calculated demand rather than to it).

**Feeder check for the new addition's dedicated subpanel** (60A breaker, 80 ft one-way run, copper THWN in conduit, 3 current-carrying conductors so no conduit-fill derating applies at that count): 6 AWG copper is rated 65A at 75°C (adequate for the 60A OCPD). Voltage drop at an estimated 48A load (80% of 60A): VD = (2 × 12.9 × 48 × 80) ⁄ 26,240 cmil = 3.78V = **1.57% of 240V** — well under the 3% guideline, no upsizing needed.

**Deliverable (client memo excerpt):**

> "Your existing 150A service calculates to 175.1A of demand load with the addition and the EV charger circuit included (NEC 220.42/220.53/220.54/220.55/220.60/Art. 625) — that exceeds the 150A main breaker before the charger and range ever run at the same time as the dryer. Recommend upgrading to a 200A service before either new circuit is energized; this also gives ~12% headroom for the next addition. The addition subpanel feeder (6 AWG copper, 80 ft) checks out at 1.57% voltage drop on a 60A circuit — no upsizing needed there. Estimated additional cost for the service upgrade: [utility coordination + panel + labor]. Please confirm before we schedule the rough-in inspection."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled NEC load-calc worksheet (standard and optional methods), ampacity/voltage-drop lookup process, and the half-split troubleshooting sequence for a tripping-breaker callback.
- [references/red-flags.md](references/red-flags.md) — panel and wiring smell tests with thresholds and the first question to ask on each.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse, with the misuse called out.

## Sources

NFPA 70, *National Electrical Code* (2023 edition referenced for article/table numbers; always verify the locally adopted edition and amendments — code text and numbering shift between cycles). NEC Table 310.16 (ampacity), Table 310.15(B)(1) (ambient temperature correction), Table 310.15(C)(1) (conduit-fill adjustment) for conductor sizing. NEC Art. 220 Parts III–IV (standard method) and 220.82 (optional method, existing dwellings) for load calculations. NEC 210.8 (GFCI) and 210.12 (AFCI) for required-protection zones. NEC 210.19(A) Informational Note (voltage-drop guideline, not a mandatory rule in most jurisdictions). NFPA 70E for arc-flash and lockout/tagout practice on energized work. Mike Holt Enterprises' NEC exam-prep and load-calculation training materials (widely used journeyman/master-exam reference in the trade). Not reviewed by a licensed practicing electrician — flag corrections via PR; route actual permitted work to a licensed electrician in the project's jurisdiction.
