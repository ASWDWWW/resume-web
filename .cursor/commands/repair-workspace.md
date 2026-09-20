# Repair this workspace operating system

Inspect before changing anything. Do not revert unfinished `Career/`, `Content/`, or resume-folder work.

Check, in order:

1. Native files exist and are valid: `AGENTS.md`, `.cursor/rules/*.mdc`, `.cursor/commands/*.md`, `.cursor/skills/*/SKILL.md`, `.cursor/agents/*.md`, `.cursor/hooks.json` plus hook scripts.
2. Markdown descriptions are not counted as registered commands or hooks. Recreate missing executable files in the supported locations.
3. Integration inventory vs live verification: GitHub identities, Gmail, Firebase, plugins. Do not silently switch accounts.
4. Control center, project profile, and sources of truth still match the repo.
5. Hooks run on Node and fail open except where they intentionally deny force-push, git config, and pasted live secrets.

Fix what is broken. Leave optional dashboard work optional. Report verified, untested, awaiting access, awaiting a decision, unsupported, and intentionally disabled.
