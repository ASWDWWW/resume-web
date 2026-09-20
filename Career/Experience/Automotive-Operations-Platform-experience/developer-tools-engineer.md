# Developer Tools Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **3.4 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Developer Tools Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Developer Tools engineers build compilers, CLIs, editors, debuggers, or internal productivity tools used by other developers.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Developer Tools Engineer

You wrote small tools in service of the product: JS syntax checker, seed payload generators, screenshot capture, flyer capture scripts. That is scripting, not a tools product.

## Concrete evidence from this project

- Node test + emulator orchestration via npm scripts.
- `generate-full-demo-seed.cjs` / `generate-seed-payloads.cjs` / `seed-realistic-invoices.cjs`.
- `page-screenshots/capture-pages.cjs` and marketing flyer capture.

## Gaps versus a typical hiring bar

No CLI used by others, no editor extensions, no build system work. Minimal overlap.

## How to talk about this

- Describe these as product-supporting scripts, not developer-tools experience.

## Repo pointers

- `dev/scripts/`
- `dev/page-screenshots/capture-pages.cjs`
- `business/marketing/tmp-flyer-shots/`
