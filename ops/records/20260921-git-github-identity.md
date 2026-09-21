# GitHub identity for commit/push

Date: 21 September 2026  
Identity: **github-aswdwww** (`ASWDWWW`). `github-fitd-fash` was not switched.

## Built

- Slash commands `/commit`, `/push`, `/commit-and-push`
- Skill `git-github` with `identity.mjs`, `commit.mjs`, `push.mjs`
- Origin pinned to `https://ASWDWWW@github.com/ASWDWWW/resume-web.git` so Git Credential Manager does not ask which account

## Tested

- `identity.mjs` verified login `ASWDWWW` (token not printed)
- `push.mjs --dry-run` → `Everything up-to-date` as `ASWDWWW` (no account picker)
- `commit.mjs` with nothing staged exits 1; `--no-verify` refused
- Hook harness still pass

## Blocked / optional

- None for this repo’s git path. Cursor GitHub MCP `get_me` was already `ASWDWWW`; agents must not call GitHub `mcp_auth`.
