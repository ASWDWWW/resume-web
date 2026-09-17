# Staff Forward Deployed Engineer

| | |
|---|---|
| **Experience rating (FITD-Bible)** | **5 / 10** ●●●●●○○○○○ |
| **Match band** | Adjacent |
| **Role in one line** | Sets FDE technical direction across many deployments; unblocks seniors; shapes the product. |

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

Staff FDE is a leverage role: patterns, reusable accelerators, hiring, multi-region delivery. You created reusable artifacts (schema, handbook, import path, bot platform) that *would* scale deployments — but you have not operated at staff scope (many seniors, many accounts).

Founder leverage is real; Staff title at a large FDE shop is a different social technology.

---

## How that applies to this title

Your platform-ish artifacts (catalog schema, functions, admin) are what a Staff FDE builds so others deploy faster. Use them as evidence of staff *instincts*.

Do not claim you have already performed Staff FDE in an org.

---

## Gaps (be honest in interviews)

No org-level FDE leadership, no cross-account reliability program. Applying Staff as a first FDE job will bounce at most firms; Senior or Founding is the better ask.

---

## Evidence in the repo

- `development/docs/handbook/` — architecture, handoff, staging, cross-platform plan, file catalog
- Cursor rules, bot runbook, brand product schema
- `business/brands/next-uploads/` — ~16.5k product JSON, schema v2, `catalogImport` function
- IG scraper + SQLite training pipeline; web analytics ingest → CRM rollups
- `development/docs/handbook/ANALYTICS-TRACKING.md` event catalog
- `development/apps/FITD-App/index.js` — Node 20 Cloud Functions (VTO, receipts, catalog, social, geo, bots)
- `firestore.rules` / `storage.rules`, staging project `fitd-app-staging`
- `geminiProxy.js`, `validateAppleReceipt`, `virtualTryOn`, implicit-interest ranking function

---

## Interview talking points

- Pitch the catalog schema + import function as an accelerator you would give every FDE.

---

*Part of [job-title experience mapping](README.md). Ratings use only work in FITD-Bible.*
