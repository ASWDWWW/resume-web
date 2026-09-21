---
name: git-github
description: Commit and push using the GitHub identity implied by origin. Use for /commit, /push, /commit-and-push, git push, or Git Credential Manager account pickers.
disable-model-invocation: true
---

# Git commit and GitHub identity

This workspace does **not** prompt for a GitHub account. Origin owner is the identity.

| Origin owner | Login | Use |
| --- | --- | --- |
| `ASWDWWW` | `ASWDWWW` | This repo and other `ASWDWWW/*` remotes |
| `FITD-fash` | `FITD-fash` | Only that owner’s remotes |

Do not run `gh auth switch`. Do not call GitHub `mcp_auth`. Do not ask the user which account. Use `user-github` as `ASWDWWW` in this repo.

## Scripts

Run from the repo root. Never print tokens.

```text
node .cursor/skills/git-github/scripts/identity.mjs
node .cursor/skills/git-github/scripts/commit.mjs --message "Subject"
node .cursor/skills/git-github/scripts/push.mjs
```

`identity.mjs` pins `origin` to `https://LOGIN@github.com/OWNER/REPO.git` (HTTPS only) so Git Credential Manager does not show an account picker. Push uses that login’s `gh` token without changing the active `gh` account.

## Commit

`/commit` is authorization to commit, not to push.

1. `git status`, `git diff`, `git log -8 --oneline` in parallel.
2. Stage the intended files. Do not add `Career/`, `Content/`, `.env`, credentials, hook logs, or unfinished resume deletions unless the user named them.
3. One or two sentences on **why**. Match recent log style.
4. `node .cursor/skills/git-github/scripts/commit.mjs --message "..."` — do not `--no-verify`, `git config`, or empty commits.
5. `git status`. Stop.

## Push

`/push` is authorization to push the current branch.

1. `node .cursor/skills/git-github/scripts/identity.mjs` then `node .cursor/skills/git-github/scripts/push.mjs`.
2. If auth fails, name the required login and stop. Do not try the other GitHub user.
3. No force-push to `main`/`master`.

## Commit and push

Commit first. Push only if the commit succeeded.
