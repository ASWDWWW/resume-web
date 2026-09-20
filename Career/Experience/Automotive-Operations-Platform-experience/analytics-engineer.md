# Analytics Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **4.1 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Analytics Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Analytics engineers sit between data engineering and BI: modeled marts, tested metrics, and self-serve dashboards (often dbt + a warehouse).

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Analytics Engineer

You implemented in-app analytics: dashboard KPIs (open WOs, MTD revenue, AR, low stock), reports with date filters, tech performance, and CSV. Metrics live in the application, not a semantic layer. That is “embedded analytics,” adjacent but not the modern analytics-engineer stack.

## Concrete evidence from this project

- Live KPIs from stored operational data.
- Reports module with range filters and export.
- Financial status derived fields (overdue, partially paid, written off).

## Gaps versus a typical hiring bar

No dbt, Looker/Hex/Mode, metric tests, or dimensional modeling documentation beyond app collections.

## How to talk about this

- “I defined and implemented operational metrics in the product.” Useful for product-analytics hybrid roles; thin for a dbt-centric Analytics Engineer seat.

## Repo pointers

- `dev/public/app/dashboard.html`
- `dev/public/app/reports.html`
- `dev/docs/IMPLEMENTATION_PLAN.md` Epic E8
