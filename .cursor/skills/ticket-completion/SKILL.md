---
name: ticket-completion
description: Complete a product or engineering ticket with acceptance checks, verification, and a written handoff. Use when finishing a ticket or implementing a scoped issue.
disable-model-invocation: true
---

# Ticket completion

Inputs: ticket path or brief. Outputs: implementation, verification notes, handoff.

1. Create or load a ticket from `ops/templates/ticket.md`.
2. Use the GitHub identity from origin (`ASWDWWW` for this workspace). Do not prompt for an account.
3. Implement only in-scope files. Preserve unfinished unrelated work.
4. Verify behavior, not just a screenshot. This repo has no npm test script; use hook tests, file checks, or browser tools for UI.
5. Do not commit unless asked.
6. Write `ops/templates/handoff.md` and update the control center.

Delegate review to `independent-reviewer` when the change is non-trivial.
