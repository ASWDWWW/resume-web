# Account routing

Agents must not silently switch accounts when an operation fails. Name the required identity, stop the external action, and continue other work.

## This workspace

| Resource | Identity |
| --- | --- |
| Git remote | `https://ASWDWWW@github.com/ASWDWWW/resume-web.git` (username in the URL so Git Credential Manager does not ask which account) |
| GitHub CLI | Use `ASWDWWW` for this origin without switching. `FITD-fash` stays logged in but unused here |
| GitHub MCP | `user-github` as `ASWDWWW`. Do not call `mcp_auth` |
| Firebase | `zakiymanigo@gmail.com` / project `zakiymanigo-career` |
| Git user | Zakiy Manigo `<zakiymanigo@gmail.com>` (do not change via `git config`) |
| Gmail (this repo) | **zakiymanigo** (`zakiymanigo@gmail.com`) |

GitHub account selection is **not interactive** in this repo. Origin owner maps to the login (`ASWDWWW/*` → `ASWDWWW`, `FITD-fash/*` → `FITD-fash`). Commit and push with `/commit`, `/push`, `/commit-and-push` and the scripts in `.cursor/skills/git-github/scripts/` (`gh auth token --user <login>`, never `gh auth switch`).

## Product → GitHub owner

| Product / repo | GitHub identity to use | Notes |
| --- | --- | --- |
| resume-web and other `ASWDWWW/*` repos | **github-aswdwww** | Automatic from origin. No account picker |
| `FITD-fash/*` | **github-fitd-fash** | Automatic only when origin owner is `FITD-fash`. Do not switch this repo’s remote |
| Unknown private FITD app repos | **awaiting a decision** | Do not switch accounts to search |

## Gmail identity

| Use | Identity |
| --- | --- |
| **This repo (`resume-web`)** | **zakiymanigo** / `zakiymanigo@gmail.com` (confirmed 20 Sep 2026) |
| FITD / other products | `gmail-fashiobusiness` or `fitdadmin@fitdai.com` — do not use for this repo |
| If Gmail MCP is signed into a different mailbox | Stop. Do not send. Ask the user to reconnect Gmail to `zakiymanigo@gmail.com` |

Gmail MCP as of 20 Sep 2026 returned Sent as `fitdadmin@fitdai.com`. That is the **wrong** identity for this workspace until the plugin is reconnected.

## Squarespace

Official MCP (`user-squarespace`) is unauthenticated **domain search**. It is not a login to `fitdai.com` or any Squarespace site. Do not buy a domain from a checkout link without an explicit request.

## Zoom

Always `user-zoom-bridge`. Catalog `plugin-zoom-zoom` stays `needsAuth` (Cursor `localhost` redirect, Zoom error 4700). Do not call that plugin’s `mcp_auth`. Meeting create/delete still needs an explicit request.

## Firebase

| Resource | Identity |
| --- | --- |
| This repo (`.firebaserc`) | `zakiymanigo-career` |
| MCP this session | User `zakiymanigo@gmail.com`, active project **`fitd-app-203cb`** (FITD-Bible tree) |

Do not deploy the FITD project from this workspace. If Firebase MCP is on the wrong project, stop and name `zakiymanigo-career` rather than switching silently.

## Payments

| Mode | Authority |
| --- | --- |
| Stripe test / TREI Stripe sandbox (other repo) | Engineering debugging with named environment |
| Stripe live | Owner (Zakiy) explicit approval in writing in the ticket |
| IAP (FitGenius / FITD) | Those product repos; not this workspace |

## Failure behavior

1. Retry once on the **same** identity.
2. If auth/permission fails, record it. Do not run `gh auth switch`, do not show an account picker, do not log into another Gmail, do not pick another Firebase project “that might work.”
3. Continue independent work.

Hooks ask before `gh auth switch` / `gh auth login` and deny `git config`.
