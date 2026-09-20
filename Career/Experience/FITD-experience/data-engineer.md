# Data Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **6 / 10** ●●●●●●○○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Pipelines, warehouses, quality, and reliable data movement. |

**Rating scale (this project only):** 10 = you already do the core of this job in production;
8–9 = strong match, hire-ready with normal ramp; 6–7 = real overlap, notable gaps;
4–5 = adjacent experience only; 2–3 = thin transfer; 0–1 = not evidenced here.


---

## Project context

FITD is a fashion AI product you designed, built, and operate: a production iOS app,
a native Android port, an Expo cross-platform scaffold, a marketing site and admin CRM,
Firebase/GCP backend (Auth, Firestore, Storage, Cloud Functions, FCM, Analytics, App Check,
Vertex AI), brand catalog ops (~57 brands / ~16.5k product records), Instagram CRM and
n8n growth automations, AI community bots, and an in-store kiosk concept. This write-up
maps **only work evidenced in FITD-Bible**, not other jobs or coursework.


---

## What you have done in this project

Data movement you built:

- Brand crawl → ~16.5k versioned product JSON → `catalogImport` → Firestore
- Instagram scrape → SQLite → image/outfit analysis scripts
- Client implicit interest → function aggregation → `recStats`
- Web analytics / leads / internships → Functions → Firestore → admin CRM
- IG CRM media in Firebase Storage; n8n outbound social

This is operational data engineering for a startup, mostly JSON/Firestore/SQLite rather than a warehouse.

---

## How that applies to this title

Data Engineer roles at small companies that live on Firebase/GCS will recognize this. You cared about schema (v1/v2 brand product schema), import paths, and operator dashboards.

Warehouse/dbt/Spark roles are a different sport.

---

## Gaps (be honest in interviews)

No Airflow/dbt/Snowflake/BigQuery modeled marts, little data-quality testing, no CDC. Batch JSON and Cloud Functions are the ceiling so far.

---

## Evidence in the repo

- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- Walk a brand from crawl folder → schema → import function → shop UI.
- What you would warehouse first if you hired a DE (events, catalog, subscriptions).

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
