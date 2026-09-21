# Construction report

Date: 20 September 2026 (re-execution of the 18-point owner-OS brief)  
Original install: 17 September 2026  
Workspace: `ASWDWWW/resume-web`  
Scope: owner operating system (documents + native Cursor configuration)  
Not in scope: operating businesses externally (no deploys, no mail send, no account switch, no live payments, no Magnific generation, no n8n execute)

Workspace construction is not authorization to operate the companies.

Phases: [CONSTRUCTION-PHASES.md](CONSTRUCTION-PHASES.md).  
Evidence: [records/20260920-os-reverify.md](records/20260920-os-reverify.md).

## Inspection (this session, before further edits)

Working:

- Static career site in `public/index.html` and Firebase hosting config for `zakiymanigo-career`
- Career evidence packets under `Career/`
- Git remote and `gh` login for `ASWDWWW`
- Native OS already present: `AGENTS.md`, 5 rules, 17 commands, 8 skills, 6 agents, registered hooks
- `ops/` control center, profile, architecture, integrations, capabilities, workflows, templates, automations, prompts

Missing / stale before this pass:

- Construction report, operating guide, and several domain files still said Figma/Stripe/n8n/Magnific were unsupported
- Zoom bridge documented as authenticated; live call failed
- n8n workflows were not in the automation catalog
- No phase map for the 18-point brief

Conflicting / overlapping:

- Two GitHub logins on `gh` (`ASWDWWW` active, `FITD-fash` inactive)
- GitHub personal connection and GitHub plugin both bind to `ASWDWWW`
- Required Gmail for this repo is `zakiymanigo@gmail.com`; MCP Sent identity is `fitdadmin@fitdai.com`
- Firebase MCP active project is `fitd-app-203cb` (FITD-Bible); this repo `.firebaserc` is `zakiymanigo-career`

Outdated / unfinished (preserved, not modified):

- Untracked `Career/`, `Content/`, new resume and cover-letter folders
- Hundreds of indexed files deleted under `Resumes & Cover Letters/use/`
- `index-safety.html` at repo root (backup; hosting serves `public/`)

## Built / updated this session

- Re-verified integrations against live MCP/CLI (no secrets stored)
- Added [CONSTRUCTION-PHASES.md](CONSTRUCTION-PHASES.md) and dated re-verify record
- Filled Figma, n8n, Magnific, Stripe, Hostinger, and Zoom status into inventory, control center, workflows, finance, marketing, communications, and the prompt library
- Registered discovered n8n workflows in the automation catalog (documentation only; nothing executed)
- Native file counts unchanged: 5 rules, 17 commands, 8 skills, 6 agents, `hooks.json`

## Tested (this session)

| Check | Result |
| --- | --- |
| Hook unit harness (11 cases) | **verified** pass |
| Native file counts | **verified** |
| `Career/`, `Content/`, `public/index.html`, `index-safety.html` still present | **verified** |
| GitHub MCP identity `ASWDWWW`; `gh` dual logins | **verified** |
| Gmail Sent identity | **verified** wrong mailbox (`fitdadmin@fitdai.com`) |
| Firebase env user `zakiymanigo@gmail.com`; MCP project FITD | **verified** (do not deploy from here) |
| Stripe account list (test + live rows) | **verified** list only |
| Figma `whoami` | **verified** |
| n8n workflow list | **verified** |
| Magnific profile + balance | **verified** (no generation) |
| Hostinger domains + billing; website list empty | **verified** |
| Hugging Face `zakiymanigo` | **verified** (expires 21 Sep 2026 03:41Z) |
| Canva brand kit list | **verified** |
| LinkedIn profile read | **verified** |
| Chrome DevTools `list_pages` | **verified** (`about:blank`) |

## Untested

- Slash command palette in the Cursor UI
- Hooks firing inside a live agent turn (stdin tests only)
- Firebase deploy
- Canva export/generate
- Figma file read / design-to-code
- Magnific paid generation
- n8n execute/publish
- Meta VR beyond disabled debug auth
- Discord, Playwright
- Browser walkthrough of the career site (site files were not changed)
- Concurrent worktrees

## Awaiting access

- Gmail MCP reconnect to `zakiymanigo@gmail.com`
- Zoom catalog OAuth (`needsAuth` / localhost redirect)
- Zoom bridge (DCR failure this session)
- Private `FITD-fash` repository list (would require an explicit account switch, which was not done)
- IONOS Cloud MCP (discovery error)

## Awaiting a decision

- Stripe account in-scope for this OS
- Whether Figma work may use the Bariatric Associates org
- Whether the active n8n Instagram poster should remain on
- Whether to keep this OS in a **public** repo
- Budgets, legal entities, fundraising target, product priority order
- Hugging Face token refresh (expiry 21 Sep 2026 03:41Z)

## Unsupported here

- Catalog Zoom plugin OAuth until Cursor stops sending `localhost`
- IONOS until the local binary + token work
- Custom metrics dashboard (intentionally later)
- Squarespace **site/DNS** admin (MCP is domain search only)

## Intentionally disabled / not run

- `gh auth switch`
- Zoom catalog `mcp_auth`
- Gmail send
- Firebase deploy
- Stripe live writes
- Magnific image/video generation
- n8n execute / publish
- Force-push and git config (hook-denied)
- Recurring always-on department agents

## Optional later

Custom dashboard; IONOS if Cloud is in use; Zoom bridge repair; moving OS to a private repo; Gmail reconnect; n8n catalog of remaining workflows after MCP-enable.

## How to operate

Read [OPERATING-GUIDE.md](OPERATING-GUIDE.md). Refresh [CONTROL-CENTER.md](CONTROL-CENTER.md) with `/control-center`.
