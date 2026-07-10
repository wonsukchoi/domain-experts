# Vocabulary

### True position (GD&T)
A diameter-based tolerance zone around a theoretically exact location, rather than a linear ± tolerance on a distance.
**In use:** "True position on those holes is ⌀0.010" — measure the combined radial deviation, not just the center-to-center distance."
**Common misuse:** Treating it as an ordinary ± linear tolerance on center distance, which ignores that the deviation is a combined radial value compared against a diametral zone, not an axis-by-axis check.

### MMC (Maximum Material Condition)
The tolerance condition where a feature contains the most material — the largest allowed size for an external feature, or the smallest allowed size for an internal one like a hole.
**In use:** "MMC on this hole is ⌀0.250" — the minimum allowed diameter, not the maximum."
**Common misuse:** Assuming MMC always means "the biggest size," which holds for shafts but inverts for holes — a common source of GD&T confusion.

### Bonus tolerance
Additional positional tolerance earned when a feature is produced away from its MMC size.
**In use:** "Hole measured 0.003" over MMC, so we get 0.003" of bonus tolerance on top of the printed ⌀0.010"."
**Common misuse:** Skipping the bonus-tolerance calculation entirely and rejecting a part that's actually within the total allowable tolerance once the produced size is factored in.

### Datum
A theoretically exact reference — a point, line, or plane — that other dimensions and tolerances are measured from.
**In use:** "We're fixturing off datum A and B exactly as called out, not whatever surface happens to sit flattest."
**Common misuse:** Treating any convenient flat or square surface as "the datum," rather than the specific one named and ordered in the print's feature control frame.

### First article inspection (FAI)
The full dimensional check of the first part produced from a new setup or program, before the batch runs.
**In use:** "FAI's clean on all but one hole — checking the fixture offset before running the rest of the lot."
**Common misuse:** Skipping it on a "simple" repeat job, on the assumption that a correct program guarantees a correct part regardless of that day's physical fixture and offset setup.

### Speeds and feeds
The cutting speed (surface feet per minute) and feed rate (inches per revolution or per minute) parameters for a given cut.
**In use:** "Chart says 400 SFM for this alloy, but we're backing it off — chip color says otherwise."
**Common misuse:** Treating catalog speeds and feeds as fixed correct values instead of a tuning starting point that gets adjusted against actual tool condition and cutting evidence.

### Chip load
The thickness of material removed per cutting edge per revolution, which governs tool wear rate and surface finish.
**In use:** "Chip load's too aggressive for a 2-flute tool at that feed rate — that's why it's chattering."
**Common misuse:** Confusing chip load with feed rate alone, without accounting for the number of flutes or teeth actually doing the cutting.

### Work coordinate system (WCS) / zero offset
The programmed origin point a CNC program's coordinates are measured from, physically established on the machine at each setup.
**In use:** "WCS zero's off by a thousandth on this setup — that's the whole part shifting, not a program error."
**Common misuse:** Assuming the work coordinate system is inherent to the program itself, rather than something re-established — and potentially wrong — at every new physical setup.

### Tool life
The expected cutting duration or part count a tool can produce before wear degrades dimension or finish past acceptable limits.
**In use:** "That insert's at 140% of rated tool life — swap it before the next batch, not after a bad part shows up."
**Common misuse:** Running a tool well past its rated life because it "still looks fine," ignoring that dimensional drift often precedes any visible damage to the tool itself.

### Datum feature order
The sequence — primary, secondary, tertiary — in which datums are referenced in a feature control frame, which determines how a part is physically fixtured and measured.
**In use:** "Datum order is A-B-C — fixture off the face first, then the pin, then the edge, in that sequence."
**Common misuse:** Assuming any combination of flat, square surfaces works as long as the part sits stable, when the specified order actually changes which dimensions are being controlled and how measurement error propagates.
