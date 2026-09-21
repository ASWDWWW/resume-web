# Integration inventory

User-reported connections were treated as claims and re-verified on **20 September 2026** (second pass, OS re-execution). No secrets are recorded. Overlapping personal and plugin connections are documented, not removed. **github-fitd-fash** was not made the active `gh` login (this workspace stays **github-aswdwww**).

Status key: **verified** · **untested** · **awaiting access** · **awaiting a decision** · **unsupported** · **intentionally disabled**

## Personal GitHub connections

### github-aswdwww

| Field | Value |
| --- | --- |
| Purpose | Default owner of this workspace and most personal/product repos |
| Account identity | GitHub user `ASWDWWW` (Zakiy Manigo) |
| Configuration scope | `gh` login `ASWDWWW` used via `gh auth token --user ASWDWWW` (no switch, no picker). Origin URL includes `ASWDWWW@`. GitHub MCP `get_me` = `ASWDWWW` |
| Permissions | MCP/gh: gist, read:org, repo (no workflow scope on this login) |
| Environment | github.com |
| Dependencies | `gh` CLI, GitHub MCP (`user-github`) |
| Verification | **verified** 20 Sep 2026 (this session) |

### github-fitd-fash

| Field | Value |
| --- | --- |
| Purpose | Separate FITD GitHub login |
| Account identity | GitHub user `FITD-fash` |
| Configuration scope | `gh` login **present but inactive**. Not switched this session |
| Permissions | gist, read:org, repo, workflow (token not recorded) |
| Environment | github.com |
| Dependencies | Same `gh` binary, different account |
| Verification | **verified** as a distinct login. Private FITD repos still **awaiting access** without an explicit switch. GitHub MCP remains `ASWDWWW` |

## Personal Gmail

### zakiymanigo (this repo)

| Field | Value |
| --- | --- |
| Purpose | Mail for `resume-web` / career site |
| Account identity | **zakiymanigo** / `zakiymanigo@gmail.com` (owner confirmed 20 Sep 2026) |
| Configuration scope | Gmail MCP `plugin-gmail-gmail` is signed in, but Sent mail used `fitdadmin@fitdai.com` |
| Permissions | Read confirmed on the currently signed-in mailbox |
| Environment | Google / Cursor MCP |
| Dependencies | Reconnect Gmail plugin to `zakiymanigo@gmail.com` for this repo |
| Verification | Routing **verified** (owner). MCP mailbox **wrong identity** until reconnect |

### gmail-fashiobusiness

Not for this repo. FITD/other products only. Do not fall back to it from `resume-web` work.

## Other personal integrations

| Integration | Purpose (reported) | Identity / scope | Permissions | Environment | Dependencies | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Hostinger | Hosting / domains / VPS | Hostinger MCP plugins; domain `zakiy-n8n-auto.cloud` (free_domain + paid domain rows). Subscriptions `.CLOUD Domain` (next bill 13 Dec 2026) and `KVM 2` (next bill 23 Feb 2028) | Domain list and billing list succeeded. Website list returned **0** sites (VPS/domain only in this API) | Hostinger API | Cursor Hostinger plugin | **verified** (domains, billing, empty website list) |
| IONOS | IONOS Cloud MCP | User MCP `ionoscloud`. Namespace status **error** (live tool discovery failed) | n/a until binary + real token | IONOS Cloud | Local exe + DCD token | **awaiting access** |
| Magnific | Image/video generation | User MCP `magnific`. Signed in as Zakiy Manigo / `zakiymanigo@gmail.com`. Plan Premium+. Account unlimited flag is on; **unlimited does not apply via MCP** — generations consume credits | Read identity + balance. Paid tools exist; not used this session | Magnific | Credits / budget in control center | **verified** (identity + balance). Paid generation **intentionally disabled** until a budget is named |
| n8n | Automations | User MCP `n8n` → Hostinger-hosted instance. 11 workflows listed | MCP can see FitGenius draft workflows (inactive). One **active** Instagram poster is not MCP-enabled | Hostinger n8n | Instance MCP in user mcp.json | **verified** (list). Execute/publish **intentionally disabled** |
| Squarespace | Domain search (official MCP) | User MCP `squarespace`. No account login. Does **not** manage `fitdai.com` site/DNS | `domains_generate_names`, `domains_search` (read-only; checkout is on squarespace.com) | Squarespace | User mcp.json | **verified** 20 Sep 2026. See `ops/integrations/squarespace.md` |
| Zoom | Meetings | Catalog `plugin-zoom-zoom` stays `needsAuth` (error 4700). Always use `user-zoom-bridge`. Tokens **verified** 20 Sep 2026. Header-path fix written; reload MCP | Catalog: do not call `mcp_auth`. Bridge: tools listed | Zoom | HTTPS bounce + local client-info | Catalog **unsupported**. Bridge **verified** (auth). Tool calls need MCP reload |

## Plugins (this Cursor session)

| Plugin | Purpose | Identity | Scope / permissions observed | Env | Dependencies | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Canva | Designs | Canva MCP; brand kit id present | Read/list | Canva | MCP | **verified** (read) |
| Chrome DevTools | Browser verification | `plugin-devtools-for-agents-chrome-devtools`; `list_pages` = `about:blank` | Page automation | Local browser | DevTools MCP | **verified** present |
| Figma | Design handoff | `plugin-figma-figma`. Zakiy Manigo / `zakiymanigo@gmail.com`. Admin on personal starter team. Guest **view** on Bariatric Associates org | Read identity + plans. File reads **untested**. Do not open the clinic org unless a TREI ticket names it | Figma | MCP | **verified** (whoami). File workflows **untested** |
| Firebase | Hosting/backend | CLI/MCP user `zakiymanigo@gmail.com`. MCP environment used project directory `FITD-Bible/.../react-fitd-website`, active project `fitd-app-203cb` | Project env read. This resume-web tree is `zakiymanigo-career` in `.firebaserc` | Firebase/GCP | Firebase MCP | **verified** signed in. Active MCP project is FITD, not career site — do not silently switch |
| GitHub | Repos/PRs | Plugin + `user-github` as `ASWDWWW` | Overlaps `github-aswdwww` | github.com | MCP | **verified** |
| Gmail | Mail | Plugin signed in, mailbox is not zakiymanigo (Sent = `fitdadmin@fitdai.com`) | Read on the wrong mailbox for this repo | Google | Reconnect to `zakiymanigo@gmail.com` | **awaiting access** (wrong identity) |
| Hugging Face | Models/hub | `zakiymanigo`; OAuth expires **2026-09-21T03:41:58Z** | Hub + inference scopes | Hugging Face | MCP | **verified**. Refresh **upcoming** |
| Meta VR | Quest/Horizon | `plugin-meta-vr-metavr` present; `auth_status` says debug tools disabled | Docs/tools | Meta | MCP | **untested** (debug auth off) |
| Stripe | Payments | MCP ready. Accounts: Fleet Trucking Platform, TaxTracker, Zakiy T. Manigo — each with live and test/sandbox rows | Account list only. Live mode **not** used | Stripe | MCP | **verified** (list). Default remains **test**. Live changes need named authority |
| Zoom | Meetings | Catalog needsAuth by design. Bridge is the Zoom connection | See Zoom row above | Zoom | Bridge | Catalog **unsupported**. Bridge **verified** |

## Extra connectors present but not in the original prompt list

| Connector | Identity | Status |
| --- | --- | --- |
| LinkedIn MCP | Zakiy Manigo, `zakiymanigo@gmail.com` | **verified** profile read |
| Discord MCP | Tools available | **untested**; not in the prompt list |
| Svelte MCP | Docs tools | **intentionally unused** unless a Svelte app is in scope |
| Playwright MCP | Browser tools | **untested**; not in the prompt list |
| Squarespace MCP | Unauthenticated domain search | **verified** (extra to original list) |

## Firebase projects previously listed for `zakiymanigo@gmail.com`

cast-live-os, feedsnatcher, fitd-app-203cb, fitd-app-staging, fitd-automations, fitgenius-5847b, insightful-care-solutions, launchpage-alex-roadservice, launchpage-studio, launchpage-tax-tracker, mesanginsista, quategory-dev, visual-life-4c6d4, zakiymanigo-career.

Do not deploy to any of these unless the ticket names the project and you authorize it.
