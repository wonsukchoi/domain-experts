# Platform/Infrastructure Engineer — Playbook

## Golden path adoption root-cause breakdown (filled example)

| Non-adopter category | Share of non-adopting 65% | Classification |
|---|---|---|
| Event-driven/consumer services (unsupported use case) | 40% | Coverage gap — fixable |
| Non-PostgreSQL database needs (unsupported) | 15% | Coverage gap — fixable |
| Genuine one-off edge cases | 10% | True edge case — needs escape hatch, not full template support |
| **Total coverage gap (fixable)** | **55 of 65 points** | |

**Use:** Always break down non-adoption by specific reason before concluding the issue is enforcement or communication — here, 85% of the non-adopting share (55 of 65 points) reflects a fixable product gap, not scattered one-off exceptions.

## Adoption before/after fix (filled example)

| Metric | Before fix | After fix (3 months later) |
|---|---|---|
| Golden path adoption rate | 35% | **78%** |
| Enforcement/mandate added? | No | No |
| **Conclusion** | | Adoption increase driven entirely by expanded template coverage, confirming the original gap was a coverage problem, not a communication/enforcement problem |

## Self-service abstraction level checklist

1. List the common tasks this abstraction needs to support (e.g., deploy a service, provision a database).
2. Confirm the abstraction hides genuine underlying complexity for these common cases (engineers shouldn't need deep infra knowledge for the standard path).
3. Confirm an explicit, documented escape hatch exists for cases the abstraction doesn't cover — not silence or a fully unsupported fallback.
4. Periodically check usage of the escape hatch — high escape-hatch usage for a specific pattern signals it should become a first-class supported case.

## Drift detection and IaC enforcement checklist

1. Confirm all infrastructure changes are required to go through the IaC pipeline (via policy, tooling, or access restriction).
2. Run drift detection on a regular schedule (daily/weekly), comparing actual infrastructure state to declared IaC state.
3. Investigate and remediate any detected drift immediately — treat every instance as a process gap to close, not a one-off exception.
4. Track drift incidents over time to identify if a specific team or system is a recurring source, indicating a process or access-control gap there specifically.

## Staged rollout checklist (multi-tenant platform change)

1. Identify a representative canary tenant/namespace for the initial rollout.
2. Deploy the change to the canary only, and monitor for a defined observation period (e.g., 24-48 hours).
3. Confirm no regressions or issues before expanding to a broader subset, then to all tenants.
4. Confirm tenant isolation (resource quotas, network policies) limits the blast radius even if an issue does occur during rollout.

## Platform adoption findings memo — filled example

> **Golden Path Adoption Review — Service Deployment Template**
> Initial adoption: 35% of new services. Root-cause breakdown of non-adopters: 40% event-driven services (unsupported use case), 15% non-PostgreSQL database needs (unsupported), 10% genuine edge cases.
> **Finding: 55 of 65 non-adopting percentage points reflect a fixable coverage gap, not enforcement failure.**
> **Fix: Expanded template to support event-driven services and multiple database types; added a documented escape hatch for genuine edge cases.**
> **Result: Adoption rose to 78% with no additional mandate — confirming the fix addressed a real product gap.**
