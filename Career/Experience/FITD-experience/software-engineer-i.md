# Software Engineer I

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **10 / 10** ●●●●●●●●●● |
| **Match band** | Exceeds the bar |
| **Role in one line** | Entry / early-career SWE: ships features with guidance, learns the stack, writes production code. |

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

SWE I work is scoped tickets, mentored PRs, and first production features. You instead owned the entire FITD stack: SwiftUI production app, Android Compose port, web + admin, Cloud Functions, security rules, AI integrations, and brand/catalog operations.

You have already done the work SWE I is hired to start learning — independently.

---

## How that applies to this title

Every SWE I competency maps cleanly: writing application code, using a cloud backend, reading docs, shipping UI, handling auth, and fixing production issues. Your intern-hiring materials and handbook show you can also explain the system to someone at this level.

For this title, FITD is overqualified evidence. Use it to skip junior-screening doubt, then show you can still take direction and work in a team process.

---

## Gaps (be honest in interviews)

The only gap is cultural, not skill: SWE I roles assume you will be mentored. Interviewers may worry a founder will reject narrow tickets. Frame FITD as proof you can finish work, not as a reason you cannot take a smaller scope.

---

## Evidence in the repo

- `development/apps/FITD-App/` — production SwiftUI app (~115 Swift files), App Store
- Auth (email, Google, Apple, anonymous), StoreKit 2, WeatherKit, FCM, App Check / DeviceCheck
- Closet, shop, AI stylist, FITD Room virtual try-on, social feed, brand toolkit
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs

---

## Interview talking points

- Show one end-to-end feature (e.g. closet upload → Gemini label → Firestore → closet grid).
- Emphasize you can work inside someone else’s architecture, not only your own.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
