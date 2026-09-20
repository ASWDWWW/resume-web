# Diagnose integrations

Read `ops/integrations/INVENTORY.md` and `ops/integrations/ROUTING.md`.

For each named connection, record purpose, account identity, scope, permissions, environment, dependencies, and verification status. Never record secrets.

Do not remove overlapping personal vs plugin connections. Do not `gh auth switch` to probe the inactive FITD-fash login.

If a plugin is missing from the MCP catalog (Figma, Stripe at setup), mark it unsupported here, not installed.

Output a status table: verified, untested, awaiting access, awaiting a decision, unsupported, intentionally disabled.
