# Red flags

Smell tests an operator catches on a walk-down or a handoff conversation. Format for each: what it usually means, the first question to ask, and the data to pull before deciding whether to correct on the spot or escalate.

## 1. Belt walks the same direction whether loaded or empty

**Usually means:** structural or idler misalignment — a cause that persists regardless of load, not a load-placement issue that would only show up under material.

**First question:** "Does it walk the same way with the belt empty as it does loaded?"

**Data to pull:** framing-square reading at the nearest training idler, tracking log for the last three shifts, whether the pattern is new or long-standing.

## 2. A training-idler correction fails to hold for a full shift, on the second or later attempt

**Usually means:** the correction is treating a symptom of a structural cause outside the idler itself, not an idler that simply needs periodic re-adjustment.

**First question:** "Has this exact idler been adjusted for this same walk within the last two shifts?"

**Data to pull:** the last three tracking/adjustment log entries for that station, hours held after each correction.

## 3. Edge fraying or spillage concentrated at one specific point along the belt, not distributed along its length

**Usually means:** localized mistracking or a chute/loading-point misalignment at that station, not a general housekeeping or wear issue.

**First question:** "Is this happening at one station consistently, or is material loss spread out?"

**Data to pull:** spillage/housekeeping logs by location, last tracking reading at that specific station.

## 4. Motor amperage is high (near full-load amps) while measured throughput is well under the conveyor's rated capacity

**Usually means:** friction or misalignment drag (a bearing, a misaligned pulley) rather than the conveyor being overloaded — amperage and rated capacity are independent signals.

**First question:** "What's this conveyor's actual tph right now, computed from measured belt speed, against its rated capacity — not just what the ammeter reads?"

**Data to pull:** current motor amp draw vs. full-load amp rating, tachometer speed vs. nameplate design speed, computed actual tph.

## 5. A conveyor's tachometer-measured belt speed sits more than 10% below its nameplate design speed with no open work order explaining why

**Usually means:** an unticketed workaround (often for a mistracking or slip issue) that quietly became the new normal and is now constraining line throughput.

**First question:** "When was this conveyor last running at full design speed, and what changed?"

**Data to pull:** speed log history, route/shift notes around the date speed dropped, any related maintenance tickets.

## 6. Only the electrical main disconnect is locked out on a conveyor with a gravity take-up or an inclined loaded belt

**Usually means:** isolation is incomplete — stored/potential energy in the counterweight carriage or the loaded incline can still move the belt or drop the carriage.

**First question:** "Is the gravity take-up counterweight physically blocked or chained, separate from the electrical lock?"

**Data to pull:** the conveyor's energy-source list for its specific configuration, physical confirmation (not just a checklist mark) that the block/chain is engaged and load-bearing.

## 7. A guard panel at a nip point is found propped open, removed, or routinely used as a jam-clearing access point

**Usually means:** the guard is functionally defeated regardless of whether its physical design meets the distance/opening standard — a practice problem, not just a hardware gap.

**First question:** "Is this panel ever opened during normal operation, and how is a jam actually cleared here?"

**Data to pull:** incident/near-miss log for that station, interview of the operator(s) who clear jams there, guard's installation spec vs. its current physical state.

## 8. A mechanical splice fastener's rated capacity sits within a thin margin of the belt's actual operating tension

**Usually means:** the fastener, not the belt, has become the limiting component — a tension spike from a jam or surge risks splice failure before the belt body would fail.

**First question:** "What percentage of this fastener's rated capacity is the belt actually running at right now?"

**Data to pull:** fastener type and its rated tensile percentage, current measured or calculated operating tension, belt tension history if tension has increased since the splice was installed.

## 9. Splice fastener plates show elongated bolt holes, missing fasteners, or visible gapping at the splice line

**Usually means:** the splice is nearing end of service life under its current tension and fastener type — a progressive mechanical fatigue, not a one-time defect.

**First question:** "How long has this splice been in service against this fastener type's expected service interval?"

**Data to pull:** splice install date, fastener manufacturer's rated cycle/service life, last inspection reading.

## 10. Plant-measured throughput (scale-verified) is consistently below the sum-of-rated-capacity assumption, and attention has focused on the highest-amperage conveyor

**Usually means:** the wrong conveyor is being investigated — capacity, not amperage, identifies the actual constraint in a multi-conveyor line.

**First question:** "What is each conveyor's actual delivered tph computed from measured speed, not which one is drawing the most current?"

**Data to pull:** measured belt speed and computed tph for every conveyor in the series, not just the one under suspicion.

## 11. A conveyor is repeatedly restarted or jogged to clear a jam without confirming lockout status first

**Usually means:** isolation discipline has eroded under time pressure — a conveyor that restarts unexpectedly during manual clearing is a documented amputation mechanism, not a rare edge case.

**First question:** "Was this conveyor locked out before anyone reached into the jam, every single time, not just usually?"

**Data to pull:** LOTO log entries against jam-clearing incident reports for that station over the last quarter.
