# Forward Deployed Engineer (FDE)

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **8.7 / 10** · **Band:** Strong match  
**How to use this in hiring:** Ready to use this as a flagship example

> This score measures how strongly *this repository* maps to a typical **Forward Deployed Engineer (FDE)** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

FDEs sit with customers, understand a messy operational workflow, and make the product succeed in that environment — often writing glue, configuring, training, and feeding requirements back to product. Palantir-style FDEs are software engineers who deploy.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Forward Deployed Engineer (FDE)

This is an FDE-shaped body of work. You embedded in a real vertical (roadside/truck repair), modeled how the shop actually runs, shipped the system into a live Firebase project, and then productized the *deployment motion* (intake, branding, UAT, training, retainer, hypercare). You are both the engineer and the person who would sit with the office manager.

## Concrete evidence from this project

- Reference deployment for Alex Road Service with production project and public demo.
- Role-based training paths (admin / office / technician).
- Start gates so delivery does not begin unpaid or unscoped.
- Customization model: duplicate platform, apply brand, select modules.
- UAT scripts meant to be run with real staff.

## Gaps versus a typical hiring bar

Classic FDE jobs involve many customer environments, travel, and sometimes classified or highly constrained IT. You have depth on one vertical and one flagship deploy, plus a playbook for the next. Less evidence of navigating hostile enterprise IT (SSO, proxies, air-gap).

## How to talk about this

- Narrative: “I did not toss a SaaS login over the wall — I built the shop’s operating system and the delivery process to install the next one.”
- Show the 10-stage flowchart as your deployment methodology.
- Be ready for “tell me about a time the customer process and the software disagreed.” Use tax/labor, technician vs office permissions, or Stripe-only payments.

## Repo pointers

- `business/docs/POST_SALE_DELIVERY_PLAYBOOK.md`
- `business/docs/DOCUMENT_HANDOFF_FLOW.html`
- `dev/` production app
- `business/Closed Sales/08 100 Percent Review/02-UAT-Script.md`
