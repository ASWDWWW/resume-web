# Finance review

Read `ops/business-operations/finance.md`. Keep actuals, estimates, and forecasts in separate files.

1. Do not present a forecast as cash in the bank.
2. Stripe: default to **test**. Live mode needs named authority in `ops/business-operations/finance.md`. Do not silently switch Stripe accounts.
3. Prepare reconciliation and invoice drafts. Do not send invoices or change subscriptions unless asked.
4. Payment troubleshooting: gather evidence, stay in test unless authorized, never log full card data.
5. Update control-center finance only with sourced figures.

If numbers are unknown, say so and list what access is missing.
