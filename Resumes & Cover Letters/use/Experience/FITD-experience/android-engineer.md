# Android Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **6 / 10** ●●●●●●○○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Native Android specialist: Kotlin, Jetpack, Play quality. |

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

You built a real native Android port: Kotlin, Jetpack Compose, Hilt DI, Coil (parity cache sizes), Ktor weather, Play Billing 7.x, Play Integrity App Check, Firebase, App Links. Consumer journeys were taken to documented parity with iOS; VTO is partial; catalog import and Apple Sign-In were intentionally omitted.

You then froze the Android tree (2026-09-13) and started Expo as the long-term shared client. That is an engineering decision, not abandonment of Android users.

---

## How that applies to this title

You can interview for Android roles that want Compose + Firebase + Play Billing. You have implemented the modern Android stack, not only a WebView wrapper. Parity notes in `README-android.md` show you thought like an Android owner (platform substitutions, not pixel-identical copies).

For a generalist mobile role this is enough. For a dedicated Android Engineer seat, treat it as a strong project, not a multi-year Android career.

---

## Gaps (be honest in interviews)

The tree is frozen; Expo is the future. Less evidence of Play Console process depth, WorkManager, Room, navigation-component at scale, or Android-specific performance work. Interviewers will notice iOS is the source of truth. Do not oversell Android seniority.

---

## Evidence in the repo

- `development/apps/FITD-App/android/` — Kotlin + Jetpack Compose (~56 files), Hilt, Coil, Ktor
- Play Billing, Play Integrity, Open-Meteo; frozen 2026-09-13 after Expo decision
- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/fitd-mobile/` — Expo 57 / React Native scaffold, Expo Router, `geminiProxy`
- StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x
- Apple receipt validation + App Store Connect subscription status function

---

## Interview talking points

- Explain each iOS→Android substitution: WeatherKit→Open-Meteo, StoreKit→Play Billing, DeviceCheck→Play Integrity.
- Be honest about freeze + Expo and what you would still hotfix natively.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
