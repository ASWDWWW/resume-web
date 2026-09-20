# Agent activation and coordination

## Sequential work (one agent)

One agent should run a workflow end-to-end when the steps share context: inspect → implement → verify → handoff. Examples: `/complete-ticket`, `/debug-issue`, `/repair-workspace`, `/founder-pivot`.

Do not start a second coding agent on the same dirty worktree.

## When to use subagents

| Subagent | Use |
| --- | --- |
| independent-reviewer | After a non-trivial diff; parallel with implementation only if the reviewer is readonly on a committed or specified diff |
| verifier | After the implementer claims done |
| security-privacy | Auth, payments, PII, restricted records |
| product-engineering | Bounded implementation when the parent is coordinating |
| business-ops | Bounded ops writing |
| communications-drafter | Bounded drafts |

Specialists are optional. There is no permanent agent per department.

## Manual activation

- User prompt
- Slash command in `.cursor/commands/`
- Explicit “use the X subagent”

## Delegation

Pass a bounded task: goal, repo, identity, files, done-when, and what not to do. The subagent does not inherit chat memory; put facts in the prompt or a file.

## Event and n8n triggers

Cursor hooks gate and log; they must not start new external side effects. n8n is not connected — if you add it later, register the workflow in `ops/automations/CATALOG.md` with trigger, limits, and disable switch.

## Shared records, not shared memory

Write tickets, decisions, handoffs, and control-center updates. The next session reads those files.

## Concurrent coding

Use separate git worktrees or checkouts. Never two writers on one working tree. Default remote remains `ASWDWWW/resume-web`.
