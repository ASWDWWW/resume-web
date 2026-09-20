# Full-Stack Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | Owns UI through data and deploy: client, API, database, and enough infra to ship. |

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

You are the full stack for FITD.

**Client:** SwiftUI, Jetpack Compose, React 19/Vite, Next.js 14, Expo Router.  
**API / server:** Firebase Cloud Functions (Node 20) — HTTPS and Firestore triggers.  
**Data:** Firestore collections, Storage, SQLite in automations, ~16.5k catalog JSON.  
**Auth / access:** Firebase Auth, custom claims, security rules, App Check.  
**Deploy:** Firebase Hosting (`fitdai.com`), Functions, staging vs. production projects.

Features routinely cross the stack: internship apply (web form → function → Storage → admin review), VTO (iOS → function → Vertex → Storage → UI), brand subscribe (StoreKit → receipt function → entitlements).

---

## How that applies to this title

Full-stack interviews ask you to build a slice. You have many slices already in production. You can discuss SSR rewrites for the admin portal on Firebase Hosting, client-vs-server Gemini calls, and why rules are your authorization layer instead of a custom API gateway.

This is one of your two or three strongest title fits.

---

## Gaps (be honest in interviews)

Classic full-stack (Postgres + REST/GraphQL + React on AWS/Vercel with CI) differs in flavor. You have not built a standalone Express/Django API with migrations, or a heavily tested monorepo pipeline. Translate Firebase confidently; do not pretend it is identical to a Kubernetes + RDS shop.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- Firestore/Storage security rules, admin custom claims, App Check
- Function secrets (`GEMINI_API_KEY`), geo sanitization, bot kill switch / audit log

---

## Interview talking points

- Draw the internship or VTO slice on a whiteboard, every hop.
- Explain when you moved Gemini behind `geminiProxy` and why that is a full-stack security change.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
