# Software Engineer I

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **9.2 / 10** · **Band:** Strong match  
**How to use this in hiring:** Ready to use this as a flagship example

> This score measures how strongly *this repository* maps to a typical **Software Engineer I** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

SE I (new-grad through early-career) is hired to implement well-scoped features, learn the codebase, write tests, and ship with guidance. Strong SE I candidates still show they can take a feature from ticket to production without being blocked on every decision.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Software Engineer I

For SE I, this project over-indexes. You did not only implement tickets — you created the tickets, the architecture, and the production path. Hiring managers looking for SE I want proof you can write real CRUD, auth, forms, and APIs. You have that across many modules, plus security rules and payments, which many SE I candidates never touch.

## Concrete evidence from this project

- Full CRUD modules with validation, search, detail pages, and role-gated UI.
- Firebase Auth session bootstrap, custom claims, inactive-account lockout.
- Client data service plus server `saveEntity` path so writes are authorized, not trusted from the browser.
- Unit-adjacent smoke tests for health check, auth rejection, and optimistic concurrency.
- Local emulator workflow and documented staff login / demo sandbox.

## Gaps versus a typical hiring bar

SE I interviews still probe data structures, debugging, and working inside someone else’s abstractions. This repo is vanilla JS + Firebase, so you should practice framework-specific questions (React state, REST/GraphQL) separately. Also practice receiving critique: there is no PR review history from other engineers.

## How to talk about this

- Position as: “end-to-end product I owned as SE I+ scope, not a class assignment.”
- Walk one user story from `IMPLEMENTATION_PLAN.md` (Given/When/Then) to the code that implements it.
- If they worry you only work solo: describe how the closed-sales packet and UAT scripts exist so *non-engineers* can validate the same system.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §6 user stories
- `dev/public/app/js/data-service.js`
- `dev/public/app/js/auth.js`
- `dev/tests/functions-smoke.test.cjs`
