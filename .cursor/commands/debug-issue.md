# Debug an issue

1. Reproduce with evidence (command output, logs, screenshot, failing test). Do not guess.
2. Name the product and environment. GitHub identity is origin (`ASWDWWW` here). Do not prompt for an account. Do not switch accounts to “see if it works.”
3. Find the smallest failing path. Check recent unfinished work before assuming a regression from the operating system.
4. Apply a minimal fix. Add or update a test or verification note when possible.
5. Hunt for the same failure on related routes or jobs.
6. Record cause, fix, and leftover risk in the ticket or `ops/templates/incident.md` if it is production.

Authorization: local debugging is allowed. Production deploys and live payment changes are not.
