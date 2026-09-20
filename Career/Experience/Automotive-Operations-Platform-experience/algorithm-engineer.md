# Algorithm Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **2.6 / 10** · **Band:** Minimal / not a fit  
**How to use this in hiring:** Do not claim this project as experience for this title

> This score measures how strongly *this repository* maps to a typical **Algorithm Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Algorithm engineers design computationally non-trivial methods: optimization, geometry, ranking, signal processing — with complexity and correctness proofs or rigorous evaluation.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Algorithm Engineer

You implemented business algorithms: tax/labor/markup math, sequential IDs, PM-due detection, overdue detection, calendar range math, VIN normalization. These are important and must be correct, but they are not algorithm-engineering as hiring managers mean it.

## Concrete evidence from this project

- Labor/parts/tax totals with shop settings and emergency multiplier (specified).
- Optimistic concurrency version checks.
- Schedule month-grid padding to weeks.

## Gaps versus a typical hiring bar

No numerical methods, no optimization, no published algorithmic novelty.

## How to talk about this

- Talk about correctness of money math, not “algorithms research.”

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §11.5 labor/markup
- `dev/public/app/js/utils.js`
- `dev/public/app/js/schedule-service.js`
