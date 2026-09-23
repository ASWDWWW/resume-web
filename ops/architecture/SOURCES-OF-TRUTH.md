# Sources of truth

Folders organize work. They are **not** security boundaries. Sensitive material needs real permissions (private repo, account ACL, or keep it off git).

## Surfaces

| Surface | Path | Authoritative for |
| --- | --- | --- |
| Product and engineering (this site) | `public/`, `css/`, `firebase.json`, `.firebaserc` | Career site code and hosting config |
| Product and engineering (ops) | `ops/product-engineering/` | Tickets, engineering workflows for the OS and this site |
| Career evidence | `Career/` | Job-title packets and career notes (untracked at OS setup). Jobs: `Career/Experience/Jobs`. Projects: `Career/Experience/Projects`. |
| Application materials | `Resumes & Cover Letters/` | Resume and cover-letter drafts |
| Media | `Content/` | Photos/video (untracked at OS setup) |
| Business operations and growth | `ops/business-operations/` | Strategy, marketing, sales/CS, finance, legal prep, fundraising, communications, team |
| Restricted company records | `ops/restricted/` | Pointers and gitignored local records |
| Owner oversight | `ops/owner/` | Control-center policy, private notes gitignored under `private/` |
| Agent configuration | `AGENTS.md`, `.cursor/` | How agents run |

Other products’ **code** is authoritative in their own GitHub repos, not here.

## Record types

| Record | Lives here | Do not use |
| --- | --- | --- |
| Tickets | `ops/product-engineering/tickets/` | Chat history |
| Customer records | Not in this repo (unresolved CRM) | Invented customers |
| Financial figures | `ops/business-operations/finance/` split actuals / estimates / forecasts | Mixing the three |
| Designs | Figma (identity verified; files untested); Canva (verified); Magnific generations (credits) | Mixing Figma/Canva/Magnific as if they were one file |
| Decisions | `ops/product-engineering/decisions/` | Silent chat agreements |
| Documents | Dated markdown under the matching surface | Stale copies in `index-safety.html` unless you restore it |

`index-safety.html` is a root backup of the site. `public/index.html` is what Firebase hosting is configured to serve.

## Reuse

Reuse GitHub issues only in the repo that owns the product. This OS uses markdown tickets so it works without an issue tracker in `resume-web` (the public repo had 0 open issues at verification).
