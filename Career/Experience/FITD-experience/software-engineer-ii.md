# Software Engineer II / SWE II

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | Mid-level SWE: owns features end-to-end, designs small systems, mentors juniors, ships independently. |

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

SWE II is the first title that expects independent ownership of a problem area. You owned several: mobile clients, Firebase backend, AI features, brand subscriptions, admin CRM, and a cross-platform migration plan (native Android freeze → Expo).

You wrote the engineering handbook, handoff contracts, product schema, and staging notes — the written design work SWE II interviews look for. You also scoped contractor onboarding (Andreea) and internship programs, which is informal mentorship.

---

## How that applies to this title

Map FITD work to SWE II expectations:

- **Feature ownership:** Get FITD, FITD Room, brand plans, catalog import, notifications.
- **System design (small/medium):** Firestore collections, function triggers, App Check, geo sanitization.
- **Cross-stack delivery:** iOS + Functions + rules + analytics for the same feature.
- **Operational judgment:** kill switches on bots, VTO treated as beta, Android freeze vs. rewrite.

That is a mid-level profile, not a junior one.

---

## Gaps (be honest in interviews)

SWE II at a large product org also means working in a shared codebase with CI, on-call, and design review. You have less evidence of collaborative process, automated tests, and high-QPS systems design. Some companies will still slot you SWE II and grow you; others will probe algorithms and distributed systems harder than FITD required.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-App/android/` — Kotlin + Jetpack Compose (~56 files), Hilt, Coil, Ktor
- Play Billing, Play Integrity, Open-Meteo; frozen 2026-09-13 after Expo decision
- `development/apps/fitd-mobile/` — Expo 57 / React Native scaffold, Expo Router, `geminiProxy`
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

- Use the Expo migration as a SWE II story: why freeze Android, what Phase 0–8 covers, what you would not rewrite.
- Design a feature on a whiteboard the way you designed `implicitProductInterest` + `recStats`.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
