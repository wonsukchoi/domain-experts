# Embedded/Firmware Engineer — Playbook

## Torn read demonstration (filled example)

| Component | Value |
|---|---|
| True old reading (raw ADC units) | 65,000 (0x0000FDE8) |
| True new reading (ISR update) | 65,600 (0x00010040) |
| ISR write order | Low word first (0x0040), then high word (0x0001) |
| Main loop read timing | High word read before ISR update (0x0000), low word read after (0x0040) |
| **Torn read result** | 0x00000040 = **64 (decimal)** |
| **Deviation from true values** | Nowhere near either 65,000 or 65,600 — a wildly incorrect reading |

**Use:** This demonstrates why torn reads are dangerous beyond "slightly stale data" — the resulting value can be arbitrarily wrong, potentially triggering an incorrect control decision (like disabling cooling during an actual overheat event) rather than just showing an outdated but plausible number.

## ISR/main-loop synchronization checklist

1. Identify every variable read or written by both an ISR and the main loop (or another task context).
2. Check whether each variable's size exceeds the microcontroller's native atomic word size.
3. If so, add explicit synchronization: disable the relevant interrupt briefly during the critical read/write, use a hardware atomic operation, or implement a sequence-counter technique.
4. Verify the fix with a targeted stress test that maximizes the chance of the race condition triggering (e.g., artificially increasing ISR frequency during test).

## WCET analysis checklist (hard real-time paths)

1. Identify every code path that must complete within a hard real-time deadline.
2. Trace the worst-case branch/loop-iteration count for each path, not the typical case.
3. Sum the worst-case instruction/cycle count for the full path, including any interrupt latency that could occur during execution.
4. Confirm the calculated worst-case time is comfortably within the required deadline, with margin for variance.

## Memory allocation strategy decision table

| Context | Recommended approach |
|---|---|
| Long-uptime device (months/years without reboot) | Static or fixed-pool allocation — avoids fragmentation-driven failure |
| Safety-critical system | Static or fixed-pool allocation — predictable, verifiable memory behavior |
| Short-lived or frequently-rebooted device | Dynamic allocation may be acceptable if fragmentation risk is genuinely bounded by uptime |

**Use:** Default to static/pool allocation unless there's a specific, checked reason dynamic allocation is safe for this device's actual uptime pattern.

## Hardware register verification checklist

1. Identify every register write/read sequence this code relies on.
2. Pull the datasheet's exact specified timing and sequencing requirements for each operation.
3. Confirm the code's actual timing (delays, ordering) matches the datasheet specification, not just what's been observed to work on the current bench setup.
4. Test across the device's specified temperature and voltage range to confirm timing margins hold under real-world variance, not just typical bench conditions.

## Firmware findings memo — filled example

> **Firmware Bug Finding — Temperature Sensor Shared Variable Race**
> Bug: The 32-bit temperature reading shared between the timer ISR and the main loop is not read/written atomically on this MCU. A torn read during an ISR update can produce a wildly incorrect value (demonstrated: true values 65,000 → 65,600, torn read produced 64).
> Consequence: A torn reading near zero could cause the fan-control logic to shut off cooling at the exact moment a real overheat condition (65,600) occurs.
> **Fix: Added interrupt masking around the shared variable's read/write in the main loop, ensuring the value is always read as fully consistent (either fully old or fully new).**
> **Recommendation: Audit all other ISR/main-loop shared variables in this codebase for the same unsynchronized access pattern.**
