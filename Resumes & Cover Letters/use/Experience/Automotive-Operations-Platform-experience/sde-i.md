# Software Development Engineer I (SDE I)

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **9.0 / 10** · **Band:** Strong match  
**How to use this in hiring:** Ready to use this as a flagship example

> This score measures how strongly *this repository* maps to a typical **Software Development Engineer I (SDE I)** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

SDE I (Amazon-style and similar) is an early software role focused on delivering features in a service, writing tests, following operational standards, and growing toward independent design. Bar-raisers look for customer obsession, ownership, and working code more than title inflation.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Software Development Engineer I (SDE I)

This project maps cleanly to SDE I: a customer (the shop) with a painful workflow (spreadsheets / phone), a shipped mechanism (ops platform), and operational docs. You thought about invoice legality, NJ tax configuration, technician field use, and a demo path for sales. That is customer-backed engineering, which SDE I interviews reward.

## Concrete evidence from this project

- Domain status machines: work orders, estimates, invoices.
- Role matrix implemented in UI, custom claims, Firestore rules, and callable guards.
- Contact form → Cloud Function with sanitization and persistence.
- Demo sandbox so stakeholders can tour the product without touching production data.
- Go-live checklist covering legal, technical, data, and training.

## Gaps versus a typical hiring bar

SDE I at large companies still uses their stack (Java/Kotlin, internal deployment, tickets in an existing service). You will need to map your Firebase/JS work onto their primitives and pass standard coding interviews. Do not oversell distributed-systems depth.

## How to talk about this

- Use Amazon language carefully: customer = shop staff and fleet accounts; mechanism = Firestore + Functions; results = runnable daily ops without spreadsheets (stated success criterion S1).
- Prepare a deep dive on `completeWorkOrder` / inventory decrement.
- Mention you wrote the plan *and* executed it — SDE I often only executes.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` success criteria S1–S6
- `dev/functions/index.js` (`completeWorkOrder`, `submitContact`)
- `dev/public/app/js/demo-mode.js`
