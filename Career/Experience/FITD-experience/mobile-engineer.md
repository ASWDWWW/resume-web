# Mobile Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | Ships iOS and/or Android apps: UI, device APIs, store release, offline-ish clients. |

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

Mobile is the center of FITD.

- **iOS production:** SwiftUI, deep links (`fitd://`, `fitd.app`), camera/gallery closet, Kingfisher cache, WeatherKit, StoreKit 2, FCM, App Check, Associated Domains.
- **Android port:** Compose, Hilt, Coil, Ktor, Play Billing, Play Integrity, App Links — then an explicit freeze in favor of Expo.
- **Expo `fitd-mobile`:** Phase 0 cross-platform replacement with Firebase JS and `geminiProxy`.

You also started an iPad kiosk client. Release notes go through v2.2+ (plans, catalog import, notifications).

---

## How that applies to this title

A Mobile Engineer is hired to own the store binary. You have done that: auth matrix, push, billing, image pipelines, and store-specific services. The Android → Expo decision is a mature mobile-platform story (duplication cost vs. one codebase).

This is among your strongest titles.

---

## Gaps (be honest in interviews)

Less evidence of large-team mobile (modularization, UI tests, feature flags at scale, Play/App Store process with many reviewers). Android depth is weaker than iOS. Offline-first sync is cache-heavy, not a CRDT/sync engine.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-App/android/` — Kotlin + Jetpack Compose (~56 files), Hilt, Coil, Ktor
- Play Billing, Play Integrity, Open-Meteo; frozen 2026-09-13 after Expo decision
- `development/apps/fitd-mobile/` — Expo 57 / React Native scaffold, Expo Router, `geminiProxy`
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x
- Apple receipt validation + App Store Connect subscription status function

---

## Interview talking points

- Compare WeatherKit vs. Open-Meteo vs. planned Expo weather as a platform-abstraction story.
- Explain App Check on both stores and why the Gemini key move matters on mobile.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
