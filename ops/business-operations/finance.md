# Finance and payments

Command: `/finance-review`. Skill: `finance-stripe`.

## Authority

| Action | Authority |
| --- | --- |
| Edit estimates/forecasts | Owner or delegated agent (draft) |
| Record actuals | Owner with a source (bank, Stripe export, store report) |
| Stripe test changes | Named ticket, test keys only |
| Stripe live changes | Zakiy explicit approval |
| Send invoice / change subscription | Zakiy explicit approval |

Stripe MCP is **unsupported** in this workspace. TREI packets mention Stripe sandbox in that product’s Azure staging — operate it there, not here.

## File split

- [actuals.md](finance/actuals.md)
- [estimates.md](finance/estimates.md)
- [forecasts.md](finance/forecasts.md)

Never copy a forecast into actuals.

## Cash flow, reconciliation, troubleshooting

Use scenarios in forecasts. Reconciliation prep = match sourced actuals to invoices. Payment troubleshooting: evidence first, no PAN/CVC in git or logs.

## Costs known

Firebase billing **enabled** on `zakiymanigo-career` (verified 17 September 2026). Spend **unresolved** (no invoices in-repo). Other cloud costs **unresolved**.
