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

Stripe MCP is **verified** (account list). Default mode: **test**. Live writes need Zakiy’s named approval in the ticket.

Visible accounts (names only): Fleet Trucking Platform, TaxTracker Pro, Zakiy T. Manigo. Which account this OS may use is **awaiting a decision**. TREI packets also mention a Stripe sandbox in that product’s Azure staging — operate it there unless a ticket names one of the MCP accounts.

## File split

- [actuals.md](finance/actuals.md)
- [estimates.md](finance/estimates.md)
- [forecasts.md](finance/forecasts.md)

Never copy a forecast into actuals.

## Cash flow, reconciliation, troubleshooting

Use scenarios in forecasts. Reconciliation prep = match sourced actuals to invoices. Payment troubleshooting: evidence first, no PAN/CVC in git or logs.

## Costs known

Firebase billing **enabled** on `zakiymanigo-career` (verified 17 September 2026). Spend **unresolved** (no invoices in-repo).

Hostinger billing list 20 Sep 2026: `.CLOUD Domain` next bill 13 Dec 2026; `KVM 2` next bill 23 Feb 2028. API `total_price` values were recorded as-is in actuals (unit not confirmed in hPanel). Other cloud costs **unresolved**.
