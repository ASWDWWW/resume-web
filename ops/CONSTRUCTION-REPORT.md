# Construction report

Date: 17 September 2026  
Workspace: `ASWDWWW/resume-web`  
Scope completed: owner operating system (documents + native Cursor configuration)  
Not in scope: operating businesses externally (no deploys, no mail send, no account switch, no live payments)

Workspace construction is not authorization to operate the companies.

## Inspection (before changes)

Working:

- Static career site in `public/index.html` and Firebase hosting config for `zakiymanigo-career`
- Career evidence packets under `Career/`
- Git remote and `gh` login for `ASWDWWW`

Missing (no prior OS):

- No `AGENTS.md`, `.cursor/rules`, commands, skills, agents, or hooks

Conflicting / overlapping:

- Two GitHub logins on `gh` (`ASWDWWW` active, `FITD-fash` inactive)
- GitHub personal connection and GitHub plugin both bind to `ASWDWWW`
- User-reported `gmail-fashiobusiness` vs observed `zakiymanigo@gmail.com`
- User-reported Figma and Stripe plugins not present in this session’s MCP catalog

Outdated / unfinished (preserved, not modified):

- Untracked `Career/`, `Content/`, new resume and cover-letter folders
- Hundreds of indexed files deleted under `Resumes & Cover Letters/use/`
- `index-safety.html` at repo root (backup; hosting serves `public/`)

## Built

- `AGENTS.md` and five always-on rules
- 17 slash commands in `.cursor/commands/`
- 8 skills in `.cursor/skills/`
- 6 subagents in `.cursor/agents/`
- Registered hooks in `.cursor/hooks.json` with Node scripts
- `ops/` control center, profile, architecture, integrations, capabilities, workflows, templates, automations, prompts, restricted/owner policy, records
- `.gitignore` entries for hook logs and restricted records

## Tested (this session)

| Check | Result |
| --- | --- |
| Hook unit harness (11 cases: deny git config, deny force-push main, ask gh auth switch, ask send MCP, allow reads, block live `sk_live_`, deny `.env` read) | **verified** pass |
| `hooks.json` parses | **verified** |
| Native file counts (5 rules, 17 commands, 8 skills, 6 agents) | **verified** |
| `Career/` overview and `public/index.html` still present | **verified** |
| GitHub MCP identity `ASWDWWW` | **verified** |
| `gh` dual logins, ASWDWWW active | **verified** |
| Firebase env and 14-project list as `zakiymanigo@gmail.com` | **verified** |
| Hugging Face `zakiymanigo` | **verified** |
| Canva owned-design search | **verified** |
| LinkedIn profile read (extra connector) | **verified** |
| Chrome DevTools `list_pages` | **verified** present (`about:blank` only) |

## Untested

- Slash command palette in the Cursor UI
- Hooks firing inside a live agent turn (stdin tests only)
- Firebase deploy
- Canva export/generate
- Meta VR beyond a failed debug auth_status
- Discord
- Browser walkthrough of the career site (site files were not changed)
- Concurrent worktrees

## Awaiting access

- Gmail MCP (`needsAuth`) for `gmail-fashiobusiness`
- Zoom MCP (`needsAuth`)
- Private `FITD-fash` repository list (would require an explicit account switch, which was not done)
- Hostinger, IONOS, Magnific, n8n APIs

## Awaiting a decision

- Default Gmail identity
- Whether to authenticate Gmail/Zoom now
- Whether to install Figma and Stripe plugins
- Whether this OS should remain in a **public** repo
- Budgets, legal entities, fundraising target, product priority order
- Hugging Face token refresh (expiry observed 17 Sep 2026 20:28Z)

## Unsupported here

- Figma MCP
- Stripe MCP
- Hostinger, IONOS, Magnific, n8n connectors
- Custom metrics dashboard (intentionally later)

## Intentionally disabled / not run

- `gh auth switch`
- Gmail/Zoom `mcp_auth`
- Firebase deploy
- Force-push and git config (hook-denied)
- Recurring always-on department agents
- n8n

## Optional later

Custom dashboard, n8n catalog, Stripe test-mode workflows once a plugin exists, Figma handoff, moving OS to a private repo.

## How to operate

Read [OPERATING-GUIDE.md](OPERATING-GUIDE.md). Refresh [CONTROL-CENTER.md](CONTROL-CENTER.md) with `/control-center`.
