# Red flags

Smell tests a PV installer or design reviewer catches on a permit-set review, a site walk, or a warranty-claim review. Format for each: what it usually means, the first question to ask, and the data to pull before signing off.

## 1. String voltage calculated only at STC (25°C), no cold-temperature correction in the permit set

**Usually means:** the designer checked Voc against the inverter's max input voltage at STC and stopped — a string that passes at STC can still exceed the inverter's max on the site's coldest morning, since Voc rises as temperature falls.

**First question:** "What temperature was this Voc calculation run at, and does it match the site's NEC 690.7 lowest-expected-ambient temperature?"

**Data to pull:** the module's published temperature coefficient of Voc; the site's ASHRAE 2% extreme minimum design temperature; a recalculation of string Voc at that temperature against the inverter's max input voltage.

## 2. Inverter faults or trips concentrated on cold, clear mornings

**Usually means:** the string is over-length for the site's actual cold-weather Voc — a classic signature, since cold-and-clear conditions produce both the lowest ambient temperature and the highest module output simultaneously, maximizing Voc exactly when the inverter is most exposed.

**First question:** "What's the string's calculated Voc at this site's design-low temperature, versus the inverter's max input voltage?"

**Data to pull:** inverter fault logs with timestamps and ambient temperature at time of fault; module Voc temperature coefficient; string module count.

## 3. Rapid-shutdown compliance documented only at the array's combiner or disconnect, with no module-level device listed

**Usually means:** the outside-array-boundary requirement is met but the inside-array-boundary requirement isn't — current NEC 690.12 requires module-level (or sub-array-level) de-energization, not just a single array-output control point.

**First question:** "Where's the rapid-shutdown control point for the conductors between individual modules, not just at the array's single output?"

**Data to pull:** the equipment list and its rapid-shutdown listing (module-level power optimizer/microinverter datasheet, or listed array-boundary RSD system documentation); the one-line diagram showing where each RSD device sits relative to individual modules.

## 4. Rapid-shutdown initiation not timed and voltage-measured at commissioning

**Usually means:** the system was installed with equipment that's *rated* for compliant rapid shutdown but never actually verified on this specific installation — wiring errors or a mis-configured relay can leave a "compliant" system slow or non-functional in practice.

**First question:** "Has anyone actually timed the voltage drop at the array after hitting the rapid-shutdown switch, or are we relying on the equipment's listing alone?"

**Data to pull:** commissioning test log showing elapsed time and measured voltage at a point within 1 ft of the array and at a point between modules inside the array.

## 5. Backfeed breaker sized by a flat number ("standard practice") rather than a calculation shown against both NEC 690.8(A) and the 705.12(B)(3)(c) 120% rule

**Usually means:** the breaker may happen to be within the busbar ceiling but not matched to the inverter's actual continuous output current — either oversized (eating headroom a future addition needs) or, in the worse case, undersized relative to a larger inverter than originally scoped.

**First question:** "What's the inverter's actual continuous AC output current, and what does 125% of that number come out to, versus what's on this breaker?"

**Data to pull:** inverter nameplate continuous output current; busbar and main breaker rating; the completed 120%-rule arithmetic for this specific panel.

## 6. A panel already near its 120%-rule ceiling, with a second PV source, battery, or EV charger backfeed proposed later

**Usually means:** the busbar has no remaining headroom under 705.12(B)(3)(c) for the new addition without a panel or busbar upgrade — a common gap when the original PV install consumed the full allowable backfeed ceiling.

**First question:** "What's the busbar's 120%-rule ceiling, and how much of it is already committed to the existing PV breaker?"

**Data to pull:** busbar rating, main breaker rating, and every existing backfed breaker on that busbar with its rating; the recalculated ceiling with the proposed addition included.

## 7. Racking lag bolts sealed with sealant/caulk directly over shingles, with no flashing visible in installation photos

**Usually means:** a surface-mount-plus-sealant shortcut instead of a flashed mount integrated into the shingle course order — sealant alone degrades with UV and thermal cycling in a way a properly lapped flashing doesn't depend on.

**First question:** "Was this attachment flashed under the course above, or is the sealant the only barrier?"

**Data to pull:** installation photos from before the shingle course was reinstalled (if any); the racking manufacturer's specified attachment method for this roofing material; a physical inspection of the penetration if accessible.

## 8. Roof leak reported within the first 1-2 winters after a PV install, with no penetration-by-penetration photo record

**Usually means:** without documentation, liability defaults to "blame the last trade that touched the roof" — which may be the solar installer even if the actual cause is a pre-existing roofing deficiency, or may let a genuine solar-attachment leak go uncorrected because it's wrongly written off as a roofing issue.

**First question:** "Do we have a photo of this specific penetration before the shingle course went back down?"

**Data to pull:** the job's penetration photo log; the original roofing scope of work (age and condition of the roof at install time); a physical inspection of the leak's actual entry point versus the nearest attachment point.

## 9. Attachment spacing uniform across the whole array with no reference to an engineering letter or the site's wind/snow load

**Usually means:** spacing was set by habit ("every 4 ft") rather than by the racking manufacturer's pull-out rating for the actual fastener and rafter species, checked against the site's structural loads — a real wind-uplift risk on a high-wind-zone or heavy-snow-zone site.

**First question:** "What's the pull-out rating this spacing is based on, and does it account for this site's wind/snow load, or is it a carryover spacing from a different job?"

**Data to pull:** the racking manufacturer's engineering letter or pull-out test data for the specific fastener/rafter combination used; the site's wind and snow design loads.

## 10. Module or string count changed in the field after permit issuance, with no resubmitted voltage calculation

**Usually means:** a field change (added module, substituted a different module model) invalidated the permitted string-voltage and rapid-shutdown design without anyone rerunning the numbers — the single most common way a "permitted, inspected" system ends up out of spec.

**First question:** "What changed between the permitted design and what's actually on the roof, and has the string-voltage calculation been rerun against that change?"

**Data to pull:** the permitted one-line diagram and load calculations; current as-built module count and model per string; a recalculated Voc at the site's design-low temperature using the as-built configuration.
