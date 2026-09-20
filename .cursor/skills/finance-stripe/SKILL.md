---
name: finance-stripe
description: Budget, forecast, invoice, and payment troubleshooting with actuals separated from estimates. Stripe live mode is opt-in. Use for finance reviews and payment issues.
disable-model-invocation: true
---

# Finance and Stripe

Stripe MCP was not in this workspace catalog at setup. If it appears later:

- Default environment: test
- Live changes need the named authority in `ops/business-operations/finance.md`
- Never log PAN, CVC, or full account numbers

Keep files separate:

- `ops/business-operations/finance/actuals.md` (sourced only)
- `ops/business-operations/finance/estimates.md`
- `ops/business-operations/finance/forecasts.md`

Do not send invoices or change subscriptions unless asked.
