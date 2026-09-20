# Forward Deployed Engineer / Solution Architect

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | Hybrid: deploys in the field and owns the reference architecture the customer will live on. |

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

You combined FDE execution (brands, kiosk, CRM) with SA artifacts (ecosystem diagram, Firestore architecture, kiosk PRD, schema). The same person wrote the system and installed it into GTM motions.

That hybrid is exactly this slash title.

---

## How that applies to this title

Vendors who have not split SE vs. FDE vs. SA will hire this. You can draw the target architecture *and* import the customer’s catalog the same week.

Use the architecture handbook as the SA half and the 57-brand pipeline as the FDE half.

---

## Gaps (be honest in interviews)

Enterprise integration patterns still thin. Hybrid roles at big vendors may still want prior customer logos.

---

## Evidence in the repo

- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding

---

## Interview talking points

- One slide: current FITD reference architecture; one slide: what changes for a retailer with their own PIM.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
