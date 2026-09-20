# Data Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **3.3 / 10** · **Band:** Weak match  
**How to use this in hiring:** Thin overlap — mention only if asked, then pivot

> This score measures how strongly *this repository* maps to a typical **Data Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Data engineers build reliable pipelines: ingest, transform, warehouse, orchestration, and data quality.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Data Engineer

You designed an operational data model (collections, standard audit fields, soft deletes, counters) and exports (CSV reports, reorder lists). That is OLTP modeling, not a data platform. Seed scripts generate realistic financial data for demos.

## Concrete evidence from this project

- Firestore collections for customers, trucks, WOs, estimates, invoices, payments, inventory transactions, audit log, leads.
- Indexes file for query shapes.
- CSV export of operational/financial reports.
- Retention table (invoices 7 years, leads 2 years) as a data-governance sketch.

## Gaps versus a typical hiring bar

No ETL/ELT, no warehouse (BigQuery/Snowflake), no dbt, no Airflow, no CDC. Weak match except for “can model operational data.”

## How to talk about this

- Describe yourself as having designed the source-of-truth operational schema a data team would later warehouse.
- Do not claim pipeline ownership.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` §4 Data Model
- `dev/firestore.indexes.json`
- `dev/scripts/seed-realistic-invoices.cjs`
