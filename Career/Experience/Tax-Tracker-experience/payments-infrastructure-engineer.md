# Payments Infrastructure Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 6.0 / 10  
**Band:** Good  
**Application guidance:** Stretch

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

Payments infra engineers own checkout, ledgers, processors, webhooks, idempotency, reconciliation, and often PCI/tokenization platforms used by the rest of the company.

## What you actually did in this project

Live Stripe products (Standard $9.99/$99.99, Diamond $19.99/$199.99), 7-day trial for first-time customers, webhook signature verification, plan mapping from Price IDs, Customer Portal, and a parallel App Store / Play Billing path (`activateIapEntitlement`) that writes `billingProvider: store` and blocks reused transaction IDs. Two processors (Stripe + Apple/Google), webhook-driven state, trial-once logic, portal for self-serve changes, IAP transaction idempotency collection, plan mapping from price IDs and product IDs. You documented live vs test keys and webhook secrets in OPS.md.

## How that work applies to this title

You implemented a real payments *integration layer*, which is how many companies start. Idempotency and 'never trust the client for entitlement' are payments-infra first principles.

## Gaps (be ready to say these out loud)

Not infrastructure at processor scale: no in-house ledger, no retry/reconciliation jobs, IAP path notes that full App Store Server API / Play Developer API verification is still to be layered on. Dual billing providers without a unified entitlement service abstraction.

## Interview / resume angle

Be precise: 'I built production billing integrations, not a payments platform.' Then show the state machine. That precision gets callbacks; inflation does not.

## Verdict

Good supporting evidence for payments-adjacent SWE. Stretch for a dedicated payments-infra team unless you have more.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
