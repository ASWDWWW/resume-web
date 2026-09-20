# Owner control center

Last reviewed: 17 September 2026 (career-site refresh merged to `ASWDWWW/resume-web` main and live-deployed to `zakiymanigo-career`).  
This is the maintainable document view. A custom dashboard is optional and not built.

Workspace construction ≠ permission to operate businesses externally.

## Goals and priorities

| Priority | Goal | Metric | Status |
| --- | --- | --- | --- |
| 1 | Keep this Cursor workspace as the owner OS | Commands, hooks, routing, and control center stay current | Built this session |
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
- Which Gmail identity is default for business mail (`gmail-fashiobusiness` reported; `zakiymanigo@gmail.com` observed on git/Firebase/LinkedIn).
- Whether to authenticate Gmail MCP and Zoom MCP.
- Whether Hostinger, IONOS, Magnific, n8n, Figma, and Stripe should be connected here.
- Confirm current business priorities and budgets.
- Whether this OS should stay in the public `resume-web` repo or move to a private repo.

## Customer issues and product health

| Product | Health signal in this workspace | External evidence |
| --- | --- | --- |
| Career site | Live `public/index.html` on Hosting with galleries from Storage | https://zakiymanigo-career.web.app (also `.firebaseapp.com`). Deployed 17 Sep 2026 as `zakiymanigo@gmail.com` / `zakiymanigo-career`. GitHub `ASWDWWW/resume-web` PR #1 merged to main. |
| TREI / BariAccess | Career packets only | Staging on Azure per packets; production dark |
| FITD | Career packets; Firebase `fitd-app-203cb` and staging | Code not in this repo |
| FitGenius | Career packets; Firebase `fitgenius-5847b` | Pre-launch per packets |
| Insightful Care | Career packets; Firebase `insightful-care-solutions` | Live site cited in packets |
| Alex Road Service | Career packets; Firebase `launchpage-alex-roadservice` | Public GitHub repo `ASWDWWW/Alex-Road-Service` |

No live customer-issue queue is connected. Use tickets under `ops/product-engineering/tickets/`.

## Sales, marketing, financial, and investor metrics

All figures below are **empty until sourced**. Do not invent.

| Kind | Location | Last sourced |
| --- | --- | --- |
| Actuals | `ops/business-operations/finance/actuals.md` | none |
| Estimates | `ops/business-operations/finance/estimates.md` | none |
| Forecasts | `ops/business-operations/finance/forecasts.md` | none |
| Marketing experiments | `ops/business-operations/marketing.md` | none |
| Fundraising metrics | `ops/business-operations/fundraising.md` | none |

## Upcoming obligations

Record dated commitments here. None confirmed in-repo as of 17 September 2026.

## Integration health, automation, costs

See `ops/integrations/INVENTORY.md`. Hooks log to `.cursor/hooks/logs/` (gitignored). n8n is not connected. Firebase billing **is enabled** on `zakiymanigo-career` (verified 17 Sep 2026; MCP `get_environment` still prints No). Other project costs are unknown.

| Automation | State |
| --- | --- |
| Cursor hooks (shell, MCP, secrets, secret-file reads, edit audit) | Registered in `.cursor/hooks.json` |
| n8n | Unsupported here until access |
| Recurring agent | Intentionally not created; use commands |
