# Application Developer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **9 / 10** ●●●●●●●●●○ |
| **Match band** | Strong match |
| **Role in one line** | Builds and maintains user-facing applications (mobile, web, or desktop) against existing services. |

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

You shipped multiple applications: the FITD iOS app, Android app, Expo mobile scaffold, marketing website, admin portal, and kiosk iPad app. Each has real user flows — auth, browsing, uploads, payments, CRM, internships — not demos.

Application developers are judged on UI completeness, state management, and integration quality. Closet caching (Kingfisher/Coil limits), lazy tabs, StoreKit/Play Billing, and the admin RBAC portal are that work.

---

## How that applies to this title

This title is a direct label for most of your time: writing application code that talks to Firebase and AI APIs. You can show App Store–oriented release notes (`WHATS_NEW.txt` v2.2+), screenshot sets, and a live marketing site.

If a shop uses “Application Developer” for enterprise internal tools, point at the admin CRM and Instagram CRM — operator applications, not only consumer UI.

---

## Gaps (be honest in interviews)

Some Application Developer jobs are Java/.NET enterprise forms or Salesforce. You do not have that stack. Lead with mobile + React/Next; do not claim ERP/line-of-business platforms you have not used.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-App/android/` — Kotlin + Jetpack Compose (~56 files), Hilt, Coil, Ktor
- Play Billing, Play Integrity, Open-Meteo; frozen 2026-09-13 after Expo decision
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)

---

## Interview talking points

- Demo or screenshot closet, Get FITD, and brand analytics as three different application types.
- Explain shared ClosetDataManager / weather state across tabs.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
