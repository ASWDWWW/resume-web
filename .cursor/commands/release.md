# Prepare a release

Use `ops/product-engineering/WORKFLOWS.md` release section.

1. Confirm product, repo owner (`ASWDWWW` vs `FITD-fash`), environment (local / staging / production), and rollback owner.
2. List commits, tickets, migrations, and feature flags in this release.
3. Run the project’s real test and build commands. Do not invent a stack this repo does not have.
4. For this career site, the app is static Firebase hosting from `public/`. Do not deploy unless the user asked.
5. Write release notes, monitoring checks, and a rollback note.
6. Mark AI features with eval status and cost notes when relevant.

Stop before production deploy unless authorization is explicit.
