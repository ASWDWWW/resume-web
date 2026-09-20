# Platform Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **4.8 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Platform Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Platform engineers build internal paved roads: CI templates, compute/runtime, identity, golden paths, and self-service so many product teams ship faster. The customer is other engineers.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Platform Engineer

You built a *product* platform for shops, and a small engineering platform for yourself: npm scripts (`check`, emulator tests, deploy), GitHub Actions, Firebase project conventions, seed scripts, and a duplicate-and-customize delivery model. That is “platform” in the product sense and a starter internal platform, not Kubernetes/backstage/IDP work.

## Concrete evidence from this project

- Single `npm run check` gate: syntax, regression tests, rules tests, functions tests, npm audit.
- Firebase emulators for Auth/Functions/Firestore/Storage.
- Seed and demo-data generators for realistic invoices.
- Documented environments: local emulators vs production `launchpage-alex-roadservice`.

## Gaps versus a typical hiring bar

No multi-tenant control plane, no service catalog, no Terraform modules used by other teams, no cluster autoscaling. Titles named Platform Engineer at mid/large companies will not treat this as equivalent experience.

## How to talk about this

- Clarify language: “I built an industry platform for repair shops, and lightweight CI/CD for that product — not an internal developer platform.”
- The duplicate-instance LaunchPage model is the closest platform-product story.

## Repo pointers

- `dev/package.json` scripts
- `.github/workflows/deploy.yml`
- `dev/scripts/`
- `business/docs/POST_SALE_DELIVERY_PLAYBOOK.md` (duplicate reference platform)
