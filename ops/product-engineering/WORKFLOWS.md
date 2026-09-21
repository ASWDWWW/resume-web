# Product and engineering workflows

Use `/complete-ticket`, `/debug-issue`, `/review-changes`, `/release`, and skill `engineering-ops`. This repo’s runnable product is the static career site. Other products are other repositories.

## Discovery and requirements

Capture a brief (`ops/templates/brief.md`) with user, problem, constraints, and non-goals. Link evidence. Do not invent clinic, FITD, or shop requirements.

## Prioritization

Update `ops/CONTROL-CENTER.md`. Owner: Zakiy. Superceded items stay in the ticket with status `superseded`.

## UX/UI and Figma handoff

Figma MCP is **verified** (identity `zakiymanigo@gmail.com`). File read and design-to-code are **untested**.

1. Load the Figma design-to-code skill before pulling a node.
2. Name the file and node in the ticket. Use the personal starter team unless a TREI ticket names the Bariatric Associates org (guest view only).
3. Adapt into this repo’s HTML/CSS; do not paste Figma export as a second source of truth.
4. Canva remains valid when the asset already lives there. Magnific is for generation with a budget, not for Figma file sync.

Do not invent a Figma file that was not provided.

## Architecture, frontend, backend, mobile, databases, APIs

Work in the product’s own repo with the routed GitHub identity. For this site: HTML/CSS in `public/` and `css/`. No application database.

## Debugging, testing, accessibility, performance

No package.json test runner here. Verify with file checks, hook JSON tests, and browser tools for UI. Check desktop and mobile viewports if layout changes.

## AI features

If adding AI to a product: write eval cases, a quality check, regression note, and cost note in the ticket. Hugging Face identity `zakiymanigo` is verified; paid inference needs budget.

## PR reviews and releases

Do not commit unless asked. No force-push to main. Career site release = review `public/` then Firebase deploy **only if authorized**. Production dark/staging facts for TREI stay in that product’s docs.

## Migrations, incidents, recovery, debt

Use `ops/templates/incident.md`. Record technical debt in tickets, not as silent rules.

## Environments

| Product | Local | Staging | Production |
| --- | --- | --- | --- |
| Career site | files in this repo | Firebase aliases default/dev both point at `zakiymanigo-career` | same project; billing on (verified 17 Sep 2026) |
| TREI | other repo | Azure staging per packets | production dark per packets |
| FITD | other repo | `fitd-app-staging` | `fitd-app-203cb` |
