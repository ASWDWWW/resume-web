# Backend Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **7 / 10** ●●●●●●●○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Designs services, data models, APIs, and server-side reliability. |

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

Your backend is Firebase, not a custom microservice fleet. You still did backend work:

- 20+ Cloud Functions: `virtualTryOn`, `geminiProxy`, `validateAppleReceipt`, `catalogImport`, social push triggers, scheduled engagement, geo sanitizers, implicit-interest aggregation, bot scheduler/admin.
- Firestore schema for users, closet, posts, brands, ads, recs, CRM, bots.
- ~477-line `firestore.rules` and Storage rules as the authorization service.
- Website functions: analytics ingest, leads, internship upload, subscription validation.
- Secrets, staging project, seed/admin scripts.

That is real server-side product engineering.

---

## How that applies to this title

Backend Engineer interviews care about trust boundaries, idempotency, and data integrity. Your bot stack (idempotency, quotas, kill switch) and receipt validation are the best stories. Catalog import and geo sanitization show you do not blindly trust clients.

You can do the job at a startup or Firebase-heavy shop immediately. At a service-oriented backend team you would ramp on their language, queues, and datastore.

---

## Gaps (be honest in interviews)

Missing typical backend depth: no independently scaled services, little queue/stream processing, no SQL schema migrations, limited load testing, no formal API versioning. Node Functions are a backend, but interviewers who want Java/Go + Postgres + Kafka will see a gap. Rate yourself honest: strong applied backend, not a specialist.

---

## Evidence in the repo

- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Firestore/Storage security rules, admin custom claims, App Check
- Function secrets (`GEMINI_API_KEY`), geo sanitization, bot kill switch / audit log
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x
- Apple receipt validation + App Store Connect subscription status function
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog

---

## Interview talking points

- Why Vertex try-on and Apple receipts must be server-side.
- How `onImplicitProductInterestWrite` aggregates client signals without a custom worker fleet.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
