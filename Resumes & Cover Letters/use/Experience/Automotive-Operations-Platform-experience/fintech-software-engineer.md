# Fintech Software Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **6.3 / 10** · **Band:** Partial match  
**How to use this in hiring:** Use as transferable evidence, not as proof you already do the job

> This score measures how strongly *this repository* maps to a typical **Fintech Software Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Fintech engineers work in regulated money products: ledgers, payments, KYC, reconciliation, and auditability. They obsess over correctness and compliance.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Fintech Software Engineer

You built a small financial system: invoices, partial payments, credits, write-offs, refunds, sequential invoice numbers, immutable payment log, Stripe as processor, NJ tax configuration, 7-year retention. That is fintech-*adjacent* inside a vertical SaaS app, not a bank or card network.

## Concrete evidence from this project

- PCI approach: SAQ A, Checkout only, no PAN/CVV stored.
- Webhook-recorded payments; staff cannot type a card payment into the app.
- Refunds with Stripe refund ids and invoice balance adjustments.
- Accountant-facing tax notes (parts taxable, labor often not in NJ).

## Gaps versus a typical hiring bar

No double-entry ledger, no KYC/AML, no card issuing, no money-movement licensing. Fintech firms will probe that. Stronger for “fintech features inside a product” than “Fintech Software Engineer” at Stripe/Plaid/a bank.

## How to talk about this

- Story: “I treated invoices as legal artifacts and payments as append-only.”
- Be precise: you integrated Stripe; you did not build a payment network.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §8.3, §11
- `dev/docs/STRIPE_SETUP.md`
- `dev/functions/index.js` (`createStripeCheckout`, `stripeWebhook`, `createStripeRefund`)
- `dev/public/app/js/payments-stripe.js`
