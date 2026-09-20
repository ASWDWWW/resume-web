# Complete a ticket

Follow `ops/product-engineering/WORKFLOWS.md` and the ticket template.

1. Load the ticket from `ops/product-engineering/tickets/` or the path the user gave. If none exists, create one from `ops/templates/ticket.md` without inventing requirements.
2. Confirm owner, repo, GitHub identity, and authorization.
3. Implement the smallest change that satisfies acceptance checks.
4. Preserve unrelated unfinished work.
5. Verify on the surfaces that share the changed state. For UI, use the browser tools when available.
6. Do not open a PR or commit unless the user asked.
7. Write the handoff using `ops/templates/handoff.md` and update `ops/CONTROL-CENTER.md`.

If blocked, record the blocker in the ticket and continue with independent work that does not need that integration.
