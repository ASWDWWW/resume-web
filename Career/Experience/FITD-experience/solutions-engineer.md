# Solutions Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **8 / 10** ●●●●●●●●○○ |
| **Match band** | Strong match |
| **Role in one line** | Technical counterpart to sales/CS: demos, integrations, customer-specific solutions. |

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

You onboard brands as if you were the SE: catalog extraction for 57 brands, import tooling, outreach emails, subscription packaging, in-app brand analytics. You designed a store kiosk for retail partners. You built CRM, internship, and investor-facing materials so a non-engineer can understand the product.

That is solutions work performed by the person who also wrote the product.

---

## How that applies to this title

Solutions Engineer interviews test: can you discover a customer problem, map it to the product, and fill gaps with configuration or light custom work? Catalog import, geo-targeted ads, and kiosk are those gaps.

You can demo FITD live and speak business (Starter/Growth/Pro) plus implementation.

---

## Gaps (be honest in interviews)

Less multi-customer enterprise integration (SSO, procurement, sandboxes, SOWs). You were solving FITD’s go-to-market, not staffing a SE team. Still a strong founder-SE profile.

---

## Evidence in the repo

- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- Firestore scripts (seed, admin claims, brand emails, geo, VTO presets)
- Instagram CRM (Flask + SQLite + GPT-4o), n8n social posting workflows
- Internship funnel, lead capture, investor/client overview, contractor onboarding
- `development/apps/react-fitd-website/` — React 19 + Vite + Tailwind marketing site (`fitdai.com`)
- `admin-portal/` — Next.js 14 CRM, RBAC claims, internship review, bot admin, prompt packs
- StoreKit 2 brand plans (Starter / Growth / Pro) and Play Billing 7.x
- Apple receipt validation + App Store Connect subscription status function

---

## Interview talking points

- A brand discovery call: their catalog → your schema → import → spotlight → analytics.
- Kiosk as a solution for stores that will not live only in a phone app.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
