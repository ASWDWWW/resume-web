# Owner control center

Last reviewed: 20 September 2026 (OS brief re-executed; integrations re-verified). Career-site refresh remains live from 17 September 2026.  
This is the maintainable document view. A custom dashboard is optional and not built.

Workspace construction ≠ permission to operate businesses externally.

## Goals and priorities

| Priority | Goal | Metric | Status |
| --- | --- | --- | --- |
| 1 | Keep this Cursor workspace as the owner OS | Commands, hooks, routing, and control center stay current | Re-verified this session |
| 2 | Career site and job-search materials | Site in `public/`; packets in `Career/`; resumes in `Resumes & Cover Letters/` | Ticket `SITE-20260917-refresh` **live** on Hosting; Storage rules released |
| 3 | Product work in other repos (TREI, FITD, FitGenius, LaunchPage, others) | Per-product repos and Firebase projects | Linked, not operated from here |

Assumed until you confirm: job search and TREI delivery are the live priorities. See `ops/records/assumptions.md`.

## Active work and owners

| Work | Owner | Notes |
| --- | --- | --- |
| Owner operating system in this repo | Zakiy Manigo | Decision owner for OS changes |
| Untracked `Career/` packets | Zakiy | Preserve; do not auto-commit |
| Untracked `Content/` media | Zakiy | Preserve |
| New resume/cover-letter folders | Zakiy | Preserve |
| Indexed files deleted under `Resumes & Cover Letters/use/` | Zakiy | Unfinished; do not revert unless asked |
| Career-site refresh (`SITE-20260917-refresh`) | Zakiy | **Live** 17 Sep 2026. PR https://github.com/ASWDWWW/resume-web/pull/1 merged to main. Hosting + Storage rules deployed to `zakiymanigo-career` as `zakiymanigo@gmail.com`. |
| TREI / BariAccess engineering | Zakiy (with Andrei on the product) | Code is not in this repo |
| FITD | Zakiy | GitHub identity `FITD-fash` is separate |

## Decisions and approvals needed

- Which GitHub identity owns each private FITD repo (`FITD-fash` private list not retrieved without account switch).
- Reconnect Gmail MCP to `zakiymanigo@gmail.com` (currently Sent as `fitdadmin@fitdai.com`).
- Zoom is **always** `user-zoom-bridge`. Catalog plugin stays `needsAuth` (error 4700). Reload **zoom-bridge** in Settings → MCP after the Windows header-path fix. See `ops/integrations/zoom.md`.
- Which Stripe account is in-scope for this OS (Fleet Trucking Platform, TaxTracker Pro, Zakiy T. Manigo). Default stays **test**.
- IONOS: local MCP binary + real DCD token, or confirm IONOS is unused.
- Hugging Face OAuth expires **21 Sep 2026 03:41Z** — refresh if Hub tools are needed after that.
- Whether Figma file work for TREI may use the Bariatric Associates org (guest view only).
- Squarespace MCP is domain search only. Site/DNS for `fitdai.com` stays in the Squarespace admin (browser), not this MCP.
- Confirm current business priorities and budgets.
- Whether this OS should stay in the public `resume-web` repo or move to a private repo.

## Customer issues and product health

| Product | Health signal in this workspace | External evidence |
| --- | --- | --- |
| Career site | Live `public/index.html` on Hosting with galleries from Storage | https://zakiymanigo-career.web.app (also `.firebaseapp.com`). Deployed 17 Sep 2026 as `zakiymanigo@gmail.com` / `zakiymanigo-career`. GitHub `ASWDWWW/resume-web` PR #1 merged to main. |
| TREI / BariAccess | Career packets only | Staging on Azure per packets; production dark |
| FITD | Career packets; Firebase `fitd-app-203cb` and staging | Code not in this repo |
| FitGenius | Career packets; Firebase `fitgenius-5847b`; n8n draft workflows exist (inactive) | Pre-launch per packets |
| Insightful Care | Career packets; Firebase `insightful-care-solutions` | Live site cited in packets |
| Automotive Operations System | Career packets; Firebase `launchpage-alex-roadservice` | Public GitHub repo `ASWDWWW/Alex-Road-Service` |

No live customer-issue queue is connected. Use tickets under `ops/product-engineering/tickets/`.

## Sales, marketing, financial, and investor metrics

All figures below are **empty until sourced**. Do not invent.

| Kind | Location | Last sourced |
| --- | --- | --- |
| Actuals | `ops/business-operations/finance/actuals.md` | Hostinger billing API 20 Sep 2026 (subscription list only) |
| Estimates | `ops/business-operations/finance/estimates.md` | none |
| Forecasts | `ops/business-operations/finance/forecasts.md` | none |
| Marketing experiments | `ops/business-operations/marketing.md` | none |
| Fundraising metrics | `ops/business-operations/fundraising.md` | none |

## Upcoming obligations

| When | Item | Source |
| --- | --- | --- |
| 21 Sep 2026 03:41Z | Hugging Face MCP OAuth expires | `hf_whoami` this session |
| 13 Dec 2026 | Hostinger `.CLOUD Domain` next billing | Hostinger billing list |
| 23 Feb 2028 | Hostinger `KVM 2` next billing | Hostinger billing list |

No other dated commitments confirmed in-repo.

## Integration health, automation, costs

See `ops/integrations/INVENTORY.md` (re-verified 20 Sep 2026 this session). Hooks log to `.cursor/hooks/logs/` (gitignored).

| Connector | This session |
| --- | --- |
| GitHub `ASWDWWW` | Signed in. `/commit`, `/push`, `/commit-and-push` pin this login |
| Gmail | Wrong mailbox (`fitdadmin@fitdai.com`) |
| Stripe | Test+live listed; live unused |
| Figma | Signed in (`zakiymanigo@gmail.com`) |
| Hostinger | Domains + billing; 0 websites |
| Magnific | Signed in; MCP generations spend credits |
| n8n | Workflow list succeeded |
| Canva, LinkedIn, Hugging Face | Signed in |
| Firebase | User `zakiymanigo@gmail.com`; MCP project is FITD, not career |
| Zoom catalog | `needsAuth` by design — unused |
| Zoom bridge | Always-on path. Reload MCP after header-path fix |
| IONOS | Discovery error |
| `github-fitd-fash` | Inactive on `gh` |

| Automation | State |
| --- | --- |
| Cursor hooks (shell, MCP, secrets, secret-file reads, edit audit) | Registered; harness **pass** this session |
| n8n FitGenius draft workflows | Inactive; MCP-available; do not publish/execute unless asked |
| n8n Instagram poster (active on instance) | Not MCP-available. Confirm in the n8n UI whether it should stay on |
| Recurring agent | Intentionally not created; use commands |
