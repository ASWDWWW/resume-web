# Construction phases

Workspace construction is not authorization to operate businesses externally.

Each phase maps to the 18-point brief. Native Cursor files live under `.cursor/` and `AGENTS.md`. Markdown under `ops/` is documentation unless a matching native file exists.

| Phase | Brief item | Authoritative files | Status 20 Sep 2026 |
| --- | --- | --- | --- |
| 1 | Inspect, preserve, implement, report | `AGENTS.md`, `.cursor/rules/00-operating-charter.mdc` | **verified** |
| 2 | Project / business intake | `ops/profile/PROJECT-PROFILE.md` | **verified** (facts vs assumptions) |
| 3 | Integration inventory + routing | `ops/integrations/INVENTORY.md`, `ROUTING.md` | **verified** this session (see inventory) |
| 4 | Architecture / sources of truth | `ops/architecture/` | **verified** |
| 5 | Control center | `ops/CONTROL-CENTER.md` | **verified** document view. Custom dashboard **intentionally later** |
| 6 | AI capability directory | `ops/capabilities/DIRECTORY.md`, `.cursor/*` | **verified** native paths |
| 7 | Agent activation | `ops/workflows/COORDINATION.md` | **verified** document |
| 8 | Product / engineering | `ops/product-engineering/WORKFLOWS.md` | **verified** document. Other product code not in this repo |
| 9 | Strategy / team | `ops/business-operations/strategy.md`, `team.md` | **verified** document. Numeric goals **awaiting a decision** |
| 10 | Marketing / sales / CS | `ops/business-operations/marketing.md`, `sales-cs.md` | **verified** document |
| 11 | Finance / payments | `ops/business-operations/finance.md` + actuals/estimates/forecasts | **verified** split. Books **empty** except Hostinger API prices |
| 12 | Legal / privacy / compliance | `ops/business-operations/legal.md` | **verified** as prep, not approval |
| 13 | Fundraising | `ops/business-operations/fundraising.md` | **verified** document. Targets **unresolved** |
| 14 | Communications / meetings | `ops/business-operations/communications.md` | Drafts **verified**. Send **intentionally disabled** until identity + authorization |
| 15 | Context isolation / learning | `.cursor/rules/context-isolation.mdc`, skill `reviewable-learning` | **verified** |
| 16 | Hooks / automation reliability | `.cursor/hooks.json`, `ops/automations/` | Hooks **verified** via harness. n8n catalog **verified** list |
| 17 | Prompt / command library | `.cursor/commands/`, `ops/prompts/LIBRARY.md` | Commands **verified** files. Slash palette UI **untested** |
| 18 | Acceptance + report | this file, `CONSTRUCTION-REPORT.md`, `OPERATING-GUIDE.md` | **verified** this session |

Do not count an `ops/` essay as a registered command or a functioning hook.
