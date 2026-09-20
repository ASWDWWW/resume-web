# iOS Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | Native iOS specialist: Swift/SwiftUI, Apple frameworks, App Store quality. |

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

The production FITD client is iOS-first. Roughly 115 Swift files cover:

- App lifecycle, lazy tabs, shared closet/weather managers
- Auth including Sign in with Apple
- Closet camera/gallery + Gemini labeling
- Shop, community, hashtags, daily styles
- AI stylist + FITD Room (Vertex VTO)
- Brand registration, StoreKit 2 plans, catalog import UI (iOS-only)
- Profiles, posts, FCM inbox, settings / delete account
- WeatherKit + fallback, Kingfisher caches, DeviceCheck, Associated Domains

You also have a separate SwiftUI kiosk target. Architecture and file catalog docs exist specifically for this codebase.

---

## How that applies to this title

This is a straightforward iOS Engineer portfolio. You can discuss SwiftUI architecture, store entitlements, privacy-sensitive camera/location, and Apple-only APIs (WeatherKit, StoreKit, DeviceCheck, Sign in with Apple). Production orientation is documented (App Store, `WHATS_NEW.txt`).

Interviewers who want “someone who has shipped an App Store app they still own” should be an easy narrative.

---

## Gaps (be honest in interviews)

Less UIKit-legacy, Combine-heavy, or modular SPM package architecture than a long-tenured iOS team. Testing (XCTest/UI tests) is not a highlighted strength. You may be asked about concurrency (`async/await`, actors) with more rigor than the repo advertises.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x
- Apple receipt validation + App Store Connect subscription status function
- Gemini 2.0 Flash: closet labeling, brand tagging, AI stylist, daily colors/styles
- Vertex AI `virtual-try-on-001` via Cloud Function proxy
- AI bots: Gemini + Imagen + Veo, kill switch, quotas, moderation, admin approval
- Heuristic `ProductRecommendationEngine` + implicit interest aggregation

---

## Interview talking points

- Tour `FITD_AppApp.swift` → `AuthenticatedView` → `MainTabView` and lazy tab loading.
- StoreKit 2 + `validateAppleReceipt` as the iOS trust story.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
