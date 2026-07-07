# Playbook

Filled procedures a technician actually runs, with real targets and step sequences — starting points to adapt per instrument, not scripts to follow blind.

## 1. Aural stretch-tuning sequence (piano)

Run with an ETD assisting, never dictating the final call.

1. **Set the temperament octave**, typically F3-F4 on a grand. Tune F3 to the ETD's reference pitch (A440 or the client's stated reference), then tune each note up to F4 by ear, checking:
   - **4ths and 5ths** for a smooth, evenly-decreasing beat rate across the octave (a 5th should beat slightly faster as you ascend; an uneven jump means a note is off).
   - **Major 3rds and 6ths**, whose beat rates roughly double as they widen by an octave — the classic aural cross-check (e.g., a major 3rd beating at ~7 beats/sec should have its extension a 10th up beating close to ~14/sec).
2. **Tune outward octave by octave**, checking each new octave against the **2:4 and 4:2 tests** (compare the new note's 2nd partial against the reference note's 4th partial, and vice versa) rather than trusting a straight 2:1 octave, because a beatless straight octave on a piano is usually a hair narrow of what the ear wants once partials are considered.
3. **Reconcile the ETD reading against the ear on every note.** The ETD gives a fast starting pull (accounting for this piano's own measured inharmonicity if it has a "aural style" calculation mode); the ear makes the final call on unisons and any note where the two disagree by more than ~1-2 cents.
4. **Set unisons last, note by note**, muting two of the three strings and tuning the third pure to the now-fixed reference string, then bringing in the second string and listening for **false beats** (a slow wow inside the unison itself, distinct from the octave/temperament beats) — a false beat means a bad string, not a tuning error, and gets flagged for replacement rather than chased indefinitely.
5. **Log the stretch curve actually used** (cents deviation from theoretical at A0, A1...A7, C8) so the next tuning starts from this piano's known behavior instead of a generic curve.

**Typical stretch magnitude** (illustrative, varies by scale design and string length): roughly 0 cents near the temperament octave, widening to -15 to -30 cents by A0 and +20 to +35 cents by C8. Upright pianos with shorter bass strings often need *more* stretch at the bottom than a grand of comparable size, because shorter, thicker bass strings are more inharmonic.

## 2. Piano action regulation pass

Order matters — regulate in this sequence so later steps aren't undone by earlier ones:

| Step | Target | Typical spec |
|---|---|---|
| 1. Key height & level | Keys level across the keyboard, front of key at rest | ~2-3/16" (11mm) above keyslip, consistent within ~1/32" across all keys |
| 2. Key dip | Downward travel of the key | 3/8"-10mm typical (grand); deeper dip on some verticals |
| 3. Hammer blow distance | Rest position of hammer from string | 1-7/8" (47.6mm) grand standard |
| 4. Let-off (escapement) | Gap between hammer and string just before contact | 1/16"-3/32" (1.5-2.4mm); too little causes blocking (hammer sticks against string), too much wastes touch travel and softens tone control |
| 5. Drop | Distance hammer falls after let-off before resetting | ~1/8" (3mm) typical, checked after let-off is set |
| 6. Touchweight (down-weight) | Static force to depress a key from rest to bottom | 48-52 grams typical for a grand action; up-weight (force to let the key rise back) 18-24 grams; friction = down-weight minus up-weight, ideally under ~20g |
| 7. Voicing | Tone quality via hammer-felt needling/hardening | done last — regulation changes hammer travel and blow distance, both of which affect the tone voicing is meant to fix |

**Rule:** if touchweight is out of spec on more than a few keys, check for a common cause (hammer mass added by rebuilding, worn key bushings adding friction) before individually leading/unleading each key — a systemic cause needs a systemic fix.

## 3. Guitar/string-instrument setup order

Always in this order — each step assumes the one above it is already correct:

1. **Level the frets** (check with a notched straightedge or fret rocker) before setting anything else; a high fret invalidates every later measurement.
2. **Set neck relief.** With a capo at the 1st fret and the low E string fretted at the body/neck joint (usually 14th-17th fret), measure the gap at the 7th-8th fret with a feeler gauge. Target ~0.010"-0.012" (0.25-0.3mm) for typical steel-string setups; slightly more for heavier gauge strings or lower tunings, close to zero (but not back-bowed) for a very low, buzz-tolerant "shred" setup.
3. **Set action height** at the 12th fret, measured from the fret top to the bottom of the string:

| Instrument type | Bass side (low E) | Treble side (high e) |
|---|---|---|
| Steel-string acoustic | 2.0-2.4mm (~6/64") | 1.6mm (~4/64") |
| Electric guitar | 1.6mm (~4/64") | 1.2mm (~3/64") |
| Classical/nylon-string | 3.5-4.0mm | 2.8-3.2mm |

4. **Cut the nut slots** to just clear the 1st fret when fretted at the 2nd (open strings should not buzz, but should sit close enough that first-position chords don't fight excess string height).
5. **Set intonation** (saddle compensation) last, checking pitch at the 12th fret harmonic against the fretted 12th fret note per string, then fine-adjusting saddle position; wound strings typically need more compensation (saddle moved back) than plain strings.
6. **Recheck relief and action after string changes or tuning changes** — different gauges or tunings change neck tension and shift every number above.

## 4. Woodwind pad seating & leak test

1. **Leak-light test.** In a darkened room, shine a small light inside the instrument (or under the pad cup) while the key is held closed under normal spring tension. Any visible light bleeding around the pad's circumference marks a leak location.
2. **Pull-through (feeler) test.** Slide a thin paper shim or feeler strip under the closed pad and pull it out slowly at four points around the circumference (12, 3, 6, 9 o'clock). Drag should feel even at all four points; a spot with noticeably less resistance is where the pad isn't seating.
3. **Reseat or replace.** Heat-set pads can be reseated by warming the cup and re-pressing against a feeler card to even out the seal; worn, hardened, or torn pads get replaced rather than chased with reseating alone.
4. **Recheck spring tension** after pad work — a pad that seats perfectly with the key held shut by hand but leaks under normal playing spring tension has a spring problem, not a pad problem.
5. **Register/vent key height** gets set after the main pads, since it interacts with tone-hole venting rather than sealing — typical clarinet register vent height runs ~2.5-3mm, checked against response in the upper register (too low chokes the note, too high makes it unstable/sharp).

## 5. Brass valve/slide alignment

1. **Check port alignment** with the valve depressed: sight down the casing and confirm the valve's ports line up flush with the outer casing's tubing at both top and bottom. Misalignment as small as a partial turn measurably restricts airflow and feels "stuffy" even with fresh oil.
2. **Check felt/cork bumper thickness** against the valve's specified travel — worn bumpers let the valve travel too far, which can misalign the ports at the bottom of the stroke even if they align at rest.
3. **Check casing for dents or out-of-round spots** along the valve's travel path; a valve that binds partway down almost always has a casing dent at that height, not a lubrication problem.
4. **Slide fit and tension** — slides should move with even resistance across their full travel, not snug in one spot and loose elsewhere; uneven tension usually means a slightly bent slide tube.

## 6. Humidity targets by instrument family

| Instrument | Target RH | Danger zone | Typical failure below/above |
|---|---|---|---|
| Piano | 42-50% | Below ~35% (sustained) | Soundboard crown loss, cracking, tuning instability |
| Steel-string/acoustic guitar | 45-55% | Below ~35% | Top cracks, fret ends protruding ("fret sprout"), action drop |
| Violin family | 40-60% | Below ~30% or rapid swings | Open seams (by design, as a pressure-relief joint), soundpost/bridge shifts |
| Woodwinds (wood body, e.g. grenadilla clarinet/oboe) | 40-55%, avoid rapid swings during break-in especially | Rapid swings during first year | Bore cracks, especially near tone holes |

**Monitoring method:** place the hygrometer/data logger inside the case or piano cabinet, not just in room air — case-level RH lags and dampens room swings and is what the instrument actually experiences. A swing of more than ~10 percentage points within a week, regardless of the absolute number, is the more useful red flag than a single out-of-range reading.
