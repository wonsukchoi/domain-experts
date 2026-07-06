### Hard real-time
A timing requirement where missing the deadline constitutes a system failure, not just a degraded experience (e.g., a motor control loop, a safety interlock).
**In use:** "This control loop is hard real-time — a missed deadline here isn't a slow response, it's a system failure."
**Common misuse:** Treating all timing requirements as equally flexible, applying soft-real-time tolerances to a deadline where a miss is actually unacceptable.

### Soft real-time
A timing requirement where missing the deadline degrades quality or user experience but doesn't constitute an outright failure.
**In use:** "The display refresh is soft real-time — an occasional missed frame is tolerable."
**Common misuse:** Confusing soft real-time tolerances with hard real-time requirements, underestimating how strictly a hard deadline actually needs to be met.

### Worst-case execution time (WCET)
The maximum possible time a piece of code could take to execute under any input or system state, used to verify hard real-time correctness — as opposed to average or typical-case timing.
**In use:** "WCET analysis shows this function could take up to 2.3ms in the worst case, still within our 5ms deadline."
**Common misuse:** Validating a hard real-time deadline using average or typical-case timing measurements instead of bounding the actual worst case.

### Heap fragmentation
The gradual breakup of available memory into small, non-contiguous free blocks over repeated allocation/deallocation cycles, which can eventually cause an allocation to fail even when total free memory appears sufficient.
**In use:** "After six months of uptime, heap fragmentation caused an allocation failure that never showed up in our two-day test runs."
**Common misuse:** Testing dynamic memory allocation only over short durations, missing fragmentation effects that only accumulate over extended runtime.

### Static/pool allocation
Memory allocation strategies using fixed, pre-determined memory (static allocation) or a fixed-size pool of pre-allocated blocks (pool allocation), avoiding the unpredictability of dynamic heap allocation over long uptimes.
**In use:** "We switched to a fixed memory pool for message buffers to avoid heap fragmentation risk on this always-on device."
**Common misuse:** Defaulting to dynamic malloc/free in constrained or long-uptime firmware without considering static or pool allocation as a more predictable alternative.

### Interrupt service routine (ISR)
A function that executes in response to a hardware interrupt, which should be kept as short as possible to avoid delaying other interrupts.
**In use:** "The ISR just captures the ADC reading and sets a flag — the actual processing happens in the main loop."
**Common misuse:** Performing significant processing directly inside an ISR, delaying other interrupts and risking missed interrupts or priority inversion.

### Priority inversion
A situation where a higher-priority task is effectively blocked by a lower-priority one, often because a long-running interrupt or task holds a resource or blocks execution that the higher-priority work needs.
**In use:** "The long-running ISR was causing priority inversion, delaying a higher-priority interrupt that needed to run."
**Common misuse:** Assuming interrupt priority levels alone guarantee correct execution order, without accounting for how a long-running lower-priority ISR can still delay higher-priority work.

### Torn read/write
A bug where a multi-byte variable is read or written in a non-atomic way, such that a concurrent update (from an ISR, for example) causes part of the old value and part of the new value to be combined into a single, often nonsensical, result.
**In use:** "The torn read on this 32-bit variable produced a value nowhere near either the old or new reading."
**Common misuse:** Assuming a variable's read/write is atomic without checking whether it fits within the microcontroller's native word size, especially for multi-byte values shared between an ISR and the main loop.

### Interrupt masking / atomic access
Techniques for protecting a shared variable from concurrent access issues, such as briefly disabling a specific interrupt during a critical read/write, or using hardware-supported atomic operations.
**In use:** "We added interrupt masking around the shared variable's read to guarantee it's never read in a torn state."
**Common misuse:** Leaving a shared ISR/main-loop variable unprotected, assuming a simple read or write is inherently safe without any explicit synchronization mechanism.

### Datasheet (hardware register timing)
The manufacturer's official technical specification for a hardware component, documenting exact required timing, sequencing, and electrical characteristics for correct operation.
**In use:** "The datasheet specifies a minimum 10-cycle delay between these two register writes, which our code wasn't respecting."
**Common misuse:** Relying on observed behavior from bench testing instead of verifying against the datasheet's actual specified timing, which can fail intermittently under real-world temperature, voltage, or hardware batch variance.
