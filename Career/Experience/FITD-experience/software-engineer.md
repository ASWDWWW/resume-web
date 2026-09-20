# Software Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | General software engineer who designs, ships, and operates production systems. |

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

You were the engineer of record for a multi-surface product, not a single ticket stream.

You wrote and shipped a production iOS client, a native Android port, a React marketing site, a Next.js admin portal, and a Node 20 Firebase backend. You designed the Firestore data model, security rules, Cloud Functions (virtual try-on, receipt validation, catalog import, social fan-out, scheduled engagement, AI bots), and a staging environment. You also built growth automations and an in-store kiosk scaffold.

That is the full software-engineering loop: product definition, implementation, data modeling, integrations, release, and ongoing operation.

---

## How that applies to this title

A Software Engineer is expected to take ambiguous problems, choose an architecture, write working code, and own quality. FITD is that job at company scale: you chose Firebase as the application platform, split client vs. function responsibilities, integrated third-party AI and billing, and documented the system so others can join.

You can speak to shipping user-facing features (closet, shop, social, subscriptions) and platform work (rules, functions, analytics, staging) in the same breath — the combination most SWE interviews actually test.

---

## Gaps (be honest in interviews)

Typical SWE interviews at large companies also probe algorithms under time pressure, code-review culture on a large team, and CI/CD. This repo shows little automated test/CI infrastructure and no large-team review process. Depth in any one language is high (especially Swift), but the role title is general — you should lead with product impact, then pick the stack the interviewer cares about.

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
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema

---

## Interview talking points

- Walk through the FITD architecture diagram: clients → Firebase → Vertex/Gemini → store billing.
- Pick one hard feature (virtual try-on or catalog import) and explain client vs. function vs. rules.
- Be ready to discuss tradeoffs of a serverless backend vs. a dedicated API server.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
