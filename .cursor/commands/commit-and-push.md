---
description: Commit intended files, then push as the origin GitHub owner.
---

# Commit and push

Read `.cursor/skills/git-github/SKILL.md` and follow it. This command is authorization to **commit and push**.

GitHub identity is automatic from `origin` (`ASWDWWW` for this repo). Do not prompt for an account. Do not run `gh auth switch`. Do not call GitHub `mcp_auth`.

## Commit

1. In parallel: `git status`, `git diff`, `git log -8 --oneline`.
2. Stage only the files for this request. Leave `Career/`, `Content/`, secrets, `.cursor/hooks/logs/`, and unfinished resume deletions unstaged unless the user named them.
3. Draft a 1–2 sentence message that explains why, matching recent log style.
4. Commit with `node .cursor/skills/git-github/scripts/commit.mjs --message "..."`. Do not `--no-verify`. Do not run `git config`.
5. If nothing was committed, stop. Do not push.

## Push

6. Run `node .cursor/skills/git-github/scripts/identity.mjs`, then `node .cursor/skills/git-github/scripts/push.mjs`.
7. Report the login and remote used. If auth fails, name the required login and stop — do not try another GitHub user.
