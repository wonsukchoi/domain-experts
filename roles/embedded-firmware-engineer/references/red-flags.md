### A hard real-time deadline is validated using typical or average-case timing measurements
- **Usually means:** The actual failure mode — a rare worst-case execution path missing the deadline — hasn't been checked, since typical-case timing doesn't bound the worst case.
- **First question:** Has worst-case execution time been analyzed or bounded for this code path, not just measured under typical conditions?
- **Data to pull:** WCET analysis (or its absence), typical vs. worst-case timing measurements for this code path.

### Firmware for a long-uptime device uses dynamic memory allocation (malloc/free) in its main operational loop
- **Usually means:** Heap fragmentation could accumulate invisibly over extended runtime and cause an allocation failure at an unpredictable point, long after initial testing concluded the code worked fine.
- **First question:** Has this firmware been soak-tested for extended uptime (weeks/months) to check for fragmentation-driven failures, or only tested over short runs?
- **Data to pull:** Memory allocation pattern in the main loop, any long-duration soak test results.

### An interrupt service routine performs significant processing rather than just capturing data and returning
- **Usually means:** Other interrupts (same or lower priority) may be getting delayed or missed while this ISR runs, risking a real-time deadline violation elsewhere in the system.
- **First question:** Can this ISR's work be reduced to capturing data/setting a flag, with actual processing deferred to the main loop or a task context?
- **Data to pull:** ISR execution time, interrupt priority configuration, whether any other interrupts have been observed to be delayed or missed.

### A variable is read/written by both an interrupt service routine and the main loop with no explicit synchronization
- **Usually means:** A torn read is possible if the variable's read/write isn't atomic on this microcontroller, potentially producing a wildly incorrect value, not just a slightly stale one.
- **First question:** Is this variable's access protected by interrupt masking, an atomic operation, or another synchronization technique, or is it accessed directly from both contexts?
- **Data to pull:** Variable's size relative to the microcontroller's native word size, current synchronization (or its absence) around its access.

### A hardware register interaction works reliably on the bench but hasn't been checked against the datasheet's specified timing
- **Usually means:** The behavior may depend on undocumented or coincidental timing that isn't guaranteed across temperature, voltage, or hardware batch variance, risking intermittent field failures.
- **First question:** Does the datasheet explicitly specify and guarantee the timing/sequencing this code relies on, or is the current behavior based on what was observed to work?
- **Data to pull:** Relevant datasheet timing specification, current code's actual timing relative to that spec.

### Firmware has only been tested at room temperature over a short duration
- **Usually means:** Temperature-dependent, voltage-dependent, or long-uptime-dependent bugs (memory fragmentation, marginal timing) may not have been exercised at all.
- **First question:** Has this firmware been tested across its specified temperature and voltage range, and over an extended uptime period?
- **Data to pull:** Test plan and conditions used, specified operating temperature/voltage range for the device.

### A shared-variable bug is dismissed as a one-off, hard-to-reproduce glitch
- **Usually means:** This is a common signature of an ISR/main-loop race condition, which is often intermittent and timing-dependent rather than consistently reproducible.
- **First question:** Is there a variable shared between an ISR and the main loop in the code path where this glitch occurred, and is it synchronized?
- **Data to pull:** Code path involved in the reported glitch, shared-variable access patterns in that path.

### A safety-critical or hard real-time function has no worst-case execution time documented anywhere
- **Usually means:** Without a documented WCET, there's no basis for confirming the function actually meets its real-time deadline under all conditions.
- **First question:** Has this function's worst-case execution time been calculated or bounded, and is it documented alongside the deadline it needs to meet?
- **Data to pull:** Function's documented (or undocumented) WCET, the specific deadline it's required to meet.
