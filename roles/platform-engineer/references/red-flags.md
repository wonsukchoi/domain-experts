### Engineers are building custom, unsupported infrastructure solutions instead of using the established golden path
- **Usually means:** The golden path likely has a real coverage gap for their specific use case, not that they need better documentation or a stronger mandate to use it.
- **First question:** What specific use case are these teams building for, and does the golden path template actually support it?
- **Data to pull:** Breakdown of non-golden-path deployments by use case/reason, golden path's documented supported scenarios.

### Platform adoption is measured only by whether a feature shipped, not by actual usage data
- **Usually means:** The platform team may be assuming success based on technical completeness without checking whether engineering teams are actually using it.
- **First question:** What percentage of eligible workflows are actually using this platform feature, measured directly, not assumed?
- **Data to pull:** Usage/adoption metrics for the platform feature since launch.

### Low platform adoption is being addressed with a stronger mandate or more documentation
- **Usually means:** This treats adoption as an enforcement/communication problem when it's more often a product coverage gap that needs to be fixed in the platform itself.
- **First question:** Has a root-cause breakdown been done on why non-adopters aren't using the platform, distinguishing coverage gaps from genuine edge cases?
- **Data to pull:** Survey or ticket data on non-adopters' specific reasons for bypassing the platform.

### A self-service abstraction has no documented escape hatch for edge cases
- **Usually means:** Teams with legitimate needs the abstraction doesn't cover are likely to be forced entirely outside the platform, rather than using a lighter-weight supported alternative.
- **First question:** Is there a documented, supported path for use cases that don't fit the standard abstraction, or are those teams left with no platform-supported option at all?
- **Data to pull:** Current escape hatch documentation (or its absence), volume of fully-custom (non-platform) deployments.

### Infrastructure changes have been made manually (via console/CLI) outside the IaC pipeline
- **Usually means:** This creates drift between actual infrastructure state and what's declared in code, which can cause an unexpected revert or a failed apply the next time the IaC pipeline runs.
- **First question:** Has drift detection been run recently, and does it show any divergence between declared and actual infrastructure state?
- **Data to pull:** Most recent drift detection report, log of any manual infrastructure changes.

### A platform-level change was rolled out to all tenants simultaneously
- **Usually means:** Given the shared blast radius of a multi-tenant platform, a bug or misconfiguration in this change could affect every dependent team at once, with no canary stage to catch it first.
- **First question:** Was this change validated on a canary tenant or namespace before the full rollout?
- **Data to pull:** Rollout plan/process used for this change.

### Tenant isolation (resource quotas, network policies) isn't enforced on a shared platform
- **Usually means:** One tenant's misbehavior (a resource spike, a misconfigured network rule) could affect other tenants sharing the same platform.
- **First question:** Are resource quotas and network isolation policies actively enforced per tenant, or is isolation assumed without explicit configuration?
- **Data to pull:** Current tenant isolation configuration, any past incidents where one tenant affected another.

### A golden path's adoption breakdown treats every non-adopter as a one-off edge case
- **Usually means:** A pattern across non-adopters (e.g., many needing the same unsupported feature) may indicate a systemic coverage gap rather than scattered individual exceptions.
- **First question:** Do non-adopters cluster around a common, specific unmet need, or are they genuinely diverse one-off cases?
- **Data to pull:** Categorized breakdown of non-adopter reasons, checking for concentration versus true dispersion.
