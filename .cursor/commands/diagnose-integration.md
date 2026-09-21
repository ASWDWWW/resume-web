# Diagnose integrations

Read `ops/integrations/INVENTORY.md` and `ops/integrations/ROUTING.md`.

For each named connection, record purpose, account identity, scope, permissions, environment, dependencies, and verification status. Never record secrets.

Do not remove overlapping personal vs plugin connections. Do not `gh auth switch` to probe the inactive FITD-fash login.

If a plugin is missing from the MCP catalog, mark it **unsupported** here, not installed. Figma, Stripe, n8n, Magnific, and Hostinger were verified present on 20 Sep 2026 — re-check rather than copying that sentence.

Output a status table: verified, untested, awaiting access, awaiting a decision, unsupported, intentionally disabled.
