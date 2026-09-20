# Frontend Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **7.6 / 10** · **Band:** Solid match  
**How to use this in hiring:** Interview-credible with this as a primary story; expect gap questions

> This score measures how strongly *this repository* maps to a typical **Frontend Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Frontend engineers own user interface quality: structure, state, accessibility, performance of first paint, and product UX across breakpoints. Strong candidates have a component model and care about empty/error/permission states.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Frontend Engineer

You built two frontends: a marketing site (services, emergency, financing, reviews, contact) and a dense internal app (tables, modals, dashboards, calendars, detail pages). There is a component layer (`components.js`, `app-components.js`), shared CSS, i18n across public + ops, and mobile-conscious work-order flows for technicians. That is substantial frontend product work, even without React.

## Concrete evidence from this project

- Public pages with SEO-ish artifacts (`sitemap.xml`), legal pages, and contact UX.
- Ops chrome: sidebar, role-filtered nav, toasts, KPIs, reports charts.
- Language switcher wrapping the entire product (100+ languages via Google Translate + branded UI).
- Media UI for photos/videos/PDFs on jobs, trucks, invoices, messages.
- Implementation-plan accessibility NFRs (contrast, labels, touch targets) as design intent.

## Gaps versus a typical hiring bar

Frontend hiring is dominated by React/Vue/Svelte, TypeScript, design systems, and frontend test runners (Playwright/Cypress/RTL). This repo’s E2E Playwright plan is documented more than implemented. No Storybook, no CSS methodology beyond custom sheets. Be ready to rebuild a screen in their framework live.

## How to talk about this

- Do not apologize for vanilla JS; explain it as a v1 constraint to ship domain software without a rewrite.
- Show technician vs office vs admin views as a frontend RBAC problem.
- Discuss demo mode as a frontend architecture choice for sales without contaminating prod.

## Repo pointers

- `dev/public/*.html`
- `dev/public/js/components.js`
- `dev/public/js/i18n.js`
- `dev/public/app/css/app.css`
