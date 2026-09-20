---
name: integration-diagnosis
description: Verify user-reported integrations against actual MCP, CLI, and config without recording secrets or switching accounts. Use when diagnosing GitHub, Gmail, plugins, Hostinger, n8n, Zoom, or routing failures.
disable-model-invocation: true
---

# Integration diagnosis

Treat the inventory as user-reported until verified.

For each connection record: purpose, identity, scope, permissions, environment, dependencies, status. No secrets.

Do not `gh auth switch`. Do not authenticate Gmail or Zoom unless the user asked to connect them now.

Overlapping personal and plugin connections are documented, not removed.

Status vocabulary: verified, untested, awaiting access, awaiting a decision, unsupported, intentionally disabled.
