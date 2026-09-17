# Application Developer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **9.0 / 10** · **Band:** Strong match  
**How to use this in hiring:** Ready to use this as a flagship example

> This score measures how strongly *this repository* maps to a typical **Application Developer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Application Developers are hired to build business applications: screens, workflows, forms, reports, and integrations that staff use every day. The emphasis is working product over platform infrastructure.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Application Developer

This is the center of the repo. The ops platform is a classic line-of-business application: customers, fleet, jobs, quoting, AR, stock, scheduling, HR-lite employees, and messaging. You also built the public application (marketing + contact). Application-developer interviews want to see you can model a business process in software — you did, including NJ tax notes and payment terms.

## Concrete evidence from this project

- Nine-plus operational modules with list/detail/create/update flows.
- Shop settings for labor rate, tax, prefixes — configuration, not hardcoded shop math.
- Reports with date range and CSV export.
- Schedule calendar with typed blocks overlaid on work orders.
- Employee onboarding checklist fields (I-9, W-4, handbook, PPE).

## Gaps versus a typical hiring bar

Many Application Developer roles use C#/.NET, Java, Salesforce, or a SPA framework. You used vanilla JS + Firebase. Translate features, do not pretend the stack is identical. Enterprise ALM (ADO, ServiceNow) is not in this repo.

## How to talk about this

- Walk the estimate → approve → work order → complete → invoice → Stripe pay path as one application workflow.
- Show a screenshot of dashboard KPIs driven from stored data, not mock widgets.
- Mention localization of the whole app (language switcher) as a real user requirement, not a demo toy.

## Repo pointers

- `dev/public/app/*.html`
- `dev/public/app/js/data-service.js`
- `dev/public/app/js/schedule-service.js`
- `dev/README.md` module table
