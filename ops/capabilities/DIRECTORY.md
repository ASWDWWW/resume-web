# AI capability directory

Every executable entry has a stable name, purpose, invocation, inputs, outputs, owner, dependencies, permissions, and verification. Markdown under `ops/` is documentation only.

Owner for all entries unless noted: Zakiy Manigo.  
Verification date: 17 September 2026.

## Prompts

| Name | Purpose | Invoke | In | Out | Deps | Perms | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prompt-library | Everyday full prompts + short examples | Read `ops/prompts/LIBRARY.md` and paste | Task | Draft/run | None | Read | **verified** file exists |

## Skills (`.cursor/skills/<name>/SKILL.md`)

| Name | Purpose | Invoke | In | Out | Deps | Perms | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| founder-pivot | Redirect OS after strategy change | `/founder-pivot` or mention skill | New direction | Pivot record | ops templates | Write ops | **verified** path |
| ticket-completion | Finish a scoped ticket | `/complete-ticket` | Ticket | Handoff | GitHub routing | Write code | **verified** path |
| communications | Draft messages | `/draft-communication` | Audience | Draft | Gmail/Zoom optional | Draft only | **verified** path |
| finance-stripe | Money files + Stripe caution | `/finance-review` | Question | Sourced notes | Stripe unsupported | Read/write finance md | **verified** path |
| integration-diagnosis | Verify connectors | `/diagnose-integration` | Name | Status table | MCP/CLI | Read | **verified** path |
| workspace-repair | Rebuild native OS files | `/repair-workspace` | Symptom | Restored files | Node | Write `.cursor` | **verified** path |
| engineering-ops | Eng lifecycle | mention skill | Ticket | Change + verify | Product repo | Write in-scope | **verified** path |
| reviewable-learning | Persist corrections scoped | mention skill | Correction | Rule/note | User agreement | Write rule | **verified** path |

Skills use `disable-model-invocation: true` so they are explicit, not silent global memory.

## Subagents (`.cursor/agents/*.md`)

| Name | Purpose | Invoke | In | Out | Deps | Perms | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| independent-reviewer | Second-pass review | `/independent-reviewer` or Task | Diff | Findings | None | readonly | **verified** path |
| verifier | Run checks | Task | Claimed work | Pass/fail | Node | write (run cmds) | **verified** path |
| security-privacy | Secrets/PII/payments | Task | Change set | Findings | None | readonly | **verified** path |
| product-engineering | Scoped implementation | Task | Ticket | Patch | Routing | write | **verified** path |
| business-ops | Ops documents | Task | Brief | Docs | ops/ | write ops | **verified** path |
| communications-drafter | Message drafts | Task | Brief | Draft | templates | write drafts | **verified** path |

No `tools:` field (not supported on Cursor subagents).

## Rules (`.cursor/rules/*.mdc`)

| Name | Purpose | Invoke | Status |
| --- | --- | --- | --- |
| 00-operating-charter | Inspect, preserve, implement, report | alwaysApply | **verified** |
| account-routing | No silent account switch | alwaysApply | **verified** |
| authorization-boundaries | Draft vs send, test vs live | alwaysApply | **verified** |
| context-isolation | Stale/untrusted/one-off | alwaysApply | **verified** |
| preserve-existing-work | Career/content/resume unfinished set | alwaysApply | **verified** |

## Commands (`.cursor/commands/*.md`)

Slash name = filename. These are registered command files, not essays.

`start-project`, `repair-workspace`, `complete-ticket`, `follow-up`, `debug-issue`, `review-changes`, `release`, `handoff`, `founder-pivot`, `business-analysis`, `marketing-campaign`, `finance-review`, `legal-prep`, `investor-update`, `draft-communication`, `diagnose-integration`, `control-center`.

Status: **verified** files in native location. Slash palette appearance **untested** in the UI this session.

## Hooks (`.cursor/hooks.json`)

| Name | Trigger | Actions | Limits | Inputs | Outputs | Retry/timeout | Dupes | Log/redact | Escalation | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shell-guard | beforeShellExecution | deny git config and force-push main; ask on gh auth and firebase deploy / stripe live | no other blocks | command JSON | permission | timeout 10s; fail open | log only | `.cursor/hooks/logs/` redacted | user confirm | **verified** script; live agent event **untested** |
| mcp-guard | beforeMCPExecution | ask on send/deploy/delete-like MCP | fail open | tool JSON | permission | 10s | log server+tool | redacted | user confirm | **verified** script; MCP event **untested** (Gmail/Zoom unauth) |
| secret-prompt | beforeSubmitPrompt | block pasted live keys | only obvious secret patterns | prompt | continue bool | 10s | n/a | log length only | user removes secret | **verified** script |
| restricted-read | beforeReadFile | deny `.env`, pem, credentials json | not folder-based | path | permission | 10s | n/a | path logged | n/a | **verified** script |
| audit-edit | afterFileEdit | log path | no mutation | path | none | 10s | append log | redacted | n/a | **verified** script |

Hooks do not spawn agents (prevents recursion). They do not retry external APIs.

## Workflows

See `ops/workflows/COORDINATION.md` and domain workflow files. Status: **verified** as documents. Execution is via commands.

## Templates

`ops/templates/*` — briefs, tickets, decisions, reports, handoffs, pivots, communication drafts, incidents, vendor assessments, investor updates. Status: **verified** files.

## Integrations

`ops/integrations/INVENTORY.md` and `ROUTING.md`.

## Automations

`ops/automations/CATALOG.md`. n8n **unsupported**. Cursor hooks **verified** files.
