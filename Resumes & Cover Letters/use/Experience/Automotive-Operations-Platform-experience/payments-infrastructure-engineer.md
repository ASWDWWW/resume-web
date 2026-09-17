# Payments Infrastructure Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **5.8 / 10** · **Band:** Partial match  
**How to use this in hiring:** Use as transferable evidence, not as proof you already do the job

> This score measures how strongly *this repository* maps to a typical **Payments Infrastructure Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Payments infrastructure engineers build or operate the rails: processors, webhooks at scale, idempotency, retries, reconciliation, and sometimes tokenization platforms.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Payments Infrastructure Engineer

You implemented a correct *application* payments layer on Stripe: Checkout session creation, signature-verified webhook, event dedupe, payment intent IDs, refunds, and invoice state machine. That is the client-of-Stripe pattern done seriously. It is not building Stripe-like infrastructure.

## Concrete evidence from this project

- Idempotent `checkout.session.completed` handling.
- `paymentIntentId` / session id stored; no card data.
- Partial pay and refund accounting on the invoice.
- Test-card documentation and payment-success page.

## Gaps versus a typical hiring bar

No multi-processor abstraction, no ledger service, no high-TPS webhook workers, no settlement files. Partial match.

## How to talk about this

- Excellent supporting example for a payments *product* team; stretch for a payments *infrastructure* team.
- Deep-dive the transaction that writes payment + invoice + stripe_events + audit together.

## Repo pointers

- `dev/functions/index.js` `recordStripePayment`, `applyStripeRefund`, `stripeWebhook`
- `dev/Development Docs/STRIPE_PAYMENTS_SETUP.md`
