# Integration inventory

User-reported connections were treated as claims and verified on 17 September 2026. No secrets are recorded. Overlapping personal and plugin connections are documented, not removed.

Status key: **verified** · **untested** · **awaiting access** · **awaiting a decision** · **unsupported** · **intentionally disabled**

## Personal GitHub connections

### github-aswdwww

| Field | Value |
| --- | --- |
| Purpose | Default owner of this workspace and most personal/product repos |
| Account identity | GitHub user `ASWDWWW` (Zakiy Manigo) |
| Configuration scope | `gh` **active** account; GitHub MCP `get_me` = `ASWDWWW`; git remote `https://github.com/ASWDWWW/resume-web.git` |
| Permissions | MCP/gh: gist, read:org, repo (no workflow scope on this login). Collaborator role on resume-web: admin |
| Environment | github.com |
| Dependencies | `gh` CLI, GitHub MCP (`user-github`) |
| Verification | **verified** |

### github-fitd-fash

| Field | Value |
| --- | --- |
| Purpose | Separate FITD GitHub login (user-reported) |
| Account identity | GitHub user `FITD-fash` |
| Configuration scope | `gh` login **present but inactive**. Do not switch to inspect private repos |
| Permissions | Token scopes on the inactive login include gist, read:org, repo, **workflow** (do not print tokens) |
| Environment | github.com |
| Dependencies | Same `gh` binary, different account |
| Verification | **verified** as a distinct login; private repo list **awaiting access** without an explicit switch. Public: `FITD-fash/cursor-zoom-oauth-callback` (Zoom OAuth bounce, no secrets in description) |

## Personal Gmail

### gmail-fashiobusiness

| Field | Value |
| --- | --- |
| Purpose | User-reported business Gmail |
| Account identity | Reported name only; mailbox address not verified in-session |
| Configuration scope | Gmail MCP namespace `plugin-gmail-gmail` |
| Permissions | Unknown (server **needsAuth**) |
| Environment | Google / Cursor MCP |
| Dependencies | User completes MCP auth |
| Verification | **awaiting access**. Overlaps with observed `zakiymanigo@gmail.com` on git, Firebase, and LinkedIn — do not auto-select |

## Other personal integrations

| Integration | Purpose (reported) | Identity / scope | Permissions | Environment | Dependencies | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Hostinger | Hosting | None in this workspace | n/a | External | DNS/account in Hostinger | **unsupported** here (no connector). Continue independently |
| IONOS | Hosting/DNS | None in this workspace | n/a | External | IONOS account | **unsupported** here |
| Magnific | Image upscale/generation | None in this workspace | n/a | External | Budget + account | **unsupported** here |
| n8n | Automations | None in this workspace | n/a | External | n8n instance URL | **unsupported** here. Catalog placeholders only |
| Zoom | Meetings | Plugin `plugin-zoom-zoom` **needsAuth**; FITD-fash public OAuth bounce repo exists | Unknown until auth | Zoom | User MCP auth | **awaiting access** |

## Plugins (this Cursor session)

| Plugin | Purpose | Identity | Scope / permissions observed | Env | Dependencies | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Canva | Designs | Canva MCP authenticated; brand kit id `kAGGMeca1oc`; recent owned designs include FITD and automotive one-pagers | Design read/search; generation tools present | Canva | MCP | **verified** (read). Publish/export **untested** |
| Chrome DevTools | Browser verification | `plugin-devtools-for-agents-chrome-devtools`; `list_pages` returned `about:blank` | Page automation | Local browser | DevTools MCP | **verified** present; site browse **untested** |
| Figma | Design handoff | Not in available MCP namespaces | n/a | n/a | Install plugin | **unsupported** in this workspace |
| Firebase | Hosting/backend | CLI/MCP user `zakiymanigo@gmail.com`; active project `zakiymanigo-career`; 14 accessible projects | Project list, hosting config; billing **on** on career project (Cloud Billing API 17 Sep 2026). MCP `get_environment` still prints `Billing Enabled: No` — do not trust that flag | Firebase/GCP | Firebase MCP + `.firebaserc` | **verified** (list/env + billingInfo). Deploy **intentionally not run** |
| GitHub | Repos/PRs | Plugin + `user-github` as `ASWDWWW` | Overlaps personal `github-aswdwww` | github.com | MCP | **verified**; overlap **documented** |
| Gmail | Mail | Plugin needsAuth | n/a | n/a | MCP auth | **awaiting access** |
| Hugging Face | Models/hub | `zakiymanigo`; OAuth scopes openid, profile, read-mcp, read-repos, jobs, contribute-repos, inference-api; token expiry 2026-09-17T20:28:23Z | Hub + inference | Hugging Face | MCP | **verified**. Expiry same calendar day — **awaiting a decision** to refresh if work continues |
| Meta VR | Quest/Horizon | `plugin-meta-vr-metavr` present; `auth_status` said debug tools disabled | Docs/tools; auth debug not enabled | Meta | MCP | **untested** |
| Stripe | Payments | Not in available MCP namespaces | n/a | test vs live TBD | Install or API | **unsupported** here |
| Zoom | Meetings | Plugin needsAuth | n/a | Zoom | MCP auth | **awaiting access** |

## Extra connectors present but not in the user inventory

Documented so agents do not treat them as assigned:

| Connector | Identity | Status |
| --- | --- | --- |
| LinkedIn MCP | Zakiy Manigo, `zakiymanigo@gmail.com` | **verified** profile read. Sending messages **awaiting a decision** |
| Discord MCP | Tools available | **untested**; not in inventory |
| Svelte MCP | Docs tools | **intentionally unused** unless a Svelte app is in scope |

## Firebase projects visible to `zakiymanigo@gmail.com`

cast-live-os, feedsnatcher, fitd-app-203cb, fitd-app-staging, fitd-automations, fitgenius-5847b, insightful-care-solutions, launchpage-alex-roadservice, launchpage-studio, launchpage-tax-tracker, mesanginsista, quategory-dev, visual-life-4c6d4, zakiymanigo-career.

Do not deploy to any of these from this OS setup.
