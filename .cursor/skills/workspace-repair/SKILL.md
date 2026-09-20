---
name: workspace-repair
description: Inspect native Cursor formats and rebuild missing operating-system files without discarding unfinished career work. Use when commands, hooks, rules, or the control center are broken or missing.
disable-model-invocation: true
---

# Workspace repair

Supported locations:

- Rules: `.cursor/rules/*.mdc`
- Commands: `.cursor/commands/*.md` (filename is the slash name)
- Skills: `.cursor/skills/<name>/SKILL.md`
- Subagents: `.cursor/agents/<name>.md`
- Hooks: `.cursor/hooks.json` plus scripts under `.cursor/hooks/`
- Persistent instructions: `AGENTS.md`

A markdown essay in `ops/` is not a registered command or hook.

Preserve `Career/`, `Content/`, `public/`, and unfinished resume deletions. Recreate only OS files. Run hook scripts with sample JSON on Node before calling them verified.
