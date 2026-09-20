# Backend Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **7.8 / 10** · **Band:** Solid match  
**How to use this in hiring:** Interview-credible with this as a primary story; expect gap questions

> This score measures how strongly *this repository* maps to a typical **Backend Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Backend engineers own APIs, data integrity, jobs, integrations, and authorization. They are judged on correctness under concurrency, failure handling, and keeping secrets and invariants off the client.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Backend Engineer

Your backend is Firebase Cloud Functions (Node 22) plus Firestore transactions and security rules. That is a real backend, not “just a frontend with a database.” Privileged writes are server-side; payments are immutable; counters are transactional; webhooks verify Stripe signatures; staff callables check role *and* active status. That is backend thinking.

## Concrete evidence from this project

- `saveEntity`, `completeWorkOrder`, `adjustInventory`, `createInvoiceFromWorkOrder` as authorized mutations.
- Stripe Checkout + refunds with idempotency keys and `stripe_events`.
- Firestore triggers for invoices, inventory, work orders, estimates, schedule blocks (notifications / derived state).
- Daily scheduled overdue marking and PII-ish contact-submission TTL.
- Admin employee provisioning that sets Auth claims, not a client-editable role field.

## Gaps versus a typical hiring bar

You do not have a traditional HTTP service (Express/FastAPI), relational schema/migrations, message queues, or multi-service RPC. Rules-as-authorization is powerful but company-specific. Expect design questions about SQL, caching, and exactly-once vs at-least-once — you have at-least-once webhook handling with dedupe, which is a good answer.

## How to talk about this

- Open with: “The client cannot write invoices, payments, or counters. Functions are the only writers.”
- Draw the checkout transaction: payment row, invoice paid/balance, event doc, audit log.
- Mention healthCheck reads Firestore so deploy liveness is not a lie.

## Repo pointers

- `dev/functions/index.js`
- `dev/functions/package.json`
- `dev/firestore.rules`
- `dev/tests/functions-smoke.test.cjs`
