# Software Development Engineer II (SDE II)

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | Amazon mid-level SDE: designs components, delivers independently, raises the operational bar. |

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

You designed multi-component systems: mobile clients + Cloud Functions + Firestore + Vertex + store billing. You introduced a Gemini proxy so keys leave the client, built bot orchestration with quotas and kill switches, and planned a cross-platform rewrite.

SDE II is “I can take a fuzzy problem and return a design plus working software.” FITD Room, catalog import, brand geo-targeting, and the admin CRM are that shape of work.

---

## How that applies to this title

SDE II loops you already ran:

- Write a design (handbook architecture, brand schema, kiosk PRD).
- Implement across client and service.
- Handle failure modes (VTO beta, OpenWeather fallback, bot moderation).
- Instrument (Firebase Analytics event catalog, CRM growth charts).

You can interview as someone who has been the tech lead of a small product, which is how many SDE IIs actually spend their time.

---

## Gaps (be honest in interviews)

Amazon SDE II bar includes stronger CS fundamentals, code quality at team scale, and often on-call for a high-availability service. FITD’s backend is serverless and low-ops; you have not run large fleets, queues at scale, or formal design reviews. Staffing-wise you are closer to “strong SDE II / early Senior” on product delivery, weaker on Amazon-native infra.

---

## Evidence in the repo

- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation
- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- Firestore/Storage security rules, admin custom claims, App Check
- Function secrets (`GEMINI_API_KEY`), geo sanitization, bot kill switch / audit log

---

## Interview talking points

- System-design the virtual-try-on path: photo upload, function auth, Vertex call, result storage, client display.
- Discuss what you would add for SDE II-quality ops: structured logs, SLOs, replay, CI.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
