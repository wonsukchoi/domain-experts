# Playbook

Filled procedures a tire repairer/changer actually runs — inspection sequences, substitution tables, and torque charts, with real thresholds and example numbers.

## 1. Puncture inspection and repair decision procedure

**Steps, always in this order:**

1. **Read the DOT date code.** Format `XXXX WWYY` (week/year), e.g. `3221` = week 32 of 2021. Tire is 4+ years old going into this inspection — note it regardless of what the injury turns out to be.
2. **Demount the tire fully.** Never assess or repair from the outside. An external-only look cannot rule out an injury that entered the shoulder at an angle and traveled toward the crown, or hidden inner-liner separation from a prior underinflation event.
3. **Locate the injury and measure it.** Two independent checks, both must pass:
   - **Zone check:** is the injury inside the tread/crown area, bounded by the shoulder? If it's in the shoulder or sidewall — repair conversation ends here, tire is condemned, regardless of size.
   - **Size check:** is the injury ≤1/4 in (6mm) diameter? Larger than that in the tread — condemned.
4. **Inspect the inner liner around the injury** for a second puncture, a bulge, or ply separation. Any of these condemns the tire even if the primary injury passed steps 1–3.
5. **If it passes all checks, perform a combination repair** (Step 2 below) — never a plug alone, never a patch applied without buffing and inspecting the inner liner first.
6. **If it fails any check, condemn and document** the reason on the invoice: zone, size, or secondary damage — specific reason, not "not repairable."

## 2. Plug vs. patch vs. combination repair — what's legal, what isn't

| Method | What it is | Standard status | When it shows up anyway |
|---|---|---|---|
| Plug only (outside-in, no demount) | Sticky rope plug pushed into puncture from the tread face, tire never removed from rim | Not a legal repair per USTMA/TIA standard — no inner-liner inspection possible, no seal of the inner liner | Roadside/get-home fixes only, explicitly time- or mileage-boxed, never invoiced as a completed repair |
| Patch only (inside, no plug/stem) | Rubber patch cemented to the inner liner over the injury, no filler in the puncture channel | Insufficient alone — patch seals the liner but leaves the puncture channel itself open to moisture and corrosion of steel belts | Rare; some shops use for very shallow injuries, but combination is the actual standard |
| **Combination repair (patch-plug unit)** | Demount → buff injury and inner liner → apply vulcanizing cement → install one-piece repair unit with plug stem through the puncture and patch bonded to the liner → trim stem flush | **The only method meeting USTMA/TIA standard** | Every qualifying repair, no exceptions for schedule pressure |
| Section repair | Larger patch spanning a bigger injury, still tread-area only | Valid for tread injuries beyond typical plug diameter but still within the repairable zone, per repair-unit manufacturer's size rating | Larger nail/screw injuries still confined to tread |

**Rule:** if the shop doesn't have a demounted tire on the rack and cement curing, it hasn't performed a repair — it's performed a temporary fix, and the customer needs to hear that distinction in those words.

## 3. Load range / speed rating substitution decision table

Pull two numbers before any substitution conversation: the vehicle's placard GAWR (front and rear, separately) and the T&RA-rated load capacity of the tire in question at its rated inflation.

**Example, LT245/75R17 (common 3/4-ton pickup fitment):**

| Load range | Ply rating | Max load per tire | Rated cold inflation |
|---|---|---|---|
| C | 6-ply | 2,335 lbs | 50 psi |
| D | 8-ply | 2,679 lbs | 65 psi |
| **E (OE on most 3/4-ton trucks)** | 10-ply | 3,042 lbs | 80 psi |

**Decision sequence:**

1. Take the axle's GAWR from the placard, divide by 2 (or by tire count on dual-rear-wheel axles) — that's the minimum per-tire capacity required.
2. Compare against the proposed tire's rated load at its rated inflation, not at whatever pressure is currently in the tire.
3. If the proposed load range clears the per-tire minimum **and** matches the load range already on the other tires on that axle (or all four, for most passenger/light-truck applications) — proceed.
4. If it clears the minimum but doesn't match the other tires' load range or rated inflation — flag the construction/inflation mismatch explicitly in writing, even though the raw number technically passes. A single mismatched corner runs a different psi schedule and flex characteristic than its axle-mates.
5. If it doesn't clear the minimum at all — refuse outright; this is not a disclose-and-proceed situation, it's a hard no.

**Speed rating mismatch, when unavoidable (e.g., one tire lost, matching speed rating unavailable same-day):**

- Never mix speed ratings on the same axle.
- If mixing across axles is unavoidable, put the **lower**-rated tires on the **rear** axle (TIA guidance, applies to both FWD and RWD) to bias any high-speed handling change toward understeer.
- Overall vehicle speed capability is limited to the lowest-rated tire on the vehicle — tell the customer this number, not the number on the tire they kept.
- Document the mismatch and the customer's acknowledgment on the invoice.

## 4. TPMS relearn procedure by system type

| System type | How it works | Relearn trigger | Typical procedure |
|---|---|---|---|
| Direct TPMS | Pressure sensor inside each wheel, transmits ID + pressure to a receiver | Any wheel/tire removal, sensor replacement, or rotation | **Stationary relearn** (ignition on/off sequence with the vehicle parked, per make) **or OBD-triggered relearn** (scan tool writes new sensor IDs directly) — check the make; some are one, some the other, some support both |
| Indirect TPMS | Infers pressure loss from wheel-speed-sensor differences via ABS, no physical pressure sensor | Any tire replacement, rotation, or pressure reset | Menu-based reset through the instrument cluster or infotainment system — no physical sensor to relearn, but the reset step is still required or the system compares against the old rolling-radius baseline |

**Sequence:**

1. Identify system type (direct vs. indirect) before starting — don't assume based on dash light behavior alone.
2. Complete the mechanical work (tire service, wheel reinstall, torque) first.
3. Set all four tires to the placard-specified cold inflation — relearn procedures on many direct systems will fail or produce false IDs if pressures are inconsistent going in.
4. Run the make-specific relearn (stationary sequence or scan tool) or the indirect system's reset menu.
5. Confirm the dash TPMS light clears and, where the tool supports it, confirm each wheel position reports a live sensor ID before releasing the vehicle.
6. If the light doesn't clear — rerun the relearn once before condemning the sensor. A skipped step or pressure inconsistency during the first attempt is a more common cause than hardware failure.

## 5. Wheel torque and lug-nut sequencing

**Star/cross patterns by lug count:**

| Lug count | Torque sequence (positions numbered clockwise from 12 o'clock) |
|---|---|
| 4-lug | 1 → 3 → 2 → 4 |
| 5-lug | 1 → 3 → 5 → 2 → 4 |
| 6-lug | 1 → 4 → 2 → 5 → 3 → 6 |
| 8-lug | 1 → 5 → 3 → 7 → 2 → 6 → 4 → 8 |

**Staged torque sequence (any lug count):** run the full star pattern at roughly 1/3 final spec, then 2/3, then full spec — never seat any single lug to final torque before every lug has had at least one pass. A tire shop example: passenger car spec 100 ft-lbs → passes at ~35 / ~70 / 100 ft-lbs. Light truck spec 150 ft-lbs → passes at ~50 / ~100 / 150 ft-lbs.

**Re-torque:** check all lugs at 25–50 miles or the customer's next visit, whichever comes first, on any wheel that was removed — new-wheel and aftermarket-wheel installs settle onto the hub under initial driving load, and factory torque commonly reads a few percent low on recheck even when correctly applied the first time.

## 6. Run-flat tire special handling

1. Ask, before inspecting: has this tire been driven with the pressure warning active or with visibly low/zero pressure? If yes and the tire is a run-flat/self-supporting design, skip straight to condemnation — the reinforced sidewall carries the vehicle's weight without air pressure for a limited distance, and that overload event damages the casing structurally in ways an external or even inner-liner visual inspection won't reveal.
2. Run-flat tires are not rated for repair by most major manufacturers (Bridgestone DriveGuard, Michelin ZP among them) even for injuries that would otherwise qualify under the standard size/zone rule — check the specific manufacturer's repair policy before proceeding, and default to no-repair if the policy isn't confirmed.
3. Vehicles equipped with run-flats from the factory frequently have no spare and rely entirely on TPMS for a low-pressure warning — confirm TPMS is functional and relearned before releasing the vehicle, since there's no backup warning system if it isn't.
