# Automation catalog

Prevent recursive triggers, conflicting agents, silent account fallback, and repeated external actions.

## Cursor hooks (registered)

See `ops/capabilities/DIRECTORY.md` for the full field set.

| ID | Trigger | Eligible | Authorized actions | Limits | Inputs | Outputs | Retry | Timeout | Duplicate prevention | Log | Escalation | Disable | Recovery |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shell-guard | beforeShellExecution | all shell | deny git config & force-push main; ask gh auth / firebase deploy / stripe live | no sends | command | permission | none | 10s | none (gate only) | redacted jsonl | user | remove entry from hooks.json | fail open except deny rules |
| mcp-guard | beforeMCPExecution | all MCP | ask on mutating names | fail open | tool JSON | permission | none | 10s | none | redacted | user | hooks.json | fail open |
| secret-prompt | beforeSubmitPrompt | all prompts | block live secret paste | pattern-based | prompt | continue | none | 10s | n/a | length | user | hooks.json | fail open |
| restricted-read | beforeReadFile | secret-like paths | deny | not folders | path | permission | none | 10s | n/a | path | n/a | hooks.json | fail open |
| audit-edit | afterFileEdit | all edits | log | no side effects | path | none | none | 10s | append-only log | redacted | n/a | hooks.json | ignore |

Hooks must not call MCP or start subagents.

## n8n

Not connected. When added, register each workflow here with the same columns plus schedule, budget, and a disable switch. Until then, agents continue independently.

## Recurring agents

Intentionally disabled. Use slash commands. A permanent agent per function is not required.
