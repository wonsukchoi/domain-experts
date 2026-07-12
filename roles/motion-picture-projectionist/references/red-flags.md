# Red flags

Smell tests a booth catches before they become a stopped show. Format for each: what it usually means, the first question to ask, and the data to pull.

## 1. KDM validity window closes within 48 hours of a scheduled showtime

**Usually means:** the distributor issued a short-window key by default (common for early or first-run bookings), or the request for an extension was never made. It is not usually malicious or an error on the booth's part — it's a default that needs active management.

**First question:** "Has an extended or replacement KDM been requested yet, and when is it due back?"

**Data to pull:** the KDM's stated valid-from/valid-until timestamps against the full run of scheduled showtimes for that title, not just tomorrow's; the distributor's key-request turnaround time on file.

## 2. Server ID mismatch on a title that shows as "ingested"

**Usually means:** hardware was serviced or replaced (server, IMB) after the KDM was issued, and the key was generated against the old ID. Ingestion and validation both check the file, not whether the key matches this specific piece of hardware.

**First question:** "Was any server or IMB hardware touched since this KDM was issued?"

**Data to pull:** current server/IMB serial number, the serial number the KDM was issued against (visible in KDM metadata), and the date of the most recent service ticket.

## 3. Brightness complaint on a 3D show, lamp otherwise logging normal hours

**Usually means:** a fault in the 3D optical path (polarizing filter wheel misalignment or wrong orientation, glasses batch defect) rather than the lamp, since 2D and 3D share the same source. Swapping the lamp here fixes nothing and burns a consumable.

**First question:** "What does the 2D reading say on this same lamp, right now?"

**Data to pull:** photometer readings at screen center in both 2D and 3D (target ranges: 2D 11–17 fL, 3D roughly 4.5–7 fL); expected 3D reading estimated at ~40–45% of the 2D reading — a measured ratio well below that points at the 3D hardware, not the source.

## 4. Frame stutter or full stall mid-reel, same title, more than once in a week

**Usually means:** degraded RAID/storage on the server rather than a one-off file corruption — a single bad-file event doesn't usually recur across multiple showings of the same title.

**First question:** "Has this happened on any other title in the same auditorium this week?"

**Data to pull:** server storage health/RAID status logs, playback error codes with timestamps, whether the pattern is title-specific or auditorium-specific (the latter points at hardware, not content).

## 5. Audio channel dropout or dialogue noticeably quiet, specific to one auditorium

**Usually means:** a channel-routing or amplifier gain change that wasn't logged after a format switch or service call, not a content or DCP fault.

**First question:** "What was the last audio configuration change made in this room, and by whom?"

**Data to pull:** current fader/reference-level setting against the room's calibrated reference (pink-noise SPL reading), amplifier channel map, service log for that auditorium.

## 6. Masking or aspect ratio visibly wrong at the start of a show

**Usually means:** a leftover preset from the prior title in that slot, since automation plays exactly what it's configured for and doesn't detect a mismatched aspect ratio on its own.

**First question:** "What was the aspect ratio of the previous title scheduled in this slot, and does the current masking preset match it instead of tonight's title?"

**Data to pull:** the title's stated aspect ratio from distributor technical notes; the auditorium's masking preset log/history.

## 7. Reel or CPL runtime doesn't reconcile with the posted showtime buffer

**Usually means:** either a wrong-version ingest (an extended cut, a different regional CPL) or an undercounted pre-show/trailer package pushing the actual start later than scheduled.

**First question:** "Does the ingested CPL's runtime match the distributor's published runtime for this title, to the second?"

**Data to pull:** CPL runtime metadata, trailer/ad-package runtime, gap to the next scheduled showtime in that auditorium.

## 8. Xenon lamp past ~80% of rated hours with any flicker reported

**Usually means:** genuine end-of-life degradation compounding with electrode wear — flicker at this stage tends to worsen quickly rather than plateau, unlike early-life flicker which is often a strike/ignition issue.

**First question:** "What are the logged hours, and has flicker been reported before or only recently?"

**Data to pull:** cumulative lamp hours from the consumables log, date of last reported flicker, current photometer reading against the 2D target.

## 9. 3D ghosting or crosstalk complaints across multiple seats, not isolated to one section

**Usually means:** a system-wide polarization or sync issue (filter wheel timing, glasses batch) rather than a seating-angle artifact, which would cluster in specific rows instead.

**First question:** "Are the complaints clustered in particular seats, or spread across the house?"

**Data to pull:** seat locations of complaints, filter wheel sync/timing status if available, a sample of the glasses in circulation for that showing.

## 10. Server requiring repeated reboots on the same day, same auditorium

**Usually means:** an underlying hardware fault (storage, power supply, thermal) that a reboot masks temporarily rather than resolves — treat the second reboot in a day as an escalation trigger, not routine.

**First question:** "Is this the first reboot today in this room, or has it happened before during this shift?"

**Data to pull:** reboot/crash timestamps for the day, any correlated error codes, ambient booth temperature if thermal shutdown is suspected.

## 11. New title's booth log has zero pre-show calibration entries

**Usually means:** the pre-open spot-check was skipped under time pressure, not that everything happened to be fine — an unlogged check and a passed check look identical after the fact, which is exactly the gap that lets a masking or luminance miss reach the audience.

**First question:** "Was the pre-open calibration actually run for this format, or assumed carried over from the last check?"

**Data to pull:** the calibration log's last entry timestamp for that auditorium and format combination.
