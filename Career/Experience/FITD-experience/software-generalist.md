# Software Generalist

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **10 / 10** ●●●●●●●●●● |
| **Match band** | Exceeds the bar |
| **Role in one line** | High-range engineer who can do mobile, web, backend, data, and enough AI/ops to ship. |

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

This title is a description of FITD-Bible. You moved across Swift, Kotlin, TypeScript/React/Next, Node Functions, Python automations, Firestore, and vendor AI without becoming a single-stack specialist.

You also covered the non-code surface: schema, rules, staging, marketing site, CRM, internships, investor docs, ads, brand ops.

---

## How that applies to this title

Software Generalist / “full-stack plus mobile plus AI” roles at startups are the intended audience. You reduce coordination cost because one person can finish a slice.

This is your most accurate non-seniority title.

---

## Gaps (be honest in interviews)

Generalists are sometimes rejected by specialist orgs. The gap is not skill — it is focus. For specialist apps, lead with the matching doc (iOS, GenAI, FDE) and treat generalist as backup narrative.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-App/android/` — Kotlin + Jetpack Compose (~56 files), Hilt, Coil, Ktor
- Play Billing, Play Integrity, Open-Meteo; frozen 2026-09-13 after Expo decision
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- Give a week-in-the-life that touches app, function, catalog, and a brand email — that is the job.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
