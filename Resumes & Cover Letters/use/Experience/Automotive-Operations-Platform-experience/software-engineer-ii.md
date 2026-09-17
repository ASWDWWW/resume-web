# Software Engineer II / SWE II

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **7.3 / 10** · **Band:** Solid match  
**How to use this in hiring:** Interview-credible with this as a primary story; expect gap questions

> This score measures how strongly *this repository* maps to a typical **Software Engineer II / SWE II** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

SWE II is hired to own moderately complex systems with incomplete requirements, make design tradeoffs, raise the quality bar (tests, observability, security), and execute with less supervision. Many companies expect 2–4 years and evidence of production incidents, not just feature delivery.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Software Engineer II / SWE II

Several SWE II signals are present: you chose vanilla JS vs rewrite, server-side writes vs client Firestore writes, Stripe Checkout vs storing cards, sequential counters in transactions, and deny-by-default rules. You wrote a threat model, NFRs, CI gates, and a runbook. That is mid-level ownership. The missing SWE II signal is operating this under load with a team, reviewing others’ designs, and surviving production incidents that were not hypothetical.

## Concrete evidence from this project

- Architecture decision table: hosting, Auth, Firestore, Functions, Storage, Stripe, App Check plan.
- Optimistic locking on entities; Stripe event idempotency via `stripe_events`.
- Security headers (CSP, HSTS, Permissions-Policy) in Firebase Hosting config.
- Scheduled jobs: overdue invoices, expired contact-submission cleanup.
- Production deploy gated on `npm run check` and GitHub `production` environment approval.

## Gaps versus a typical hiring bar

SWE II loops often include: designing against an existing service graph, mentoring SE I, SLOs with real traffic, and a typed/framework codebase. This is a single Firebase project with you as bus-factor-1 (you even recorded that as risk R3). Treat SWE II as a stretch you can argue, not a default level.

## How to talk about this

- Tell the “client must not write financial records” story: rules `allow write: if false` on invoices/payments; Functions own mutations.
- Discuss the tradeoff of vanilla JS for v1 vs a framework rewrite.
- If they ask “what would you do at 10× shops?”: indexes, pagination, PITR, cost alerts — you already wrote those as risks.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §3, §7, §8, §14
- `dev/firestore.rules`
- `dev/firebase.json` headers
- `.github/workflows/deploy.yml`
