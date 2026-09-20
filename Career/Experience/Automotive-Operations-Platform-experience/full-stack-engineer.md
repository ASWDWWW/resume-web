# Full-Stack Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **8.8 / 10** · **Band:** Strong match  
**How to use this in hiring:** Ready to use this as a flagship example

> This score measures how strongly *this repository* maps to a typical **Full-Stack Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Full-stack engineers own UI and server/data together: they can ship a feature that needs a screen, an API, a schema change, and auth. The bar is competence on both sides, not world-class specialization in either.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Full-Stack Engineer

This is a full-stack build by construction. Frontend: multi-page HTML/CSS/JS, responsive ops UI, i18n, media uploads. Backend: Cloud Functions, Admin SDK, Stripe, scheduled jobs. Data: Firestore model + indexes. Auth: Firebase Auth + custom claims. Infra-as-product: Hosting headers, storage rules. You repeatedly crossed the boundary (checkout starts in the client, money moves only on the server).

## Concrete evidence from this project

- Client callable wrappers (`payments-stripe.js`) to Functions that hold Stripe secrets.
- Firestore sync + local cache; demo mode for offline sales demos.
- Storage rules that bind file paths to work-order assignment and conversation participation.
- Public site + gated `/app/*` in one hosting site with different cache policies.
- Shared `ARS` namespace modules instead of an SPA framework — still a coherent client architecture.

## Gaps versus a typical hiring bar

Job posts often require React/Next/Node+Postgres or similar. You should be ready to say why Firebase was right for an SMB shop and how you would rebuild the same domain on their stack. SSR, ORMs, and CSS-in-JS are not evidenced.

## How to talk about this

- One story that hits both layers: “Pay invoice” — UI permission check, callable `createStripeCheckout`, Checkout session, webhook, transaction updating invoice + payment + audit.
- One story that is frontend-heavy: schedule grid and role-based nav.
- One story that is backend-heavy: `nextSequentialId` counters.

## Repo pointers

- `dev/public/app/js/payments-stripe.js`
- `dev/functions/index.js`
- `dev/storage.rules`
- `dev/public/css/styles.css` and `dev/public/app/css/app.css`
