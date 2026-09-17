# Software Development Engineer II (SDE II)

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **6.8 / 10** · **Band:** Partial match  
**How to use this in hiring:** Use as transferable evidence, not as proof you already do the job

> This score measures how strongly *this repository* maps to a typical **Software Development Engineer II (SDE II)** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

SDE II is expected to own a problem space, design components that other engineers consume, handle ambiguity, and deliver across quarters with measurable operational quality. The coding bar is higher; system design for SDE II is “a service and its failure modes,” not “a website.”

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Software Development Engineer II (SDE II)

You have SDE II-shaped *product* ownership (payments correctness, RBAC, audit, CI) but SDE II-shaped *systems* experience is thinner: one region, one Firebase project, no multi-service orchestration, no real traffic profile. The implementation plan’s NFRs and threat model are the right *thinking*; they are not yet proven under load.

## Concrete evidence from this project

- Idempotent Stripe webhook + refund path with event-id dedupe.
- Employee lifecycle callables: create, reset password, archive, unarchive, delete, role claims.
- Health check that actually reads Firestore, not a static 200.
- Rules unit tests with role fixtures including terminated users.
- Documented RTO/RPO, cost model, and incident severities.

## Gaps versus a typical hiring bar

Typical SDE II design interviews expect queues, caching, sharding, multi-region, and API versioning. You should study those independently. Internally, there is no evidence of influencing other SDEs’ designs.

## How to talk about this

- Frame as “SDE II scope on a small system”: you owned correctness of money and identity, which companies care about more than framework fashion.
- Be explicit: “I have not operated this at Amazon scale; here is how I would evolve counters, indexes, and backups.”
- Use the risk register (key-person dependency, Firebase cost, rule misconfig) as a design-review artifact.

## Repo pointers

- `dev/functions/index.js` Stripe + employee admin
- `dev/tests/security-rules.test.cjs`
- `dev/docs/IMPLEMENTATION_PLAN.md` §10–§14
