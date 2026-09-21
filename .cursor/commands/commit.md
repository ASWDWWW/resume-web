---
description: Commit intended files as ASWDWWW. Does not push.
---

# Commit

Read `.cursor/skills/git-github/SKILL.md` and follow it. This command is authorization to **commit**, not to push.

GitHub identity is automatic from `origin` (`ASWDWWW` for this repo). Do not prompt for an account. Do not run `gh auth switch`. Do not call GitHub `mcp_auth`.

1. In parallel: `git status`, `git diff`, `git log -8 --oneline`.
2. Stage only the files for this request. Leave `Career/`, `Content/`, secrets, `.cursor/hooks/logs/`, and unfinished resume deletions unstaged unless the user named them.
3. Draft a 1–2 sentence message that explains why, matching recent log style.
4. Commit with `node .cursor/skills/git-github/scripts/commit.mjs --message "..."` (Windows-safe). Do not `--no-verify`. Do not run `git config`.
5. Run `git status`. If there is nothing to commit, stop. Do not push.
