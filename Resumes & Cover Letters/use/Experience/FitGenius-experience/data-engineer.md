# Data Engineer

**Experience rating:** 4.6 / 10 — Weak / stretch  
**Application guidance:** Unlikely — only if posting is unusually broad  
**Family:** ML / data  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Data engineers build reliable pipelines into warehouses: ingestion, transformation, orchestration, quality, SLAs. Spark/dbt/Airflow/Kafka are common.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You wrote analytics events from the client, stored an audit trail in Firestore, and rolled up admin analytics in Cloud Functions. Docs mention optional BigQuery export in Console — not a pipeline you coded. No warehouse, no ETL orchestrator.

## How that work applies to **Data Engineer**

Only early-stage 'data' roles that mean 'we need events and a dashboard.' Skip true DE postings.

## Strengths a hiring manager can credit

- Event catalog with dual-write intent (GA4 + Firestore)
- Server-side rollups for an admin UI
- Privacy-aware about what is logged

## Gaps versus a typical hiring bar

- No warehouse modeling
- No batch/stream platform
- No data-quality framework

## How to talk about it

Call it product analytics plumbing, not data engineering.

## Repo evidence

`analyticsService.ts`, `functions/src/adminAnalytics.ts`, `docs/development/ANALYTICS.md`

## Rating rationale

Event logging ≠ data engineering.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
