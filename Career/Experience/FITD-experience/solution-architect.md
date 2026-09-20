# Solution Architect

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **7 / 10** ●●●●●●●○○○ |
| **Match band** | Solid overlap |
| **Role in one line** | Designs the technical shape of a customer or product solution across systems. |

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

You architected the FITD ecosystem: data layer (scraper, catalog), content layer (Firebase, functions), distribution (n8n, stores, web), and a retail kiosk. Handbook architecture + mermaid diagrams + brand schema + kiosk PRD are architect artifacts.

You chose managed Firebase vs. custom servers — an architecture decision with cost and security consequences.

---

## How that applies to this title

Solution Architect roles that are pre-sales or internal architecture for mid-size systems fit your communication style (docs, diagrams, options). You can design a customer’s path: mobile + catalog + VTO + analytics.

Enterprise SA (multi-year programs, compliance architectures) is a bigger jump.

---

## Gaps (be honest in interviews)

No TOGAF-style practice, limited integration architecture (EDI, SSO, data residency). Title “architect” at large vendors implies more years of multi-account design. FITD is one architecture you own completely — strong, but single-context.

---

## Evidence in the repo

- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function
- `development/apps/FITD-Kiosk/` — SwiftUI iPad kiosk, camera capture, VTO display
- Hardware sourcing docs: touchscreen + camera + network device (no custom firmware)
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog

---

## Interview talking points

- Present the ecosystem diagram from the root README as your reference architecture.
- Defend Firebase and the conditions under which you would leave it.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
