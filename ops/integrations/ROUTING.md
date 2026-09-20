# Account routing

Agents must not silently switch accounts when an operation fails. Name the required identity, stop the external action, and continue other work.

## This workspace

| Resource | Identity |
| --- | --- |
| Git remote | `ASWDWWW/resume-web` |
| GitHub CLI | Active: `ASWDWWW`. Inactive: `FITD-fash` |
| GitHub MCP | `ASWDWWW` |
| Firebase | `zakiymanigo@gmail.com` / project `zakiymanigo-career` |
| Git user | Zakiy Manigo `<zakiymanigo@gmail.com>` (do not change via `git config`) |

## Product → GitHub owner

| Product / repo | GitHub identity to use | Notes |
| --- | --- | --- |
| resume-web and other `ASWDWWW/*` repos | **github-aswdwww** | Default |
| `FITD-fash/*` | **github-fitd-fash** | Only after the user asks to use that login |
| Unknown private FITD app repos | **awaiting a decision** | Do not switch accounts to search |

## Gmail identity

| Use | Identity |
| --- | --- |
| User-reported business mail | `gmail-fashiobusiness` (unauthenticated) |
| Observed personal identity | `zakiymanigo@gmail.com` (git, Firebase, LinkedIn) |
| If both could apply | Ask. Never fall back |

## Payments

| Mode | Authority |
| --- | --- |
| Stripe test / TREI Stripe sandbox (other repo) | Engineering debugging with named environment |
| Stripe live | Owner (Zakiy) explicit approval in writing in the ticket |
| IAP (FitGenius / FITD) | Those product repos; not this workspace |

## Failure behavior

1. Retry once on the **same** identity.
2. If auth/permission fails, record it. Do not run `gh auth switch`, do not log into another Gmail, do not pick another Firebase project “that might work.”
3. Continue independent work.

Hooks ask before `gh auth switch` / `gh auth login` and deny `git config`.
