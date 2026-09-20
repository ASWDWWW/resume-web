# Agent operating instructions

This repository is two things at once:

1. The public career site for Zakiy T. Manigo (`public/`, Firebase project `zakiymanigo-career`).
2. The owner operating system for the businesses, products, and career work that live around that site.

Building or repairing this workspace is **not** authorization to operate a business externally (send email, take payments, publish ads, deploy production, change live Stripe, contact investors or customers).

## Before changing anything

1. Inspect the workspace. Preserve existing code, configuration, instructions, and unfinished work.
2. Identify what is working, missing, conflicting, or outdated.
3. Implement the authorized setup or task. Do not stop at recommendations unless blocked.
4. If an integration is unavailable, continue independently and record the gap.
5. Report precisely what was built, tested, blocked, or left optional.

Unfinished work already present: untracked `Career/` and `Content/`; new resume and cover-letter folders; hundreds of deleted files under `Resumes & Cover Letters/use/`. Do not revert, delete, or “clean up” that work unless the user asks.

## Read these first

- [ops/CONTROL-CENTER.md](ops/CONTROL-CENTER.md) — current goals, work, and health
- [ops/profile/PROJECT-PROFILE.md](ops/profile/PROJECT-PROFILE.md) — business facts vs assumptions
- [ops/integrations/ROUTING.md](ops/integrations/ROUTING.md) — which GitHub and Gmail identity to use
- [ops/architecture/SOURCES-OF-TRUTH.md](ops/architecture/SOURCES-OF-TRUTH.md) — where records live
- [ops/capabilities/DIRECTORY.md](ops/capabilities/DIRECTORY.md) — commands, skills, agents, hooks

## Hard rules

- Never silently switch GitHub, Gmail, Firebase, Stripe, or other accounts when an operation fails.
- This workspace’s git remote is `ASWDWWW/resume-web`. Use `github-aswdwww` unless the user names `github-fitd-fash`.
- Draft messages, invoices, filings, and outreach. Sending, charging, deploying, or advertising requires explicit authorization plus the correct identity.
- Folders named `restricted` or `private` are not security. Do not store secrets in git.
- Do not turn a one-off correction into a global rule.
- Generated legal or compliance text is a draft for professional review, not approval.

## How to start a task

Use the matching slash command when one exists (`/complete-ticket`, `/founder-pivot`, `/diagnose-integration`, and others listed in the capability directory). Sequential work stays on one agent. Use subagents for independent review, verification, or bounded research.
