# Mobile Engineer — Playbook

## Sync conflict scenario table (filled example)

| Field | Phone edit (offline) | Web edit (online) | Naive whole-record last-write-wins result | Field-level merge result |
|---|---|---|---|---|
| Title | Not touched | "Draft proposal" → "Draft proposal v2" @ 2:00 PM | **Lost** (reverted to "Draft proposal") | **Preserved** ("Draft proposal v2") |
| Due date | March 20 → March 25 @ 1:55 PM | Not touched | March 25 (syncs at 2:10 PM, whole record wins) | **Preserved** (March 25) |

**Use:** Always check whether a sync design distinguishes fields edited independently (safe to merge) from the same field edited on both sides (a true conflict needing explicit resolution) — whole-record overwrite treats every sync as the latter, silently discarding the former.

## Conflict classification decision table

| Scenario | Classification | Resolution |
|---|---|---|
| Different fields edited by different clients | Not a true conflict | Field-level merge — preserve both edits |
| Same field edited by both clients to the same value | Not a true conflict | Merge trivially (values match) |
| Same field edited by both clients to different values | **True conflict** | Apply a defined per-field last-write-wins rule, or prompt the user to choose |

## App store release readiness checklist

1. Review current App Store Review Guidelines / Google Play Developer Policy for any new feature in this release (payments, permissions, data collection, third-party SDKs).
2. Confirm the build has been tested on the review team's likely test conditions (fresh install, no test/demo account bypass).
3. Build in buffer time for review turnaround (historically variable, plan for the higher end of past experience) and possible rejection-and-resubmission cycle.
4. Confirm app metadata (screenshots, description, privacy details) is complete and accurate for this release.

## Background work platform-limit checklist

1. Identify what background work this feature requires (sync, location tracking, notifications).
2. Confirm it's implemented using the platform's documented background task API (not a naive continuous loop or timer).
3. Test under real battery-optimization conditions: iOS with background app refresh disabled, Android with Doze mode / battery optimization enabled for the app.
4. Confirm the feature degrades gracefully (delayed sync, batched updates) rather than silently failing when background execution is restricted.

## Lifecycle transition test checklist (per screen/feature)

1. Background the app mid-task (e.g., mid-form-entry) and confirm state is preserved on return.
2. Trigger a configuration change (rotate the device) mid-task and confirm state survives.
3. Simulate process death (via developer tools) while backgrounded and confirm state restoration on relaunch.
4. Confirm these tests are run as part of the standard test suite, not just a one-time manual check.

## Device/OS test matrix (illustrative structure)

| Device tier | OS version range | Priority |
|---|---|---|
| Current-generation flagship | Latest OS | High (primary dev/test device) |
| Mid-range, 2-3 years old | Latest minus 1-2 major versions | High (represents bulk of real user base) |
| Low-end / budget | Oldest OS version still supported | Medium-High (most likely to surface performance/crash issues) |

**Use:** Prioritize testing on the mid-range and low-end tiers specifically — the flagship test device is the least representative of where real-world crashes and performance issues concentrate.

## Sync design findings memo — filled example

> **Sync Conflict Resolution Review — Task Management App**
> Issue: Whole-record last-write-wins sync silently discarded a web-client title edit when a later-syncing offline phone edit (to an unrelated field, due_date) overwrote the entire record.
> **Fix: Switched to field-level merge, tracking per-field modification timestamps** so edits to different fields from different clients merge correctly instead of one overwriting the other.
> **Remaining gap: True same-field conflicts (e.g., both clients editing due_date differently) still need an explicit resolution rule or user-facing conflict prompt — field-level merge alone doesn't resolve genuine same-field conflicts.**
