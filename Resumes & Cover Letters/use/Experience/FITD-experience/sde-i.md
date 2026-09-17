# Software Development Engineer I (SDE I)

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **10 / 10** ●●●●●●●●●● |
| **Match band** | Exceeds the bar |
| **Role in one line** | Amazon-style new-grad / early SDE: writes production code, learns operational bar, delivers with a mentor. |

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

SDE I is scoped implementation on an existing service. You built FITD’s services and clients yourself: Cloud Functions, Firestore rules, iOS/Android apps, and web. You operated staging vs. production Firebase projects and store billing.

That is above the SDE I delivery bar. The Amazon-flavored title adds an expectation that you can follow a well-specified design and write maintainable code — your handbook and schema docs show you can specify as well as implement.

---

## How that applies to this title

Translate FITD into SDE language: you owned a customer-facing application on a managed AWS-like platform (GCP/Firebase), wrote backend functions with explicit IAM-style access (security rules + admin claims), and integrated external APIs (Gemini, Vertex, WeatherKit, App Store).

Leadership principles you can evidence: Ownership (whole product), Bias for Action (ship VTO as beta), Dive Deep (catalog schema, geo sanitize), Invent and Simplify (Firebase instead of a custom server).

---

## Gaps (be honest in interviews)

Amazon SDE I interviews still require data structures and coding under time. This repo does not prove leetcode fluency. Operational excellence (alarms, tickets, weekly metrics reviews) is lighter than a typical AWS team. Do not claim Amazon-scale distributed systems experience.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Firestore/Storage security rules, admin custom claims, App Check
- Function secrets (`GEMINI_API_KEY`), geo sanitization, bot kill switch / audit log
- StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x
- Apple receipt validation + App Store Connect subscription status function

---

## Interview talking points

- Describe `validateAppleReceipt` as a trust-boundary function: why it cannot live only on device.
- Walk security rules as your authorization service.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
