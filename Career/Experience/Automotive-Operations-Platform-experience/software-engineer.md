# Software Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **8.7 / 10** · **Band:** Strong match  
**How to use this in hiring:** Ready to use this as a flagship example

> This score measures how strongly *this repository* maps to a typical **Software Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

A Software Engineer is hired to design, build, test, and ship working software: product features, data models, integrations, and the operational pieces that keep a system reliable. The bar is ownership of real user-facing and backend work, not a single layer of the stack.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Software Engineer

This project is a complete software-engineering loop, not a tutorial. You specified a domain (shop operations), designed collections and status machines, implemented client and server behavior, enforced access in rules and Cloud Functions, integrated Stripe, wrote tests that run in CI, deployed to Firebase Hosting, and documented go-live and incident handling. That is the job: take an ambiguous business need and leave a running system with constraints (money, roles, audit, backups).

## Concrete evidence from this project

- Shipped a public 11-page marketing site and an authenticated ops platform (customers, trucks, work orders, estimates, invoices, payments, inventory, reports, employees, schedule, messages, leads).
- Wrote ~1,800 lines of Cloud Functions: callable APIs, Firestore triggers, scheduled jobs, Stripe webhook, health check.
- Implemented sequential IDs, optimistic concurrency, immutable payments, and audit logging.
- Added GitHub Actions that install, lint/syntax-check, run rules + functions tests, and deploy production only from `main` after a protected environment.
- Authored the implementation plan, runbook, Firebase/Stripe setup docs, and UAT-oriented business packet.

## Gaps versus a typical hiring bar

Most Software Engineer job descriptions also want a shared team codebase (code review as a reviewer, design docs reviewed by peers), a mainstream application framework at scale, and on-call on a system you did not solely invent. You have depth of ownership and weaker evidence of collaborating inside an existing large org.

## How to talk about this

- Lead with: “I designed and shipped a production shop-management system covering lead → work order → invoice → Stripe payment.”
- Name constraints: RBAC, PCI-aware payments (no card data on the platform), sequential legal invoice numbers, deny-by-default Firestore writes.
- Be ready to walk a work-order completion that decrements inventory in a transaction.

## Repo pointers

- `dev/` — application, functions, rules, tests
- `dev/docs/IMPLEMENTATION_PLAN.md` — architecture, NFRs, RBAC, test plan
- `dev/functions/index.js` — server APIs
- `.github/workflows/deploy.yml` — CI/CD
