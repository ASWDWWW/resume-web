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

Instance listed 20 Sep 2026. Agents must not `execute_workflow` or `publish_workflow` unless the user names the workflow and authorizes it. Cursor hooks remain the only registered local automations.

| ID (name) | Trigger | Eligible | Authorized actions | Limits | Schedule / budget | Disable | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FG Weekly Social Drafts | claimed: Mondays 09:00 ET | FitGenius drafts | write calendar drafts | does not post | unknown | leave inactive | MCP-available, **inactive** |
| FG Review Draft Queues | manual | FitGenius drafts | review queues | does not post/send | none | leave inactive | MCP-available, **inactive** |
| FG Business Draft Pack | manual | FitGenius drafts | outreach/support macros | does not send | none | leave inactive | MCP-available, **inactive** |
| FG Bootstrap Tables | one-time | FitGenius tables | create tables | safe to re-run per description | none | leave inactive | MCP-available, **inactive** |
| Scheduled Instagram Posting (Single + Reel + Mixed Carousel + Optional Story) | unknown (MCP details blocked) | Instagram | posting (instance **active**) | not callable from Cursor MCP | unknown | disable in n8n UI | **active** on instance, MCP-unavailable |
| Older Instagram / Reddit / AI video workflows | unknown | various | posting / gen | not MCP-available | unknown | leave as found | inactive except the row above |

Failure handling: `FAILURE-HANDLING.md`. Do not retry sends from Cursor if n8n already posted.

## Recurring agents

Intentionally disabled. Use slash commands. A permanent agent per function is not required.
