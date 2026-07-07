# Playbook

Filled worksheets and sequences a working locksmith actually runs, starting points to adapt, not scripts.

## 1. Owner/authority verification form (filled example)

Completed and kept on file before any lockout, rekey, or safe job — the liability record that separates this trade from unauthorized entry.

```
JOB: Residential lockout, 214 Maple St Unit 3B          DATE: 2026-06-14 14:20
REQUESTER: Dana Ruiz                    PHONE: (555) 019-2231
ID PRESENTED: Driver's license, matches service address: YES
  (if NO — see fallback order below)
SECONDARY PROOF: Lease agreement, page 1 + signature page — photographed
DISPATCH/EMERGENCY OVERRIDE: n/a
TECHNICIAN: R. Alvarez                  SIGNATURE: [signed]
NOTES: Requester locked out after losing purse; lease confirms unit and
  name match. Proceeding with non-destructive entry.
```

**Fallback order when ID doesn't match the service address directly** (most to least preferred):

1. Government ID + lease/deed/mortgage statement in the requester's name at that address.
2. Government ID + a property-management work order naming the requester as tenant/owner/agent.
3. Property manager or landlord present in person with their own ID and a management agreement, authorizing entry on a tenant's behalf.
4. Documented police or fire department dispatch (incident/case number recorded) overriding normal verification for a welfare check or emergency.
5. **No path above satisfied → decline the job and say why.** "I can't verify you have authority to this property, so I can't do the work" is a complete, professional answer; it is not the technician's job to adjudicate an ambiguous ownership dispute on a doorstep.

## 2. Rekey-vs-replace decision worksheet

**Step 1 — teardown check (2–3 sample cylinders minimum).** Pull, inspect springs and wafers/pins for wear or shear damage, check keyway for foreign material or shim marks.

**Step 2 — cycle-life check.**

```
Rated cycles (ANSI/BHMA A156.2):  Grade 1 ≈ 800,000 | Grade 2 ≈ 400,000 | Grade 3 ≈ 200,000
Estimated daily cycles (traffic observation or customer report)
Estimated annual cycles = daily × 365
Estimated years of rated life used = (years installed × annual cycles) ÷ rated cycles
```

*Example — a Grade 2 common-door cylinder at 150 opens/day, installed 3 years ago:*
annual cycles = 150 × 365 = 54,750 → rated life = 400,000 ÷ 54,750 ≈ 7.3 years → 3 ÷ 7.3 ≈ 41% of rated life consumed. Still serviceable; rekey candidate, not replace.

**Step 3 — apply the crossover rule.**

| Condition | Default |
|---|---|
| Undamaged teardown, <70% of rated cycle life consumed, no hierarchy compromise | Rekey |
| Undamaged teardown, but a master/grand-master-level key is unaccounted for | Rekey at that hierarchy level, scoped to every cylinder sharing those cuts |
| Worn/sheared parts found in teardown | Replace |
| Customer wants a genuine grade upgrade (e.g., Grade 3 builder stock to Grade 1) | Replace |
| >85% of rated cycle life consumed on a heavy-traffic door | Replace, even if undamaged — quote it before it fails on-site |

**Step 4 — cost comparison, always shown to the customer as a table, not a single number** (see SKILL.md worked example for a full filled version).

## 3. Master key system design worksheet (TPP/MACS)

**Inputs for a filled example — 6-pin cylinders, 10 available depths (0–9), MACS = 7 (manufacturer chart value, verify per pin kit):**

```
Chambers:            6
Depths available:    10 (0–9)
MACS:                7 (max depth difference between adjacent chambers)
Hierarchy:            Master (M) → Change keys (32, one per apartment unit)
Rotating constant:    Chamber 1 reserved unsplit (no master wafer) — security floor
Splittable chambers:  2–6 (5 chambers eligible for a master wafer)
```

**Design rule applied:** reserve at least 1 of 6 chambers as an unsplit rotating constant regardless of system size — dropping it to gain one more usable combination is the standard mistake that makes a cylinder easy to pick, because the added shear point at every chamber gives a pick a second travel point to feel for.

**Capacity sanity check (order-of-magnitude, not a security guarantee):** with 5 splittable chambers and MACS-constrained depth choices, a 6-pin/2-level (M + change key) system in this configuration comfortably supports the 32 unique change keys this building needs with room to spare for future units — the constraint in practice is rarely raw combinatorics, it's keeping enough chambers unsplit and enough MACS-compliant depth spacing that the system stays pick-resistant, not running out of theoretical key codes.

**Keying schedule record (what actually gets filed per system):**

```
SYSTEM: Maple St Apartments            LEVELS: Master, Change key
CYLINDER ID   LOCATION            KEYED TO           HIERARCHY LEVEL
C-01          Unit 1A             CK-01, M           Change key + Master
C-02          Unit 1B             CK-02, M           Change key + Master
...
C-33          Laundry room        M                  Master only (staff access)
C-34          Mailroom            M                  Master only
C-35          Gym                 M                  Master only
C-36          Roof access         M                  Master only
```

Update this record every time a cylinder is added, rekeyed, or a key is issued or revoked — it's the artifact that makes the next incident (lost key, tenant turnover) a scoped job instead of a guess.

## 4. Safe rating translation matrix

**Customer says "I need a good safe" — translate to two independent axes before recommending a product:**

| Burglary class (UL 687) | What it certifies | Typical use case |
|---|---|---|
| TL-15 | Resists common hand and power tools, door face only, 15 minutes net working time | Retail cash box, light commercial |
| TL-30 | Same tool set, door face only, 30 minutes | Small business, higher cash volume |
| TL-30x6 | Same 30-minute standard, attack tested on all 6 sides | Free-standing safe not against a protected wall |
| TRTL-30x6 | Adds cutting torch resistance, all 6 sides, 30 minutes | Jewelry, higher-value commercial |
| TRTL-60x6 / TXTL-60x6 | Torch (+explosives for TX), all 6 sides, 60 minutes | High-value commercial, bank-adjacent use |

| Fire class (UL 72) | What it certifies |
|---|---|
| Class 350, 1-hour | Interior stays below 350°F (paper char point) through a 1-hour standard fire exposure test |
| Class 350, 2-hour | Same threshold, 2-hour exposure |
| Class 150 / Class 125 | Lower interior-temperature thresholds for magnetic media / electronic data storage |

**The translation the customer actually needs:** ask what's being protected (cash and valuables → burglary class matters most; irreplaceable documents/media → fire class matters most; both → the safe needs a rating on both axes, and a box rated only for burglary can still cook its contents in a house fire even though nothing forced it open). Quote a model by both classes, never by burglary rating alone when the customer's stated concern is fire, or vice versa.

## 5. Lost-combination safe job (owner-verified, escalating)

1. **Verify ownership** — proof of purchase, a locksmith's or safe company's prior service record, or (for a business) a corporate officer's ID plus the entity's registration. Photograph the safe's model/serial plate before starting.
2. **Attempt manufacturer reset/recovery path first** — factory default combination records, manipulation of the wheel pack via dial feel and a borescope where the lock design allows it, or a manufacturer-issued recovery code tied to the serial number.
3. **If non-destructive recovery isn't viable, drill at the manufacturer's documented service point** for that model — the smallest opening that reaches the wheel pack or lever nose, sized to the safe's rated hard plate.
4. **Document the drill location and depth**, photograph before and after, and provide the owner a written note of what was done — this record matters for the owner's insurance and for whoever services the safe next.
5. **Reset to a new combination chosen by the verified owner on site**, install a drill-hole plug/patch per manufacturer spec if the safe is to remain UL-rated, and give the owner the new combination in writing, never left in a message or left with anyone else.

## 6. Lockout escalation ladder (non-destructive first, cost ceiling before destructive)

1. **Non-destructive manipulation** — picking, bypass tools appropriate to the specific lock type, shimming a compatible latch. Time-box this to a stated ceiling (e.g., 20–30 minutes on a standard pin tumbler) agreed with the customer before starting, especially on a billed emergency call.
2. **If non-destructive attempts exceed the agreed ceiling**, stop and present the destructive option and its cost before proceeding — don't silently escalate on the customer's dime.
3. **Destructive entry** (drilling the cylinder, cutting a low-security padlock shackle) only after the ceiling is reached or the lock type makes non-destructive entry impractical (e.g., a damaged or already-compromised cylinder).
4. **Photograph the pre- and post-entry condition** of any destructively entered lock — for the owner's records and to preempt any dispute about pre-existing damage.
5. **Replace the entered hardware** (not just leave it non-functional) before leaving the job, and confirm the verified owner has a working key before the technician leaves the site.
