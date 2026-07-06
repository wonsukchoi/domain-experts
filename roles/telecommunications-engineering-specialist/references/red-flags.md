### Cabling run exceeds 55m and is specified as Category 6 for a 10GbE-capable environment
- **Usually means:** original spec was written against a 1GbE requirement and never revisited for the next refresh cycle; second likeliest is a cost-driven downgrade made without documenting the future re-cable tradeoff.
- **First question:** what speed does this run need to support at the end of the equipment's expected service life, not just today?
- **Data to pull:** cable category/length schedule from the as-built cabling documentation, plus the hardware refresh roadmap.

### Fiber link within its "max distance" spec but experiencing intermittent errors
- **Usually means:** the actual installed connector/splice count exceeds what the max-distance figure assumed; second likeliest is a degraded connector (dirty/scratched end-face) adding unaccounted loss.
- **First question:** what's the actual measured loss on this link via OTDR or power meter, versus the calculated budget?
- **Data to pull:** OTDR trace, as-built connector/splice count for the path, transceiver power budget spec sheet.

### Carrier circuit order placed after cabling/hardware procurement has already started
- **Usually means:** project sequencing treated the circuit as a late-stage task instead of the longest-lead dependency; second likeliest is nobody obtained a firm quoted lead time before scheduling other milestones.
- **First question:** what is the carrier's currently quoted turn-up date, and does the go-live date assume it?
- **Data to pull:** carrier order confirmation with quoted turn-up date, project milestone schedule.

### PBX/VoIP trunk group sized as a fixed ratio to extension count (e.g., 1:8) with no traffic data behind it
- **Usually means:** no busy-hour call data was pulled from an existing comparable system; second likeliest is the ratio was copied from a prior, differently-used site.
- **First question:** what does the busy-hour concurrent-call count actually look like on a comparable existing system?
- **Data to pull:** call detail records (CDR) from a comparable site for the busy hour, or a documented traffic study.

### Cable certification report shows "PASS" with margin under 1 dB on insertion loss or under 2 dB on NEXT
- **Usually means:** the run is at or near its physical limit (excess length, marginal termination, or connector quality issue) and is the run most likely to fail after aging, added patch cords, or temperature swings.
- **First question:** is this run's margin consistent with the rest of the cable plant, or an outlier?
- **Data to pull:** full certification report with per-parameter margin, not just the pass/fail summary line.

### Wireless AP count was derived from square footage alone (e.g., "1 AP per 1,500 sq ft") with no RF survey
- **Usually means:** design skipped the predictive RF survey step, likely due to schedule pressure; second likeliest is the space has unusual construction materials (reinforced concrete, metal studs) not accounted for in a generic ratio.
- **First question:** has a predictive RF survey or post-install walk test been run for this specific floor plan and construction type?
- **Data to pull:** RF survey heatmap or walk-test signal-strength measurements per area.

### PRI/T1 span utilization consistently above 90% of provisioned channels during the measured busy hour
- **Usually means:** growth exceeded the headroom assumption used at design time; second likeliest is a new call pattern (e.g., a new call center function) added after the original sizing was done.
- **First question:** has actual busy-hour concurrent-call count been re-measured since original sizing, and how does it compare to the original 20%-headroom assumption?
- **Data to pull:** current PRI/trunk utilization report, original traffic-sizing worksheet.

### Structured cabling pathway (conduit/riser) is at or above 80% fill without a documented expansion plan
- **Usually means:** original pathway sizing didn't account for a known future cabling phase; second likeliest is ad-hoc cabling added outside the documented project scope.
- **First question:** what future cabling phases are known, and does the current pathway have capacity for them per code fill limits?
- **Data to pull:** conduit/riser fill calculation against code maximum (commonly 40% fill for conduit per NEC guidance), pathway as-built drawing.

### Demarc/smart jack location and the carrier's circuit ID don't match the as-built documentation
- **Usually means:** a carrier-side change (circuit re-route, equipment swap) wasn't reflected back into internal documentation; second likeliest is a documentation error at initial turn-up.
- **First question:** when was this documentation last verified against the carrier's current circuit records?
- **Data to pull:** current carrier circuit ID and demarc location from the carrier's own records, compared against internal as-built.
