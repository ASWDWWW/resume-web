---
name: communications
description: Prepare meeting notes and stakeholder messages with evidence and identity checks. Drafts only unless the user explicitly authorizes sending. Use for Gmail, Zoom, coworker, customer, executive, or investor messages.
disable-model-invocation: true
---

# Communications

Gmail MCP is signed into a FITD Sent mailbox (`fitdadmin@fitdai.com`). Catalog Zoom OAuth stays `needsAuth` (error 4700). Always use `user-zoom-bridge`. Never call catalog Zoom `mcp_auth`. Continue with drafts until Gmail is reconnected to `zakiymanigo@gmail.com` and a send is authorized.

1. Gather evidence and quote sources.
2. Choose audience and the sending identity from `ops/integrations/ROUTING.md`. If two Gmail identities exist, ask.
3. Match examples in `ops/business-operations/communications.md`.
4. Fill `ops/templates/communication-draft.md`.
5. Sending, meeting creation, and recording analysis require available APIs plus explicit authorization.

Never silently switch Gmail accounts after a send failure.
