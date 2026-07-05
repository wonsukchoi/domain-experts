# Security Policy

## Supported versions

Only the latest version published to npm ([`domain-experts`](https://www.npmjs.com/package/domain-experts)) and the current `main` branch receive security fixes. Older npm versions are snapshots and are not patched — upgrade instead.

| Version | Supported |
| ------- | --------- |
| Latest npm release | ✅ |
| `main` | ✅ |
| Older releases | ❌ |

## Reporting a vulnerability

**Do not open a public issue for security reports.**

Report privately via [GitHub Security Advisories](https://github.com/wonsukchoi/domain-experts/security/advisories/new) ("Report a vulnerability" on the repo's Security tab). If that isn't available to you, email the maintainer at wonsukchoi97@gmail.com with `[SECURITY] domain-experts` in the subject.

Please include:

- What the issue is and where (file path, CLI command, or role slug)
- Steps to reproduce or a proof of concept
- Impact as you understand it

You can expect an acknowledgment within 7 days and a fix or status update within 30 days. Credit is given in the release notes unless you ask otherwise.

## Scope — what counts as a vulnerability here

This project ships markdown skill files that AI agents load as instructions, plus a small Node.js CLI. That makes the threat model unusual:

**In scope:**

- **Prompt injection in role content** — text in `roles/**` or `skills/**` crafted to make an agent that loads it exfiltrate data, execute unintended commands, ignore its harness instructions, or misrepresent itself. This is the highest-severity class for this repo.
- **Malicious or unsafe behavior in the CLI** (`bin/cli.js`) or scripts (`scripts/*.py`) — arbitrary code execution, path traversal, command injection via role names or search input.
- **Supply-chain issues** — compromised or typosquatted dependencies, install scripts, or a published npm tarball that doesn't match the repo.
- **Secrets committed to the repo** — tokens, keys, or credentials in any tracked file or git history.

**Out of scope:**

- Wrong, outdated, or low-quality professional content in a role (open a regular issue or PR — see [CONTRIBUTING.md](./CONTRIBUTING.md))
- Vulnerabilities in the AI agent or harness that loads these skills
- Issues requiring a compromised maintainer account or machine

## For contributors

- Role content is executed as agent instructions. Never include text that directs an agent to run commands, fetch URLs, or handle credentials outside the role's stated domain. Reviewers treat instruction-like content in unexpected places as a red flag.
- Never commit tokens, API keys, or credentials — including in worked examples. Use obviously fake placeholder values.
- The CLI must not `eval`, shell out with user input, or read files outside the repo tree.

## npm publishing

Releases are published manually by the maintainer with 2FA enabled on the npm account. There is no automated publish pipeline, so a green CI run never implies a release was made.
