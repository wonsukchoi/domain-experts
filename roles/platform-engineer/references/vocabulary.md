### Golden path / paved road
The officially supported, opinionated default workflow a platform provides for a common task (deploying a service, provisioning a database), designed to be the easiest option available, not just the approved one.
**In use:** "The golden path for a new service is a single CLI command using our standard template."
**Common misuse:** Building a golden path and assuming it will be adopted because it's the "approved" way, without checking whether it's actually the easiest path for engineers' real use cases.

### Self-service abstraction
A platform-provided interface that lets engineering teams provision infrastructure or deploy services without needing deep expertise in the underlying systems.
**In use:** "The self-service abstraction lets teams request a database with one config file, without needing to understand the underlying Terraform."
**Common misuse:** Setting the abstraction level too low (still requiring deep infrastructure knowledge) or too high (hiding all control, with no escape hatch), either of which undermines adoption.

### Escape hatch
A supported, documented path for handling edge cases that a platform's standard self-service abstraction doesn't cover, avoiding forcing teams entirely outside the platform.
**In use:** "The escape hatch lets teams with non-standard database needs get a lightweight review instead of either fitting a mismatched template or going fully unsupported."
**Common misuse:** Omitting an escape hatch entirely, which forces teams with legitimate edge-case needs to build fully custom, unsupported solutions outside the platform.

### Platform as a product
The practice of treating an internal developer platform's engineering teams as customers, measuring success by adoption, satisfaction, and usage data rather than technical feature completeness alone.
**In use:** "We're treating this platform as a product — adoption rate and developer surveys are the real success metric, not just whether the feature works."
**Common misuse:** Evaluating a platform team's success purely by what shipped and whether it's technically correct, without checking whether it's actually being used.

### Infrastructure as code (IaC) drift
The divergence between an infrastructure's actual state and what's declared in its infrastructure-as-code definitions, typically caused by manual, out-of-band changes.
**In use:** "Drift detection caught a manually changed security group rule that wasn't reflected in our Terraform config."
**Common misuse:** Making infrastructure changes directly via console/CLI outside the IaC pipeline, allowing drift to accumulate invisibly until it causes an unexpected revert or failed apply.

### Drift detection
An automated process that compares actual infrastructure state against its declared IaC definition, flagging any divergence.
**In use:** "Drift detection runs nightly and alerts us to any out-of-band infrastructure changes."
**Common misuse:** Relying on IaC alone without running regular drift detection, missing manual changes until they cause a problem during the next deployment.

### Multi-tenancy (platform)
An architecture where a single shared platform serves multiple internal teams or services simultaneously, each acting as a "tenant" with resources and configuration isolated from the others.
**In use:** "This is a multi-tenant platform — a bug here could affect every team's services at once, so we need tenant isolation and staged rollouts."
**Common misuse:** Treating a shared platform change like a single-service deployment, missing that its blast radius spans every tenant depending on it.

### Canary rollout (platform)
A staged deployment strategy that applies a change to a small subset (a canary tenant or namespace) before rolling it out broadly, limiting the blast radius if something goes wrong.
**In use:** "We rolled this platform change out to one canary tenant first and monitored for 24 hours before expanding to everyone."
**Common misuse:** Deploying a platform-level change to all tenants simultaneously, skipping the canary stage that would catch a problem before it affects everyone.

### Tenant isolation
Configuration (resource quotas, network policies) ensuring one tenant on a shared platform can't consume excessive resources or interfere with another tenant's workloads.
**In use:** "Resource quotas prevent one team's runaway job from starving other tenants' workloads on the same cluster."
**Common misuse:** Assuming tenants are naturally isolated without explicit quota and network policy configuration, allowing one tenant's misbehavior to affect others.

### Developer experience (DX) metrics
Quantified measures of how effectively a platform serves its internal engineering customers — adoption rate, time-to-first-deploy, support ticket volume, and similar indicators.
**In use:** "Time-to-first-deploy dropped from 3 days to 20 minutes after the new template launched — that's the DX metric that actually matters."
**Common misuse:** Reporting platform success only through feature-completeness or launch announcements, without tracking concrete DX metrics that reveal whether the platform is actually working for its users.
