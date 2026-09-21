---
description: Push the current branch as the origin GitHub owner. No account picker.
---

# Push

Read `.cursor/skills/git-github/SKILL.md` and follow it. This command is authorization to **push** the current branch.

Do not prompt for a GitHub account. Do not run `gh auth switch`. Do not call GitHub `mcp_auth`. Use `user-github` only as `ASWDWWW` in this repo.

1. Run `node .cursor/skills/git-github/scripts/identity.mjs`. The required login must match origin (`ASWDWWW` here).
2. Run `node .cursor/skills/git-github/scripts/push.mjs`. Extra git-push flags may be appended except force to `main`/`master`.
3. Report the login and remote used.

If auth or permission fails, name the required login and stop. Do not try `FITD-fash` (or any other user) as a fallback.
